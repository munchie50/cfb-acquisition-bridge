# CFB Engine — Challenger B Corrected Feature Execution Preflight v1.161

Status: FROZEN WHILE v1.160 EQUIVALENCE RUNS / NO CORRECTED FEATURE EXECUTION YET
Parent: v1.159

## Dependency gate
Corrected-population feature execution is prohibited unless v1.160 independently reproduces all four accepted v1.109/v1.115 artifacts on the original v1.108 schedule at identical key sets and numerical values (1e-12 tolerance for serialization/runtime floating representation).

## Corrected execution after PASS
The first corrected 2016-2024 run must be diagnostic-only and must report, before any dataset/model fitting:
- target games by season from v1.157;
- target team-sides expected vs materialized;
- missing PBP/primitives by game and population class;
- complete feature rows by game and population class;
- opening/no-prior rows separately from missing-input rows;
- exact coverage of the 1,342 v1.158 newly admitted games;
- no 2025 access.

A corrected target game is not silently removed merely because its own PBP is unavailable. It remains in the eligibility ledger and fails closed where required inputs cannot be qualified.

## Chronology
The corrected producer must use explicit strict inequality source kickoff < target kickoff for every contributing same-season prior game. Equal timestamps are excluded/fail-closed and ledgered. Game-ID ordering may never break a timestamp tie for feature availability.

## Performance firewall
No targets/model fitting/2023-2024 corrected performance may be computed by this diagnostic run. This gate evaluates feature availability and semantic equivalence only.

Locks unchanged: no fitting, no scoring, 2025 protected, no market join.
