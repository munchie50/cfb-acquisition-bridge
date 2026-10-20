# CFB Market Monitor Week 8 preflight — 2026-10-20 07:00 CT

- cycle_id: CFB_MARKET_MONITOR_20261020T115644Z
- authority_head_before_observability_write: `b0f906823dc4b3e4ade2733ed42646314e79d2c1`
- RUN_STARTED: `evidence/run_receipts/CFB_MARKET_MONITOR_20261020T115644Z_RUN_STARTED.md` / blob `33acd221b1a742cb3e7f3e02009bd60a080b1cf4`
- recovery_index: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md` / blob `174dcc9f9a7ed3420c034329da6b9a30f76537a3`
- Week8_profile: `evidence/CFB_WEEK8_ORIGINAL_LINEAGE_PUBLICATION_PROFILE_2026-10-20.md` / blob `64562352da0fce99abece09602e4822d6cbc17d8`
- outcome: source/runtime/lineage preflight proved; canonical Week8 publication blocked before proposal mutation.

## Proved current inputs

1. Computation runtime: Python 3.12.14.
2. Repository history was fully recovered so immutable review ancestry could be checked.
3. Authenticated original freeze archive `10897612260` was recovered at its accepted boundary. With `CFB_ACCEPTED_FREEZE_ARCHIVE` bound to that file, `python -m unittest discover -s scripts -p test_cfb_week8_publication.py` completed 36/36 tests successfully.
4. Week8 original lineage is `evidence/scheduler_qa/CFB_WEEK8_ORIGINAL_ANCESTRY_RECOVERY_20261020.json` / blob `337a23b03a10617ff87d9ba8c1c224cd3ebe1d9c`: exact 56 identities, 49 original predictions, 7 original exclusions.
5. Genuinely fresh complete CBS response:
   - path: `evidence/operational/CFB_CBS_WEEK8_FULL_BOARD_TABLES_20261020T120230Z.md`
   - blob: `272007830337fa897812cb16dc5aa2ffb28f6dba`
   - recovered_by: `2026-10-20T12:02:30Z`
   - Firecrawl scrape: `01a15930-f443-740a-a46e-91a5da60d41c`
   - source status: HTTP 200
   - deterministic normalization: 56/56 games, 112/112 team rows, 56 future games, no missing identities
   - normalized source SHA256: `a9c5af8574ab0957591533a76604b3385ce90259e35a56d02b3faf1565a93c4c`
   - source class: `UNIDENTIFIED_FIELD_LEVEL_MIXED_BOOK_FALLBACK_ONLY`
   - consensus: `CONSENSUS_UNAVAILABLE`
   - Caesars: `UNVERIFIED`
   - executability: `UNVERIFIED`
6. Existing canonical readbacks remain:
   - market `87d735251e328226087daa9aa1519c22c702a762`
   - decision `65b87247a18060069402d9814692ab57ce97dcf3`
   - execution `75caee4052e02ea7d2453d1d37fd3866e13ecc07`
   - postgame scorecard `7a6defc4b93ff5c1752890130ff9bdaf50deb2e5`
   - no `cfb-week8-market-v1` or `cfb-week8-decision-v1` canonical packet is present.
7. Tuesday candidate automation is scheduled for 10:00 CT. It was not yet due at this cycle and candidate generation would remain NOT_ACCEPTED until independent acceptance. The accepted original56 FIRST_FROZEN lineage exists independently and was not replaced by a REFRESH.

## Exact publication blocker

The Week8 producer is now the correct route and source normalization succeeds. Publication cannot lawfully advance because this invocation does not have a complete set of 56 independently earned current decision rows satisfying the all-game/all-market review controls. A diagnostic invocation with an empty decision-row set reached the Week8 bootstrap population guard and stopped with:

`ValueError: bootstrap population mismatch`

This is not a missing-prediction blocker. It is a missing independently earned decision/research boundary. The live source exposes current spread, moneyline and total fields, but:

- full material/injury/weather review was not completed for all 56 games;
- source-display kickoff timestamps remain `RETAINED_UNVERIFIED`, not independently qualified;
- no new immutable conditional review references were earned;
- no independently qualified non-Caesars constituent collection established consensus;
- no actual Caesars execution offer was verified;
- alternates/team totals and plausible parlay prices were not comprehensively available or independently reviewed.

The profile expressly prohibits automatic PASS or synthetic INCONCLUSIVE rows. Therefore no canonical Week8 market/decision packet, Hot Sheet, recommendation, wager, settlement, navigation selection, or Champion/REFRESH mutation was written.

## Nearest-window source observations — not decisions

| Game | Source-display kickoff | Engine Prediction (Frozen) | Fresh CBS fallback |
|---|---|---|---|
| Missouri State @ Delaware | Tue 6:00 PM CT, RETAINED_UNVERIFIED | Delaware -11.1; total 55.3; home win 0.768 | Missouri State +3 (-111), ML +130; Delaware -2.5 (-122), ML -152; total 52.5 |
| Middle Tennessee @ Florida International | Tue 6:00 PM CT, RETAINED_UNVERIFIED | FIU -3.2; total 47.3; home win 0.507 | MTSU +10.5 (-120), ML +320; FIU -10 (-110), ML -380; total 45.5 |
| South Alabama @ Marshall | Tue 6:30 PM CT, RETAINED_UNVERIFIED | South Alabama -4.4; total 50.2; home win 0.420 | South Alabama -3 (-111), ML -152; Marshall +3.5 (-124), ML +136; total 65.5 |

Raw model/market disagreement is an investigation flag only. No acceptable number, state transition, or bet is inferred.

## Settlement and execution

No new user-confirmed ticket or execution was supplied. The execution ledger remains at 15 historical established wagers / $53.45 cumulative stake; the latest four-ticket settlement remains $20.00 staked, $14.55 returned, -$5.45 net. No new settlement or scorecard join applies to Week8 before games.

## Required next safe action

At the next prospective Monitor boundary, recover a new fresh complete response, independently qualify kickoff/material/source evidence, complete and preserve the full 56-game decision review across both spread sides, both moneylines, totals, available alternates/team totals and bounded plausible parlays, then run `scripts/cfb_week8_publication.py` with those earned decision rows. Only validated proposals may proceed to serialized SHA-guarded canonical writes, independent renderer/invariant/readiness/navigation audits, current Hot Sheet selection, and two-phase terminal closure.

RUN_INCOMPLETE
