# TERMINAL_CANDIDATE — RUN_INCOMPLETE
observed_utc: 2026-11-12T13:04:39.872Z
correlation_id: scheduled-20261112-0700-11
trigger_type: NATURAL_SCHEDULED
startup_receipt: evidence/run_receipts/CFB_MARKET_MONITOR_TRACE_20261112T130402809Z_scheduled-20261112-0700-11.md
startup_blob: 1ca6b00f03d43c40f8757fd5d38df77564070cfd
startup_status: VERIFIED
bundle_receipt_blob: 1653ba3cff6ad39b1b56e90288dcb85d9544f6fa
bundle_pin: 42ecacdd6fc2b303edacfaec2370ee4f3e825887
bundle_compatibility: FAILED; authenticated compare pin...main ahead 35 behind 0, includes modified evidence/plans/CFB_INTEGRATED_BETTING_INTELLIGENCE_ROADMAP_20261111.md and added evidence/audits plus scripts/cfb_parlay_matrix.py; not allowed append-only drift.
checkout_probe: FAILED; git ls-remote HTTPS refs/heads/main exit 128, Could not resolve host: github.com
network_only_permission: UNAVAILABLE (not exposed by shell tool)
clone: NOT_ATTEMPTED (probe failed)
helper_transport: NOT_EXECUTED (no verified complete cross-tool transfer)
direct_api: NOT_ATTEMPTED (same runtime DNS route unavailable)
review_validation: BLOCKED_NO_WORKTREE
independent_recovery: VERIFIED; Friday delivery handoff blob 97c7be5d739e921978ae1aaab7b7e0bcb14c552c; accepted Week11 prediction state blob 15b8572f331daa18f6779e460ea52e15cf648bff; Friday card blob ad26aad424b9695e92879836a9d3a7058d0b63da; latest Saturday review candidate blob 64034099e03f019f4b1d929587ae8b93a374654a.
independent_sweep: Existing 23 Saturday six-market PASS reviews retained; Friday three and five conditional review retained. No new verified live source or review created in this invocation; fresh acquisition/normalizer and immutable review validation require qualified producer/runtime. Do not claim refreshed prices.
compiler: BLOCKED_NO_WORKTREE
publication: NOT_EXECUTED; preserve last verified Hot Sheet
selected_CI: NOT_EXECUTED
classifier_execution: NOT_RUN
failure_category: DNS_RESOLUTION (Git probe); MISSING_INPUT (verified runtime)
next_action: Next natural capable Monitor must recover latest main, use valid checkout, refresh CBS and Friday/Saturday material, revalidate five conditionals, compile, independently read back selected sheet and close.
