# CFB startup and terminal receipt enforcement — QA contract
Date: 2026-10-31
Status: QA DRAFT / NOT INSTALLED IN PRODUCTION
Parent: main commit 8a845ca98e8e136432d2a05d37661180756c8ecd
Backlog: issue #18
Authority: Production Routine v5.0 plus accepted v5.1-A/C, controls v1.132/v1.133.

## Smallest enforceable contract
An execution is not a producer RUN_PASS merely because the ChatGPT scheduler marks its delivery completed or GitHub CI passes.

For each natural Market Monitor run, require the following independently linkable evidence before declaring producer success:
1. STARTUP_AUTHORITY_READ: exact repo/ref/commit and hashes or immutable paths for active routine and core controls, read during that execution.
2. PRODUCER_STARTED: run ID, timestamp, linked invocation or producer-start receipt. A scheduler no_update with null chat_ref is NOT producer-start proof.
3. PRODUCER_CLOSED: same run ID, accepted full-slate output, qualified market/decision/Hot Sheet lineage and terminal closure.
4. INDEPENDENT_READBACK: separate authoritative readback of accepted artifact pointers and matching producer closure. Static CI green is not a substitute.

## Fail-closed classification
- Missing startup authority read: STARTUP_UNVERIFIED; no RUN_PASS.
- no_update + null chat_ref and no linked producer start: DISPATCH_OR_HANDOFF_UNVERIFIED, not a proven model failure.
- Producer start but missing matching closure: PRODUCER_INCOMPLETE.
- Producer closure but missing independent acceptance: ACCEPTANCE_UNVERIFIED.
- All four evidence stages verified for same run: eligible for RUN_PASS, subject to existing substantive controls.

## Known regression fixtures
- 2026-10-30 15:15:24Z diagnostic no_update (~1.6 sec), null chat_ref, before v5.1 activation: DISPATCH_OR_HANDOFF_UNVERIFIED.
- 2026-10-30 18:00:00Z ordinary Monitor no_update (~1 sec), null chat_ref: DISPATCH_OR_HANDOFF_UNVERIFIED.
- R21 45/45 CI: proves static CI pass and index integration, NOT a qualified Week9 current-market RUN_PASS.
- R22 completed rescue receipt: proves bounded recovery work, explicitly RUN_INCOMPLETE for current Hot Sheet.

## Demonstration debt
This file defines a QA acceptance contract only. No scheduler-internal authenticated receipt feed or producer instrumentation is established. Next: implement a pure read-only classifier against saved fixtures on this branch; test each classification; only then evaluate minimal integration into existing QA/Health path. Natural scheduled proof is required before production closure. No new task, routine, model, money, Hot Sheet or canonical ledger change.
