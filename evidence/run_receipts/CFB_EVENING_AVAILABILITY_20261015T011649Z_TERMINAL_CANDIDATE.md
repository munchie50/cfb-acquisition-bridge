# CFB Evening Availability terminal candidate — 2026-10-14

- cycle_id: CFB_EVENING_AVAILABILITY_20261015T011649Z
- workflow: CFB Beta Production incremental Evening Availability
- observation_boundary: 2026-10-14 20:16:49 America/Chicago
- repository: munchie50/cfb-acquisition-bridge
- recovered_authority: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md @ 60ae42d0006f70fc978e42e9d0db470cceb0dbf2
- active_cadence: evidence/CFB_ENGINE_FOOTBALL_WEEK_OPERATING_CADENCE_CONTRACT_v1_247.md @ 2a41f5cee71152c9f0a84cc3ee2f634020819dc2
- persistence_authority: evidence/CFB_GITHUB_CONTENTS_PERSISTENCE_PROCEDURE_2026-10-03.md @ f90f0d87f5027fe93bf4ca2c22440539904890ef
- terminal_authority: evidence/CFB_TERMINAL_RUN_RECEIPT_CLOSURE_CONTRACT_2026-10-05.md @ 9a2f158beddcde783c25fbecfa6d8d66dd8b2ca8
- consensus_caesars_authority: evidence/CFB_CONSENSUS_BENCHMARK_AND_CAESARS_EXECUTION_CONTROL_2026-10-10.md @ c87498072194ee07e62ac8c40dfc61f5e3b30ad9
- complete_response_authority: evidence/CFB_CBS_COMPLETE_RESPONSE_CAPTURE_PROCEDURE_2026-10-14.md @ ab554daa0446c3fccd27b7026a74700d65bc6daf

## Fresh complete-response capture

- capture: evidence/operational/CFB_CBS_FULL_BOARD_TABLES_20261015T011649Z.md
- capture_blob: 5d6f37ed470342a641f75436287661cfc5a9151c
- retained_table_sha256: 2f8b09237bab9ef51bc7d58cf98b9726355495587d0a57b15c449d3c2111e959
- scrape_id: 01a13d24-9616-729d-8a5f-197bd0dadab5
- coverage: 62 game headers; 124 team rows; all 58 future Thursday-through-Saturday games present
- source_clock: response recovered during run; exact bookmaker update time unavailable
- qualification: UNIDENTIFIED_FIELD_LEVEL_MIXED_BOOK_FALLBACK_ONLY
- consensus: CONSENSUS_UNAVAILABLE
- actual Caesars: UNVERIFIED
- executability: UNVERIFIED
- Final/Open columns: quarantined
- capture_readback: PASS

## Persisted and independently read-back canonical state

- market: evidence/operational/CFB_MARKET_MONITOR_STATE.md @ 00b0c8c68fd1abf920aa1e06346bae4b7406c82e
- market_result: complete-response provenance, all three Thursday observations, movement, official-preview boundary and weather appended
- decision: evidence/operational/CFB_DECISION_WAIT_LEDGER.md @ 5f258a879ed5a15c93e20599ad1e1f6c34c174c5
- decision_result: East Carolina @ UAB INCONCLUSIVE→PASS; Colorado State @ Texas State INCONCLUSIVE→PASS; Georgia Southern @ Old Dominion remains governed INCONCLUSIVE
- execution: evidence/operational/CFB_EXECUTION_LEDGER.md @ 75caee4052e02ea7d2453d1d37fd3866e13ecc07
- execution_result: read back unchanged; no Week 7 production or sandbox execution
- scorecard: evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md @ 11160bb2f725555994067e72985024dc809a9241
- scorecard_result: read back unchanged; no newly final established wager or new authoritative final requiring settlement
- inherited primary Hot Sheet: evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-14_1300CT.md @ edb1806a4ebe4d1ae0c5e4a5c75d50869d9b4b3e
- Hot Sheet ownership result: read back as daytime baseline and intentionally not replaced by Evening Availability. The next Market Monitor must render the new canonical 56 INCONCLUSIVE / 6 PASS state into the sole primary Hot Sheet.

## Thursday decisions and portfolio

- East Carolina @ UAB: PASS. Original FIRST_FROZEN excluded; accepted REFRESH not substituted; no threshold.
- Georgia Southern @ Old Dominion: INCONCLUSIVE until Thursday 13:00 CT reconciliation. If governed WAIT is earned, hard final cutoff 17:30 CT. Otherwise actionable or PASS. No trip tonight.
- Colorado State @ Texas State: PASS. Extreme frozen-versus-market reversal is model-risk evidence, not calibrated EV; no qualified execution evidence or threshold.
- current Week 7 state: 56 INCONCLUSIVE; 6 PASS
- production exposure: $0
- separate sandbox exposure: $0
- new execution: NONE
- settlement: NONE
- casino trip: NONE
- acceptable number/price newly established: NONE
- task/schedule mutation: NONE

## Integrity

- original 51 FIRST_FROZEN predictions plus 11 exclusions preserved
- accepted REFRESH lineage preserved separately
- Wednesday PASS decisions not reopened
- no raw disagreement converted to EV, probability, confidence or automatic action
- no invented book identity, consensus, Caesars price or execution
- no Champion mutation, Challenger promotion, scientific acceptance, outcome-informed reconstruction or competing Hot Sheet
- historical incomplete cycles remain unchanged

All applicable Evening Availability work, canonical changes and readbacks succeeded. The remaining current-publication reconciliation debt belongs to the sole primary Market Monitor; this downstream run did not weaken or evade it.

RUN_PASS