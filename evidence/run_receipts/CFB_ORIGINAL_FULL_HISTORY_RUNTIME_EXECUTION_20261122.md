# CFB original full-history runtime — actual execution evidence

status: SUPPORTED_GIT_RUNTIME_VERIFIED (isolated manual executor); canonical publication NOT_ACCEPTED
source: authenticated public GitHub HTTPS clone of munchie50/cfb-acquisition-bridge, `main` pinned independently to `fbda9547ed732a4df3c3cf7628f4e48b474a23c6`
executor: Firecrawl-hosted isolated Bash/Python environment; installed genuine Git 2.39.5 using apt-get; Python 3.11; no production changes
original_helper: scripts/cfb_runtime_checkout.py --destination /tmp/cfb-governed-verified --expected-head fbda9547ed732a4df3c3cf7628f4e48b474a23c6
original_helper_exit: 0
original_helper_stdout_status: SUPPORTED_GIT_RUNTIME_VERIFIED
original_helper_stdout_head: fbda9547ed732a4df3c3cf7628f4e48b474a23c6
original_helper_stdout_checkout_source: github_https
original_helper_verified_immutable_reviews: 64
full_ancestry_check: PASS, nonshallow repository; detached pinned commit; required original compiler files present
first_previous_blocker: original shell Git executable and full-history checkout unavailable — **RESOLVED FOR THIS ISOLATED MANUAL EXECUTOR**
subsequent_original_readonly_probe: python3 scripts/cfb_recovery_consumer_preflight.py --index evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_295.md --repository-root . --as-of 2026-11-22T20:11:17Z
preflight_exit: 1
preflight_error: ValueError: stale recovery pointer: evidence/operational/CFB_EXECUTION_LEDGER.md
preflight_disposition: READONLY_POINTER_STALENESS_CONFIRMED; do not rewrite historical index or silently advance pointers; separate governed index candidate and consumer contract acceptance needed
scope_limit: this verifies original helper and all 64 immutable review refs in a real complete Git worktree, NOT the automation worker environment, source freshness, accepted decision binding, market quotes, or canonical RUN_PASS. No wagering, scientific promotion, schedule, or cash mutations.
