# Market Monitor manual recovery startup trace

- observed_utc: 2026-11-03T01:00:00Z (approximate, derived from Monday evening local-time observation; NOT a measured clock timestamp)
- trigger_type: user-requested manual run via existing CFB Market Monitor Rebuilt run_now
- correlation_id: CFBMM-MANUAL-20261102-RECOVERY
- task_id: 6ae766e788d881919726d0eeb44450dd
- stage: RUN_STARTED
- result: STARTUP_TRACE_ATTEMPT
- authority: munchie50/cfb-acquisition-bridge main
- caution: observed time approximate; no fabricated exact invocation ID

## Stage and closure
- AUTHORITY_READ: VERIFIED. Recovery index v1.249; accepted Week10 S0 pointer and Monday handoff read from main.
- SOURCE_COVERAGE: VERIFIED. R91/R93 63 games, 378 branches; R93 all WAIT as of its recorded cutoff, not canonical decisions.
- MATERIAL_GATE: WAIT. Official MAC Nov3 reports still pending on Nov2 evening; expected Nov3 17:00 and 18:00 CST.
- MARKET_GATE: INCOMPLETE. No authenticated operator-level executable quote evidence in current accepted records; qualification script not executed in this invocation. Do not claim it ran.
- DECISION_PRODUCER: NOT_RUN; input evidence prerequisites unmet. No canonical ledger mutation.
- PUBLICATION: NOT_RUN; no current authenticated decision rows. Preserve last accepted Hot Sheet.
- failure_category: MISSING_INPUT (official current-game availability and executable operator quote proof). fallback_attempted: official MAC read; fallback_result: reports pending. classifier_execution: NOT_RUN.
- terminal: RUN_INCOMPLETE; this is an accurate bounded manual recovery, not RUN_PASS. Next action: recheck MAC at report release and collect venue-attested quote evidence; then run existing qualification/decision/publication gates.
