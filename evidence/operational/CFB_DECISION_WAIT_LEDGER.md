# CFB Decision and WAIT Ledger

Status: ACTIVE APPEND-ONLY OPERATIONAL SURFACE
Initialized: 2026-09-27

## Recovery semantics
Canonical durable ledger for prospective BET EARLY / BET NOW / WAIT / PASS / INCONCLUSIVE decisions. Decisions are preserved before outcomes and never rewritten.

## Required decision fields
- decision timestamp CT
- game/market
- linked Champion snapshot
- qualified market observation reference
- decision state
- minimum acceptable line/price where supported
- rationale and maturity
- realistic next execution window

## Additional WAIT fields
- awaited information
- why it matters
- current opportunity/price at risk
- next trigger/review point
- latest useful decision point where supportable
- later disposition: HELPED / HURT / NEUTRAL / UNRESOLVED

## Initial state
No missing historical decision or WAIT state is inferred. Earlier unpersisted states remain UNRECOVERABLE unless separate genuinely pre-event evidence establishes them.

## Write-path validation — 2026-09-27 13:03 CT
- Purpose: controlled repair validation for canonical existing-file mutation.
- Governance effect: none; no decision, execution, settlement, prediction, score, or outcome state created.
- Method: SHA-guarded existing-file update followed by direct repository readback.


## Prospective decisions — 2026-09-27 13:08 CT
Champion snapshot: v1.208 FIRST_FROZEN / v1.193 accepted Beta Champion. Market observation: CFB_MARKET_MONITOR_STATE 2026-09-27 13:08 CT capture. Maturity: OBSERVATION ONLY / betting-layer calibration not yet sufficient to convert raw fair-line disagreement into invented EV or automatic wager authority.

- Alabama at Mississippi State — INCONCLUSIVE. Large Champion/market side disagreement (Champion Mississippi State by 9.865 vs market Alabama -5.5). Await: independent qualified market confirmation plus football/injury/source review sufficient to determine whether disagreement reflects information outside frozen Champion inputs. Opportunity at risk: Mississippi State +5.5. Next review: next governed market-monitor pass; do not chase if the number moves beyond any later-established acceptable threshold.
- Ohio State at Iowa — INCONCLUSIVE. Very large Champion/market side disagreement (Champion Iowa by 6.290 vs FanDuel Ohio State -14.5). Await: independent qualified market confirmation and matchup/injury/source review before any controlled-Beta expression. Opportunity at risk: Iowa +14.5 (-122) at observed source. Next review: next governed market-monitor pass.
- Maryland at Nebraska — WAIT. Champion Nebraska by 10.521 versus market Nebraska -12.5; raw side disagreement is modest and does not itself establish a bet. Await: cross-book confirmation and next information cycle. Current opportunity: Maryland +12.5 (-110); total 52.5 versus Champion 56.012. Next review: next governed monitor pass. Nebraska inclusion preserved regardless of Hot Sheet cutoff.
- Vanderbilt at Georgia — WAIT. Side is near Champion/market alignment; total differs by about 4.06 points (Champion 57.560 vs market 53.5). Await: cross-book total confirmation and matchup/injury review. Current opportunity: total 53.5 (-110). Next review: next governed monitor pass.


## Full-slate decision sweep — 2026-09-27 13:13 CT
- Scope: 47 relevant FBS-vs-FBS FIRST_FROZEN Week 5 games reconciled against the broad market benchmark where available.
- BET EARLY: 0 established from this sweep.
- BET NOW: 0 established from this sweep.
- Large raw Champion/market disagreements are INCONCLUSIVE pending independent market confirmation plus football/injury/source reconciliation; raw disagreement is not treated as calibrated EV or automatic wager authority.
- Other available games remain WAIT/monitor where no stronger governed state is supported.
- NOT_YET_AVAILABLE: UTSA at Rice; Utah State at Boise State; Arkansas State at Louisiana. Recheck on next governed market-monitor pass.
- Nebraska remains WAIT and is explicitly retained on the Early Board regardless of Hot Sheet cutoff.
- Minimum acceptable line/price is not invented where the betting layer has not earned one. Do not chase later movement beyond any prospectively established threshold.


## Prospective decision refresh — 2026-09-29 20:20 CT
Champion snapshot: v1.208 FIRST_FROZEN / v1.193 accepted Beta Champion.
Market reference: CFB_MARKET_MONITOR_STATE 2026-09-29 20:20 CT prospective reset capture.
Boundary: this is a new prospective decision boundary after the 2026-09-28 persistence gap; no missing Monday decision is reconstructed.

- BET EARLY: 0 newly established.
- BET NOW: 0 newly established.
- Priority large-disagreement games remain INCONCLUSIVE pending football/injury/source reconciliation and betting-layer evidence sufficient to establish an actionable threshold: Western Kentucky-New Mexico State; North Texas-Tulsa; Notre Dame-North Carolina; Alabama-Mississippi State; Syracuse-UConn; Michigan-Minnesota; Ohio State-Iowa; Memphis-Charlotte; Eastern Michigan-UMass; Old Dominion-Georgia State; Marshall-James Madison; Kentucky-South Carolina; Texas Tech-Colorado.
- Maryland at Nebraska — WAIT. Champion Nebraska by 10.5205 / total 56.0116; current broad market Nebraska -14.5 (-112) / total 52.0, with BetMGM cross-check at Nebraska -15 / 52.5. The side has moved farther from the Champion since Sunday's broad -13.5 observation. Await: next availability/injury and market cycle plus cross-book/executable-price review. Do not chase; no minimum acceptable line/price has yet been earned.
- Vanderbilt at Georgia — WAIT. Champion Georgia by 24.5805 / total 57.5598; current broad market Georgia -24 / total 50.5. Side remains close to Champion while total disagreement has widened. Await: total confirmation plus matchup/availability review.
- Previously unavailable UTSA-Rice, Utah State-Boise State, and Arkansas State-Louisiana now have current market coverage. They return to normal monitoring from this timestamp forward; no earlier decision is inferred.

Execution planning: no new casino trip is triggered by this refresh. Preserve the 1–2 trip/week portfolio objective; third trip requires a compelling documented reason.
Next trigger: scheduled CFB Market Monitor plus Wednesday-Friday Evening Availability where applicable. Any material new availability/price information must append prospectively.


## 2026-09-30 morning authorized-extra reconciliation
Boundary: prospective only; linked to the 2026-09-30 authorized-extra market observation already persisted in CFB_MARKET_MONITOR_STATE.md. The incomplete 07:01 CT cycle is not reconstructed.
Champion: v1.208 FIRST_FROZEN / v1.193 remains unchanged.

- No new actionable wager state is established by this reconciliation.
- Existing unresolved large model/market disagreements remain pending the previously required football, availability, and source reconciliation; raw disagreement alone does not establish action.
- Maryland at Nebraska remains WAIT. Frozen Engine: Nebraska by 10.5205, total 56.0116. Current qualified consensus observation: Nebraska -14.5 (-112), total 52.0. No acceptable threshold is established by this append.
- Vanderbilt at Georgia remains WAIT. Frozen Engine: Georgia by 24.5805, total 57.5598. Current qualified consensus observation: Georgia -24.5 (-109), total 51.0.
- Portfolio execution posture is unchanged: no additional casino trip is triggered by this reconciliation.
- No calibrated probability, EV, confidence, or threshold is inferred from market distance.

Next trigger: governed reconciliation deadlines and the normal 13:00 CT Market Monitor.


## 2026-10-01 ~17:40 CT user-authorized extra reconciliation
Boundary: prospective only; the missed 13:00 CT decision deadline is preserved as missed and is not reconstructed. Champion v1.208 FIRST_FROZEN / v1.193 unchanged.

THURSDAY — deadline reconciliation:
- Western Kentucky at New Mexico State — PASS. Prior state was INCONCLUSIVE. The governed Thursday default reconciliation deadline was the safely pre-kickoff 13:00 CT Market Monitor, which did not execute. At this new late prospective boundary, current benchmark remains New Mexico State -2.5 / 57.5, but no governed minimum acceptable line/price or calibrated actionable edge has been earned and relevant availability uncertainty remains. Do not force a bet or chase after the missed decision window.
- North Texas at Tulsa — PASS. Prior state was INCONCLUSIVE. The governed Thursday default 13:00 CT reconciliation deadline was missed. Current benchmark is Tulsa -1.5 / 57.5; late QB/availability uncertainty remains and no governed actionable threshold has been earned. Do not force a bet or create an extra casino trip to compensate for the missed cycle.

FRIDAY/SATURDAY:
- No new BET EARLY or BET NOW state is established by this extra cycle.
- Friday and Saturday games remain governed by their existing states and applicable future reconciliation deadlines. Newly retrieved benchmark movement is monitoring evidence only.
- Portfolio execution posture: no additional casino trip is triggered by this cycle.


## 2026-10-01 ~20:06 CT evening downstream reconciliation
Boundary: prospective only; Thursday persisted PASS states remain closed after their practical execution boundary. Champion v1.193 / v1.208 remains unchanged.

- Western Kentucky at New Mexico State — PASS remains final for this cycle; no reopening after deadline.
- North Texas at Tulsa — PASS remains final for this cycle. Later same-day confirmation that Baylor Hayes would start resolves part of the earlier availability uncertainty but does not retroactively reopen the decision.
- Pittsburgh at Virginia Tech — existing unresolved state retained for Friday. Current public reference moved to Pittsburgh +2.5 / Virginia Tech -2.5 with total 54.5. No earned minimum acceptable line/price is established here. Next governed reconciliation: Friday 13:00 CT; at that boundary it must transition to actionable, governed WAIT with hard final cutoff, or PASS.
- Penn State at Northwestern — not eligible for Champion-relative decision presentation under the recovered v1.208 Week 5 substrate because it is an explicit FIRST_FROZEN exclusion. Keep any market monitoring separately labeled unmodeled/excluded.
- Liberty at Delaware — likewise explicit FIRST_FROZEN exclusion; do not render as unresolved Champion prediction.

Portfolio posture: no additional trip is triggered by this evening reconciliation. No execution inferred.


## Friday recovery decision reconciliation — 2026-10-02 ~18:00 CT
Boundary: prospective only. The missed Friday 13:00 scheduled reconciliation is not reconstructed. Direct recovery of accepted artifact 10897612260 restored exact frozen Week 5 modeled rows. Decisions below use current qualified market/availability evidence; raw disagreement alone remains insufficient.

### BET NOW — portfolio execution candidates
- Alabama at Mississippi State — BET NOW: Mississippi State +5.5 or better; do not pay worse than -115. Current exact-price reference recovered at +5.5 (+100), with broad board +6. Frozen Engine favors Mississippi State by 9.8652. The disagreement persisted all week; current matchup reporting describes both teams as unbeaten and competitive, with no recovered availability evidence sufficient to explain a market reversal of this magnitude. If +5.5 is unavailable, take +6 or better; do not chase below +5.5.
- Syracuse at UConn — BET NOW: UConn +6.5 or better; do not pay worse than -115. Current exact-price reference +6.5 (+100). Frozen Engine favors UConn by 6.8817. Independent current numberFire material also favored UConn to win while current local matchup reporting identifies Syracuse QB performance/health uncertainty. Conflicting Syracuse-local opinion remains acknowledged; this is a controlled Beta expression, not calibrated EV.
- Ohio State at Iowa — BET NOW: Iowa +14 or better; prefer +14.5; do not pay worse than -120. Current exact-price reference +14.5 (-115). Frozen Engine favors Iowa by 6.2898. Iowa is 4-0 after beating Michigan; current reporting confirms elite early defensive results and a strong rushing profile, while independent current models/analysts also identify spread value near +14.5 even when projecting Ohio State to win. Do not take +13.5.
- Eastern Michigan at Massachusetts — BET NOW: UMass -6 or better; maximum -6.5 at -115 or better. Current DraftKings reference -6 (-108). Frozen Engine UMass by 22.0802 / home win 0.894632. Current UMass is 4-0 with a sellout expected; multiple current previews support UMass as the stronger side. Do not lay -7 or worse.
- Marshall at James Madison — BET NOW: James Madison -18.5 or better at -115 or better. Current cross-book references include Caesars -18.5 (-107), DraftKings -18.5 (-105), FanDuel -18.5 (-110). Frozen Engine JMU by 29.5062 / home win 0.955715; current preview evidence also supports JMU materially above the market number. Do not lay -19.5 or worse.

### WAIT / PASS
- Vanderbilt at Georgia — WAIT on total. Frozen total 57.5598 vs market 50.5, but Vanderbilt QB Jared Curtis remains a pregame decision. Trigger: confirmed Curtis availability. Hard cutoff: final practical pregame execution window before 11:45 CT kickoff Saturday. Side PASS at current Georgia -24.5 because frozen side is essentially aligned.
- Maryland at Nebraska — PASS side at Nebraska -14.5. Frozen fair margin Nebraska 10.5205; no chase. Nebraska remains on Hot Sheet. Total remains monitoring only; no threshold invented.
- Notre Dame at North Carolina — PASS for this Friday trip. Frozen Notre Dame by 3.1262 vs market about Notre Dame -21/-21.5, but current football analysis strongly supports Notre Dame and multiple Notre Dame injuries/UNC uncertainties complicate the stale-frozen disagreement. Do not force UNC solely from raw model distance.
- Michigan at Minnesota — PASS for this Friday trip. Frozen Engine favors Minnesota by 5.6597 vs market Michigan -5.5/-6.5, but current matchup/injury-aware analysis materially favors Michigan. The disagreement is not clean enough for controlled action.
- Texas Tech at Colorado — WAIT. Frozen Texas Tech by 1.7697 vs Colorado +13.5; some current analysis supports Colorado against the spread, but Colorado quarterback instability and player-dismissal context remains material. Later kickoff preserves a Saturday review window.
- South Carolina vs Kentucky — WAIT. Frozen South Carolina by 13.7709 vs current South Carolina -2.5/-3, but current defensive-line injury context and market movement toward Kentucky require one more availability review before action.
- All other modeled Week 5 games: no new BET NOW/BET EARLY state established by this Friday recovery unless separately listed above. Morning games not listed actionable are PASS for this execution trip rather than silently retaining INCONCLUSIVE beyond the Friday-evening decision boundary. Afternoon/evening non-actionable games remain eligible for the governed Saturday review where their execution window remains practical.

Portfolio posture: the five BET NOW candidates are intended to be batched into one Friday execution trip if the stated line/price floors are available. No execution is recorded until actual wager evidence is established.

- Pittsburgh at Virginia Tech — PASS at the Friday recovery boundary. Frozen Engine Virginia Tech by 7.8503 / total 51.6457 versus current broad Virginia Tech about -3 / 54.5, but the governed 13:00 reconciliation was missed and the practical execution window is too compressed to manufacture a late trip. Preserve as PASS; do not chase immediately before kickoff.
