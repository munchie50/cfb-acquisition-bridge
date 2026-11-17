# CFB embedded helper canary RESULT

- Outcome: BOUNDARY_PASS
- Run clock: 2026-11-17 13:32:52 UTC
- Result clock: 2026-11-17 13:34:57 UTC
- Trigger: one-time scheduled invocation
- Invocation ID: not exposed
- Correlation ID: CFB_EMBEDDED_HELPER_CANARY_20261117T133252Z_a27be1c5
- STARTED receipt: evidence/scheduler_qa/CFB_EMBEDDED_HELPER_CANARY_20261117T133252Z_a27be1c5_STARTED.md at 5a6ab5b29ca6132bd2fa39103bb93274a3985658, independently read back with exact contents
- GitHub connector: operational. Authenticated main pinned at 5a6ab5b29ca6132bd2fa39103bb93274a3985658 after STARTED. The helper blob metadata at that commit matched b13930cb714eb87c8dce6136ffab6fbceeb44898.
- Shell startup: PASS. Python 3.12.14 and Git 2.52.0.
- Embedded helper: PASS. Base64 and gzip decoded, byte count 3780 and Git blob b13930cb714eb87c8dce6136ffab6fbceeb44898 matched.
- Checkout: PASS. The command exited 0 with SUPPORTED_GIT_RUNTIME_VERIFIED. The helper verified HEAD 5a6ab5b29ca6132bd2fa39103bb93274a3985658, full non-shallow ancestry, and 60 retained immutable reviews.
- Execution: one attempt in a fresh private destination, using default proxy and Git settings.
- Scope: startup canary only.
