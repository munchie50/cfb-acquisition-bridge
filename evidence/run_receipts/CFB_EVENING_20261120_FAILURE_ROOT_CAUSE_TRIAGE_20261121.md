# Evening 19:30 CT Nov20 — targeted failure triage (noncanonical)

Source receipts: evidence/run_receipts/CFB_EVENING_AVAILABILITY_20261121T013041433Z_RUN_CLOSURE.md (blob 2bc8e5b6c4c9be8e83ab6ac7eb11e7e525fc57a1) and ..._EVENING_DOWNSTREAM_HANDOFF.md (blob 7b510b22ceb6d3b2c8df9e490ec492321aa8ea55), independently fetched in this investigation.

## Observed stage classification
- DISPATCH/STARTUP: PASS, 19:30:27 CT worker start; persisted/read-back RUN_STARTED.
- AUTHORITY: PASS for reading v1.295, but it explicitly selects a Nov19 partial Monitor state. Nov20 provisional preview is NOT canonical.
- CONNECTOR_TO_RUNTIME: BLOCKED. Original Python/full-Git-ancestry runtime not established in this scheduled worker. This is not proof of DNS failure, scheduler failure or missing GitHub file content.
- SOURCE_CAPTURE/FORMAT: BLOCKED for fresh complete CBS 70-game evening capture; three prospective matchup checks are not full coverage.
- OFFER_QUALIFICATION: BLOCKED; observed editorial/mixed-book lines lack independently verified offer update clocks and jurisdiction/venue confirmation. No wagers.
- CANONICAL_WRITE/SELECTOR: NOT EXECUTED; original selector requires one supported canonical CURRENT_HOT_SHEET path and exact decision-ledger pointer. The Nov20 provisional preview cannot be promoted by relabeling. Separate large-ledger write transport failure is historical evidence, not observed anew tonight.
- READBACK/DELIVERY: PASS for noncanonical handoff and closure; user-delivery status UNKNOWN. Scheduler recorded completed != engine RUN_PASS.

## Drift findings
1. Current recovery navigation v1.295 selects Nov19 partial despite Nov20 manual 70-game provisional research. This is an explicit accepted-vs-provisional boundary, not license to overwrite authority.
2. Evening handoff carries only three individually refreshed matchups plus unresolved 70-game cohort. Its numeric game IDs remain NOT_VERIFIED; cannot claim original typed handoff.
3. Original-module selector integration QA file exists at qa/cfb_week12_original_selector_integration_qa.py (current read blob dc7764ca7827c3460c737ecfa37af90ce1ba4cc7) but no verified end-to-end execution. Earlier synthetic checks do not close it.
4. 19:30 task next scheduled slot is Wednesday Nov25; Saturday obligations must be carried by existing Market Monitor/Weekly QA, not by creating a fifth task.

## Smallest safe corrective sequence
A. Existing Saturday Monitor: acknowledge the exact noncanonical handoff and its 3 named matchup IDs; reconcile original cutoffs, live availability and market qualifications for early games. Keep Week12 70-game preview provisional, no automatic wagers.
B. Offline selector QA: stage exact checked-in source modules and immutable decision base/delta into the same Python runtime, verify Git blob identities, execute qa/cfb_week12_original_selector_integration_qa.py --repo ... --blob-dir ... and persist exact output/readback. Do not retry Git HTTPS DNS, Actions scheduler or re-collect already completed Nov20 manual research as a substitute.
C. Only after original QA and approved canonical publication transaction: perform guarded current-sheet + decision-pointer commit with exact blob checks, then independently read back; do not mutate Champion/frozen predictions.
D. Scheduled Evening repair must demonstrate a natural worker's complete current CBS capture, original typed compiler/handoff and independent readback in one invocation. A separate manual or other-runtime success is diagnostic only.

Classification: FAILURE IS DOWNSTREAM RUNTIME/CANONICAL HANDOFF; scheduler dispatch and noncanonical persistence are verified operational. No production status upgraded. No task schedules, canonical ledgers, Hot Sheet or bets changed by this triage.

## Independent continuation check — original modules and actual Monitor schedule
Fresh connector readback: scripts/cfb_hot_sheet_current_decision_binding_gate.py blob 9ff23f2ada4c99a94757fa5f5a86c2f071e54b2a; scripts/cfb_recovery_navigation_reader.py blob b6901d80f3535ee8e218755dda830ef13d3c2869; scripts/cfb_overlay_publication_probe.py blob 298c8ef0245ccfb2ee8bffdf8f7aaa7114ff96b8. The checked-in QA file uses --blob-dir to avoid git cat-file for the immutable ledger bytes. It still requires actual staged files and a Python runtime; its existence is not execution evidence.

Automation readback confirms existing CFB Market Monitor Rebuilt task 6ae766e788d881919726d0eeb44450dd is enabled, scheduled daily at 07:00 and 13:00 America/Chicago, with next slot Saturday Nov21 07:00 CT. This resolves the earlier conditional "if scheduled" handoff language without changing the immutable prior receipt. Existing Evening task next slot Wed Nov25 19:30 CT. No new automation or schedule edit required.

Root-cause split: (i) original selector QA can be exercised with offline exact bytes, but source/blob transfer into same runtime is not verified; (ii) scheduled Evening original compiler and full source capture are a distinct natural-worker capability gap. Do not mark (ii) repaired when (i) eventually passes. No actual test run, typed handoff or canonical publication was performed by this continuation.
