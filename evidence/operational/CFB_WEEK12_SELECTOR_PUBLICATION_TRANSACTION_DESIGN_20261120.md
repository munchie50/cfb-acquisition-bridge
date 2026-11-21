# Week12 selector publication transaction — candidate design, NOT approved or executed

## Scope and observed mismatch
Fresh original module readback: `scripts/cfb_hot_sheet_current_decision_binding_gate.py` requires exactly one `CURRENT_HOT_SHEET:` pointer to `evidence/operational/CFB_WEEK<N>_HOT_SHEET_YYYY-MM-DD_HHMMCT.md`, and a `CFB_DECISION_WAIT_LEDGER.md` pointer whose Git blob equals the actual supplied canonical ledger. Week12 provisional release and rendered preview are **not** valid canonical sheet paths. Existing recovery index points to Nov19; the Week12 reconstructed decision blob `98941e228072e6941b1c33e42d4d8dba570f7182` is an overlay, not the current canonical ledger file. Therefore changing only a sheet pointer or renaming the preview cannot pass the actual selector without either mutating canonical state or introducing a governed overlay-aware reader.

## Minimum governed approach (proposal only)
1. **Preserve** existing canonical ledger and index unchanged until explicit authorization and original-module integration QA. Do not copy provisional preview into canonical naming to trick selector.
2. Define a **candidate-only overlay binding contract** with immutable base SHA `6862be6a1bd88a3290b1e90a49c33a7a87e92559`, delta SHA `646bbe85edba726037e1b98125783ff2cd87a4e8`, reconstructed Git blob SHA `98941e228072e6941b1c33e42d4d8dba570f7182`, and an explicit original-ledger versus overlay source role. The reader must verify all three SHA identities from bytes, not trust declarations.
3. Candidate transaction record must include unique transaction ID, immutable parent index blob, expected canonical ledger blob, sequence number, writer/lease identity and expiry, UTC creation time, exact candidate sheet path/blob, overlay base/delta/result hashes, and scope `QA_ONLY_NOT_CANONICAL`. Reject missing fields, duplicate IDs, future timestamps, stale parents, expired lease, competing writers and mismatched content.
4. **Prepare phase:** stage immutable content and run original selector QA plus overlay-reader lineage/competing-writer negative cases against isolated QA index; do not mutate active pointers.
5. **Commit phase (requires separate governance approval):** serialize writes with compare-and-swap against freshly fetched parent SHA; publish ledger and sheet content first, then single reconciled navigation index last; verify exact readback and rollback or fail closed if parent changes. GitHub sequential file writes are **not atomic** across files, so no reader may treat intermediate states as accepted.
6. **Acceptance phase:** independently fetch all referenced blobs, run the original production reader and binding gate on canonical state, verify acceptance contract and actual scheduled-worker evidence separately. Never infer RUN_PASS or actionable wagers from selector-only PASS.

## Blockers and non-goals
- Original checked-in QA `qa/cfb_week12_original_selector_integration_qa.py` still needs exact source + 3.6MB immutable base blob and 63KB delta staged and executed in genuine Python; connector retrieval alone does not prove filesystem transfer.
- Do not recreate CBS board, redo successful compiler/hash work, retry Git HTTPS/DNS, or route through previously rejected GitHub Actions scheduler.
- No Champion promotion, frozen-model substitution, wagering authorization, or modification to the four production automations.
