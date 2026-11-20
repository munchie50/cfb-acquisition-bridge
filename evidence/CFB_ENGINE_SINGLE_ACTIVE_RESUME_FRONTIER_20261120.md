# CFB ENGINE — SINGLE ACTIVE RESUME FRONTIER — Nov 20, 2026

**State at last verified main:** `1bc6679c065792410911447955e714a917a261ee` (re-read main before each mutation; this SHA is a checkpoint, not a permanent head). This document supersedes the *next-action instructions* of the older `evidence/CFB_ENGINE_ACTIVE_CONTINUATION_CHECKPOINT_20261120.md`, without superseding its verified evidence or governing authority.

## User outcome and completed work
Friday Nov20 07CT and 13CT manual Market Monitor research recovery COMPLETED through provisional release, not canonical production acceptance. 70-game CBS board, normalizer, official compiler, FIRST_FROZEN preservation, market and decision base+delta, QA reconstruction, preview and independent readback all DONE. Published provisional pointer `evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_MANUAL_PROVISIONAL_RELEASE.md`, complete 70-game preview `evidence/operational/CFB_WEEK12_20261120_MANUAL_RENDERED_HOT_SHEET_PREVIEW_NOT_ACCEPTED.md`, publication commit `045b77db5fa0f98406f24be529a01a74dc555726`. 68 review PASS, two expired historical conditionals, zero INCONCLUSIVE, **zero authorized wagers**. Original scheduled 07CT/13CT internal engine statuses remain RUN_INCOMPLETE; do not backdate or call full production day complete.

## Evidence verified after initial handoff
- Real decision base SHA `6862be6a1bd88a3290b1e90a49c33a7a87e92559`; delta `646bbe85edba726037e1b98125783ff2cd87a4e8`; reconstructed UTF-8 Git blob SHA `98941e228072e6941b1c33e42d4d8dba570f7182`. Independent hash proof receipt `evidence/run_receipts/CFB_WEEK12_20261120_UTF8_EXACT_DECISION_BLOB_INDEPENDENT_VERIFICATION.md`.
- Five equivalent JS real-data binding scenarios and six synthetic Python selector scenarios recorded in receipts; **neither is original-module integration acceptance**.
- Actual `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_295.md` latest explicit frontier Nov19 points to Nov19 sheet blob `4c8ebeb5dd95b7ea7309f45a9275f7509a198905` and old decision base `6862be6a...`. Original selector requires one schema-compliant current sheet path, exact pointer blob, and decision pointer matching supplied ledger. The Nov20 provisional release path is not valid as a canonical sheet path. Detailed audit `evidence/run_receipts/CFB_WEEK12_20261120_EXACT_PRODUCTION_SELECTOR_POINTER_DRIFT_AUDIT.md`.
- QA-only original-module integration test `qa/cfb_week12_original_selector_integration_qa.py` at commit `1bc6679c...`, independently read back, supports `--blob-dir` with connector-staged SHA-named files; this removes `git cat-file` and network checkout for that mode. **Test file built, NOT executed end-to-end.** Its import of `cfb_overlay_publication_probe` is source-only in offline mode, not a git invocation.

## ONE NEXT EXECUTABLE ACTION
**Execute original checked-in modules in offline Python** using GitHub connector-staged exact files, not GitHub HTTPS clone:
1. Via GitHub connector fetch actual original `scripts/cfb_recovery_navigation_reader.py`, `scripts/cfb_hot_sheet_current_decision_binding_gate.py`, `scripts/cfb_overlay_publication_probe.py`, `qa/cfb_week12_original_selector_integration_qa.py`, preview, and the two immutable SHA blobs.
2. Stage locally (Python/container tool) with SHA filenames for blobs and repository-relative paths for sources and preview. **Do not claim this staging has occurred until it has.** If connector data cannot be transferred to Python in this chat, identify that precise transfer boundary; do not fall back to HTTPS, GitHub Actions scheduler, or paid Firecrawl credit-exhausted runtime.
3. Execute `python qa/cfb_week12_original_selector_integration_qa.py --repo <staged-dir> --blob-dir <staged-dir>/blobs`; fix only QA errors; persist exact stdout/stderr and independently read back. Positive pass is QA ONLY, not production acceptance.
4. Then design a governed, content-addressed selector/pointer publication transaction with parent/sequence/lease controls; no canonical mutation before approval and tests.

## Explicit do-not-repeat / no-drift controls
No repeat CBS collection, compiler, full review, hash proof, five/six-case replica tests, DNS/HTTPS checkout diagnostics, GitHub Actions scheduler trials. No fifth scheduled task, no modification of four production task definitions, no Champion/frozen-model/ledger/index mutation, no fabricated sportsbook quotes or wagers, no fake RUN_PASS. Four tasks previously verified enabled. Fresh recheck only if evidence of changed task state or new prospective market/player evidence.

## Mandatory conversation handoff
New chat: read THIS file and fresh main first, then latest receipts and the original module/test sources. If new work succeeds, update/supersede THIS single frontier with exact verified commit, exact completed slice, and exactly one next executable action. Never restart completed slices merely because conversation changed.
