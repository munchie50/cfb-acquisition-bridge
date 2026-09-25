# CFB Engine Primitive Missing-Field Case Audit — v1.96
Date: 2026-09-25
Status: bounded semantic exception audit; no semantic/model/source/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.95. Audited the exact 10 offset==0 cases preserved by primitive_missing_field_context.csv in successful full-season artifact 10889583560 and cross-checked primitive_field_coverage_by_game.csv.

## Exact 10-case population
All 10 preserved cases are from 2022 or 2025, as intentionally selected by the producer.

2022:
- game 401404080, play 401404080101901: scrimmage row, missing down only; text: J. Hill rushed for 6 yards; play_type Rush; yards_gained 6; distance 10.
- game 401404102, play 401404102102902: scrimmage row, missing down only; text: B. Robinson rushed for 4 yards; play_type Rush; yards_gained 4; distance 6.
- game 401404124, play 401404124103901: scrimmage row, missing down only; text: N. Singleton rushed for 3 yards; play_type Rush; yards_gained 3; distance 10.
- game 401404146, play 401404146104901: scrimmage row, missing down only; text: T. Henderson rushed for 2 yards; play_type Rush; yards_gained 2; distance 10.
- game 401404168, play 401404168105901: scrimmage row, missing down only; text: B. Corum rushed for 5 yards; play_type Rush; yards_gained 5; distance 10.

2025:
- game 401762892, play 401762892102901: scrimmage row, missing distance only; text: C. Brown rushed for 5 yards; play_type Rush; down 1; yards_gained 5.
- game 401762894, play 401762894103901: scrimmage row, missing distance only; text: D. Sampson rushed for 4 yards; play_type Rush; down 2; yards_gained 4.
- game 401762896, play 401762896104901: scrimmage row, missing distance only; text: O. Gordon rushed for 3 yards; play_type Rush; down 3; yards_gained 3.
- game 401762898, play 401762898105901: scrimmage row, missing distance only; text: A. Jeanty rushed for 6 yards; play_type Rush; down 1; yards_gained 6.
- game 401762900, play 401762900106901: scrimmage row, missing distance only; text: N. Singleton rushed for 2 yards; play_type Rush; down 2; yards_gained 2.

No preserved target case is missing play ID, offense, defense, period, drive ID, yards_gained, yards_to_goal, or play_type.

## Per-game coverage cross-check
The corresponding 10 game rows in primitive_field_coverage_by_game.csv each contain exactly one relevant scrimmage-field absence:
- five 2022 games: scrimmage_missing_down=1, other audited missing counters zero;
- five 2025 games: scrimmage_missing_distance=1, other audited missing counters zero.

## Semantic effect
These rows remain identifiable scrimmage plays through rush/pass/pass_attempt evidence and therefore still contribute to primitive_scrimmage_plays. The missing down/distance fields do not erase the occurrence from the primitive play-volume count.

No evidence supports inventing the missing down or distance values. Preserve them as source-null exceptions.

This bounded audit therefore finds:
- primitive play-volume occurrence affected: NO for these 10 rows;
- down/distance contextual completeness affected: YES;
- safe source-value reconstruction: NO;
- need to remove these rows from primitive_scrimmage_plays: NO.

## Classification
The exact 10-case missing-field exception population is bounded and source-null-preserving. It does not create a known primitive_scrimmage_plays coverage gap.

PRIMITIVE_SEMANTIC_CORRECTNESS remains PARTIAL overall, but this specific missing-field branch is CLOSED as a primitive play-volume blocker. Reopen only if a downstream feature explicitly requires the missing contextual field and has an evidence-backed recovery rule.

## Governance
Latest integrated Library ZIP remains v1.73; v1.74-v1.96 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
No fitting/tuning/source/model/production promotion.
