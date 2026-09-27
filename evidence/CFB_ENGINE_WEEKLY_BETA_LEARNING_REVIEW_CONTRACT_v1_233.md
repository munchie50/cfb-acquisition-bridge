# CFB Engine - Weekly Beta Learning Review Contract v1.233

Status: ACTIVE WEEKLY LEARNING OUTPUT CONTROL
Date: 2026-09-26
Parents: v1.224, v1.226, v1.227, v1.229, v1.231, v1.232

## Purpose
After Sunday CFB QA and Q&A, produce one authoritative Weekly Beta Learning Review that becomes durable development evidence for future CFB builds, Challenger initialization, redesigns, and maturity reviews. It is not merely a recap.

Future material CFB development must consult accumulated Weekly Beta Learning Reviews plus unresolved learning-ledger items. Applicable lessons must be incorporated and tested, explicitly deferred with rationale, or explicitly found not relevant. They may not silently disappear.

## Required review sections
1. Executive state: accepted Beta Champion lineage, data cutoff/freshness, FIRST_FROZEN/refresh/exclusion/fail-closed accounting, unresolved authority/data issues.
2. Prediction assessment: margin/total/win-probability performance, meaningful slices where supported, major misses and strengths, bias/error patterns, and variance versus potentially systematic evidence without forced diagnosis.
3. Game-level learning: frozen prediction, result, error direction/magnitude, relevant matchup/game characteristics, possible feature/data/model/chronology implications, and unresolved cases.
4. Champion-versus-market: blind Champion view, first qualified market observation, movement, qualified close where available, disagreement direction/magnitude, movement toward/away from Champion, and CLV only when qualified.
5. Betting/decision assessment: BET EARLY/BET NOW/WAIT/PASS, minimum acceptable number, timing, actual execution when established, no-bet decisions, qualified CLV, and outcome last. Prediction, selection, timing, execution, and outcome remain separate.
6. Real-world Beta failures: source, freshness, timing, execution, schedule, exclusion, workflow, screenshot ambiguity, conflicting-input and other operational friction; state whether controls caught each issue and the consequence.
7. Exclusion/fail-closed learning: why exclusions occurred, whether exclusion was correct, recurring coverage weaknesses, and possible safe improvements.
8. Challenger/Sandbox findings: hypotheses, experiments, positive/negative/inconclusive results, discovered assumptions, next experiments, and ideas to retire. Preserve failed ideas.
9. Learning-loop ledger: observation -> classification -> diagnosis -> disposition -> experiment/fix -> evidence -> status/closure. Identify OPEN items and evidence required to close them.
10. Changes and deliberate non-changes: what changed because evidence justified it and what was investigated but deliberately left unchanged due to insufficient evidence.
11. Next-week learning agenda: highest-value lessons, biggest unanswered questions, prioritized hypotheses, prospective evidence sought, and evidence that would falsify important hypotheses.
12. What We Know Now That We Did Not Know Seven Days Ago: concise institutional-learning summary.

## Adam wager comparison
Include a dedicated section comparing each wager Adam actually placed against the engine's own independent matchup run and assessment. Candidate slips or contemplated wagers are not actual wagers unless execution is established under the screenshot/execution controls.

For each established wager preserve and compare, where available:
- game and Adam's exact wager/line/price/stake;
- execution timestamp/source;
- Beta Champion frozen matchup prediction and fair spread/total/win probability relevant to the wager;
- engine matchup assessment and principal football reasons available from the governed pre-event state;
- qualified market state at decision/execution and minimum acceptable line/price when available;
- whether the engine's frozen assessment AGREED, DISAGREED, or was INCONCLUSIVE with Adam's wager at the number he actually obtained, with factual explanation;
- whether the engine itself had BET EARLY, BET NOW, WAIT, PASS, or no established decision;
- later qualified close/CLV when available;
- actual result, shown after the pre-event comparison;
- postgame assessment of whether the pregame reasoning held up, failed, or remains unresolved;
- resulting learning disposition/hypothesis, if any.

Agreement/disagreement must be reconstructed only from genuinely frozen pre-event engine evidence, not from the outcome. Do not rewrite the engine's opinion to match Adam's bet, and do not treat Adam's wager as model input. A winning wager does not prove the reasoning was good; a losing wager does not prove it was bad.

Also provide a portfolio-level comparison across Adam's established wagers: where Adam and the engine agreed, disagreed, or were inconclusive; where Adam obtained better/worse execution relative to qualified benchmarks; whether repeated differences reveal a testable human-versus-engine insight; and whether any apparent pattern is still too small or noisy to interpret.

## Future-build consumption
Every future Challenger initialization, material model/feature/betting-layer redesign, source/operations redesign, or Beta maturity review must consult accumulated Weekly Beta Learning Reviews and unresolved ledger items. The build/review must record which applicable lessons were incorporated, tested, deferred with rationale, superseded, or judged not relevant.

This requirement does not authorize automatic self-modification. Learning becomes change only through the existing governed hypothesis, Sandbox, prospective Beta, independent-evaluation, and authorization path.

## Output and scheduling
The review should be persisted as a dated/versioned repository evidence document after the Sunday QA/Q&A cycle and linked into recovery/audit lineage as appropriate. No new scheduled task is created; the existing Sunday QA is the operational trigger.

Scientific effect: none by itself. This contract governs learning output and future-build consumption without modifying frozen Champion state.