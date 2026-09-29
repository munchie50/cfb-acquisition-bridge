# CFB QA Sandbox — S2_K1 Source-Context Companion Contract
Date: 2026-09-28
Status: FROZEN IMPLEMENTATION CONTRACT / NOT YET EXECUTED OR ACCEPTED

## Purpose
Supply the missing source-game opponent context and frozen population baselines required by the already-frozen S2_K1 transform without reconstructing, refitting, or altering S0.

## Authoritative parent boundaries
- Accepted generalized S0 refresh substrate: v1.246.
- Accepted target-side export: challenger_b_2026_refresh_team_side_substrate_v1_246.csv.
- Frozen historical S1/S2 semantics: scripts/cfb_qa_sandbox_candidate_generator_2026_09_27.py.
- Frozen S2 mapping and chronology contracts remain unchanged.

## Input-source lock
The companion uses only the same qualified 2026 schedule R and play-by-play P inputs already consumed by v1.246, under the same execution cutoff. No new external data source is introduced.

## Required source-context rows
For every qualified prior source game used by an eligible target side, persist:
- target game, target side/team, target kickoff, target qualified-prior count;
- source game and source kickoff;
- source opponent identity;
- source opponent qualified-prior count at source kickoff;
- source opponent exact 17-feature pregame state when reproducible;
- mechanical/derived completion-safe status needed by frozen S2 context handling;
- strict chronology and own-target-game exclusion indicators.

Opponent pregame state must be computed from games strictly before the source kickoff. No source game may appear in its own opponent pregame history.

## Frozen population baseline rows
For every S2-paired feature and required target/source cutoff, persist the exact season-local frozen baseline using the historical calendar-day-normalized cutoff rule.

Component-backed baselines must use pooled strict-prior numerators/denominators, not means of team feature rates. rest_days uses the mean reproducible strict-prior side state exactly as frozen historical semantics require.

## Frozen S2 behavior supported
- k = 1 only.
- exact 10 mapped feature pairs; 7 S1-only features remain S1 values.
- target S1 minus mean(valid paired opponent S1 residuals).
- opponent residual = opponent S1 minus paired population baseline at source kickoff.
- zero-history opponent context contributes residual 0 when a completion-safe baseline exists.
- unavailable completion-safe source context is skipped.
- mapped target context fails only when no valid completion-safe residual remains.
- no recursion.

## Forbidden
No target outcomes, postgame target information, market/spread/odds, user wagers/execution, protected 2025 TEST, refit/recalibration, new k-grid, Champion mutation, production promotion, or live prospective freeze.

## Implementation architecture
Build a separate QA companion exporter. Do not modify accepted v1.246 scientific calculations or use the companion to regenerate S0 target features. The companion may reuse the same raw R/P inputs and exact v1.246 feature definitions solely to construct the additional source-opponent pregame/context surface required by frozen S2.

## Acceptance gates before S2 consumer
1. strict target -> source -> opponent-prior chronology;
2. no own-game leakage at either chronology level;
3. exact 17-feature identity and exact 10/7 mapping lock;
4. pooled baseline numerator/denominator identity;
5. calendar-day-normalized cutoff identity;
6. completion-safe skip/zero-history semantics;
7. no 2025/outcome/market/wager exposure;
8. deterministic row identity and hashes;
9. source implementation identity pinned and read back.

Passing this contract authorizes only construction of the separate S2_K1 consumer. It does not authorize live freezing, outcome scoring, acceptance, promotion, or production change.
