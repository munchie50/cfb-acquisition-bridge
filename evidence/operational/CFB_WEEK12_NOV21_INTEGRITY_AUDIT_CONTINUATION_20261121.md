# CFB Engine — Nov 21 integrity audit, durable continuation checkpoint

Status: AUDIT IN PROGRESS / READ ONLY / NOT ACCEPTED. User ordered end-to-end investigation of whether Nov 16–21 changes improved or damaged the engine, with new chats resuming at the exact stopping point. This file is an AUDIT CHECKPOINT, not a superseding constitution/current-state or publication. Do not restart broad investigation or imply completed acceptance.

## Authority and constraints
Read constitution/master contracts then latest accepted current-state and recovery index; compare actual Git main, current automations and natural receipts. Frozen v1 Champion remains protected. No blind rollback, no new fifth task, no DNS/HTTPS checkout retries, no fabricated wager approvals. Exactly four existing production tasks. Do not modify canonical ledgers/Hot Sheet, scheduler, model or runtime without concrete regression proof and scoped authorization. Use fresh-read, smallest delta, readback, independent validation. Distinguish BUILT, EXECUTED, VERIFIED, ACCEPTED and PRODUCTION.

## Verified during this audit turn
- GitHub repo munchie50/cfb-acquisition-bridge main latest observed commit ca4e17cb9899251c8ca44dbeda8b2aca3bc1d76e (2026-11-21T16:42:07Z). Fresh-read on resume; may advance.
- GitHub compare base 926ad2762f10c4952d1ccc1a688cc93d59f89dfc to main: ahead 99 commits, 49 files changed: 44 added, 5 modified; 42 evidence/docs files and 7 scripts/QA files. This is only a bounded Nov21 slice, NOT complete Nov16–21 diff.
- Modified: qa/cfb_week12_original_selector_integration_qa.py; scripts/cfb_overlay_publication_probe.py; scripts/cfb_runtime_checkout.py. Added: scripts/cfb_data_integrity_gate.py; qa/test_cfb_data_integrity_gate.py; qa/test_cfb_overlay_preview_binding.py; qa/test_cfb_runtime_checkout_bundle.py.
- Fresh-read scripts/cfb_data_integrity_gate.py blob ddba40c9729d75e82a2eb704e54312e0e41e5812: explicitly read-only; detects duplicate IDs, missing six-market fields, conflicting states and alias/source ambiguity; not betting approval. QA blob 59dae8244b0f6834c99174e00f6f2274e019f077. Source inspected; not executed in this audit.
- Fresh-read scripts/cfb_overlay_publication_probe.py blob 04e33ecb646c5ed98eaac63b1b66944b9ad693da: read-only Git blob reconstruction, packet boundary and pair consistency checks; does not authorize publication. Source inspected; not executed in this audit.
- Fresh-read scripts/cfb_runtime_checkout.py blob 6ef3b59688506be2f46c62e8d82a137373a2802d: pinned real worktree, optional authenticated Git bundle, no direct canonical mutation; actual end-to-end transport remains unproven.
- Recovery index evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_295.md blob ebc25a8385ba82b0988cdbe39507d3a793c71e1e selects November19 partial canonical Hot Sheet evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-19_1338CT.md blob 4c8ebeb5dd95b7ea7309f45a9275f7509a198905, which declares 68 PASS / 2 closed conditional and no verified venue offer or automatic bet. Nov21 manual sheet is noncanonical.
- Existing recovery continuation evidence/CFB_ENGINE_SINGLE_ACTIVE_RESUME_FRONTIER_20261120.md blob 9f7d0ad3a9e2bad43378a9092203f94bd0930dd3 describes scheduler prompt overlays, source transfer blockage, unexecuted original selector integration QA, no canonical publication and large task prompts (~44–50K chars). Its Nov20 last-action is historical, NOT this audit's next action.
- Compare to September baseline showed 4256 commits; too broad to attribute this week. No production acceptance claim.

## Preliminary verdict
Concrete progress: content-addressed audit/overlay reconstruction safeguards, regression QA fixtures, read-only Saturday forecast analysis, documented failure boundaries. Material risk: rapid proliferation of evidence and controls, large overlapping scheduled task prompts, original selector QA and natural scheduled production acceptance not proven. No evidence yet that frozen Champion was mutated or destroyed; NOT independently proven intact. No evidence that this week's changes yielded a working end-to-end actionable Hot Sheet. Do not label audit complete.

## Exact next steps — resume here, do not repeat above
1. Establish Nov16 baseline commit using GitHub commit search with date qualifiers or pagination and compare Nov16..current main. Classify changed files into model/frozen, canonical ledgers/pointers, runtime/scripts, QA, automation workflows, evidence/docs. Inspect deletions and changes to original critical paths. Preserve provenance.
2. Check frozen Champion immutable blob identities and authoritative governance before/after. Confirm current pointer identities and whether canonical surfaces moved; flag any contamination.
3. Inspect latest natural scheduled run receipts for all FOUR existing tasks (Market Monitor, Weekly QA, Health, Evening) with RUN_STARTED, work performed, closure, readback, delivery. Scheduler success != engine success. Check prompt drift and overlapping instructions; recommend simplification, do not blindly edit.
4. Reconcile original selector, market/decision ledger overlays, Hot Sheet acceptance, current six-market/venue price and deadline gates. Read exact source and test outputs. Distinguish QA tests written vs run.
5. End-to-end test only where supported, report unsupported execution boundary. Build KEEP/SIMPLIFY/QUARANTINE/REVERT matrix with verified evidence and no automatic rollback. Deliver concise day-by-day progress vs regression and one next executable action.
6. Persist audit increments to THIS FILE (update_file using fresh SHA), with latest repo head and next exact action. New chat: user says 'resume integrity audit' -> first read THIS FILE and authoritative latest sources, continue from next step, do NOT restart.

This file itself must be independently read back and commit confirmed before calling it persisted.
