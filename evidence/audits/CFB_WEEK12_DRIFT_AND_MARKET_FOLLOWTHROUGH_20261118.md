# November 18 Week 12 manual drift and market follow-through

CBS returned 70 identities and 140 rows at 21:43:51 UTC. The 67 prospective games and 402 main-market fields were compared to 21:25:52 UTC. Fourteen number or price fields changed across eight games: Central Michigan–Buffalo, UTEP's game, Texas's game, Northern Illinois–North Dakota State, Pitt–Louisville, Georgia–South Carolina, San Diego State–Boise State, and Hawai'i–Nevada. Samford–Auburn still has six missing fields. CBS field-level mixed display cannot certify matched alternate lines, synchronized consensus or venue terms. See the [source capture](../operational/CFB_WEEK12_CBS_FULL_BOARD_20261118T214351Z_MANUAL.md).

## Corrections

- Wofford–Ole Miss: the previous explanation wrongly carried the no-quote premise into a sheet that displayed prices. Corrected to current plus-48.5/+100 and the remaining uncertainty about depth usage and Wofford protection. Passed the game after checking both sides, moneylines and totals.
- North Texas–Tulane: prior +6.5 reference conflicts with current UNT -6/-111. Neal Brown confirmed Jackson will miss the remaining regular season and Jimerson is expected to take over. That is a material correction to the former QB question. Do not assign a numeric adjustment or treat opposite market displays as true steam. Require matched independent market and role evidence before Thursday 13 CT. https://www.underdogdynasty.com/american-conference/47820/north-texas-qb-tayven-jackson-out-for-regular-season-chris-jimerson-jr-takes-over
- Georgia State–Marshall: the prior two positive spread fields are gone. The current asymmetric spread and two negative moneylines still require a coherent paired source. The existing deadline remains in force.

## Decision and availability checks

| Case | Disposition at 15:45 Central |
|---|---|
| Central Michigan–Buffalo | CMU +2.5 moved from -105 to +100. PASS stays in force at this bounded review; report expected 17:30 CT. Akron–UMass report expected 17:00 CT. No assumption of clearance. |
| Wake Forest–Georgia Tech | GT +21/-115 and Wake -21/-105. Original and accepted supplemental directions differ, and +21 sits far from either projected margin. Keep personnel applicability and same-book spread check open. |
| North Carolina–Virginia | UNC +1.5/-108 and Virginia -1.5/-110. With the accepted supplemental margin near even, the UNC quarterback and actual ACC listings still bear on any side; no new limit. |
| South Florida–FAU | USF -1/-108 and -110 versus FAU +1.5/-112 and -105. Current personnel/defensive continuity is relevant to the small side signal; the mixed 64.5 observations do not resolve the pace/risk case. |
| NC State–Florida State | NC State +10.5/-112. Retain watch for named-book quote and Bailey/Daniels and line availability. ACC confirmed kickoff; its Saturday report remains the next material input. |
| Arkansas State–Louisiana Tech | A secondary report names Jalen Ortiz interim. Treat the new lead as unconfirmed by the school. +13.5/-108 does not establish offensive continuity or a fresh issued limit. |
| Georgia–South Carolina | Georgia -16.5 improved three cents; South Carolina under 50.5/+100 versus prior under 51.5/-118. Number loss and price improvement are separate; Sellers/Bobo applicability remains material. Beamer directed readers to Wednesday evening's report. |
| Pitt–Louisville | Pitt +14.5 worsened from -115 to -120 and ML +490 to +450. Maintain the watch with no new limit pending offensive/QB corroboration. |
| Colorado State–Fresno State | Unofficial depth chart lists Hejny and the official Fresno preview links both game-note packages. Fresh +20.5/-115 falls short of resolving CSU lineup applicability and large-win tail risk. |
| Clemson–Duke | Wednesday report reproduction lists Clemson QBs Reynolds and Vizzina and Duke QB Walker out. The original model exclusion remains in force; no material new approved price or fresh selection. |
| Maryland–USC | Maryland +17.5/-110 in CBS display. A public compilation lists DraftKings +17.5/-115. Existing Thursday recheck and original cutoff stand; no venue confirmation. |

For remaining observed price moves, no new decision: UTEP and NIU had total-juice-only moves, Texas's total moved a point and ten cents, the SDSU–Boise total price changes were small, and Hawai'i received an extra half-point at worse juice while Nevada's moneyline shortened. Those are repricing observations. Full new material review across unaffected and previously changed games remains outstanding.

## Alternates and parlay depth

Public Maryland market listings displayed standard spread and derivative coverage. The reviewed sources did not establish an executable alternate number/price or an authentic combined quote. Maryland is the sole active straight conditional and therefore the only supported candidate in the current distinct-game pool. Including it in any later build would overlap with the straight card. No 3–5 leg build qualifies, and no theoretical payout is substituted for a sportsbook quote. The research depth target remains open.

## Publication checks

The pre-correction 15:31 sheet exact selected index commit 46ab717982d5da0aed83f21874b3dc223138f321 passed [GitHub Actions run 44402938242](https://github.com/munchie50/cfb-acquisition-bridge/actions/runs/44402938242). The three pre-index pushes had failed CI and are intermediate boundaries. Locally the pre-correction saved publication audit passed with zero reported exceptions; original frozen archive verification reproduced 56 predictions, 14 exclusions and all 168 numeric fields. All 65 neutral publication tests passed. The corrected proposal compiled and rendered all 70 games. Selection, corrected post-integration CI and readback are handled at the new integration boundary.
