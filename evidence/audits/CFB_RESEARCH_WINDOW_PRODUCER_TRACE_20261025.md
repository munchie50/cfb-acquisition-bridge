# Producer trace supplement — research/window follow-up

Run CFB_RESEARCH_WINDOW_FOLLOWUP_20261025T013517Z. Supplements CFB_RESEARCH_WINDOW_FOLLOWUP_20261025.md.
Current source scripts/cfb_hot_sheet_readiness.py at 55698ac802f728cf3ccb236a18d755e24658e2b6 explicitly maps row.cutoff_authority=='UNVERIFIED' to review.practical_cutoff='MISSING', then applies assess(review). It also retains row.planning_cutoff_utc in the output. This explains how a planning timestamp and PRACTICAL_CUTOFF_MISSING coexist. The marker is about unearned authority, not necessarily absence of a date. No18-case false-blocking claim is supported.

Current conditional profile scripts/cfb_conditional_recommendation_profile.py at c3d6ca0da2c39074c54f8dbe471d508863ae44d2 requires cutoff_authority REVIEW_EVIDENCED and exact agreement between canonical fields and immutable review, with valid execution window/cutoff/kickoff ordering. This is a justified integrity condition. Do not weaken it to improve apparent coverage.

The exact historical invocation/producer ancestry for every October17 row is not certified by reading today's code. This is current-mechanism proof and a narrower diagnostic interpretation, not a retroactive natural-run demonstration. Earlier report's request to trace the originating validation path is partially fulfilled; a deployment or semantic change is not warranted by the inspected evidence. Source wording clarification can remain part of existing QA explanation; no new gate or checklist is required.

Three incomplete-review cases and two independent original exclusions remain demonstrated by exact historical lineage/deadline joins. Four later conditional cases in the18-row deadline cohort remain separate prospective decisions. Four exact preview failures remain evidence-limited; no alternate-source failure or historical bet opportunity is inferred. No code, canonical state, outcome, model, risk limit, schedule or recovery index changed.
