# S2_K1 Week8 prospective outcome comparison — October25,2026

Status: independently verified descriptive comparison of one44-game prospective cohort.
Actual report clock: 2026-10-25T16:43:54Z

The user repeated the instruction to begin the listed QA work after the historical numerical baseline finished. The separate bounded scoring authority was saved and independently read back before S2output access in this stage: evidence/run_receipts/CFB_S2_WEEK8_BOUNDED_SCORING_20261025T163928Z_AUTHORITY_AND_RUN_STARTED.md (Git blob20ff2cf2d68347bdb0281d306f62737ee16e24b5). Earlier freeze/weekly records correctly saying scoring was unauthorized remain historical and unchanged.

## Result

S2_K1 was worse than the exact matching S0 REFRESH control on both margin/total MAE and RMSE, Brier, log loss and winner-direction counts in this first cohort. Signed mean errors were closer to zero, but smaller bias did not produce better overall errors. This does not support promotion. Disposition: CONTINUE IN QA / OBSERVE; no model, parameter or threshold changes, no automatic scientific acceptance or retirement.

| Metric | Matching S0 | S2_K1 | S2 minus S0 |
|---|---:|---:|---:|
| margin mae | 10.682253193 | 11.628763537 | 0.946510344 |
| margin rmse | 13.766117132 | 14.958998277 | 1.192881146 |
| margin bias | 1.107990474 | 0.707970598 | -0.400019876 |
| total mae | 15.393091392 | 15.760982186 | 0.367890794 |
| total rmse | 18.959405762 | 19.384623048 | 0.425217286 |
| total bias | 1.336151823 | 0.731805767 | -0.604346056 |
| win brier | 0.200439326 | 0.222437693 | 0.021998367 |
| win log loss | 0.588506194 | 0.639605110 | 0.051098917 |
| margin direction correct | 30 | 29 | -1 |
| probability classifier correct | 31 | 28 | -3 |

Lower MAE/RMSE/Brier/log loss is better; bias should be interpreted by distance from zero. Correct counts are out of44. Margin-sign winner direction and probability-threshold classification are separately reported; neither is bet profitability.

## Frozen population and source separation

All44candidate games and their unchanged same-cutoff S0controls are included. Both were genuinely frozen before kickoff from the October13 accepted source; accepted freeze6b0d6b0983fec9c2d9ccb217413639a643409b57 and all four output SHA256/Git blob bindings were authenticated. Candidate/control values, original model dates, qualified current kickoffs and all frozen metadata remain byte-identical. No forecast was regenerated or retimed.

Control is exact October13 S0 REFRESH on these same44games, not the September26 operational FIRST_FROZEN cohort. Five study games were original FIRST_FROZEN exclusions but eligible in the independently accepted REFRESH study. Their results were already retained as scorecard outcome context and are valid here; they remain production exclusions and are not added to the original-model baseline. Do not compare this44-game S0 result with the249-game baseline as if the samples or source cutoffs matched.

All44finals match both the governed scorecard and the independently parsed complete56-game CBS results capture at2aa53f5793bb511373eba9bbbf6e6249d3984836. Only final identity and scores were extracted from the latter; its completed-game prices remain quarantined and are not scientific inputs.

## Predeclared slices

| Slice | Games | Interpretation |
|---|---:|---|
| DEPTH_1_2 | 0 | No evidence for shallow history |
| DEPTH_3_4 | 0 | No evidence for intermediate history |
| DEPTH_5_PLUS | 44 | Entire cohort; identical to all-game result |
| Margin disagreement >=7 | 1 | Too small for a general conclusion |
| Total disagreement >=7 | 0 | Empty; not omitted or threshold-adjusted |
| Win probability disagreement >=0.10 | 5 | Small descriptive subset; S2 probability losses were worse |

All declared metrics for each nonempty slice and explicit null results for empty slices are in the machine artifact. Win-disagreement games had S0Brier0.115252 versus S2Brier0.226497 and probability classification5/5versus2/5; n5is small and cannot establish a new rule. No threshold was chosen from the results. This cohort cannot test the original shallow-history hypothesis because it has no such games.

## Verification

The independent verifier checked all44IDs/directed final pairs against the full CBS capture, preserved all frozen fields including264candidate/control numeric strings, and reproduced eight loss metrics plus two classifiers per model in every nonempty declared group using50-digit Decimal arithmetic. Seven disposable corruptions were rejected: omitted/duplicate games, changed history slice/cutoff, late freeze, invalid probability and conflicting excluded-game final identity. All four original output hashes remained unchanged. No probability clipping was applied; no boundary infinities occurred.

Main machine result: evidence/audits/CFB_S2_WEEK8_OUTCOME_COMPARISON_20261025.json. Independent proof: evidence/audits/CFB_S2_WEEK8_OUTCOME_VERIFICATION_20261025.json. Read-only scoring/independent verification helpers accompany them. Output source and authority hashes are retained.

## Existing QA action and next proof

The separate scoring-authority/finality blocker is closed for this exact cohort and stage. The S2promotion tracking action advances from FROZEN/UNSCORED to FIRST PROSPECTIVE COHORT SCORED / CONTINUE IN QA. Adequate prospective evidence, missing history-depth coverage and acceptance/production authority remain open. A later weekly source boundary still needs its own matched accepted companions and genuinely pre-event freeze under the existing cadence. Preserve k1, construction, coefficients, scaling, metrics and slice boundaries; do not tune from this outcome. A later result can improve or worsen the assessment, but no sample-size/promotion threshold or deadline is invented here.

Benefit: honest negative prospective evidence closes an unscored-cohort backlog and tests whether the historical signal carried forward. Cost: bounded retained-data scoring and readback, no source credits or model run. Net HELPFUL for evaluation integrity; predictive result adverse in this cohort, financial effect UNKNOWN. No wager/market join, stake, production change, Champion mutation or protected2025TESTaccess occurred. Natural production/research delivery remains a separate open QA item.
