# CFB Engine Full-Season Primitive Artifact Audit — v1.91
Date: 2026-09-25
Status: bounded primitive-coverage checkpoint; no gate/model/source/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.90. Recovered an actual successful artifact from the authentic full-season producer rather than launching a new workflow.

## Verified successful run/artifact
Workflow: CFB Semantic Canary Full-Season Audit
Run: 36195406478 (run #44)
Conclusion: success
Head SHA: 109cbc8aa50396005eb2d73d1d853c123b65c80d
Artifact ID: 10889583560
Artifact name: cfb-semantic-canary-full-season-v19
Artifact digest: sha256:6774a059d701c1f7dc0364023f0f8a29e30d780408ba090f1e75a1cbd36e1a19

Artifact was downloaded and inspected directly.

## Primitive season game counts
2016 857
2017 869
2018 881
2019 887
2020 550
2021 887
2022 1459
2023 1494
2024 1609
2025 1657

This directly proves that the authentic producer generated primitive game rows for 2021, 2023, 2024, and 2025; those seasons are not missing from the executable primitive output.

## Integrity
team_game_primitive_integrity:
- rows: 22,299
- unique_keys: 22,299
- duplicate_key_rows: 0
- negative_scrimmage: 0
- negative_interceptions: 0
- negative_fumble_rows: 0
- negative_tod: 0

lineage_join_readiness:
- primitive_rows: 22,299
- unique_game_ids: 11,150
- missing_game_ids: 0
- duplicate_team_game_keys: 0
- authoritative_game_timestamp_in_this_artifact: FALSE
- prediction_cutoff_in_this_artifact: FALSE
- join_key: game_id
- required external authority: qualified schedule chronology / v0.23 temporal lineage

## Classification
For 2021/2023/2024/2025, primitive production existence and internal key/nonnegative integrity are bounded PASS on this artifact.

This is NOT yet a full Primitive Historical Coverage Gate PASS. The artifact itself explicitly withholds authoritative game timestamps and prediction cutoffs, and season counts alone do not prove reconciliation to an independently frozen candidate-game universe.

Next proof obligation: reconcile 2021/2023/2024/2025 primitive game IDs/counts against the appropriate authoritative candidate-game/schedule universe while preserving the known chronology/prediction-cutoff boundary.

## Governance
Latest integrated Library ZIP remains v1.73; v1.74-v1.91 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
RAW_TURNOVER_RATE remains OPEN/bounded. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
