# CFB Engine Semantic Canary Exception Audit — v1.97
Date: 2026-09-25
Status: bounded semantic-control audit; no semantic/model/source/production promotion.

## Test-routine action
Continued v5 from verified/read-back v1.96. Audited the successful full-season v19 artifact's semantic exception outputs and contract rather than inventing a new rule.

Workflow run 36195406478: SUCCESS
Artifact 10889583560: cfb-semantic-canary-full-season-v19
Producer: .github/workflows/Main.yml, semantic_canary_v0.17

## Full-season semantic audit
The producer's explicit promotion-readiness condition requires:
- tod_not_fourth_attempt == 0 for every season;
- tod_gain_reaches_line == 0 for every season;
- fourth_fail_unexplained == 0 for every season.

The successful v19 run completed its internal assertions and emitted V05_FULL_SEASON_SEMANTIC_AUDIT_PASS.

The artifact exception files were audited:
- downs_turnover_counterexamples.csv: no data rows
- fourth_down_unexplained.csv: no data rows
- range_exception_rows.csv: bounded separately by producer diagnostics and not a basis for silent semantic promotion

## Important contract boundary
Despite the clean bounded semantic controls, canary_contract_v05 and the artifact manifest explicitly retain:
- turnover_on_downs_semantic_promotion = false
- other_turnover_composites_promoted = false
- provider turnover composites as evidence only
- fumble_recovered_stat not promoted as lost-fumble identity.

Therefore a successful semantic canary is evidence of internal consistency under the candidate rule; it is NOT authorization to promote TURNOVER_ON_DOWNS into frozen production semantics.

## Classification
- FOURTH_DOWN_ATTEMPT semantic control: bounded PASS under the existing promoted definition.
- Candidate TURNOVER_ON_DOWNS internal exception controls: bounded PASS on the v19 full-season artifact.
- TURNOVER_ON_DOWNS promotion: NOT AUTHORIZED / remains candidate.
- Provider turnover composites: NOT PROMOTED.
- RAW_TURNOVER_RATE: remains OPEN/bounded and separate.

## Dependency consequence
The current full-season exception files do not expose an unresolved counterexample population requiring rule repair. Do not manufacture semantic work merely because PRIMITIVE_SEMANTIC_CORRECTNESS is globally PARTIAL.

Next global dependency reconsideration should move to another authentic unresolved proof obligation unless independent evidence appears that challenges these candidate semantics.

## Governance
Latest integrated Library ZIP remains v1.73; v1.74-v1.97 are bounded repository evidence checkpoints.
Production/master routine v4; active test routine v5.
Production v1 untouched; v2 challenger/shadow; 2025 TEST protected.
No fitting/tuning/source/model/production promotion.
