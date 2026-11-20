# Week12 Friday manual catch-up — mixed-book price integrity gate

STATUS: VERIFIED READ-ONLY DATA QUALITY SCREEN; NO NEW DECISIONS, WAGERS OR CANONICAL HOT SHEET.

## Inputs
- evidence/operational/CFB_WEEK12_20261120_0700_MANUAL_FULL_WORKING_CARD.md blob 00512a3f7820b9d3b2a6222b46a2a47c96db3bb3
- evidence/operational/CFB_MARKET_MONITOR_STATE.md recovered through GitHub REST contents (6,815,072 characters). Do not overwrite append-only ledger.

## Executed checks
Parsed all 64 game rows (6 Friday, 58 Saturday). All rows contain six semicolon-separated display fields. In 27/64 games, the visitor and home spread numbers do not sum to zero (differences of 0.5 or 1.0 points), and in 19/64 the displayed over and under totals differ (typically by 1 point). This confirms mixed-book side-by-side market columns cannot be treated as a synchronized, venue-executable paired offer. A six-field display is NOT a verified six-market executable snapshot. Two games also display missing moneyline offers, as recorded in preceding inventory audit.

Examples: Iowa State @ UCF visitor -1, home +1.5, over48.5 and under49.5; BYU @ Kansas visitor -5.5/home +6, over46.5/under47.5; Houston @ West Virginia over70.5/under71.5. Keep side-specific numbers and prices separate; do not manufacture consensus midpoint as a bookmaker quote. Previous model-total midpoint calculations are research-only diagnostics, not executable values.

## Correction to prior interpretation
The recovered Market Monitor ledger has 10 occurrences of the literal date 2026-11-20, but sampled contexts were 'kickoff_utc' fields for Friday games. Therefore earlier claim that these date occurrences established Friday market observations was not supported. Do not infer Friday capture coverage from the date substring count. Friday CBS source is independently present in the separate manual capture file, with its own timing/venue caveats. Current Decision/WAIT ledger has no literal 2026-11-20 in bounded search; no fresh Friday prospective decision was verified by that check.

## Next production work
For every actionable candidate, require a side-specific, book-identified and time-qualified quote plus verified material news and cutoff, then run governed v1 compiler and independent readback if checkout/ancestry gate permits. Do not promote prior PASS labels. No model or acceptance-rule relaxation. Friday 13:00 CT deadline not retroactively met.
