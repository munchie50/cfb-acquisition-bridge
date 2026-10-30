# CFB Engine — Continuous Edge Discovery and Autonomous Learning Mandate
Date: 2026-10-30
Status: USER-DIRECTED STANDING REQUIREMENT; IMPLEMENTATION AND ACCEPTANCE PENDING
Scope: CFB production observation, QA research, and governed improvement. This record does not modify the frozen Champion, staking, schedules, or existing contracts.

## User objective
The engine must proactively learn to identify both operational weaknesses and evidence-backed betting edges that may improve real-world wagering outcomes. Do not limit learning to fixing failures or to wagers the user placed. Examine the full eligible slate, including PASS, conditional, and excluded cases with explicit eligibility accounting.

## Two parallel learning tracks
1. Operational autonomy: detect recurring failures, omissions, data bottlenecks, delayed decisions, inefficient retrieval, missing market/parlay outputs, and preventable manual interventions. Diagnose root causes, test the smallest safe fix, independently verify persistence and regression behavior, and record whether the change actually helped.
2. Betting-edge discovery: systematically examine predictions, actual independent game outcomes, frozen pregame snapshots, line/price movements, spread/total/moneyline and available derivative markets, matchup features, injuries and personnel uncertainty, passes, timing, and parlay construction. Form explicit testable hypotheses; compare with baselines, alternative explanations, and full-slate counterfactuals. Evaluate calibrated probabilities where qualified, price-aware net results, uncertainty, closing-line value where qualified, and out-of-sample robustness. Track false edges and negative findings too.

## Required persistent evidence per pattern
- Pattern ID, discovery date, affected games/seasons/markets, source provenance and sample size.
- Objective symptom, hypothesis, suspected mechanism, confounders, and possible selection bias.
- Proposed change, risk class, reproducible experiment, historical split and prospective shadow validation.
- Results including uncertainty, market-price and margin effects, comparisons to current frozen Champion, and adverse cases.
- Decision: monitor, reject, iterate, QA candidate, accepted operational repair, or governed production promotion.
- Owner/next action, checkpoint, supersession, and recheck trigger; avoid repeated investigation of closed issues without new evidence.

## Execution behavior
- At every relevant QA cycle, inspect the improvement register for open hypotheses, repeated failure patterns, newly available outcomes, and untested opportunity classes. Add newly discovered patterns proactively; don't wait for user prompting.
- At every applicable Hot Sheet cycle, verify required coverage and market/parlay evaluation outputs. Missing output is an explicit incomplete or bounded blocker, never silent success. An output-section detector alone is not substantive decision validation.
- Distinguish observed data, candidate edge, verified edge, experimental recommendation, executable venue-verified wager, and actual user execution.
- Preserve user's limited weekly execution trips and prospective decision cutoffs.
- Tickets are execution evidence, never Champion training inputs. No fabricated probabilities, offered prices, results, or model confidence.
- Frozen production Champion and active contracts retain authority. No unapproved model, threshold, staking, bankroll, scheduling, or production authority change. Reconcile independently before promotion.
- Keep exactly four established production scheduled tasks; integrate analysis into existing QA/health workflows where authorized rather than creating a fifth task.
- If automation cannot run unattended, state that limitation and persist the precise next action. A saved mandate is not proof that a scheduler has been updated.

## Success measures
Coverage completeness, omission recurrence, recovery time, decision timeliness, data spend, prospective calibration, qualified closing-line value, risk-adjusted price-aware returns, out-of-sample performance, and false-discovery/rejected-hypothesis tracking. A higher win rate alone is insufficient.

## Next implementation gates
1. Add an append-only improvement/pattern register with statuses and evidence pointers.
2. Wire bounded pattern scans and missing-output checks into existing weekly QA and relevant monitor routines; test with historical failures and new negative cases.
3. Add reproducible full-slate outcome and price-aware hypothesis evaluation, prospective shadow tracking, and promotion criteria.
4. Independently test, read back, and document the first complete detect -> diagnose -> test -> verify -> learn cycle. Do not claim autonomy before demonstrated execution.
