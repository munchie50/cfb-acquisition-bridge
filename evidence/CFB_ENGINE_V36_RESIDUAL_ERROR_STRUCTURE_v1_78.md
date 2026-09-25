# CFB Engine V36 Residual Error Structure — v1.78
Date: 2026-09-25
Status: bounded audit checkpoint; no V37, no semantic/model/source/gate/production promotion.

## Test-routine selection
After v1.74-v1.77 converted four non-executable branches into explicit evidence boundaries, global dependency reconsideration selected RAW_TURNOVER_RATE / V36 because it retains executable preserved inputs and a non-expired workflow artifact.

## Evidence readback
- Workflow commit: c9f30bdce6c145188191e53797022e971edf4e24
- Run: 36188441197
- Artifact: 10886388130, cfb-2022-giveaway-replay-v36
- Artifact digest: sha256:b8b8dbf0d1bc35f967c21e85d92bd3ba14d29ab951d6190ed2cd64d1a267df21
- Frozen replay RDS SHA-256: dcf59fe1f694c5eaef0ce89d1ce14dbcbe571c60fa7d94f40399e50c9a38ea8a
- Frozen ESPN team-box SHA-256: f0254f784613d3918315f3cd1998ca3cbaf90fe39165ee9d6b05ed13fe88a239

Downloaded and directly audited the preserved V36 artifact instead of launching V37.

## Reproduced reconciliation
Official-control comparable population: 1,792 team-games.

Baseline V36 artifact official summary:
- interceptions exact: 1,699 / 1,792 = 94.81%, aggregate delta -2
- fumbles_lost exact: 1,491 / 1,792 = 83.20%, aggregate delta -225
- giveaways exact: 1,428 / 1,792 = 79.69%, aggregate delta -227

Conservative shadow recomputed from artifact:
- fumbles_lost exact: 1,552 / 1,792 = 86.61%, aggregate delta -137
- giveaways exact: 1,488 / 1,792 = 83.04%, aggregate delta -139

## New residual structure
For conservative-shadow fumbles_lost, 240 / 1,792 comparable team-games remain non-exact:
- 183 under official control
- 57 over official control
- residual difference distribution: -3: 2; -2: 19; -1: 162; +1: 49; +2: 4; +3: 4
- these 240 mismatches occur across 215 games
- 190 games have only one mismatching team side
- 25 games have both team sides mismatching
- only 14 games contain residual mismatches in both directions (one under and one over)
- 10 mismatch games have net-zero game-level residual

## Classification / consequence
The remaining V36 error is not predominantly a simple within-game side swap. Most mismatch games have only one mismatching side, and the residual population is strongly undercount-skewed (183 under vs 57 over). That argues against spending the next iteration primarily on generic team-side reassignment.

This does NOT authorize a new occurrence rule. It narrows the next evidence question: inspect the residual undercount population for common event/occurrence classes while separately guarding against the 57 overcounts. Any V37 must be justified by a bounded semantic hypothesis that improves the residual without relaxing the frozen controls.

RAW_TURNOVER_RATE remains OPEN.

## Governance
Latest integrated Library ZIP remains v1.73. Repository v1.74-v1.77 are bounded evidence checkpoints; this v1.78 is likewise bounded repository evidence.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
Primitive Historical Coverage Gate OPEN. Prediction cutoff UNKNOWN/fail-closed. Second-order opponent-adjusted lineage is an unrecovered evidence boundary.
No fitting/tuning/source/model/production promotion.
