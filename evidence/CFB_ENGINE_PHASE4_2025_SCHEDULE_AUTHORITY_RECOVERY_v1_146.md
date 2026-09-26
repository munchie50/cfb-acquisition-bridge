# CFB Engine — 2025 Schedule Authority Recovery v1.146

Status: HISTORICAL AUTHORITY RECOVERED / RAW BYTES NOT CURRENTLY RECOVERED
Parent: v1.145 holdout substrate recovery
No 2025 outcomes scored or used for model evaluation.

## Recovered authority
Repository v1.92 proves that the persisted Schedule Acquisition v0.22 package previously contained:
- cfb_schedules_2016.csv through cfb_schedules_2025.csv
- schedule_manifest_2016_2025.json
- schedule_population_audit_2017_2025.json
- population_ledger_2017_2025_pre_scope.json

For 2025, that accepted audit recorded:
- raw/completed schedule rows: 3831
- played regular FBS-vs-FBS before scope: 762
- explicit championship labeled: 9
- scope-ready primary if explicit labels sufficient: 753
- unique admitted game IDs: 762
- duplicate admitted IDs: 0
- missing admitted IDs: 0
- provider-division disagreements in admitted rows: 0

Authority provenance recorded by v1.92: CBS season-membership maps 2017–2025; SportsDataverse schedule bytes; provider division diagnostic only.

## Recovery result
Deterministic current repository enumeration found no persisted 2025 schedule CSV.
Current Library enumeration/search did not recover the named Schedule Acquisition v0.22 ZIP or cfb_schedules_2025.csv bytes.

Therefore:
- the 762-ID population/count is authoritative historical evidence;
- it is NOT sufficient to reconstruct exact game metadata or schedule bytes;
- do not regenerate a schedule and call it byte-identical to v0.22;
- do not infer the 753-vs-762 championship treatment beyond the recorded v1.92 scope statement.

## Executable fallback
The current repository's authentic full-season workflow Main.yml still acquires 2025 PBP and proves broad 2025 game-ID substrate, but explicitly states authoritative chronology remains external. PBP game IDs cannot substitute for qualified schedule kickoff/home-away/neutral metadata.

A new 2025 schedule acquisition may be performed only as a new versioned source qualification, preserving provenance and comparing its admitted game-ID set/count to the authoritative historical 762-ID evidence. Outcome columns must be projected away before any holdout feature/prediction execution.

## Next action
Build a source-qualified 2025 schedule reacquisition/projection contract before retrieval. Freeze required metadata, population rule, comparison to the historical 762-ID authority, and outcome-stripping assertions. Only after that contract is persisted may fresh schedule bytes be acquired for holdout preparation.

Locks: no 2025 scoring; no outcome-bearing schedule to prediction code; no market join; no model redesign; no promotion.
