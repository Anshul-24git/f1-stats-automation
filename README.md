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

**Last Race:** Bahrain Grand Prix in Malaysia (Round 16) - Sepang International Circuit, Malaysia (Oct 4)
**Next Race:** Singapore Grand Prix (Round 17) - Marina Bay Street Circuit, Singapore (Oct 11)

**Drivers' Leader:** Andrea Kimi Antonelli - 320.0 pts (8 wins)
**Constructors' Leader:** Mercedes - 556.0 pts (11 wins)

📊 16 races completed | 7 remaining | Last updated: Oct 05, 2026 15:33 UTC

## 🏆 Championship Battle

| Driver | Team | Points | Gap to Leader |
| --- | --- | ---: | --- |
| 🥇 Andrea Kimi Antonelli | Mercedes | 320 | — |
| 🥈 George Russell | Mercedes | 236 | -84 pts |
| 🥉 Lewis Hamilton | Ferrari | 214 | -106 pts |
| 4 Charles Leclerc | Ferrari | 191 | -129 pts |
| 5 Lando Norris | McLaren | 188 | -132 pts |

## 🏁 Last Race: Bahrain Grand Prix in Malaysia (Round 16)

| Pos | Driver | Team | Time/Status | Points |
| --- | --- | --- | --- | ---: |
| 🥇 | Max Verstappen ⚡ | Red Bull | 1:47:14.808 | 25 |
| 🥈 | Andrea Kimi Antonelli | Mercedes | +2.307 | 18 |
| 🥉 | Lewis Hamilton | Ferrari | +4.919 | 15 |
| 4 | Charles Leclerc | Ferrari | +7.258 | 12 |
| 5 | Isack Hadjar | Red Bull | +8.571 | 10 |
| 6 | Oscar Piastri | McLaren | +9.454 | 8 |
| 7 | Liam Lawson | RB F1 Team | +12.753 | 6 |
| 8 | Fernando Alonso | Aston Martin | +13.372 | 4 |
| 9 | Lando Norris | McLaren | +13.993 | 2 |
| 10 | Arvid Lindblad | RB F1 Team | +15.928 | 1 |

## 🏎️ Drivers' Championship — 2026

| Pos | Driver | Team | Points | Wins |
| ---: | --- | --- | ---: | ---: |
| 1 | Andrea Kimi Antonelli | Mercedes | 320 | 8 |
| 2 | George Russell | Mercedes | 236 | 3 |
| 3 | Lewis Hamilton | Ferrari | 214 | 1 |
| 4 | Charles Leclerc | Ferrari | 191 | 1 |
| 5 | Lando Norris | McLaren | 188 | 2 |
| 6 | Max Verstappen | Red Bull | 188 | 1 |
| 7 | Oscar Piastri | McLaren | 128 | 0 |
| 8 | Isack Hadjar | Red Bull | 96 | 0 |
| 9 | Liam Lawson | RB F1 Team | 65 | 0 |
| 10 | Pierre Gasly | Alpine F1 Team | 41 | 0 |
| 11 | Arvid Lindblad | RB F1 Team | 38 | 0 |
| 12 | Franco Colapinto | Alpine F1 Team | 27 | 0 |
| 13 | Oliver Bearman | Haas F1 Team | 20 | 0 |
| 14 | Gabriel Bortoleto | Audi | 10 | 0 |
| 15 | Nico Hülkenberg | Audi | 7 | 0 |
| 16 | Esteban Ocon | Haas F1 Team | 7 | 0 |
| 17 | Fernando Alonso | Aston Martin | 7 | 0 |
| 18 | Carlos Sainz | Williams | 7 | 0 |
| 19 | Alexander Albon | Williams | 5 | 0 |
| 20 | Yuki Tsunoda | RB F1 Team | 1 | 0 |
| 21 | Lance Stroll | Aston Martin | 0 | 0 |
| 22 | Valtteri Bottas | Cadillac F1 Team | 0 | 0 |
| 23 | Sergio Pérez | Cadillac F1 Team | 0 | 0 |

## 🏗️ Constructors' Championship — 2026

| Pos | Team | Points | Wins |
| ---: | --- | ---: | ---: |
| 1 | Mercedes | 556 | 11 |
| 2 | Ferrari | 405 | 2 |
| 3 | McLaren | 316 | 2 |
| 4 | Red Bull | 298 | 1 |
| 5 | RB F1 Team | 90 | 0 |
| 6 | Alpine F1 Team | 68 | 0 |
| 7 | Haas F1 Team | 27 | 0 |
| 8 | Audi | 17 | 0 |
| 9 | Williams | 12 | 0 |
| 10 | Aston Martin | 7 | 0 |
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
| 13 | Italian Grand Prix | Autodromo Nazionale di Monza | Sep 6 | ✅ Completed |
| 14 | Spanish Grand Prix | Madring | Sep 13 | ✅ Completed |
| 15 | Azerbaijan Grand Prix | Baku City Circuit | Sep 26 | ✅ Completed |
| 16 | Bahrain Grand Prix in Malaysia | Sepang International Circuit | Oct 4 | ✅ Completed |
| 17 | Singapore Grand Prix | Marina Bay Street Circuit | Oct 11 | 🔜 Next Race |
| 18 | United States Grand Prix | Circuit of the Americas | Oct 25 | ⬜ Upcoming |
| 19 | Mexico City Grand Prix | Autódromo Hermanos Rodríguez | Nov 1 | ⬜ Upcoming |
| 20 | Brazilian Grand Prix | Autódromo José Carlos Pace | Nov 8 | ⬜ Upcoming |
| 21 | Las Vegas Grand Prix | Las Vegas Strip Street Circuit | Nov 22 | ⬜ Upcoming |
| 22 | Qatar Grand Prix | Lusail International Circuit | Nov 29 | ⬜ Upcoming |
| 23 | Abu Dhabi Grand Prix | Yas Marina Circuit | Dec 6 | ⬜ Upcoming |

---
> 🤖 Auto-updated by [GitHub Actions](../../actions) using the [Jolpica F1 API](https://github.com/jolpica/jolpica-f1) | [View raw data](data/)
<!-- F1_AUTO_END -->


<!-- F1_LEADER -->
🏁 Current F1 leader (2026): Andrea Kimi Antonelli - 320 pts, 8 wins
