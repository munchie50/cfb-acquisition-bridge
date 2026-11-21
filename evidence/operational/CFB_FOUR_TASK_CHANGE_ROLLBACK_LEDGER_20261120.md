# CFB four-task change and rollback ledger — November 20, 2026

Status: BACKUPS VERIFIED / ROLLBACK PROCEDURE DOCUMENTED / RESTORE TEST NOT PERFORMED.
Authority: current accepted constitution, active contracts, recovery index, repository accepted artifacts. This ledger is operational provenance, not new model/publication authority.

## Verified snapshot and restoration map

| Task | Automation ID | Exact precompaction backup path | Backup blob SHA | Backup prompt chars | Current prompt chars | Current relationship |
|---|---|---|---|---:|---:|---|
| Market Monitor | 6ae766e788d881919726d0eeb44450dd | evidence/operational/CFB_MARKET_MONITOR_TASK_PROMPT_BACKUP_20261120_PRECOMPACTION.md | 91c14d252c625b55a9b816c137cd737bc9d2f9c1 | 55973 | 7102 | COMPACTED; exact backup independently parsed |
| Weekly QA | 6ae76c7a6d38819190b5cae3bdd6cc53 | evidence/operational/CFB_WEEKLY_QA_TASK_PROMPT_BACKUP_20261120_PRECOMPACTION.md | 66c143dbbde7577b325b5e903c9a70f0635050ba | 53138 | 6139 | COMPACTED; exact backup independently parsed |
| Engine Health | 6ae76df2ece4819197f91fb10076dea7 | evidence/operational/CFB_HEALTH_TASK_PROMPT_BACKUP_20261120_PRECOMPACTION.md | 3783e1a11dda99d985f7501b10e6da85ad867f32 | 53518 | 53518 | NOT COMPACTED; exact active prompt equals backup |
| Evening Availability | 6ae76df60e0c819182e2cfab1b83846a | evidence/operational/CFB_EVENING_AVAILABILITY_TASK_PROMPT_BACKUP_20261120_PRECOMPACTION.md | bc36577ebd9ed5c948600d58998087d7f2a408e4 | 48337 | 48337 | NOT COMPACTED; exact active prompt equals backup |

All four tasks observed enabled; schedules independently peeked and not mutated in this backup/ledger operation. Existing schedules: Market Monitor daily 07:00 and 13:00 CT; Weekly QA Saturday/Sunday 09:00 CT; Health daily 16:30 CT; Evening Wednesday/Thursday/Friday 19:30 CT.

## Related committed evidence

- Market Monitor exact prompt backup commit: 409945df12e6415ade0e45447f11bb584f19c76f.
- Weekly QA exact prompt backup commit: 8c41dd8668029f9f67f79dc7750f07808f25e326.
- Health exact prompt backup commit: 897116a8c4eb9c14a859b4793d223bf84354b8e7.
- Evening exact prompt backup commit: d549baf8c54e4e438055e0b74a98ef48f4456737.
- Saturday 58-row frozen eligibility (46 numeric, 12 excluded) checkpoint: a0feaef85cc6846a5613e6a229563bfa20828441.
- Early-cohort manual read-only receipt: evidence/run_receipts/CFB_MARKET_MONITOR_MANUAL_EARLY_COHORT_READONLY_20261120.md.
- Evening handoff corrections: evidence/run_receipts/CFB_EVENING_AVAILABILITY_20261121T013041433Z_EVENING_DOWNSTREAM_HANDOFF.md.
- Active compacted prompts are stored in the automation service; exact postcompaction copies are not yet independently committed in GitHub. A future complete change audit should add SHA-pinned postcompaction copies and a restore dry run.

## Bounded rollback procedure (only on explicit authorized regression fix)

1. Fresh-peek target automation, capture active prompt, schedule, enabled state, next trigger and last execution receipt; write a new append-only pre-rollback snapshot and independently read it back.
2. Fresh-fetch the exact backup blob above from GitHub main, verify its blob SHA, parse only the prompt after the first \n---\n separator, and compare recovered character length against this ledger. If SHA/length differ, STOP; do not guess.
3. Confirm accepted authority still permits restoration: old prompts contain retired DNS/checkout paths, outdated deadlines and contradictory historical instructions. A blind full restoration could reintroduce known defects. Prefer targeted reversion of the affected clause when possible; if full rollback is explicitly authorized, retain current higher-priority safety guard and document the resulting prompt precisely.
4. Update ONLY the target existing automation prompt, not schedule, enablement, model, other tasks or ledger. Fresh-peek and compare exact restored text, schedule and enabled state; record timestamp, operator, reason, before/after SHA, affected receipts and regression test.
5. A saved rollback is NOT a successful engine run. Prove next natural execution and original canonical acceptance independently. Do not create a fifth task.

## Open drift / next action

- Health and Evening prompts still carry 53,518 and 48,337 characters respectively; backup is now verified, but controlled compaction and actual runtime QA remain outstanding.
- Market Monitor and Weekly QA compaction readback passed, but no controlled restore dry run or end-to-end production acceptance passed.
- Friday 13:00 CT missed cutoff remains missed. Current complete six-market review, qualified offers, compiler and accepted canonical Hot Sheet are not verified. No betting authority created by this ledger.
