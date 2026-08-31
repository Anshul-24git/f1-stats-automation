# 🏎️ F1 Stats Automation

[![F1 Stats Automation](https://github.com/Anshul-24git/f1-stats-automation/actions/workflows/f1-daily.yml/badge.svg)](https://github.com/Anshul-24git/f1-stats-automation/actions/workflows/f1-daily.yml)

> **Live Formula 1 standings, race results, and season calendar — auto-updated daily by GitHub Actions.**

This repository tracks the current F1 season with comprehensive data including driver & constructor championships, last race results with podium finishers, and a complete season calendar. Data is fetched from the [Jolpica F1 API](https://github.com/jolpica/jolpica-f1) (successor to the retired Ergast API) and committed automatically.

### ✨ Features

- 🏆 **Championship Battle** — Top 5 title contenders with points gaps
- 🏁 **Last Race Results** — Top 10 finishers with fastest lap indicator
- 🏎️ **Full Driver Standings** — Complete championship table
- 🏗️ **Constructor Standings** — Team championship rankings
- 📅 **Season Calendar** — Every race with completion status
- 📊 **Season Stats** — Races completed, remaining, live update timestamps
- 🤖 **Fully Automated** — Daily updates via GitHub Actions, zero maintenance

### 🔧 How It Works

1. A GitHub Actions workflow runs daily at 07:00 UTC (and can be triggered manually)
2. The Python script fetches live data from the Jolpica F1 API
3. JSON data files in [`data/`](data/) are updated only when standings change
4. This README is regenerated with the latest stats
5. Changes are committed and pushed automatically

---

<!-- F1_AUTO_START -->
Season Status: 2026 in progress

**Last Race:** Dutch Grand Prix (Round 12) - Circuit Park Zandvoort, Netherlands (Aug 23)
**Next Race:** Italian Grand Prix (Round 13) - Autodromo Nazionale di Monza, Italy (Sep 6)

**Drivers' Leader:** Andrea Kimi Antonelli - 242.0 pts (6 wins)
**Constructors' Leader:** Mercedes - 425.0 pts (8 wins)

📊 12 races completed | 11 remaining | Last updated: Aug 31, 2026 14:51 UTC

## 🏆 Championship Battle

| Driver | Team | Points | Gap to Leader |
| --- | --- | ---: | --- |
| 🥇 Andrea Kimi Antonelli | Mercedes | 242 | — |
| 🥈 George Russell | Mercedes | 183 | -59 pts |
| 🥉 Lewis Hamilton | Ferrari | 183 | -59 pts |
| 4 Lando Norris | McLaren | 159 | -83 pts |
| 5 Charles Leclerc | Ferrari | 155 | -87 pts |

## 🏁 Last Race: Dutch Grand Prix (Round 12)

| Pos | Driver | Team | Time/Status | Points |
| --- | --- | --- | --- | ---: |
| 🥇 | Lando Norris | McLaren | 2:04:44.859 | 25 |
| 🥈 | Andrea Kimi Antonelli | Mercedes | +11.536 | 18 |
| 🥉 | George Russell | Mercedes | +15.906 | 15 |
| 4 | Lewis Hamilton | Ferrari | +16.755 | 12 |
| 5 | Charles Leclerc ⚡ | Ferrari | +17.258 | 10 |
| 6 | Oscar Piastri | McLaren | +32.332 | 8 |
| 7 | Liam Lawson | Red Bull | +1:19.915 | 6 |
| 8 | Nico Hülkenberg | Audi | +36.049 | 4 |
| 9 | Fernando Alonso | Aston Martin | +48.393 | 2 |
| 10 | Pierre Gasly | Alpine F1 Team | +49.640 | 1 |

## 🏎️ Drivers' Championship — 2026

| Pos | Driver | Team | Points | Wins |
| ---: | --- | --- | ---: | ---: |
| 1 | Andrea Kimi Antonelli | Mercedes | 242 | 6 |
| 2 | George Russell | Mercedes | 183 | 2 |
| 3 | Lewis Hamilton | Ferrari | 183 | 1 |
| 4 | Lando Norris | McLaren | 159 | 2 |
| 5 | Charles Leclerc | Ferrari | 155 | 1 |
| 6 | Max Verstappen | Red Bull | 112 | 0 |
| 7 | Oscar Piastri | McLaren | 104 | 0 |
| 8 | Isack Hadjar | Red Bull | 68 | 0 |
| 9 | Liam Lawson | RB F1 Team | 49 | 0 |
| 10 | Pierre Gasly | Alpine F1 Team | 44 | 0 |
| 11 | Arvid Lindblad | RB F1 Team | 23 | 0 |
| 12 | Franco Colapinto | Alpine F1 Team | 19 | 0 |
| 13 | Oliver Bearman | Haas F1 Team | 18 | 0 |
| 14 | Gabriel Bortoleto | Audi | 10 | 0 |
| 15 | Nico Hülkenberg | Audi | 6 | 0 |
| 16 | Carlos Sainz | Williams | 6 | 0 |
| 17 | Alexander Albon | Williams | 5 | 0 |
| 18 | Esteban Ocon | Haas F1 Team | 3 | 0 |
| 19 | Fernando Alonso | Aston Martin | 3 | 0 |
| 20 | Yuki Tsunoda | RB F1 Team | 0 | 0 |
| 21 | Lance Stroll | Aston Martin | 0 | 0 |
| 22 | Valtteri Bottas | Cadillac F1 Team | 0 | 0 |
| 23 | Sergio Pérez | Cadillac F1 Team | 0 | 0 |

## 🏗️ Constructors' Championship — 2026

| Pos | Team | Points | Wins |
| ---: | --- | ---: | ---: |
| 1 | Mercedes | 425 | 8 |
| 2 | Ferrari | 338 | 2 |
| 3 | McLaren | 263 | 2 |
| 4 | Red Bull | 186 | 0 |
| 5 | RB F1 Team | 66 | 0 |
| 6 | Alpine F1 Team | 63 | 0 |
| 7 | Haas F1 Team | 21 | 0 |
| 8 | Audi | 16 | 0 |
| 9 | Williams | 11 | 0 |
| 10 | Aston Martin | 3 | 0 |
| 11 | Cadillac F1 Team | 0 | 0 |

## 📅 Season Calendar — 2026

| Round | Race | Circuit | Date | Status |
| ---: | --- | --- | --- | --- |
| 1 | Australian Grand Prix | Albert Park Grand Prix Circuit | Mar 8 | ✅ Completed |
| 2 | Chinese Grand Prix | Shanghai International Circuit | Mar 15 | ✅ Completed |
| 3 | Japanese Grand Prix | Suzuka Circuit | Mar 29 | ✅ Completed |
| 4 | Miami Grand Prix | Miami International Autodrome | May 3 | ✅ Completed |
| 5 | Canadian Grand Prix | Circuit Gilles Villeneuve | May 24 | ✅ Completed |
| 6 | Monaco Grand Prix | Circuit de Monaco | Jun 7 | ✅ Completed |
| 7 | Barcelona Grand Prix | Circuit de Barcelona-Catalunya | Jun 14 | ✅ Completed |
| 8 | Austrian Grand Prix | Red Bull Ring | Jun 28 | ✅ Completed |
| 9 | British Grand Prix | Silverstone Circuit | Jul 5 | ✅ Completed |
| 10 | Belgian Grand Prix | Circuit de Spa-Francorchamps | Jul 19 | ✅ Completed |
| 11 | Hungarian Grand Prix | Hungaroring | Jul 26 | ✅ Completed |
| 12 | Dutch Grand Prix | Circuit Park Zandvoort | Aug 23 | ✅ Completed |
| 13 | Italian Grand Prix | Autodromo Nazionale di Monza | Sep 6 | 🔜 Next Race |
| 14 | Spanish Grand Prix | Madring | Sep 13 | ⬜ Upcoming |
| 15 | Azerbaijan Grand Prix | Baku City Circuit | Sep 26 | ⬜ Upcoming |
| 16 | Bahrain Grand Prix in Malaysia | Sepang International Circuit | Oct 4 | ⬜ Upcoming |
| 17 | Singapore Grand Prix | Marina Bay Street Circuit | Oct 11 | ⬜ Upcoming |
| 18 | United States Grand Prix | Circuit of the Americas | Oct 25 | ⬜ Upcoming |
| 19 | Mexico City Grand Prix | Autódromo Hermanos Rodríguez | Nov 1 | ⬜ Upcoming |
| 20 | Brazilian Grand Prix | Autódromo José Carlos Pace | Nov 8 | ⬜ Upcoming |
| 21 | Las Vegas Grand Prix | Las Vegas Strip Street Circuit | Nov 22 | ⬜ Upcoming |
| 22 | Qatar Grand Prix | Losail International Circuit | Nov 29 | ⬜ Upcoming |
| 23 | Abu Dhabi Grand Prix | Yas Marina Circuit | Dec 6 | ⬜ Upcoming |

---
> 🤖 Auto-updated by [GitHub Actions](../../actions) using the [Jolpica F1 API](https://github.com/jolpica/jolpica-f1) | [View raw data](data/)
<!-- F1_AUTO_END -->


<!-- F1_LEADER -->
🏁 Current F1 leader (2026): Andrea Kimi Antonelli - 242 pts, 6 wins
