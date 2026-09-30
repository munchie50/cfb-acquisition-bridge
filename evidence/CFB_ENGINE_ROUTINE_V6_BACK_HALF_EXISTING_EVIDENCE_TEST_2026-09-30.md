# CFB Routine v6 Back-Half Candidate — Existing-Evidence Demonstration Matrix — 2026-09-30

Status: CANDIDATE TEST EVIDENCE / NO PRODUCTION ROUTINE PROMOTION

## Test objective
Exercise the v6 candidate controls against existing persisted evidence before requesting any additional live run.

## Case A — Sep. 30 Market Monitor silent/incomplete completion
Issue: scheduled cycle activity did not prove conforming engine completion.
Root cause class: observability/completion-proof gap.
Correction: Market Monitor now requires RUN_STARTED plus separate terminal receipt, canonical persistence/readback and Hot Sheet readback; Dual Engine Health owns independent retrospective audit.
Producer control: Market Monitor task itself strengthened; separate fifth watchdog disabled and superseded by four-task topology.
Existing demonstration: user-authorized extra cycle proved RUN_STARTED persistence and terminal RUN_INCOMPLETE persistence/readback; subsequent repair closure proved bounded missing-surface repair.
Independent reconciliation: historical RUN_INCOMPLETE remains immutable and repair closure remains separate.
State under v6 candidate: DEMONSTRATION_PENDING for a normal scheduled Market Monitor RUN_PASS. No extra live run required; natural 13:00 CT cycle is the correct trigger.

## Case B — Hot Sheet NEXT-UP placeholder defect
Issue: Thursday/Friday headings existed but actual governed games were not rendered.
Root cause class: presentation requirement documented without deterministic producer invariant.
Correction: deterministic kickoff sectioning contract installed; Market Monitor producer instructions updated; Thursday/Friday current render corrected without changing model/market/decision state.
Producer control: authoritative kickoff -> America/Chicago -> exactly one mutually exclusive bucket; unresolved kickoff fails closed; populated sections prohibit placeholders.
Reconciliation invariant: section union equals governed slate; no duplicate identity; section count sum equals governed-slate cardinality.
Existing demonstration: Thursday/Friday schedule membership can be statically reconciled against authoritative schedule evidence and current persisted market observations.
State under v6 candidate: PARTIALLY_DEMONSTRATED. Full 47-game exactly-once render remains DEMONSTRATION_PENDING for the natural next Market Monitor; no extra live run required.

## Case C — Decision-ledger write friction
Issue: initial write using action-oriented wager wording was blocked by tool/safety controls.
Root cause class: content-sensitive tool/safety friction, not repository/ledger corruption.
Correction: bounded factual reconciliation write succeeded without evading safety controls.
Producer/path verification: same canonical ledger accepted a neutral operational reconciliation and persisted/read back.
State under v6 candidate: DEMONSTRATED and RECONCILED for repository-path health. Historical blocked attempt remains preserved; no retry needed.

## Case D — Fifth watchdog topology
Issue: observability repair initially created a fifth recurring-task design inconsistent with four-task operating envelope.
Root cause class: local repair bypassed global task-capacity governance.
Correction: watchdog disabled; incident evidence superseded; Market Monitor owns self-proof and Dual Engine Health owns independent audit.
State under v6 candidate: CORRECTED/PERSISTED/READ_BACK. Static topology is demonstrable from current task state; future health audit behavior is naturally demonstrated at its next scheduled cycle. No extra run required.

## Candidate findings
The candidate successfully changes closure semantics:
- installed != demonstrated;
- repaired artifact != repaired producer;
- expected-vs-actual cardinality becomes explicit;
- WAIT creates bounded proof/debt work;
- natural scheduled runs are preferred over artificial proof runs.

## Open demonstration debt
1. Normal scheduled Market Monitor must prove full end-to-end completion under strengthened observability.
2. Same run must prove full governed-slate exactly-once Hot Sheet section reconciliation.
3. Dual Engine Health must later prove independent detection/audit of expected Market Monitor cycles under its strengthened ownership.

These are natural scheduled demonstrations. Additional manual Market Monitor/Health runs are not justified at this time.

## Result
V6_BACK_HALF_CANDIDATE_EXISTING_EVIDENCE_TEST = PASS_WITH_NATURAL_RUN_DEMONSTRATION_DEBT
Production/master routine remains v5.
