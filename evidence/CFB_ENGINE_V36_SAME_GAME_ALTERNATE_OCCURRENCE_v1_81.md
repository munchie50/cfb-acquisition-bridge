# CFB Engine V36 Same-Game Alternate Occurrence Diagnostic — v1.81
Date: 2026-09-25
Status: bounded diagnostic checkpoint; no V37 and no semantic/model/source/gate/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.80. For the 46 replay=0 / official=1 target team-games whose target-role candidate fumbles explicitly resolve as same-team recoveries, searched the preserved V36 same-game raw-fumble diagnostic for alternate fumble rows outside the target-role candidates.

## Population
- target team-games: 46
- same-game raw fumble rows represented in the preserved diagnostic: 87
- target-role rows: 68
- alternate/non-target-role rows: 19

Alternate rows occur in only 15 of the 46 target team-games.
Therefore 31/46 target team-games have no alternate raw-fumble row in the preserved same-game diagnostic.

## Alternate-row classification
Of the 19 alternate rows:
- 13 have no explicit recovery mention
- 6 have explicit recovery text
- 6 have coposs TRUE
- 13 have coposs FALSE
- 5 are already classified as a fumble loss for some side by the frozen V36 semantics
- 14 are not classified as a loss

Only 2/19 alternate rows have both explicit recovery text and coposs TRUE.
No alternate row provides the simple missing pattern "explicit recovery to the target opponent + possession change" in a way that can be safely promoted into a generic correction from this artifact alone.

## Consequence
The search does not recover an obvious hidden opponent-recovery event for most of the 46 contradictory target team-games:
- 31/46 have no alternate raw-fumble candidate at all in the same-game diagnostic.
- The 15 with alternate rows are heterogeneous and include rows already assigned to other sides/events.
- The preserved artifact therefore does not support forcing the 46 official undercounts into the replay through a simple alternate-row reassignment rule.

This narrows the branch further. The remaining discrepancy may involve occurrence detection outside the current raw-fumble candidate definition, aggregate-control/source semantic differences, or both. Any next semantic change requires a new bounded occurrence hypothesis tied to raw play evidence, not control-target fitting.

RAW_TURNOVER_RATE remains OPEN.

## Governance
V36 frozen inputs/artifact remain the evidence substrate. v1.80 readback verified before this checkpoint.
Latest integrated Library ZIP remains v1.73; v1.74-v1.81 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
Primitive Historical Coverage Gate OPEN. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
