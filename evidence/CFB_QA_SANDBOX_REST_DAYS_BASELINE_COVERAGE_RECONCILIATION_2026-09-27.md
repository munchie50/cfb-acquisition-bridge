# CFB QA Sandbox Rest-Days Baseline Coverage Reconciliation — 2026-09-27

## Status
DIAGNOSTIC FAIL / PRE-EXECUTION COVERAGE CORRECTION REQUIRED.

Production effect: NONE.
Champion effect: NONE.
Outcome access: NONE.
2025 protected TEST access: NONE.

## Frozen rule
The pooled-baseline freeze requires rest_days to use the season-local mean of valid strictly-prior rest intervals available before the completion-safe cutoff. rest_days is S1-only under the frozen S2 feature mapping.

The completion-safe cutoff remains 00:00:00 UTC on the applicable UTC calendar date. No same-date game, later game, outcome, market, wager, or 2025 record may contribute.

## Finding
The prior chronology evidence stated that all 6,246 accepted target games had a usable completion-safe population baseline. That statement proved general population-game coverage but did not prove feature-specific rest_days availability.

Reproduction against the authoritative v1.172 mechanical-feature surface and v1.179 accepted population found 42 accepted target games with no valid strictly-prior rest_days population observation before the frozen cutoff:
- 2017: 1 game
- 2019: 41 games

The 2017 case is game_id 400935254 (Oregon State vs Portland State, 2017-09-02).
The 2019 cases are the accepted games on 2019-09-07 before a valid earlier-date rest interval exists under the frozen cutoff.

No 2025 row or outcome information was accessed.

## S2 scope clarification
rest_days has no frozen S2 opponent-context mapping. Therefore missing rest_days baselines at historical source-game opponent cutoffs do not independently invalidate S2 source residuals. Only target-game rest_days construction is relevant.

Because every S1 and S2 candidate vector includes the S1-transformed rest_days feature, a target game with no reproducible rest_days baseline cannot produce an S1 or S2 candidate under the frozen fail-closed rule.

## Cardinality consequence
Existing reconciled S2 fail-closed omissions: 12 games.
Target games missing rest_days baseline: 42 games.
Overlap: exactly 1 game, 2017 game_id 400935254.
Union unavailable for S2: 53 games.

Therefore:
- S0 rows: 6,246
- S1 rows: (6,246 - 42) * 4 = 24,816
- S2 rows: (6,246 - 53) * 4 = 24,772
- total candidate rows: 55,834

This supersedes the 56,166 / 24,936 executable cardinality expectation for the current frozen transform while preserving the previously corrected 13-side / 12-game S2-context enumeration.

## Root cause
The pre-execution chronology proof conflated availability of prior population games with availability of every feature-specific baseline. The live generator correctly failed closed when rest_days had no reproducible prior population value.

## Required bounded correction
The generator must fail closed at the candidate-family/game level rather than aborting the entire freeze when the frozen rest_days baseline is unavailable:
- S0 remains available for all 6,246 accepted games.
- S1 is omitted for the 42 target games lacking a rest_days baseline.
- S2 is omitted for those same 42 games plus the already-reconciled S2-context failures, with one-game overlap.
- no imputation, alternate baseline, cross-season carryover, relaxed cutoff, or outcome-driven repair is permitted.

The independent workflow gate must assert the corrected family counts and omission identities before artifact upload.

This is an implementation/audit reconciliation of the already-frozen fail-closed rule, not a new scientific choice.
