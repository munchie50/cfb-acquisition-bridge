# Nov20 Week12 — real-source decision binding readback (not synthetic)

STATUS: REAL_BYTES_AND_DECLARATION_MATCH / NO_CANONICAL_PROMOTION.

Latest recovered main before read: `7eb2f889cd4ea96e41317fc38c9292846f1f5b5e`. Via authenticated GitHub connector fetched exact decision base blob `6862be6a1bd88a3290b1e90a49c33a7a87e92559` (3,605,685 characters), decision delta blob `646bbe85edba726037e1b98125783ff2cd87a4e8` (63,367 characters), and published Week12 70-game preview (140,912 characters). Concatenation is 3,669,052 characters, agreeing with prior independently verified reconstructed decision Git blob `98941e228072e6941b1c33e42d4d8dba570f7182`. Delta begins with typed `cfb-week12-decision-v1` fence. Preview has exactly one `Canonical inputs:` declaration; its decision reference is exactly `98941e228072e6941b1c33e42d4d8dba570f7182` and market reference `c81855dc8f3ff002082e9c105b2d8d9c2e9bc684`.

This new check independently fetched real bytes and compared exact lengths/declarations; it **did not recompute Git SHA1** of concatenation in this run and does **not** claim execution of original Python `audit()` or `publication()`. Exact reconstructed SHA had been established by earlier read-only probe and independent retest. Distinguish these evidence scopes.

**Drift:** previously suggested building a new overlay reader or rerunning compiler is obsolete. Existing reader, bootstrap, QA lease and provisional publication are completed. Newest proof strengthens source-to-preview pairing, while canonical current index/decision binding remains open. Four tasks unchanged. The 07CT/13CT production runs remain RUN_INCOMPLETE, no executable wagers.

**Next narrow engineering gate:** execute original `audit(preview, reconstructed_decision)` in a suitable runtime, then separately test current index selector against proposed governed virtual-ledger contract. Do not alter canonical production selector or weaken acceptance before approval. Firecrawl hosted execution credits exhausted; local container cannot resolve GitHub, but GitHub connector can retrieve immutable bytes. A future implementation can transfer only required immutable bytes through connector, avoiding shell network entirely.

**Published manual release:** `evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_MANUAL_PROVISIONAL_RELEASE.md`.
