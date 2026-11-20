# CFB Nov20 — production selector exact-pointer drift audit

**STATUS: VERIFIED INDEX/SELECTOR MISMATCH; NO PRODUCTION MUTATION.**

Reopened actual `scripts/cfb_recovery_navigation_reader.py`, `scripts/cfb_hot_sheet_current_decision_binding_gate.py`, and full 308,827-character `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_295.md` from current main. Parsed both `cfb-frontier-json` checkpoints and inspected latest record `2026-11-19T19:38:55.689014+00:00`.

Latest current decision pointer: `evidence/operational/CFB_DECISION_WAIT_LEDGER.md` blob `6862be6a1bd88a3290b1e90a49c33a7a87e92559`. Latest current Hot Sheet pointer: `evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-19_1338CT.md` blob `4c8ebeb5dd95b7ea7309f45a9275f7509a198905`. Both precede Nov20 reconstructed decision `98941e228072e6941b1c33e42d4d8dba570f7182` and Nov20 manually published provisional release. Latest navigation is explicitly NAVIGATION_ONLY_NOT_AUTHORITY and must not supersede later receipts.

Original `publication(index,ledger,loader,as_of)` requires exactly one purpose prefix `CURRENT_HOT_SHEET:`, a current sheet path matching `evidence/operational/CFB_WEEK[1-2 digits]_HOT_SHEET_YYYY-MM-DD_HHMMCT.md`, one decision pointer whose blob matches supplied ledger, exact sheet pointer bytes, then `audit(sheet,ledger)`. The current provisional release path `evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_MANUAL_PROVISIONAL_RELEASE.md` does not match that path regex, and is a release *pointer* to the noncanonical preview, not a canonical accepted sheet. Therefore merely changing a decision pointer, or adding the provisional release to the index, is not a valid fix.

**Minimal safe integration design:** keep provisional release unchanged. In QA only, reconstruct actual market/decision from immutable base+delta and verify their hashes; run original audit on complete rendered preview and virtual ledger; prepare a separate schema-compliant canonical sheet artifact candidate only after content/authority review; test a simulated append-only navigation checkpoint with exactly one current sheet and one matching decision pointer; verify actual `publication` function in QA; obtain explicit governed contract approval before mutating main canonical ledger/index. Do not fake a production PASS by updating index alone. Concurrency/manifest parent lineage also remains open.

**No repeat:** full CBS source, compiler, 70-game preview, packet deltas, independent reconstructed decision Git SHA, and five equivalent negative tests already completed. Manual 07CT/13CT recovery is published provisionally; original scheduled runs remain RUN_INCOMPLETE. Four automations unchanged. No wager approval.

**Next executable slice:** QA-only original-module selector test with a constructed isolated index and content-addressed sheet candidate. This audit itself did not run that test or change authority.
