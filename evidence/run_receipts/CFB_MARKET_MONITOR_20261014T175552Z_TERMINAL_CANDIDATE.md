# CFB Market Monitor terminal candidate — 2026-10-14 13:00 CT

- cycle_id: CFB_MARKET_MONITOR_20261014T175552Z
- workflow: CFB Beta Production Market Monitor
- terminal_candidate_at: 2026-10-14T18:03:00Z
- recovered_authority: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md with active v1.247 football-week cadence and accepted persistence, deterministic kickoff sectioning, terminal closure, neutral publication, and consensus/Caesars controls
- RUN_STARTED: evidence/run_receipts/CFB_MARKET_MONITOR_20261014T175552Z_RUN_STARTED.md
- RUN_STARTED_blob: ad11f0b9f200a6a7379b40c25633852577d4cbd3
- observability_order: PASS — authority recovered before RUN_STARTED; RUN_STARTED persisted/read back before external research or governed mutation

## Persisted and independently read-back governed surfaces

- market: evidence/operational/CFB_MARKET_MONITOR_STATE.md
- market_blob: 8c2d57bc469a1121fe94b1a956920e91c199275f
- market_result: live CBS Week7 board re-fetched at 2026-10-14T17:58:01Z; exact Wednesday deadline offers and movement appended; historical observations preserved
- decision: evidence/operational/CFB_DECISION_WAIT_LEDGER.md
- decision_blob: 441b966c075ba350dace2925a88681d034989d99
- decision_result: Kennesaw State at Missouri State and Western Kentucky at Sam Houston prospectively transitioned INCONCLUSIVE to PASS at the governed deadline
- execution: evidence/operational/CFB_EXECUTION_LEDGER.md
- execution_blob: 75caee4052e02ea7d2453d1d37fd3866e13ecc07
- execution_result: independently read back and unchanged; no Week7 production or sandbox execution
- scorecard: evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md
- scorecard_blob: 11160bb2f725555994067e72985024dc809a9241
- scorecard_result: independently read back and unchanged at this boundary; no new final beyond the already joined Tuesday games
- Hot Sheet: evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-14_1300CT.md
- Hot Sheet_blob: edb1806a4ebe4d1ae0c5e4a5c75d50869d9b4b3e
- Hot Sheet_result: created and independently read back; Thursday is primary and current-requalification limits are explicit
- recovery_navigation: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md
- recovery_navigation_blob: 604782daab2317cfbf802dd770ccbfea93e2454f
- recovery_navigation_result: current canonical and Hot Sheet selectors persisted/read back

## Wednesday deadline result

- Kennesaw State at Missouri State: PASS — Kennesaw State -2.5 (-111), ML -140; Missouri State +2.5 (-105), ML +120; total 52.5 (-110/-105). Consensus unavailable; Caesars unverified; no acceptable threshold; quarterback uncertainty and weather risk do not establish an edge.
- Western Kentucky at Sam Houston: PASS — Western Kentucky -1 (-111), ML -115; Sam Houston +1.5 (-114), ML +102; source-rendered over52.5(-111)/under53.5(-112). The extreme frozen/model disagreement is a model-risk investigation flag, not calibrated EV; no acceptable threshold.
- actionable production wagers: 0
- actionable sandbox wagers: 0
- casino trip: NONE
- production exposure: $0
- sandbox exposure: $0
- new execution: NONE
- settlement: NONE

## Hot Sheet exactly-once assertion

- governed slate cardinality: 62
- unique chronological game identities: 62
- duplicates: 0
- union equals governed slate: PASS
- section counts: TUESDAY 2; WEDNESDAY 2; THURSDAY 3; FRIDAY 3; SATURDAY MORNING 13; SATURDAY AFTERNOON 17; SATURDAY EVENING/NIGHT 22; UNRESOLVED KICKOFF 0
- count sum: 62
- decision-state count: 58 INCONCLUSIVE; 4 PASS
- earliest still-active section: THURSDAY
- each populated section contains actual game rows: PASS
- required row fields present: PASS

## Integrity and terminal gate

- FIRST_FROZEN preserved: PASS — 51 predictions and 11 exclusions; no frozen prediction changed
- accepted REFRESH lineage preserved separately: PASS
- earliest qualified observations preserved: PASS
- downstream evidence kept separate from Champion: PASS
- no invented EV, probability, confidence, constituent identity, or Caesars price: PASS
- no automatic Champion mutation, Challenger promotion, or scientific acceptance: PASS
- task/schedule mutation: NONE
- terminal blocker: the live full board was retrieved and bounded line-range reads covered the slate, but only 85 of the expected 120 active two-team offer rows were independently recoverable in the returned content slices. Constituent book identities were also not exposed. Exact current full-slate per-game normalization therefore remains unproved. The Hot Sheet retains latest qualified fallback for affected later rows and labels CURRENT_REQUALIFICATION_UNAVAILABLE; RUN_PASS is prohibited.
- next safe action: the downstream evening availability run should consume the persisted PASS decisions without reopening Wednesday games. The next prospective monitor must use a complete source response or identified multi-book constituents to requalify every active row; do not reconstruct this historical cycle.
- historical incomplete cycles: unchanged

RUN_INCOMPLETE