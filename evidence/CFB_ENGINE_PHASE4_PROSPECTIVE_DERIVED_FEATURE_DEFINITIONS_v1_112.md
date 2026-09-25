# CFB Engine — Phase 4 Prospective Derived Feature Definition Contract v1.112

Date: 2026-09-25
Status: FROZEN FOR SEMANTIC CANARY — CHALLENGER/SHADOW ONLY
Predecessor: CFB_ENGINE_PHASE4_DERIVED_FEATURE_DEFINITION_BOUNDARY_v1_111.md
Production effect: NONE
Model fitting/tuning: NOT AUTHORIZED
2025 TEST: EXCLUDED

## Authority and purpose
The frozen Phase 4 inventory requires explosiveness, down/situation efficiency, finishing drives, and field position, while explicitly requiring their definitions to be frozen before tuning. No authoritative historical artifact supplies exact formulas. This checkpoint therefore makes prospective football-semantic definition choices before any model-performance inspection.

These are feature definitions, not fitted weights, priors, shrinkage, or promotion decisions.

## Common population and timing
Use only eligible offensive scrimmage plays from completed prior games in the same season. Opening game of each season has no prior-game feature history. Punts and other special-teams plays are excluded from scrimmage denominators. Null required context makes that play ineligible for the affected derived feature; do not zero-fill missing context. 2025 is excluded.

## D1 — Explosiveness
An eligible offensive scrimmage play is explosive when yards_gained >= 20.
Features:
- offensive_explosive_play_rate = explosive offensive scrimmage plays / eligible offensive scrimmage plays
- defensive_explosive_play_rate = opponent explosive scrimmage plays allowed / eligible opponent scrimmage plays
Rationale: one simple threshold avoids separate rush/pass threshold tuning in the first challenger. Threshold is frozen prospectively, not selected from validation performance.

## D2 — Success rate
For an eligible offensive scrimmage play with non-null down, distance, and yards_gained:
- 1st down success: yards_gained >= 0.50 * distance
- 2nd down success: yards_gained >= 0.70 * distance
- 3rd or 4th down success: yards_gained >= distance
Features:
- offensive_success_rate = successful eligible offensive plays / context-qualified eligible offensive plays
- defensive_success_rate_allowed = opponent successful plays / context-qualified opponent plays
No standard-down/passing-down split is authorized in this version; that would require an additional situational-definition freeze.

## D3 — Finishing drives
A scoring opportunity is a drive on which the offense has at least one context-qualified play with yards_to_goal <= 40.
A qualifying drive is counted once regardless of repeated plays inside the 40.
Drive points are the offense's points scored on that drive, derived only from validated drive/play scoring semantics. Do not infer points from final game score allocation.
Feature:
- points_per_scoring_opportunity = sum qualifying-drive offensive points / number of qualifying scoring-opportunity drives.
Until drive-point derivation passes semantic canary, this feature remains DEFINITION_FROZEN / EXECUTION_PENDING.

## D4 — Field position
For each offensive drive, starting field position is the yards_to_goal on the earliest valid offensive play in that drive.
Exclude drives with no valid drive_id or no valid starting yards_to_goal.
Feature:
- average_starting_yards_to_goal = mean starting yards_to_goal across qualified prior offensive drives.
Lower values mean better starting field position. No inversion or normalization is authorized in this version.

## Missing data
Zero denominator => NA. Missing required play/drive context excludes that observation only from the affected feature denominator and must be counted in diagnostics.

## Canary acceptance requirements
Before these features can join the deterministic feature dataset:
1. audit 2016-2024 field/context coverage by season;
2. prove drive_id and yards_to_goal produce stable drive-start identities;
3. prove scoring-opportunity drive deduplication;
4. independently reproduce sampled explosiveness, success, and field-position rows;
5. independently reproduce finishing-drive rows only after drive-point semantics are validated;
6. confirm zero 2025 rows and season-reset behavior.

No model outcome, validation metric, market value, or 2025 result may be used to alter these definitions within v1.112.
