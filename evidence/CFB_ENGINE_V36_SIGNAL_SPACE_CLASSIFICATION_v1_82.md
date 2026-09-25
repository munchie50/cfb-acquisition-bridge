# CFB Engine V36 Residual Signal-Space Classification — v1.82
Date: 2026-09-25
Status: bounded diagnostic checkpoint; no V37 and no semantic/model/source/gate/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.81. Used the preserved V36 all-offensive-row diagnostic for the original replay=0 / official=1 missing-target population to determine whether missing losses sit outside the current raw-fumble detector but inside broader text/possession signal space.

## Preserved all-offensive-row diagnostic
For the 99 original missing-candidate targets, V36 preserved 3,211 target offensive rows and 284 broad signal rows.

Signal definition in V36:
- text contains fumb / muff / recover, OR
- already-detected fumble, OR
- change_of_poss > 0, OR
- change_of_pos_team > 0.

The 284 signal rows decompose as:
- already-detected fumble: 151
- text fumble/recovery signal: 118
- possession-change signal: 177
- possession-change signal with neither text signal nor detected fumble: 107

Those 107 possession-only rows are the only broad-signal class that is definitely outside both the existing raw-fumble detector and explicit fumble/recovery text.

## Interpretation
This establishes that the residual search space is not exhausted by the current raw-fumble candidate set: the frozen source contains a substantial possession-change-only population within the target offensive rows.

However, possession change is not synonymous with fumble loss. It also includes ordinary turnovers/drive transitions and other events. Therefore the 107 rows are a diagnostic candidate space only, not evidence for a new turnover rule.

The next bounded test should classify those 107 possession-only rows by play_type/text/event context and determine whether any semantically explicit fumble-loss subtype exists independently of the official aggregate target. A rule must be derivable from play evidence first and only then evaluated against control.

## Consequence
v1.81 showed no simple alternate raw-fumble reassignment. v1.82 now identifies the next authentic occurrence-recovery substrate: possession-change-only rows outside current fumble/text detection.

Do not launch V37 by broadening fumble occurrence to all possession-change rows. That would be target fitting and would confound fumbles with other possession transitions.

RAW_TURNOVER_RATE remains OPEN.

## Governance
V36 frozen inputs/artifact remain the evidence substrate. v1.81 readback verified before this checkpoint.
Latest integrated Library ZIP remains v1.73; v1.74-v1.82 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
Primitive Historical Coverage Gate OPEN. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
