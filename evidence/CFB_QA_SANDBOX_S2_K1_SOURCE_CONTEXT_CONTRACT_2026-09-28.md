# CFB QA Sandbox — S2_K1 Source-Context Companion Contract

Current QA status (2026-09-29): **REAL TARGET-SIDE AND v4 SOURCE-CONTEXT CAPABILITIES ACCEPTED / PROSPECTIVE CADENCE WAIT.** Earlier dated statuses are retained as historical evidence; the final 2026-09-29 reconciliation governs the current frontier.
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


## Recovered primitive ancestry and 2026 adapter lock
Exact recovered builder: `scripts/phase4_challenger_b_corrected_features_v1_172.py`, Git blob `37c05aba201d3c2935b5d2b646437552949766fd`.

The 2026 companion must reuse these frozen per-game primitive semantics:
- mechanical: off_plays, off_yards, rush_plays, pass_plays, rush_yards, pass_yards, pass_attempts, interceptions, def_plays, def_yards;
- derived: off_scr, off_exp, off_succ_q, off_succ, def_scr, def_exp, def_succ_q, def_succ, start_ytg_sum, start_drive_n;
- derived event counts zero-fill only after team/game identity is established by scrimmage participation;
- drive start uses first yards_to_goal by game/team/drive in source order;
- mechanical/derived primitive completeness are per-game team-side flags;
- history completeness is cumulative strict-prior state and is distinct from own-game primitive completeness;
- strict same-team chronology must be deterministic and fail on equal-kickoff ambiguity.

2026-only adapter:
v1.172 used a separately persisted historical known-missing-PBP game-ID ledger. The accepted v1.246 2026 source boundary instead establishes PBP availability directly from the supplied P surface and already fails a target side when its required prior game IDs are not all represented. The companion will therefore derive `pbp_game_present` from membership in the supplied 2026 P game-ID set. It must not invent or import a different missing-ID ledger.

Population baseline construction will pool only per-game primitive rows whose corresponding primitive-complete flag is true and whose kickoff is strictly before `pd.Timestamp(source_kickoff).normalize()`, matching the frozen historical baseline rule. rest_days remains the mean of reproducible strict-prior team-side rest-day states under the same normalized cutoff.

This adapter does not change frozen S2 science; it maps the accepted 2026 source-availability boundary onto the recovered v1.172 primitive semantics.


## 2026-09-29 reconciled current frontier — supersedes older ACTIVE/NEXT statuses above
Direct terminal/artifact reconciliation accepted:
- real S0 target-side boundary: CFB_QA_V1_246_REAL_TARGET_SIDE_ACCEPTANCE_2026-09-29.md (run 36636336698, artifact 11064541770; 1,114 sides);
- v4 source-context capability: CFB_QA_S2_K1_SOURCE_CONTEXT_V4_ACCEPTANCE_2026-09-29.md (run 36637810698, artifact 11065575217; 4,355 context rows, 662 rows per primitive surface).
Exact hashes, counts, independent semantic proof and limitations are in those acceptance records. All 1,114 target-side counts, including six zero-history cases, passed. No S2 predictions or 2026 S2 outcomes evaluated.
Current disposition: ACCEPTED QA INPUT CAPABILITIES / S2_K1 STILL STUDY-ONLY / CADENCE WAIT.
v1.246 and source-context infrastructure gates are closed for these retained bytes. Do not blindly rerun earlier pending dependencies. Original historical raw-byte replay limitation remains.
Next: at the next v1.216 weekly cadence, requalify source state and determine refresh/no-op before constructing/producing a prospective S2 consumer. September 29 is within the cycle anchored by September 26 FIRST_FROZEN; no exception is authorized here. Structural QA runs do not constitute an operational prospective refresh.
No-op means no manufactured snapshot. Qualified consumer/freeze must remain exact k=1, use same-cutoff accepted boundaries, whitelist frozen input fields, freeze deterministic history-depth slices, and remain separate from S0. Outcome scoring remains separately gated. Champion unchanged.
