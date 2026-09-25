# CFB Engine Primitive Historical Coverage — Schedule Universe Recovery v1.92
Date: 2026-09-25
Status: authoritative-universe recovery checkpoint; no gate/model/source/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.91. Recovered the persisted Schedule Acquisition 2016-2025 package rather than inventing a comparison universe.

Package: CFB_ENGINE_WORKING_STATE_2026-09-23_SCHEDULE_ACQUISITION_v0_22.zip
Recovered authoritative inputs include:
- cfb_schedules_2016.csv ... cfb_schedules_2025.csv
- schedule_manifest_2016_2025.json
- schedule_population_audit_2017_2025.json
- population_ledger_2017_2025_pre_scope.json

The schedule audit states authority: CBS season membership maps 2017-2025; SportsDataverse schedule bytes; provider division diagnostic only.

## Target-season schedule universe
2021:
- raw/completed schedule rows 2408
- played regular FBS-vs-FBS before scope 732
- explicit championship labeled 0
- scope-ready primary if explicit labels sufficient 732
- unique admitted game IDs 732

2023:
- raw rows 3734; completed 3724
- played regular FBS-vs-FBS before scope 750
- explicit championship labeled 10
- scope-ready primary if explicit labels sufficient 740
- unique admitted game IDs 750

2024:
- raw rows 3801; completed 3799
- played regular FBS-vs-FBS before scope 752
- explicit championship labeled 9
- scope-ready primary if explicit labels sufficient 743
- unique admitted game IDs 752

2025:
- raw/completed rows 3831
- played regular FBS-vs-FBS before scope 762
- explicit championship labeled 9
- scope-ready primary if explicit labels sufficient 753
- unique admitted game IDs 762

All four target seasons report zero duplicate admitted game IDs, zero missing admitted game IDs, zero missing final scores in admitted rows, and zero provider-division disagreements in admitted rows.

## Important comparison rule
The v1.91 primitive-season counts (2021 887; 2023 1494; 2024 1609; 2025 1657) are NOT directly comparable to the scope-ready FBS-vs-FBS counts above because the full-season primitive producer covers a broader PBP universe.

Therefore count equality is not a valid coverage test. The correct next test is game-ID set inclusion:
authoritative admitted/scope-ready candidate IDs -> primitive_game_ids for the same season.

This avoids a false mismatch caused by comparing different populations.

## Next executable proof
Use the recovered population ledger / schedule audit to derive exact target game-ID sets for 2021/2023/2024/2025 and compare them to the v19 primitive_game_ids artifact:
- missing target IDs
- extra primitive IDs (diagnostic only)
- duplicate/malformed keys
- explicit championship scope treatment preserved separately.

Primitive Historical Coverage Gate remains OPEN until set-level reconciliation is complete.

## Governance
Latest integrated Library ZIP remains v1.73; v1.74-v1.92 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
RAW_TURNOVER_RATE remains OPEN/bounded. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
