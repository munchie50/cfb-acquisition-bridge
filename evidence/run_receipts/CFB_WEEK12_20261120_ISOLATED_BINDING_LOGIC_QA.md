# CFB Week12 Nov20 — isolated decision-binding feasibility test

**STATUS: SYNTHETIC LOGIC TEST PASSED; NOT LIVE PACKET ACCEPTANCE.**

Reopened current `scripts/cfb_hot_sheet_current_decision_binding_gate.py` and `scripts/cfb_overlay_publication_probe.py` from main at `dd1b3fa464155334de5fbb0dce4d3e923a94494c`. Executed isolated Python test locally with the **same `blob` and `audit` logic** as the checked-in binding module and a synthetic base+delta ledger. Four outcomes:

1. Synthetic Hot Sheet declaring Git blob SHA of concatenated virtual ledger and supplying that virtual ledger: `PASS_SUPPLIED_CURRENT_DECISION_BINDING_ONLY`.
2. Same Hot Sheet supplied old base canonical ledger: rejected `stale current publication`.
3. Same Hot Sheet supplied tampered appended ledger: rejected `stale current publication`.
4. Same Hot Sheet supplied empty ledger: rejected `stale current publication`.

**Scope limitation:** This did not import and execute the live repository module against actual 6.9MB/3.7MB Week12 artifacts, nor test the `publication(index,...)` selector, and is not acceptance evidence for actual Week12. It isolates the source-level hypothesis: `audit(sheet, reconstructed_ledger)` can pass without altering the audit or weakening its digest comparison; current canonical publication still fails because index/ledger pointers are different.

**Concrete deeper finding:** existing overlay `reconstruct` validates schema, exact Git blobs, packet framing, cycle/as_of and expected digest, but its manifest schema contains no previous-manifest hash, parent commit, sequence, or lease. Thus lineage/competing-writer correctness is **not established by the reader**; QA branch stale-lease behavior alone cannot establish it. Next smallest slice is QA-only manifest-chain validation, not repeat checkout/compile or declare RUN_PASS.

**Operational state:** 07CT/13CT manual recovery and provisional 70-game Hot Sheet already published; 68 PASS, two expired historical CONDITIONAL, no actionable authorized wager. Scheduled production statuses remain RUN_INCOMPLETE. Firecrawl execution credits exhausted; no paid runtime retries. Four tasks unchanged.

**Recovery:** `evidence/CFB_ENGINE_ACTIVE_CONTINUATION_CHECKPOINT_20261120.md` and `evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_MANUAL_PROVISIONAL_RELEASE.md`.
