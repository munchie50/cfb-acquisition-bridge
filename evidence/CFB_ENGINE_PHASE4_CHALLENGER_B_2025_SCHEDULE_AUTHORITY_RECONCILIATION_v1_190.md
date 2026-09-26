# CFB Engine — Challenger B 2025 Schedule Authority Reconciliation v1.190

Status: **BLOCKED — v1.186 ACCEPTANCE COUNTS DO NOT MATCH PINNED ARTIFACT**
Parent: v1.189 implementation / v1.188 execution attempt
Supersedes for 2025 schedule-count authority: v1.186 PASS claim pending correction
Production v1 remains champion/fallback.

## Trigger

The v1.188 prospective prediction producer correctly failed closed when the schedule file downloaded from the exact artifact pinned by v1.186 did not satisfy the v1.186 frozen 880-game identity.

Observed from run 36214302458:
- file columns exactly match the outcome-blind projection schema;
- rows: 934;
- unique game IDs: 934;
- producer stopped before feature construction or prediction scoring.

## Independent artifact readback

Artifact 10893997859 was downloaded independently and its ZIP digest remains the v1.186-pinned digest:

`sha256:e6d8b794dda56535fcabe4c479444c600325fedb00e0186afe0a031f7a74263a`

Its embedded `manifest.json` reports for 2025:
- qualified_rows: **934**
- FBS-vs-FBS: **808**
- FBS-vs-non-FBS: **126**
- regular: **879**
- conference championship: **9**
- postseason: **46**
- neutral: **64**
- projection SHA-256: `289b72810b0c1ebcf0426b9b869d37f46601c40f9f2028d58e79bfa96616ee34`

The contained `challenger_b_schedule_2025_v1_157.csv` independently reads as 934 rows with 934 unique game IDs and reproduces those class counts.

## Contradiction

v1.186 states that the same run/artifact contains:
- 880 qualified games;
- 770 FBS-vs-FBS;
- 110 FBS-vs-non-FBS;
- 839 regular;
- 10 conference championship;
- 31 postseason;
- 54 neutral.

Those claims cannot be accepted as artifact-backed because the exact pinned artifact reports different values.

## Fail-closed effect

1. v1.186 is reclassified from PASS to **BLOCKED / EVIDENCE-CONTRADICTED** for 2025 schedule-count and keyset authority.
2. v1.187 procedure remains conceptually frozen, but its exact 880-game target-key dependency is unresolved and MUST NOT be executed by substituting the 934-game artifact.
3. v1.188 producer remains unaccepted. Its failure is a successful authority guard, not permission to relax the guard.
4. v1.189 independent acceptance cannot run until a corrected, artifact-backed 2025 target keyset is frozen.
5. No 2025 target outcomes may be joined, inspected for model correction, or scored.
6. No market data, refit, recalibration, redesign, or promotion is authorized.

## Required recovery

Reconstruct the intended full-relevant-FBS 2025 population from the authoritative membership/population semantics and source lineage, determine why v1.186 recorded 880 while the pinned artifact contains 934, then freeze a corrected outcome-blind projection with:
- exact keyset;
- independently reproduced counts;
- raw-source and projection hashes;
- explicit reconciliation against both the 934-row artifact and the erroneous v1.186 statement.

Only after that corrected projection is independently accepted may prospective feature/prediction execution resume.

## Outcome boundary

2025 outcomes remain sealed. This reconciliation does not authorize TEST opening or scoring.
