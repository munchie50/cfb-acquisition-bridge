# CFB Engine — Phase 4 Derived Feature Coverage Disposition v1.114

Date: 2026-09-25
Status: BOUNDED PASS / PARTIAL BY DOMAIN
Predecessor: CFB_ENGINE_PHASE4_PROSPECTIVE_DERIVED_FEATURE_DEFINITIONS_v1_112.md
Run: 36200019556
Run conclusion: SUCCESS
Head SHA: ba2b14d52d808ad178576a71b00392631b68a59e
Artifact ID: 10890972719
Artifact digest: sha256:dc781ed8e9e1febf9e197b5566748d1fb995e4633d11be8076744065eb6a209d
Coverage CSV SHA-256: 2f219c504bac531130e170b350454d170965a60c06b8abb8eda50620ef6c710e
Production effect: NONE
2025 TEST: EXCLUDED
Fitting/tuning: NOT AUTHORIZED

## Population
2016-2024 development PBP only.
Total PBP rows: 1,684,541.
Eligible scrimmage plays: 1,280,965.

## Explosiveness
All 1,280,965 eligible scrimmage plays have non-null yards_gained.
Missing explosiveness context: 0.
Disposition: CONTEXT COVERAGE PASS for frozen v1.112 >=20-yard definition.
Still requires deterministic feature-generation canary and independent row reproduction before feature acceptance.

## Success rate
Context-qualified eligible plays: 1,280,459.
Explicitly excluded for missing/invalid required context: 506 of 1,280,965.
No zero-fill is permitted.
Disposition: BOUNDED CONTEXT COVERAGE PASS with explicit missing-context denominator handling.
Still requires deterministic feature-generation canary and independent row reproduction.

## Drive identity / field position
Rows with valid pos_team + drive_id + yards_to_goal: 1,684,541.
Missing drive_id rows in audited offensive context: 0.
Missing yards_to_goal rows in audited offensive context: 0.
Unique valid game/team/drive identities: 242,385.
Disposition: CONTEXT COVERAGE PASS for frozen drive-start field-position definition.
Still requires deterministic feature-generation canary and independent row reproduction.

## Scoring opportunities
Rows at opponent 40 or closer: 533,479.
Unique game/team/drive scoring opportunities after deduplication: 116,272.
Repeated inside-40 rows: 417,207.
Disposition: scoring-opportunity IDENTIFICATION / DEDUP SUBSTRATE PASS for frozen v1.112 definition. Drive must be counted once.

## Finishing-drive points
drive_result is not uniformly populated in later seasons and the existing validated semantic producer does not establish drive-level offensive point totals.
drive_result_detailed is broadly populated but has only been qualified for bounded event classification, not numeric drive scoring.
Disposition: DEFINITION FROZEN / POINT-ATTRIBUTION BLOCKED. Do not infer numeric drive points from labels or final game score allocation.

## Gate
Explosiveness, success rate, and field position may advance to deterministic TRAIN/VALIDATION-only feature-generation canary under v1.112.
Scoring-opportunity identity may be carried as a validated drive denominator substrate.
points_per_scoring_opportunity may NOT advance until independent drive-point semantics are qualified.

No model performance, market information, or 2025 TEST result was inspected to reach these dispositions.
