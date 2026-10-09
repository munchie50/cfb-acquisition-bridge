# Scheduler QA v6 — October 8 receipt-directory recovery

Status: VERIFIED ROOT-CAUSE NARROWING; production defect remains OPEN.

An exhaustive GitHub contents listing of evidence/run_receipts/ on main found 53 entries, including the 2026-10-08 morning Market Monitor receipts under UTC timestamp-based filenames. Earlier exact-name probes missed these; missing guessed filenames are not proof of absent receipts.

Run CFB_MARKET_MONITOR_20261008T115635537Z:
- RUN_STARTED blob 541890e15da763d0012468a286b40554e8542fe3.
- TERMINAL_CANDIDATE blob 36bb04d0d6e0816760218ed17e23b073b63db3c8; classified RUN_INCOMPLETE.
- RUN_CLOSURE blob 32c568b0591625a6b446307cb98ec5109a1f10f0; separate closure read back candidate first.
- Blocker: canonical evidence/operational/CFB_MARKET_MONITOR_STATE.md update rejected by connector safety checks, including one reduced retry after unchanged SHA c8616b340917e5db2674ec6c16581dd0d09275a5. No canonical market update or Hot Sheet refresh persisted.

Conclusions: The October 8 morning scheduled execution triggered, recovered authority, researched market data, and closed honestly as RUN_INCOMPLETE. This is NOT a successful production run. The observed morning failure is in canonical existing-file update permissions/safety or payload path, not inability to write append-only receipts. The separate October 8 13:00 task-invocation discrepancy remains unexplained and must not be collapsed into the morning write failure.

Next minimal isolation: compare diagnostic-only append/create success against SHA-guarded update of an isolated existing scheduler_qa fixture, then classify tool-policy block versus stale SHA versus payload-content rejection. Never use canonical market state as a test target. Preserve four production tasks and immutable frozen model.
