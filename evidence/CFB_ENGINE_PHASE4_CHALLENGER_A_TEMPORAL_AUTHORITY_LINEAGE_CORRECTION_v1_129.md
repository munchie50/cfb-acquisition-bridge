# CFB Engine — Phase 4 Challenger-A Temporal Authority / Lineage Correction v1.129

Status: CORRECTION / AUTHORITATIVE LINEAGE RECONCILIATION
Scope: Challenger A / v2 shadow only
Production effect: NONE
2025 TEST: PROTECTED / UNTOUCHED
Fitting: NOT AUTHORIZED
Current parent: v1.128

## Finding

A routine persistence/readback audit found that the previously reported v1.125 temporal-qualification commit identity (53e15965f3b3101f4bcedd03b84a1a40ee01c2c4) does not resolve in the repository, no default-branch file named CFB_ENGINE_PHASE4_CHALLENGER_A_TEMPORAL_QUALIFICATION_CONTRACT_v1_125.md exists, and repository history for that path is empty.

Therefore v1.125 must NOT be treated as persisted authority.

v1.124 is authentic and verified at commit 2fe92c271af7ed1e7aeeea6bcad67bdc0427ff90, blob e17c6ac9d36fcaf681cd5ccd0258c9f35a2dd414.

v1.126 is authentic at commit b24fe34c8550f9ea7e66d5ed60bc223edf2b05d2, blob 54206c0452e1c5ed2978cc64f5ef21c799a03c68, and its actual Git parent is v1.124. Its prose reference to v1.125 is a stale/non-persisted dependency reference, not proof that v1.125 existed.

## Correct temporal authority

For Challenger A, the persisted temporal population authority is now:

1. bounded historical evidence v1.24/v1.25/v1.52-v1.54/v1.76;
2. v1.127 conservative 2022 temporal exclusion contract, commit f0c11ef951a9366c848018052177369f37d48a60, blob 084f2e159c1aac3654c2f8706d957600adb8cc6d;
3. v1.128 execution proof, commit 093535b741d8ee4c6ad445314b1e6d3015a6247c, blob 1701a3c3399113c1bdf5dc4bf8457f2218dbd493.

v1.127/v1.128 reproduce the exact bounded 43 team-side propagation count and convert it to 42 unique game-level exclusions without inventing a prediction cutoff.

## Effect on v1.126

Do not rewrite the frozen v1.126 artifact. Interpret every v1.126 dependency on “rows qualified by v1.124/v1.125” as:

- population/target qualification under verified v1.124; and
- temporal fail-closed qualification under the surviving historical evidence plus v1.127/v1.128.

All other v1.126 prospective model/evaluation decisions remain frozen unchanged.

## Routine lesson

A reported commit/hash is not persistence proof until the object is independently resolvable and its ancestry/path is verified. Parent references inside a later artifact do not establish that a missing checkpoint existed.

This is an instance of the production-v5 persistence/readback rule and should be retained for future routine consolidation.

## Gate effect

The missing-v1.125 lineage defect is CLOSED by explicit correction rather than reconstruction.

Remaining before fitting:
1. freeze exact game-level predictor representation;
2. build the exact schedule-authoritative game-level dataset;
3. apply v1.128's 42 unique game exclusions plus complete-input fail-closed rules;
4. run final 2025/market-blind/leakage and population audits;
5. persist/read back dataset/code/config identities and hashes;
6. final pre-fitting readiness reconciliation and required fitting authorization.

No fitting is authorized by this correction.
