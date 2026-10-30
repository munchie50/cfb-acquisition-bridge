# v5.1-A and v5.1-C — independent gate challenge and amendment-ready language
Date: 2026-10-30
Status: QA REVIEW / NOT ACCEPTED PRODUCTION.

## Independent challenge
Original v5.0 authority requires dependency reconsideration, evidence-constrained stopping, persistence/readback, and output acceptance; candidate A does not override those. Candidate C does not treat static proof as natural producer proof. The Sep30 WAIT case and Sep30 Monitor/Hot Sheet/ledger/watchdog matrix substantiate those specific behaviors. The Oct08 recovery proof substantiates exact readback without claiming production closure.

Counterexamples considered: no independent work at WAIT (stop, do not fabricate); incomplete run despite receipt (not CLOSED); successful repository readback but missing natural producer proof (READ_BACK only); scheduler NO_UPDATE with no linked receipt (dispatch unknown). None permits unsafe retry, phantom PASS, extra task, or market/model mutation. These are logical challenge cases; not new natural demonstrations.

## Proposed narrow v5.1 amendment
A: 'At an evidence-constrained WAIT, make one bounded independent-work sweep of existing open verification, integration, monitoring, and recovery debt. Execute only genuinely independent authorized work. Otherwise retain WAIT with precise trigger. Do not manufacture runs or observations.'
C: 'For material corrections, record strongest evidenced stage: CORRECTED, PERSISTED, READ_BACK, DEMONSTRATED, INDEPENDENTLY_RECONCILED, CLOSED. A readback is not itself producer demonstration. Mark CLOSED only when applicable producer and independent gates are satisfied; otherwise record specific debt and natural next trigger.'
Both are additive clarifications; no new required stage, task, market run, or model control. A and C independently removable. Existing v5.0 remains rollback baseline.

## Decision
A: READY_FOR_USER_APPROVAL_SUBJECT_TO_AUTHORITATIVE_INDEPENDENT_ACCEPTANCE.
C: READY_FOR_USER_APPROVAL_SUBJECT_TO_AUTHORITATIVE_INDEPENDENT_ACCEPTANCE.
B: HOLD_FOR_OVERHEAD_MEASUREMENT, not a blocker to A/C.
Do not infer this document is an independent external review or live production verification. Require accepted branch write/readback, effective timestamp, rollback mapping and next natural-use monitoring before claiming active v5.1.
