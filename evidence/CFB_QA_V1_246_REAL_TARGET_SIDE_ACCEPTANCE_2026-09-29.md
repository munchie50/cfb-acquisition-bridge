# CFB QA — v1.246 Real Target-Side Substrate Acceptance — 2026-09-29

Status: **ACCEPTED QA TARGET-SIDE SUBSTRATE ONLY**
Scientific producer authority remains the layered acceptance in CFB_QA_REFRESH_V1_246_EQUIVALENCE_STATUS_2026-09-28.md.

## Post-run acceptance
- Producer: scripts/phase4_challenger_b_2026_refresh_predict_v1_246.py; Git blob ae48cf05dde9647646c8ae2a71f90a2d97bf4cc2.
- Run/job 36636336698 / 109637770259; head edd9c7899507f7efe289aea3fbe6d7ce780bf2ca; independently read SUCCESS and passed immutable raw/frozen fit locks in job logs.
- Artifact 11064541770, cfb-qa-v1-246-real-target-side-substrate.
- ZIP SHA-256 78b58979a7a1a81bd3af0473c65fb760a94b73421e0ee97aa51adce1a540a259 independently reproduced.
- Target-side CSV SHA-256 eb2ea9a24831fbb485070c038118aedd11934951f28d02484d30654b0e067e75 independently reproduced and equals both substrate and feature-ledger manifest identities.
- Same retained raw artifact 11031055060; ZIP 1495f453e5d9f262baddfa2b7ad21d2d9e8d5f8c2436f058f88fcb6ebc6d8d68.
- Cutoff 2026-09-29T11:39:08.824054+00:00.
- 557 targets, 1,114 unique home/away side rows; 551 game-level eligible S0 predictions and six exclusions reported by producer manifest and independently reproduced from side eligibility.
- 1,108 eligible sides; all 18,836 eligible feature values independently reproduced from recovered v1.172 mechanical/derived primitives and strict-prior rest intervals at rtol=0/atol=1e-12.
- All 1,114 target-side identities, kickoffs and prior counts matched source population, including six zero-history sides.
- snapshot_type=REFRESH_SNAPSHOT, parent_lineage=v1.216, exact cutoff, no duplicate identities or forbidden target-outcome/market/wager/execution fields.
- Raw manifest, every internal raw file hash, exact relevant-FBS filtering, source-only chronology and original-string identities independently verified.

QA_REAL_SUBSTRATE_MANIFEST remains immutable QA_REAL_TARGET_SIDE_SUBSTRATE_FROZEN_NOT_S2_EXECUTED; producer manifest remains EXECUTED_NOT_ACCEPTED. Both record s2_predictions_produced/target_outcomes_joined/market_joined false where applicable; fit_or_optimization_performed=false.

## Scope and limitations
This three-file retained artifact contains the team-side CSV and two manifests. Prediction, exclusion, chronology and target-ledger CSVs named by the producer manifest are NOT contained in this retained ZIP. This record accepts the real target-side boundary, not an operational prospective S0 prediction snapshot or unseen prediction-file bytes.
The 551/6 counts are independently supported by side eligibility, but final prediction CSV bytes are not audited here.
No cadence exception, FIRST_FROZEN replacement, Champion/model mutation, S2 prediction, outcome evaluation, 2025 access or promotion.
Historical original raw-PBP replay limitation remains unchanged.
See CFB_QA_S2_K1_SOURCE_CONTEXT_V4_ACCEPTANCE_2026-09-29.md for shared audit details and exact source-context acceptance.

Integration debt closed: deterministic repository inventory and direct current readiness/source-context/equivalence reads found no explicit post-run acceptance for run 36636336698 before this record. Earlier v1.246 synthetic/export acceptance remains preserved; this supplies the separate real-data boundary disposition.
