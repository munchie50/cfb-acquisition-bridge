# CFB QA — Weekly Target-Baseline Candidate Integration — 2026-09-30

Status: INSTALLED IN WEEKLY CANDIDATE BOUNDARY / NOT ACCEPTED / NO S2 PREDICTIONS

Executable-readiness review confirmed the accepted v4 companion already emits the exact 2026 mechanical_primitives.csv and derived_primitives.csv required by the recovered target-baseline companion. No additional source acquisition or duplicate primitive producer is required.

The Tuesday candidate workflow now:
1. runs the accepted S0 refresh producer;
2. runs accepted v4 source-context producer;
3. runs the S2_K1 target-baseline companion from S0 target-side + v4 primitive outputs at the same immutable cutoff;
4. requires baseline manifest status EXECUTED_NOT_ACCEPTED and explicit false S2/outcome/market flags;
5. retains baseline/target_baselines.csv and baseline/manifest.json inside the same candidate artifact;
6. records target-baseline producer Git blob c04f59ae2c4a591727816476d5b1099990bf6657 in the boundary manifest.

The producer is pinned in workflow authority recovery with git hash-object. The weekly no-op regression guard was extended so target-baseline generation must remain conditional on candidate_needed=true; unchanged source state cannot manufacture it.

This integration does not accept the target-baseline surface. Independent same-cutoff reconciliation/acceptance remains required before the S2_K1 consumer can execute.

No workflow was manually dispatched. No new source bytes, prediction, outcome evaluation, protected 2025 TEST access or Champion change occurred. Frontier remains CADENCE WAIT.
