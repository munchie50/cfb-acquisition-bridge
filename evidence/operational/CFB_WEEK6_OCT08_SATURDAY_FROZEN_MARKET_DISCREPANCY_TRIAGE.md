# Week 6 Saturday — frozen/market discrepancy triage (Test Routine v6)

Status: research triage only; **NO betting edge, recommendation or calibrated EV certified**.

Sources: Oct 8 Saturday source audit (GitHub blob cab9d35705d3b260d8a1e84f9e38cbe56e01b567); corrected 38/38 matchup identity audit (blob 52c1921768058e2025e4f2307a2cba9338da7a75). ESPN odds board displayed linked DraftKings prices; no Caesars executable quotes or independent price timestamps verified.

Method: compare absolute magnitude of frozen favorite margin against displayed sportsbook favorite spread. Raw gap = |frozen margin| − |market favorite spread|. Direction conflict means the predicted favorite name differs from the market favorite name. This comparison is **not** a side-specific cover probability, expected value or bet selection, especially for opposite-favorite games. No acceptance threshold is inferred.

- Compared: 38/38
- Frozen favorite differs from market favorite: 11
- Raw absolute gap >= 10 points: 6

| Kickoff CT | Matchup | Frozen predicted favorite | DK market favorite | DK linked away/home spreads | Absolute raw gap | Favorite conflict |
|---|---|---|---|---|---:|---|
| Sat 11:00 AM | Arizona @ West Virginia | West Virginia -3.4 | Arizona -3 | -3 (-115) / +3 (-105) | 0.4 | YES |
| Sat 11:00 AM | Texas A&M @ Missouri | Missouri -7.7 | Missouri -3.5 | +3.5 (-115) / -3.5 (-105) | 4.2 | no |
| Sat 11:00 AM | UCF @ Oklahoma State | Oklahoma State -4.3 | Oklahoma State -10.5 | +10.5 (-108) / -10.5 (-112) | -6.2 | no |
| Sat 11:00 AM | North Carolina @ Pittsburgh | Pittsburgh -8.3 | Pittsburgh -3.5 | +3.5 (-108) / -3.5 (-112) | 4.8 | no |
| Sat 11:00 AM | Wake Forest @ NC State | NC State -9.3 | Wake Forest -3.5 | -3.5 (-105) / +3.5 (-115) | 5.8 | YES |
| Sat 11:00 AM | Sacramento State @ Bowling Green | Sacramento State -12.7 | Bowling Green -7.5 | +7.5 (-110) / -7.5 (-110) | 5.2 | YES |
| Sat 11:45 AM | South Carolina @ Florida | Florida -7.1 | Florida -11.5 | +11.5 (-112) / -11.5 (-108) | -4.4 | no |
| Sat 12:00 PM | Old Dominion @ App State | App State -14.3 | App State -9.5 | +9.5 (-105) / -9.5 (-115) | 4.8 | no |
| Sat 1:00 PM | Miami (OH) @ Massachusetts | Massachusetts -14.8 | Miami (OH) -2.5 | -2.5 (-108) / +2.5 (-112) | 12.3 | YES |
| Sat 2:30 PM | Texas @ Oklahoma | Oklahoma -3.4 | Texas -7.5 | -7.5 (-110) / +7.5 (-110) | -4.1 | YES |
| Sat 2:30 PM | UCLA @ Oregon | Oregon -5.1 | Oregon -11.5 | +11.5 (-110) / -11.5 (-110) | -6.4 | no |
| Sat 2:30 PM | Stanford @ Notre Dame | Notre Dame -27.6 | Notre Dame -39.5 | +39.5 (-115) / -39.5 (-105) | -11.9 | no |
| Sat 2:30 PM | Ole Miss @ Vanderbilt | Vanderbilt -1.9 | Ole Miss -9.5 | -9.5 (-108) / +9.5 (-112) | -7.6 | YES |
| Sat 2:30 PM | Illinois @ Michigan State | Illinois -4.4 | Illinois -2.5 | -2.5 (-120) / +2.5 (+100) | 1.9 | no |
| Sat 2:30 PM | Houston @ Kansas State | Kansas State -10.6 | Kansas State -2.5 | +2.5 (-105) / -2.5 (-115) | 8.1 | no |
| Sat 2:30 PM | Eastern Michigan @ Akron | Akron -11.1 | Eastern Michigan -6.5 | -6.5 (-118) / +6.5 (-102) | 4.6 | YES |
| Sat 2:30 PM | Duke @ Georgia Tech | Georgia Tech -0.9 | Duke -6.5 | -6.5 (-115) / +6.5 (-105) | -5.6 | YES |
| Sat 2:30 PM | Central Michigan @ Ohio | Central Michigan -1.1 | Ohio -3 | +3 (-112) / -3 (-108) | -1.9 | YES |
| Sat 2:30 PM | Charlotte @ North Texas | North Texas -7.8 | North Texas -28.5 | +28.5 (-108) / -28.5 (-112) | -20.7 | no |
| Sat 2:30 PM | Buffalo @ Toledo | Toledo -22.1 | Toledo -21 | +21 (-112) / -21 (-108) | 1.1 | no |
| Sat 2:30 PM | Kent State @ Western Michigan | Western Michigan -26.7 | Western Michigan -13.5 | +13.5 (+100) / -13.5 (-120) | 13.2 | no |
| Sat 3:00 PM | Rice @ East Carolina | East Carolina -0.4 | East Carolina -10 | +10 (-112) / -10 (-108) | -9.6 | no |
| Sat 3:15 PM | Maryland @ Ohio State | Ohio State -11.4 | Ohio State -32.5 | +32.5 (-110) / -32.5 (-110) | -21.1 | no |
| Sat 3:15 PM | Tennessee @ Arkansas | Tennessee -19.0 | Tennessee -13.5 | -13.5 (-110) / +13.5 (-110) | 5.5 | no |
| Sat 5:00 PM | San Diego State @ Oregon State | Oregon State -7.7 | Oregon State -15.5 | +15.5 (-108) / -15.5 (-112) | -7.8 | no |
| Sat 6:00 PM | Nevada @ UTEP | Nevada -5.1 | Nevada -10 | -10 (-108) / +10 (-112) | -4.9 | no |
| Sat 6:00 PM | North Dakota State @ UNLV | North Dakota State -8.7 | North Dakota State -3 | -3 (-118) / +3 (-102) | 5.7 | no |
| Sat 6:00 PM | LSU @ Kentucky | LSU -2.5 | LSU -8.5 | -8.5 (-112) / +8.5 (-108) | -6.0 | no |
| Sat 6:30 PM | Air Force @ Northern Illinois | Air Force -16.1 | Air Force -7.5 | -7.5 (-108) / +7.5 (-112) | 8.6 | no |
| Sat 6:30 PM | Syracuse @ Virginia | Virginia -10.1 | Virginia -10 | +10 (-110) / -10 (-110) | 0.1 | no |
| Sat 6:30 PM | James Madison @ Georgia Southern | James Madison -8.0 | James Madison -7.5 | -7.5 (-105) / +7.5 (-115) | 0.5 | no |
| Sat 6:30 PM | Georgia @ Alabama | Georgia -7.0 | Alabama -1.5 | +1.5 (-108) / -1.5 (-112) | 5.5 | YES |
| Sat 6:30 PM | Louisiana @ Louisiana Tech | Louisiana Tech -0.1 | Louisiana Tech -3 | +3 (-112) / -3 (-108) | -2.9 | no |
| Sat 6:30 PM | USC @ Penn State | Penn State -11.8 | Penn State -1.5 | +1.5 (-112) / -1.5 (-108) | 10.3 | no |
| Sat 7:00 PM | Minnesota @ Purdue | Minnesota -5.8 | Minnesota -2.5 | -2.5 (-110) / +2.5 (-110) | 3.3 | no |
| Sat 9:15 PM | Kansas @ Utah | Utah -18.9 | Utah -15.5 | +15.5 (-110) / -15.5 (-110) | 3.4 | no |
| Sat 9:30 PM | Hawai'i @ Arizona State | Arizona State -14.1 | Arizona State -20.5 | +20.5 (-105) / -20.5 (-115) | -6.4 | no |
| Sat 9:30 PM | Boise State @ Fresno State | Fresno State -1.6 | Boise State -6.5 | -6.5 (-110) / +6.5 (-110) | -4.9 | YES |

## Highest-priority manual data/football review (not bets)
- Maryland @ Ohio State: frozen Ohio State -11.4, market Ohio State -32.5; raw magnitude gap -21.1; favorite conflict no.
- Charlotte @ North Texas: frozen North Texas -7.8, market North Texas -28.5; raw magnitude gap -20.7; favorite conflict no.
- Kent State @ Western Michigan: frozen Western Michigan -26.7, market Western Michigan -13.5; raw magnitude gap 13.2; favorite conflict no.
- Miami (OH) @ Massachusetts: frozen Massachusetts -14.8, market Miami (OH) -2.5; raw magnitude gap 12.3; favorite conflict YES.
- Stanford @ Notre Dame: frozen Notre Dame -27.6, market Notre Dame -39.5; raw magnitude gap -11.9; favorite conflict no.
- USC @ Penn State: frozen Penn State -11.8, market Penn State -1.5; raw magnitude gap 10.3; favorite conflict no.
- Rice @ East Carolina: frozen East Carolina -0.4, market East Carolina -10; raw magnitude gap -9.6; favorite conflict no.
- Air Force @ Northern Illinois: frozen Air Force -16.1, market Air Force -7.5; raw magnitude gap 8.6; favorite conflict no.
- Houston @ Kansas State: frozen Kansas State -10.6, market Kansas State -2.5; raw magnitude gap 8.1; favorite conflict no.
- San Diego State @ Oregon State: frozen Oregon State -7.7, market Oregon State -15.5; raw magnitude gap -7.8; favorite conflict no.

## Decision gate
No automatic BET NOW/BET EARLY. Need verified live executable Caesars prices, preserved acceptable cutoffs, injuries/roster/football reconciliation, maturity and cutoff checks, and portfolio-trip review before any recommendation. Do not mutate frozen predictions, backfill after kickoff, or count this research audit as production completion.
