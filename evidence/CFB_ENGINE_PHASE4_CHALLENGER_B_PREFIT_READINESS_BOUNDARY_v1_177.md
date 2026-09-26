# CFB Engine — Challenger B Pre-Fitting Readiness Boundary v1.177

Status: **PREFIT READINESS AUDIT COMPLETE / FITTING NOT AUTHORIZED**
Parent current recovery: v1.176
Substantive feature parent: v1.173
No model fitting, scoring, 2025 access, or market join occurred.

## Purpose
Identify what can safely carry forward from Challenger A and what must be prospectively re-frozen for corrected-population Challenger B before any model performance is exposed.

## Reusable frozen modeling mechanics
The following Challenger-A mechanics are technically reusable only if a future Challenger-B prospective contract explicitly adopts them before performance:
- transparent ridge linear/logistic family;
- TRAIN-only centering/scaling;
- forward-chain season ordering;
- frozen lambda-grid concept;
- complete-case/no model-stage imputation;
- market-blind inputs;
- raw logistic probabilities before any separately governed calibration;
- independent artifact/readback acceptance rather than green-run acceptance.

This checkpoint does **not** silently adopt those choices for Challenger B.

## Challenger-A implementation that MUST NOT be reused as-is
`scripts/phase4_challenger_a_dataset_freeze_v1_131.py` is population-specific:
- reads old v1.109/v1.115 accepted feature artifacts;
- embeds the old 42-game / 43-team-side v1.128 temporal exclusion set;
- binds Challenger-A v1.123-v1.130 authority;
- builds only the old accepted Challenger-A population.

`.github/workflows/phase4_challenger_a_dataset_freeze_v1_131.yml` explicitly downloads old feature artifacts 10890704969 and 10891634424.

Therefore Challenger B requires a new dataset-freeze producer/workflow bound to accepted corrected feature artifact:
- v1.172 run 36211493651
- artifact 10895523493
- digest sha256:702930b2ba905c9f917acbc627d12342e8190cfb44a4c8afd1aee49fbf59e239

The old v1.128 42-game exclusion set must not be copied forward automatically. Corrected v1.172 strict-prior chronology is the relevant feature-history authority; any game-level exclusion still required must be re-derived from current corrected inputs and frozen prospectively.

## Decisions still required before a Challenger-B dataset freeze
Before constructing a fit-eligible B dataset/config, freeze prospectively:
1. exact Challenger-B feature column family and whether it is intentionally identical to the accepted v1.123 17 numeric team features;
2. game-level representation (for example, whether v1.130 side-preserving home/away copies are explicitly adopted unchanged);
3. exact target construction and qualified schedule source;
4. complete row eligibility/exclusion rules for the 7,701-game corrected universe, including treatment of the 45 own-game PBP-missing population members and history-incomplete rows;
5. TRAIN/VALIDATION season partitions and evidence-spending consequences;
6. model family, penalty grid, selection metric, scaling, venue encoding and numerical convention;
7. required stability slices under corrected population metadata;
8. exact 2025 hard-exclusion and market-blind assertions;
9. independent dataset acceptance criteria before fitting authorization.

These are decision-before-evidence controls. They must not be chosen after viewing Challenger-B TRAIN/VALIDATION performance.

## Expected execution order
1. freeze Challenger-B modeling/evaluation contract;
2. freeze game-level representation and numerical convention;
3. build new corrected-population dataset-freeze producer/workflow from accepted v1.172 artifact and qualified historical schedule authority;
4. execute dataset freeze only;
5. independently audit population, chronology-derived eligibility, targets, missingness, 2025 absence, market blindness, hashes and exclusions;
6. persist/read back dataset acceptance;
7. reconcile pre-fitting gate;
8. only then obtain/record explicit Challenger-B fitting authorization;
9. fit/evaluate under the frozen contract.

## Current gate
**BLOCKED BY PROSPECTIVE CONTRACT + DATASET FREEZE, NOT BY FEATURE REBUILD.**

The corrected historical feature substrate is accepted. There is no authorization to fit Challenger B yet, and no fit implementation should be created in a way that can accidentally execute before the prospective contract/dataset gates close.

Locks unchanged: production v1 champion/fallback; 2025 TEST protected; no market join; no Challenger-B fitting/scoring; no production promotion.
