# CFB Engine Full-Season Primitive Producer Recovery — v1.90
Date: 2026-09-25
Status: executable-ancestry recovery checkpoint; no gate/model/source/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.89. Deterministically enumerated repository root/workflows/evidence and inspected the primary full-season workflow rather than relying on incomplete code search.

## Recovered authentic producer
Repository path: .github/workflows/Main.yml
Current blob SHA: e69c381f1e76f1c322645a54e3404a195bf0085f

The workflow is explicitly named "CFB Semantic Canary Full-Season Audit" and contains an authentic 2016-2025 acquisition and primitive producer:
- acquires play_by_play_2016.rds through play_by_play_2025.rds from the pinned sportsdataverse-data cfbfastR_cfb_pbp release path;
- loops year in 2016:2025;
- derives scrimmage/event semantics;
- emits team_game_primitives including primitive_scrimmage_plays;
- emits primitive_season_game_counts.csv, primitive_game_ids.csv, primitive_game_team_rows.csv, integrity/field-coverage evidence, canonical text, and SHA-256;
- explicitly states scope "2016-2025 primitive join-key export and seasonal game reconciliation; authoritative chronology remains external";
- workflow artifact name cfb-semantic-canary-full-season-v19.

## Major correction to v1.88/v1.89 uncertainty
2021/2023/2024/2025 are NOT without executable ancestry. The authentic current repository producer covers all four seasons directly. The earlier zero code-search results were an indexing/search limitation, not substrate absence.

This is exactly the v5 Executable Ancestry Recovery lesson: deterministic enumeration recovered the producer after incomplete search failed.

## Next executable proof
The highest-value next step is not reconstructing a season-specific producer. It is to recover/verify the latest successful run/artifact for this full-season workflow (or safely execute the existing workflow if no valid artifact survives), then read primitive_season_game_counts / integrity outputs for 2021, 2023, 2024, 2025.

Do not claim those seasons pass the Primitive Historical Coverage Gate merely because the producer exists. Producer recovery proves executable readiness, not output acceptance.

Primitive Historical Coverage Gate remains OPEN.

## Governance
Latest integrated Library ZIP remains v1.73; v1.74-v1.90 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
RAW_TURNOVER_RATE remains OPEN/bounded. Prediction cutoff UNKNOWN/fail-closed. Second-order lineage evidence boundary preserved.
No fitting/tuning/source/model/production promotion.
