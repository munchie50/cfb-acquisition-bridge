# TERMINAL_CANDIDATE
correlation_id: scheduled-11-20261111T190135Z
observed_start_utc: 2026-11-11T19:01:35.735Z
trigger: natural_scheduled_13CT
startup_receipt_blob: 7961558042f128bc06fb08e1a383d14e7f7ac858
startup_receipt_commit: 212d9a46b2ed459203218d5c9c12afb30e5e70e2
controlled_07CT_handoff: NOT_APPLICABLE_TO_13CT
stage_authority_read: PARTIAL_PASS; Week11 Friday handoff blob 97c7be5d739e921978ae1aaab7b7e0bcb14c552c; prediction pointer blob 15b8572f331daa18f6779e460ea52e15cf648bff; helper blob b13930cb714eb87c8dce6136ffab6fbceeb44898
stage_git_probe: FAILED
failure_category: DNS_RESOLUTION
first_failing_operation: git ls-remote https://github.com/munchie50/cfb-acquisition-bridge.git refs/heads/main
sanitized_error: fatal: unable to access HTTPS repository: Could not resolve host: github.com
exit_code: 128
shell_tool: container.exec
network_only_permission: UNAVAILABLE_NOT_EXPOSED
clone: NOT_ATTEMPTED
helper_execution: NOT_ATTEMPTED; same github.com DNS route blocked
full_worktree: NOT_VERIFIED
immutable_review_validation: NOT_RUN
current_CBS_acquisition: NOT_EXECUTED
six_market_current_decisions: NOT_EXECUTED
compiler_and_render: BLOCKED_BY_WORKTREE_AND_QUALIFIED_INPUTS
canonical_publication: NOT_EXECUTED
selected_live_sheet_readback: NOT_EXECUTED
classifier_execution: NOT_RUN
independent_sweep: PARTIAL; authenticated Week11 delivery handoff and updated accepted prediction pointer recovered, no new game-specific material certification
next_safe_action: resume on existing natural Monitor invocation with working Git transport; fresh read authority and current source clocks; preserve original cutoffs and existing sheet
terminal_status: RUN_INCOMPLETE
credentials_logged: false
