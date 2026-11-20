> **ACTIVE RESUME ROUTING — NOV 20:** This document is a historical handoff. Before acting, open `evidence/CFB_ENGINE_SINGLE_ACTIVE_RESUME_FRONTIER_20261120.md` and fresh `main`. The single active frontier supersedes this file's next-action instructions. After each verified engineering slice, update/supersede that frontier and read it back; do not restart completed work. This is a repository discovery pointer, not an automatic session-start hook.

# CFB Market Monitor — ACTIVE CONTINUATION CHECKPOINT (Nov 20, 2026)

**Purpose:** conversation-limit emergency handoff. Read this first, then latest main and superseding receipts. Do not treat screenshots as a request to restart work.

## Verified release / exact resume point
- Current published **manual provisional** Week12 Hot Sheet pointer: `evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_MANUAL_PROVISIONAL_RELEASE.md`.
- Complete 70-game content: `evidence/operational/CFB_WEEK12_20261120_MANUAL_RENDERED_HOT_SHEET_PREVIEW_NOT_ACCEPTED.md`.
- Publication commit: `045b77db5fa0f98406f24be529a01a74dc555726`. Release independently read back.
- 70 unique games, 68 PASS, two **closed historical** CONDITIONAL, 0 INCONCLUSIVE, **zero actionable approved wagers**. Original FIRST_FROZEN preserved.
- Friday 07CT and 13CT research catch-up, normalizer, compiler, deltas, overlay reconstruction, QA manifest and preview all already completed. Do not redo.
- Original due cycles still `RUN_INCOMPLETE` for canonical acceptance; 13CT deadline missed and cannot be backdated.

## Current independent status check
Four production automations still enabled: Market Monitor, Health, Weekly QA, Evening Availability. Market Monitor scheduled Nov20 13CT invocation has a completed scheduler record but its internal result is `RUN_INCOMPLETE`; a scheduler 'completed' status is not engine RUN_PASS. No fifth task created.

## True remaining engineering frontier
- Current `scripts/cfb_hot_sheet_current_decision_binding_gate.py` expects sheet's decision SHA to match exact full canonical ledger, plus current Hot Sheet and decision pointers from recovery navigation. Reconstructed virtual decision blob differs from unappended main canonical ledger. Overlay manifest alone cannot satisfy this.
- Existing `scripts/cfb_overlay_publication_probe.py` and QA branch lease tests **already exist and passed their scoped tests**. Extend, don't rebuild. Consumer must validate pair/parent/sequence, missing/duplicate/reordered packets, concurrent writers, then pass exact reconstructed ledger into unchanged audit; formal contract/selector amendment required for canonical promotion.
- New Firecrawl execution attempt blocked by **credit exhaustion**, not DNS. Do not retry paid hosted execution without available credits or user authorization. Connector read/write still works.
- Do not force canonical pointer, weaken decision gate, fabricate sportsbook price, mark production RUN_PASS, or change Champion/4 tasks.

## KISS alternative perspective
Manual **delivery** is solved by the published provisional release. Stop making canonical transport a prerequisite for the user to read the Hot Sheet. Future engineering QA may use a temporary local reconstructed full-ledger file and call the **existing audit(sheet, virtual_ledger)** without touching canonical index; that only proves decision-binding compatibility, not production publication. After tests and authorized contract change, tackle selector/pointer publication. Separate those two gates so a failure is localized.

## Next action
Do **not** re-run previous football collection. First determine whether new prospective named-book quotes/personnel evidence warrants a new review. If not, preserve current no-wager verdict. For engineering, write the smallest QA-only consumer binding test against existing probe and existing audit, then verify independently when a working execution runtime is available. Publish its exact test evidence and readback; only then discuss production contract changes.

## Supporting evidence
- `evidence/run_receipts/CFB_WEEK12_20261120_CONTINUATION_FRONTIER_BINDING_DEEP_DIVE.md`
- `evidence/run_receipts/CFB_WEEK12_20261120_OVERLAY_QA_BRANCH_PUBLICATION_AND_STALE_LEASE.md`
- `evidence/run_receipts/CFB_WEEK12_20261120_MANUAL_OVERLAY_RECONSTRUCTION_INDEPENDENT_RETEST_2132CT.md`
- `evidence/run_receipts/CFB_WEEK12_20261120_MANUAL_LANE_SUPERSESSION_AND_PREVIEW_READBACK.md`

**States:** MANUAL_PROVISIONAL_PUBLISHED / CANONICAL_RUN_INCOMPLETE / SCHEDULER_UNVERIFIED.
