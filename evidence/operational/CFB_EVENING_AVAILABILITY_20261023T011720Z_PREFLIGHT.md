# CFB Evening Availability preflight — 2026-10-23 UTC

- cycle_id: CFB_EVENING_AVAILABILITY_20261023T011720Z
- role: downstream typed handoff only; no competing Hot Sheet
- actual_as_of_utc: 2026-10-23T01:24:00Z
- actual_as_of_ct: 2026-10-22 20:24:00 America/Chicago
- RUN_STARTED_blob_read_back: `4b74dc81f96fc0b40687a73fe67bcbf652cb7184`
- Python_runtime: 3.12.14 AVAILABLE
- source_path: `evidence/operational/CFB_CBS_WEEK8_CURRENT_RESPONSE_20261023T012200Z.md`
- source_blob_read_back: `3e1a32b70acb357585abf1f6bed6c87637557151`
- source_SHA256: `946568a6a2989ca360a8ae14fc0e8f5072a9d5cff04c7b22ae92c35bbe0ea178`
- source_URL: https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-8/
- response_recovered_by_utc: 2026-10-23T01:22:00Z
- clock_semantics: RESPONSE_RECOVERED_BY upper bound; not exact bookmaker update time
- source_population: 56 governed games / 112 team rows / 49 future / seven started-or-past at capture / zero missing IDs
- source_qualification: UNIDENTIFIED_FIELD_LEVEL_MIXED_BOOK_FALLBACK_ONLY
- consensus: CONSENSUS_UNAVAILABLE
- Caesars: UNVERIFIED
- executability: UNVERIFIED
- quarantined_source_fields: Final and Open
- compiler_result: VALIDATED_WEEK8_PROPOSALS_ONLY_NOT_PERSISTED
- proposal_market_blob: `9da9d59e4ca1295ef7f44f730fe0ef75d3ff76e6`
- proposal_decision_blob: `0e480fa11f26e63c9ece1923ea59524aafff5c67`
- proposal_population: 56; 43 INCONCLUSIVE / nine PASS / four HISTORICAL_GAP
- elapsed_current_quotes_after_proposal: zero
- overdue_open_decisions_at_actual_clock: zero
- decision_transition: NONE; Friday 13:00 CT reconciliation has not arrived, and no new evidence earned a supported action, WAIT, line/price limit or analytical PASS
- canonical_Hot_Sheet_effect: NONE; next Market Monitor retains sole publication ownership

## Nearest-window material revalidation

The manual Friday review recovered by 2026-10-23T01:10:15Z remains applicable at this run boundary and was checked against current official/source discovery. It covers both spread sides, both moneylines, over/under, offered derivatives and parlay suitability for the four eligible Friday games. No newly discovered fact supports promotion beyond its recorded maturity.

- UMass at UConn: official UConn preview confirms Friday 7:00 PM ET. UMass's documented backup-QB scenario remains unresolved for final availability. Current CBS fallback is UMass +14.5 -110 / +530, UConn -14.5 -105 / -667, over 50.5 -108 / under 50.5 -110. No side, moneyline or total recommendation is earned.
- Duke at Virginia: official Virginia report still lists Flores, Costner and Minter out; Hillman and Courtney questionable. Current CBS fallback is Duke +2.5 -110 / +108, Virginia -2 -111 / -125, over 46.5 -115 / under 47.5 -114. Personnel uncertainty prevents automatic use of the frozen-model gap.
- Air Force at Wyoming: official Wyoming report confirms Evan Svoboda/Szarka context as previously preserved: Szarka season-ending and Medders taking over; Air Force rushing and possession strengths remain countered by Wyoming's improving dual-threat offense and home setting. Current CBS fallback is Air Force -5.5 -105 / -205, Wyoming +6 -111 / +180, over 44.5 -118 / under 45.5 -114. Existing Air Force spread view remains an EXPERIMENTAL_LEAN only, not a qualified recommendation.
- NC State at Stanford: dated NC State line injuries and Stanford personnel uncertainty remain material; no final official active list was recovered. Current CBS fallback is NC State -6.5 -122 / -260, Stanford +7 -111 / +215, over 55.5 -105 / under 55.5 -111. No side, moneyline or total recommendation is earned.

Weather recheck for Friday game windows: Storrs clear near 49°F at 6 PM CT; Charlottesville mostly clear near 56°F at 6 PM CT; Laramie intermittent clouds near 53°F around the source-displayed evening window after an earlier afternoon thunderstorm chance; Stanford mostly clear near 64°F around 7 PM local. These broad location forecasts do not independently establish stadium wind or a betting edge.

## Timing and portfolio boundary

The user's actual latest placement constraint is Friday October 23 at 7:00 PM CT. It does not prove earlier access. UMass-UConn and Duke-Virginia are source-displayed for 6:00 PM CT and therefore cannot safely use the 7:00 PM cap. Air Force-Wyoming and NC State-Stanford are later, but their existing Friday 1:00 PM CT research reconciliation remains unchanged. No extra trip, wager, execution or sandbox action is created.

## Concurrency and integrity

Manual cycle `CFB_MARKET_MONITOR_20261023T011631Z` began immediately before this scheduled Evening cycle and is researching Saturday early-window/source gaps. It has not changed canonical market, decision, execution, money, scorecard or selected Hot Sheet surfaces at this preflight. Evening will serialize only its typed market/decision append using immediate prewrite SHAs and will not claim the manual cycle's unclosed work.

Champion, FIRST_FROZEN, accepted REFRESH, execution, money and scorecard effects: NONE.
