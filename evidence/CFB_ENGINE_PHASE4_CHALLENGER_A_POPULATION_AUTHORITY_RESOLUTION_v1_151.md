# CFB Engine — Challenger-A Population Authority Resolution v1.151

Status: DEFECT CONFIRMED AS IMPLEMENTATION INCOMPLETENESS / NO LEGITIMATE NARROWING RECOVERED
Parent: v1.150

## Authority trace
Current frozen v1.124 was read back directly. It explicitly defines one canonical scheduled game with at least one FBS participant in the relevant-FBS universe and includes FBS-vs-FCS, conference championships, bowls and CFP/postseason when qualified.

The higher historical authority recovered by v1.105 states the engine mission covers the full relevant FBS slate and that the frozen Phase-4 methodology/inventory/contracts govern the redesign. Current Library/package indexes confirm the authentic frozen Phase-4 evaluation methodology, redesign contract and feature/data inventory are the governing ancestry.

No later pre-performance contract or freeze was recovered that narrows Challenger-A from v1.124's relevant-FBS population to regular FBS-vs-FBS only.

## Implementation trace
The schedule input added at v1.108, blob e8d96b9135f625a868cc613e124545ac51828e54, was inherited from legacy v0.22 population-ledger/primitive-coverage work:
- 2016 explicitly PROVISIONAL_FBS_VS_FBS;
- 2017-2024 PRIMARY_REGULAR_PROVISIONAL plus conference-championship-pending rows in 2022-2024;
- no represented FBS-vs-FCS/bowl/CFP classes required by v1.124.

Thus v1.108 supplied a provenance-qualified schedule subset but was not population-conformant for the subsequently frozen v1.124 Challenger-A target population. v1.131 then consumed that subset without a contract-vs-membership conformance gate.

## Resolution
Classify option A from v1.150:
- v1.124 is the governing intended Challenger-A population.
- v1.108/v1.131 implementation was incomplete at population scope.
- v1.140 is preserved and reclassified as **Challenger-A legacy-scope execution evidence**, not full Challenger-A acceptance.
- v1.140's numerical results remain historical evidence for the exact executed subset and must not be discarded or rewritten.
- 2023-2024 remains exposed/spent for that candidate lineage.

No authority supports rewriting v1.124 to fit the executed subset.

## Forward path
Do not open 2025 under either the legacy subset or a TEST-only broadened population.

Create a prospectively named corrected challenger lineage (Challenger B or equivalent) that:
1. implements v1.124 population semantics across TRAIN/VALIDATION/TEST consistently;
2. preserves Challenger-A feature/model decisions as historical prior choices unless a separately prospectively justified change is made;
3. treats 2023-2024 as non-fresh evidence for any choices inherited because those results are already known;
4. defines an honest evidence strategy before fitting the corrected population;
5. leaves 2025 untouched until corrected candidate predictions are frozen under a new gate.

## Acceptance correction
Any current-state/handoff wording that says v1.140 is full Challenger-A BOUNDED PASS must be interpreted through v1.150-v1.151: the pass is bounded to the executed legacy population only.

## Core learning installation
Future dataset acceptance must include a machine-checkable **population-contract conformance gate**:
- enumerate required inclusion classes from the active contract;
- enumerate actual schedule membership/scope classes;
- prove required classes are represented or explicitly fail closed;
- never accept aggregate row-count/hash equality as population-semantic proof.

This control is mandatory for the corrected challenger before fitting.

Locks: production v1 unchanged; Challenger A not promoted; 2025 unscored; no market join; no production promotion.
