# CFB Production Operating Routine v5.2 — selective diagnostic amendment
Date: 2026-10-31
Status: USER-AUTHORIZED PRODUCTION PROCEDURAL AMENDMENT; NATURAL-USE DEMONSTRATION PENDING
Authority: explicit user approval in CFB Engine conversation 2026-10-31. Additive to accepted v5.1 amendment (2026-10-30) and v5.0 production promotion (v1.103). Retain both intact as rollback baseline.
Scope: diagnosis and work selection only. No Champion/Challenger, market, model, betting, source, publication, scheduler, task-count, or acceptance-gate changes.

## v5.2-D — escalating evidence-driven troubleshooting
For a new fault, use KISS: establish actual vs expected, current authoritative state, exact failed boundary and smallest testable hypothesis. For repeated or cross-component failures, escalate to onion-layer tracing of dispatch -> initialization -> authority recovery -> producer inputs -> outputs -> persistence -> publication -> independent reconciliation, skipping inapplicable layers. Compare verified last-good and first-bad checkpoints before speculative reconstruction. Use cross-boundary/Rubik's Cube analysis to check whether an apparently local repair violates downstream contracts. Record hypotheses as CONFIRMED, REJECTED, or OPEN with evidence; do not repeat rejected hypotheses without new evidence. Do not infer root cause from NO_UPDATE alone.

## v5.2-E — smallest correction and proof discipline
Identify first absent authentic producer artifact; distinguish missing dispatch, startup receipt, decision authoring, and output acceptance. Reuse original executable ancestry and existing QA/Health records. Execute smallest authorized correction; persist and independently read back. Use v5.1-C closure stages unchanged. Where natural execution is required, mark DEMONSTRATION_PENDING with exact natural trigger rather than manufacture an extra run or call a file write a repair.

## v5.2-F — regression learning with no extra bureaucracy
At existing checkpoints record root-cause class, what the test ruled out, boundary affected, prevention guard, expected vs actual, and whether it generalized. Reconsider dependency priorities and use v5.1-A independent WAIT sweep. No new mandatory document, recurring task, runner, or run for these labels. Independent runners only for genuinely independent read-only work; reconcile before serialized authority mutation.

## Controlled production trial and rollback
Active for diagnostic work immediately upon commit and independent readback; efficacy remains UNDEMONSTRATED until real work yields measured useful findings without delaying primary execution. Evaluate against current Market Monitor shared NO_UPDATE and decision_rows producer frontier, without changing their controls. If diagnostic overhead or regression occurs, disable only v5.2-D/E/F and revert to accepted v5.1, preserving evidence. v5.1-B evidence reuse, proactive branch-planning variants, and all other v6 candidates remain QA-only; no full v6 promotion.

## Established command
'Continue work using established routine' means recover newest accepted production routine via authoritative GitHub governance, use v5.0 + accepted v5.1 A/C + this additive v5.2 D/E/F while active, execute highest-value authorized work, and preserve established proof/stop rules. Do not treat conversational shorthand as authority over newer accepted persisted records.
