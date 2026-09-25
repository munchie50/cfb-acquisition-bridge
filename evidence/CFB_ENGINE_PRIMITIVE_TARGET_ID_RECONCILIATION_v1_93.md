# CFB Engine Primitive Historical Coverage — Target ID Reconciliation v1.93
Date: 2026-09-25
Status: bounded primitive target-coverage proof; no full gate/model/source/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.92. Compared exact game-ID sets from the recovered authoritative pre-scope population ledger against primitive_game_ids.csv from successful full-season artifact 10889583560.

## Set-level results
2021:
- authoritative ledger target IDs: 732 PRIMARY_REGULAR_PROVISIONAL
- missing from primitive output: 0
- primitive IDs outside ledger: 155

2023:
- authoritative ledger target IDs: 750 total = 740 PRIMARY_REGULAR_PROVISIONAL + 10 CONFERENCE_CHAMPIONSHIP_PENDING
- missing regular IDs: 0
- missing championship-pending IDs: 0
- primitive IDs outside ledger: 744

2024:
- authoritative ledger target IDs: 752 total = 743 PRIMARY_REGULAR_PROVISIONAL + 9 CONFERENCE_CHAMPIONSHIP_PENDING
- missing regular IDs: 0
- missing championship-pending IDs: 0
- primitive IDs outside ledger: 857

2025:
- authoritative ledger target IDs: 762 total = 753 PRIMARY_REGULAR_PROVISIONAL + 9 CONFERENCE_CHAMPIONSHIP_PENDING
- missing regular IDs: 0
- missing championship-pending IDs: 0
- primitive IDs outside ledger: 895

## Proof
Every authoritative pre-scope target game ID for 2021, 2023, 2024, and 2025 exists in the authentic full-season primitive output.

Target-ID primitive coverage:
- 2021: 732/732
- 2023: 750/750
- 2024: 752/752
- 2025: 762/762

The large primitive-extra populations are expected from the broader PBP producer and are diagnostic only; they are not treated as target coverage failures.

## Classification
Primitive game-ID coverage for the recovered authoritative pre-scope universes is bounded PASS for 2021/2023/2024/2025.

This does not silently promote the full Primitive Historical Coverage Gate. Remaining gate questions include scope finalization/qualification where applicable, chronology/prediction-time authority, and any separately documented semantic/source proof obligations. The artifact itself still withholds authoritative prediction cutoffs.

## Governance
Latest integrated Library ZIP remains v1.73; v1.74-v1.93 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
RAW_TURNOVER_RATE remains OPEN/bounded. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
