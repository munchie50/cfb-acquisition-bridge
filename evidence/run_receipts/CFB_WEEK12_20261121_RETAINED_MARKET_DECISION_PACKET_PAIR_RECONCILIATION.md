# Nov21 retained Week12 Nov20 market/decision packet pair — actual readback reconciliation

Status: PACKET_PAIR_RETRIEVED_AND_SCHEMA_RECONCILED / CANONICAL_PUBLICATION_BLOCKED / NO_BET.

Fresh GitHub contents reads returned full existing source files:
- evidence/run_receipts/CFB_WEEK12_20261120_MARKET_PACKET_DELTA_UNPUBLISHED.md, blob 754856df54bfb5040f552e827f44d9cd8dd30afd, 127,606 characters.
- evidence/run_receipts/CFB_WEEK12_20261120_DECISION_PACKET_DELTA_UNPUBLISHED.md, blob 646bbe85edba726037e1b98125783ff2cd87a4e8, 63,367 characters.

Both contain exactly one framed typed cfb-week12-*-v1 JSON packet, parsed successfully in the active connector orchestration session. Both report cycle CFB_MARKET_MONITOR_20261120T204508Z, as_of_utc 2026-11-20T20:50:24.828310+00:00. Both have 70 rows with 70 distinct game_id values; bidirectional ID set difference empty.

Market current_availability: AVAILABLE 64, UNAVAILABLE 6. AVAILABLE is historical packet availability and **does not** mean contemporaneous same-book venue-qualified six-side executable offers. Decision: 68 PASS, 2 CONDITIONAL from separate readback; cutoff_authority UNVERIFIED 68, REVIEW_EVIDENCED 2. Non-null planning_cutoff_utc only four records: 401858531 and 401858534 at 2026-11-21T13:00:00Z; 401866464 at 2026-11-17T23:30:00Z and 401866465 at 2026-11-17T22:30:00Z. 66 null planning cutoff fields. Do not backfill or reopen elapsed cutoffs.

Previous read-only direct Git blob recovery: current canonical market ledger SHA 21e2172c709dcf482c4750a7490b82aacac05949 and current canonical decision SHA 6862be6a1bd88a3290b1e90a49c33a7a87e92559; reconstructed decision SHA 98941e228072e6941b1c33e42d4d8dba570f7182 is exact canonical decision prefix plus the 63,367-character delta. Reconstructed market SHA c81855dc8f3ff002082e9c105b2d8d9c2e9bc684 not available via direct Git blob API in this invocation. Do not claim reconstructed market byte-hash verification, selector PASS, current qualified offers, or accepted publication.

Net: material blocker of locating the missing market packet is RESOLVED using existing artifacts. Packet-level 70/70 pair and chronology consistency verified. Remaining governance blockers: reconstructed market full-blob SHA verification, lineage/selector authority, index pointer and current prospective offer qualification. No canonical write, Champion modification, fifth task or wager.
