# CFB QA Sandbox S2 Fail-Closed Cardinality Correction — 2026-09-27

## Status
SUPERSEDING CORRECTION — enumeration/cardinality only.

This record preserves the original frozen S2 fail-closed rule and supersedes only the earlier pre-execution enumeration that reported 12 affected target sides / 11 unique games.

## Scope
No scientific rule, candidate family, coefficient, scaling input, chronology rule, protected TEST boundary, outcome boundary, Champion state, or promotion state is changed by this correction.

The governing rule remains: S2 uses only valid completion-safe source-game opponent residuals. If either target side has zero valid residuals, S2 is unavailable for that game and fails closed. No S1 relabel, imputation, alternate k, relaxed cutoff, recursive context, outcome information, or later information is permitted.

## Reconciled cardinality
Independent reconciliation against the frozen v1.172 feature/primitives substrate and v1.179 accepted population found:

- accepted target games: 6,246
- affected target sides with zero valid completion-safe S2 context: 13
- unique affected games: 12
- S0 prediction rows: 6,246
- S1 prediction rows: 24,984
- S2 prediction rows: 24,936
- total prediction rows: 56,166
- fail-closed S2 omissions across the four-k grid: 48

The original 11 affected game IDs remain affected:
400935254, 401022521, 401022524, 401112443, 401246425, 401403946, 401403976, 401405073, 401413257, 401415219, 401426543.

The missing twelfth game is:
- season 2016, game_id 400869117 — California vs San Diego State; California target side.

## Missed California case
Before target game 400869117, California had two qualified prior source games.

- Source game 400869090 vs Hawai'i: the source opponent had zero qualified prior games and no reproducible completion-safe population baseline at that source cutoff, so no valid residual is available.
- Source game 400869107 vs San Diego State: the source opponent had positive prior history but the frozen v1.172 source state was history-incomplete and the mapped raw feature values were non-finite, so no valid residual is available.

California therefore has zero valid S2 source residuals and the target game must fail closed for S2 under the already-frozen rule.

## Root cause and classification
The earlier pre-execution cardinality proof was incomplete. It established row/key availability but did not fully prove source-opponent completion-safe feature availability for every mapped residual. The defect is an audit/enumeration weakness, not a change to the frozen S2 method.

The live workflow exposed the missing edge case before any accepted candidate artifact or outcome scoring. No outcome, market, wager, later-game information, or 2025 protected TEST data was used to discover or correct it.

## Implementation reconciliation
Diagnostic reconciliation evidence was persisted in commit aad201dc9fbce5a8c32c16d84c64987d7ebfb73b.

The bounded generator correction was persisted in commit 24c4500e132340dcb640e96526ef562003f0c729.
Corrected generator SHA-256:
f2e0bf46fd40e3d40b7d2ddf318cdf06a597fd22c0b577d572a05377446f6a22

The workflow cardinality expectations were reconciled to 56,166 total rows and 24,936 S2 rows. The 30-minute infrastructure timeout was later extended after a controlled run was cancelled at the execution ceiling; that timeout change did not alter generator bytes or scientific logic.

## Authority effect
The earlier S2 fail-closed cardinality evidence remains preserved as historical evidence but is superseded for its 12-side / 11-game enumeration and derived 56,170 / 24,940 row counts.

This correction is authoritative for those enumeration/cardinality facts. The frozen S2 fail-closed rule itself remains unchanged.

Production effect: NONE.
Champion effect: NONE.
Promotion effect: NONE.
Outcome access: NONE.
2025 protected TEST access: NONE.
