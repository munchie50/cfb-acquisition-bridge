# CFB Engine — 2025 Holdout Substrate Recovery v1.145

Status: PRE-OUTCOME HOLDOUT PREPARATION BLOCKED AT FEATURE SUBSTRATE
Parent: v1.144 market diagnostic preflight
No 2025 outcomes scored or inspected for model evaluation.

## Recovery performed
The exact accepted feature artifacts used by the v1.131 frozen Challenger-A dataset were independently downloaded again:
- mechanical artifact 10890704969
- derived artifact 10891634424

Their retained feature tables were inspected directly.

Mechanical accepted feature canary:
- 12,718 team-game rows
- seasons present: 2016–2024 only
- 2025 rows: 0

Derived accepted feature canary:
- 12,718 team-game rows
- seasons present: 2016–2024 only
- 2025 rows: 0

Therefore the accepted v1.131/v1.140 feature substrate cannot simply be filtered forward to produce 2025 holdout predictions. The earlier full-season producer evidence that 762 2025 game IDs exist does not establish that the exact accepted 17-feature Challenger-A representation has been generated for those games.

## Classification
2025 prediction freeze is BLOCKED at exact accepted-feature generation, not at model scoring and not at authorization.

Do not:
- use 2025 outcomes to backfill or debug features;
- substitute a different feature producer;
- infer that 2025 full-season game-ID coverage equals Challenger-A feature coverage;
- join market information;
- score 2025 outcomes.

## Required next proof
Recover the executable ancestry for the accepted v1.109 mechanical and v1.115 derived feature producers, then determine whether those exact frozen definitions can be run prospectively for 2025 from pregame/strictly-prior information without outcome leakage.

If executable ancestry is recoverable:
1. freeze a 2025-only feature-generation contract using the unchanged v1.123 definitions;
2. generate team-game features without targets/outcomes;
3. verify exact game/team identity, missingness, temporal availability and no market fields;
4. construct one game row using frozen v1.130 representation;
5. apply the already-selected Challenger-A model/scaling without refitting;
6. durably freeze predictions;
7. independently audit;
8. only then request/record the separate authorization required by v1.143 before outcome scoring.

If exact executable ancestry is not recoverable, preserve the blocker and do not reconstruct feature semantics from observed 2025 outcomes.

Locks unchanged: production v1 champion; Challenger A shadow; 2025 TEST unscored; no market join; no promotion.
