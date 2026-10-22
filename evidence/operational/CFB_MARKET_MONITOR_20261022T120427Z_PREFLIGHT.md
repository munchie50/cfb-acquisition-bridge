# CFB Market Monitor preflight — 2026-10-22 07:04 CT

- cycle_id: CFB_MARKET_MONITOR_20261022T120427Z
- result: RUN_INCOMPLETE
- run_started_readback_blob: 3e57a69d70e92ad67b6b3d336371edf1b56df24c
- supported_runtime: Python 3.12.14
- authority_head_at_start: 94cc9161dc19b53ef72418d2d86281eb901ef34d
- recovery_index: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md
- cadence: evidence/CFB_ENGINE_FOOTBALL_WEEK_OPERATING_CADENCE_CONTRACT_v1_247.md
- Week8 profile: evidence/CFB_WEEK8_ORIGINAL_LINEAGE_PUBLICATION_PROFILE_2026-10-20.md
- accepted original census: 56 targets / 49 predictions / 7 exclusions

## Fresh complete source

- path: evidence/operational/CFB_CBS_WEEK8_CURRENT_RESPONSE_20261022T120641Z.md
- readback_blob: dc301d105aaf595b15e7ee2bf18fcbbd53c4d3ff
- readback_chars: 172974
- source: https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-8/
- recovered_at_utc: 2026-10-22T12:06:41Z
- normalized population: exactly 56 games
- temporal classification: 52 FUTURE_AT_CAPTURE; 4 PAST_SOURCE_DATE_ONLY_EXACT_KICKOFF_UNAVAILABLE
- elapsed identities: 401871069 Missouri State @ Delaware; 401871055 Middle Tennessee @ Florida International; 401871092 South Alabama @ Marshall; 401871070 New Mexico State @ Sam Houston
- source role: qualified retained source packet only. The mixed-book rows are not qualified multi-book consensus; Caesars is UNVERIFIED.

## Executable preflight

Normal advance command used `scripts/cfb_week8_publication.py` with the actual canonical market/decision files, actual Week8 original lineage, the fresh complete capture, actual cycle_id and actual as_of/recovered-by clock.

Compiler result:

`ValueError: initial Week8 bootstrap cannot reconstruct elapsed decisions`

The Week8 readiness audit, run with `--profile WEEK8` against the actual canonical files and clock, separately returned:

`ValueError: missing/incomplete canonical presentation block`

This is a real publication blocker. A saved replay, synthetic decision row, hindsight PASS, or reconstruction of the four elapsed games is prohibited. No Week8 market packet, decision packet, rendered Hot Sheet, current navigation binding, recommendation, wager or execution was created.

## Current Thursday source observations — diagnostic only

| Game | Engine Prediction (Frozen) | Fresh mixed-book fallback | Movement from 2026-10-22 01:25Z capture | Status |
|---|---|---|---|---|
| James Madison @ App State, 18:00 CT | James Madison -3.6 / total 52.5 / App State home p 0.434 | James Madison -11.5 (-105); App State +11.5 (-111); ML -426/+360; total 56.5 (-108/-110) | JMU spread moved one point from -10.5; total unchanged | CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; investigation flag only |
| Liberty @ Kennesaw State, 18:00 CT | FIRST_FROZEN EXCLUDED — away_prior_pbp_missing | Liberty -9.5 (-112); Kennesaw +9.5 (-105); ML -365/+310; total 50.5 (-105/-111) | spread unchanged; Liberty price -111 to -112; total unchanged | no model comparison; CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED |
| East Carolina @ Memphis, 18:30 CT | Memphis -15.6 / total 55.5 / Memphis home p 0.832 | Memphis -10.5 (-108); ECU +10.5 (-108); ML -417/+333; total 54.5 (-111/-105) | spread unchanged; Memphis price -105 to -108; total unchanged | CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; investigation flag only |

Raw frozen-versus-fallback disagreement is not calibrated EV and did not generate a recommendation. No threshold, joint price, parlay probability, payout, stake, or execution was invented. Alternates/team totals and a qualified joint-price parlay review were not available from the retained response and remain NOT_EVALUATED, not PASS.

## Availability and weather boundary

- Sun Belt's current availability-report surface was recovered, and a current secondary report retained App State QB Malachi Singleton plus RBs J'Marion Burnette and Treyaun Webb as questionable. Complete immutable current player rows for both teams were not recovered in a form eligible for a decision review.
- Conference USA's official availability-control page was recovered, but its embedded current Liberty/Kennesaw participant rows were not independently retained. Missing rows remain visible research debt.
- No independently qualified complete current ECU/Memphis availability packet was recovered.
- Boone forecast for the 19:00 ET kickoff was clear near 56°F; Memphis forecast for the 18:30 CT kickoff was clear near 72°F. No weather fact earned a decision change. A qualified Kennesaw forecast was not retained.
- Sources: https://sunbeltsports.org/news/2025/8/11/football-availability-report-new.aspx ; https://conferenceusa.com/sports/2025/8/23/FB_0823254134.aspx ; https://ncfootballnews.com/games/app-state-football-vs-james-madison-2026/

## Canonical readback and safe mutation

- market_state_blob: 87d735251e328226087daa9aa1519c22c702a762 (unchanged; no Week8 packet)
- decision_ledger_blob: 65b87247a18060069402d9814692ab57ce97dcf3 (unchanged; no Week8 packet)
- execution_ledger_blob: 75caee4052e02ea7d2453d1d37fd3866e13ecc07 (unchanged; no new production or $20 sandbox execution)
- scorecard_blob: c9203836e0be102593a8eb7d508f7d8bd4c05bd2 (changed and independently read back)
- authoritative result joined: New Mexico State 30, Sam Houston 24, source https://gobearkats.com/game-center/15542
- original frozen row: Sam Houston +13.8 home margin / 53.8 total / 0.786 home win probability
- actual: home margin -6 / total 54 / margin error -19.8 / total error +0.2 / SU correct 0
- scientific effect: NONE; Champion/FIRST_FROZEN/REFRESH lineage unchanged
- settlement: none; no established execution existed

## Publication disposition

A governed Week8 Hot Sheet could not be produced or read back, so RUN_PASS is prohibited. The user-facing current Week8 full-slate/top-10 decision remains incomplete. The existing historical Week7 Hot Sheet was not relabeled or presented as current.

Next safe action: an explicit accepted governance disposition must decide whether a prospective remaining-game Week8 stream may begin without reconstructing the four elapsed decision histories, while retaining those historical gaps. If accepted, the next Monitor may acquire complete current source, independently qualified kickoff/review inputs, run normal Week8 compilation, publish/read back exactly one current Hot Sheet, and close prospectively. Until then, preserve the source, scorecard join, canonical parents and all four recurring schedules without replay.

RUN_INCOMPLETE
