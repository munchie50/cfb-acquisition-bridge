# Scheduler V6 exact-path receipt probe

Status: QA OBSERVATION; trigger failure not yet proven.

ChatGPT task state readback: four enabled production tasks. Market Monitor scheduled 07:00 and 13:00 America/Chicago, last_run_time 2026-10-08T12:00:52.813719Z (07:00:52 CT). A separate Health task reported invocation after the 13:00 CT boundary. This is a discrepancy, not causal evidence.

Exact GitHub main path checks:
- evidence/run_receipts/CFB_RUN_STARTED_2026-10-07_1300CT_MARKET_MONITOR.md: FOUND, blob 76014f644fce283b3fa26c2e8b2950008bdff1bc.
- evidence/run_receipts/CFB_RUN_STARTED_2026-10-08_0700CT_MARKET_MONITOR.md: NOT_FOUND (404).
- evidence/run_receipts/CFB_RUN_STARTED_2026-10-08_1300CT_MARKET_MONITOR.md: NOT_FOUND (404).
- GitHub indexed code search for these Oct 8 filenames and CFB_CANARY_V5: zero results; not an exhaustive tree listing.

Inference boundary: missing exact filenames cannot prove that the scheduled task did not trigger, because alternate timestamped filenames may exist. The last-run metadata also cannot prove a run's terminal completion. Next diagnostic must obtain an exhaustive run-receipt directory/tree listing or platform invocation/failure log, correlate invocation IDs with terminal receipts, then execute a scheduled diagnostic if needed. Manual 49-row diagnostic has independently read-back two-phase closure but does not certify automatic triggering.

No production task changes, canonical mutations, frozen model changes or wagers.
