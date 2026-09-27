# CFB QA Sandbox Candidate Generator Pre-Execution Correction — 2026-09-27

Status: CORRECTED BEFORE EXECUTION / BEFORE PREDICTION FREEZE / BEFORE SCORING
Parent implementation commit: b9aa9fb0149855eb044e787ee2afbf22f9aa253d
Production effect: NONE
Scientific result effect: NONE

Pre-execution inspection found that frozen train_scaling.csv is correctly keyed by the Champion's 34 predictor names (home_<feature>, away_<feature>), while the newly persisted Sandbox generator asserted a 17-name raw-feature index.

Had the generator been executed unchanged, its own scaling-feature guard would have stopped execution. No candidate predictions were generated or frozen and no outcomes were scored.

Correction:
- expected scaling schema changed from the 17 raw feature names to the exact 34 home_/away_ predictor names already used by the frozen Champion;
- S1/S2 transform semantics, k grid, mappings, chronology, coefficients, scaling values, eligibility, outcome isolation and 2025 prohibition are unchanged.

This is a prospective implementation/schema correction discovered by preflight, not a result-driven experiment change.
