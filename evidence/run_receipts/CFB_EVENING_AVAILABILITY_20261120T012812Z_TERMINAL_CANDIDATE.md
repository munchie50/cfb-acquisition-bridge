# EVENING TERMINAL CANDIDATE
cycle: CFB_EVENING_AVAILABILITY_20261120T012812Z
trigger: SCHEDULED
status: RUN_INCOMPLETE
first_worker_utc: 2026-11-20T01:28:12Z
scheduler_reported_actual_start: UNKNOWN
startup_receipt: evidence/run_receipts/CFB_EVENING_AVAILABILITY_20261120T012812Z_RUN_STARTED.md
startup_readback: PASS, blob 6ab0923e37e25152caee8e8f40654cb0d6798d2b
fresh_main_observed: aac55662876bb2a2abf1b9b8b1b7b957b44ad46b
latest_recovery_index: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_295.md
index_tree_blob: ebc25a8385ba82b0988cdbe39507d3a793c71e1e
index_tree_bytes: 308845
index_fetch: NONEMPTY, beginning/end present; full local byte/hash independent verification not performed
runtime_direct_shell_probe: PASS, Python 3.13.5, Git 2.47.3
combined_exec_command: UNAVAILABLE in connector orchestration namespace
helper_metadata: scripts/cfb_runtime_checkout.py, 3780 bytes, blob b13930cb714eb87c8dce6136ffab6fbceeb44898
first_operational_blocker: CHECKOUT_DNS_BLOCKED: git ls-remote https://github.com/munchie50/cfb-acquisition-bridge.git HEAD -> fatal: Could not resolve host: github.com
helper_execution: NOT_STARTED; DNS failure independently demonstrated before clone; no repeated checkout
verified_git_worktree: NOT_AVAILABLE
fresh_complete_CBS_source: NOT_ACQUIRED
compiler/readiness/typed_handoff: NOT_REACHED because no verified worktree
current source provenance: index v1.295 selects November 19 70-game/140-row capture, historical and not fresh for this run
market_decision_mutations: NONE
Hot_Sheet_publication: NONE (Monitor sole owner)
execution_ledger_mutations: NONE
independent_work: fresh connector main tree, latest authority identification and readback, terminal audit
firecrawl_spend: NONE
next_supported_action: restore github.com DNS in scheduled worker, rerun exact pinned helper in a subsequent existing slot, then obtain fresh CBS and complete typed handoff
scientific_or_Champion_effect: NONE
schedules: UNCHANGED
