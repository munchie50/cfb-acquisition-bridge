# Week12 manual Market Monitor — connector immutable blob smoke test

STATUS: TEST_EXECUTED_AND_READBACK_VERIFIED; LIMITED SOURCE-RECOVERY PRIMITIVE ONLY. NOT A FULL CHECKOUT, NOT PRODUCTION ACCEPTANCE.

Context: manual 07:00 and 13:00 CT Nov20 Market Monitor catch-up. Existing direct Git HTTPS checkout fails worker DNS. This test did not use GitHub Actions or change scheduler tasks.

1. Read current recovery index evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_295.md: blob ebc25a8385ba82b0988cdbe39507d3a793c71e1e.
2. Authenticated GitHub REST recursive tree main read: observed head e8b5c545621b0db469d64d4927bf5b1c0a54ab21; 3083 entries; truncated=false.
3. Read scripts/cfb_runtime_checkout.py by path: blob b13930cb714eb87c8dce6136ffab6fbceeb44898, 3780 characters.
4. Independently fetch same blob by exact SHA using GitHub connector fetch_blob: 3780 characters; exact string equality to path fetch TRUE.
5. Independently fetch the observed head by GitHub connector fetch_commit: SHA e8b5c545621b0db469d64d4927bf5b1c0a54ab21 returned and matched. This wrapper did not expose a parent/commit-tree proof; no ancestry verification claimed.

LIMITATIONS: Matching two connector reads does not establish Git blob hash recomputation, a full authenticated worktree, all source dependency coverage, historical commit ancestry, retained immutable review refs, champion v1 execution, source freshness, or a qualified market observation. These remain open gates. No canonical ledger, frozen model, decisions, money ledger or Hot Sheet modified.

NEXT MINIMAL TEST: compare raw Git blob SHA-1 locally to independently fetched bytes, validate a pinned commit tree and parent chain with authenticated REST evidence, materialize an isolated full dependency fixture, run a deterministic reference test; only then seek approval for any replacement of existing checkout acceptance gate. Continue football and market qualification separately; no retroactive 07CT/13CT approvals.
