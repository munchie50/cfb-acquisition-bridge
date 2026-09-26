# CFB Engine — Challenger B Prospective Modeling Inheritance Contract v1.178

Status: **FROZEN PROSPECTIVELY / NO CHALLENGER-B PERFORMANCE EXPOSED**
Parent: v1.177
Higher population authority: v1.124 as corrected/enforced by v1.151
Feature substrate: accepted v1.173 / v1.172
No fitting, scoring, 2025 access, or market join occurred.

## Governing principle
Challenger B exists to correct Challenger A's population implementation defect, not to opportunistically redesign the model after 2023–2024 performance was observed.

v1.151 explicitly requires the corrected lineage to implement v1.124 population semantics consistently and preserve Challenger-A feature/model decisions as historical prior choices unless a separately prospectively justified change is made.

No new evidence-backed reason to change those choices has been established. Therefore Challenger B inherits them unchanged, with 2023–2024 treated as spent/corroborative evidence rather than fresh design evidence.

## Frozen population and targets
Adopt v1.124 unchanged:
- one canonical scheduled game with at least one FBS participant in the frozen relevant-FBS universe when required input/identity/temporal state qualifies;
- include FBS-vs-FBS, FBS-vs-non-FBS/FCS where present, regular season, conference championships and postseason;
- targets: home scoring margin, total points, home win probability from official final score;
- one game = one target observation;
- no market-derived target or population selection;
- cancelled/unplayed/ambiguous/unqualified rows fail closed.

Corrected 2016–2024 target universe authority is v1.157/v1.162/v1.164: 7,701 games / 15,402 team-sides.

## Frozen feature family
Adopt the v1.123 first-challenger feature/play contract unchanged, executed on corrected v1.172 substrate:
- 17 numeric history-derived/team-side features plus venue context;
- no finishing-drives feature;
- no combined turnover/fumble-lost feature;
- no opponent-adjustment/SOS feature;
- no new kneel/spike/garbage-time transformation;
- no preseason/previous-season prior;
- no model-stage imputation or zero-fill of unavailable history;
- no market/external-rating input.

The accepted v1.172 producer semantics and v1.173 acceptance govern corrected feature values and chronology.

## Frozen game-level representation
Adopt v1.130 unchanged:
- side-preserving home/away copies of each of the 17 numeric team features = 34 numeric predictors;
- one deterministic game-level venue state;
- no differences, sums, ratios, interactions or other engineered matchup transforms;
- canonical schedule home/away identity controls target and side assignment.

## Frozen model/search/numerical mechanics
Adopt v1.126 and v1.135 unchanged:
- Gaussian ridge linear regression for margin and total;
- ridge logistic regression for home-win probability;
- lambda grid exactly {0, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100};
- TRAIN-only centering/scaling of numeric predictors; venue dummy unstandardized;
- intercept unpenalized; non-intercept coefficients penalized;
- no lasso/elastic net, trees, boosting, neural nets, splines, interactions, adaptive grid expansion or post-hoc calibration;
- complete-case model eligibility; no model-stage imputation;
- raw logistic probabilities;
- same frozen target metrics and reporting requirements.

## Evidence strategy
Historical split labels remain:
- TRAIN: 2016–2022
- 2023–2024: **SPENT / CORROBORATIVE**, not fresh validation for inherited design choices;
- 2025: PROTECTED TEST, untouched;
- 2026: prospective live shadow.

For Challenger B, 2023–2024 may be reported after TRAIN-side model selection as corrected-population corroborative performance, but it must not:
- choose/change features;
- choose/change representation;
- change lambda grid or selection metric;
- change missingness/eligibility rules;
- add calibration;
- trigger a same-lineage redesign while being described as fresh validation.

Within 2016–2022, lambda selection remains forward-chaining with strictly earlier seasons used to evaluate each TRAIN fold as in v1.135.

This contract does not claim 2023–2024 is independent fresh validation for Challenger B.

## Dataset-freeze requirements before fitting authorization
A new Challenger-B dataset builder/workflow must:
1. consume the accepted v1.172 corrected feature artifact, not v1.109/v1.115 Challenger-A artifacts;
2. consume corrected schedule/target authority covering all 7,701 games;
3. machine-check v1.124 population-contract conformance by population class, as required by v1.151;
4. build canonical one-game rows with 34 numeric predictors plus venue state;
5. derive eligibility from corrected current inputs, not copy v1.128's old 42-game exclusion list;
6. emit a complete exclusion ledger with mutually intelligible reasons, including opening/no-prior/history-incomplete/input-identity/target/venue failures;
7. explicitly account for all 45 PBP-missing population games and all 1,342 newly admitted games;
8. assert no 2025 rows or inputs;
9. assert no market/external-rating predictors;
10. persist exact dataset/config/ledger hashes and row counts by season/population class;
11. pass independent readback/audit before any fitting authorization.

## Current gate
The prospective modeling choices are now frozen. The next authorized technical work is **Challenger-B dataset-freeze implementation and execution only**.

This checkpoint does not authorize model fitting or scoring. A successful dataset freeze must still receive independent acceptance and pre-fitting reconciliation before explicit Challenger-B fitting authorization.

Locks unchanged: production v1 champion/fallback; 2025 protected; no market join; no Challenger-B fitting/scoring; no production promotion.
