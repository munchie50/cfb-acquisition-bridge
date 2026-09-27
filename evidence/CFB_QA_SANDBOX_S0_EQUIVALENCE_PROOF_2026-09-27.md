# CFB QA Sandbox S0 Equivalence Proof — 2026-09-27

Status: PASS — S0 CONTROL REPRODUCED / S1-S2 MAY PROCEED
Parent: CFB_QA_SANDBOX_EXECUTION_AUTHORIZATION_2026-09-27
Production effect: NONE

## Artifact identity
Recovered accepted v1.179 dataset artifact ZIP SHA256:
8eeb67f5da87df4a75f2f785838553679928e370eefeea3945f2b2e688e69780

Recovered accepted v1.172 feature substrate ZIP SHA256:
702930b2ba905c9f917acbc627d12342e8190cfb44a4c8afd1aee49fbf59e239

Recovered frozen v1.183 fit artifact ZIP SHA256:
3a2cabfcd37e0bcf0cae85efc77eaa6755ffb12734d1e48c4c582ed1de375587

Frozen coefficient SHA256:
bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221

Frozen scaling SHA256:
68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45

## Population
Accepted model rows: 6,246.
TRAIN 2016-2022: 4,700.
SPENT/CORROBORATIVE 2023-2024: 1,546.
2025 rows accessed: 0.
Numeric predictors: 34.

## S0 replay
The frozen v1.193/v1.183 coefficients and persisted TRAIN scaling were replayed against the accepted 2023-2024 matrix.

Row identity: PASS, 1,546/1,546 unique rows joined one-to-one.

Maximum absolute replay-versus-persisted prediction difference:
- margin: 2.1316282072803006e-14 points
- total: 2.842170943040401e-14 points
- win probability: 4.996003610813204e-16

These are floating-point representation noise and establish numerical equivalence.

Persisted scaling versus direct TRAIN recomputation:
- maximum mean difference: 3.552713678800501e-15
- maximum population-SD difference: 9.71445146547012e-17

## Gate result
S0 EQUIVALENCE PASS.
The Sandbox control is the accepted Champion lineage rather than a reconstructed approximation. S1/S2 construction may proceed under the frozen Sandbox contract.

This does not authorize Champion mutation, 2025 access, market inputs, user-wager inputs, production changes, or promotion.

Scientific effect: none.
