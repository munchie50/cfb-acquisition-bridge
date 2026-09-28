# CFB QA Sandbox — Historical Outcome Evaluation Authorization — 2026-09-28

Status: AUTHORIZED — BOUNDED HISTORICAL SCORING ONLY
Production effect: NONE
Champion effect: NONE
2025 protected TEST access: FORBIDDEN
Market/wager/execution input access: FORBIDDEN
Candidate mutation/refit/promotion: NOT AUTHORIZED

## Authorization
The user's 2026-09-28 instruction to continue QA work using the governing routine authorizes the next bounded phase identified by the accepted Sandbox checkpoint: historical outcome scoring/evaluation of the already-frozen candidate predictions.

This authorization does not extend to 2025 TEST, candidate/k selection as a production decision, refitting, Champion mutation, Challenger promotion, market-conditioned parameter selection, or production deployment.

## Immutable prediction authority
Accepted freeze:
- evidence/CFB_QA_SANDBOX_CANDIDATE_FREEZE_ACCEPTANCE_2026-09-28.md
- run 36421939025
- artifact 10970862853
- ZIP SHA-256 8955c64f72ea8068279aed3b4ac1f062200394fbc1eb278cb1864de4da9fe5c9
- predictions SHA-256 ed858f1bd72decd93d02aec4de507c3217470b8d01294c2cf677a2d79ed78ee3
- manifest SHA-256 270de37c5fa523e333799a2325f8baa4488cfa0eb114970886d43702fc2211e7
- generator SHA-256 ed089fc928b3ef51d59f97c578491c21e122cc1b51b00e7ad8af0bf1885d1497

Frozen candidates: S0; S1_K1/K2/K4/K8; S2_K1/K2/K4/K8.
No prediction may be recomputed, altered, dropped, or replaced for performance reasons.

## Outcome authority
Use only accepted v1.179 historical dataset targets keyed by season/game_id:
- dataset SHA-256 f8c479c83abf5dac3be6dcb4bba3d6a0996ae2623297a9a3514465824b7c4af8
- eligible historical rows: 6,246
- seasons: 2016–2024 only
- targets: target_home_margin, target_total_points, target_home_win
- partition semantics: TRAIN 2016–2022; SPENT_CORROBORATIVE 2023–2024; 2025 TEST_PROTECTED.

Scoring must fail closed on duplicate/missing target identity, any 2025 row, any outcome mismatch in cardinality accounting, or prediction hash mismatch.

## Predeclared metrics
Per the pre-outcome experiment contract, compute:
- margin: MAE, RMSE, signed bias;
- total: MAE, RMSE, signed bias;
- win: Brier score, log loss, winner-direction accuracy.

Also report:
- by-season metrics;
- history-depth slices based on the frozen target-side qualified-prior information available in the immutable prediction artifact if present; if the frozen artifact does not carry the required depth field, classify that slice as unavailable rather than reconstructing it post-outcome;
- large-disagreement QA slices only if disagreement can be defined solely from frozen candidate predictions/control before consulting outcomes.

No new metric may replace these primary metrics after results are seen.

## Comparison discipline
S0 is the control.
Week 4/2026 is not part of this historical scoring and remains diagnostic/corroborative only under the original contract.
Broadness/stability across seasons and depth slices matters; one aggregate improvement or isolated outlier repair is insufficient for advancement.
Margin improvement may not be interpreted alone if it creates material total/win degradation.

## Execution/acceptance
1. verify immutable prediction and outcome-source identities;
2. join outcomes one-to-many from game target to frozen candidate rows;
3. score without mutating predictions;
4. persist scored summary/detail artifacts and hashes;
5. independently reproduce key cardinalities and metrics;
6. only then interpret results.
Runner green is not scientific acceptance.

Scientific effect before accepted scoring: NONE.
