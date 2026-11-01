# CFB Week10 freeze-to-decision dependency preflight

Status: BOUNDED_QA_COMPLETE / NATURAL_PRODUCER_AND_DECISIONS_PENDING
Authority: latest current recovery index v1.246 blob 6b25766c90e3ae212efd529dc2b545c226e6abc7 inherits v1.245 and v1.247 cadence. Production v5/v5.1-A/C; v6 HOLD. This is QA evidence, not model/decision publication.

## Exact current dependency
Accepted prediction source state: evidence/operational/CFB_ACCEPTED_PREDICTION_SOURCE_STATE.json blob 42c6fed3dee79be8693d6750122ae08beeb24e3a; cutoff 2026-10-27T15:38:14.731739Z, accepted boundary CFB_QA_WEEKLY_REFRESH_ACCEPTANCE_2026-10-31_OCT27.md. This pointer cannot advance from workflow success alone; independent accepted prediction boundary is mandatory.

## Verified producer controls
Monday source-readiness workflow blob db945f573f0ced3fd97f0e9a4c7a37766bd1d5fe, cron 15:00 UTC Monday: downloads raw schedule/PBP, executes no-prediction preflight, retains manifest and artifacts. Tuesday candidate workflow blob a6f11072af8339abf92fd963589ce173d5fa5868, cron 15:00 UTC Tuesday: checks pinned code, fresh source hashes against accepted pointer, preflight future targets, retrieves pinned Champion fit, produces S0/context/target-baseline candidate when source changed. No automatic acceptance. Wednesday fallback blob 03959537eb7d8192734fbe9f39562958ee5d5774, cron 15:00 UTC Wednesday: checks preceding Tuesday *scheduled* run success; if absent/failing dispatches Tuesday workflow. It does not independently verify scientific acceptance; Tuesday success is only candidate/workflow completion. All workflows configured, natural Week10 execution not established here.

## Conditional branch plan and earliest evidence
1. Monday no-prediction preflight PASS: verify actual Actions run, raw SHA256, cutoff, future count, manifest, artifacts; Tuesday proceeds. Monday failure: inspect exact first source/preflight failure; do not fake source readiness or manually shift cutoff.
2. Tuesday changed qualified sources and future targets: candidate artifacts may exist; independently audit complete S0 targets/predictions/exclusions, chronology, hashes and same-cutoff context, then authorized acceptance/pointer advancement. Tuesday NOOP from unchanged source: preserve accepted pointer, verify whether current Week10 target predictions are actually covered; NOOP is not fresh Week10 certification. Tuesday failure: Wednesday bounded fallback may dispatch, but no automatic acceptance.
3. Independently accepted Week10 frozen Champion and material/market/operator qualification: Monitor may author six-market reviews, retain original line/price/cutoff, qualify consensus/venue separately, then guarded canonical Hot Sheet/decision persistence. Until then all 378 source-observed branches are uncertified, not 378 analytical PASS judgments.
4. Downstream QA: verify Monitor's actual current 63-game six-market review coverage, independent decision maturity and user-practical cutoffs. No fabricated Top10, EV, wagers, or venue confirmations.

## Current source gap
Natural Monitor closure c30170a15c85ff4905a8c2bd0254fda882d13754: 60/63 CBS displayed, two other-source displays (UCF/Kansas, Rutgers/Wisconsin), one unavailable (NIU/San Jose State). Fallbacks are not verified executable offers. Existing QA handoff audit blob 77aaaf145f84160e592e43c7224bb7fba9a66ac1 retained.

## Distinct operational risk identified
Wednesday fallback uses Tuesday scheduled **workflow success**, not independent candidate scientific acceptance, to decide no-op. This is consistent with its workflow-dispatch role but cannot be treated as acceptance proof. Tuesday workflow's pinned Champion-fit artifact download is another concrete dependency to inspect if a natural run fails; static YAML readback does not prove artifact availability. Do not mutate workflow without observed failure or separately justified bounded approval.

No Firecrawl spend, no additional recurring task, no schedule/model/Champion/cash/decision mutation. Big Nine PAUSED.
