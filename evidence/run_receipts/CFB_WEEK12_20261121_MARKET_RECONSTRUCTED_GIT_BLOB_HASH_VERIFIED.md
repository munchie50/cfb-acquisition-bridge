# Nov21 exact Week12 market reconstructed Git blob hash — independent verification

Status: READ_ONLY_RECONSTRUCTION_HASH_PASS / PRODUCTION_PUBLICATION_NOT_ACCEPTED.

Source inputs freshly fetched in same tool invocation:
- Current canonical market Git blob 21e2172c709dcf482c4750a7490b82aacac05949: 6,815,072 Unicode characters, retrieved via GitHub fetch_blob.
- Retained Nov20 market delta evidence/run_receipts/CFB_WEEK12_20261120_MARKET_PACKET_DELTA_UNPUBLISHED.md, blob 754856df54bfb5040f552e827f44d9cd8dd30afd: 127,606 Unicode characters, retrieved via GitHub fetch_file.
- Exact concatenation UTF-8 length 6,943,338 bytes. In an independent JavaScript execution, manually encoded UTF-8 and computed SHA-1 over Git blob framing `blob 6943338\\0` plus the full content bytes.
- Computed Git blob SHA1 **c81855dc8f3ff002082e9c105b2d8d9c2e9bc684** exactly equals previously retained expected reconstructed market blob.
- Previous GitHub fetch_blob 404 for this unreferenced reconstructed object is not evidence of a hash mismatch; the full bytes were reconstituted and checked directly without mutating GitHub object storage.
- Decision counterpart reconstructed Git blob 98941e228072e6941b1c33e42d4d8dba570f7182 was previously fetched and verified as exact canonical decision prefix + 63,367-character typed delta. Both retained typed packets have identical Nov20 cycle/as_of and 70 matching unique game IDs.

Scope: exact market content identity and packet-level pair consistency VERIFIED. No production selector invocation, no canonical ledger pointer write, no recovery-index selector approval, no current venue-qualified six-side offer, and no new authorized wager. Remaining blocker is governed original acceptance/publication and prospective market/personnel gates; do not reclassify historical 68 PASS as bets or reopen deadlines. Do not redo CBS 70/70 normalization, compiler, DNS, or old bundle work absent new regression.
