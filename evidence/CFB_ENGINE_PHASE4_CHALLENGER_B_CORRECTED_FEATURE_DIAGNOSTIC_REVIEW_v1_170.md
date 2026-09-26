# CFB Engine Phase 4 Challenger B Corrected Feature Diagnostic Review v1.170

Status: **BOUNDED DIAGNOSTIC PASS — NOT YET ACCEPTED**

## Execution authority
- Workflow run: 36210947192
- Head commit: 227d1940970ddff4785986232af8312b254f52be
- Artifact id: 10895472735
- Artifact digest: sha256:b66350cb4ddf1e4cca2ff9b0771bfee86796f442ffc3845620584e53249f4bed
- Note: workflow artifact container is incorrectly named `cfb-phase4-challenger-b-corrected-features-v1-169`; contained files and manifest are v1.170. Naming defect does not promote or invalidate contained evidence but must be corrected for future recovery clarity.

## Independently reconciled results
- Exact target population: 7,701 games / 15,402 team-sides.
- Zero duplicate season/game/team target keys.
- Seasons are 2016–2024 only.
- Exact v1.158 newly admitted population: 1,342 games.
- Exact authoritative game-level PBP absence: 45 games / 90 team-sides.
- PBP-present but mechanical primitive-unmaterialized: exactly 10 team-sides / 10 games, all the previously isolated Savannah State / Saint Francis FBS-vs-non-FBS identities.
- Opening/no-prior team-sides: 1,922.
- Mechanical history incomplete: 287 team-sides.
- Derived history incomplete: 287 team-sides.
- No row with a positive missing-prior mechanical source count is marked mechanical-history complete; inverse also holds.
- No row with a positive missing-prior derived source count is marked derived-history complete; inverse also holds.
- Mechanical and derived feature tables each preserve all 15,402 target rows with zero duplicate target keys.
- Manifest reports 2025_accessed=false and fit_or_score=false.

## What v1.170 proves
v1.170 fixes the v1.169 source-qualification defect: authoritative game-level PBP availability is attached to schedule-first target rows, and cumulative PBP-derived history fails closed on either missing game-level PBP or unavailable required team-side primitives. The 45-game PBP gap is no longer conflated with the 10 PBP-present identity/materialization cases.

## Remaining acceptance blockers
1. Reconcile the 10 PBP-present Savannah State / Saint Francis team identities against raw PBP `pos_team` / `def_pos_team` labels. Do not introduce speculative aliases or synthetic zero primitives.
2. Independently compare derived primitive materialization semantics with frozen v1.115, especially legitimate zero-event aggregates versus truly unavailable primitives.
3. Explicitly prove strict source kickoff < target kickoff / target-game exclusion from contributing source sets in the independent acceptance audit.
4. Correct the workflow artifact-name typo for recovery clarity before a successor accepted package.

No Challenger-B fitting, 2025 scoring/access, market join, or production promotion is authorized by this review.
