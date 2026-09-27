# CFB Engine — Durable Operational Evidence Chain v1.242

Status: **ACTIVE OPERATIONAL PERSISTENCE CONTROL**
Date: 2026-09-27
Parents: v1.224, v1.226, v1.233, v1.236, v1.237, v1.238, v1.239, v1.240

## Purpose
Close the persistence gap exposed by the 2026-09-27 Sunday QA rerun. Scheduled work may not rely on transient chat/task context for evidence required by later QA. Required downstream state must have canonical durable repository surfaces.

## Canonical operational surfaces
1. `evidence/operational/CFB_MARKET_MONITOR_STATE.md`
2. `evidence/operational/CFB_DECISION_WAIT_LEDGER.md`
3. `evidence/operational/CFB_EXECUTION_LEDGER.md`
4. `evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md`
5. `evidence/run_receipts/` for timestamped append-only run receipts.

These paths are recovery authority for their operational layer. Search/index availability is not required for recovery; fetch/read the canonical path directly.

## Write-before-complete rule
A scheduled run that creates or changes any governed market observation, decision/WAIT state, established execution/settlement, or postgame scorecard state must persist that state to its canonical surface before it may claim RUN_PASS.

If there is no material state change, the run receipt must explicitly say NO_MATERIAL_CHANGE and identify the canonical surface read back.

## Market Monitor persistence
Every qualified observation and NOT_YET_AVAILABLE check required by active market-monitor authority must be appended to the market surface with timestamp/provenance. FIRST_QUALIFIED_MARKET_OBSERVATION is immutable. Later observations never overwrite it.

## Decision and WAIT persistence
Every prospective BET EARLY/BET NOW/WAIT/PASS/INCONCLUSIVE state produced by a governed run must be appended before outcome. WAIT must carry its required reason/trigger/opportunity-at-risk/latest-useful-point fields where supportable. Later WAIT disposition is appended, not rewritten.

## Execution persistence
Only established actual executions enter the execution ledger. Screenshot/user execution evidence remains downstream observational evidence and is prohibited from Champion model inputs. Missing original evidence is not backfilled from memory.

## Postgame scoring persistence
After final results are authoritative, a scoring run may join them to genuinely pre-event FIRST_FROZEN predictions. It must preserve prediction identity and chronology, source final results, compute only supported errors/outcomes, and leave ambiguous joins UNRESOLVED. Results cannot create or alter a frozen prediction.

## Sunday QA recovery gate
Sunday QA must directly read back all four canonical operational surfaces plus the newest recovery index. Missing data inside a valid surface is reported as a coverage gap; missing required surface/readback is a persistence failure.

Weekly QA may use only genuinely persisted pre-event market/decision/execution evidence for historical comparisons. It must not manufacture a missing historical Sunday state after outcomes.

## Receipt path
v1.239's required receipt location `evidence/run_receipts/` is confirmed as the canonical path. The directory is initialized by README. A receipt written elsewhere is durable historical evidence but is nonconforming for future runs.

## Discovery and observability
Current recovery discovery should use deterministic repository state/commit history and direct path readback. Repository code-search indexing is convenience only and must not be a required recovery dependency.

## Completion
RUN_PASS requires:
- applicable canonical surfaces persisted;
- direct independent readback of each applicable surface;
- required run-specific artifact(s) persisted/read back;
- conforming timestamped receipt under `evidence/run_receipts/` persisted/read back.

## Scientific boundaries
This repair changes operational persistence and recoverability only. It does not alter Champion coefficients, predictions, model inputs, betting calibration, promotion authority, screenshot boundary, or user execution authority.

Scientific effect: none.
