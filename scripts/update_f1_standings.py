import json
import os
from datetime import datetime

import requests

# Ergast-compatible F1 API
BASE_URL = "https://api.jolpi.ca/ergast/f1"

# Markers used inside README.md
AUTO_START = "<!-- F1_AUTO_START -->"
AUTO_END = "<!-- F1_AUTO_END -->"


def fetch_standings(kind: str = "driver"):
    """
    Fetch current season standings.

    kind: 'driver' or 'constructor'
    """
    if kind == "driver":
        endpoint = f"{BASE_URL}/current/driverStandings.json"
    else:
        endpoint = f"{BASE_URL}/current/constructorStandings.json"

    resp = requests.get(endpoint, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    standings_lists = data["MRData"]["StandingsTable"].get("StandingsLists", [])
    if not standings_lists:
        return {
            "season": None,
            "kind": kind,
            "updated_at_utc": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "standings": [],
        }

    standings_list = standings_lists[0]
    season = standings_list["season"]

    raw = standings_list[
        "DriverStandings" if kind == "driver" else "ConstructorStandings"
    ]

    simplified = []
    for row in raw:
        if kind == "driver":
            driver = row["Driver"]
            simplified.append(
                {
                    "position": int(row["position"]),
                    "points": float(row["points"]),
                    "wins": int(row["wins"]),
                    "driverId": driver["driverId"],
                    "code": driver.get("code"),
                    "name": f"{driver['givenName']} {driver['familyName']}",
                    "nationality": driver["nationality"],
                    "constructor": row["Constructors"][0]["name"],
                }
            )
        else:
            constructor = row["Constructor"]
            simplified.append(
                {
                    "position": int(row["position"]),
                    "points": float(row["points"]),
                    "wins": int(row["wins"]),
                    "constructorId": constructor["constructorId"],
                    "name": constructor["name"],
                    "nationality": constructor["nationality"],
                }
            )

    return {
        "season": season,
        "kind": kind,
        "updated_at_utc": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "standings": simplified,
    }


def fetch_race(which: str):
    """
    Fetch last or next race of the current season.

    which: 'last' or 'next'
    """
    endpoint = f"{BASE_URL}/current/{which}.json"
    resp = requests.get(endpoint, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    races = data["MRData"]["RaceTable"].get("Races", [])
    if not races:
        return None

    r = races[0]
    return {
        "round": int(r["round"]),
        "raceName": r["raceName"],
        "circuit": r["Circuit"]["circuitName"],
        "date": r["date"],  # YYYY-MM-DD
        "country": r["Circuit"]["Location"]["country"],
    }


def write_if_changed(path: str, new_data: dict) -> bool:
    """
    Writes JSON only if content actually changed.
    Returns True if file was changed.
    """
    existing = None
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except json.JSONDecodeError:
            existing = None

    if existing == new_data:
        print(f"No changes detected for {path}")
        return False

    with open(path, "w", encoding="utf-8") as f:
        json.dump(new_data, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"Updated {path}")
    return True


def build_readme_section(driver_data, constructor_data, last_race, next_race):
    """
    Build the auto-generated README section as Markdown.
    """
    season = driver_data["season"]

    if not driver_data["standings"] or not constructor_data["standings"]:
        # Fallback in case the API ever fails or is empty
        return "Data unavailable at the moment. Please try again later."

    top_driver = driver_data["standings"][0]
    top_constructor = constructor_data["standings"][0]

    # Header text differs depending on whether season is finished
    if next_race is None:
        status_line = f"🏁 **Season {season} is finished.**"
        champion_lines = [
            f"🏆 **Drivers' Champion ({season})**: {top_driver['name']} "
            f"({top_driver['points']} pts, {top_driver['wins']} wins, {top_driver['constructor']})",
            f"🏆 **Constructors' Champion ({season})**: {top_constructor['name']} "
            f"({top_constructor['points']} pts, {top_constructor['wins']} wins)",
        ]
    else:
        status_line = f"🏎️ **Season {season} in progress.**"
        champion_lines = [
            f"👑 Current drivers' leader: {top_driver['name']} "
            f"({top_driver['points']} pts, {top_driver['wins']} wins, {top_driver['constructor']})",
            f"👑 Current constructors' leader: {top_constructor['name']} "
            f"({top_constructor['points']} pts, {top_constructor['wins']} wins)",
        ]

    lines = [status_line, ""]

    # Last race info
    if last_race:
        lines.append(
            f"- 🏁 **Last race** (Round {last_race['round']}): "
            f"{last_race['raceName']} – {last_race['circuit']} "
            f"({last_race['country']}, {last_race['date']})"
        )

    # Next race or season finished
    if next_race:
        lines.append(
            f"- 🗓 **Next race** (Round {next_race['round']}): "
            f"{next_race['raceName']} – {next_race['circuit']} "
            f"({next_race['country']}, {next_race['date']})"
        )
    else:
        lines.append("- 🗓 **Next race**: Season finished ✅")

    lines.append("")
    lines.extend(champion_lines)
    lines.append("")

    # Top 10 drivers table
    lines.append(f"## Top 10 Drivers – {season}")
    lines.append("")
    lines.append("| Pos | Driver | Constructor | Points | Wins |")
    lines.append("| --- | ------ | ----------- | ------ | ---- |")

    for row in driver_data["standings"][:10]:
        lines.append(
            f"| {row['position']} | {row['name']} | {row['constructor']} | "
            f"{row['points']} | {row['wins']} |"
        )

    return "\n".join(lines)


def update_readme(driver_data, constructor_data) -> bool:
    """
    Update README.md's auto-generated section.
    Returns True if the file changed.
    """
    last_race = None
    next_race = None

    try:
        last_race = fetch_race("last")
    except requests.RequestException as e:
        print(f"Warning: failed to fetch last race: {e}")

    try:
        next_race = fetch_race("next")
    except requests.RequestException as e:
        # When season is over, next race may not exist
        print(f"Info: failed to fetch next race (season might be over): {e}")
        next_race = None

    auto_section = build_readme_section(driver_data, constructor_data, last_race, next_race)

    readme_path = "README.md"

    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            original_content = f.read()
    else:
        # Basic header if README is missing
        original_content = "# F1 Daily Stats Tracker\n\n" + AUTO_START + "\n" + AUTO_END + "\n"

    if AUTO_START not in original_content or AUTO_END not in original_content:
        # Append auto section at the end if markers missing
        new_content = (
            original_content.rstrip()
            + "\n\n"
            + AUTO_START
            + "\n"
            + auto_section
            + "\n"
            + AUTO_END
            + "\n"
        )
    else:
        before, _, rest = original_content.partition(AUTO_START)
        _, _, after = rest.partition(AUTO_END)
        new_content = before + AUTO_START + "\n" + auto_section + "\n" + AUTO_END + after

    if new_content == original_content:
        print("No changes detected for README.md")
        return False

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("Updated README.md")
    return True


def main():
    os.makedirs("data", exist_ok=True)

    changed = False

    driver_data = fetch_standings("driver")
    constructor_data = fetch_standings("constructor")

    if write_if_changed("data/driver_standings.json", driver_data):
        changed = True

    if write_if_changed("data/constructor_standings.json", constructor_data):
        changed = True

    if update_readme(driver_data, constructor_data):
        changed = True

    if changed:
        print("Repo updated with latest F1 data.")
    else:
        print("No repo changes.")


if __name__ == "__main__":
    main()
