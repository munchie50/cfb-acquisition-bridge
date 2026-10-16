# CFB Evening Availability Terminal Candidate — 2026-10-15 20:09 CT

- run_identity: CFB_EVENING_AVAILABILITY_20261016T010936Z
- run_type: CFB Evening Availability
- prospective_boundary: 2026-10-15 20:09 CT / 2026-10-16T01:09:36Z
- recovered_authority:
  - evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md @ b1de5d4e7b079a28a57322035cde0e89637fceec
  - evidence/CFB_ENGINE_FOOTBALL_WEEK_OPERATING_CADENCE_CONTRACT_v1_247.md @ 2a41f5cee71152c9f0a84cc3ee2f634020819dc2
  - evidence/CFB_GITHUB_CONTENTS_PERSISTENCE_PROCEDURE_2026-10-03.md @ f90f0d87f5027fe93bf4ca2c22440539904890ef
  - evidence/CFB_TERMINAL_RUN_RECEIPT_CLOSURE_CONTRACT_2026-10-05.md @ 9a2f158beddcde783c25fbecfa6d8d66dd8b2ca8
  - evidence/CFB_CONSENSUS_BENCHMARK_AND_CAESARS_EXECUTION_CONTROL_2026-10-10.md @ c87498072194ee07e62ac8c40dfc61f5e3b30ad9
- downstream_baseline: CFB_MARKET_MONITOR_20261015T175838Z
- earned_terminal_state: RUN_PASS
- material_change: YES

## Work result

The nearest active Friday section was refreshed prospectively. Washington quarterback Demond Williams Jr. is officially QUESTIONABLE on the Big Ten initial and first availability updates. A current page updated 20:02 CT lists Appalachian State quarterback Malachi Singleton QUESTIONABLE. Fresh Friday market rows were retained as UNIDENTIFIED_FIELD_LEVEL_MIXED_BOOK_FALLBACK_ONLY; CONSENSUS_UNAVAILABLE; actual Caesars UNVERIFIED; execution UNVERIFIED.

Memphis at Tulane, Washington at Purdue, and Appalachian State at Coastal Carolina remain INCONCLUSIVE before the governed Friday 13:00 CT reconciliation deadline. Each retains an explicit next trigger and a hard final practical cutoff one hour before kickoff. No acceptable number or price was earned, no bet was forced, and no trip was authorized. Week 7 production exposure remains $0; separate $20 sandbox exposure remains $0.

## Persisted and independently read-back surfaces

- evidence/operational/CFB_MARKET_MONITOR_STATE.md @ 05ccbf405bd1d5e35a1842d718c4e45325d7bee7
  - operation: update_file
  - attempt_count: 1
  - baseline_sha: 29b5aa348e3224ed596c41ce96d2fa73b5e193af
  - baseline_chars: 257867
  - delta_chars: 3947
  - expected cycle and both quarterback identities independently read back: YES
  - planned_delta_digest: UNAVAILABLE
- evidence/operational/CFB_DECISION_WAIT_LEDGER.md @ 0ed8166d1cbeab88d6e9ec5259a0c033de1f90db
  - operation: update_file
  - attempt_count: 1
  - baseline_sha: 9d36041b96e12deaec608019ea5d77cd754fe845
  - baseline_chars: 116444
  - delta_chars: 3497
  - expected cycle, deadlines and 55 INCONCLUSIVE / 7 PASS census independently read back: YES
  - planned_delta_digest: UNAVAILABLE
- evidence/operational/CFB_EXECUTION_LEDGER.md @ 75caee4052e02ea7d2453d1d37fd3866e13ecc07 — read back; no Week 7 execution appended.
- evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md @ d0726d8f758bfcde02a0196379bc46ec83d0a0ff — read back; no new final eligible for this downstream run and no outcome-informed reconstruction.
- evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-15_1300CT.md @ 02e470ddb486008cba819735e06de77d1639ea3e — latest sole-primary-producer Hot Sheet read back. This downstream task did not create or overwrite a competing Hot Sheet.

## Source provenance

- CBS Week 7 page, fresh maxAge=0 fetch, HTTP 200, Firecrawl scrape id 01a14244-d7ac-73e2-8729-f7316fef9593: https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-7/
- Big Ten official availability: https://bigten.org/fb/availability-reports/
- App State/Coastal game center page, updated 2026-10-15 20:02 CT: https://ncfootballnews.com/games/app-state-at-coastal-carolina-football-2026/
- Memphis and Tulane official game centers: https://gotigersgo.com/game-center/20060 and https://tulanegreenwave.com/game-center/23453

## Integrity boundaries

Champion v1.193, FIRST_FROZEN and accepted REFRESH lineage are unchanged. Downstream market, availability and decision evidence remains separate from frozen predictions. No automatic Champion mutation, Challenger promotion, scientific acceptance, invented EV/probability/confidence, execution, settlement, or outcome-informed reconstruction occurred. No automation lifecycle mutation occurred.

This is a terminal candidate. Final closure requires independent readback of this exact candidate followed by a separate RUN_CLOSURE record.
