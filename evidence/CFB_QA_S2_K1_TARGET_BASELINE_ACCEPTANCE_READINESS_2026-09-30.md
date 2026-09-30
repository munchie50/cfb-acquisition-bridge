# CFB QA — S2_K1 Independent Target-Baseline Acceptance Readiness — 2026-09-30

Status: ACCEPTANCE MACHINERY INSTALLED / STATICALLY RECONCILED / LIVE ACCEPTANCE PENDING

## Purpose
Close the executable-readiness gap identified by the v6 candidate WAIT -> SWEEP without manufacturing a weekly candidate or S2_K1 prediction.

## Installed independent auditor
`scripts/cfb_qa_s2_k1_target_baseline_acceptance_v1_2026_09_30.py`

The auditor does not import or invoke the target-baseline candidate producer. It independently reconstructs the frozen 17-feature baseline vector from the same-cutoff S0 target identity surface plus v4 mechanical/derived primitive histories, then compares those expected values to the candidate.

Checks include:
- candidate manifest remains EXECUTED_NOT_ACCEPTED before audit;
- exact cutoff reconciliation;
- target-side identity/cardinality reconciliation;
- all 17 frozen features;
- 16 pooled primitive formulas independently recomputed;
- rest_days reconstructed from consecutive same-team/same-season schedule kickoffs;
- UTC-calendar-day strict-prior population rule;
- no same-date population rows;
- no target future rows used as population baseline;
- no cross-season rest carryover;
- every baseline finite/available;
- candidate values equal independent recomputation at absolute tolerance 1e-12;
- candidate file hash reproduced from manifest;
- no target outcomes, market, wager/execution, protected 2025 TEST, fit or optimization.

Passing output status is `PASS_S2_K1_TARGET_BASELINE_ACCEPTANCE`.

## Installed regression guard
`scripts/cfb_qa_s2_k1_target_baseline_acceptance_static_gate.py`

The guard pins the critical independence/chronology/contamination invariants and prohibits importing/invoking the candidate producer. It also requires expected reconstruction to occur before candidate-value comparison.

## Expected vs actual
Expected under v6 WAIT -> SWEEP: remove acceptance-plumbing debt now while leaving actual acceptance dependent on a genuine same-cutoff candidate.
Actual: independent auditor and static guard are installed. No live candidate was generated or accepted. No S2 prediction/outcome/market/model mutation occurred.
Reconciliation: PASS.

## Demonstration status
Acceptance machinery readiness: DEMONSTRATED by source-level/static reconciliation and persistence/readback.
Actual target-baseline acceptance: DEMONSTRATION_PENDING until a genuine qualified same-cutoff candidate exists.

No manual workflow dispatch is justified merely to exercise the auditor.

## Governance
Production/master routine remains v5; v6 remains candidate/test.
Champion v1.193 unchanged.
2025 TEST protected.
