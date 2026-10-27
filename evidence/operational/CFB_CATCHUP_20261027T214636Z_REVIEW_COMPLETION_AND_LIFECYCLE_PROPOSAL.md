# CFB catch-up review completion and bounded publication proposal

Recorded UTC: 2026-10-27T22:04:16.606Z
Cycle: CFB_CATCHUP_20261027T214636Z
Status: RESEARCH_DISPOSITIONS_COMPLETE / FULL_MONITOR_RUN_INCOMPLETE

All45original-prediction games now have recorded research dispositions:39PASS,2new active conditional reviews,4expired noncanonical reviews. The11original model exclusions remain unchanged. This does not certify current market freshness, live publication, scientific accuracy or scheduled reliability.

## New conditional limits

| Game | Limit | Observed FanDuel benchmark | Disposition |
| --- | --- | --- | --- |
| Georgia Tech at Pittsburgh | Pittsburgh -6.5 or better, price -115 or better | Pittsburgh -7.5/-108, recovered by2026-10-27T21:50:25.899Z | Fails points cap; no bet at that quote |
| Boston College at Duke | Boston College +7.5 or higher, price -115 or better | Boston College +7.5/-124, recovered by2026-10-27T21:50:25.899Z | Fails price cap; no bet at that quote |

These are qualitative controlled-Beta recommendations, not calibrated EV, stakes or verified execution offers. Both reconcileWednesdayOct28 noonCT/17Z and expire13:00CT/18Z. These are new game-specific reviews, not renewals of the four expired cases. No extra trip or user availability assumed.

Review bindings:
- evidence/operational/recommendation_reviews/CFB_PITTSBURGH_CONTROLLED_BETA_20261027T214636Z.json; commit2fc90d9cef54610994a4e77b951fc92e8dbbabca; blobd8d9db2bfda198665fc42e76c0ab4fe75ab41bff.
- evidence/operational/recommendation_reviews/CFB_BOSTON_COLLEGE_CONTROLLED_BETA_20261027T214636Z.json; commitb9d76af90a9de25585f5cad6605e37f440c6c9a9; blob470a83cc91a51f913680f968765fd2633a71cf8c.

## Saved research and verification

- Twelve newPASS and two newconditional bindings: evidence/operational/CFB_CATCHUP_20261027T214636Z_DECISIONS_PROGRESS.json; commitef3078971237bba01469a2a244e1c876e34089c5; blob17b3fb55d66228f0a5a25d03b676622fd1e6b4a5.
- Final three researchedPASS: evidence/operational/CFB_CATCHUP_20261027T214636Z_FINAL_THREE_REVIEWS.json; commit4de3f2003e5d5070d6c56fed5874aa814735fb60; blob6fe7abd33b89bd1b0051aeeb536cdcd58a8d63ce.
- Existing unchangedV2semantics passed for both new immutable reviews using remote exact-content/commit-time/ancestry verification; only local load_review replaced in memory. Full production publisher/CI not executed.
- Authentic first-frozen archive hash verified;51original numeric strings across17new game reviews match. Existing full Week9 frozen-field invariant passes56identities/45predictions/11exclusions/135numeric fields in last selected sheet. Original-model proof is not new publication acceptance.
- QA evidence: evidence/scheduler_qa/CFB_CATCHUP_20261027T214636Z_QA_EVIDENCE.json; commit3aaae12c8a2a907bb3f49b68d5ef68a4510caa0b; blobbd267d26df2b395caa39f70523608968375b7245.

## Exact remaining publication blocker

Canonical decision ledger at immutable commit4de3f2003e5d5070d6c56fed5874aa814735fb60 independently recovered in full:1504623UTF8bytes; Git blob5df8464b0b2372134939cf81d576e155d641113b. Its latest Week9 packet is2026-10-26T12:07:18Z. All four relevant game rows remainINCONCLUSIVE and none references the saved immutable review path/blob. The old reviews expired2026-10-27T18:00:00Z; they cannot be revived, silently converted to analyticalPASS, or presented as previously canonical.

The active profile evidence/CFB_WEEK9_ORIGINAL_LINEAGE_PUBLICATION_PROFILE_2026-10-25.md says:
> Closed conditional reviews may be retained only byte-equivalent to their originating decision, validated against the exact paired original source boundary.

Those four have no such originating canonical boundary. No full current56game packet has been published, and no recovery frontier/current-sheet selection has changed.

## Concrete proposal requiring approval before integration

Add a bounded history-only EXPIRED_UNPUBLISHED_REVIEW status for the exact four independently recovered review identities. It records the present fact that the review expired before canonical publication and preserves the originalreview, limits, reconciliation, executionwindow, cutoff and missed-publication failure. It creates no past decision, active recommendation, currentPASS, wager or deadline extension.

The standalone proposed guard is restricted to the exact four recovered commit/path/blob/commit-time identities and Week9 original lineage; it rejects altered clocks/limits, wrong game, changed bytes, already-published reviews, pre-expiry records and after-kickoff reconstruction. Four authentic cases passed;ten negative cases rejected.

QA-only code: evidence/scheduler_qa/CFB_CATCHUP_20261027T214636Z_EXPIRED_UNPUBLISHED_PROPOSAL.py; commitaa74a77e520205f4fc924f9ba0496e4e3a9707bb; bloba92cab12f8c49def80b1c0e411db1fe2c54d9020. It is NOT registered in production schemas and does NOT authorize publication. Approval would permit the narrow lifecycle-rule addition and its shared compiler/renderer/readiness/consumer integration tests; fresh source capture, complete56row validation, canonical append/readbacks, current-frontierpreflight and existing selected-publicationCI still must pass before selecting a new sheet.

Scientific/Champion/model/task/schedule/money/execution effect: NONE. The earlier4expired cases remain closed. The one-time acquisition batch is completed, not continuing background analytical work.
