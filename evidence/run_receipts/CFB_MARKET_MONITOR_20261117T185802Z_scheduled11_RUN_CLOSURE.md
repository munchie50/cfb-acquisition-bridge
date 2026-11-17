# Market Monitor run closure

observed_utc: 2026-11-17T18:58:02.334Z
correlation_id: 20261117T185717Z_scheduled11
status: RUN_INCOMPLETE
terminal_candidate_path: evidence/run_receipts/CFB_MARKET_MONITOR_20261117T185754Z_scheduled11_TERMINAL_CANDIDATE.md
terminal_candidate_commit: dbc140eaed6f2e75c7dff38417cfa86bd1308e76
terminal_candidate_blob: 003453ee820ab7a42c55aea2b549d48816464ba7
terminal_candidate_readback: PASS (2246 UTF-8 characters)
startup_trace_blob: b6132728ab04d79af89a8ad44fe0376e3eb9b498
first_runtime_failure: urllib.error.URLError: [Errno -3] Temporary failure in name resolution on immutable REST blob transfer
remaining_blocker: helper bytes not materialized in executor; authenticated current index not verified; no current compiler/publication
no_current_publication: true
no_wagers_or_money_changes: true
next_action: use verified connector-to-executor handoff and pinned index in supported runtime, then complete live slate and governed publication
