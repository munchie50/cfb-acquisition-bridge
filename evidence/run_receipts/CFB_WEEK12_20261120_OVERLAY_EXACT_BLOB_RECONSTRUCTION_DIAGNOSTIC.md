# Week12 07CT/13CT overdue manual monitor — exact blob reconstruction diagnostic

STATUS: READ_ONLY_EXACT_BLOB_RECONSTRUCTION_PASS; NOT_CANONICAL_PUBLICATION; RUN_INCOMPLETE.

Fresh full Git checkout, current main at start `f379196eb2dbf07e0c3c1b9d5e5ec279fd0c2e6b`. No production ledger mutation, no schedule/workflow changes, no engine recalculation. Read actual repo files and computed Git SHA1 blob identifiers over raw UTF-8 bytes, not merely names or summaries.

Validated exact Git blobs: canonical market `21e2172c709dcf482c4750a7490b82aacac05949`, canonical decision `6862be6a1bd88a3290b1e90a49c33a7a87e92559`, Week12 market delta `754856df54bfb5040f552e827f44d9cd8dd30afd`, Week12 decision delta `646bbe85edba726037e1b98125783ff2cd87a4e8`. All four matched expected values. Parsed fenced typed packet contents and checked same cycle/as_of and exact 70/70 unique game identity equality.

Raw byte exact assembly without separators: market canonical bytes + market delta bytes => Git blob `c81855dc8f3ff002082e9c105b2d8d9c2e9bc684`; decision canonical bytes + decision delta bytes => Git blob `98941e228072e6941b1c33e42d4d8dba570f7182`. Official `scripts/cfb_week12_publication.py` `bootstrap_check` with existing original lineage returned `PASS_WEEK12_CONDITIONAL_PROPOSAL_ONLY`. SHA-based negative checks demonstrated mutation, reordering and omission change expected digest; these were checks, not comprehensive adapter adversarial tests.

This is concrete evidence for an immutable-packet overlay reader avoiding oversized GitHub connector write payloads, but no adapter or manifest has been promoted into production. Before using this as canonical authority, amend active persistence/consumer contracts explicitly, implement atomic paired manifest publication and strict content-addressed adapter, test negative cases including stale parent and competing writers, independently verify acceptance and Hot Sheet. The two overdue Friday runs remain RUN_INCOMPLETE; Friday 13CT cutoff remains missed. No new wagering authorization.
