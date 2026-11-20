# Week 12 Friday 07CT/13CT manual recovery — canonical streams found, runtime Git boundary

Date 2026-11-20. Authority: main archive pinned at 0d1119263521b9b55824a2f12030c54e9fa7c674. Prior source normalizer executed PASS 70/70 in alternate Firecrawl Python runtime. This is an actual stage receipt, not RUN_PASS.

## Drift correction

Initial narrow search for `cfb-week12-source-bootstrap-v1` inside evidence returned no matches and suggested incorrectly that packet streams were missing. A corrected scan for `cfb-week12-market-v1` and `cfb-week12-decision-v1` identified retained canonical streams in `evidence/operational/CFB_MARKET_MONITOR_STATE.md` (6,815,072 Python text characters) and `evidence/operational/CFB_DECISION_WAIT_LEDGER.md` (3,605,685 characters). This explicitly supersedes the earlier missing-input inference. Canonical streams are present. The Hot Sheet's hashes alone were not sufficient to locate these files.

## Executed bootstrap test

Actual invocation in alternate Python runtime: `cfb_week12_publication.bootstrap_check(market_text, decision_text, original_week12_lineage_json)` with exact retained files. Outcome: `FileNotFoundError: [Errno 2] No such file or directory: 'git'`. `cfb_conditional_recommendation_profile.load_review` invokes `git -C <root> merge-base --is-ancestor <review_commit> HEAD`, `git show <commit>:<review_path>`, and commit timestamp readback; Git executable is absent in alternate runtime. Source ZIP has no .git history. Do NOT bypass review ancestry with a stub, monkeypatch, or unverified file contents. No compiler acceptance or production Hot Sheet publication is claimed.

## Next bounded work

Supply a real Git executable and verified full-history checkout/offline Git bundle to the alternate runtime, or an approved equivalent immutable-ancestry verifier with exact commit/path/blob/timestamp checks. Then re-run official bootstrap_check on recovered canonical streams, refresh_rows on a newly retained source captured within 900 seconds, and governed compile/publish/readback. Friday 13CT cutoff remains missed, no retroactive publication or CBS mixed-book executable price claims. Preserve v1 champion/v2 shadow boundaries. Keep 07CT/13CT RUN_INCOMPLETE pending full acceptance.
