# CFB Engine — Review Findings and Durable Action Register — 2026-09-28

Status: ACTIVE REVIEW/ACTION REGISTER
Scope: findings from the bounded historical-integrity, whole-engine seam, production-operations, technical-debt, recovery/governance, and cold-recovery reviews. This record does not change Champion/model/scientific authority.

## Confirmed healthy / closed findings
1. Historical/model seams are strongly reconciled: 7,701-game population -> 15,402 team-sides -> 6,246 eligible + 1,455 excluded -> 4,700 TRAIN + 1,546 spent/corroborative -> v1.193 fit -> 2026 prospective lineage.
2. v1.193 correctly repaired v1.184 evidence-transcription errors without refitting; accepted artifacts outrank prose.
3. 2026 FIRST_FROZEN lineage is independently reproducible and immutable under v1.208/v1.215/v1.216.
4. Current `.github/workflows/Main.yml` is path-limited/manual; the earlier concern that it broadly triggers on nearly every main push is stale historical debt, not current debt.
5. QA performance optimization materially reduced candidate generation from >90 minutes to about 19 minutes to the cardinality gate; Run #12 comparison found no evidence that the optimization introduced the S2 semantic defect.

## QA Sandbox findings
A. Full execution history Runs #1–#12 and Run #12 root cause are now reconciled in `evidence/CFB_QA_SANDBOX_EXECUTION_ATTEMPT_LEDGER_2026-09-28.md`.
B. Current Sandbox recovery doorway is `evidence/CFB_QA_SANDBOX_CURRENT_CHECKPOINT_2026-09-28.md`.
C. Stale S2 inner exception handling was confirmed causal for Run #12's excess omissions and boundedly corrected on main commit `2f8aad0963d6a09ae9b8eb749163f3ff65d3566a`; corrected generator blob `40447984a58dbc530cbe942bc1176f0c5bcbe9b2`.
D. Corrected generator identity observation/pinning and fresh candidate freeze remain open.
E. Outcome scoring remains separately unauthorized.

## Production operational findings — open durable actions
1. **Controlled execution reconciliation:** the canonical execution ledger currently lacks the previously established 2026-09-26 controlled executions. Reconcile only from original screenshot/evidence records; do not backfill from memory. Preserve downstream/execution-only classification and prohibit model contamination.
2. **Closing-market surface:** recovery authority says prediction, market, decision, execution, close and outcome must remain separate, but the canonical operational surfaces currently provide no dedicated durable closing-market ledger. Establish an append-only close surface with qualified source/timestamp semantics and no retrospective substitution when genuine close was not captured.
3. **Terminal receipt closure:** a reviewed Sunday-market receipt declared RUN_PASS while its own persistence/readback section still described same-commit creation/readback as pending. Strengthen terminal semantics so RUN_PASS is issued only after applicable surfaces and the terminal receipt itself have persisted/readback proof; use a closure/finalization pattern rather than optimistic certification.
4. **2026-09-28 market-monitor persistence:** the 07:00 CT run correctly remained RUN_INCOMPLETE when canonical mutation was blocked. Do not reconstruct or smuggle those observations into authoritative history. Handle future observations prospectively after the write path is valid.
5. **Sunday Early Board evidence:** verify exact persisted location/readback/closure before treating the earlier RUN_PASS receipt as fully reconciled.

## Recovery/governance findings
1. Current production recovery is usable from v1.245, but the QA doorway was stale before this reconciliation. The current Sandbox checkpoint now includes a staleness rule: terminal external run or superseded parent -> reconcile before following NEXT.
2. Operating procedure should be explicit at recovery surfaces: Production Routine v5 (v1.103) + active learning rule v1.132 + active execution controls v1.133.
3. Shared Universal Project Standards v1.4 does not silently alter CFB authority. Perform a bounded CFB applicability review and record adopt/defer/not-applicable for material v1.4 changes.
4. Recovery must not rely on code-search indexing or conversation memory; direct repository enumeration/readback remains authority.

## Technical-debt classification
HIGH: production close-market durable surface.
HIGH: terminal receipt/readback closure semantics.
HIGH while QA active: corrected S2 generator identity/pinning/fresh freeze.
MEDIUM: controlled execution ledger reconciliation from original evidence.
MEDIUM: permanent diagnostic ergonomics so cardinality failures expose actual family counts/omissions before generic assertion without weakening fail-closed gates.
LOW/RESOLVED: broad Main.yml trigger concern (current trigger is already bounded).
DO NOT WEAKEN: generator/input identity controls despite controlled-stop workflow noise.

## Required closure discipline
For each open action:
- preserve predecessor evidence;
- make the smallest bounded correction;
- keep scientific/model authority unchanged unless separately governed;
- persist and directly read back the changed surface;
- record demonstration evidence before classifying the lesson LEARNED.

This register is an action/review record, not authorization for outcome access, model tuning, Champion mutation, Challenger promotion, destructive cleanup, or retrospective manufacture of missing pre-event evidence.
