# CFB Edge-First Decision Threshold — read-only challenger proposal
Date: 2026-11-20
Status: PROPOSED / NOT PRODUCTION / NOT ACCEPTED

## Observed defect
The Week 12 canonical Hot Sheet reports 68 PASS and 2 CONDITIONAL with no open primary recommendations. PASS conflates reviewed/no-wager, price hold, material football uncertainty, missing offer qualification, and cutoff failure. Game-level PASS is not evidence of a zero-edge model outcome. The frozen champion and original price limits remain authoritative until governed promotion.

## Proposed orthogonal dimensions
- FOOTBALL: SUPPORTED_EDGE / COUNTERCASE_DOMINATES / MATERIAL_UNCERTAINTY / UNCALIBRATED / NOT_REVIEWED.
- PRICE: QUALIFIED_VALUE / PRICE_HOLD / NUMBER_HOLD / QUOTE_UNAVAILABLE / NOT_EVALUATED.
- EXECUTION: VENUE_VERIFIED / VENUE_UNVERIFIED / WINDOW_CLOSED / NOT_CHECKED.
- DELIVERY: BET_CANDIDATE / PRICE_HOLD / WATCH_SPECIFIC_HOLD / NO_BET_REVIEWED / DATA_INCOMPLETE / CLOSED_HISTORY.

Do not relabel legacy canonical PASS as BET_CANDIDATE. Preserve all source decisions and append an independently derived display classification with reason, evidence, market, source clock, cutoff, and price.

## Proposed value test, challenger only
For a qualified two-outcome no-push market, decimal net profit per dollar b and estimated calibrated p, EV=p*b-(1-p). At integer lines, model push separately and compute EV=p_win*b-p_loss. Evaluate original estimate, uncertainty-adjusted lower bound, and the observed market break-even price; do not use uncalibrated spread or total projections as direct probabilities. Candidate qualifies when conservative estimated EV exceeds a preregistered hurdle, relevant material countercases are explicitly assessed, and an authentic available number/price is within the supported range. Compare +2%, +3%, +5% conservative expected return per dollar risked as SHADOW hypotheses, not accepted limits. No fixed high win-probability requirement.

## Matched retrospective and prospective acceptance
Freeze current champion decisions and quoted lines first. On identical pregame game-market snapshots, compute challenger decisions, incremental selections, true qualified price/line coverage, misses, pushes, ROI/net by market, calibration error, drawdown, and false suppressions. Count missing prices and expired windows separately. Compare at unchanged practical Friday 1 PM CT trip deadline and no more than the existing four tasks. Validate over multiple non-overlapping forward weeks and independently review risk/coverage; do not select the hurdle on winning outcomes or promote without explicit approval.

## Week 12 evidence limits
Selected canonical Week12 Hot Sheet: evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-19_1338CT.md, Git blob 4c8ebeb5dd95b7ea7309f45a9275f7509a198905. Its 68 PASS and 2 CONDITIONAL are legacy game-level decisions, not 68 proof-of-no-value classifications. A keyword diagnostic is not a causal count. No prospective challenger decisions or live wagers are authorized by this proposal.

## Next implementation
Create a read-only game/market-level classification report from the original six-market review plus qualified quote and timing evidence. Preserve raw state, football rationale, price blocker, venue and practical cutoff separately. Add negative fixtures for price-only hold, credible positive-value ordinary-risk candidate, uncalibrated model, missing quote, conflicting material injury, and expired deadline. Execute exact pinned source and original QA; only then consider a separately approved publication presentation change. Never bypass existing immutable/frozen/canonical gates.
