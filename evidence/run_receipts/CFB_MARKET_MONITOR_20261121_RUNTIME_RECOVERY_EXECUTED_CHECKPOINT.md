# November 21 CFB runtime recovery — actual executed checkpoint

Status: HOSTED_RUNTIME_RECOVERED_AND_ORIGINAL_VALIDATOR_PASS / PRODUCTION_RUN_INCOMPLETE / NO_NEW_WAGERS.
Authority snapshot: GitHub main 47e02dfad2fc003fbaba154b1db3a4a52fd4ded6, latest preceding checkpoint evidence/run_receipts/CFB_MARKET_MONITOR_20261121_13CT_MANUAL_CATCHUP_CONTINUATION.md. This receipt supersedes the missing-Git limitation **only for the tested hosted session**, not for future automation workers.

## Actual independent tests (2026-11-21)
1. Tested conversation container: Git 2.47.3 present; direct unauthenticated HTTPS repository probe failed name resolution. Abandoned DNS diagnosis NOT reopened.
2. Opened independent Firecrawl-hosted Bash session. Initially Git absent, empty /data/workspace. Verified root and apt-get available. Executed apt-get update and apt-get install git; both exit 0; git version 2.39.5.
3. Ran GIT_TERMINAL_PROMPT=0 git clone --no-checkout https://github.com/munchie50/cfb-acquisition-bridge.git repo in hosted session; exit 0; HEAD 47e02dfad2fc003fbaba154b1db3a4a52fd4ded6. Checked out main; git rev-parse --is-shallow-repository=false, git rev-list --count HEAD=4878; git fsck --connectivity-only completed without reported errors.
4. Executed unchanged original scripts/cfb_runtime_checkout.py --destination /data/workspace/verified_checkout --expected-head 47e02dfad2fc003fbaba154b1db3a4a52fd4ded6; exit 0; status SUPPORTED_GIT_RUNTIME_VERIFIED; Python 3.11.2; 64 immutable historical review references verified by original loader; checkout source github_https. This is the original full-history ancestry and immutable-review validator, not a synthetic substitute.
5. Executed python -m unittest discover -s qa -p test_cfb_runtime_checkout_bundle.py -v against verified checkout; exit 0; 5 tests OK including bad pin, bundle digest mismatch, digest required, local bundle immutable gate, stale main.

## Acceptance boundary and next unfinished action
- Original Git runtime and immutable review gate: EXECUTED / PASS in hosted session. Firecrawl ephemeral session provisioning does NOT prove permanent scheduled-worker runtime repair.
- Already passed Nov21 original selector integration and canonical selector readback remain closed; Nov20 CBS/70-game reconstruction remains closed. Do not repeat absent changed inputs.
- First unfinished action: use verified checkout to perform original production preflight/readiness and prospective source/market qualification for still-open games, recording exact commands, input timestamps and offers. Do not fabricate named-book offers, reopen elapsed cutoffs, or convert 68 historical PASS classifications to wagers.
- Canonical Week12 acceptance/publication remains HOLD pending genuine nonprovisional evidence, governed transaction and independent readback. Production Market Monitor remains RUN_INCOMPLETE. No canonical ledger/index, Champion v1, FIRST_FROZEN, wager, money, or automation schedule changes.

## Reuse note
Hosted session identifier 01a1ffa9-fe10-7228-a6f5-cf223862f621; Firecrawl scrapeId 01a1ffa9-fd20-7559-aba0-6f17558c2aba; verified checkout /data/workspace/verified_checkout. Session persistence is not guaranteed; if unavailable, provision Git via apt and run unchanged original checkout again only as needed for a new worker.
