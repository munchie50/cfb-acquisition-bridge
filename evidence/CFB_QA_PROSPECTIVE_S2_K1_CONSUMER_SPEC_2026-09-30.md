# CFB QA — Prospective S2_K1 Consumer Executable Specification — 2026-09-30

Status: PRE-EXECUTION IMPLEMENTATION CONTRACT / NO S2_K1 PREDICTIONS GENERATED
Parents: CFB_QA_SANDBOX_PROSPECTIVE_S2_K1_CONTINUATION_CONTRACT_2026-09-28.md; CFB_QA_S2_K1_SOURCE_CONTEXT_V4_ACCEPTANCE_2026-09-29.md; CFB_QA_SANDBOX_S1_S2_TRANSFORM_SPEC_2026-09-27.md; CFB_QA_SANDBOX_POOLED_BASELINE_MAPPING_FREEZE_2026-09-27.md.

## Purpose
Freeze the exact prospective S2_K1 consumer interface and mechanics before a qualified weekly REFRESH_SNAPSHOT exists. This closes implementation ambiguity without manufacturing a prospective prediction.

## Required accepted inputs
A future execution may consume only one same-cutoff, independently accepted weekly boundary:
1. complete accepted v1.246 S0 REFRESH_SNAPSHOT package;
2. same-cutoff accepted v4 source-context package produced from the exact same raw schedule/PBP identities;
3. frozen Champion v1.193 scaling and coefficients.

Candidate workflow success alone is insufficient. Cutoff, target identities and raw source identities must reconcile before execution.

## Target population
Start from the accepted S0 target ledger. S2_K1 may produce a prediction only when:
- S0 has an eligible prediction for the target;
- both target sides have positive qualified_prior_games;
- every required mapped-feature source context needed by the frozen one-step correction is valid under v4 completion-safe rules;
- every required population baseline exists.

Otherwise S2_K1 fails closed for that target. It never manufactures S0 eligibility.

## Frozen transform
k = 1 only.

For each target side and feature F:
S1_F = n/(n+1) * Raw_F + 1/(n+1) * B_F(target cutoff).

For the ten frozen mapped features, for each qualified source game g:
R_F(o,g,1) = S1_paired_F(o,g,1) - B_paired_F(g).

The target-side context term is the simple mean of valid source-game opponent residuals. Apply the frozen historical mapping/sign direction exactly once:
S2_F = S1_F + signed_mean_context_F.

No recursion. No S2 value may enter another context calculation.

The ten mapped pairs remain exactly:
- points_for_per_game ↔ points_against_per_game
- offensive_scrimmage_plays_per_game ↔ defensive_scrimmage_plays_per_game
- offensive_yards_per_play ↔ defensive_yards_per_play
- offensive_explosive_play_rate ↔ defensive_explosive_play_rate
- offensive_success_rate ↔ defensive_success_rate_allowed

The seven unmapped features remain S1-only:
rush_play_rate, pass_play_rate, rush_yards_per_play, pass_yards_per_play, interception_rate, rest_days, average_starting_yards_to_goal.

No mapping, sign, k, baseline rule, eligibility rule, scaling or coefficient change is permitted.

## Input allowlist
Consumer code must explicitly select only:
- S0 target identity/cutoff/venue fields;
- target-side qualified_prior_games and the 17 raw frozen features;
- v4 source_context identity/chronology fields;
- for the ten mapped pairs: paired raw opponent value, paired population baseline, availability/completion flags and the source/target/opponent identities required to prove chronology;
- accepted scaling and coefficients.

Unused source schedule metadata in primitive/context packages, including winner/rank fields, must never enter the consumer dataframe.

Forbidden: target outcomes/PBP, scores/results, market/spread/odds/closing fields, wager/execution/decision fields, protected 2025 TEST, later source state.

## Prediction
Construct the 34 home_/away_ S2_K1 features, standardize only with frozen v1.193 TRAIN scaling, and apply frozen v1.193 coefficients/lambdas:
margin 0.1; total 0.1; win 0.01.
No fit, optimization, recalibration or threshold tuning.

## Required pre-outcome output
Separate Sandbox artifact only; never overwrite S0.

Per eligible target:
season, game_id, start_date, home_team, away_team, venue_state,
snapshot_type=REFRESH_SNAPSHOT,
snapshot_cutoff_utc,
candidate_id=S2_K1,
k=1,
home_qualified_prior_games,
away_qualified_prior_games,
history_depth_slice,
pred_margin, pred_total, pred_win,
S0 artifact identity/hash,
v4 context artifact identity/hash,
raw schedule/PBP SHA-256,
consumer file SHA-256/Git blob,
frozen config SHA-256.

History-depth slice is immutable:
- DEPTH_1_2 if min(home,away) is 1–2;
- DEPTH_3_4 if min is 3–4;
- DEPTH_5_PLUS if min >=5.

Persist explicit exclusions separately with fail-closed reasons.

## Freeze gate
Before any outcome evaluation:
- target/cutoff/source identity reconciliation PASS;
- k exactly 1 and candidate exactly S2_K1;
- frozen mapping/config hash persisted;
- forbidden-column scan zero;
- chronology/context availability checks PASS;
- prediction/exclusion population accounting PASS;
- finite predictions and win in [0,1];
- output bytes and manifest hashes persisted/read back;
- S0 remains untouched.

Outcome scoring remains separately gated.

## Current disposition
Specification frozen. Consumer executable may be constructed/tested structurally against synthetic or already-spent non-2025 fixtures only if that does not create a live prospective snapshot. Actual prospective execution requires the next accepted weekly S0 + same-cutoff v4 context boundary. Frontier remains CADENCE WAIT.
