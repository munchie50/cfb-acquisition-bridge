# CFB Evening Availability Week 8 Preflight — 2026-10-22 UTC

- cycle_id: CFB_EVENING_AVAILABILITY_20261022T012217Z
- assessed_at_utc: 2026-10-22T01:26:00Z
- assessed_at_ct: 2026-10-21 20:26:00 America/Chicago
- status: RUN_INCOMPLETE
- blocker_code: INITIAL_WEEK8_BOOTSTRAP_AFTER_ELAPSED_TARGET
- role: downstream Evening handoff only; no Hot Sheet selection/publication
- RUN_STARTED_blob: `a85d981a28387639d226ce820c7b98135e07b26b`
- authority_head_at_recovery: `51d916c7ba9349dea65053b293d802e9e5c20351`
- recovery_index_blob: `174dcc9f9a7ed3420c034329da6b9a30f76537a3`
- cadence_blob: `2a41f5cee71152c9f0a84cc3ee2f634020819dc2`
- Week8_profile_blob: `64562352da0fce99abece09602e4822d6cbc17d8`

## Fresh source and runtime proof

A complete live retrieval of the CBS Week 8 odds page was retained and independently read back:

- path: `evidence/operational/CFB_CBS_WEEK8_CURRENT_RESPONSE_20261022T012543Z.md`
- blob: `a9eacced476482b7bf34a7da44cb1261ae98023e`
- characters: 172899
- source URL: https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-8/
- recovered_by_utc: `2026-10-22T01:25:43Z`
- source class: unidentified mixed-book fallback
- consensus: CONSENSUS_UNAVAILABLE
- Caesars: UNVERIFIED

Python 3.12.14 executed the current WEEK8 route against the actual canonical parents, exact original-lineage file, actual cycle, current capture and current clocks. Normalization reconciled exactly 56 game identities / 112 team rows. Temporal census is 52 `FUTURE_AT_CAPTURE`, three `PAST_SOURCE_DATE_ONLY_EXACT_KICKOFF_UNAVAILABLE`, and one `STARTED_OR_PAST_AT_CAPTURE` (New Mexico State at Sam Houston). The compiler failed exactly:

`ValueError: initial Week8 bootstrap cannot reconstruct elapsed decisions`

The separate WEEK8 readiness audit also executed and failed exactly:

`ValueError: missing/incomplete canonical presentation block`

No proposal file was accepted or persisted.

## Nearest-window bounded research

The fresh board retained the three Thursday games as future source-display rows. These are fallback observations only, not consensus, verified Caesars offers, executable prices or decisions.

- James Madison at App State: displayed James Madison -10.5 (-108), App State +10.5 (-108), total 56.5; spread unchanged from the afternoon capture.
- Liberty at Kennesaw State: displayed Liberty -9.5 (-111), Kennesaw State +9.5 (-108), total 50.5. The displayed Liberty side moved from -10 (-111) in the afternoon capture.
- East Carolina at Memphis: displayed Memphis -10.5 (-105), East Carolina +10.5 (-112), total 54.5. The displayed Memphis side moved from -9.5 (-111) in the afternoon capture.

Bounded material review found the published Sun Belt availability summary still lists App State quarterback Malachi Singleton and running backs J'Marion Burnette and Treyaun Webb as questionable; App State defensive lineman Aiden Benton is out and Jordan Harris is out for the season. James Madison lists Deacon Rawls questionable and Jayden Studio / Frankie Tinilau doubtful. Source: https://ncfootballnews.com/games/app-state-football-vs-james-madison-2026/ . This is material research, but no independently qualified final report, immutable review, acceptable number or decision authority was earned.

The Liberty–Kennesaw and East Carolina–Memphis bounded previews confirmed the scheduled matchups and current football context but did not provide independently qualified final availability evidence supporting a decision. Sources:
- https://www.underdogdynasty.com/conference-usa/47021/weekday-cusa-previews-2026-week-8
- https://www.underdogdynasty.com/american-conference/47067/2026-week-8-preview-east-carolina-pirates-memphis-tigers
- https://ecupirates.com/sports/football/schedule
- https://gotigersgo.com/game-center/20061

A bounded weather check showed clear conditions around the three Thursday kickoff windows (approximately 54°F Boone, 68°F Kennesaw, 72°F Memphis) with no precipitation signal. Wind detail and an independently archived game-specific weather packet were unavailable; weather therefore remains non-actionable research, not a canonical decision fact.

## Canonical and decision disposition

Canonical readbacks remain:

- market: `87d735251e328226087daa9aa1519c22c702a762`; no Week8 typed packet
- decision: `65b87247a18060069402d9814692ab57ce97dcf3`; no Week8 typed packet
- execution: `75caee4052e02ea7d2453d1d37fd3866e13ecc07`; no Week8 wager
- scorecard: `674cfdbd884d51ef66e6b02d8caa215f368bf217`; Tuesday FIRST_FROZEN scoring preserved
- current selected Hot Sheet: historical Week7 blob `9dbec0ff1469fd06132ecd47374bcae25e9b3f5c`; not a Week8 decision surface

Evening cannot append a typed handoff because no Week8 canonical stream exists and initial bootstrap after elapsed targets is prohibited. It cannot reconstruct Tuesday or Wednesday decisions, silently omit elapsed identities, force PASS/INCONCLUSIVE, issue a conditional review without qualified evidence, or create a prose-only canonical tail. The bounded research above is diagnostic evidence only.

No market/decision/execution/scorecard canonical mutation, recommendation, acceptable number, parlay, wager, settlement, casino trip, Champion mutation, accepted REFRESH mutation, task mutation or schedule mutation occurred.

## Next safe action

An explicit governed disposition remains required: preserve the missing Tuesday and Wednesday decision history as permanent gaps and either authorize a prospective remaining-game Week8 stream without backfill or retain Week8 as unpublishable under the current profile. If authorized, the sole Market Monitor—not Evening—must create and validate the remaining-game typed stream and publish the current Hot Sheet.

RUN_INCOMPLETE
