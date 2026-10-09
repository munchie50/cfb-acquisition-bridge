# Friday Week 6 — prospective benchmark and decision review — October 9

Run: CFB_MANUAL_FRIDAY_REVIEW_20261009T123613Z. User-directed manual incremental work under Test Routine v6; separate from the morning scheduled cycle.
Status: CANONICAL_BENCHMARK_AND_PASS_REVIEW_PERSISTED_READ_BACK; full production refresh remains incomplete.
Champion v1.193/FIRST_FROZEN unchanged. Active v1.226 permits benchmark observation capture with independent timestamp semantics; benchmark is not execution.

## Fresh source observation
URL: https://www.espn.com/college-football/odds
Firecrawl maxAge=0; statusCode 200; scrapeId 01a120a7-b731-77a0-a31c-0d87b256d146.
Observation boundary: 2026-10-09T12:34:26.452Z / 07:34:26.452 CT.
Time means retrieval observation. Underlying bookmaker offer update time UNAVAILABLE; Caesars availability/price/executability NOT_VERIFIED.
Extraction: match exact ESPN game IDs, take the six linked DraftKings quotes from each matching game block, away spread/over/moneyline then home spread/under/moneyline. Open-column unlinked values are excluded. Five unique IDs; 26 checks passed for count, quote shape, opposite spread signs, paired totals, moneylines and future kickoff boundary.

| Game | ESPN ID | Scheduled UTC kickoff | Away spread/price | Home spread/price | Total/price | Away/home ML |
| --- | --- | --- | --- | --- | --- | --- |
| Florida State @ Louisville | 401858254 | 2026-10-09T23:00Z | +3.5 -108 | -3.5 -112 | o59.5 -112 / u59.5 -108 | +150 / -180 |
| Iowa @ Washington | 401858487 | 2026-10-10T01:00Z | +2.5 -105 | -2.5 -115 | o41.5 -105 / u41.5 -115 | +124 / -148 |
| Washington State @ Utah State | 401860922 | 2026-10-10T01:00Z | +5.5 -112 | -5.5 -108 | o43.5 -115 / u43.5 -105 | +170 / -205 |
| Wyoming @ San Jose State | 401864519 | 2026-10-10T01:00Z | +4.5 -112 | -4.5 -108 | o42.5 -112 / u42.5 -108 | +160 / -192 |
| Iowa State @ BYU | 401856826 | 2026-10-10T02:15Z | +10.5 -112 | -10.5 -108 | o46.5 -108 / u46.5 -112 | +330 / -425 |

Compared with preserved Oct 8 re-quote blob 135f4e0a2c4813dccef3a6c48f103eae20d5ee36: Iowa/Washington's spread changed from 3 to 2.5 with changed prices; Wyoming/SJSU's spread stayed 4.5 with changed prices. This is cross-retrieval benchmark comparison, not certified offer chronology or an earned price threshold.

## Availability and source boundary
Fresh reads of:
- https://cyclones.com/news/2026/10/7/football-primer-iowa-state-at-no-8-byu — scrape 01a120a8-5cbd-76fa-a56c-bfa026d6f9a1. Opponent-authored October 7 article still expects LJ Martin sidelined and Isaiah Glasker absent; this is not final independent inactive confirmation.
- https://byucougars.com/news/2026/10/5/byu-football-game-week-2026-iowa-state — scrape 01a120a8-a21b-7218-a581-49bd905bdb16. Article gives prospective Friday 20:15 MT kickoff while surrounding page chrome displays score-like data for that future matchup. The conflicting score/status region is quarantined from outcomes, availability inference and decision use. Primary-domain status is not sufficient to override chronology.
- https://hawkeyesports.com/sports/football/schedule — scrape 01a120a8-721a-7713-8035-7dda30efc282. Friday Washington entry retains 20:00 CDT.
- https://hawkeyesports.com/news/2026/10/5/notes-friday-night-at-washington — scrape 01a120a8-8643-7106-999d-54e471a863ef. Dated article retains 20:05 CT. Exact-minute conflict persists; date/section is known and no cutoff is extended.

Searches were bounded and did not establish exhaustive current injury status across the five games. Search absence is not evidence of health. No future scoreboard content was treated as actual result or used to adjust a frozen prediction.

## Prospective operational disposition
Decision boundary: 2026-10-09T12:38:21.065Z.
All five: PASS side / PASS total, no bet at this current review boundary. No qualified executable offer plus earned actionable rule/minimum acceptable price is established. This is insufficient evidence for action; it does not certify that market prices are bad, a frozen prediction is wrong, or a profitable opportunity cannot later arise.
No moneyline/parlay recommendation, stake, wager or extra casino trip established.
Minimum acceptable line/price and hard final execution cutoff remain NOT_ESTABLISHED; no numeric threshold or calibrated EV is fabricated.
Next: Friday 13:00 CT default reconciliation or earlier genuinely material qualified information before an actual useful execution cutoff. Do not reopen from raw movement alone, chase, or backfill Thursday's missing review.

## Executed persistence and readback
RUN_STARTED blob 3163c18d7f60cb360535dbc635f74efe6491e234.
Market append commit 6af3252d1ab27baa549275f8b7de97ebeeeac67a, exact read-back blob d13c5be0a12aed50242515e10362cdcd388cdcf2; complete prior bytes preserved.
Decision append commit 62b41d185a8f033444fcd07c5cfdbd644f95a5fa, exact read-back blob 1030aac4df11c82c74a936317db2591b1dbb5f52; complete prior bytes preserved.
Metadata collector executed on both real planned appends before writes. Independent content and expected Git blob readbacks matched afterward. This demonstrates permitted manual runtime metadata capture, not successful future-failure capture or natural scheduled production reliability.

Market planned-attempt metadata:
{
  "schema": "CFB_PLANNED_APPEND_METADATA_V1",
  "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS",
  "prior_git_blob_sha": "c8616b340917e5db2674ec6c16581dd0d09275a5",
  "proposed_git_blob_sha": "d13c5be0a12aed50242515e10362cdcd388cdcf2",
  "prior_sha256": "90c3f7a1cd6af54b6ca9f6bf7cbcb2db6bd83795eba7d65651b2fb8ace53a245",
  "proposed_sha256": "16b89d6abca4ecbaf4b55936aab3eb63943923151217c5dd9e8f8ed721a582b8",
  "delta_sha256": "25b99cabc0910e58270014b1467e96bbb9062d4b4b730117839b13b4076dfac7",
  "prior_bytes": 28901,
  "proposed_bytes": 31200,
  "delta_bytes": 2299,
  "prior_characters": 28865,
  "proposed_characters": 31162,
  "delta_characters": 2297,
  "prior_bytes_preserved": true,
  "field_inventory": [
    "availability",
    "book",
    "executability",
    "game_identity",
    "line",
    "observation_timestamp",
    "price",
    "provenance",
    "source"
  ],
  "inventory_basis": "CALLER_DECLARED_NOT_SEMANTICALLY_VALIDATED",
  "raw_content_included": false
}

Decision planned-attempt metadata:
{
  "schema": "CFB_PLANNED_APPEND_METADATA_V1",
  "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS",
  "prior_git_blob_sha": "07ede9343706473b37a8b509777d68d3a27beec7",
  "proposed_git_blob_sha": "1030aac4df11c82c74a936317db2591b1dbb5f52",
  "prior_sha256": "d81d9c73814a51fb0f70d84cede9306b42f206593152f6f98ee9bd37a558eac6",
  "proposed_sha256": "0c555c8b71425d748ebc13b075df9bd79d0d11ea1721d63584613f7948c47e4a",
  "delta_sha256": "26e196f5c5032bf4b68b276c9d64c0d4ac9f6d86c311c5f10265a5fc3209782a",
  "prior_bytes": 23669,
  "proposed_bytes": 26598,
  "delta_bytes": 2929,
  "prior_characters": 23565,
  "proposed_characters": 26482,
  "delta_characters": 2917,
  "prior_bytes_preserved": true,
  "field_inventory": [
    "champion_snapshot",
    "decision_state",
    "game_identity",
    "observation_timestamp",
    "provenance"
  ],
  "inventory_basis": "CALLER_DECLARED_NOT_SEMANTICALLY_VALIDATED",
  "raw_content_included": false
}

## Remaining acceptance debt
This is a bounded five-game manual update, not a full 49-row fresh production Hot Sheet. Morning scheduled cycle remains STARTED-only. No historical scheduled status is upgraded. Full-slate current observations, practical execution constraints and governed Hot Sheet persistence/readback remain required for production RUN_PASS.
Separate terminal candidate and closure must preserve RUN_INCOMPLETE for this partial production maintenance scope. Task lifecycle/cadences unchanged; natural 13:00 producer verification remains pending.
