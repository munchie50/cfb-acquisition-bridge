# Week12 Nov20 7am manual catch-up — accepted REFRESH versus frozen and market

**Status: SOURCE_LINEAGE_JOIN / ANALYTICAL_TRIAGE_ONLY / NO_BET_APPROVAL**

The accepted Nov10 REFRESH prediction rows are from `evidence/audits/CFB_WEEK12_ALL_GAMES_REVIEW_20261117T194240Z_all_games.json` under `accepted_refresh_exact_coverage.week12_predictions`. The original FIRST_FROZEN remains the model authority and is NOT replaced. Joined by exact normalized away/home names, not by row position. Market home spread is public mixed-book CBS Nov20 from the full working card; spread difference is arithmetic only, not a bet edge. REFRESH pred_margin positive means home team favored in projected margin; therefore for spread comparisons convert refresh margin to **negative** projected home spread. The table shows margin and the CBS home spread separately; divergence is abs((-refresh margin) - CBS home spread).

| Day | Matchup | Original frozen home margin | Accepted Nov10 refresh home margin | Friday CBS home spread | Abs refresh-to-market spread gap | Frozen/refresh direction conflict |
|---|---|---:|---:|---:|---:|---|
| Fri Nov 20 | Iowa State @ UCF | -5.2 | 6.23 | +1.5 | 7.73 | YES |
| Fri Nov 20 | Bowling Green @ Toledo | -28.0 | 17.33 | -16.5 | 0.83 | YES |
| Fri Nov 20 | Clemson @ Duke | EXCLUDED | 13.04 | -12.5 | 0.54 | NO |
| Fri Nov 20 | Oregon @ Michigan State | 5.1 | -3.49 | +17.5 | 14.01 | YES |
| Fri Nov 20 | UTEP @ Air Force | -20.4 | 16.84 | -21.5 | 4.66 | YES |
| Fri Nov 20 | New Mexico @ Wyoming | 9.3 | -3.47 | +9.5 | 6.03 | YES |
| Sat Nov 21 | Vanderbilt @ Florida | -15.3 | 9.17 | -13.5 | 4.33 | YES |
| Sat Nov 21 | Wake Forest @ Georgia Tech | -5.5 | -13.23 | +20.5 | 7.27 | NO |
| Sat Nov 21 | Wofford @ Ole Miss | -23.5 | 29.53 | -48.5 | 18.97 | YES |
| Sat Nov 21 | Ohio State @ Nebraska | -4.9 | 1.14 | +3.5 | 4.64 | YES |
| Sat Nov 21 | Northwestern @ Minnesota | EXCLUDED | -3.86 | +2.5 | 1.36 | NO |
| Sat Nov 21 | BYU @ Kansas | 6.4 | 0.97 | +6 | 6.97 | NO |
| Sat Nov 21 | Wisconsin @ Purdue | 2.6 | -3.30 | +6 | 2.70 | YES |
| Sat Nov 21 | Memphis @ Navy | EXCLUDED | -1.34 | +3 | 1.66 | NO |
| Sat Nov 21 | East Carolina @ Army | EXCLUDED | 5.35 | -5.5 | 0.15 | NO |
| Sat Nov 21 | Colorado @ Cincinnati | -14.4 | 7.58 | -2.5 | 5.08 | YES |
| Sat Nov 21 | Syracuse @ Boston College | 0.9 | 0.90 | +2.5 | 3.40 | NO |
| Sat Nov 21 | North Texas @ Tulane | -2.6 | -7.33 | +6.5 | 0.83 | NO |
| Sat Nov 21 | North Carolina @ Virginia | -7.2 | 0.29 | -1.5 | 1.21 | YES |
| Sat Nov 21 | Houston @ West Virginia | 0.5 | -5.20 | +7.5 | 2.30 | YES |
| Sat Nov 21 | Western Kentucky @ Liberty | EXCLUDED | 19.64 | -16.5 | 3.14 | NO |
| Sat Nov 21 | Charlotte @ Tulsa | -20.4 | 18.64 | -22.5 | 3.86 | YES |
| Sat Nov 21 | Middle Tennessee @ Sam Houston | -13.7 | 3.84 | +6.5 | 10.34 | YES |
| Sat Nov 21 | Missouri State @ Jacksonville State | -7.9 | 13.50 | -10.5 | 3.00 | YES |
| Sat Nov 21 | UL Monroe @ App State | -24.5 | 12.09 | -13.5 | 1.41 | YES |
| Sat Nov 21 | South Florida @ Florida Atlantic | 12.7 | -2.48 | +1.5 | 0.98 | YES |
| Sat Nov 21 | Iowa @ Illinois | 1.2 | -0.55 | +9 | 8.45 | YES |
| Sat Nov 21 | Florida International @ Kennesaw State | -3.5 | 3.00 | -2.5 | 0.50 | YES |
| Sat Nov 21 | Delaware @ New Mexico State | 0.1 | 1.31 | +3.5 | 4.81 | NO |
| Sat Nov 21 | Coastal Carolina @ Louisiana | EXCLUDED | 8.35 | -10.5 | 2.15 | NO |
| Sat Nov 21 | Texas Tech @ Baylor | -8.1 | 4.79 | +5 | 9.79 | YES |
| Sat Nov 21 | Rutgers @ Penn State | EXCLUDED | 12.46 | -25.5 | 13.04 | NO |
| Sat Nov 21 | Indiana @ Washington | EXCLUDED | -3.13 | +7.5 | 4.37 | NO |
| Sat Nov 21 | Arkansas @ Texas | -21.2 | 14.68 | -20.5 | 5.82 | YES |
| Sat Nov 21 | Samford @ Auburn | EXCLUDED | 20.49 | -48.5 | 28.01 | NO |
| Sat Nov 21 | LSU @ Tennessee | -9.6 | 1.25 | +1.5 | 2.75 | YES |
| Sat Nov 21 | Old Dominion @ UConn | -11.9 | 12.03 | -13.5 | 1.47 | YES |
| Sat Nov 21 | NC State @ Florida State | 4.4 | 3.68 | -10.5 | 6.82 | NO |
| Sat Nov 21 | UCLA @ Michigan | -3.0 | -2.43 | +3.5 | 1.07 | NO |
| Sat Nov 21 | Texas A&M @ Oklahoma | -8.9 | 4.17 | -7 | 2.83 | YES |
| Sat Nov 21 | Georgia State @ Marshall | 10.3 | -3.48 | -2.5 | 5.98 | YES |
| Sat Nov 21 | Northern Illinois @ North Dakota State | -22.3 | 18.40 | -24.5 | 6.10 | YES |
| Sat Nov 21 | South Alabama @ Southern Miss | -2.0 | 2.62 | +3.5 | 6.12 | YES |
| Sat Nov 21 | Georgia Southern @ Troy | -2.1 | -1.59 | +9.5 | 7.91 | NO |
| Sat Nov 21 | Washington State @ Texas State | -0.1 | 15.06 | -13.5 | 1.56 | YES |
| Sat Nov 21 | Maryland @ USC | -1.6 | 10.41 | -17.5 | 7.09 | YES |
| Sat Nov 21 | Arkansas State @ Louisiana Tech | -0.4 | 5.54 | -14.5 | 8.96 | YES |
| Sat Nov 21 | UNLV @ San José State | -6.5 | 3.23 | +6.5 | 9.73 | YES |
| Sat Nov 21 | Virginia Tech @ Miami | -12.0 | 12.58 | -20.5 | 7.92 | YES |
| Sat Nov 21 | Arizona @ Kansas State | -13.8 | -1.38 | +7.5 | 6.12 | NO |
| Sat Nov 21 | Pittsburgh @ Louisville | -4.7 | 8.21 | -13.5 | 5.29 | YES |
| Sat Nov 21 | SMU @ Notre Dame | -11.6 | 7.52 | -20.5 | 12.98 | YES |
| Sat Nov 21 | Georgia @ South Carolina | 3.2 | -4.36 | +15 | 10.64 | YES |
| Sat Nov 21 | Kentucky @ Missouri | -8.1 | 4.73 | -4.5 | 0.23 | YES |
| Sat Nov 21 | Colorado State @ Fresno State | -3.8 | 12.25 | -19.5 | 7.25 | YES |
| Sat Nov 21 | Stanford @ California | EXCLUDED | 6.18 | +2.5 | 8.68 | NO |
| Sat Nov 21 | UTSA @ UAB | EXCLUDED | 2.66 | +6.5 | 9.16 | NO |
| Sat Nov 21 | Utah @ TCU | 2.2 | -0.95 | +7.5 | 6.55 | YES |
| Sat Nov 21 | San Diego State @ Boise State | -10.9 | 18.12 | -17.5 | 0.62 | YES |
| Sat Nov 21 | Oklahoma State @ Arizona State | 0.1 | -3.06 | +2.5 | 0.56 | YES |
| Sat Nov 21 | Hawai'i @ Nevada | -10.1 | 3.31 | -5.5 | 2.19 | YES |
| Sat Nov 21 | Utah State @ Oregon State | -11.4 | 10.09 | -8 | 2.09 | YES |

Exact name join: 62/64; unmatched: Tennessee Tech @ Mississippi State; Chattanooga @ Alabama. Unmatched are not assigned predictions by inference.
Direction conflicts among matched numerical frozen rows: 42.

No fresh 2026-11-20 accepted model run is implied. No new CONDITIONAL, acceptable price, execution, or publication promotion. Personnel/market gate still required.