# F1 Daily Stats Tracker

This repo auto-updates using GitHub Actions to track the current F1 season
(driver & constructor standings) via the Ergast timing API.

## Setup

To ensure that automated commits count towards your GitHub activity:

1. **Create a Personal Access Token (PAT)**:
   - Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Generate a new token with `repo` scope (or fine-grained token with `contents:write` permission)
   - Copy the token

2. **Add the token as a repository secret**:
   - Go to your repository Settings → Secrets and variables → Actions
   - Create a new repository secret named `PAT_TOKEN`
   - Paste your Personal Access Token as the value

3. The workflow will automatically use your PAT for commits, which will appear under your GitHub username and count towards your contribution graph.

> **Note**: If you don't set up a PAT_TOKEN secret, the workflow will fall back to using the default GITHUB_TOKEN, but those commits may not count towards your GitHub activity graph.

<!-- F1_AUTO_START -->
🏁 **Season 2025 is finished.**

- 🏁 **Last race** (Round 24): Abu Dhabi Grand Prix – Yas Marina Circuit (UAE, 2025-12-07)
- 🗓 **Next race**: Season finished ✅

🏆 **Drivers' Champion (2025)**: Lando Norris (423.0 pts, 7 wins, McLaren)
🏆 **Constructors' Champion (2025)**: McLaren (833.0 pts, 14 wins)

## Top 10 Drivers – 2025

| Pos | Driver | Constructor | Points | Wins |
| --- | ------ | ----------- | ------ | ---- |
| 1 | Lando Norris | McLaren | 423.0 | 7 |
| 2 | Max Verstappen | Red Bull | 421.0 | 8 |
| 3 | Oscar Piastri | McLaren | 410.0 | 7 |
| 4 | George Russell | Mercedes | 319.0 | 2 |
| 5 | Charles Leclerc | Ferrari | 242.0 | 0 |
| 6 | Lewis Hamilton | Ferrari | 156.0 | 0 |
| 7 | Andrea Kimi Antonelli | Mercedes | 150.0 | 0 |
| 8 | Alexander Albon | Williams | 73.0 | 0 |
| 9 | Carlos Sainz | Williams | 64.0 | 0 |
| 10 | Fernando Alonso | Aston Martin | 56.0 | 0 |
<!-- F1_AUTO_END -->


<!-- F1_LEADER -->
🏁 Current F1 leader (2025): Lando Norris - 408.0 pts, 7 wins
