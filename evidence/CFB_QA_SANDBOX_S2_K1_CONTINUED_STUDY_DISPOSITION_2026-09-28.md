# CFB QA Sandbox — S2_K1 Continued-Study Disposition — 2026-09-28

## Status
**CONTINUE S2_K1 IN SANDBOX STUDY / NOT ACCEPTED OR PROMOTED**

This disposition applies the original pre-outcome acceptance bar after independent acceptance of historical scoring evidence. It authorizes no production or Champion change.

## Authority
- Governing experiment contract: evidence/CFB_QA_SANDBOX_OPPONENT_STRENGTH_STABILIZATION_CONTRACT_2026-09-27.md
- Accepted scoring evidence: evidence/CFB_QA_SANDBOX_OUTCOME_SCORING_ACCEPTANCE_2026-09-28.md
- Frozen prediction artifact: 10970862853; prediction SHA-256 ed858f1bd72decd93d02aec4de507c3217470b8d01294c2cf677a2d79ed78ee3
- Accepted scoring run: 36491252415; artifact 11000219253.

## Frozen-bar assessment
1. Chronology/leakage: PASS for the accepted construction/scoring lineage.
2. Broad rather than outlier-only improvement: SUPPORTS CONTINUATION. On exact common games S2_K1 improves margin MAE and proper win-probability metrics; margin MAE improves in 7 of 9 seasons. Predeclared large-disagreement slices also show favorable same-game comparisons.
3. No material total/win degradation: MIXED BUT NOT A STOP FOR SANDBOX CONTINUATION. Overall total MAE and winner-direction accuracy degrade slightly, while Brier/log loss improve. This mixed evidence prevents scientific acceptance/promotion but does not erase the broader signal.
4. Stability across multiple seasons/history depth: PARTIAL. Multiple-season evidence is broadly favorable but 2022 and 2024 margin MAE worsen. History-depth stability is UNAVAILABLE because the necessary field was not frozen; it must not be reconstructed after outcomes.
5. No market/user-wager/outcome construction: PASS.
6. Artifact/hash/readback persistence: PASS through accepted scoring evidence.

## Disposition
S2_K1 is retained unchanged as the sole candidate for continued Sandbox validation. S1 candidates and heavier S2 k values do not warrant priority continuation from this experiment's accepted historical evidence.

This is deliberately weaker than candidate acceptance. The missing history-depth diagnostic and mixed total/direction behavior mean the original advancement evidence is incomplete.

## Next valid evidence
Use a genuinely prospective, outcome-blind continuation window. Freeze S2_K1 and S0 predictions plus the required history-depth metadata before outcomes. Do not tune k, formulas, thresholds, coefficients, scaling, or candidate family from the historical outcomes now observed. Evaluate only after the prospective window closes under separate bounded scoring authority.

## Prohibitions
- no Champion mutation or production promotion;
- no 2025 protected TEST access absent separate authority;
- no market/wager/execution inputs;
- no post-outcome history-depth reconstruction;
- no k-grid expansion, refit, recalibration, or formula redesign under this disposition.

Scientific effect: continued Sandbox study only.
Production effect: NONE.
Champion effect: NONE.
