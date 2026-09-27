# CFB QA Sandbox — S2 Cardinality Reconciliation — 2026-09-27

Status: DIAGNOSTIC FAIL — PRE-EXECUTION 12-SIDE / 11-GAME CARDINALITY PROOF IS INCOMPLETE
Production effect: NONE
Champion effect: NONE
Outcome access: NONE
2025 access: NONE

## Purpose
Reconcile the live Sandbox generator failure `non-finite S1 input` against the frozen S1/S2 transform, v1.172 completeness authority, completion-safe UTC-date population cutoff, and the pre-execution S2 fail-closed cardinality proof.

## Authoritative inputs
- v1.172 artifact 10895523493, digest sha256:702930b2ba905c9f917acbc627d12342e8190cfb44a4c8afd1aee49fbf59e239
- v1.179 artifact 10896565577, digest sha256:8eeb67f5da87df4a75f2f785838553679928e370eefeea3945f2b2e688e69780
- frozen S1/S2 transform specification
- frozen completion-safe population chronology
- frozen S2 fail-closed cardinality clarification

No predictions, outcomes, market, wagers, or 2025 TEST records were used.

## Reconciliation rule
For each accepted target side and each qualified prior source game:
1. opponent context must resolve to the opponent pregame row at the source-game key;
2. the paired population baseline must exist under the frozen 00:00 UTC same-date exclusion cutoff;
3. for an opponent with zero qualified prior games, the frozen S1 formula algebraically collapses to the population baseline when that baseline exists, producing a zero opponent residual;
4. for positive-history opponent states, the required paired raw feature must be finite and the accepted v1.172 history-complete state must hold;
5. a target mapped feature requires at least one valid source-game residual; otherwise S2 fails closed.

## Result
The previously frozen eleven affected games are reproduced, but they are not exhaustive.

Reconciled unavailable target sides: **13**.
Reconciled unavailable games: **12**.

The additional missed game is:
- 2016 / 400869117 / California vs San Diego State — affected target side: California.

For California before game 400869117:
- source game 400869090 vs Hawai'i: opponent has zero prior history, but the required completion-safe population baseline does not yet exist at the source-game cutoff, so no valid residual exists;
- source game 400869107 vs San Diego State: opponent has positive prior history but its v1.172 pregame history state is incomplete and required mapped raw features are non-finite, so no valid residual exists.

Therefore California has prior team history but zero valid S2 source residuals under the already-frozen validity rules.

## Effect on prior proof
The pre-execution S2 cardinality proof stating 12 affected sides / 11 games and 44 omitted S2 rows is incomplete.

The reconciliation implies, before any further independent implementation validation:
- S0 rows: 6,246;
- S1 rows: 24,984;
- S2 candidate games potentially available: 6,234 rather than 6,235;
- S2 rows under k={1,2,4,8}: 24,936 rather than 24,940;
- total candidate rows: 56,166 rather than 56,170;
- fail-closed S2 omissions: 48 rather than 44.

These revised counts are diagnostic consequences of the frozen validity rules, not yet an accepted replacement freeze. They MUST NOT be used to score outcomes or silently mutate the experiment contract.

## Governance consequence
Do not stack another exception handler onto the generator.
Do not retain the current zero-history omission patch as settled merely because it avoids the first runtime failure.
First reconcile and explicitly correct the pre-execution cardinality authority and generator implementation so both encode the same frozen S1/S2 semantics. Prediction generation remains blocked until that reconciliation is accepted and read back.

Scientific effect: none.
