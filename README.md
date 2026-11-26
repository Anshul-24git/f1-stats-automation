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

**Last Race:** Las Vegas Grand Prix (Round 21) - Las Vegas Strip Street Circuit, USA (Nov 22)
**Next Race:** Qatar Grand Prix (Round 22) - Lusail International Circuit, Qatar (Nov 29)

**Drivers' Leader:** Andrea Kimi Antonelli - 402.0 pts (9 wins)
**Constructors' Leader:** Mercedes - 666.0 pts (12 wins)

📊 21 races completed | 2 remaining | Last updated: Nov 26, 2026 17:31 UTC

## 🏆 Championship Battle

| Driver | Team | Points | Gap to Leader |
| --- | --- | ---: | --- |
| 🥇 Andrea Kimi Antonelli | Mercedes | 402 | — |
| 🥈 Max Verstappen | Red Bull | 304 | -98 pts |
| 🥉 Lewis Hamilton | Ferrari | 267 | -135 pts |
| 4 George Russell | Mercedes | 264 | -138 pts |
| 5 Lando Norris | McLaren | 264 | -138 pts |

## 🏁 Last Race: Las Vegas Grand Prix (Round 21)

| Pos | Driver | Team | Time/Status | Points |
| --- | --- | --- | --- | ---: |
| 🥇 | Max Verstappen | Red Bull | 1:27:39.624 | 25 |
| 🥈 | Lando Norris | McLaren | +0.639 | 18 |
| 🥉 | Oscar Piastri | McLaren | +1.529 | 15 |
| 4 | Andrea Kimi Antonelli | Mercedes | +2.574 | 12 |
| 5 | Pierre Gasly | Alpine F1 Team | +2.927 | 10 |
| 6 | Franco Colapinto | Alpine F1 Team | +7.955 | 8 |
| 7 | Lewis Hamilton | Ferrari | +12.795 | 6 |
| 8 | Carlos Sainz | Williams | +12.938 | 4 |
| 9 | George Russell | Mercedes | +13.192 | 2 |
| 10 | Charles Leclerc | Ferrari | +17.554 | 1 |

## 🏎️ Drivers' Championship — 2026

| Pos | Driver | Team | Points | Wins |
| ---: | --- | --- | ---: | ---: |
| 1 | Andrea Kimi Antonelli | Mercedes | 402 | 9 |
| 2 | Max Verstappen | Red Bull | 304 | 4 |
| 3 | Lewis Hamilton | Ferrari | 267 | 1 |
| 4 | George Russell | Mercedes | 264 | 3 |
| 5 | Lando Norris | McLaren | 264 | 3 |
| 6 | Charles Leclerc | Ferrari | 250 | 1 |
| 7 | Oscar Piastri | McLaren | 167 | 0 |
| 8 | Isack Hadjar | Red Bull | 122 | 0 |
| 9 | Liam Lawson | RB F1 Team | 89 | 0 |
| 10 | Pierre Gasly | Alpine F1 Team | 52 | 0 |
| 11 | Arvid Lindblad | RB F1 Team | 38 | 0 |
| 12 | Franco Colapinto | Alpine F1 Team | 35 | 0 |
| 13 | Oliver Bearman | Haas F1 Team | 23 | 0 |
| 14 | Gabriel Bortoleto | Audi | 14 | 0 |
| 15 | Nico Hülkenberg | Audi | 14 | 0 |
| 16 | Carlos Sainz | Williams | 11 | 0 |
| 17 | Esteban Ocon | Haas F1 Team | 7 | 0 |
| 18 | Fernando Alonso | Aston Martin | 7 | 0 |
| 19 | Alexander Albon | Williams | 5 | 0 |
| 20 | Yuki Tsunoda | RB F1 Team | 1 | 0 |
| 21 | Ryo Hirakawa | Haas F1 Team | 1 | 0 |
| 22 | Lance Stroll | Aston Martin | 0 | 0 |
| 23 | Valtteri Bottas | Cadillac F1 Team | 0 | 0 |
| 24 | Sergio Pérez | Cadillac F1 Team | 0 | 0 |
| 25 | Rafael Camara | Haas F1 Team | 0 | 0 |

## 🏗️ Constructors' Championship — 2026

| Pos | Team | Points | Wins |
| ---: | --- | ---: | ---: |
| 1 | Mercedes | 666 | 12 |
| 2 | Ferrari | 517 | 2 |
| 3 | Red Bull | 440 | 4 |
| 4 | McLaren | 431 | 3 |
| 5 | RB F1 Team | 114 | 0 |
| 6 | Alpine F1 Team | 87 | 0 |
| 7 | Haas F1 Team | 31 | 0 |
| 8 | Audi | 28 | 0 |
| 9 | Williams | 16 | 0 |
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
| 17 | Singapore Grand Prix | Marina Bay Street Circuit | Oct 11 | ✅ Completed |
| 18 | United States Grand Prix | Circuit of the Americas | Oct 25 | ✅ Completed |
| 19 | Mexico City Grand Prix | Autódromo Hermanos Rodríguez | Nov 1 | ✅ Completed |
| 20 | Brazilian Grand Prix | Autódromo José Carlos Pace | Nov 8 | ✅ Completed |
| 21 | Las Vegas Grand Prix | Las Vegas Strip Street Circuit | Nov 22 | ✅ Completed |
| 22 | Qatar Grand Prix | Lusail International Circuit | Nov 29 | 🔜 Next Race |
| 23 | Abu Dhabi Grand Prix | Yas Marina Circuit | Dec 6 | ⬜ Upcoming |

---
> 🤖 Auto-updated by [GitHub Actions](../../actions) using the [Jolpica F1 API](https://github.com/jolpica/jolpica-f1) | [View raw data](data/)
<!-- F1_AUTO_END -->


<!-- F1_LEADER -->
🏁 Current F1 leader (2026): Andrea Kimi Antonelli - 402 pts, 9 wins
