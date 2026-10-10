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


## 2026-10-02 ~19:40 CT Friday evening availability reconciliation
Downstream of the ~18:00 Friday Recovery baseline. No historical decision is reconstructed.
- Mississippi State +5.5 or better (max -115): BET NOW unchanged.
- UConn +6.5 or better (max -115): BET NOW unchanged.
- Iowa +14 or better, prefer +14.5 (max -120): BET NOW unchanged; current Friday reporting still shows +14.5.
- UMass -6 preferred, maximum -6.5 at -115: BET NOW unchanged.
- James Madison -18.5 or better (max -115): BET NOW unchanged.
- Vanderbilt-Georgia total: WAIT unchanged. Trigger remains final Jared Curtis pregame status; hard cutoff remains final practical execution window before kickoff. Do not bet the total tonight solely from the frozen/market gap.
- Texas Tech-Colorado: WAIT unchanged. New information: Texas Tech backup QB Thomas Castellanos ruled ineligible. This does not resolve the broader Colorado QB/roster uncertainty or earn an actionable threshold tonight. Reconcile Saturday before the later kickoff.
- Kentucky-South Carolina: WAIT unchanged. Kentucky LB Alex Afari is newly ineligible; South Carolina defensive-line availability concerns remain. Mixed availability evidence does not earn a Friday bet. Reconcile Saturday.
- Nebraska-Maryland side: PASS/no-chase unchanged.
Portfolio posture: no sixth Friday wager is added. The existing five-candidate trip remains the complete Friday execution card, conditional on actual line/price cutoffs at the window. No execution recorded.


## Saturday morning decision reconciliation — 2026-10-03 07:19 CT
Prospective boundary: CFB_RUN_STARTED_2026-10-03_0719CT_MARKET_MONITOR. Current market source is the same-cycle persisted full-slate FantasyData consensus capture in CFB_MARKET_MONITOR_STATE. Champion remains v1.193 / v1.208 FIRST_FROZEN.

### BET NOW — unchanged and currently within established cutoffs
- Alabama @ Mississippi State — Mississippi State +5.5 (-113): BET NOW. Minimum +5.5 or better; max price -115. Current number qualifies. If unavailable at actual execution window, do not take +5 or worse.
- Syracuse @ UConn — UConn +6.5 (-106): BET NOW. Minimum +6.5 or better; max price -115. Current number qualifies.
- Ohio State @ Iowa — Iowa +14.5 (-117): BET NOW. Minimum +14 or better; prefer +14.5; max price -120. Current number qualifies. Do not take +13.5.
- Eastern Michigan @ UMass — UMass -5.5 (-109): BET NOW. This is better than Friday's -6 reference and inside the established maximum -6.5 at -115 or better.
- Marshall @ James Madison — James Madison -18 (-110): BET NOW. This is better than Friday's -18.5 reference and inside the established max -115 price.

Execution state: NONE ESTABLISHED in CFB_EXECUTION_LEDGER as of this read. Do not infer that Friday's planned trip occurred. If these candidates were not already executed, one practical Saturday-morning execution window before the 11:00 CT games is the portfolio window; actual book numbers must satisfy each persisted cutoff. Do not chase.

### WAIT with hard reconciliation/cutoff
- Vanderbilt @ Georgia total — WAIT. Current total 50.5; frozen total 57.5598. Jared Curtis remains scheduled for pregame evaluation. Reconciliation deadline: 10:15 CT (approximately 90 minutes before 11:45 CT kickoff, aligned to final pregame availability reporting). Hard practical execution cutoff: 10:45 CT. At deadline resolve to actionable or PASS; no forced bet.
- Kentucky @ South Carolina — WAIT. Current SC -2.5 / total 53.5. Kentucky has multiple confirmed absences including Alex Afari; South Carolina still carries defensive-line uncertainty including Gabriel Brownlow-Dindy and Dylan Stewart's suspension. Reconciliation deadline: 13:45 CT. Hard practical execution cutoff: 14:15 CT for 15:15 CT kickoff. Resolve to actionable or PASS.
- Texas Tech @ Colorado — WAIT. Current TTU -13.5 / total 50.5. Thomas Castellanos is ineligible; Colorado QB choice/roster context remains decision-relevant. Reconciliation deadline: 17:00 CT. Hard practical execution cutoff: 17:30 CT for 18:30 CT kickoff. Resolve to actionable or PASS.

### PASS / no-chase
- Maryland @ Nebraska — PASS side at Nebraska -14.5. Frozen Engine Prediction (Frozen) fair spread Nebraska -10.5205; current market is beyond the frozen fair margin. Nebraska remains mandatory Hot Sheet display.
- Notre Dame @ North Carolina and Michigan @ Minnesota — Friday PASS remains closed; no reopening from raw frozen/market disagreement.
- Other Saturday morning modeled games not listed BET NOW or WAIT remain PASS at this morning execution boundary rather than drifting as INCONCLUSIVE.
- Afternoon/evening modeled games not already resolved remain governed by their applicable later-window review; no new threshold is invented solely from raw model/market disagreement.

Portfolio rule: no separate later Saturday trip is justified yet by the three WAIT games. A later trip requires an earned actionable transition at a stated cutoff and must be considered against the 1–2 trip/week objective. No execution is inferred.


## Week 6 Sunday opening-board decision boundary — 2026-10-04 ~08:40 CT
All 49 accepted modeled Week 6 rows begin OBSERVATION-STAGE / INCONCLUSIVE. Raw frozen-vs-market disagreement is an investigation flag only; no BET EARLY/BET NOW is manufactured from the opening board alone.
Reconciliation deadlines by current authoritative kickoff section:
- Tuesday (1 modeled game): Monday 13:00 CT review; must resolve to actionable, governed WAIT with explicit trigger/hard cutoff, or PASS by Tuesday final practical execution window.
- Wednesday (2): Tuesday 13:00 CT review; final practical Wednesday cutoff.
- Thursday (3): Wednesday evening availability review; final practical Thursday cutoff.
- Friday (5): Thursday evening review; final practical Friday cutoff.
- Saturday morning (7): Friday evening review; final practical pre-kickoff cutoff.
- Saturday afternoon (17): Saturday 07:00 review; final practical pre-kickoff cutoff.
- Saturday evening/night (14): Saturday 13:00 review; final practical pre-kickoff cutoff.
Exactly-once modeled count = 49; UNRESOLVED kickoff = 0. Indiana @ Nebraska is separately excluded/unmodeled under v1.208 and cannot receive a manufactured frozen prediction. Portfolio/trip optimization remains 1–2 trips/week; early-week games do not automatically justify an extra trip. No execution inferred.


## Tuesday morning recovery decision reconciliation — 2026-10-06 ~07:04 CT
Prospective boundary: manual recovery run after scheduled-control failures. Uses accepted frozen v1.208 predictions and same-run qualified market observations. Raw disagreement is not calibrated EV.

### Tuesday final-day decision
- Southern Miss @ Troy — **PASS side / PASS total at this morning boundary.** Frozen fair spread Troy -6.4 versus current Troy -10.5 (-108): the market requires laying materially beyond the frozen fair margin and no governed evidence earns chasing that number. Frozen total 51.9 versus current 50.5 is only a modest raw disagreement and no established threshold/edge converts it to an actionable wager. No extra casino trip is justified. Re-open only if genuinely new pre-kickoff information prospectively earns a governed decision before the practical cutoff; do not relax the PASS from price movement alone.

### Wednesday 13:00 CT reconciliation boundary remains active
- Jacksonville State @ Kennesaw State — **INCONCLUSIVE until Tue 13:00 review.** Frozen fair Kennesaw State -3.6; current market Kennesaw State +3.5 (-124), total 50.5. Large raw disagreement is an investigation flag only. No BET NOW threshold is manufactured.
- New Mexico State @ FIU — **INCONCLUSIVE until Tue 13:00 review.** Frozen fair FIU -3.2; current FIU -6 (-112), with CBS displaying side-specific total quotes around 46.5/47.5. No actionable threshold is earned solely from movement.

Portfolio posture: no Tuesday-morning trip is created. The 13:00 CT Market Monitor remains the required prospective Wednesday reconciliation point. No execution recorded.

## Friday prospective fail-closed review — 2026-10-09T12:38:21.065Z
Run: CFB_MANUAL_FRIDAY_REVIEW_20261009T123613Z; manual incremental review, separate from the morning scheduled STARTED-only cycle.
Authority: v1.226/v1.235/v1.237/v1.242; Champion v1.193 and FIRST_FROZEN unchanged. Current public benchmark capture: canonical market blob d13c5be0a12aed50242515e10362cdcd388cdcf2, observation boundary 2026-10-09T12:34:26.452Z. These are ESPN DraftKings-labelled retrieval observations, not verified executable Caesars offers or calibrated edges.

Current state for each listed game: PASS / NO BET AT THIS REVIEW BOUNDARY. The evidence does not establish an executable offer and an earned minimum acceptable line/price or otherwise justify action. This is a conservative prospective no-bet disposition, not proof that the price is bad or that the frozen model is wrong.
- Florida State @ Louisville — PASS side / PASS total. Large prior frozen-versus-benchmark discrepancy remains investigation-only; current team/offer completeness and an earned threshold are not established.
- Iowa @ Washington — PASS side / PASS total. Benchmark number/price changed, but no actionable rule or executable price is earned. Official 20:00 versus 20:05 CT kickoff conflict remains OPEN; do not extend a cutoff.
- Washington State @ Utah State — PASS side / PASS total. Opposite prior frozen/benchmark favorites remain investigation-only; no qualified execution offer or earned threshold established.
- Wyoming @ San Jose State — PASS side / PASS total. Benchmark price changed while spread stayed 4.5; neither small raw disagreement nor price change establishes a betting rule.
- Iowa State @ BYU — PASS side / PASS total. Opponent-authored expectations for LJ Martin/Isaiah Glasker remain unconfirmed final availability. A future-game score displayed in BYU page chrome is excluded from outcome and decision use. No earned threshold/executable offer established.

Moneyline/parlay recommendations: NONE established. Minimum acceptable line/price: NOT_ESTABLISHED for all five; none invented. Hard final execution cutoff: NOT_ESTABLISHED; no promise of a book/travel opportunity.
Next review: scheduled Friday 13:00 CT default v1.237 reconciliation, or earlier genuinely material qualified information before a valid practical execution cutoff. Reconsider prospectively only if evidence earns a changed decision; raw benchmark movement alone does not reopen or relax this PASS.
Opportunity at risk: a potentially useful price before verified information, not an earned bet. No drifting WAIT is created without a supportable final cutoff. Portfolio: no additional casino trip justified by this review; no user execution inferred.
Thursday missed-review evidence remains missing and is not retroactively repaired. These new decisions exist only from the current boundary onward. Later observations or outcomes must not rewrite them.


## Friday 13:01 CT scheduled decision reconciliation — 2026-10-09
Run: CFB_MARKET_MONITOR_20261009T180108Z. Uses independently read-back canonical market blob bbc222ec291ba1faff3f083f6da132d8e8214cae. Champion v1.193 and FIRST_FROZEN remain unchanged. Public CBS mixed-book benchmarks are not verified Caesars offers; raw disagreement is not calibrated EV.

### Friday — final scheduled review
The five prospective PASS / NO BET decisions established by the 07:38 CT manual review remain closed:
- Florida State @ Louisville — PASS side / PASS total.
- Iowa @ Washington — PASS side / PASS total.
- Washington State @ Utah State — PASS side / PASS total.
- Wyoming @ San Jose State — PASS side / PASS total.
- Iowa State @ BYU — PASS side / PASS total.
No minimum acceptable line/price is established; no late reopening from market movement alone; no casino trip is justified. Practical execution window: CLOSED by decision, not by kickoff.

### Saturday morning — Friday review resolved prospectively
All seven modeled rows transition from INCONCLUSIVE to PASS / NO BET at this review boundary. None has a verified executable Caesars offer plus an earned rule/minimum acceptable threshold. No bet is forced merely to clear INCONCLUSIVE.
- Arizona @ West Virginia — PASS side / PASS total. Frozen West Virginia -3.4 / 53.8 versus benchmark Arizona -3 / 61.5 is a large investigation flag only.
- Texas A&M @ Missouri — PASS side / PASS total. Frozen Missouri -7.7 / 48.5 versus benchmark Missouri -3.5 / 48.5; no calibrated threshold or executable offer.
- UCF @ Oklahoma State — PASS side / PASS total. Frozen Oklahoma State -4.3 / 55.1 versus displayed benchmark around Oklahoma State -9.5 to -10.5 / 53.5 to 54.5; side is beyond the frozen fair margin and no chase is permitted.
- North Carolina @ Pittsburgh — PASS side / PASS total. Frozen Pittsburgh -8.3 / 46.7 versus benchmark Pittsburgh -3.5 / 47.5; no earned actionable rule.
- Wake Forest @ NC State — PASS side / PASS total. Frozen NC State -9.3 / 59.3 versus benchmark Wake Forest -3.5 / 58.5; opposite favorites remain investigation-only.
- Sacramento State @ Bowling Green — PASS side / PASS total. Frozen Sacramento State -12.7 / 45.8 versus benchmark Bowling Green -7.5 / 44.5; opposite favorites remain investigation-only.
- South Carolina @ Florida — PASS side / PASS total. Frozen Florida -7.1 / 61.9 versus benchmark Florida -12.5 / 61.5; side is beyond frozen fair margin and no chase is permitted.

Minimum acceptable line/price: NOT_ESTABLISHED for all seven and none invented.
Pending reason/information: none retained as a drifting WAIT; current evidence is insufficient to earn action.
Reconciliation deadline: satisfied by this scheduled review.
Final practical execution cutoff: CLOSED by PASS.
Opportunity at risk: none established.
Portfolio posture: no Friday or Saturday-morning casino trip is justified from these rows.

### Later Saturday windows
- Saturday afternoon 17 modeled rows remain INCONCLUSIVE until the governed Saturday 07:00 CT reconciliation. Required transition then: earned actionable state, explicit governed WAIT with hard cutoff, or PASS.
- Saturday evening/night 14 modeled rows remain INCONCLUSIVE until the governed Saturday 13:00 CT reconciliation with the same fail-closed transition rule.
No execution is established or inferred. No additional trip is authorized. Market movement alone cannot create or relax an acceptable threshold.


## Friday dinner practical-window reconciliation — 2026-10-10T00:42:26Z
Run: CFB_DINNER_CARD_REVIEW_20261010T003803Z; manual user-directed review. User needs Saturday bets tonight; default Saturday review times do not govern these four dinner-window decisions. Exact departure time unspecified; no later WAIT created.
- Kent State @ Western Michigan: PASS / NO BET FOR THIS DINNER WINDOW. Frozen -26.7 / 48.3; saved benchmark -13.5 / 43.5 is not a current Caesars quote. Official preview supports directional research, but no earned selection/price cutoff or complete current availability/offer established.
- Houston @ Kansas State: PASS / NO BET FOR THIS DINNER WINDOW. Frozen -10.6 / 55.0; saved benchmark -2.5 / 55.5. Official season-ending Anciaux injury and Houston run-defense/third-down matchup make evidence mixed; no earned cutoff established.
- USC @ Penn State: PASS / NO BET FOR THIS DINNER WINDOW. Frozen -11.8 / 55.0; saved benchmark -1.5 / 54.5. Retrieved availability has significant absences/questionables; current Friday report and earned cutoff not established.
- Air Force @ Northern Illinois: PASS / NO BET FOR THIS DINNER WINDOW. Frozen -16.1 / 48.4; saved benchmark -7.5 / 46.5. Starting QB Szarka confirmed season-ending injury in report of team announcement; replacement offense not sufficiently assessed to earn a cutoff.
All four: acceptable line/maximum price NOT_ESTABLISHED; decision reconciliation satisfied now; current dinner execution window CLOSED by PASS. BET NOW singles/parlays NONE; no execution inferred; no separate trip justified. This is no-bet at the current practical window, not a price-quality/model-quality verdict. A later genuinely material qualified change requires a new prospective decision before any independently established execution window; price movement alone cannot reopen this PASS.
Full provenance/limitations: evidence/operational/CFB_WEEK6_DINNER_EXECUTION_CARD_2026-10-09.md. Other 27 later-window rows not individually reconciled in this manual four-candidate scope. Saturday-morning seven retain earlier PASS; Nebraska remains UNMODELED. Production sheet and frozen authority unchanged.


## October 9 19:53:50 CT — full Saturday dinner review

Run CFB_FULL_SATURDAY_DINNER_REVIEW_20261010T004642Z; prospective start 19:46:42 CT. Complete 38 modeled Saturday identities, side+total separately, plus Nebraska excluded. Evidence/card: evidence/operational/CFB_WEEK6_FULL_SATURDAY_DINNER_REVIEW_2026-10-09.md (report commit a6eace644007f2d1c001ae027fcd65ff50447602). Its source URL inventory may include navigation links; only specifically evaluated football evidence supports decisions, not presence of a URL.

Decision boundary 2026-10-10T00:53:50Z. Three qualitative controlled-Beta CONDITIONAL BET NOW side recommendations: App State -10 or better; UMass +4.5 or better; Fresno State +7 or better; each maximum -115, actual Caesars line/price must meet cutoff during dinner visit before kickoff. Retained ESPN/DK benchmark capture interval 00:46:42Z–00:53:50Z, source offer-update unknown, execution unverified. No bet placed, calibrated EV, cover probabilities or numerical injury adjustments invented. Champion/FIRST_FROZEN unchanged.

| Game | Side verdict | Total verdict |
|---|---|---|
| Arizona @ West Virginia | PASS | PASS |
| Texas A&M @ Missouri | PASS | PASS |
| UCF @ Oklahoma State | PASS | PASS |
| North Carolina @ Pittsburgh | PASS | PASS |
| Wake Forest @ NC State | PASS | PASS |
| Sacramento State @ Bowling Green | PASS | PASS |
| South Carolina @ Florida | PASS | PASS |
| Old Dominion @ App State | BET NOW CONDITIONAL — CONTROLLED BETA | PASS |
| Miami (OH) @ Massachusetts | BET NOW CONDITIONAL — CONTROLLED BETA | PASS |
| Texas vs Oklahoma | PASS | PASS |
| UCLA @ Oregon | PASS | PASS |
| Stanford @ Notre Dame | PASS | PASS |
| Ole Miss @ Vanderbilt | PASS | PASS |
| Illinois @ Michigan State | PASS | PASS |
| Houston @ Kansas State | PASS | PASS |
| Eastern Michigan @ Akron | PASS | PASS |
| Duke @ Georgia Tech | PASS | PASS |
| Central Michigan @ Ohio | PASS | PASS |
| Charlotte @ North Texas | PASS | PASS |
| Buffalo @ Toledo | PASS | PASS |
| Kent State @ Western Michigan | PASS | PASS |
| Rice @ East Carolina | PASS | PASS |
| Maryland @ Ohio State | PASS | PASS |
| Tennessee @ Arkansas | PASS | PASS |
| San Diego State @ Oregon State | PASS | PASS |
| Nevada @ UTEP | PASS | PASS |
| North Dakota State @ UNLV | PASS | PASS |
| LSU @ Kentucky | PASS | PASS |
| Air Force @ Northern Illinois | PASS | PASS |
| Syracuse @ Virginia | PASS | PASS |
| James Madison @ Georgia Southern | PASS | PASS |
| Georgia @ Alabama | PASS | PASS |
| Louisiana @ Louisiana Tech | PASS | PASS |
| USC @ Penn State | PASS | PASS |
| Minnesota @ Purdue | PASS | PASS |
| Kansas @ Utah | PASS | PASS |
| Hawai'i @ Arizona State | PASS | PASS |
| Boise State @ Fresno State | BET NOW CONDITIONAL — CONTROLLED BETA | PASS |

Nebraska unmodeled: PASS/no Champion-derived wager. No WAIT drifts. Earlier morning seven and dinner four PASS preserved. Newly reviewed App/UMass/Fresno were unresolved rows; qualitative football/current availability corroboration, not movement alone. Other35 sides and all38 totals PASS for the report's row-specific reasons. Kentucky excluded after final injury-report coverage. Rice/ECU time prospectively noon CT. Full final-team availability coverage incomplete; this is controlled Beta, not production certification. Earlier four-only RUN_INCOMPLETE unchanged. Scheduling/prompt enforcement repair and natural execution proof remain pending.
