# CFB Test Routine v6 — bounded evidence strength audit — 2026-10-30
Status: AUDIT_COMPLETE_FOR_RECOVERED_EVIDENCE / CORE_HOLD_TARGETED_GATES / NOT A PROMOTION.

Authority: v5 production governor, v6 QA method. Original v6 core evaluated separately from Oct30 QA-only stability amendment. Evidence read directly from main: original v6 48,835-character candidate, Sep30 existing-evidence matrix, Sep30 WAIT sweep, Oct06 time-hidden replay, Oct08 independent structural sweep, Oct08 recovery-frontier reconciliation, v5 promotion authority, Oct30 prior promotion review.

## Evidence-to-claim audit
1. Core sequence preserves v5 front half, adds producer verification, demonstration, expected-actual, monitor exceptions and closure debt: DOCUMENTED; no conflicting front-half reorder found in inspected candidate. Candidate has 25 later sections; scope growth warrants consolidation at promotion rather than assuming all sections independently proven.
2. WAIT -> SWEEP: DEMONSTRATED_PASS Sep30 with trigger, expected/actual, useful independent work and dependency restraint.
3. Recovery/navigation, persistence, readback: DEMONSTRATED_BOUNDED Oct08, exact readback and 9/9 references. Not natural scheduler proof.
4. Three independent static checks: EXECUTED_PASS Oct08 on exact blob bytes. Static consumer, Hot Sheet, weekly no-op tests do not prove real-time quote accuracy or live end-to-end production.
5. Time-hidden replay: INITIAL_BOUNDARY_AND_DEFECT_DETECTION_PASS Oct06; remaining chronological checkpoints expressly IN_PROGRESS. Not a full replay PASS.
6. Natural Monitor + Health integration: Sep30 matrix explicitly lists outstanding natural run/section/Health demonstrations. Oct29 natural Monitor success is relevant new evidence but its exact receipt-to-core mapping and independent Health reconciliation have not been completed here. Mark POTENTIALLY_SATISFIABLE, not PASS.
7. Failure-class/representative-load gate: documented Oct03, not shown fully demonstrated across scheduler NO_UPDATE and canonical rejection classes. Oct30 failure root cause remains UNKNOWN.
8. Core v5-v6 comparative regressions, overhead, rollback and integrated independent routine-level acceptance: NOT YET EVIDENCED in reviewed records.

## Risk / benefit judgment
Benefits supported: improved proof discipline, no false closure on static checks, useful WAIT work, authentic ancestry/readback. Residual risks: extensive candidate appendages, runtime overhead not measured, natural scheduler startup not solved, temptation to equate using candidate with acceptance. No evidence that v6 caused Oct30 failure; no evidence that v6 fixes scheduler startup by itself.

## Smallest next work
(a) Independently map latest accepted Oct29 Monitor and subsequent Health receipts to Sep30 missing natural gates; (b) complete only mandatory historical replay gaps, or explicitly justify non-mandatory; (c) one bounded same-evidence v5-v6 coverage/latency/regression assessment; (d) integrated independent signoff and user authorization. No reset of prior passes, no requirement to wait arbitrary weeks. Keep new stability amendment separate. Natural Oct30 NO_UPDATE investigation remains separately open.

Decision: CORE_V6_PROMOTION = HOLD_FOR_SPECIFIC_EVIDENCE; CORE_V6_QA_USE = YES_WITH_AUTHORITY_DECLARATION. No production or task changes.
