# CFB QA Sandbox — S2 Fail-Closed Cardinality — 2026-09-27

Status: PRE-EXECUTION CLARIFICATION / FROZEN BEFORE CANDIDATE PREDICTION OR OUTCOME JOIN

Parent chronology clarification: CFB_QA_SANDBOX_COMPLETION_SAFE_POPULATION_CHRONOLOGY_2026-09-27.md

## Rule
S2 is scored at game level and requires a valid S2 feature vector for both participating sides. For a mapped S2 feature, source-game opponent residuals are restricted to valid completion-safe contexts under the frozen UTC-date cutoff. If either target side has zero valid completion-safe opponent residuals, that game's S2 candidate is unavailable and fails closed.

An unavailable S2 candidate is omitted. It MUST NOT:
- be emitted as S1 under an S2 candidate ID;
- impute an opponent residual;
- substitute a different k;
- relax the completion-safe cutoff.

S0 and S1 remain available and unchanged for the same game.

## Pre-execution cardinality proof
Accepted Sandbox games: 6,246.
Completion-safe S2 audit found:
- 12 affected target team-sides;
- 11 unique affected games;
- every affected side has exactly one prior team game;
- affected-game identity is independent of k because context eligibility precedes shrinkage magnitude.

Therefore:
- S0 rows: 6,246;
- S1 rows: 24,984 = 6,246 x 4 k values;
- S2 rows: 24,940 = (6,246 - 11) x 4 k values;
- total frozen expected prediction rows: 56,170;
- S2 rows omitted fail-closed: 44.

Affected game IDs:
2017 400935254
2018 401022521
2018 401022524
2019 401112443
2020 401246425
2022 401403946
2022 401403976
2022 401405073
2022 401413257
2022 401415219
2022 401426543

No 2025 TEST row, outcome, market, wager, or candidate result was used to establish this rule.

## Locks unchanged
k grid {1,2,4,8}; S2 mapping/sign; S0 Champion control; frozen Champion coefficients/scaling; no recursion; no target/later-game information; no Champion mutation; no production promotion. Predictions still must be frozen and hashed before outcome scoring.
