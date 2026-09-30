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


## Full relevant-FBS slate sweep — 2026-09-27 13:13 CT
- Scope: all 47 FBS-vs-FBS FIRST_FROZEN games in the Oct. 1–3 Week 5 window.
- Broad benchmark: CBS Sports Week 5 FBS scoreboard, retrieved prospectively during this run. Benchmark lines without displayed prices are retained as benchmark observations only; they do not replace the exact-book/price records already captured at 13:08 CT.
- Coverage: benchmark side/total available for 44 of 47; NOT_YET_AVAILABLE for UTSA at Rice, Utah State at Boise State, and Arkansas State at Louisiana.
- Champion comparison source: accepted v1.208 FIRST_FROZEN artifact 10897612260. Full comparison is persisted in the governed Early Board/Hot Sheet created by this run.
- Chronology: this 13:13 sweep does not backfill the failed/unpersisted 13:00 observation boundary.


## Prospective reset capture — 2026-09-29 20:20 CT
Observation class: INTERMEDIATE / NEW_PROSPECTIVE_BOUNDARY. This capture resumes governed monitoring after the unrecoverable 2026-09-28 persistence gap. It does not reconstruct Monday observations.
Source semantics: FantasyData Week 5 consensus odds page retrieved live on 2026-09-29, with direct/cross-source confirmation where noted. Source URL: https://fantasydata.com/ncaa-football/odds
Champion link: v1.208 FIRST_FROZEN artifact 10897612260 / accepted Beta Champion lineage v1.193. Frozen prediction bytes were recovered directly from accepted artifact 10897612260; no model values were recomputed from current market information.

Current priority observations:
- Western Kentucky at New Mexico State: WKU +2.5 (-108), NMSU -2.5 (-112), total 57.5. Champion: NMSU by 26.5495, total 55.5829.
- North Texas at Tulsa: North Texas +1 (-111), Tulsa -1 (-110), total 57.5. Champion: Tulsa by 15.1102, total 56.2123.
- Notre Dame at North Carolina: Notre Dame -21 (-110), UNC +21 (-110), total 47.5. Champion: Notre Dame by 3.1262, total 45.3242.
- Alabama at Mississippi State: Alabama -6 (-110), MSST +6 (-112), total 60.5. Champion: MSST by 9.8652, total 60.0377.
- Syracuse at UConn: Syracuse -6.5 (-110), UConn +6.5 (-110), total 50.5. Champion: UConn by 6.8817, total 55.6316.
- Michigan at Minnesota: Michigan -5.5 (-111), Minnesota +5.5 (-111), total 43.5. Champion: Minnesota by 5.6597, total 45.2986.
- Ohio State at Iowa: Ohio State -14 (-111), Iowa +14 (-111), total 45.5. Champion: Iowa by 6.2898, total 51.1058.
- Memphis at Charlotte: Memphis -20.5 (-112), Charlotte +20.5 (-110), total 53.5. Champion: Memphis by 10.0046, total 61.3418.
- Eastern Michigan at Massachusetts: EMU +6.5 (-112), UMass -6.5 (-109), total 48.5. Champion: UMass by 22.0802, total 49.0269.
- Old Dominion at Georgia State: ODU +1.5 (-110), Georgia State -1.5 (-112), total 50.5. Champion: Georgia State by 11.1151, total 52.7631.
- Marshall at James Madison: Marshall +18.5 (-112), JMU -18.5 (-110), total 55.5. Champion: JMU by 29.5062, total 51.9170.
- Maryland at Nebraska: Maryland +14.5 (-110), Nebraska -14.5 (-112), total 52.0. Champion: Nebraska by 10.5205, total 56.0116. Direct BetMGM cross-check displayed Nebraska -15 and total 52.5 during the same evening research window, confirming meaningful cross-book spread variance rather than a single exact universal line.
- Kentucky at South Carolina: Kentucky +3 (-116), South Carolina -3 (-107), total 53.5. Champion: South Carolina by 13.7709, total 58.7110.
- Texas Tech at Colorado: Texas Tech -13 (-113), Colorado +13 (-109), total 50.5. Champion: Texas Tech by 1.7697, total 53.2790.
- Vanderbilt at Georgia: Vanderbilt +24 (-113), Georgia -24 (-110), total 50.5. Champion: Georgia by 24.5805, total 57.5598.

Coverage repair: current broad Week 5 board now displays qualified lines for the three games that were NOT_YET_AVAILABLE in the 2026-09-27 sweep: UTSA at Rice (UTSA -11.5, total 54.5), Utah State at Boise State (Boise State -20.5, total 51.5), and Arkansas State at Louisiana (Louisiana -6.5, total 47.5). These are current 2026-09-29 observations only; they are not backfilled as Sunday/Monday observations.

Interpretation: current market disagreement remains an investigation/decision-prioritization signal only. No market data entered the frozen Champion. No missing Monday line was reconstructed.
