# CFB Saturday 13CT manual catch-up — scoped continuation

Status: MANUAL_CATCHUP_IN_PROGRESS / PRODUCTION_RUN_INCOMPLETE / NO_WAGERS.
Source run: scheduled-20261121-1300-ct-turn11; natural scheduler closure RUN_INCOMPLETE.
Authority: original contracts, recovery index v1.295, retained November 20 reconstruction and November 21 run receipts. Do not promote noncanonical preview or renew elapsed cutoffs.

## Fresh-read evidence
- Saturday 13CT frontier: evidence/run_receipts/CFB_MARKET_MONITOR_20261121T190208Z_13CT_FRONTIER_RECONCILIATION_NONCANONICAL.md SHA 978b23cff1ddbd3d2d335107b18801bb6e6b442f.
- Preserved 70-game preview: 68 PASS (not wagers), two closed historical conditionals, zero inconclusive; not accepted. 58 Saturday matchups, 12 original exclusions; 20 saved kickoff windows at or before the afternoon worker start; 38 later windows not automatically eligible because original cutoff authority and named-book offers unverified.
- Existing read-only adapter: scripts/cfb_overlay_publication_probe.py, previous commit b6a37b372e19e2310e9d214f6cb6934ce97bfa82. It now rejects duplicate cycles and non-increasing UTC timestamps in paired packet streams.
- Existing original selector gate requires exact full decision ledger SHA and recovery-index canonical decision pointer; unchanged.
- Existing QA: qa/test_cfb_overlay_preview_binding.py. Newly added regression fixture had double-escaped literal packet framing. Corrected in commit ac6c23bb0c1e315a2acdbc951ebbf1f4ceb0d01a; fresh GitHub readback verified. No tests executed in this turn; do not mark QA PASS.

## Completed in this catch-up
1. Fresh-read actual 13CT reconciliation and latest overlay/QA sources.
2. Detected and corrected malformed newly added QA fixture, read back from GitHub main.
3. Preserved canonical ledgers, selector, Champion, schedules, frozen predictions, wagers, money and historical cutoffs.

## Unfinished, ordered
1. Execute qa/test_cfb_overlay_preview_binding.py with original existing QA and report actual results. Correct any observed regression without weakening gate.
2. Execute actual immutable Week12 manifest-pinned pair reconstruction and original selector integration QA, using verified Git blob inputs and retained lineage; test stale lease/parent/sequence and duplicate/missing/reordered pairs. Distinguish fixtures from real-data validation.
3. Independently qualify only genuinely prospective games against original deadline and timestamped named-book offers. Do not retroactively authorize Saturday games or use historical prices as executable quotes.
4. Governed selector decision: no automatic canonical ledger/recovery pointer promotion from a noncanonical preview. Run original publication gate only after approved state and exact readback.
5. Record final RUN_PASS only if all original production obligations genuinely met; otherwise RUN_INCOMPLETE with precise remaining blockers.

Do not repeat abandoned DNS troubleshooting or already completed CBS 70/70 normalization/compiler. No fifth automation.

## Subsequent manual catch-up increment — execution boundary audit
- Fresh-read this checkpoint at blob b2cb994c9fca4118868cf66173f7841f8bf73b5f and the corrective GitHub commit ac6c23bb0c1e315a2acdbc951ebbf1f4ceb0d01a.
- Queried commit-associated GitHub workflow runs: empty list. This endpoint is scoped to pull-request-triggered runs, so empty is NOT proof that no other CI ran. Do not claim regression tests passed.
- Attempted local repository access once; unavailable in the current runtime. Do not pursue DNS or checkout diagnostics; avoid fabricating execution evidence.
- Current result: code and fixture are persisted, QA EXECUTION_UNVERIFIED, original publication BLOCKED, production RUN_INCOMPLETE. No production mutations or schedule changes.
- First unfinished action remains execute corrected qa/test_cfb_overlay_preview_binding.py and original selector integration QA in a working repository runtime, capture actual stdout/exit codes and pinned commit. Next, validate immutable real Week12 pair and governance gate. No premature acceptance.

## Drift review — later same-day manual continuation
- Fresh-read source identities on main: overlay probe 16028db308e15399e0c3de036d05d01fa4d5525a; original canonical binding gate 8a6022e3aeea0d5c5fc0e9d455a9b56b4f1eb581. Both unchanged from the previously reviewed versions.
- QA file now has blob 6c4a7f1ed7cdb670c447fde8d2bc4174c9658b89 rather than the earlier readback SHA after the fixture fix. The corrected packet framing remains present. Treat this as a concurrent content change requiring commit-level provenance before attributing it; do not blindly overwrite.
- No local runnable checkout: direct attempt failed at host resolution; abandoned network diagnostics not reopened. Connector reads remain available. Commit-associated workflow query returned no PR-triggered runs, not an exhaustive CI inventory.
- Tests remain EXECUTION_UNVERIFIED, not PASS. Original selector still rejects noncanonical preview and requires canonical recovery pointer; no authorized canonical promotion.
- Next: inspect provenance of changed QA blob, execute real regression suite in an authorized runner, then actual pinned Week12 reconstruction; do not rerun completed CBS acquisition.

## Resolved false-positive drift — verified GitHub commit provenance
- GitHub commit-history query for qa/test_cfb_overlay_preview_binding.py shows latest path change ac6c23bb0c1e315a2acdbc951ebbf1f4ceb0d01a (fixture escaping correction).
- GitHub commit details for ac6c23b identify resulting file blob 6c4a7f1ed7cdb670c447fde8d2bc4174c9658b89.
- Fresh fetch_file at exact commit and at main both return that same blob, with identical 11134-character content. The earlier reported 4985caa326dc7a41cb0c2273231d16b6d8d54bb9 was a bad prior readback identity, NOT evidence of an intervening modification.
- Close QA-file drift finding as FALSE_POSITIVE_PROVENANCE; no code rewrite necessary. Preserve corrected fixture and focus next on actual test execution and real-data integration. Do not mark execution PASS from GitHub commit identity alone.

## Confirmed root-cause correction — wrong first-failure path
- Saturday 13CT receipt first_failure attempted evidence/operational/CFB_WEEK12_20261120_MANUAL_PROVISIONAL_RELEASE.md and got HTTP 404.
- Fresh GitHub directory enumeration of evidence/operational on main reveals the ACTUAL release path evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_MANUAL_PROVISIONAL_RELEASE.md, Git blob 80d2974a40e07481f4886568ee79ca8c7109290b. Fresh fetch_file succeeded and read its full release contract.
- Thus the 404 was a WRONG_PATH retrieval defect, not proof the release was missing or that source acquisition needed restarting. Existing release explicitly authorizes noncanonical manual delivery of the preserved 70-game preview, but disclaims canonical acceptance, original deadline satisfaction and wagering authority.
- Canonical selector design evidence/operational/CFB_WEEK12_SELECTOR_PUBLICATION_TRANSACTION_DESIGN_20261120.md blob 90573bccd14ad5139628fdb40b992b705be10536 independently confirms the selector mismatch is distinct and already designed as a governed, unapproved transaction; don't duplicate or promote its detached QA candidates.
- Operational fix for future Monitor handoffs: use the actual verified release path above and follow its linked rendered preview. Do not edit historical immutable run receipts or loosen canonical gate. Any production automation prompt edit requires fresh prompt read and scoped change review.
- Remaining: test execution evidence and canonical integration remain unverified. No accepted wagers or RUN_PASS.

## Production task instruction correction — verified
- Read live existing Market Monitor task 6ae766e788d881919726d0eeb44450dd. Its active prompt contained exactly one stale path evidence/operational/CFB_WEEK12_20261120_MANUAL_PROVISIONAL_RELEASE.md and no occurrence of the actual release path.
- Applied smallest possible in-place prompt correction, replacing that exact path with evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_MANUAL_PROVISIONAL_RELEASE.md; no other prompt text altered.
- Independent automation peek readback verified entire replacement prompt byte-for-byte, stale path absent, correct path present, identical schedule and enabled status. No new task, no schedule change, no canonical ledger/index or wager mutation.
- Status: WRONG_PATH_INSTRUCTION_DEFECT_FIXED_AND_READBACK_VERIFIED. Future worker execution still unverified; publication selector and executable-offer blockers remain distinct and unresolved. Do not claim RUN_PASS from task prompt update.

## Actual Python execution — overlay regression QA PASS
- Staged exact main sources via authenticated GitHub fetch_file into isolated hosted Python 3.11 environment: scripts/cfb_overlay_publication_probe.py blob 16028db308e15399e0c3de036d05d01fa4d5525a, qa/test_cfb_overlay_preview_binding.py blob 6c4a7f1ed7cdb670c447fde8d2bc4174c9658b89, plus original cfb_hot_sheet_current_decision_binding_gate.py, cfb_week12_publication.py and cfb_recovery_navigation_reader.py.
- First test attempt returned exit 1 because isolated staging omitted existing cfb_recovery_navigation_reader module (ModuleNotFoundError). Staged that existing dependency; no source patch needed.
- Reran exact command python -m unittest discover -s qa -p test_cfb_overlay_preview_binding.py -v; subprocess exit 0; 11 tests in 0.008s, OK. Explicitly includes duplicate/reordered cycle regression and provisional fail-closed binding cases.
- This is EXECUTED/PASS for the 11-test overlay unit suite, not actual Week12 manifest data, canonical selector integration, lease/CAS proof, fresh sportsbook qualification, or scheduled worker RUN_PASS.
- Next unfinished: run original selector integration QA and actual immutable manifest-pinned reconstructed pair, then governed publication decision. No production data/schedules changed.

## Original selector QA preflight — scoped findings, NOT EXECUTED
- Fresh-read qa/cfb_week12_original_selector_integration_qa.py blob fbdc1ba2a478902c3f6c54ec8e52322dae50036a. Its real immutable base 6862be6a1bd88a3290b1e90a49c33a7a87e92559 plus delta 646bbe85edba726037e1b98125783ff2cd87a4e8 must hash to 98941e228072e6941b1c33e42d4d8dba570f7182; fixture tests are synthetic QA-only and do not accept canonical production.
- Fresh-read actual-canonical readback QA blob a116848b9f050967a8d1fd166b634ec286de0667, which additionally pins both original module blobs, index, ledger, sheet, and real pointers. It supersedes earlier QA script blob identifiers recorded in the selector design document; do not use stale module identity.
- Fresh-read current recovery index blob ebc25a8385ba82b0988cdbe39507d3a793c71e1e; it still contains CURRENT_HOT_SHEET:November19 partial manual catch-up, not Week12 reconstructed canonical acceptance.
- Attempted additional hosted execution for large-blob staging; provider returned maximum concurrent jobs (2), so actual immutable-pair integration was NOT executed. The prior 11/11 overlay unit PASS remains valid; do not conflate with full ledger integration.
- Next: free/obtain hosted execution slot, stage pinned base/delta and preview, execute original selector QA; then independently execute actual canonical selector QA on one pinned remote snapshot. Do not promote noncanonical preview or mutate production pointers.
