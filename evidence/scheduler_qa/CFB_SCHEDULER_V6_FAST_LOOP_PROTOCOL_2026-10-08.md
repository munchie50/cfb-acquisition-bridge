# CFB Scheduler QA — accelerated diagnostic loop (Test Routine v6)

Status: TEST PROTOCOL ACTIVE FOR MANUAL QA; NOT scheduler defect closure or routine promotion.

## Authority and guardrails
Recovered recovery index, October 7 scheduler production contrast, and October 5 terminal closure contract from main. Four production recurring tasks remain the protected topology. The existing temporary canary was documented disabled on October 8; do not create a fifth recurring task or modify any production cadence. Champion, FIRST_FROZEN, Hot Sheet, decision and betting surfaces remain immutable to these diagnostics.

## Accelerated loop
Run manual diagnostic stages consecutively without waiting for an hourly scheduler tick: (1) fresh authority/readback, (2) source retrieval or bounded fixture, (3) representative 49-row payload preparation, (4) diagnostic-only GitHub persistence and independent SHA readback, (5) terminal candidate persisted/read back, (6) separate RUN_CLOSURE persisted/read back. Repeat only the smallest failed stage after classifying the failure; preserve prior attempts. No claims of PASS from merely creating this protocol.

For every attempt record prospective run ID, start and end timestamps when observed, source identity and data-integrity status, payload row count/digest, diagnostic write commit/blob SHA, terminal candidate readback, closure readback, elapsed time if measured, failure stage, and next minimal rerun. If an external source falsely marks a future game Final, record SOURCE_INTEGRITY_FAIL and stop before canonical processing. Distinguish source integrity from scheduler/control-plane behavior.

## Automatic-trigger proof
Manual success proves workload/persistence/closure only. Keep automatic-trigger verification separate, using an already authorized scheduled canary or natural Market Monitor execution. ChatGPT recurring tasks cannot be scheduled more frequently than hourly; do not circumvent this with additional tasks. Production acceptance requires natural scheduled Market Monitor terminal closure with applicable canonical surfaces and independent readback.

## Immediate acceptance gates
A. Manual isolated diagnostic can complete two-phase closure with exact persisted readback.
B. Representative payload and failure-injection tests do not mutate canonical state.
C. Automatic scheduled invocation independently demonstrates the same staged terminal closure.
D. Natural production run meets its separate contract. Until D, scheduler defect OPEN and v6 remains candidate.

This file changes only the QA testing method, not any automation or production control.
