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
- Under alternate Old Dominion 21 at UConn 29, the single modeled game's realized home margin changes 9 -> 8 and total changes 49 -> 50. Winner direction and Brier are unchanged. Margin MAE changes to 13.486111246752518 only if all else held fixed? NO: that number came from a previous candidate where Arizona was reversed; do not reuse it. Recompute alternate-cohort metrics directly from current 70/70 candidate before any publication.
- No Nov21 ticket concerns Old Dominion at UConn, so conditional ticket outcomes are unaffected.
- This quarantine is a scoped QA hold, not a rollback of CBS scoreboard extraction or an assertion of an official result.

## First unfinished action
Obtain primary UConn/Old Dominion official game boxscore or NCAA gamecenter final with score and stable game ID. Recompute only affected metric row and supersede this quarantine with an independently evidenced decision. Keep canonical scorecard and book settlement unchanged.
