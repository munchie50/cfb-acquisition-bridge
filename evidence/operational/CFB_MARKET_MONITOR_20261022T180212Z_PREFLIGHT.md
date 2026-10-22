# CFB Market Monitor preflight — 2026-10-22 13:02 CT

- cycle_id: CFB_MARKET_MONITOR_20261022T180212Z
- result: RUN_INCOMPLETE
- run_started_readback_blob: dd971b699ffa68c6fbb8661e0a24488ca64b6de4
- supported_runtime: Python 3.12.14
- authority_head_at_start: 556cc8e539b77c42d78ece4b01b20eacfb7005c9
- recovery_index: evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md
- cadence: evidence/CFB_ENGINE_FOOTBALL_WEEK_OPERATING_CADENCE_CONTRACT_v1_247.md
- Week8 profile: evidence/CFB_WEEK8_ORIGINAL_LINEAGE_PUBLICATION_PROFILE_2026-10-20.md
- accepted original census: 56 targets / 49 predictions / 7 exclusions
- governance change since morning: NONE

## Fresh complete source

- path: evidence/operational/CFB_CBS_WEEK8_CURRENT_RESPONSE_20261022T180321Z.md
- readback_blob: 60114670f65e6cb893a8d99f4c01c024df499b66
- readback_chars: 173169
- source: https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-8/
- recovered_at_utc: 2026-10-22T18:03:21Z
- normalized population: exactly 56 games
- temporal classification: 52 FUTURE_AT_CAPTURE; 4 PAST_SOURCE_DATE_ONLY_EXACT_KICKOFF_UNAVAILABLE
- elapsed identities: 401871069 Missouri State @ Delaware; 401871055 Middle Tennessee @ Florida International; 401871092 South Alabama @ Marshall; 401871070 New Mexico State @ Sam Houston
- source role: mixed-book fallback, not qualified multi-book consensus; Caesars and executability UNVERIFIED

## Executable preflight

Normal advance execution used `scripts/cfb_week8_publication.py` with actual canonical inputs, the fresh source, accepted Week8 lineage, actual cycle_id and actual source/as-of clock.

Compiler result:

`ValueError: initial Week8 bootstrap cannot reconstruct elapsed decisions`

The actual `scripts/cfb_hot_sheet_readiness.py --profile WEEK8` audit separately returned:

`ValueError: missing/incomplete canonical presentation block`

The blocker is unchanged and earned. No later repository authority permits a prospective remaining-game stream that bypasses the missing four historical decision rows. No reconstruction, automatic PASS, synthetic INCONCLUSIVE, deadline extension, or stale-sheet relabeling was performed.

## Thursday practical-window observations — diagnostic only

| Game | Engine Prediction (Frozen) | 13:03 CT mixed-book fallback | Movement since 07:06 CT | Availability/review status |
|---|---|---|---|---|
| James Madison @ App State, 18:00 CT | James Madison -3.6 / total 52.5 / App State home p 0.434 | JMU -11.5 (-110), App State +12 (-111); ML -465/+360; total 56.5 (-108/-110) | favorite price -105 to -110; underdog line +11.5 to +12; JMU ML -426 to -465 | App State QB Malachi Singleton changed from questionable to available; RB J'Marion Burnette remained a game-time decision. Complete immutable two-team review absent. |
| Liberty @ Kennesaw State, 18:00 CT | FIRST_FROZEN EXCLUDED — away_prior_pbp_missing | Liberty -9.5 (-110), Kennesaw +9.5 (-108); ML -365/+300; total 50.5 (-105/-108) | favorite price -112 to -110; dog price -105 to -108; dog ML +310 to +300 | CUSA current player report still not independently retained; no model comparison exists. |
| East Carolina @ Memphis, 18:30 CT | Memphis -15.6 / total 55.5 / Memphis home p 0.832 | Memphis -10.5 (-108), ECU +10.5 (-112); ML -417/+333; total 54.5 (-108/-110) | ECU price -108 to -112; total prices changed | no complete independently qualified current availability/review packet |

The asymmetric JMU/App State spread confirms cross-book dispersion rather than a consensus line. Raw disagreement with frozen predictions is an investigation flag only, not calibrated EV. No side, total, moneyline, alternate, team total or parlay earned an actionable or PASS state in canonical Week8 state. Missing research is not proof of no value. No threshold, stake, probability, payout, or execution was invented.

Availability sources: https://www.rotowire.com/cfootball/headlines/malachi-singleton-news-available-thursday-236296 ; https://www.foxsports.com/college-football/james-madison-dukes-vs-appalachian-state-mountaineers-oct-22-2026-game-boxscore-43767 ; https://conferenceusa.com/sports/2025/8/23/FB_0823254134.aspx

## Canonical readback

- market_state_blob: 87d735251e328226087daa9aa1519c22c702a762 (unchanged; no Week8 packet)
- decision_ledger_blob: 65b87247a18060069402d9814692ab57ce97dcf3 (unchanged; no Week8 packet)
- execution_ledger_blob: 75caee4052e02ea7d2453d1d37fd3866e13ecc07 (unchanged; no production or $20 sandbox execution)
- scorecard_blob: c9203836e0be102593a8eb7d508f7d8bd4c05bd2 (unchanged after morning's authoritative Wednesday join)
- settlements: NONE
- Champion/FIRST_FROZEN/REFRESH mutation: NONE

## Publication disposition

The required Week8 Hot Sheet, full-slate all-market review and ranked Top 10 opportunities were not publishable/readable, so RUN_PASS is prohibited. This cycle adds a fresh source and material pre-kickoff availability/price diagnostics, but it does not create a competing card.

Next safe action: obtain an explicit accepted governance disposition authorizing or declining a prospective remaining-game Week8 stream while permanently retaining the four missing historical decision identities. If authorized, the next prospective cycle must acquire complete current source, independently qualified kickoffs/reviews, compile typed market/decision packets, render/audit one current Hot Sheet, persist all surfaces serially, and read them back. Historical decisions remain non-reconstructible.

RUN_INCOMPLETE
