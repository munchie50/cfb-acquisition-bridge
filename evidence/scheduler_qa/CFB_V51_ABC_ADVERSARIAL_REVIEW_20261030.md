# v5.1 A/B/C — isolated adversarial regression and overhead review
Date: 2026-10-30
Status: QA REVIEW COMPLETE / NO PRODUCTION CHANGE
Baseline: original v5.0; candidates: v5.1-A/B/C. Inputs: Sep30 WAIT demonstration, Sep30 back-half evidence matrix, Oct08 recovery readback, Oct30 retrospective audit. Method: deterministic case/expected-action comparison; no new live runs.

| Scenario | A expected | B expected | C expected | Result |
| --- | --- | --- | --- | --- |
| Genuine WAIT with independent acceptance work | sweep finds prerequisite, leaves dependent task WAIT | reuse accepted evidence | label outstanding natural proof | PASS in Sep30 case |
| WAIT with no independent qualified work | stop after bounded sweep, do not manufacture work | no forced extra run | WAIT with exact trigger | DESIGN_PASS; no observed negative-case execution |
| Existing static PASS but natural producer unproven | no need to repeat static test | reuse static result, await natural proof | no false CLOSED | PASS in Sep30/Oct08 records |
| RUN_STARTED + terminal incomplete | independent recovery only if safe | reuse durable stage | INCOMPLETE, not PASS | PASS classification Sep30 |
| Write accepted and readback exact | no unnecessary sweep | do not rewrite | READ_BACK, not necessarily natural end-to-end | PASS classification Oct08 |
| NO_UPDATE, no linked receipt | independently inspect task/receipt evidence | do not blind retry | unknown dispatch, not CLOSED | DESIGN_PASS; actual failure root cause unknown |

## Baseline delta
A adds bounded WAIT sweep categories to v5 global reconsideration, no new authority. B adds proof-order preference to v5 bounded diagnostics/stop and does not weaken producer verification. C adds explicit proof-stage labels to v5 existing persistence/readback and output acceptance. No duplicate mandatory producer execution or extra scheduled task. None would necessarily prevent an opaque scheduler NO_UPDATE.

## Overhead assessment
Incremental external task count: 0. Mandatory extra live runs: 0. Additional repository writes per routine use: 0 (use existing checkpoint/receipt). Expected operator overhead: one short branch/label in existing work record when material, but no timed prospective measurement available. Hence B efficiency benefit remains UNMEASURED; cannot claim measured time savings or absence of material latency in natural production.

## Independent acceptance readiness
A: historical demonstration + adversarial case reasoning PASS, but no independent natural prospective negative-case demonstration. READY_FOR_REVIEW, not accepted.
B: historical selection behavior PASS, overhead measurement PENDING; READY_FOR_REVIEW_WITH_METRIC_DEBT.
C: multiple actual historical classifications PASS; READY_FOR_REVIEW, not accepted.
Decision: preserve independent control IDs and rollback. Recommend acceptance review for A/C, B conditional on observed overhead. User authorization for selective promotion intent is recorded; no production amendment accepted or activated here.

## Next branch
If independent reviewer accepts A/C, create additive versioned production amendment on authoritative main with explicit effective timestamp and rollback pointers, then readback. If reviewer finds semantic conflict, revise affected control only. For B measure overhead on next existing QA/production work unit before accepting. No fifth task, no model/bet change.
