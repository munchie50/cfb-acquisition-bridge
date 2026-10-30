# CFB automation anticipation and reliability QA — 2026-10-30

Status: QA ONLY / NOT PRODUCTION PROMOTION. Independent of running temporary CFB recovery.

## Verified routine differential
Accepted commit d698f46897fd4138c8bda3c64ea7c2742b6ffeab adds evidence/CFB_ROUTINE_V5_1_SELECTIVE_PRODUCTION_AMENDMENT_20261030.md to base v5.0. A = bounded independent-work sweep at evidence WAIT. C = staged material-correction closure with producer demonstration and independent reconciliation. B remains QA. Amendment explicitly makes no scheduler configuration, task-count, market-source or model changes. Thus v5.1 cannot presently be identified as root cause of scheduler NO_UPDATE without further evidence.

## Observed execution contrast
Friday 2026-10-30 13:00 CT Market Monitor task receipt 98ff3b68-c558-8324-b75e-3aaf1c1341c8 returned NO_UPDATE after ~1 second, no chat_ref. Earlier accepted manual comparative run CFB_MARKET_MONITOR_20261030T010121Z_RUN_CLOSURE.md shows saved manual RUN_PASS, not natural Friday producer proof. Historical evidence/scheduler_qa/CFB_SCHEDULER_V6_PRODUCTION_DISPATCH_VS_PERSISTENCE_GATE_2026-10-08.md documents independent dispatch-not-evidenced and canonical-write-blocked failure classes. Do not conflate them.

## Anticipatory automation QA proposal (no deployment)
1. Preflight before scheduled run: validate task enabled/cadence, repo read permission, authoritative state pointers, current game calendar, acquisition budget, and whether source access is sufficient. Record distinct PASS/WAIT/FAIL reason codes.
2. Execution heartbeat: emit immutable STARTED receipt early, then per-stage progress (authority, slate, sources, material news, decision, publication, integration), preserving last completed stage and source clocks. A missing heartbeat is a diagnostic signal, not proof of a failed model.
3. Post-run watchdog: compare scheduler receipt status with producer receipts, canonical file hashes, CI and user-facing Hot Sheet freshness. Explicitly distinguish NO_UPDATE, START_ONLY, WRITE_REJECTED, PARTIAL_SOURCE, PUBLISHED_UNVERIFIED and RUN_PASS.
4. Bounded recovery: resume from verified last completed stage, preserve idempotency and frozen inputs, re-fetch only missing source/game/market branches. No silent changes to pass decisions, deadlines, or expired conditions.
5. Escalation and safety: alert for missed user decision cutoff, stale Hot Sheet or insufficient coverage; fail closed for unsupported bets. No autonomous wager placement, champion promotion, schedule/task mutation or budget expansion.
6. Learning loop: log failure signature, root-cause evidence, repair action, before/after time and source credits, repeated-failure counts; promote only measured QA improvements.
7. Independence: QA runner verifies producer output; green static CI alone is not acceptance. Serialize authoritative writes and reconcile parallel research before publication.

## Next QA acceptance
Compare a successful natural scheduled run and a failed NO_UPDATE at dispatch/STARTED/persistence boundaries. Implement and test read-only classification first; then shadow monitoring without modifying four production tasks. Only promote if measured lower recovery time and no false-positive success or recommendation changes. The temporary fifth-slot recovery task is an exception and must be disabled after its one-time attempt, retaining its configuration for reuse.

No claim that this proposal is built, running or accepted. No production changes.
