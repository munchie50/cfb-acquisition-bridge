# CFB Engine Health Terminal Candidate — 2026-10-27

- cycle_id: CFB_ENGINE_HEALTH_20261027T222334Z
- candidate_at_utc: 2026-10-27T22:27:59.825Z
- authority_path: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md
- authority_blob_at_recovery: ddeca11cea78e0df52aeade13cf5b5c56c97d850
- run_started_blob: bdd165e2d37ff82e4f39fb62d33094ad28eb6376
- health_audit_path: evidence/scheduler_qa/CFB_ENGINE_HEALTH_20261027T222334Z_AUDIT.md
- health_audit_blob: 9fbdd0fc73b7d128dcca37f30d04d0439c1a05e5
- current_selected_frontier_commit: 0a20ffdc28278ed4ab6c5f2988f85ecf53faa3c6
- current_hot_sheet_path: evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-27_1721CT.md
- current_hot_sheet_blob: 95d094e51f103338a4d4c5db3509da9fb32aabc4
- market_state_blob: c01f80d016cf23c988d3480354c8bd68f24071b7
- decision_ledger_blob: 96a3b543ab0fc3b272079ce15ba7f2cb0441d843
- execution_ledger_blob: 1a938f42e9f03e723bd50348f8a78dbd8b7098e9
- scorecard_blob: 1e8e0a9c3cd34c163c32f6782cdfccf30b9e13d8
- topology: FOUR_ENABLED_RECURRING_TASKS; ONE_PRIMARY_HOT_SHEET_PRODUCER; NO_MUTATION
- scheduled_monitor_cycles_audited: CFB_MARKET_MONITOR_20261027T115654Z=RUN_INCOMPLETE; CFB_MARKET_MONITOR_20261027T175928Z=RUN_INCOMPLETE
- evening_new_due_cycle: NONE_TUESDAY
- manual_recovery_cycle: CFB_MARKET_MONITOR_20261027T220849Z
- manual_recovery_state: CURRENT_SHEET_SELECTED; CI_40594891746_IN_PROGRESS_AT_BOUNDARY; TERMINAL_CANDIDATE_AND_CLOSURE_ABSENT
- historical_closure_debt: CARRIED_FORWARD
- health_mutation: NO_MATERIAL_CHANGE
- firecrawl_chargeable_work: NONE
- blocker: current manual producer terminal completion and passing selected-publication CI were not proved at the Health boundary; scheduled Oct 27 cycles remain durably incomplete; historical debt remains.
- next_safe_action: existing producer invocation completes its own CI and two-phase terminal closure; Health does not replay or dispatch.
- result: RUN_INCOMPLETE

RUN_INCOMPLETE
