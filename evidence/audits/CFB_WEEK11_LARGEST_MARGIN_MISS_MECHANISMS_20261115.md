# Week 11 largest frozen margin errors — two-case diagnosis

Scope: the two largest absolute margin errors from the [67-game triage](CFB_WEEK11_FROZEN_MODEL_MISS_TRIAGE_20261115.json), blob `3462a0388ee573931700b647ab4e8f180cadd9a4`. Errors are realized home margin minus frozen home margin. This is a retrospective mechanism check. It preserves the contemporaneous PASS on both games.

| Game | Frozen call | Final | Signed margin error |
|---|---|---|---:|
| Colorado State at Washington State | Washington State by 1.95 | Washington State 73–7 | +64.05 |
| Wake Forest at SMU | SMU by 9.90 | Wake Forest 49–7 | −51.90 |

## Colorado State at Washington State

The saved pregame review recognized Colorado State's weak defense and tempered the favorite's range because of Washington State's finishing. CBS had restored the market display, but the opposite spread rows showed different numbers and no limit was earned. The frozen winner direction was correct while the model underestimated the margin by 64.05 and the total by 29.70.

Washington State's recap reports 535 rushing yards, nine rushing touchdowns, eight red-zone scores, and only 61 rushing yards allowed. That supports a large realized rushing and finishing gap. The team's season-high rushing and touchdown output is reason to test whether this was foreseeable across similar cases. It does not establish that the extreme outcome should have been forecast.

QA next test: in a matched sample with pregame defensive rushing weakness and conflicting favorite finishing signals, compare expected and realized rushing efficiency and finishing. Include ordinary wins and failed covers. Keep separate whether a reliable pregame number and price was available. [Washington State recap](https://wsucougars.com/news/2026/11/14/washington-state-rolls-to-73-7-win-over-colorado-state)

## Wake Forest at SMU

The pregame review knew Gio Lopez was probable. It flagged uncertainty about his role, SMU personnel and mismatched market numbers. The final margin reversed the favorite, but the combined 56 points were only 5.40 below the frozen total. The major error was which team scored the points.

Wake Forest built a 42–7 halftime lead, forced three turnovers and held SMU to 275 total yards. Lopez contributed a 44-yard touchdown pass. Wake's opening scores also used the running game, and a fourth-down stop deep in SMU territory preceded its second touchdown. The official game evidence supports multiple mechanisms beyond quarterback availability. It does not resolve how far the pregame model should have moved once Lopez was probable.

QA next test: for comparable documented pregame quarterback role changes, assess both team scoring projections and winner direction separately from total. Count games where the original favorite held and cases where the role became clear too late. Preserve the market and practical deadline constraints. [Wake Forest recap](https://godeacs.com/news/2026/11/14/football-rushing-attack-dominant-defensive-effort-power-no-13-wake-forest-past-smu-49-7) · [Official box score](https://godeacs.com/sports/football/stats/2026/smu/boxscore/14641)

Disposition: two mechanism diagnoses completed. Original model inputs, causal attribution, matched controls, and prospective discrimination remain open. No recommendation, source acceptance, or threshold change.
