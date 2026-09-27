# CFB Engine — Betting Layer Research and Test Roadmap v1.227

Status: **DOCUMENTED CANDIDATE ROADMAP — NO AUTOMATIC PRODUCTION AUTHORITY**
Date: 2026-09-26
Parents: v1.144, v1.198, v1.216, v1.226

## Objective

Eventually evaluate the full betting decision stack without contaminating the independent CFB Champion or optimizing thresholds after outcomes are known.

Sequence:
Champion football prediction -> freeze -> qualified market observation -> decision/timing -> execution -> qualified close -> outcome -> separate evaluation -> Challenger/betting-layer research.

## NOW — active evidence collection under v1.226

1. market/price history;
2. executable price versus benchmark separation;
3. qualified closing-line comparison / CLV;
4. key-number context;
5. timing/execution quality;
6. PASS/WAIT/no-bet opportunity preservation.

These are prioritized because evidence can be collected prospectively without claiming calibrated cover probabilities.

## NEXT — candidate tests after sufficient clean prospective evidence

### Edge calibration
Test predeclared raw-disagreement buckets and continuous relationships against outcomes/closing market.
Requirements:
- adequate prospective sample;
- buckets/analysis plan frozen before outcome inspection for confirmatory tests;
- avoid selecting thresholds because historical returns look best;
- separate sides and totals unless evidence supports pooling.

### Market-disagreement decomposition
Study where Champion differs from market by game class, venue, favorite/underdog size, competition class, season phase and other predeclared slices.
Use for hypothesis generation first; any resulting rule must be frozen and prospectively tested.

### Side / total / moneyline expression
Evaluate whether a Champion opinion is better expressed as spread, total, ML, or no bet.
Requirements include qualified prices, vig/odds semantics and calibrated probability evidence. No current automatic selection rule.

### Fair-line uncertainty
Develop/test uncertainty estimates around Champion point predictions.
Do not fabricate confidence bands from point predictions. Method must be frozen and validated before influencing betting thresholds.

### Book dispersion / line shopping
Measure differences among simultaneously available qualified books and the execution benefit from shopping.
Keep benchmark consensus distinct from executable sportsbook prices.

## LATER — requires calibrated probability/market evidence

### Cover/total probability and expected value
Translate model/market disagreement into calibrated probability only after prospective validation.
EV must use actual offered odds and explicit vig/price semantics.
Do not equate raw point edge with EV.

### Stake sizing / bankroll management
Evaluate only after probability calibration is credible.
Candidate methods may include flat staking and conservative fractional-Kelly comparisons.
No staking algorithm is authorized by this roadmap.

### Portfolio exposure
Measure correlated exposure across games/teams/conferences/game environments and shared model-error factors.
A slate is not automatically a set of independent wagers.

### Correlation and parlays
Require explicit leg probabilities, correlation treatment, offered parlay price and minimum acceptable price.
Never manufacture an engine-recommended parlay by multiplying unqualified probabilities.

### Alternative lines / price-line tradeoffs
Evaluate -6.5 at one price versus -7 at another using calibrated distributions/price semantics rather than intuition alone.

## Evaluation architecture

Keep distinct scorecards for:
1. football prediction quality;
2. market-disagreement signal quality;
3. bet-selection/threshold quality;
4. timing quality;
5. execution quality;
6. staking/portfolio quality, when authorized;
7. realized outcome/variance.

A losing wager can coexist with good prediction/timing/execution evidence; a winning wager does not prove those decisions were good.

## Champion / Challenger boundary

The Champion remains the independent football prediction engine.
Betting-layer research may use frozen Champion outputs plus separately qualified market/execution/outcome evidence.
No betting-layer finding silently becomes a Champion feature or changes the frozen football model.
Any new betting rule must be developed/tested in Challenger/sandbox state, frozen prospectively, independently evaluated, and explicitly promoted under applicable governance.

## Promotion principle

For every candidate concept:
hypothesis -> source/semantic qualification -> frozen test definition -> development/corroboration -> prospective test -> independent acceptance -> explicit production authorization where required.

No concept is promoted merely because retrospective ROI, hit rate, or a selected slice looks attractive.
