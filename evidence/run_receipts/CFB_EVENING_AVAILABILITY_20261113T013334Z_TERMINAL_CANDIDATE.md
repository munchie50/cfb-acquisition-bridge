# TERMINAL_CANDIDATE
cycle: CFB_EVENING_AVAILABILITY_20261113T013334Z
correlation_id: CFB_EVENING_AVAILABILITY_20261113T013334Z
status: RUN_INCOMPLETE
startup: evidence/run_receipts/CFB_EVENING_AVAILABILITY_20261113T013334Z_RUN_STARTED.md (readback PASS; commit 009618bed3836a881297369425a3cd123876cc39)
pre_checkout_visibility: evidence/run_receipts/CFB_EVENING_AVAILABILITY_20261113T013334Z_PRE_CHECKOUT_PACKAGE_VISIBILITY.md (readback PASS; commit 20b1de7c3bbb32624239b186b3d74b742c4912dc)
nominal_slot_ct: 2026-11-12 19:30 CST
scheduler_actual_start_utc: UNKNOWN
worker_first_observed_utc: 2026-11-13T01:33:34Z
scheduled_to_first_observation_seconds: 214 (not scheduler latency measurement)
latest_index: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_287.md; blob 1d45bd5995f5cab1b43679a69c6bc3678a66a0ef; tree size 143253 bytes; complete fetch beginning/end present
checkout: CHECKOUT_DNS_BLOCKED
first_checkout_error: fatal: unable to access 'https://github.com/munchie50/cfb-acquisition-bridge.git/': Could not resolve host: github.com
runtime: Python 3.13.5; Git 2.47.3; connector GitHub read/write available; HTTPS Git DNS unavailable
observed_main_head_before_checkout: 20b1de7c3bbb32624239b186b3d74b742c4912dc
checkout_helper: scripts/cfb_runtime_checkout.py; blob b13930cb714eb87c8dce6136ffab6fbceeb44898; full helper recovered; required Git network route demonstrably blocked; no clone retry
precheckout_producer: NO_MATCHING_RUN_IN_RETURNED_RESULTS for 19:22 CT scheduled workflow 416507937 (bounded 20 schedule runs)
artifact_id: NOT_REACHED_NO_MATCHING_RUN
manifest_source_recovered_by_utc: NOT_REACHED
verifier_actual_utc: NOT_REACHED
source_age_seconds_at_verification: NOT_REACHED
freshness_limit_seconds: 900
package_verification: NOT_REACHED_NO_PACKAGE_AND_NO_WORKTREE
package_consumption: NOT_REACHED
compiler_readiness_and_typed_handoff: BLOCKED_COMPUTATION_RUNTIME_UNAVAILABLE
independent_sweep: recovered latest saved Week11 2026-11-12 14:01 CT Hot Sheet blob 55e6a8da230de0ac8d3b62a006c145b6fef9f1b6; 67 games, 62 PASS, five CONDITIONAL, 0 INCONCLUSIVE, no execution. Saved market observations from 2026-11-12 19:59:54Z are historical and stale at this invocation; no current offer asserted. Paid acquisition not attempted because source budget and worktree gates not established; no independent current source qualified.
operational_mutations: NONE; no new decisions, execution, Champion or competing Hot Sheet
next_supported_action: Repair scheduled runtime Git HTTPS DNS; verify same-slot producer existence and exact artifact; rerun normal typed downstream workflow at next existing slot, without deadline extension.
