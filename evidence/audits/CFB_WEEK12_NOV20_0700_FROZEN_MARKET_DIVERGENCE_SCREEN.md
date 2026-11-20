# Week12 Nov20 7am manual catch-up — corrected frozen-to-market spread screen

**Status: DRIFT_CORRECTED / ARITHMETIC SCREEN ONLY / NO BET APPROVAL**

## Correction and supersession

The original screen erroneously treated FIRST_FROZEN's signed spread as a positive margin. Correct: `FIRST_FROZEN: Ole Miss -23.5` means projected home margin +23.5 and projected home spread -23.5. For a named away team with a negative spread, projected home margin is negative. Comparison is `abs((-frozen_home_margin) - CBS_home_spread)`. This file supersedes the initial screen and its ranking. Market values are mixed-book CBS, NOT executable offers. Large gaps are research priorities, not model edges.

Numerical frozen games 51/64; excluded/nonnumeric 13/64.

| Game | Frozen projected home spread | CBS home spread | Absolute gap | CBS away/home spread mismatch |
|---|---:|---:|---:|---:|
| Wake Forest @ Georgia Tech | -5.5 | 20.5 | 26.0 | 0.0 |
| Wofford @ Ole Miss | -23.5 | -48.5 | 25.0 | 1.0 |
| Arizona @ Kansas State | -13.8 | 7.5 | 21.3 | 0.0 |
| Middle Tennessee @ Sam Houston | -13.7 | 6.5 | 20.2 | 0.5 |
| Maryland @ USC | -1.6 | -17.5 | 15.9 | 0.0 |
| Colorado State @ Fresno State | -3.8 | -19.5 | 15.7 | 1.0 |
| NC State @ Florida State | 4.4 | -10.5 | 14.9 | 0.0 |
| Arkansas State @ Louisiana Tech | -0.4 | -14.5 | 14.1 | 0.0 |
| Washington State @ Texas State | -0.1 | -13.5 | 13.4 | 0.0 |
| Texas Tech @ Baylor | -8.1 | 5.0 | 13.1 | 0.5 |
| UNLV @ San José State | -6.5 | 6.5 | 13.0 | 0.0 |
| Georgia State @ Marshall | 10.3 | -2.5 | 12.8 | 0.0 |
| Oregon @ Michigan State | 5.1 | 17.5 | 12.4 | 0.0 |
| Colorado @ Cincinnati | -14.4 | -2.5 | 11.9 | 0.5 |
| Georgia @ South Carolina | 3.2 | 15.0 | 11.8 | 0.5 |
| Georgia Southern @ Troy | -2.1 | 9.5 | 11.6 | 0.5 |
| Bowling Green @ Toledo | -28.0 | -16.5 | 11.5 | 0.0 |
| South Florida @ Florida Atlantic | 12.7 | 1.5 | 11.2 | 0.5 |
| LSU @ Tennessee | -9.6 | 1.5 | 11.1 | 0.5 |
| UL Monroe @ App State | -24.5 | -13.5 | 11.0 | 0.5 |
| North Texas @ Tulane | -2.6 | 6.5 | 9.1 | 0.0 |
| SMU @ Notre Dame | -11.6 | -20.5 | 8.9 | 0.0 |
| Pittsburgh @ Louisville | -4.7 | -13.5 | 8.8 | 0.5 |
| Virginia Tech @ Miami | -12.0 | -20.5 | 8.5 | 0.0 |
| Ohio State @ Nebraska | -4.9 | 3.5 | 8.4 | 0.0 |
| Iowa @ Illinois | 1.2 | 9.0 | 7.8 | 0.5 |
| Houston @ West Virginia | 0.5 | 7.5 | 7.0 | 0.0 |
| Iowa State @ UCF | -5.2 | 1.5 | 6.7 | 0.5 |
| San Diego State @ Boise State | -10.9 | -17.5 | 6.6 | 0.0 |
| UCLA @ Michigan | -3.0 | 3.5 | 6.5 | 0.0 |
| North Carolina @ Virginia | -7.2 | -1.5 | 5.7 | 0.0 |
| South Alabama @ Southern Miss | -2.0 | 3.5 | 5.5 | 0.0 |
| Utah @ TCU | 2.2 | 7.5 | 5.3 | 0.5 |
| Hawai'i @ Nevada | -10.1 | -5.5 | 4.6 | 0.0 |
| Kentucky @ Missouri | -8.1 | -4.5 | 3.6 | 0.0 |
| Utah State @ Oregon State | -11.4 | -8.0 | 3.4 | 0.5 |
| Wisconsin @ Purdue | 2.6 | 6.0 | 3.4 | 0.5 |
| Delaware @ New Mexico State | 0.1 | 3.5 | 3.4 | 0.5 |
| Missouri State @ Jacksonville State | -7.9 | -10.5 | 2.6 | 0.0 |
| Oklahoma State @ Arizona State | 0.1 | 2.5 | 2.4 | 0.0 |
| Northern Illinois @ North Dakota State | -22.3 | -24.5 | 2.2 | 0.5 |
| Charlotte @ Tulsa | -20.4 | -22.5 | 2.1 | 0.0 |
| Texas A&M @ Oklahoma | -8.9 | -7.0 | 1.9 | 0.5 |
| Vanderbilt @ Florida | -15.3 | -13.5 | 1.8 | 0.0 |
| Syracuse @ Boston College | 0.9 | 2.5 | 1.6 | 0.0 |
| Old Dominion @ UConn | -11.9 | -13.5 | 1.6 | 0.0 |
| UTEP @ Air Force | -20.4 | -21.5 | 1.1 | 0.5 |
| Florida International @ Kennesaw State | -3.5 | -2.5 | 1.0 | 0.0 |
| Arkansas @ Texas | -21.2 | -20.5 | 0.7 | 0.0 |
| BYU @ Kansas | 6.4 | 6.0 | 0.4 | 0.5 |
| New Mexico @ Wyoming | 9.3 | 9.5 | 0.2 | 1.0 |

Nonnumeric frozen games: Clemson @ Duke; Northwestern @ Minnesota; Memphis @ Navy; East Carolina @ Army; Tennessee Tech @ Mississippi State; Western Kentucky @ Liberty; Chattanooga @ Alabama; Coastal Carolina @ Louisiana; Rutgers @ Penn State; Indiana @ Washington; Samford @ Auburn; Stanford @ California; UTSA @ UAB.

No model re-run, personnel gate acceptance, venue offer or production Hot Sheet promotion.