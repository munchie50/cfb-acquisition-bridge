# CFB Engine — Current Recovery Index v1.245

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
