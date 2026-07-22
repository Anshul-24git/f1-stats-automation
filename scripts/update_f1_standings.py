import os
import json
import requests
import datetime
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import re

BASE_URL = 'https://api.jolpi.ca/ergast/f1'
TIMEOUT = 30

def get_session():
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def fetch_data(url):
    session = get_session()
    response = session.get(url, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()

def fetch_standings(kind):
    try:
        url = f"{BASE_URL}/current/{kind}Standings.json"
        data = fetch_data(url)
        standings_list = data.get('MRData', {}).get('StandingsTable', {}).get('StandingsLists', [])
        if standings_list:
            return standings_list[0]
        return None
    except Exception as e:
        print(f"Error fetching {kind} standings: {e}")
        return None

def fetch_race(which):
    try:
        url = f"{BASE_URL}/current/{which}.json"
        data = fetch_data(url)
        races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])
        if races:
            return races[0]
        return None
    except Exception as e:
        print(f"Error fetching {which} race: {e}")
        return None

def fetch_last_race_results():
    try:
        url = f"{BASE_URL}/current/last/results.json"
        data = fetch_data(url)
        races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])
        if races:
            return races[0]
        return None
    except Exception as e:
        print(f"Error fetching last race results: {e}")
        return None

def fetch_season_calendar():
    try:
        url = f"{BASE_URL}/current.json"
        data = fetch_data(url)
        races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])
        return races
    except Exception as e:
        print(f"Error fetching season calendar: {e}")
        return []

def fetch_qualifying_results():
    try:
        url = f"{BASE_URL}/current/last/qualifying.json"
        data = fetch_data(url)
        races = data.get('MRData', {}).get('RaceTable', {}).get('Races', [])
        if races:
            return races[0]
        return None
    except Exception as e:
        print(f"Error fetching qualifying results: {e}")
        return None

def write_if_changed(filepath, new_data):
    current_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                old_data = json.load(f)
                
            old_data_cmp = {k: v for k, v in old_data.items() if k != 'updated_at_utc'}
            new_data_cmp = {k: v for k, v in new_data.items() if k != 'updated_at_utc'}
            
            if old_data_cmp == new_data_cmp:
                print(f"No changes in {filepath}")
                return False
        except json.JSONDecodeError:
            pass

    new_data_with_time = new_data.copy()
    new_data_with_time['updated_at_utc'] = current_time
    
    with open(filepath, 'w') as f:
        json.dump(new_data_with_time, f, indent=2)
    print(f"Updated {filepath}")
    return True

def format_date(date_str):
    if not date_str:
        return "TBD"
    try:
        d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return d.strftime("%b ") + str(d.day)
    except:
        return date_str

def get_medal(pos):
    pos = int(pos)
    if pos == 1: return "🥇"
    if pos == 2: return "🥈"
    if pos == 3: return "🥉"
    return str(pos)

def build_readme_section(driver_standings, constructor_standings, last_race, next_race, last_results, calendar):
    lines = []
    
    # 1. Status Line
    season = "Unknown"
    if driver_standings and 'season' in driver_standings:
        season = driver_standings['season']
    elif calendar and len(calendar) > 0:
        season = calendar[0].get('season', "Unknown")
        
    now = datetime.datetime.now(datetime.timezone.utc)
    lines.append(f"Season Status: {season} in progress")
    lines.append("")
    
    # 2. Race Info
    if last_race:
        lines.append(f"**Last Race:** {last_race.get('raceName')} (Round {last_race.get('round')}) - {last_race.get('Circuit', {}).get('circuitName')}, {last_race.get('Circuit', {}).get('Location', {}).get('country')} ({format_date(last_race.get('date'))})")
    if next_race:
        lines.append(f"**Next Race:** {next_race.get('raceName')} (Round {next_race.get('round')}) - {next_race.get('Circuit', {}).get('circuitName')}, {next_race.get('Circuit', {}).get('Location', {}).get('country')} ({format_date(next_race.get('date'))})")
    lines.append("")
    
    # 3. Championship Leaders
    d_leader = None
    if driver_standings and driver_standings.get('DriverStandings'):
        d_leader = driver_standings['DriverStandings'][0]
        name = f"{d_leader.get('Driver', {}).get('givenName')} {d_leader.get('Driver', {}).get('familyName')}"
        pts = float(d_leader.get('points', 0))
        wins = int(d_leader.get('wins', 0))
        lines.append(f"**Drivers' Leader:** {name} - {pts} pts ({wins} wins)")
        
    if constructor_standings and constructor_standings.get('ConstructorStandings'):
        c_leader = constructor_standings['ConstructorStandings'][0]
        c_name = c_leader.get('Constructor', {}).get('name')
        c_pts = float(c_leader.get('points', 0))
        c_wins = int(c_leader.get('wins', 0))
        lines.append(f"**Constructors' Leader:** {c_name} - {c_pts} pts ({c_wins} wins)")
    lines.append("")
    
    # 4. Season Stats Summary
    completed = len([r for r in calendar if datetime.datetime.strptime(r.get('date'), "%Y-%m-%d").date() < now.date()]) if calendar else 0
    total = len(calendar) if calendar else 0
    remaining = total - completed
    update_str = now.strftime("%b %d, %Y %H:%M UTC")
    lines.append(f"📊 {completed} races completed | {remaining} remaining | Last updated: {update_str}")
    lines.append("")
    
    # 5. Championship Battle
    lines.append("## 🏆 Championship Battle\n")
    lines.append("| Driver | Team | Points | Gap to Leader |")
    lines.append("| --- | --- | ---: | --- |")
    if driver_standings and driver_standings.get('DriverStandings'):
        leader_pts = float(driver_standings['DriverStandings'][0].get('points', 0))
        for i, ds in enumerate(driver_standings['DriverStandings'][:5]):
            pos = int(ds.get('position', i+1))
            medal = get_medal(pos)
            name = f"{ds.get('Driver', {}).get('givenName')} {ds.get('Driver', {}).get('familyName')}"
            team = ds.get('Constructors', [{}])[0].get('name', 'Unknown')
            pts = float(ds.get('points', 0))
            if pos == 1:
                gap = "—"
            else:
                gap = f"-{leader_pts - pts:g} pts"
            pts_str = f"{pts:g}"
            lines.append(f"| {medal} {name} | {team} | {pts_str} | {gap} |")
    lines.append("")
    
    # 6. Last Race Podium
    if last_results:
        r_name = last_results.get('raceName', 'Unknown')
        r_round = last_results.get('round', '?')
        lines.append(f"## 🏁 Last Race: {r_name} (Round {r_round})\n")
        lines.append("| Pos | Driver | Team | Time/Status | Points |")
        lines.append("| --- | --- | --- | --- | ---: |")
        results = last_results.get('Results', [])
        for res in results[:10]:
            pos = int(res.get('position', 0))
            medal_or_pos = get_medal(pos)
            name = f"{res.get('Driver', {}).get('givenName')} {res.get('Driver', {}).get('familyName')}"
            team = res.get('Constructor', {}).get('name', 'Unknown')
            pts = float(res.get('points', 0))
            pts_str = f"{pts:g}"
            
            status = res.get('status', '')
            time_obj = res.get('Time', {})
            if time_obj:
                time_str = time_obj.get('time', status)
            else:
                time_str = status
                
            fastest = ""
            fl_obj = res.get('FastestLap', {})
            if fl_obj and fl_obj.get('rank') == '1':
                fastest = " ⚡"
                
            lines.append(f"| {medal_or_pos} | {name}{fastest} | {team} | {time_str} | {pts_str} |")
    lines.append("")
    
    # 7. Full Drivers' Championship
    lines.append(f"## 🏎️ Drivers' Championship — {season}\n")
    lines.append("| Pos | Driver | Team | Points | Wins |")
    lines.append("| ---: | --- | --- | ---: | ---: |")
    if driver_standings and driver_standings.get('DriverStandings'):
        for ds in driver_standings['DriverStandings']:
            pos = int(ds.get('position', 0))
            name = f"{ds.get('Driver', {}).get('givenName')} {ds.get('Driver', {}).get('familyName')}"
            team = ds.get('Constructors', [{}])[0].get('name', 'Unknown')
            pts = float(ds.get('points', 0))
            pts_str = f"{pts:g}"
            wins = int(ds.get('wins', 0))
            lines.append(f"| {pos} | {name} | {team} | {pts_str} | {wins} |")
    lines.append("")
    
    # 8. Constructors' Championship
    lines.append(f"## 🏗️ Constructors' Championship — {season}\n")
    lines.append("| Pos | Team | Points | Wins |")
    lines.append("| ---: | --- | ---: | ---: |")
    if constructor_standings and constructor_standings.get('ConstructorStandings'):
        for cs in constructor_standings['ConstructorStandings']:
            pos = int(cs.get('position', 0))
            team = cs.get('Constructor', {}).get('name', 'Unknown')
            pts = float(cs.get('points', 0))
            pts_str = f"{pts:g}"
            wins = int(cs.get('wins', 0))
            lines.append(f"| {pos} | {team} | {pts_str} | {wins} |")
    lines.append("")
    
    # 9. Season Calendar
    lines.append(f"## 📅 Season Calendar — {season}\n")
    lines.append("| Round | Race | Circuit | Date | Status |")
    lines.append("| ---: | --- | --- | --- | --- |")
    
    next_race_round = None
    if next_race:
        next_race_round = next_race.get('round')
        
    if calendar:
        for r in calendar:
            rd = r.get('round', '')
            name = r.get('raceName', '')
            circuit = r.get('Circuit', {}).get('circuitName', '')
            date_val = r.get('date', '')
            date_str = format_date(date_val)
            
            status = "⬜ Upcoming"
            if rd == next_race_round:
                status = "🔜 Next Race"
            elif date_val:
                try:
                    d = datetime.datetime.strptime(date_val, "%Y-%m-%d").date()
                    if d < now.date():
                        status = "✅ Completed"
                except:
                    pass
                    
            lines.append(f"| {rd} | {name} | {circuit} | {date_str} | {status} |")
    lines.append("")
    
    # 10. Footer
    lines.append("---")
    lines.append("> 🤖 Auto-updated by [GitHub Actions](../../actions) using the [Jolpica F1 API](https://github.com/jolpica/jolpica-f1) | [View raw data](data/)")
    
    return "\n".join(lines)

def update_readme(readme_path, new_section_content, driver_standings):
    if not os.path.exists(readme_path):
        print(f"README.md not found at {readme_path}")
        return
        
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace main section
    start_marker = "<!-- F1_AUTO_START -->"
    end_marker = "<!-- F1_AUTO_END -->"
    
    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        new_content = before + start_marker + "\n" + new_section_content + "\n" + end_marker + after
    else:
        new_content = content + "\n\n" + start_marker + "\n" + new_section_content + "\n" + end_marker + "\n"
        
    # Update leader line
    leader_marker = "<!-- F1_LEADER -->"
    leader_info = ""
    if driver_standings and driver_standings.get('DriverStandings'):
        d_leader = driver_standings['DriverStandings'][0]
        name = f"{d_leader.get('Driver', {}).get('givenName')} {d_leader.get('Driver', {}).get('familyName')}"
        pts = float(d_leader.get('points', 0))
        wins = int(d_leader.get('wins', 0))
        season = driver_standings.get('season', datetime.datetime.now().year)
        leader_info = f"🏁 Current F1 leader ({season}): {name} - {pts:g} pts, {wins} wins"
        
    if leader_marker in new_content:
        lines = new_content.split('\n')
        for i, line in enumerate(lines):
            if leader_marker in line:
                if i + 1 < len(lines):
                    lines[i+1] = leader_info
                else:
                    lines.append(leader_info)
                break
        new_content = '\n'.join(lines)
    else:
        new_content += f"\n{leader_marker}\n{leader_info}\n"
        
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated README.md")

def main():
    os.makedirs('data', exist_ok=True)
    
    print("Fetching F1 Data...")
    driver_standings = fetch_standings('driver')
    constructor_standings = fetch_standings('constructor')
    last_race = fetch_race('last')
    next_race = fetch_race('next')
    last_results = fetch_last_race_results()
    calendar = fetch_season_calendar()
    qualifying = fetch_qualifying_results()
    
    print("\nWriting JSON data files...")
    if driver_standings:
        write_if_changed('data/driver_standings.json', {'data': driver_standings})
    if constructor_standings:
        write_if_changed('data/constructor_standings.json', {'data': constructor_standings})
    if last_results:
        write_if_changed('data/last_race_results.json', {'data': last_results, 'qualifying': qualifying})
    if calendar:
        write_if_changed('data/season_calendar.json', {'data': calendar})
        
    print("\nGenerating README section...")
    readme_section = build_readme_section(
        driver_standings, 
        constructor_standings, 
        last_race, 
        next_race, 
        last_results, 
        calendar
    )
    
    update_readme('README.md', readme_section, driver_standings)
    print("Done!")

if __name__ == "__main__":
    main()
