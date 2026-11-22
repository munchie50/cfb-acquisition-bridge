# Week12 Old Dominion @ UConn — CBS internally contradictory final, QA quarantine

Status: SOURCE_CONFLICT_UNRESOLVED / DO_NOT_ACCEPT_GAME_401861968_IN_CANONICAL_SCORECARD.

## Direct source readback
CBS game-specific box score: https://www.cbssports.com/college-football/gametracker/boxscore/NCAAF_20261121_ODU@UCONN/
- Header score and Week12 aggregate CBS scoreboard: Old Dominion 20, UConn 29.
- Associated Press recap embedded in the **same CBS page**, dated Nov21 2026: states UConn defeated Old Dominion 29–21, including a late Old Dominion touchdown.
- Thus CBS header vs CBS AP recap disagree by one point. These are NOT two independently authenticated final results. Previous NCAA spotcheck also reported 21–29, but its exact independently captured game-level source payload has not been durably preserved here.
- The score candidate currently uses 20–29 as a **CBS scoreboard value**, not certified official score. Its game row 401861968 must be quarantined for official acceptance until independently verified via a primary official team/NCAA game-level record.

## Other conflict resolved within CBS
Arizona at Kansas State game-specific box score https://www.cbssports.com/college-football/gametracker/boxscore/NCAAF_20261121_ARIZ@KSTATE/ shows Arizona 35, Kansas State 28, FINAL/OT; recap also reports Arizona 35–28. Kansas State +10 conditional ticket remains WIN, cover margin +3.

## Derived-metric sensitivity
- Published Week12 56-modeled QA candidate currently assumes Old Dominion 20 at UConn 29; modeled 43/56 winner direction, margin MAE 13.718254103895376, total MAE 11.627854203068864, Brier 0.19718225044930882.
- Under alternate Old Dominion 21 at UConn 29, the single modeled game's realized home margin changes 9 -> 8 and total changes 49 -> 50. Winner direction and Brier are unchanged. Recomputed directly from the current corrected Arizona cohort with only Old Dominion changing to 21: winner direction 43/56, margin MAE 13.736111246752518, total MAE 11.611958254609503, Brier 0.19718225044930882. These are sensitivity figures only, not accepted metrics.
- No Nov21 ticket concerns Old Dominion at UConn, so conditional ticket outcomes are unaffected.
- This quarantine is a scoped QA hold, not a rollback of CBS scoreboard extraction or an assertion of an official result.

## First unfinished action
Obtain primary UConn/Old Dominion official game boxscore or NCAA gamecenter final with score and stable game ID. Recompute only affected metric row and supersede this quarantine with an independently evidenced decision. Keep canonical scorecard and book settlement unchanged.


## Nov22 resolution — supersedes quarantine
- NCAA official game-specific https://www.ncaa.com/game/6604217 confirms Old Dominion 21, UConn 29, FINAL; quarter sums ODU 0+14+0+7=21 and UConn 14+6+6+3=29.
- Independent ESPN game 401861968 also reports 21-29. CBS page header/aggregate 20-29 is a one-point source defect; CBS AP recap says 29-21. Resolved in favor of NCAA official primary game record.
- Corrected candidate source blob 548b1a19f337e00a0a18b8ee8fa45345cd959ce3 commit c66d82835376653552a58f9f6e45c8164eb2f45c. 70/70 CBS event joins remain, with explicit NCAA official override on game 401861968.
- Recomputed frozen scoring candidate blob 148e06da9a1cdcbe45cefd5af43843f7c3deb473 commit ea8e911101a72f345a637ff4a1db3913b3789549: 43/56 winner direction, margin MAE 13.736111246752518, total MAE 11.611958254609505, Brier 0.19718225044930882.
- Rebound ticket candidate blob 8b9018d1a3015281a91547c976855c5d794800d3 commit 048f3e8f51f000b0a6661c4eebfcc5bd91e868b2. No ticket covers this game; 5 conditional wins / 8 losses, $75 stakes unchanged. Actual settlement remains unverified.
- SHA-guarded writes and independent exact content readbacks passed. Quarantine is RESOLVED_FOR_SOURCE_FINAL_QA, NOT automatic canonical scorecard acceptance. Freeze provenance acceptance still open.
