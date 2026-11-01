# CFB GitHub large-authority retrieval — verified diagnostic (2026-11-01)

Scope: non-destructive retrieval-layer recovery after rebuilt Market Monitor RUN_INCOMPLETE. No canonical production mutation or Hot Sheet promotion.

Observed current main path fetch for `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md`: GitHub fetch_file returned content length 0 while reporting nonempty blob `57327859afb17ca42451189d3661f4c16fae4f90`. Direct fetch_blob by that SHA returned 4,230,445 characters, beginning with the correct v1.245 header and ending in the document's closing fenced JSON. Repeated direct fetch returned same length and header/tail.

`CFB_MARKET_MONITOR_STATE.md`: prior accepted blob `69caf5b1184eedccc90be7562e4a3bd7cb8b7375`; direct fetch_blob returned 3,836,615 characters and correct state header. Path fetch_file in this diagnostic returned 404; do not infer missing blob from this result.

`CFB_DECISION_WAIT_LEDGER.md`: prior accepted blob `bb5a9cc83b6a1425dc2972ca84b33aa2bbbf8fa9`; direct fetch_blob returned 1,900,825 characters and correct ledger header. Path fetch_file returned 404.

## Supported workaround and gate

1. Discover the newest accepted recovery index and canonical path/blob SHA from current authoritative repository records; do not assume these historical SHAs remain current.
2. Try path fetch only for metadata. If content is empty/404 for a known nonempty SHA, use `fetch_blob(repository_full_name, blob_sha)` to retrieve exact content. Verify document identity/header, nonempty payload, ending/integrity, and SHA identity from the trusted reference; ideally independently verify Git blob SHA locally before any mutation.
3. Never write back partial/truncated/empty large files. If full-content validation cannot be established, fail closed and record exact frontier.
4. Resume governed current production evaluation only after all current required authorities and frozen invariant dependencies have been recovered and independently checked. Do not infer RUN_PASS or current Week10 recommendations from this diagnostic.

This proves the retrieval workaround can access historical accepted blobs, not that the current market and decision surfaces have been safely updated. No production task or schedule changed.
