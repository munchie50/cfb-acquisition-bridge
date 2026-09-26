# CFB Engine — Challenger B 2026 Rolling Live-Shadow Lineage Contract v1.216

Status: **PROSPECTIVELY FROZEN — DUPLICATE-TARGET LINEAGE DEFINED BEFORE SECOND SNAPSHOT**
Parents: v1.143, v1.202, v1.208, v1.215
Production v1 remains champion/fallback.

## Purpose
The first accepted live-shadow freeze v1.208 covers all 622 games that were future at its cutoff. Later source snapshots can contain fresher completed-game information for games that are still future. This contract defines how repeated pregame predictions for the same target are preserved and evaluated before any second snapshot is created.

## Lineage rule
For each target game:
1. **FIRST_FROZEN** is the earliest independently accepted fair prediction frozen before target kickoff.
2. FIRST_FROZEN is immutable and remains the primary prospective evidence record for that target.
3. A later prediction for the same target may be created only at a later cutoff still strictly before kickoff and is classified **REFRESH_SNAPSHOT**.
4. REFRESH_SNAPSHOT never overwrites, replaces, edits, or backfills FIRST_FROZEN.
5. Every snapshot must retain its own cutoff, source hashes, chronology, eligibility/exclusion state, feature values, prediction values, output hashes, and parent lineage.
6. A target excluded at an earlier snapshot may become eligible at a later snapshot if newly available pre-cutoff source information satisfies the unchanged rules. This creates a REFRESH_SNAPSHOT prediction only; it does not alter the earlier exclusion.
7. A target predicted earlier may become excluded later because of source/completeness conditions; both records remain preserved.
8. No snapshot may use target own outcome/PBP, information unavailable by its execution cutoff, market data, or later-game information.

## Evaluation rule
- Primary prospective model evaluation uses FIRST_FROZEN only, one record per target.
- REFRESH_SNAPSHOT performance is reported separately as a time/recency diagnostic.
- Do not select a better-looking snapshot after outcomes are known.
- Any direct first-vs-refresh comparison must use the predeclared common target set where both snapshots produced eligible predictions.
- Outcomes do not authorize feature/model/calibration/threshold redesign.
- Market, execution, and betting-result evaluation remain separate.

## Cadence
Use a **weekly rolling snapshot** during the active 2026 season, unless an operational/source failure requires a separately documented exception.
- Capture a new immutable UTC cutoff.
- Requalify exact current schedule/PBP source bytes and hashes.
- Target only games strictly after the new cutoff.
- Preserve all prior snapshot artifacts.
- Do not rerun merely because an upstream source changed within the same weekly cycle.
- If a weekly snapshot fails, repair only the failed snapshot machinery; never mutate prior accepted snapshots.

This cadence is operational, not performance-selected. It may be changed prospectively by a later contract, never retroactively.

## Second-snapshot boundary
A second snapshot may proceed only with:
- current source preflight and frozen hashes;
- unchanged v1.193 model identity;
- unchanged v1.172 feature semantics;
- unchanged relevant-FBS population authority unless separately corrected prospectively;
- explicit snapshot/lineage labels in outputs;
- independent acceptance before treating the refresh as accepted prospective evidence.

No promotion, refit, recalibration, market join, or production change is authorized.
