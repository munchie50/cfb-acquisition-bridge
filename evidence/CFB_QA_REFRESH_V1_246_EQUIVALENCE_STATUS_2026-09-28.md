# CFB QA — Refresh v1.246 Equivalence Status — 2026-09-28

Status: **GATE DEFINED / EXECUTION PENDING — DO NOT TREAT AS PASS**

## Purpose
Prove the generalized REFRESH_SNAPSHOT producer preserves v1.206 scientific behavior on the exact accepted first-freeze inputs.

## Exact gate
Workflow: .github/workflows/cfb_qa_refresh_v1_246_equivalence.yml

Immutable replay inputs:
- preflight artifact 10897001956, ZIP SHA-256 4dc70419b9aa3afdfa2570861490598da69b2bccfed878e438dc17b69a9a7ea8;
- fit artifact 10895838069, ZIP SHA-256 3a2cabfcd37e0bcf0cae85efc77eaa6755ffb12734d1e48c4c582ed1de375587;
- schedule SHA-256 5b2ff52996862b06b67309f1ebc27742e55c279ff4785c7a942915cdf820f1b1;
- PBP SHA-256 81e38e7e874d249300bb108de0029a8ffb0b19c31cfea6e7aafab5507115e5da;
- cutoff 2026-09-26T03:47:37.497112+00:00.

Required result:
- old/new scientific CSV columns and values identical within 1e-12 after stripping only snapshot_type and snapshot_cutoff_utc;
- 622 targets, 526 eligible predictions, 96 exclusions;
- REFRESH_SNAPSHOT / v1.216 lineage present in new manifest.

## Current execution state
No workflow run exists. The connected GitHub interface supports workflow inspection/rerun but not first-time workflow_dispatch. A generic REST dispatch attempt was rejected by the connector before GitHub execution.

This is infrastructure availability, not equivalence evidence and not a scientific failure.

## Structural review
The v1.246 source was derived from v1.206 without modifying feature formulas, source/PBP construction, strict-prior selection, model coefficient/scaling identities, prediction equations, or forbidden-field scan. Intended changes are limited to:
- dynamic target cardinality and population-class counts;
- strict future-at-cutoff assertion;
- dynamic team-side/population accounting;
- REFRESH_SNAPSHOT metadata and v1.216 parent lineage;
- refresh-specific output filenames/manifest.

Structural review is weaker than executable equivalence and cannot close the gate.

## Stop rule
Do not build the S2_K1 live companion on v1.246 as accepted substrate until the exact executable equivalence gate passes and is independently read back.


## 2026-09-28 pre-execution implementation defect
WAIT-sweep source readback found two literal backslash-n sequences introduced during v1.246 construction. They made the producer syntactically invalid before any scientific execution.

Smallest repair:
- commit cec992bf9fd9c617d11307640592ef88a3be6c68;
- no formula, chronology, coefficient/scaling, source, target, or lineage rule changed;
- only the two malformed literal newline boundaries were converted to actual source line breaks.

Classification: implementation/construction defect caught pre-execution. The equivalence gate remains PENDING and must still execute; this repair is not equivalence evidence.


## Verification correction
A subsequent direct full-source readback proved the first newline repair/verification was itself insufficient: the repository still contained the literal backslash-n bytes. The earlier check searched for the wrong escaped representation and produced a false clean result.

Actual byte-level repair:
- commit fc98cffc6300a81ea9e8d33445d753a53ed62a00;
- direct readback blob/content SHA 43f00fb6cada12a651307cdd14af79096c978efa;
- literal backslash-n occurrence count in the producer: 0;
- both affected boundaries directly read back as real source line breaks.

Process lesson: for escaped-text construction defects, verify the actual persisted bytes/full source, not a differently escaped search literal.

Equivalence remains PENDING.


## Construction validation after escape repairs
Persisted producer identity reviewed: abbdb43b38f24052e7d5cdb29e7065cb63c08c56.

Parser/source review confirms the repaired newline representation is syntactically valid. Direct v1.206-vs-v1.246 source comparison shows the feature list, strict-prior source selection, side-feature formulas, chronology audit, Champion coefficient/scaling hash locks, standardization, prediction equations, and prediction invariants remain unchanged.

Intentional generalized-refresh differences remain:
- dynamic nonempty unique target cardinality instead of fixed 622;
- allowed population classes instead of fixed 599/23 counts;
- target kickoff must be strictly after refresh cutoff;
- team-side/population accounting is dynamic;
- REFRESH_SNAPSHOT and cutoff metadata are appended;
- refresh-specific filenames;
- manifest uses dynamic counts and records parent lineage v1.216.

Classification: CONSTRUCTION VALIDATION PASS ONLY. This does not prove byte/output equivalence on accepted v1.206 inputs and does not satisfy the executable equivalence gate.

Current gate state: PENDING.


## First executable replay attempt — source drift stop
Run 36497510380 / job 109180408219 executed the equivalence workflow. Exact accepted v1.204 preflight ZIP and v1.193 fit ZIP checks passed. Reacquired current upstream schedule bytes did not match frozen schedule SHA-256 5b2ff52996862b06b67309f1ebc27742e55c279ff4785c7a942915cdf820f1b1, so the workflow failed closed before compilation or either producer executed. No equivalence evidence was produced.

Classification: MUTABLE-UPSTREAM REPLAY INPUT FAILURE, not scientific/equivalence failure.

Recovery audit found:
- v1.204 artifact 10897001956 preserves projection/preflight outputs and source hashes, not raw schedule/PBP bytes;
- v1.206 artifact 10897612260 remains available and is being inspected as possible preserved derived replay authority;
- current upstream bytes may not substitute for frozen source bytes.

Gate remains PENDING.


## Alternate scientific-equivalence proof design — frozen downstream substrate
The exact 2026 PBP RDS container used by v1.206 is no longer recoverable from the mutable upstream release. This does not authorize substitution of current PBP bytes and does not convert the raw-byte replay gate to PASS.

A separate bounded proof is authorized for QA construction validation:
1. Treat accepted v1.206 artifact 10897612260 (digest sha256:772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf) as immutable downstream scientific authority.
2. The accepted feature-eligibility ledger is the boundary after strict-prior schedule/PBP feature construction. For eligible sides it preserves the 17 model feature values consumed by the prediction matrix; chronology audit preserves prior-game counts/max-prior kickoff/strict chronology; target ledger preserves target population; exclusions preserve fail-closed disposition; predictions preserve final standardized Champion-model outputs.
3. Compare v1.206 and v1.246 source from that boundary forward: identical feature ordering, scaling identity checks, standardization, coefficient application, probability transformation, and prediction invariants, allowing only generalized target/snapshot metadata/output naming differences already enumerated.
4. Independently recompute accepted v1.206 final predictions from its preserved feature ledger plus the frozen accepted fit artifact and require exact agreement within the existing 1e-12 numeric tolerance.
5. If steps 3–4 pass, classify SCIENTIFIC TRANSFORMATION EQUIVALENCE PASS FROM ACCEPTED FEATURE BOUNDARY. Do not call RAW-SOURCE BYTE REPLAY PASS; that remains unresolved because the historical RDS container was overwritten upstream.
6. This proof may validate v1.246 construction semantics but may not authorize production promotion, Champion mutation, retrospective data replacement, or use of current PBP as a substitute.

Reason: RDS serialization bytes are transport/container provenance. The model consumes the loaded strict-prior projected feature values; those consumed values and their chronology/fail-closed outcomes were durably preserved in the accepted v1.206 artifact.


## Frozen feature-boundary reproduction — PASS
- Authoritative completed run: `36503794587`
- Head: `369ce94294fdcc7d9eb8b865c7ce1929e15e6463`
- Job: `109200493173`
- Accepted v1.206 artifact ZIP SHA verification: PASS.
- Frozen fit artifact ZIP SHA verification: PASS.
- Reconstructed the 34 home/away model features for all 526 accepted prediction rows from the accepted v1.206 feature-eligibility ledger.
- Reapplied exact accepted scaling, venue-neutral term, coefficient terms/lambdas, and clipped logistic win transform.
- Exact marker: `V1_206_FROZEN_FEATURE_BOUNDARY_REPRODUCTION_PASS 526`.
- Numeric comparison used rtol=0, atol=1e-12 for margin, total, and win predictions.

Classification: **FROZEN FEATURE BOUNDARY SUFFICIENCY PASS.** The accepted v1.206 artifact plus frozen fit artifact preserve the complete numerical boundary required to reproduce all 526 accepted v1.206 model predictions.

This does **not** convert the historical raw-PBP replay gate to PASS. Exact historical PBP RDS container bytes remain unavailable because the upstream release asset was mutable and overwritten. The raw-byte replay limitation remains explicitly recorded.

Next bounded QA gate: use this accepted feature boundary to validate that the generalized v1.246 refresh producer's downstream scientific transformation is identical to v1.206 while separately validating its intended generalized target/snapshot plumbing. No S2_K1 live companion acceptance or prospective freeze is implied.


## v1.246 static scientific-core identity — PASS
- Run: `36504978563`
- Head: `7e8a9d56e37bceb8ef275a64cf3f91ea36910ea9`
- Job: `109204260758`
- Marker: `V1_246_GENERALIZED_PLUMBING_STATIC_PASS`.
- v1.246 compiled successfully.
- Source comparison from the 17-feature declaration through the final prediction invariant is exact after normalizing only the two authorized dynamic-accounting expressions: `len(L)==2*len(S)` versus fixed 1244 and `len(X)+len(E)==len(S)` versus fixed 622.
- Static checks also confirm strict-future target enforcement, allowed population classes, REFRESH_SNAPSHOT metadata, cutoff metadata, parent lineage v1.216, dynamic target count/population manifest fields, and actual newline manifest termination.

Classification: **STATIC SCIENTIFIC-CORE IDENTITY PASS / DYNAMIC EXECUTION STILL REQUIRED.**
This is not by itself generalized-refresh acceptance. A synthetic/dynamic execution gate must exercise variable target cardinality and fail-closed target validation before v1.246 can be accepted as the S0 refresh substrate.


## v1.246 dynamic target-contract execution — PASS
- Run: `36505279253`
- Head: `03c715009f14ac657d8a92458a7ae005ad666abb`
- Job: `109205204346`
- Marker: `V1_246_DYNAMIC_TARGET_CONTRACT_PASS`.
- Valid 1-, 2-, and 3-target schedules passed all v1.246 target validation and advanced to the intentionally absent raw-source boundary.
- Duplicate game IDs failed closed at target schedule identity.
- A target not strictly after cutoff failed closed.
- An unauthorized population class failed closed.
- An empty target population failed closed.
- These cases execute the actual v1.246 producer entry path; they are not source-text assertions.

Classification: **DYNAMIC GENERALIZED TARGET CONTRACT PASS.**

### Layered equivalence status
The evidence now establishes three independent layers:
1. accepted v1.206 frozen feature-boundary numerical reproduction for all 526 accepted predictions at rtol=0/atol=1e-12;
2. v1.206→v1.246 scientific-core source identity through the final prediction invariant, except only the two authorized dynamic-accounting expressions;
3. actual v1.246 dynamic target-validation execution for variable cardinality and fail-closed invalid cases.

Exact historical raw-PBP RDS byte replay remains unresolved and is not reclassified.

Remaining acceptance question is bounded to end-to-end generalized output plumbing after feature construction (dynamic ledger/output cardinality, snapshot columns, manifest/file hashes). Do not call v1.246 accepted substrate until that executable output layer is either demonstrated or formally shown redundant by preserved accepted evidence.
