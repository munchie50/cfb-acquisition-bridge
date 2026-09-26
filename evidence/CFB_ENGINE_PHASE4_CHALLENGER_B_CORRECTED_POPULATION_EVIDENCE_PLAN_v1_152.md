# CFB Engine — Corrected Population Challenger Evidence Plan v1.152

Status: PROSPECTIVE GOVERNANCE FREEZE / NO FITTING AUTHORIZED
Parent: v1.151
Working identity: Challenger B (corrected-population descendant)

## Why a new lineage is required
Challenger A's 2023-2024 results were exposed on a legacy FBS-vs-FBS-centered subset that does not conform to frozen v1.124 population semantics. Correcting the population is material and cannot be silently folded into the already-exposed candidate.

## Fixed inheritance
Unless a later prospectively justified contract says otherwise, Challenger B inherits the football-model choices frozen before Challenger-A performance:
- v1.123 feature/play definitions;
- v1.124 targets and relevant-FBS population semantics;
- v1.126 transparent ridge/GLM model family, transformations, lambda grid and metrics;
- v1.127-v1.129 conservative 2022 temporal exclusions;
- v1.130 side-preserving game representation;
- v1.135 numerical conventions.

This plan does not authorize changing those choices because of observed Challenger-A validation results.

## Corrected population requirement
Build one authoritative schedule universe for 2016-2025 satisfying v1.124:
- at least one FBS participant in the frozen relevant-FBS universe;
- FBS-vs-FBS and qualified FBS-vs-FCS;
- regular season, conference championships, bowls and CFP/postseason;
- canonical home/away and neutral-site metadata;
- cancelled/unplayed/identity-conflicted rows fail closed as specified.

The same population rule must apply across TRAIN 2016-2022, VALIDATION 2023-2024 and protected TEST 2025.

## Evidence independence
2023-2024 outcomes are already known from Challenger A. Therefore:
- they may be used to measure the corrected inherited candidate only as **spent/corroborative validation**, not fresh evidence for redesign or selection;
- no feature/model/lambda/calibration/population rule may be selected from corrected 2023-2024 performance;
- selected Challenger-A lambdas may be inherited as frozen candidate parameters, OR lambda selection may be rerun using TRAIN-only forward chains exactly under v1.126; the choice between those two must be frozen before corrected validation performance is exposed;
- 2025 remains the untouched holdout capable of supplying fresh candidate evidence only after full prediction freeze and separate authorization.

## Required gates before any corrected fit/evaluation
1. population source/provenance contract;
2. machine-checkable population-contract conformance audit;
3. corrected schedule freeze/hash for 2016-2024 with 2025 separately outcome-blind;
4. feature-availability and chronology audit across newly included classes;
5. exact candidate-parameter rule (inherit selected lambdas vs TRAIN-only reselection) frozen;
6. deterministic corrected dataset build;
7. independent leakage audit and persistence/readback;
8. explicit fitting/evaluation authorization.

No corrected 2023-2024 performance may be viewed before gates 1-7 are frozen.

## Immediate next dependency
Recover or construct the full relevant-FBS schedule population using the same source lineage where possible, beginning with a source/population membership contract and class counts. Do not fit or score.

Locks: production v1 champion; Challenger A historical legacy-scope evidence; Challenger B prospective only; 2025 protected; no market join; no promotion.
