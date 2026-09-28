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
