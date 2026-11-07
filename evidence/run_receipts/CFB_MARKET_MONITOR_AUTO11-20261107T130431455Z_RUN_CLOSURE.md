# CFB Market Monitor terminal closure
observed_start_utc: 2026-11-07T13:04:31.455Z
trigger_type: scheduled_automation
invocation_id: unavailable
correlation_id: CFBMM-AUTO11-20261107T130431455Z
terminal_outcome: RUN_INCOMPLETE
startup_trace: evidence/run_receipts/CFB_MARKET_MONITOR_TRACE_20261107T130431455Z_CFBMM-AUTO11-20261107T130431455Z.md
startup_trace_blob_sha: 23cda2f8b3e7f50a00215ca5bac9f4415e017e83
main_commit_observed_after_startup: 24e5460f3dd1af46065cde2fdf6c10f424e9fc9d
helper_path: scripts/cfb_runtime_checkout.py
helper_blob_sha: b13930cb714eb87c8dce6136ffab6fbceeb44898
helper_bytes_connector_blob: 3780
helper_base64_chars: 5040
helper_base64_syntax: PASS
helper_runtime_transport: BLOCKED
failure_category: TOOL_NOT_EXPOSED
sanitized_error_excerpt: functions.exec orchestration exposes no exec_command or shell tool; cannot pass structured connector response to binary writer in same tool call without manually transcribing payload. No runtime handoff attempted.
fallback_attempted: independent GitHub fetch_blob; returned 3780 content characters
fallback_result: CONNECTOR_READ_VERIFIED_ONLY
bootstrap_outcome: NOT_EXECUTED
pinned_git_ancestry: NOT_VERIFIED
classifier_execution: NOT_RUN
source_acquisition: NOT_EXECUTED
six_market_decision_rows: NOT_AUTHORED
week10_compiler: NOT_EXECUTED
publication: NOT_EXECUTED
selected_ci: NOT_EXECUTED
next_safe_action: Expose exec_command in the same code orchestration cell as authenticated fetch_file to transfer exact base64 bytes, validate size and git hash-object, then run unchanged helper once and resume current live production; do not substitute a replay or inferred decision.
no_changes: Champion, models, wagers, money, automations and schedules unchanged by this invocation.
