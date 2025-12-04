import json
import os
from datetime import datetime

import requests

BASE_URL = "https://api.jolpi.ca/ergast/f1"  # Ergast-compatible F1 API


def fetch_standings(kind: str = "driver"):
    """
    kind: 'driver' or 'constructor'
    """
    if kind == "driver":
        endpoint = f"{BASE_URL}/current/driverStandings.json"
    else:
        endpoint = f"{BASE_URL}/current/constructorStandings.json"

    resp = requests.get(endpoint, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    standings_list = data["MRData"]["StandingsTable"]["StandingsLists"][0]
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


def write_if_changed(path: str, new_data: dict) -> bool:
    """
    Writes JSON only if content actually changed.
    Returns True if file was changed.
    """
    existing = None
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
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


def main():
    os.makedirs("data", exist_ok=True)

    changed = False

    driver_data = fetch_standings("driver")
    constructor_data = fetch_standings("constructor")

    if write_if_changed("data/driver_standings.json", driver_data):
        changed = True
    if write_if_changed("data/constructor_standings.json", constructor_data):
        changed = True

    # Also update a short summary in README for humans
    if driver_data["standings"]:
        top_driver = driver_data["standings"][0]
        line = (
            f"🏁 Current F1 leader ({driver_data['season']}): "
            f"{top_driver['name']} - {top_driver['points']} pts, "
            f"{top_driver['wins']} wins"
        )

        readme_path = "README.md"
        if os.path.exists(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            content = "# F1 Daily Stats Tracker\n\n"

        marker = "<!-- F1_LEADER -->"
        if marker not in content:
            content += f"\n\n{marker}\n{line}\n"
        else:
            before, _, after = content.partition(marker)
            # after starts with the marker; keep marker and replace following line
            after_lines = after.splitlines()
            if len(after_lines) >= 2:
                after_lines[1] = line
            else:
                after_lines.append(line)
            after = "\n".join(after_lines)
            content = before + marker + after

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)

        changed = True

    if changed:
        print("Repo updated with latest F1 data.")
    else:
        print("No repo changes.")


if __name__ == "__main__":
    main()
