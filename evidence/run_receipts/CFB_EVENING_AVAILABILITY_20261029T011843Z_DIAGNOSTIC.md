# CFB Evening Availability diagnostic — 2026-10-28

- cycle_id: CFB_EVENING_AVAILABILITY_20261029T011843Z
- workflow: CFB Beta Production incremental Evening Availability
- observation_boundary: 2026-10-29T01:20:12Z / 2026-10-28 20:20:12 America/Chicago
- role: downstream canonical integrity and availability review; not a competing Hot Sheet producer
- repository: munchie50/cfb-acquisition-bridge
- recovered_authority: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md @ 356b5920ab9cba100baa5669588995161585e48b
- active_cadence: evidence/CFB_ENGINE_FOOTBALL_WEEK_OPERATING_CADENCE_CONTRACT_v1_247.md @ 2a41f5cee71152c9f0a84cc3ee2f634020819dc2
- persistence_authority: evidence/CFB_GITHUB_CONTENTS_PERSISTENCE_PROCEDURE_2026-10-03.md @ 27e6500d0e4f001d8f71449e15f813e6fb83bedf
- terminal_authority: evidence/CFB_TERMINAL_RUN_RECEIPT_CLOSURE_CONTRACT_2026-10-05.md @ 501cda05d80229402a485493f10b1a4bbb76d3b8
- consensus_caesars_authority: evidence/CFB_CONSENSUS_BENCHMARK_AND_CAESARS_EXECUTION_CONTROL_2026-10-10.md @ c8daffd209ca1575d057b8d73839fa74998ccce6
- typed_publication_authority: evidence/CFB_NEUTRAL_SOURCE_DERIVED_PUBLICATION_CONTRACT_2026-10-12.md @ 29b06d911ee9c10b4314ca296cf0e24ae161d3c7
- complete_response_authority: evidence/CFB_CBS_COMPLETE_RESPONSE_CAPTURE_PROCEDURE_2026-10-14.md @ ab554daa0446c3fccd27b7026a74700d65bc6daf
- shared_budget_authority: evidence/CFB_FIRECRAWL_CYCLE_BUDGET_CONTROL_2026-10-24.md @ d27ff9d78cf84e29a28b906ffe75e6c7895e82cb
- RUN_STARTED: evidence/run_receipts/CFB_EVENING_AVAILABILITY_20261029T011843Z_RUN_STARTED.md @ dbecc0dfdb36c0fb4c526dc6b0dcfd0f742350c8; independent readback PASS

## Current producer boundary and durable daytime state

- The latest selected primary Hot Sheet remains evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-27_2050CT.md @ a11e571c9f2eab663b68cc4e0d25283a7da33092.
- The 2026-10-28 07:00 and 13:00 CT scheduled Monitor cycles closed RUN_INCOMPLETE because their scheduled runtime could not prove the immutable review Git ancestry required by the current compiler. The 13:00 full-board fallback completed nine seconds after its hard cutoff and remained an unselected diagnostic.
- The earlier current-clock manual Monitor pass does not prove scheduled runtime reliability. The repository runtime-repair cycle CFB_GIT_RUNTIME_REPAIR_20261028T122659Z and later Monitor cycle CFB_MARKET_MONITOR_20261028T124125Z remain START_ONLY; no conforming terminal candidate or RUN_CLOSURE was found after bounded commit enumeration.
- Therefore the selected sheet is not silently upgraded, and this Evening cycle does not replace it.

## Independently read-back canonical inputs

- market: evidence/operational/CFB_MARKET_MONITOR_STATE.md @ 2110b9167e823b3169335ffd12e6780b4067f1de
- decision: evidence/operational/CFB_DECISION_WAIT_LEDGER.md @ 8b43d28b71a0e70b12a4cbda3d14e886f13fa110
- execution: evidence/operational/CFB_EXECUTION_LEDGER.md @ 1a938f42e9f03e723bd50348f8a78dbd8b7098e9
- scorecard: evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md @ fd6529a4ab27ac12d74ace4441005535c605cadb
- inherited decision posture: zero active recommendations; 50 PASS/no-action rows; two expired conditional reviews; four earlier expired unpublished reviews
- production exposure: no new established Week9 execution proved
- separate $20 sandbox exposure: no new established Week9 execution proved
- settlement: none earned in this cycle
- casino trip: none earned in this cycle

## Fresh bounded near-window observation

Source recovered during this cycle: CBS Sports Week9 odds page, public response crawled 2026-10-29 UTC; exact bookmaker update clocks unavailable. The response is an unidentified field-level mixed-book display and is not a qualified consensus or a verified execution venue. Final/Open columns were not used as live results. Constituent identities and dispersion were unavailable; Caesars was not independently verified.

| Game | Fresh displayed spread / ML / total | Comparison with 2026-10-28 13:00 diagnostic | Earned disposition |
|---|---|---|---|
| Troy @ James Madison | Troy +19.5 -110, ML +800; JMU -18.5 -105, ML -1053; o49.5 -110 / u50.5 -115 | JMU lay shortened from displayed -20.5; dog cushion fell from +21 | Existing PASS not reopened; raw movement is not EV and no immutable material review was earned |
| Florida Atlantic @ North Texas | FAU +14 -115, ML +420; UNT -13.5 -115, ML -521; o76.5 -114 / u76.5 -105 | Spread/ML materially consistent; total remains far above the first retained 71.5 context | Original FAU conditional is expired history only; no chase or revival |
| Tulane @ Charlotte | Tulane -8.5 -110, ML -350; Charlotte +9.5 -108, ML +285; o46.5 -118 / u47.5 -111 | Favorite lay shortened from displayed -10 and Charlotte cushion fell from +10.5 | Existing PASS not reopened |
| Baylor @ UCF | Baylor +1.5 -118, ML -105; UCF +1.5 -110, ML -102; o47.5 -115 / u48.5 -115 | Mixed-book spread cells are internally non-consensus and cannot be represented as one executable market | CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; existing PASS not reopened |
| Kent State @ Sacramento State | Kent State -8.5 -104, ML -310; Sacramento State +9.5 -110, ML +275; o46.5 -108 / u46.5 -110 | Bounded current fallback only | Existing PASS not reopened |

Official team pages confirmed the Thursday kickoff contexts and current team previews for Troy–James Madison and Florida Atlantic–North Texas, but did not provide a qualified player-status report in the recovered response. Friday player-status evidence was not independently qualified in this cycle. Missing availability evidence is retained as unserved research, not converted to clearance or a recommendation.

- qualification: UNIDENTIFIED_FIELD_LEVEL_MIXED_BOOK_FALLBACK_ONLY
- consensus: CONSENSUS_UNAVAILABLE
- actual Caesars: UNVERIFIED
- executability: UNVERIFIED
- offer-update clocks: UNKNOWN
- complete full-slate response retained under governed procedure: NO
- chargeable Firecrawl work: NONE
- budget reason: prior saved provider state was plan/remaining 1000/1000, cycle day 1/31 and release cap 32, but an unsettled runtime-repair/acquisition boundary remained and a known serial upper request cost was unavailable; paid acquisition was deferred

## Invocation computation and typed-handoff preflight

- Python runtime: 3.12.14 available
- supported repository ancestry in this invocation: NO — the workspace is not a Git worktree
- governed compiler/readiness scripts in this invocation: NOT FOUND
- scripts/cfb_neutral_weekly_reconciliation.py normal advance: NOT EXECUTED
- scripts/cfb_hot_sheet_readiness.py: NOT EXECUTED
- immutable review ancestry proof: UNAVAILABLE
- fresh complete typed proposal: NOT PRODUCED
- canonical publication mutation: PROHIBITED
- typed market/decision append: NOT WRITTEN
- competing Hot Sheet: NOT CREATED

This is not merely an installed-code test failure: the actual scheduled invocation lacked the supported checkout and immutable review ancestry needed to validate the required typed handoff. Writing a prose-only canonical tail or downgrading current states would violate the active contract.

## Result and next safe action

- canonical market/decision/execution/scorecard mutation: NONE
- Champion/FIRST_FROZEN/REFRESH mutation: NONE
- newly earned BET EARLY/BET NOW/WAIT/CONDITIONAL: NONE
- expired conditional revival: NONE
- new execution or settlement: NONE
- task/schedule mutation: NONE
- Hot Sheet ownership: unchanged; the CFB Market Monitor remains sole primary producer

Blocker: COMPUTATION_RUNTIME_UNSUPPORTED_FOR_GOVERNED_COMPILER / IMMUTABLE_REVIEW_ANCESTRY_UNAVAILABLE.

Next safe action: complete and durably close the existing Git-runtime repair, then let the next prospective producer use a supported checkout to acquire a genuinely fresh complete source response, qualify official availability and source constituents, run the normal typed compiler/readiness path, and make only earned append-only transitions. Do not replay this cycle, extend expired cutoffs, or reconstruct a recommendation.

DIAGNOSTIC_ONLY
