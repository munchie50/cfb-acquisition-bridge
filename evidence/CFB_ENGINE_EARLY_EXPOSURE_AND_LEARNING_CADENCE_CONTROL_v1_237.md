# CFB Engine - Early Exposure and Learning Cadence Control v1.237

Status: ACTIVE DEVELOPMENT / BETA CADENCE CONTROL
Date: 2026-09-26
Parents: v1.227, v1.229, v1.231, v1.233, v1.235, v1.236

## Purpose
Prevent promising betting or decision layers from remaining hidden behind elapsed time, undefined confidence, or indefinite research status. Controlled real-world observation should begin as soon as a candidate can be stated honestly and measured safely.

## Core principle
Time itself is not evidence. A layer must not remain silent for weeks merely because it is new or imperfect. Once a candidate method has enough definition to produce a reproducible, timestamped, auditable output, begin exposing its outputs at the highest authority level actually earned.

Early exposure does not mean falsely calling an unvalidated idea production-grade. Use explicit maturity labels so observation and learning can begin before full confidence is earned.

## Output maturity ladder
A candidate may surface as:
1. OBSERVATION ONLY - measurable signal, insufficient basis for a recommendation.
2. EXPERIMENTAL LEAN - directional candidate with stated uncertainty; track prospectively.
3. CONTROLLED BETA RECOMMENDATION - defined rule/logic and sufficient safeguards for controlled real-world use, with confidence/uncertainty shown.
4. PRODUCTION-QUALIFIED RECOMMENDATION - earned under applicable acceptance/promotion authority.

Do not suppress levels 1-3 merely because level 4 has not been earned.

## Recommendation cadence
Once a layer reaches EXPERIMENTAL LEAN or CONTROLLED BETA RECOMMENDATION, it should continue producing prospective outputs on each applicable weekly cycle unless a documented blocker makes the output invalid. Preserve every output before outcomes. Evaluate it afterward. Silence requires a reason, not merely low confidence.

Confidence need not be 100 percent. Show uncertainty honestly. Where numeric confidence is not calibrated, use a descriptive evidence state rather than inventing a percentage.

## Parlay layer
Parlay research should move toward early prospective exposure rather than remaining dormant for an entire season. As soon as candidate parlay construction logic is defined and auditable, surface experimental parlay candidates prospectively on the Hot Sheet with clear maturity labels, constituent legs, prices when qualified, known correlation considerations, uncertainty, rationale, and whether each leg independently survives its own betting-layer screen.

Do not manufacture parlay EV by multiplying uncalibrated probabilities or assuming independence. Until calibration/price/correlation authority is earned, label candidates accordingly. Controlled real-money use, if chosen, remains distinguishable from production-qualified recommendation and must be recorded as execution evidence rather than retroactively validating the method.

## Other time-hidden layers
Sunday QA must inspect active and roadmap layers for TIME-HIDDEN status: a useful candidate exists but outputs are being withheld mainly because no explicit exposure threshold/cadence was defined. For each such layer, either define the smallest safe prospective exposure, document the concrete blocker and evidence needed, or retire/defer it with rationale. Do not permit indefinite WAIT/RESEARCH by default.

This applies to parlay/correlation, moneyline-versus-spread expression, totals expression, alternative-line/price tradeoffs, uncertainty, edge calibration, market-disagreement decomposition, timing thresholds, book dispersion, staking/portfolio work, and future layers as applicable.

## Learning through controlled use
Observation and controlled prospective use are legitimate ways to learn when authority and uncertainty are explicit. Preserve candidate output, decision, execution if any, market/price context, close where qualified, outcome, and post-event assessment separately. A win does not validate a method; a loss does not invalidate it. Accumulated prospective evidence informs the next governed step.

## Guardrails
- No automatic Champion mutation.
- No outcome-informed reconstruction of earlier recommendations.
- No invented probability, EV, confidence percentage, correlation, or price semantics.
- No promotion merely because outputs are now visible.
- No requirement for perfect confidence before observation or controlled Beta exposure.
- Real-money execution does not substitute for scientific acceptance.
- Material safety/source/semantic blockers remain fail-closed.

## Weekly reporting
Weekly Beta Review must identify: newly exposed candidate layers; their maturity state; outputs produced; confidence/uncertainty; what was learned; layers still hidden; exact reason each remains hidden; and the next evidence/action required to expose it.

Scientific effect: none by itself. This control accelerates transparent prospective learning while preserving existing model, evidence, calibration and promotion boundaries.

## Kickoff-window reconciliation deadlines — 2026-09-29
INCONCLUSIVE is a temporary investigation state, not an indefinite destination. Every INCONCLUSIVE game must carry a prospective reconciliation deadline tied to its kickoff window and practical execution needs.

Default America/Chicago deadline windows:
- THURSDAY games: reconcile by the final scheduled Market Monitor pass that leaves a practical pre-kickoff execution opportunity; if the ordinary 13:00 CT pass is safely pre-kickoff, use it as the default decision deadline, otherwise use the last earlier governed pass.
- FRIDAY games: default reconciliation deadline Friday 13:00 CT, unless kickoff/execution constraints require an earlier governed pass.
- SATURDAY MORNING games (kickoff before 12:00 CT): default reconciliation deadline Friday evening availability review; if no Friday evening run is applicable, use the last Friday Market Monitor pass.
- SATURDAY AFTERNOON games (12:00–16:59 CT): default reconciliation deadline Saturday 07:00 CT Market Monitor.
- SATURDAY EVENING/NIGHT games (17:00 CT or later): default reconciliation deadline Saturday 13:00 CT Market Monitor.

These are decision-reconciliation deadlines, not automatic bet triggers and not promises that a particular sportsbook remains executable. A game-specific earlier deadline must be used when kickoff, travel, sportsbook access, line availability, or the portfolio execution plan makes the default too late.

At the reconciliation deadline:
- INCONCLUSIVE may not simply roll forward because research remains imperfect.
- If governed evidence supports action, transition prospectively to BET NOW or other earned actionable state.
- If a specific unresolved condition can still mature before a genuine later execution cutoff, WAIT is allowed only with an explicit trigger, opportunity at risk, next review, and hard final execution cutoff.
- If evidence is insufficient to justify action and no governed WAIT condition remains, transition to PASS.
- Never force a bet merely to eliminate INCONCLUSIVE.

At the game's final practical execution cutoff, WAIT must resolve to an earned actionable state or PASS. Preserve every transition append-only; never rewrite the earlier INCONCLUSIVE/WAIT record.

Decision deadlines must coordinate with the portfolio objective of roughly 1–2 casino trips per week. Kickoff windows organize research and decision maturity; they do not independently create five execution trips.

Scientific effect: none. This is downstream decision-cadence governance only and cannot alter frozen Engine predictions or admit market/injury/wager/outcome information into the model.


## Practical-trip full-scope enforcement clarification — October 9, 2026

This operational clarification enforces the existing earlier-practical-constraint rule; default clocks and recommendation/model authority are unchanged.

At authority recovery, recover the latest explicit user execution/travel/sportsbook constraint and prospective canonical decision context BEFORE ranking candidates or choosing the next default review. A stated need to bet tonight for tomorrow requires review of every requested remaining modeled game/window and each requested market, including earlier PASS rows at their preserved earned state. A ranked watchlist is not full evaluation. Declare expected scope, reconcile identity union/unique cardinality, retain separate side/total verdicts and row-specific rationale/qualification; render ranked recommendations separately. Include required unmodeled exclusions without manufacturing forecasts.

Effective deadline is the earliest independently established default, practical trip deadline and final execution cutoff. Later access cannot relax an earlier default/cutoff; unknown exact access time remains unknown. An immediate user request is an immediate manual work priority, not permission to invent a historical pre-trip time, backfill decisions, dispatch another task or guarantee a scheduled job ran. If the default next run is after known opportunity, do not defer current user-directed work to it; record the scheduling/enforcement gap explicitly. Never infer actual sportsbook availability from quote retrieval, or let earlier timing force a bet, lower maturity safeguards, loosen a cutoff, rewrite earlier PASS or leak outcomes into pregame state.

Before a full-review/card coverage claim, apply scripts/cfb_full_review_scope_gate.py when its qualified Week6 schema/runtime is applicable, or independently perform the exact declared identity/market/rationale reconciliation. Unknown/future schema requires separate qualification, not coercion. This helper certifies structural coverage only, not football research completeness, quote truth, final roster, execution or decision quality. Deadline utility composes supplied timezone-aware clocks; it does not establish their source authority. Known source/football blockers remain explicit per row; controlled Beta can still surface with documented uncertainty under the existing maturity ladder.

Proof: evidence/scheduler_qa/CFB_FULL_SATURDAY_SCOPE_AND_TRIP_DEADLINE_GUARD_2026-10-09.md, blob af73e23d60731aeff36bcb915252a240378a36a0;16local regression cases, actual narrow report rejection/full38report structuralPASS, existing GitHubrun38011828740/job114093326128success, immutable/main source/workflowreadbacks. Current3conditional recommendations unchanged; actualCaesars/finalavailability unverified. Clarification is installed; natural MarketMonitor/Evening consumer enforcement remains DEMONSTRATION_PENDING. No schedule/task creation/cadence change, ProductionRoutinev5promotion or scientific acceptance.
