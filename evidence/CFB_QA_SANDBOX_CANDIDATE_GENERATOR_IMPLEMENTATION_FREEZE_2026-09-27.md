# CFB QA Sandbox Candidate Generator Implementation Freeze — 2026-09-27

Status: IMPLEMENTATION SEMANTICS FROZEN — OUTCOME SCORING NOT STARTED
Parent: CFB_QA_SANDBOX_CONSTRUCTION_SENTINEL_AUDIT_2026-09-27
Production effect: NONE
Champion effect: NONE

## Fixed implementation inputs
Accepted v1.172 primitive/feature substrate, accepted v1.179 eligible model population, and frozen v1.183/v1.193 scaling and coefficients only.
2025 is forbidden.

## Candidate population
Use exactly the accepted v1.179 eligible game rows. Opening/no-prior and other accepted exclusions remain exclusions. Candidate construction may not manufacture additional eligibility.

## Population baseline mechanics
At each target/source cutoff, component-based features use pooled completed strict-prior primitive numerators and denominators. Per-game points and scrimmage-play features use pooled completed strict-prior totals divided by completed team-games. Rest days uses the strictly-prior population of valid rest intervals. No full-season or future aggregate is permitted.

## S1
For each feature and team-side with n qualified prior games:
S1 = n/(n+k)*raw + k/(n+k)*baseline
for k in {1,2,4,8}.

## S2
Start from S1. Only the ten frozen mapped features receive opponent correction. For each target side, use its qualified source games only. For each source game, read the paired opponent feature from the opponent's S1 pregame state at that source kickoff. Subtract the population baseline available before that source kickoff to form the opponent residual. Apply the frozen normalization direction and average valid source-game residuals once. No S2 recursion.

The seven unmapped features remain identical to S1.

## Frozen prediction mechanics
For every candidate feature vector:
- use the accepted TRAIN 2016-2022 feature means/SDs from frozen train_scaling.csv;
- use the frozen selected coefficients;
- retain accepted venue_neutral encoding;
- do not refit coefficients or scaling for this experiment.

This isolates the effect of the feature stabilization transform.

## Outcome-blind freeze artifact
The prediction artifact may contain only:
season, game_id, start_date, home_team, away_team, venue_state, candidate_id, k, pred_margin, pred_total, pred_win, construction/audit identifiers.

It must not contain target, actual, final-score, market, odds, wager, decision, close, or outcome fields.

Expected candidate IDs:
S0
S1_K1, S1_K2, S1_K4, S1_K8
S2_K1, S2_K2, S2_K4, S2_K8

S0 must remain numerically equivalent to the frozen Champion.

## Freeze-before-score gate
Generator/config hashes, prediction artifact hash, row counts, forbidden-column scan, chronology audit, and readback must PASS before any target columns are joined for evaluation.

Scientific effect at implementation freeze: none.
