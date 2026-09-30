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
