# CFB Engine — Current Recovery Index v1.245

Current QA status (2026-09-29): **REAL TARGET-SIDE AND v4 SOURCE-CONTEXT CAPABILITIES ACCEPTED / PROSPECTIVE CADENCE WAIT.** Earlier dated statuses are retained as historical evidence; the final 2026-09-29 reconciliation governs the current frontier.

Status: **CURRENT ENTRY POINT — CFB BETA PRODUCTION CHAMPION ACTIVE**
Date: 2026-09-28
Supersedes v1.243 as the current entry point. Historical evidence remains preserved.

## Recovery rule
This file is the single current recovery doorway. Scheduled and manual CFB work must deterministically discover the newest accepted Current Recovery Index from repository state/commit history, directly read it back, and follow its dependencies. Code-search indexing is not recovery authority.

## Current production authority
The accepted **CFB Beta Production Champion** is unchanged from v1.240/v1.229/v1.222. Retired production-v1 remains historical/non-operational and may not substitute.

Champion identity remains v1.193:
- TRAIN 2016–2022: 4,700 eligible games
- spent/corroborative 2023–2024: 1,546
- lambdas: margin 0.1, total 0.1, win 0.01
- coefficients SHA bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221
- scaling SHA 68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45

2026 prospective lineage remains rooted in v1.208/v1.215/v1.216:
- 622 future relevant-FBS targets
- 526 FIRST_FROZEN predictions
- 96 exclusions
- FIRST_FROZEN immutable; valid later snapshots append as REFRESH_SNAPSHOT.

## Active authority
Inherit all active dependencies listed by v1.240, including v1.229, v1.222, v1.208, v1.215, v1.216, v1.193, v1.198, v1.224, v1.226, v1.227, v1.231, v1.233, v1.235, v1.236, v1.237, v1.238 and v1.239.

Add:
- **v1.242 Durable Operational Evidence Chain** — canonical repository persistence for market monitoring, decisions/WAIT, executions, postgame FIRST_FROZEN scoring, and conforming run receipts.

The 2026-09-27 Weekly Beta Learning Review v1.241 and its RUN_INCOMPLETE receipt remain historical evidence of the persistence gap that v1.242 repairs; they are not authority to reconstruct missing pre-event evidence.

## Canonical operational recovery surfaces
Directly recover/read:
1. `evidence/operational/CFB_MARKET_MONITOR_STATE.md`
2. `evidence/operational/CFB_DECISION_WAIT_LEDGER.md`
3. `evidence/operational/CFB_EXECUTION_LEDGER.md`
4. `evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md`
5. `evidence/run_receipts/` for new conforming receipts.

A scheduled run must persist applicable changes to these surfaces before RUN_PASS. NO_MATERIAL_CHANGE still requires direct readback and receipt documentation.

## Sunday QA
Sunday QA directly consumes the four operational surfaces. It may report missing historical coverage honestly, but may not reconstruct missing pre-event market/decision/execution evidence after outcomes. RUN_PASS requires the dated/versioned Weekly Beta Learning Review plus applicable surface readbacks and conforming run receipt under v1.239/v1.242.

## Locks
Keep prediction, market, decision, execution, close and outcome separate. User screenshots/wagers are downstream execution evidence only and never Champion model inputs. No outcome-driven refit, retroactive prediction/decision manufacture, invented probability/EV/confidence, automatic Champion mutation, or automatic Challenger promotion.

## Active QA Sandbox recovery pointer
The isolated opponent-strength/small-sample stabilization QA Sandbox remains non-production and does not alter Champion authority.

For current QA Sandbox continuation, directly recover/read:
- `evidence/CFB_QA_SANDBOX_CURRENT_CHECKPOINT_2026-09-28.md`
- `evidence/CFB_QA_SANDBOX_EXECUTION_ATTEMPT_LEDGER_2026-09-28.md`

These are recovery/navigation surfaces for the active experiment, not scientific acceptance or production promotion. The checkpoint carries the DONE / ACTIVE / BLOCKED / NEXT / DO NOT TOUCH frontier and distinguishes scientific, implementation/performance, and infrastructure changes.

Scientific effect: none. v1.245 advances recovery/navigation authority only; Champion v1.193 remains unchanged.


## 2026-09-29 reconciled current frontier — supersedes older ACTIVE/NEXT statuses above
Direct terminal/artifact reconciliation accepted:
- real S0 target-side boundary: CFB_QA_V1_246_REAL_TARGET_SIDE_ACCEPTANCE_2026-09-29.md (run 36636336698, artifact 11064541770; 1,114 sides);
- v4 source-context capability: CFB_QA_S2_K1_SOURCE_CONTEXT_V4_ACCEPTANCE_2026-09-29.md (run 36637810698, artifact 11065575217; 4,355 context rows, 662 rows per primitive surface).
Exact hashes, counts, independent semantic proof and limitations are in those acceptance records. All 1,114 target-side counts, including six zero-history cases, passed. No S2 predictions or 2026 S2 outcomes evaluated.
Current disposition: ACCEPTED QA INPUT CAPABILITIES / S2_K1 STILL STUDY-ONLY / CADENCE WAIT.
v1.246 and source-context infrastructure gates are closed for these retained bytes. Do not blindly rerun earlier pending dependencies. Original historical raw-byte replay limitation remains.
Next: at the next v1.216 weekly cadence, requalify source state and determine refresh/no-op before constructing/producing a prospective S2 consumer. September 29 is within the cycle anchored by September 26 FIRST_FROZEN; no exception is authorized here. Structural QA runs do not constitute an operational prospective refresh.
No-op means no manufactured snapshot. Qualified consumer/freeze must remain exact k=1, use same-cutoff accepted boundaries, whitelist frozen input fields, freeze deterministic history-depth slices, and remain separate from S0. Outcome scoring remains separately gated. Champion unchanged.


## 2026-09-29 prospective football-week cadence correction — v1.247
Authority: `CFB_ENGINE_FOOTBALL_WEEK_OPERATING_CADENCE_CONTRACT_v1_247.md`.
The v1.216 seven-day/FIRST_FROZEN-anniversary timing is superseded prospectively as the operating dispatch clock; all v1.216 lineage and evidence rules remain.
New planning rhythm (America/Chicago): Sunday postgame closure, Monday source readiness, Tuesday preferred qualified immutable S0/S2_K1 freeze, Wednesday bounded source/operational fallback, Thursday–Saturday downstream market/decision/execution work.
Do not create an extra September 29 snapshot. The next normal cycle begins after the current Week 5 slate. Fresh preflight remains mandatory; no-op means create nothing. S2_K1 remains study-only and scientifically unchanged; Champion v1.193 and FIRST_FROZEN remain unchanged.
