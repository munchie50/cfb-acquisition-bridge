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


## Friday scheduled evening decision reconciliation — 2026-10-09 20:22 CT
Run: CFB_EVENING_AVAILABILITY_20261010T011934Z. Downstream of the persisted 19:53 CT full Saturday dinner review; no competing baseline.
- Appalachian State side: BET NOW CONDITIONAL remains. Accept only Appalachian State -10 or better at max -115. Fresh public -10 benchmark has no verified price/book execution; actual Caesars offer must qualify. Execution window: one combined trip tonight or Saturday before practical pre-kickoff cutoff; do not chase -10.5 or worse.
- Massachusetts side: BET NOW CONDITIONAL remains. Accept only Massachusetts +4.5 or better at max -115. No newer qualified quote was recovered; actual Caesars offer must qualify. Same combined-trip rule; worse than +4.5 is PASS.
- Fresno State side: current public Fresno +6.5 does not meet the established +7 or better / max -115 threshold. State at this observed number: WAIT for actual Caesars comparison, with hard final execution cutoff 20:30 CT Saturday for the 21:30 CT kickoff. If +7 or better at max -115 is not available by cutoff, PASS; never chase +6.5.
- Georgia @ Alabama side and total: PASS remains. Hurricane risk is material, and the game remains scheduled; no raw weather/market disagreement earns a wager.
- Remaining 35 Saturday sides and all 38 Saturday totals remain PASS as persisted in the full dinner review. No new WAIT is created from silence or raw disagreement.
Portfolio/execution: no wager is established by this run. The three conditional singles are the only potential card and should share one practical trip; no third trip is justified. CFB_EXECUTION_LEDGER remains unchanged. Champion/FIRST_FROZEN unchanged.


## Saturday scheduled decision refresh — 2026-10-10 07:08 CT
Run: CFB_MARKET_MONITOR_20261010T120036Z. Linked Champion snapshot: accepted Champion v1.193 / FIRST_FROZEN v1.208. Qualified observation: canonical market append at 2026-10-10 07:03 CT, CBS Sports mixed-book public benchmark. Actual Caesars availability/executability remains UNVERIFIED; no execution is inferred.

- Appalachian State side: BET NOW CONDITIONAL — CONTROLLED BETA. Current public Appalachian State -9.5 (-115) qualifies against the established -10 or better, maximum -115 limit. Accept only an independently verified actual Caesars offer at -10 or better and no worse than -115. Reconciliation deadline is satisfied; practical final execution cutoff 11:00 CT for the 12:00 CT kickoff. Worse line/price => PASS; do not chase.
- Massachusetts side: BET NOW CONDITIONAL — CONTROLLED BETA. Current public Massachusetts +4.5 (-108) qualifies against the established +4.5 or better, maximum -115 limit. Accept only an independently verified actual Caesars offer at +4.5 or better and no worse than -115. Reconciliation deadline is satisfied; practical final execution cutoff 12:00 CT for the 13:00 CT kickoff. Worse line/price => PASS; do not chase.
- Fresno State side: WAIT resolves prospectively to BET NOW CONDITIONAL — CONTROLLED BETA. Current public Fresno State +7 (-110) reaches the established +7 or better, maximum -115 limit; the prior +6.5 WAIT is preserved as history. Accept only an independently verified actual Caesars offer at +7 or better and no worse than -115. Practical final execution cutoff remains 20:30 CT for the 21:30 CT kickoff. Worse line/price => PASS; do not chase.
- Remaining 35 Saturday sides and all 38 Saturday totals remain PASS. Fresh board movement alone is an investigation flag, not calibrated EV, and does not reopen resolved PASS decisions.
- Nebraska remains UNMODELED / no Champion-relative wager manufactured.

Portfolio/execution window: the three conditional singles are the only potential card. Prefer one combined practical trip before the earliest 11:00 CT cutoff; a later Fresno-only trip is not justified absent a documented compelling reason and a qualifying actual offer. No third trip. No wager is established by this refresh; CFB_EXECUTION_LEDGER remains unchanged. Champion/FIRST_FROZEN remains unchanged.


## Saturday 13:00 CT final reconciliation and execution-aware disposition — 2026-10-10 13:12 CT
Run: CFB_MARKET_MONITOR_20261010T180302Z. Linked Champion snapshot: accepted Champion v1.193 / FIRST_FROZEN v1.208. Market evidence: canonical 13:03 CT mixed-book fallback append, blob d25896f5eb476b2c70dae292d7e099627f0f528c. Consensus qualification: CONSENSUS_UNAVAILABLE for every governed game; current Caesars offer UNVERIFIED.

This is the required Saturday-evening decision boundary. No INCONCLUSIVE or WAIT is carried forward:
- Appalachian State side: prior BET NOW CONDITIONAL is now execution-complete for portfolio management. Canonical execution CFB_OCT09-03 records actual Appalachian State -10 (-110), $5. The numerical limit was satisfied. Game is underway; no duplicate wager and no later quote may reopen the decision.
- Massachusetts side: prior BET NOW CONDITIONAL is now execution-complete for portfolio management. Canonical execution CFB_OCT09-04 records actual Massachusetts +5 (-110), $5. The numerical limit was satisfied. Kickoff boundary has passed; no duplicate wager and no later quote may reopen the decision.
- Fresno State side: prior BET NOW CONDITIONAL is now execution-complete for portfolio management. Canonical execution CFB_OCT09-02 records actual Fresno State +7 (-113), $5, within the established +7 or better / max -115 limit. The later fallback +7.5 (-105) is not a verified current Caesars offer and does not justify a duplicate or chase.
- James Madison @ Georgia Southern: decision remains PASS / TOTAL PASS. Canonical execution CFB_OCT09-01 records an actual James Madison -7.5 (-107), $5 separately. Execution evidence does not rewrite the prospective PASS or manufacture prior recommendation attribution. No additional wager.
- Remaining 34 Saturday sides and all 38 Saturday totals remain PASS. Fresh mixed-book movement alone is not calibrated EV and does not reopen resolved decisions.
- Nebraska remains UNMODELED / no Champion-relative wager manufactured.

Portfolio disposition: four October 9 issued tickets are established executions totaling $20. No further casino trip or Saturday wager is recommended by this reconciliation. Current Caesars offers are unverified, all practical App State/UMass cutoffs are closed, Fresno is already executed, and a third trip is not justified. Settlements remain pending authoritative finals. Champion/FIRST_FROZEN unchanged.


## Week 7 Sunday opening decision capture — 2026-10-11 07:08 CT

**Cycle:** CFB_MARKET_MONITOR_20261011T120436Z  
**Governed boundary:** No accepted Week 7 frozen prediction exists yet. All games remain prospectively INCONCLUSIVE until accepted lineage and qualified decision inputs exist. No bet is forced. No acceptable line/price is established.  
**Portfolio:** No Week 7 trip or execution established; maintain approximately 1–2 casino trips/week and never chase.  
**Exactly-once:** governed slate 62; unique identities 62; section union 62; duplicates 0; exact-once PASS. Counts: TUESDAY 2, WEDNESDAY 2, THURSDAY 3, FRIDAY 3, SATURDAY MORNING 13, SATURDAY AFTERNOON 18, SATURDAY EVENING/NIGHT 21, UNRESOLVED KICKOFF 0.

| Kickoff CT | Game | State | Awaited information / decision relevance | Reconciliation deadline | Hard final execution cutoff | Acceptable number / price | Execution window |
|---|---|---|---|---|---|---|---|
| Tue Oct 13 6:00 PM CT | Delaware @ Middle Tenn. | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Tue Oct 13 1:00 PM CT | Tue Oct 13 5:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Tue Oct 13 7:00 PM CT | FIU @ Jacksonville St. | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Tue Oct 13 1:00 PM CT | Tue Oct 13 6:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Wed Oct 14 6:30 PM CT | Kennesaw St. @ Missouri St. | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Wed Oct 14 1:00 PM CT | Wed Oct 14 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Wed Oct 14 7:00 PM CT | W. Kentucky @ Sam Houston | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Wed Oct 14 1:00 PM CT | Wed Oct 14 6:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Thu Oct 15 6:30 PM CT | Ga. Southern @ Old Dominion | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Thu Oct 15 1:00 PM CT | Thu Oct 15 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Thu Oct 15 6:30 PM CT | East Carolina @ UAB | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Thu Oct 15 1:00 PM CT | Thu Oct 15 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Thu Oct 15 7:00 PM CT | Colorado St. @ Texas St. | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Thu Oct 15 1:00 PM CT | Thu Oct 15 6:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Fri Oct 16 6:30 PM CT | Memphis @ Tulane | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 1:00 PM CT | Fri Oct 16 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Fri Oct 16 7:00 PM CT | App. St. @ C. Carolina | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 1:00 PM CT | Fri Oct 16 6:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Fri Oct 16 7:00 PM CT | Washington @ Purdue | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 1:00 PM CT | Fri Oct 16 6:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Cincinnati @ West Virginia | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Florida @ Texas | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Virginia @ SMU | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Miss. State @ LSU | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Kansas @ Kansas State | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Northwestern @ Michigan St. | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Ohio State @ Indiana | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Charleston So. @ Clemson | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Ball St. @ Bowling Green | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Pittsburgh @ Boston College | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | Georgia St. @ James Madison | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:00 AM CT | FAU @ Army | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 11:30 AM CT | Rutgers @ Maryland | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Fri Oct 16 7:30 PM CT | Sat Oct 17 10:30 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 12:00 PM CT | Charlotte @ Temple | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 11:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 12:00 PM CT | UMass @ Buffalo | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 11:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 12:00 PM CT | The Citadel @ Texas A&M | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 11:00 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 12:30 PM CT | W. Michigan @ C. Michigan | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 11:30 AM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:00 PM CT | Nebraska @ Oregon | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | Arizona St. @ Texas Tech | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | Georgia Tech @ Virginia Tech | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | UNLV @ Air Force | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | N. Illinois @ Wyoming | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | Missouri @ Ole Miss | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | Akron @ Miami-OH | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | Alabama @ Tennessee | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | Auburn @ Georgia | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | Toledo @ E. Michigan | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | North Carolina @ Duke | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 2:30 PM CT | Penn State @ Michigan | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 1:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 3:30 PM CT | Tulsa @ Rice | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 2:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 4:00 PM CT | Troy @ Louisiana | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 7:00 AM CT | Sat Oct 17 3:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 5:00 PM CT | Washington St. @ Oregon State | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 4:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:00 PM CT | Florida State @ Miami (Fla.) | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:00 PM CT | Kent St. @ South Florida | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:00 PM CT | TCU @ Baylor | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:00 PM CT | Nevada @ N. Dakota St. | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:00 PM CT | Arkansas St. @ So. Miss | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:00 PM CT | Arkansas @ Vanderbilt | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:30 PM CT | Elon @ Stanford | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:30 PM CT | Wisconsin @ UCLA | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:30 PM CT | Louisville @ Syracuse | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:30 PM CT | Notre Dame @ BYU | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:30 PM CT | Kentucky @ Oklahoma | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 6:30 PM CT | Oklahoma State @ Houston | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 5:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 7:00 PM CT | Louisiana Tech @ UL-Monroe | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 6:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 7:00 PM CT | Navy @ UTSA | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 6:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 8:00 PM CT | San Jose St. @ UTEP | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 7:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 9:00 PM CT | Ohio @ Sacramento St. | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 8:00 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 9:15 PM CT | Utah @ Colorado | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 8:15 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 9:30 PM CT | Wake Forest @ California | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 8:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 9:30 PM CT | Fresno St. @ San Diego St. | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 8:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |
| Sat Oct 17 9:30 PM CT | New Mexico @ Hawaii | INCONCLUSIVE | Accepted frozen prediction; qualified multi-book benchmark; independently verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 8:30 PM CT | Not established | None until inputs are earned; at deadline transition to actionable, governed WAIT with explicit trigger, or PASS |


## Week 7 afternoon decision reconciliation — 2026-10-11 13:05 CT

**Cycle:** CFB_MARKET_MONITOR_20261011T180208Z  
**Outcome:** 62/62 games remain **INCONCLUSIVE** because an accepted Week 7 Champion/FIRST_FROZEN prediction is not yet earned, qualified multi-book consensus is unavailable, and an actual Caesars execution offer is unverified. No raw market move is converted into EV, confidence, or an actionable wager. No acceptable number/price is established. Production and $20 sandbox executions remain none for Week 7.  
**Portfolio control:** no trip is authorized; retain the approximately 1–2 trips/week objective and do not chase a later number.

### Prospective kickoff-clock correction

| Game | Prior carried kickoff | Authoritative current kickoff | State | Pending reason / next trigger | Reconciliation deadline | Hard final execution cutoff | Acceptable number / execution window |
|---|---|---|---|---|---|---|---|
| Nebraska @ Oregon | Sat Oct 17 2:00 PM CT (07:08 capture; now superseded prospectively) | Sat Oct 17 10:00 PM CT — Oregon athletics announcement, 8:00 PM PT on FOX | INCONCLUSIVE | Accepted frozen prediction plus qualified benchmark or verified Caesars offer; availability/weather as relevant | Sat Oct 17 1:00 PM CT | Sat Oct 17 9:00 PM CT | Not established; no execution before inputs are earned |

All other governed Week 7 game states, triggers, reconciliation deadlines, and hard cutoffs are unchanged from the 07:08 CT opening capture. Tuesday games remain due for reconciliation Tuesday 13:00 CT; INCONCLUSIVE may not drift beyond its applicable deadline.


## Week 7 FIRST_FROZEN lineage clarification — 2026-10-11 14:29 CT

Original September26 accepted artifact10897612260 (ZIP 772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf) covers all62 currentWeek7 targets:51 immutable FIRST_FROZEN predictions and11 explicit original exclusions. This prospectively corrects the earlier blanket no-accepted-Week7-FIRST_FROZEN claim; historical statements remain preserved. All4Tuesday/Wednesday games have original predictions. Historical Challenger B is the active Beta Production Champion under v1.222, not a different model.

Accepted October6 REFRESH artifact11423386216 (ZIP 674501a82f6eb207b58b30c483910304c881b3ce29ba2506258152455cb6047b) covers61 predictions+1 exclusion, including10 targets excluded in the original snapshot. REFRESH never substitutes for or rewrites original predictions/exclusions. The upcoming Monday readiness/Tuesday candidate is a separate weekly-cycle dependency, not the existence test for original accepted predictions.

All62 decision dispositions remain INCONCLUSIVE; acceptable numbers/prices remain not established. No bet, trip, execution or confidence is authorized. Qualified consensus/current Caesars and material availability remain unresolved.51 rows can display accepted original numbers;11 original exclusions stay explicit. Current schedule and historical model clocks remain separate. Existing saved reconciliation/cutoff values are retained only as planning information: CUTOFF_AUTHORITY_UNVERIFIED; effective practical provenance remains unresolved. No deadline is relaxed or invented.

## Week 7 Monday decision reconciliation — 2026-10-12 07:07 CT

**Cycle:** CFB_MARKET_MONITOR_20261012T120147Z  
**State:** 62/62 remain **INCONCLUSIVE**. Accepted original FIRST_FROZEN is available for 51 games and 11 retain explicit original exclusions; no model value is reconstructed or replaced by the October 6 REFRESH. The Monday live public board produced 55 identified DraftKings fallback observations and seven current-quote unavailabilities, but no qualified multi-book consensus, independently verified Caesars offer, or practical execution-access authority. Raw disagreement is only an investigation flag. No acceptable number/price, wager, trip, or confidence was earned.  
**WAIT integrity:** no WAIT exists and none was rolled forward. No practical final cutoff is independently qualified; retained saved clocks remain planning times with CUTOFF_AUTHORITY_UNVERIFIED and are not relaxed or promoted.  
**Portfolio:** production and separate $20 sandbox Week 7 exposures remain zero. No casino trip is authorized; retain the approximately 1–2 trips/week objective and never chase.

| Nearest game | State | Pending reason / awaited information | Decision relevance / opportunity at risk | Reconciliation deadline | Retained planning cutoff | Acceptable number / execution window |
|---|---|---|---|---|---|---|
| Delaware @ Middle Tennessee | INCONCLUSIVE | Qualified multi-book benchmark; verified Caesars offer; material availability; practical access | Original FIRST_FROZEN exists; DraftKings fallback shows Delaware -2.5 -110 / Middle Tennessee +2.5 -110 and total 47.5, but no calibrated EV | Tue Oct 13 1:00 PM CT | Tue Oct 13 5:00 PM CT; CUTOFF_AUTHORITY_UNVERIFIED | Not established; at deadline transition prospectively to earned actionable state, governed WAIT with explicit trigger and hard cutoff, or PASS |
| FIU @ Jacksonville State | INCONCLUSIVE | Qualified multi-book benchmark; verified Caesars offer; material availability; practical access | Original FIRST_FROZEN exists; DraftKings fallback shows FIU +3 -112 / Jacksonville State -3 -108 and total 43.5, but no calibrated EV | Tue Oct 13 1:00 PM CT | Tue Oct 13 6:00 PM CT; CUTOFF_AUTHORITY_UNVERIFIED | Not established; at deadline transition prospectively to earned actionable state, governed WAIT with explicit trigger and hard cutoff, or PASS |

All remaining 60 governed games preserve their already-recorded game-specific reconciliation deadlines and retained planning cutoffs. INCONCLUSIVE may not drift beyond those deadlines; no bet is forced merely to eliminate it.

## Week 7 Monday afternoon decision reconciliation — 2026-10-12 13:05 CT

**Cycle:** CFB_MARKET_MONITOR_20261012T180232Z  
**State:** 62/62 remain **INCONCLUSIVE**. The repository Monday source-readiness workflow passed its no-prediction source preflight, but that is not a new model snapshot or acceptance. The afternoon DraftKings public view exposed eight governed games: five internally coherent single-book fallback observations and three spread/moneyline direction conflicts withheld from current decision evidence. Qualified multi-book consensus and independently verified Caesars remain unavailable for every game. No raw disagreement is treated as EV, confidence, or an automatic bet.  
**WAIT integrity:** no WAIT exists and none was rolled forward. No acceptable number/price, trip, production wager, or separate $20 sandbox wager was established. Retained practical cutoffs remain CUTOFF_AUTHORITY_UNVERIFIED.  
**Portfolio:** no casino trip is authorized. Preserve the approximately 1–2 trips/week objective and do not chase.

| Nearest game | State | Current qualified fallback used | Withheld/awaited information | Decision relevance / opportunity at risk | Reconciliation deadline | Retained planning cutoff | Acceptable number / execution window |
|---|---|---|---|---|---|---|---|
| Delaware @ Middle Tennessee | INCONCLUSIVE | Retain Monday 07:07 CT DraftKings: Delaware -2.5 -110 / Middle Tennessee +2.5 -110; total 47.5; ML -135/+114 | 13:05 observation withheld for side/ML favorite-direction conflict; qualified consensus; verified Caesars; availability; practical access | Original FIRST_FROZEN exists; movement cannot be certified from conflicted fields | Tue Oct 13 1:00 PM CT | Tue Oct 13 5:00 PM CT; CUTOFF_AUTHORITY_UNVERIFIED | Not established; at deadline transition to earned actionable state, governed WAIT with explicit trigger and hard cutoff, or PASS |
| FIU @ Jacksonville State | INCONCLUSIVE | DraftKings 13:05 CT: FIU +3 -115 / Jacksonville State -3 -105; total 43.5; ML +120/-142 | Qualified consensus; verified Caesars; availability; practical access | Original FIRST_FROZEN exists; single-book fallback alone is insufficient for calibrated action | Tue Oct 13 1:00 PM CT | Tue Oct 13 6:00 PM CT; CUTOFF_AUTHORITY_UNVERIFIED | Not established; at deadline transition to earned actionable state, governed WAIT with explicit trigger and hard cutoff, or PASS |

All remaining 60 governed games retain their recorded reconciliation deadlines and cutoffs. Five coherent afternoon fallback observations update comparison context only; three conflicted observations do not. INCONCLUSIVE may not drift beyond its applicable deadline, and no bet is forced.


```cfb-neutral-decision-v1
{
  "schema": "CFB_NEUTRAL_DECISION_PRESENTATION_V1",
  "cycle_id": "CFB_MARKET_MONITOR_20261013T115928Z",
  "as_of_utc": "2026-10-13T12:09:29Z",
  "rows": [
    {
      "game_id": "401871067",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; Tuesday weather forecast clear, no qualified official availability change located, consensus unavailable, Caesars unverified, and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-13T18:00:00Z",
      "planning_cutoff_utc": "2026-10-13T22:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401871053",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; Tuesday weather forecast clear, no qualified official availability change located, consensus unavailable, Caesars unverified, and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-13T18:00:00Z",
      "planning_cutoff_utc": "2026-10-13T23:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401871054",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-14T18:00:00Z",
      "planning_cutoff_utc": "2026-10-14T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401871068",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-14T18:00:00Z",
      "planning_cutoff_utc": "2026-10-14T23:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401869950",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-15T18:00:00Z",
      "planning_cutoff_utc": "2026-10-15T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401862800",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-15T18:00:00Z",
      "planning_cutoff_utc": "2026-10-15T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401860923",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-15T18:00:00Z",
      "planning_cutoff_utc": "2026-10-15T23:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401862801",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-16T18:00:00Z",
      "planning_cutoff_utc": "2026-10-16T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401869844",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-16T18:00:00Z",
      "planning_cutoff_utc": "2026-10-16T23:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858493",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-16T18:00:00Z",
      "planning_cutoff_utc": "2026-10-16T23:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856724",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858268",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856720",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856830",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856829",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401869957",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858267",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401862802",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858491",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401866441",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858261",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858488",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858489",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T00:30:00Z",
      "planning_cutoff_utc": "2026-10-17T15:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401862803",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T16:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856725",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T16:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401866442",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T16:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401866443",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T16:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858264",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401864522",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401864524",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856828",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856721",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858490",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856723",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856719",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401866444",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858266",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401866478",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T18:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401862805",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T19:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401869966",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-17T20:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401860903",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T21:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858263",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401862806",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856832",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401864520",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401869934",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856726",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858262",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858494",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858265",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856809",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856722",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856831",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T22:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401871091",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T23:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401862804",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-17T23:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401864523",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-18T00:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401866445",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-18T01:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401856833",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-18T01:15:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858269",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-18T01:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401860904",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-18T01:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401864521",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T18:00:00Z",
      "planning_cutoff_utc": "2026-10-18T01:30:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    },
    {
      "game_id": "401858492",
      "state": "INCONCLUSIVE",
      "reason": "Current full-slate CBS mixed-book fallback captured; consensus unavailable, Caesars unverified, material availability and practical access unresolved; no actionable number earned",
      "reconciliation_utc": "2026-10-17T12:00:00Z",
      "planning_cutoff_utc": "2026-10-18T02:00:00Z",
      "cutoff_authority": "UNVERIFIED",
      "acceptable_number": null,
      "execution_window": null
    }
  ]
}
```


## Tuesday deadline reconciliation — 2026-10-13 13:04 CT

**Cycle:** CFB_MARKET_MONITOR_20261013T180204Z  
**Authority boundary:** Prospective decision at the scheduled 13:00 CT reconciliation point. Frozen predictions remain unchanged. The current board is an unidentified CBS mixed-book fallback; qualified consensus is unavailable and actual Caesars execution is unverified. Raw model/market disagreement is not calibrated EV.

| Game | State transition | Current fallback | Reason / awaited information | Acceptable number / price | Execution window |
|---|---|---|---|---|---|
| Delaware @ Middle Tennessee | INCONCLUSIVE → PASS | Delaware -1 (-111), ML -114; Middle Tennessee +1.5 (-114), ML -104; total 47.5 (-114/-105) | No qualified consensus, no verified Caesars offer, no established actionable threshold, and Delaware QB Nick Minicucci's lower-body availability remains decision-relevant. The earned conservative disposition is no bet; do not reopen from price movement alone. | Not established | CLOSED — no production or sandbox wager; no casino trip |
| FIU @ Jacksonville State | INCONCLUSIVE → PASS | FIU +3 (-110), ML +128; Jacksonville State -2.5 (-124), ML -148; total 43.5 (-110/-108) | Frozen Jacksonville State -4.5 versus fallback -2.5 is only a raw investigation flag. Consensus, Caesars executability, and calibrated EV remain unavailable; no governed threshold was earned. | Not established | CLOSED — no production or sandbox wager; no casino trip |

**Portfolio:** Week 7 production exposure remains $0; separate $20 sandbox exposure remains $0. No trip is authorized for Tuesday. The remaining 60 games retain their already assigned prospective reconciliation deadlines; no other state is changed by this append.


## Wednesday morning pre-deadline reconciliation — 2026-10-14 07:04 CT

**Cycle:** CFB_MARKET_MONITOR_20261014T120046Z  
**Authority boundary:** Prospective review before the governed 13:00 CT Wednesday reconciliation deadline. Frozen predictions remain unchanged. The refreshed board is an unidentified CBS mixed-book fallback; qualified consensus is unavailable and actual Caesars execution is unverified. Raw model/market disagreement is not calibrated EV.

| Game | State | Current fallback | Reason / awaited information | Next trigger and hard cutoff | Acceptable number / execution window |
|---|---|---|---|---|---|
| Kennesaw State @ Missouri State | INCONCLUSIVE (retained) | Kennesaw State -3 (-108), ML -154; Missouri State +3.5 (-122), ML +136; total 52.5 (-105/-114) | Consensus unavailable; Caesars unverified; no governed acceptable number or price earned. Official preview supplied no qualified new scratch/QB change. Springfield weather is cloudy near kickoff with later thunderstorm risk, which remains monitoring evidence only. | Reconcile at 2026-10-14T18:00:00Z; no drift beyond that point. If still unqualified, transition prospectively to governed WAIT with an explicit trigger and hard cutoff or PASS. Planning cutoff 2026-10-14T22:30:00Z. | Not established; no executable recommendation before the deadline |
| Western Kentucky @ Sam Houston | INCONCLUSIVE (retained) | Western Kentucky -1.5 (-110), ML -122; Sam Houston +1.5 (-108), ML +105; total 52.5 (-110/-108) | Favorite flip from the preserved opening fallback is an investigation flag only. Consensus unavailable; Caesars unverified; no governed acceptable number or price earned. Official preview supplied no qualified new scratch/QB change. | Reconcile at 2026-10-14T18:00:00Z; no drift beyond that point. If still unqualified, transition prospectively to governed WAIT with an explicit trigger and hard cutoff or PASS. Planning cutoff 2026-10-14T23:00:00Z. | Not established; no executable recommendation before the deadline |

**Portfolio:** Week 7 production exposure remains $0; separate $20 sandbox exposure remains $0. No morning casino trip is authorized. The 58 other unresolved games retain their assigned prospective reconciliation deadlines, and the two Tuesday games remain PASS. No Champion/FIRST_FROZEN/REFRESH field changed.


## Wednesday deadline reconciliation — 2026-10-14 13:00 CT

**Cycle:** CFB_MARKET_MONITOR_20261014T175552Z  
**Authority boundary:** Prospective decision at the governed Wednesday reconciliation deadline. Frozen predictions remain unchanged. The refreshed board is an unidentified CBS mixed-book fallback; qualified consensus is unavailable and actual Caesars execution is unverified. Raw model/market disagreement is not calibrated EV.

| Game | State transition | Current fallback | Reason / awaited information | Acceptable number / price | Execution window |
|---|---|---|---|---|---|
| Kennesaw State @ Missouri State | INCONCLUSIVE → PASS | Kennesaw State -2.5 (-111), ML -140; Missouri State +2.5 (-105), ML +120; total 52.5 (-110/-105) | No qualified consensus, no verified Caesars offer, and no governed acceptable threshold was earned. Missouri State quarterback uncertainty and late weather risk add uncertainty rather than a usable edge. The earned disposition is no bet; do not reopen from price movement alone. | Not established | CLOSED — no production or sandbox wager; no casino trip |
| Western Kentucky @ Sam Houston | INCONCLUSIVE → PASS | Western Kentucky -1 (-111), ML -115; Sam Houston +1.5 (-114), ML +102; source-rendered over 52.5 (-111) / under 53.5 (-112) | Frozen Sam Houston -36.5 versus a near-pick'em fallback is a severe raw disagreement and likely model-risk signal, not calibrated EV. The asymmetric displayed total, unavailable consensus, unverified Caesars offer, and absent governed threshold prohibit action. | Not established | CLOSED — no production or sandbox wager; no casino trip |

**Portfolio:** Week 7 production exposure remains $0; separate $20 sandbox exposure remains $0. No Wednesday trip is authorized. The remaining 58 active games retain their assigned prospective reconciliation deadlines; the two Tuesday and two Wednesday games are now PASS. No Champion/FIRST_FROZEN/REFRESH field changed.


## Wednesday Evening Availability Thursday carry-forward — 2026-10-14 20:16 CT

**Cycle:** CFB_EVENING_AVAILABILITY_20261015T011649Z  
**Authority boundary:** Downstream prospective reassessment from the latest canonical afternoon state. Fresh full-board capture is an unidentified field-level mixed-book fallback; qualified consensus is unavailable, actual Caesars is unverified, and no offer is executable. Original FIRST_FROZEN and accepted REFRESH remain unchanged and separate.

| Game | State transition | Current fallback | Decision relevance / pending information | Acceptable number / price | Next trigger and hard final cutoff | Execution window |
|---|---|---|---|---|---|---|
| East Carolina @ UAB | INCONCLUSIVE → PASS | East Carolina -4.5 (-114), ML -200; UAB +5.5 (-112), ML +170; total 47.5 (-106/-110) | Original FIRST_FROZEN is EXCLUDED because home-prior points were missing. The October 6 REFRESH is not substituted. With no frozen Champion prediction, qualified consensus, verified Caesars offer or governed threshold, no production or sandbox wager can be earned. Do not reopen from price movement alone. | Not established | CLOSED prospectively; no later than the Thursday 13:00 CT reconciliation | CLOSED — no wager and no trip |
| Georgia Southern @ Old Dominion | INCONCLUSIVE → INCONCLUSIVE | Georgia Southern -3.5 (-108), ML -172; Old Dominion +3.5 (-108), ML +150; total 47.5 (-110/-108) | Original frozen opinion is Old Dominion -1.2 / 41.1 / 0.476 home. Raw spread/total disagreement is an investigation flag, not EV. Await an identified qualified consensus or independently verified actual Caesars offer plus material official availability; none exists tonight. | Not established | Thursday 13:00 CT reconciliation: transition to actionable, governed WAIT with explicit trigger, or PASS. Any WAIT must finally resolve by 17:30 CT, one hour before kickoff. | No trip tonight. Earliest realistic execution is a combined Thursday trip after 13:00 CT only if an acceptable number is prospectively earned; otherwise PASS |
| Colorado State @ Texas State | INCONCLUSIVE → PASS | Colorado State +14.5 (-112), ML +475; Texas State -14 (-115), ML -599; total 69.5 (-111/-108) | Original frozen opinion is Colorado State -2.4 / 63.4 / 0.456 home while the fallback makes Texas State roughly a two-touchdown favorite. This extreme reversal is a model-risk investigation flag, not calibrated EV. No qualified consensus, verified Caesars offer or acceptable threshold exists. Do not force a side or total. | Not established | CLOSED prospectively; no later than the Thursday 13:00 CT reconciliation | CLOSED — no wager and no trip |

**Portfolio result:** No Wednesday-night trip. Week 7 production exposure remains $0 and separate Week 7 sandbox exposure remains $0. Current state becomes 56 INCONCLUSIVE and 6 PASS. The one remaining Thursday INCONCLUSIVE has a Thursday 13:00 CT reconciliation deadline and a hard 17:30 CT final execution cutoff if a governed WAIT is earned. No acceptable number, price, EV, probability or confidence was invented. No Champion/FIRST_FROZEN/REFRESH field changed.


## Thursday 13:00 CT reconciliation — 2026-10-15

**Cycle:** CFB_MARKET_MONITOR_20261015T175838Z  
**Prospective boundary:** 2026-10-15T18:00:00Z. The established Thursday reconciliation deadline is reached. No current observation below is qualified multi-book consensus and no actual Caesars offer is independently verified. No acceptable number/price has been established. Market/model disagreement is not calibrated EV.

| Game | Prospective state | Current fallback evidence | Reason / awaited information | Acceptable number / price | Next trigger / hard cutoff | Execution window |
|---|---|---|---|---|---|---|
| Georgia Southern @ Old Dominion | PASS | Georgia Southern -3 (-111), ML -156; Old Dominion +3.5 (-118), ML +140; o46.5 (-106) / u46.5 (-110) | The deadline arrived without identified three-book consensus, verified Caesars execution, or a governed acceptable threshold. Frozen Old Dominion -1.2 / 41.1 / 0.476 home remains immutable; disagreement is a model-risk flag only. No governed WAIT trigger was earned. | Not established | CLOSED prospectively at the 13:00 CT reconciliation; do not chase later movement | CLOSED — no wager and no trip |
| East Carolina @ UAB | PASS reaffirmed | East Carolina -5.5 (-110), ML -213; UAB +5.5 (-108), ML +180; o48.5 (-105) / u48.5 (-114) | Prior PASS remains controlling. The new mixed-book fallback does not establish consensus, Caesars execution, or an acceptable threshold. | Not established | CLOSED | CLOSED — no wager and no trip |
| Colorado State @ Texas State | PASS reaffirmed | Colorado State +14.5 (-105), ML +475; Texas State -14.5 (-110), ML -625; o70.5 (-110) / u70.5 (-105) | Prior PASS remains controlling. The extreme frozen/market disagreement remains an investigation flag, not calibrated EV; no qualified consensus, verified Caesars offer, or acceptable threshold exists. | Not established | CLOSED | CLOSED — no wager and no trip |

**Portfolio result:** All three Thursday games are PASS / NO BET. No Thursday trip is authorized. Week 7 production exposure remains $0 and separate Week 7 sandbox exposure remains $0. Current state becomes 55 INCONCLUSIVE and 7 PASS. Friday is now the earliest active chronological section. No acceptable number, price, EV, probability or confidence was invented. No Champion/FIRST_FROZEN/REFRESH field changed.
