# Saturday Week12 — read-only frozen forecast analytics, Nov21 2026

Status: EXECUTED as independent in-memory JavaScript computation on freshly fetched GitHub Hot Sheet, NOT certified analytics-v1 JSONL pipeline, NOT governed backtest, NOT production selector. Source: evidence/operational/CFB_WEEK12_SATURDAY_20261121_0948CT_MANUAL_CATCHUP_HOT_SHEET_NONCANONICAL.md, source Git blob f2f94238f122b786f18a386a3b2f0b56c42a37da. Computation parsed 58 exact markdown table rows under 'Current Saturday triage — all 58 games', with 46 numeric FIRST_FROZEN and 12 excluded.

## Recomputed metrics
- 46/58 (79.31%) numeric frozen predictions; 12/58 (20.69%) originally excluded.
- 14/46 (30.43%) numeric spreads have abs(frozen spread) <= 3.0, so a market number/price can materially change the decision. This is a *sensitivity bucket*, not a new model threshold.
- 7/46 (15.22%) have abs(frozen spread) >= 14.0, a large-margin bucket; this does not imply value or authorization.
- Frozen totals range 40.1 to 59.6, descriptive only.
- 4/46 (8.70%) have opposite implied winner between frozen spread favorite and home win probability relative to 0.5: Houston @ West Virginia (Houston -0.5; home win 0.503), Iowa @ Illinois (Iowa -1.2; home win 0.529), Georgia Southern @ Troy (Troy -2.1; home win 0.493), Arkansas State @ Louisiana Tech (Louisiana Tech -0.4; home win 0.494). These four were already flagged in prior audit; independently reproduced, not newly discovered.
- The 14 near-pick'em games: Syracuse @ Boston College, Wisconsin @ Purdue, North Texas @ Tulane, Houston @ West Virginia, Iowa @ Illinois, Delaware @ New Mexico State, UCLA @ Michigan, Georgia Southern @ Troy, South Alabama @ Southern Miss, Washington State @ Texas State, Maryland @ USC, Arkansas State @ Louisiana Tech, Utah @ TCU, Oklahoma State @ Arizona State.
- Large-margin group (7): Vanderbilt @ Florida, Wofford @ Ole Miss, Colorado @ Cincinnati, Charlotte @ Tulsa, UL Monroe @ App State, Arkansas @ Texas, Northern Illinois @ North Dakota State.

## Six public discrepancy probes — descriptive, not executable
Using previously preserved *historical* public indicative spreads, compare signed home margin. Iowa @ Illinois: engine Iowa -1.2 vs public Iowa -8.5 => 7.3-point discrepancy. LSU @ Tennessee: engine Tennessee -9.6 vs public LSU -1.5 => 11.1 points opposite favorite. Texas Tech @ Baylor: engine Baylor -8.1 vs public Texas Tech -5.5 => 13.6 opposite favorite. UCLA @ Michigan: engine Michigan -3.0 vs public UCLA -3.5 => 6.5 opposite favorite. Arizona @ Kansas State: engine Kansas State -13.8 vs public Arizona -7.5 => 21.3 opposite favorite. Utah @ TCU: engine Utah -2.2 vs public Utah -8.5 => 6.3 points. Differences are absolute distances of team-specific signed lines, not model edge, EV, confidence or bets. The public observations are stale/mixed clock and unqualified.

## Practical Hot Sheet improvement without governance mutation
Prioritize research by *unresolved personnel and market contradictions* rather than spread gap alone. Iowa Illinois (QB hold), LSU Tennessee (starter hold), Texas Tech Baylor (personnel hold), UCLA Michigan, Arizona Kansas State, Utah TCU are research watchlist only. Keep all 12 original exclusions excluded; keep the two expired 07:00 CT deadlines closed. No current same-book venue-qualified six-side offers verified, so no selector-eligible bets.

## Analytics-v1 governed contract boundary
evidence/operational/CFB_ANALYTICS_V1_CADENCE_AND_LEARNING_CONTRACT_20261120.md blob cd81e90e4691b1856bf88f08c506972bc0311ac1 requires certified point-in-time JSONL observations, source provenance, exact decision_at, and same-book/unit/quote type grouping. No such independently certified export was supplied in this execution. Therefore: ANALYTICS_V1_INPUT_UNAVAILABLE; CLV, ROI, market-movement backtest, calibration, and model-learning results NOT COMPUTED. This audit must not be substituted for the original champion selector or change frozen numbers.
