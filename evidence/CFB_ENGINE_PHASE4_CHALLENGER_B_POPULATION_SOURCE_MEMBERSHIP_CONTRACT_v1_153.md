# CFB Engine — Challenger B Population Source and Membership Contract v1.153

Status: PROSPECTIVELY FROZEN / SOURCE ACQUISITION AUTHORIZED / NO FITTING OR SCORING
Parent: v1.152

## Governing population
Implement v1.124 literally: one canonical scheduled game belongs to the relevant-FBS universe when at least one participant is an FBS team under the season-appropriate membership authority and the game is a played/qualified game in the relevant season. Include:
- FBS vs FBS;
- FBS vs non-FBS/FCS;
- regular season;
- conference championships;
- bowls;
- CFP/postseason.
Exclude cancelled/unplayed games and unresolved identity conflicts.

## Source architecture
Primary schedule/event metadata source: SportsDataverse/cfbfastR schedule lineage, matching the source lineage already used by v1.148 and historically recorded by v1.92.
Required raw fields where available:
season, game_id, start_date, home_team, away_team, neutral_site, season_type/week/status/completed, home_division, away_division, plus classification metadata needed to distinguish postseason.

### Membership authority
Provider division labels are diagnostic, not sufficient authority by themselves, because v1.92 records historical CBS season-membership maps as population authority and provider division as diagnostic only.

For 2017-2025, first attempt to recover the exact historical CBS season-membership maps/ledger ancestry before substituting any new membership authority.
For 2016, historical scope was provisional; do not silently treat that provisional FBS-vs-FBS list as full v1.124 population authority.

If exact historical membership authority cannot be recovered for a season, classify that season MEMBERSHIP_AUTHORITY_OPEN and stop population acceptance rather than silently using provider labels.

## Outcome isolation
2016-2024 schedule outcomes may be present in raw source evidence because TRAIN/VALIDATION outcomes are already authorized historical evaluation data, but population membership/classification MUST NOT depend on scores/winners/model performance.

2025 raw source may contain historical outcomes only in quarantined source bytes. Any 2025 population projection must omit points, scores, winner/result and betting fields. No 2025 outcome may enter feature, prediction, model, or acceptance code before the separately authorized scoring gate.

## Population-conformance proof
Before schedule freeze, produce per-season and aggregate counts for:
- FBS-vs-FBS;
- FBS-vs-FCS/non-FBS;
- regular;
- conference championship;
- bowl/CFP/postseason;
- neutral;
- excluded cancelled/unplayed;
- unresolved membership/identity.
Also prove unique game IDs, canonical participant identity, kickoff presence and classification coverage.

The audit must compare actual represented classes against every required v1.124 inclusion class. A zero class is not automatically failure if the authoritative season genuinely has zero such games, but this requires explicit source evidence rather than omission.

## Legacy reconciliation
Compare corrected 2016-2024 game-ID membership with v1.108's 6,398 schedule rows and report:
- legacy IDs retained;
- newly included IDs by class;
- legacy IDs removed and exact reason.
Do not use Challenger-A performance to adjudicate membership.

For 2025 compare the corrected outcome-blind population with v1.148's 762 regular FBS-vs-FBS IDs, reporting additions/removals by class without scoring.

## Acceptance
PASS requires membership authority + source provenance + class coverage + identity/chronology checks.
Provider-label-only population may be diagnostic but cannot PASS where historical membership authority is required and unrecovered.

Locks: Challenger B prospective; no fitting; no scoring; 2025 protected; no market join; production v1 unchanged.
