# CFB Engine — Challenger B Fit Authority Reconciliation v1.192

Status: **BLOCKED — v1.184 ACCEPTANCE RECORD CONTRADICTS ITS PINNED v1.183 RUN/ARTIFACT**
Parents: v1.183, v1.184, v1.191
Production v1 remains champion/fallback. 2025 outcomes remain sealed.

## Trigger

The v1.188 prospective producer passed schedule/population and chronology-safe feature construction far enough to reach the frozen coefficient gate, then failed closed with `coefficient identity`.

The failure was traced to the exact v1.183 artifact pinned by v1.184:
- run: 36212803830
- artifact: 10895838069
- artifact ZIP digest: `sha256:3a2cabfcd37e0bcf0cae85efc77eaa6755ffb12734d1e48c4c582ed1de375587`

## Exact run/artifact readback

The v1.183 workflow log itself reports:
- TRAIN rows: **4,700**
- spent/corroborative rows: **1,546**
- selected lambda margin: **0.1**
- selected lambda total: **0.1**
- selected lambda win: **0.01**

The downloaded immutable artifact independently reproduces the same values in `summary.json` and `selected_coefficients.csv`.

The artifact manifest hashes:
- `selected_coefficients.csv`: `bf15ce41180bfb4e250d311df279e98c13b65432756ae07f7a30264cbae0e221`
- `train_scaling.csv`: `68fb5193ccb8828ac8d34dfe820101181c2bde078a04a6d5afd4c08bcf0cab45`

The v1.183 implementation selects the minimum forward-chain mean score under the frozen 12-decimal / larger-lambda tie rule, and the persisted grid supports the artifact's selected lambdas.

## Contradiction

v1.184 claims that the same run/artifact contains:
- TRAIN rows: 4,806
- spent/corroborative rows: 1,440
- lambdas margin 10 / total 100 / win 10
- materially different spent/corroborative metrics.

Those statements do not match the exact run log or immutable artifact they cite.

## Fail-closed effect

1. v1.184 is reclassified as **EVIDENCE-CONTRADICTED** for fit row counts, selected lambdas, and corroborative metrics.
2. v1.185/v1.187 downstream references to 10/100/10 are not valid frozen-model identity until this contradiction is resolved.
3. v1.188 remains unaccepted; its coefficient-identity stop is correct and MUST NOT be bypassed by choosing either lambda set ad hoc.
4. v1.189 acceptance is blocked until one authoritative fit identity is frozen from reproducible evidence.
5. No 2025 outcome opening/scoring, market join, refit, recalibration, redesign, or promotion is authorized.

## Required recovery

Reconcile the accepted v1.179 dataset artifact, v1.183 implementation/run, and v1.184 written acceptance. Determine whether:
- the pinned v1.183 artifact is the intended frozen Challenger-B fit and v1.184 was transcribed from a different/non-authoritative execution; or
- a different artifact/run was intended and must be identified and independently reproduced.

The resolution must freeze exact dataset identity, row counts, scaling hash, coefficient hash, selected lambdas, and fit artifact digest before 2025 prospective prediction execution resumes.
