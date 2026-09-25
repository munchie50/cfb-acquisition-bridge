# CFB Engine — Phase 4 Pre-Fitting Readiness Gate v1.121

Status: ACTIVE GATE — BLOCKS FIRST V2 FITTING UNTIL ALL BLOCKERS ARE CLOSED
Scope: challenger/shadow v2 only
Production v1: untouched champion/fallback
2025 TEST: protected; no model-performance exposure
Parent authorities: frozen Phase 4 contracts; routine v5; v1.105–v1.120

## Purpose

Create one authoritative control surface between validated feature construction and first model fitting. This gate references existing proof instead of duplicating it.

Decision-before-evidence rule for this gate:
If seeing TRAIN/VALIDATION model performance could reasonably influence a modeling decision, freeze that decision or the allowed decision/search space before examining that performance.

This is a Phase 4 pre-fitting governance rule. It does not silently modify production routine v5; any proposed master-routine adoption must first enter the v6 candidate/test lane.

## Readiness matrix

| Workstream | Requirement | Existing authority/evidence | Status | Blocks fitting? | Exact next action / completion evidence |
|---|---|---|---|---|---|
| Historical semantic integrity | 2016–2026 engine-relevant rules/statistical regimes mapped | v1.116 gate; v1.117 ledger; v1.120 OT bounded audit | ACTION REQUIRED BEFORE FITTING | YES | Complete targeted 2016, 2017, 2020, 2022, 2026 primary-source reviews; close remaining 2018 field-position compatibility interpretation; preserve 2023/2024 environment regimes |
| Historical semantic integrity | 2021+ third-and-later OT conversions excluded from scrimmage denominators | v1.119/v1.120 | PASS — BOUNDED | NO | Reopen only on contradictory evidence |
| Feature semantic integrity | Mechanical initial feature canary | v1.107/v1.110 | PASS — BOUNDED | NO | Do not reopen absent contradictory evidence |
| Feature semantic integrity | Explosiveness/success/field-position derived canary | v1.112–v1.120 | PASS — BOUNDED | NO | Do not reopen absent contradictory evidence |
| Feature semantic integrity | Finishing-drives numeric points attribution | v1.113/v1.114 | ACTION REQUIRED BEFORE FITTING only if feature remains in first fitted challenger | CONDITIONAL YES | Recover authentic drive-point semantics or explicitly exclude feature from first challenger before performance |
| Feature semantic integrity | Combined raw turnover/giveaway rate | V36/v1.78–v1.87 | ACTION REQUIRED BEFORE FITTING only if feature remains in first fitted challenger | CONDITIONAL YES | Either close semantics or prospectively exclude combined turnover feature; interception rate remains separately defined |
| Feature semantic integrity | Opponent adjustment/SOS | v1.77 second-order lineage boundary | ACTION REQUIRED BEFORE FITTING if included | CONDITIONAL YES | Recover authentic formula/producer or prospectively exclude from first challenger; do not invent formula |
| Feature semantic integrity | Special-play eligibility incl. kneels/spikes/OT | frozen contracts + v1.120 OT evidence | ACTION REQUIRED BEFORE FITTING | YES | Freeze feature-specific treatment prospectively; do not apply one universal filter without evidence |
| Feature semantic integrity | Garbage-time treatment | not yet frozen | ACTION REQUIRED BEFORE FITTING | YES | Prospectively freeze treatment/search space before performance; default must not be selected from validation results |
| Feature semantic integrity | Missingness semantics | v1.107/v1.112 define NA/affected-observation exclusion for current features | PARTIAL | YES | Consolidate feature-level missingness policy for exact first-challenger feature set |
| Feature semantic integrity | Early-season / preseason prior behavior | frozen methodology: no preseason prior in first no-prior canary | PARTIAL | YES | Freeze first-challenger early-season policy; any prior/shrinkage requires separate prospective definition/leakage test |
| Target & population | Exact prediction target(s) and overtime treatment | master/Phase 4 objective identifies fair spread/total/win probability; exact first-fit target not yet frozen here | ACTION REQUIRED BEFORE FITTING | YES | Freeze exact first-challenger target and OT treatment |
| Target & population | Game population: FBS/FCS, bowls/CFP/championships, forfeits/cancellations | qualified schedule evidence exists; exact first-fit population contract not consolidated | ACTION REQUIRED BEFORE FITTING | YES | Freeze included/excluded game classes and sample weighting |
| Temporal integrity | Prediction-time qualification | v1.52–v1.54/v1.76; authoritative cutoff absent for bounded rows | ACTION REQUIRED / FAIL-CLOSED | YES | Define first-fit population so every included feature row has acceptable point-in-time qualification; do not substitute schedule kickoff for missing authoritative cutoff |
| Modeling/validation | Allowed model families/transforms/interactions/hyperparameter search | not yet frozen for first challenger | ACTION REQUIRED BEFORE FITTING | YES | Freeze allowed search space before seeing performance |
| Modeling/validation | Forward-chaining partitions | frozen: TRAIN 2016–2022; VALIDATION 2023–2024; TEST 2025 | PASS | NO | Preserve exactly |
| Modeling/validation | Metrics/model-selection/calibration/uncertainty/negative controls | methodology partially defines forward validation; exact first-fit selection contract not yet consolidated | ACTION REQUIRED BEFORE FITTING | YES | Freeze evaluation and selection rules before first fit |
| Reproducibility/governance | Market-blind fair-model separation | frozen Phase 4 redesign contract | PASS / VERIFY AT FIT | NO now | Final leakage/market-blind audit on frozen first-fit dataset/config |
| Reproducibility/governance | Exact dataset/code/config identity | canary artifacts hashed; first-fit package not yet frozen | ACTION REQUIRED BEFORE FITTING | YES | Freeze hashes/config/environment immediately before execution |
| Reproducibility/governance | Champion/challenger, rollback, production promotion | existing governance: production v1 champion/fallback; v2 shadow; explicit promotion authorization required | PASS | NO | Preserve; no redesign |
| Protected test | 2025 untouched until candidate freeze | repeated workflow assertions and contracts | PASS TO DATE | YES if violated | Continue zero TEST performance exposure |

## Current blocker set

The first fitted challenger is NOT authorized yet. Actual blockers are:
1. finish historical rules/statistical-semantics compatibility review;
2. freeze special-play and garbage-time treatment for the exact first-challenger features;
3. consolidate missingness and early-season behavior;
4. freeze exact first-fit target and game population;
5. resolve prediction-time qualification by exclusion/fail-closed policy for rows/features lacking authoritative cutoff;
6. prospectively decide whether finishing drives, combined turnover rate, and opponent adjustment/SOS are excluded or must be resolved before first fit;
7. freeze modeling/search/evaluation/calibration rules;
8. freeze exact first-fit dataset/code/config and run final market-blind/leakage audit.

## Dependency order

A. Historical semantics + feature eligibility
B. Exact first-challenger feature set (including explicit exclusions)
C. Target/population/temporal qualification
D. Modeling and evaluation contract
E. Frozen dataset/code/config + final leakage audit
F. Only then request/confirm fitting authorization under existing governance

## Non-actions

- Do not reopen v1.110 or v1.120 without contradictory evidence.
- Do not invent opponent-adjustment lineage.
- Do not force finishing drives or combined turnover into the first challenger merely because they were in an aspirational inventory.
- Do not use validation performance to choose definitions that should have been frozen prospectively.
- Do not inspect 2025 model performance.
- Do not fit or tune from this checkpoint.

## Routine observation

The decision-before-evidence principle is useful beyond Phase 4, but production routine v5 is unchanged. Record this as a candidate v6 procedural observation for later controlled evaluation rather than silently promoting it now.
