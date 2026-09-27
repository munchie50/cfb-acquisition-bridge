# CFB Market Monitor State

Status: ACTIVE APPEND-ONLY OPERATIONAL SURFACE
Initialized: 2026-09-27

## Recovery semantics
This is the canonical durable recovery surface for qualified CFB market-monitor observations. Append only; never reconstruct an earlier observation from a later quote or outcome.

## Required record fields
- game/market identity
- observation timestamp CT
- source/book/benchmark
- line and price
- FIRST_QUALIFIED_MARKET_OBSERVATION / INTERMEDIATE / EXECUTION / CLOSE / NOT_YET_AVAILABLE
- availability/executability
- provenance/timestamp semantics
- linked Champion snapshot identity where applicable

## Initial state
No historical Sunday observation is backfilled here. Missing earlier observations remain missing rather than being reconstructed after the fact.

## Write-path validation — 2026-09-27 13:03 CT
- Purpose: controlled repair validation for canonical existing-file mutation.
- Governance effect: none; no market observation, decision, execution, prediction, or outcome state created.
- Method: existing file fetched with current blob SHA, then replaced through SHA-guarded repository update.


## Prospective capture — 2026-09-27 13:08 CT
Observation class: FIRST_QUALIFIED_MARKET_OBSERVATION for the records below. These are the earliest qualified observations durably established after the write-path repair; they do not reconstruct the unpersisted 13:00 CT observations.
Source semantics: live web retrieval during this run. ESPN game/odds surfaces identify DraftKings where stated; FanDuel is identified directly where stated. Exact fields not established are omitted rather than inferred.
Champion link: v1.208 FIRST_FROZEN artifact 10897612260 / accepted Beta Champion lineage v1.193.

- Game 401858475 — Maryland at Nebraska, 2026-10-03 15:00 CT. ESPN/DraftKings: Maryland +12.5 (-110); total 52.5 (-110 each side shown); Maryland ML +410. Availability: executable market displayed. Champion FIRST_FROZEN: Nebraska by 10.5205; total 56.0116; Nebraska win 0.733503. Market-vs-Champion: market makes Nebraska a larger favorite than Champion by about 1.98 points; market total about 3.51 below Champion.
- Game 401856707 — Alabama at Mississippi State, 2026-10-03 11:00 CT. ESPN/DraftKings: Alabama -5.5 (-110), Mississippi State +5.5 (-110); total 59.5 (-110); Alabama ML -218, Mississippi State +180. Availability: executable market displayed. Champion FIRST_FROZEN: Mississippi State by 9.8652; total 60.0377; Mississippi State win 0.743319. Market-vs-Champion: major side disagreement; Champion favors Mississippi State outright while market favors Alabama by 5.5. Total nearly aligned.
- Game 401856705 — Vanderbilt at Georgia, 2026-10-03 11:45 CT. ESPN/DraftKings: Vanderbilt +25.5 (-110), Georgia -25.5 (-110); total 53.5 (-110); Vanderbilt ML +1700, Georgia -4500. Availability: executable market displayed. Champion FIRST_FROZEN: Georgia by 24.5805; total 57.5598; Georgia win 0.922243. Market-vs-Champion: side near alignment; market total about 4.06 below Champion.
- Game 401858473 — Ohio State at Iowa, 2026-10-03 14:30 CT. FanDuel: Ohio State -14.5 (+100), Iowa +14.5 (-122); total 43.5 (-110); Ohio State ML -720, Iowa +500. Availability: executable market displayed. Champion FIRST_FROZEN: Iowa by 6.2898; total 51.1058; Iowa win 0.593141. Market-vs-Champion: major side disagreement; Champion favors Iowa outright while market favors Ohio State by 14.5. Market total about 7.61 below Champion.
