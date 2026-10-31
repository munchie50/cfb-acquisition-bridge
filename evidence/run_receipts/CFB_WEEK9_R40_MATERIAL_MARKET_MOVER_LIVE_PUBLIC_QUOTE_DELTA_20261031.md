# CFB Week 9 R40 — follow-on 16-case saved-drift queue, current same-public-page price observations
**RUN_INCOMPLETE — no new approved bets, certified decision rows, review packets, or Hot Sheet.**
Recorded 2026-10-31T04:54:21.758Z UTC. This is an observation/receipt clock, not an operator price-update timestamp.

## Continuation after independently verified R39
- R39 receipt `evidence/run_receipts/CFB_WEEK9_R39_LIVE_SATURDAY_MARKET_AND_OFFICIAL_STATUS_RECHECK_20261031.md`, blob `1e6375a9a66b702f1b58b28ad3dd656cb8ed42ea`, commit `1a0b8edeee796d64e5088a25781b769ff0a01011`, independently re-fetched; its only changed path was that receipt. Five protected canonical blobs independently read back unchanged (see R39 readback).
- The R26 frontier contains **16** previously flagged material saved-mixed-book drift cases; **one** (Kent State @ Sacramento State, 401866451) expired by kickoff 2026-10-31T02:30Z and remains **EXPIRED_NO_RETROACTIVE_APPROVAL**.
- R39 freshly checked four of the 15 still-future flagged cases: Bowling Green/Western Michigan, Auburn/Ole Miss, UConn/Air Force, Ohio State/USC. R40 independently checked the **remaining 11** future flagged cases using the **same FanDuel public team-page URLs** recorded in R26. All fresh retrievals completed 2026-10-31T04:54:00Z–04:54:06Z; all are *public displays only*, no user-authenticated execution offer, stake limit or operator update clock.
- Together R39+R40 cover **15/15 unexpired material-flag cases**, with Kent State separately closed. This does **not** certify that the original CBS mixed-book-to-current comparisons were temporal moves.

## Actual new same-public-page quote differences since R26 (prior retrieval by 2026-10-31T03:16:55.476Z)
1. **Florida @ Georgia (401856734)**: public FanDuel away Florida ML **+340 -> +360**, home Georgia ML **-450 -> -465**; spreads unchanged +11.5/-110 and -11.5/-110; total unchanged 56.5/-110 both directions. Fresh scrape `01a1904e-b85d-76c8-ac5d-b496976fb396`, https://sportsbook.fanduel.com/teams/college-football/florida-gators/odds . These are *observed differences between two retrievals of the same public page*, NOT verified operator update timestamps or executable prices. Both moneyline branches remain **NOT_CERTIFIED**, material SEC personnel and venue proof outstanding.
2. **Miami @ North Carolina (401858282)**: public FanDuel away Miami ML **-600 -> -580**, home UNC ML **+450 -> +440**; spreads unchanged Miami -14.5/+100, UNC +14.5/-122; total unchanged 53.5/-110 both directions. Fresh scrape `01a1904e-c173-732e-a4ac-0c3cd03bd47d`, https://sportsbook.fanduel.com/teams/college-football/north-carolina-tar-heels/odds . Same public-page observation qualification only; no current Champion betting approval.

## Other nine checked cases (all displayed fields numerically unchanged versus R26)
| Game ID | Game | Fresh scrape ID | Six public branches |
|---|---|---|---|
| 401860910 | Colorado State @ Utah State | 01a1904e-b85c-716d-92c4-b7767a0d1b4a | unchanged |
| 401864531 | UTEP @ North Dakota State | 01a1904e-b85b-75a4-8cc8-f2b3e565d4b3 | **unavailable all six** |
| 401864529 | New Mexico @ San José State | 01a1904e-b86a-726b-b7de-0f22a981c127 | unchanged |
| 401858508 | Nevada @ UCLA | 01a1904e-b868-7048-aded-91deb9333eb5 | unchanged |
| 401858506 | Purdue @ Penn State | 01a1904e-bfc7-714e-9be3-77c0dfa4aa66 | unchanged |
| 401856737 | Mississippi State @ Texas | 01a1904e-c089-7675-a53d-3bdf014f2746 | unchanged; QB change still material |
| 401856733 | Missouri @ Arkansas | 01a1904e-c129-760f-be40-80068ddd4ddc | unchanged |
| 401860908 | Texas State @ Boise State | 01a1904e-c17f-73c0-a076-3de68c75108b | unchanged |
| 401864530 | Northern Illinois @ UNLV | 01a1904e-c64e-7713-bc5e-f33349b7b4c6 | unchanged |

**R40 scope:** 11 future flagged cases, 10 populated public six-branch displays (60 observed branches), one unavailable. Four ML prices changed across two games; 56 other populated public branch displays unchanged. None earned authentic current Champion decision or packet certification. Existing R28 cross-book numeric reconciliation remains distinct from this later *same-public-page observed change*.

## Attempt ledger and exact blockers
| Action | Outcome | Blocker | Next eligible action |
|---|---|---|---|
| R39 independent receipt and protected artifact readback | PASS; only R39 receipt changed | No new current decisions | Advance next independent backlog branch |
| R26 material-flag list crosswalk | 16 unique; 1 expired; 4 already rechecked in R39; 11 newly rechecked | Original cross-book drift is not proven temporal | Preserve source distinction |
| Eleven new live public FanDuel retrievals | 2 games with ML display differences; 8 other populated unchanged; UTEP display unavailable | Public page not executable venue; no operator update timestamp; missing calibrated review | Carry exact new public deltas to existing manual review, no betting inference |
| Authentic Champion six-market decision / 35 packet certification | 0 newly qualified | Qualified personnel, current decision reasoning, user venue quote/limit and final source freshness absent | Earn only with full gates |
| Guarded serial publication / CI | NOT ATTEMPTED | 56 genuine current decision rows and contract gates not satisfied | Never fabricate rows or become a second Hot Sheet producer |

**Original deadlines immutable:** Maryland +2.5 **NOT APPROVED**, Sat 2026-10-31T14:00Z; Ohio State-USC Under 51.5 **NOT APPROVED**, Sat 2026-10-31T20:00Z. Ohio State frozen Champion total 58.139 and accepted October27 total 56.417 both exceed 51.5. Air Force Medders OUT, replacement quarterback uncertified. All 16 material saved-drift case flags preserved. 35-case frontier retains 32 prospective manual preflights and three elapsed closures, zero new certified packets or decisions. Original Champion, betting limits, four standing task schedules and five protected production artifacts unchanged.

**Next entry:** Maryland original 14:00Z conditional and earliest Saturday case qualification, then Air Force personnel impact, then Ohio State-USC 20:00Z. Monitor only new authoritative personnel/market changes and seek actual venue offer/limit; do not replay prior preflights or historical normalization. When no useful authorized Week9 recovery remains, explicitly recommend disabling temporary rescue task; do not alter four standing tasks.

**Terminal: RUN_INCOMPLETE. Independent readback required.**
