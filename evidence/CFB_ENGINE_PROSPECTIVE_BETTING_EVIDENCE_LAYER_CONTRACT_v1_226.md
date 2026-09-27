# CFB Engine — Prospective Betting Evidence Layer Contract v1.226

Status: **ACTIVE PROSPECTIVE EVIDENCE-CAPTURE CONTROL — NOT A CALIBRATED BETTING MODEL**
Date: 2026-09-26
Parents: v1.144, v1.216, v1.224, v1.225
Scope: 2026+ prospective Champion-vs-market/execution evidence

## Purpose

Capture the highest-value betting evidence now, while the CFB Production Champion remains independently frozen, so later betting-layer calibration can be tested without reconstructing prices, timing, passes, or closing lines after outcomes are known.

This contract does not create cover probabilities, expected value, Kelly sizing, parlay recommendations, or new Champion model inputs.

## Separation invariant

Maintain four independent records:
1. **Champion prediction state** — fair spread, fair total, win probability, snapshot lineage and cutoff.
2. **Market observation state** — qualified sportsbook/benchmark observations with source and observation time.
3. **Engine decision state** — BET EARLY / BET NOW / WAIT / PASS, minimum acceptable line/price, decision time and reason.
4. **Actual execution state** — only wagers Adam actually places, with sportsbook, accepted line/odds, stake and execution evidence/time.

None may be rewritten to make another layer look better after market movement or outcomes.

## Required prospective capture

Where the information is available and qualified, preserve append-only observations for:

### A. Market/price history
- game/market identity;
- sportsbook or qualified benchmark/consensus source;
- observation timestamp;
- spread/total/moneyline and associated price;
- whether observation is FIRST_OBSERVED, INTERMEDIATE, EXECUTION, or CLOSE;
- source/provenance and timestamp semantics.

Never reconstruct an earlier market observation from a later source.

### B. Executable price versus benchmark
Execution-book prices and benchmark/consensus prices remain distinct.
- Adam's actual accepted sportsbook price is execution evidence.
- A benchmark/consensus observation requires its own qualified source.
- Do not call one sportsbook quote "the market" unless the applicable contract permits it.

### C. Closing-line value / closing-market comparison
CLV is a diagnostic, not a bet result.
- Evaluate only against a separately qualified closing benchmark with defined timestamp/source semantics.
- Preserve both spread/total number and price; do not reduce CLV to line movement alone when odds changed.
- Report movement toward/away from the frozen Champion opinion separately from actual wager outcome.
- If closing benchmark is unavailable/unqualified, mark CLV UNVERIFIED rather than infer it.

### D. Key-number awareness
For football spreads, preserve whether a contemplated or executed move crosses or lands on a materially common scoring margin.
- Key-number status is decision context, not an automatic bet trigger.
- Do not assign a numeric value, probability uplift, or universal hierarchy to key numbers until prospectively tested/qualified.
- Minimum acceptable line remains authoritative; never chase through it merely because a key-number heuristic exists.

### E. Timing/execution quality
Preserve separately:
- first qualified opportunity;
- engine decision time/status;
- actual execution time/price, if any;
- later qualified market observations;
- qualified close.

This supports later analysis of whether BET EARLY / WAIT / BET NOW / PASS timing preserved or lost price without changing the underlying football prediction.

### F. PASS / no-bet opportunities
Preserve a decision record when the engine evaluates an opportunity and returns PASS or WAIT, including the observed price and minimum acceptable threshold when available.
- Never convert a historical PASS/WAIT into a hypothetical bet after seeing the result.
- Later evaluation may ask whether thresholds/timing were useful, but outcome knowledge cannot rewrite the original decision.

## Current permissible diagnostics

Before calibrated cover-probability/EV authority exists, permissible prospective diagnostics include:
- raw Champion fair-line minus qualified market-line disagreement;
- direction and magnitude of qualified market movement;
- whether movement crossed a recorded minimum acceptable line;
- key-number crossing/landing flags without invented numeric value;
- execution price versus contemporaneous qualified benchmark;
- execution/first-observed price versus qualified closing benchmark;
- outcome tracked separately from the above.

A raw point discrepancy is not a cover probability or expected value.

## Fail-closed rules

- Missing/ambiguous timestamp -> do not invent sequence.
- Missing qualified closing benchmark -> CLV UNVERIFIED.
- Screenshot market information -> v1.224 classification first.
- Candidate bet -> not actual execution without execution evidence/confirmation.
- No qualified market source -> no actionable market-relative conclusion.
- Market movement never rewrites Champion prediction.
- Outcome never rewrites prior prediction, decision, market observation, or execution record.

## Acceptance

**PASS — evidence capture may begin prospectively.**

This contract improves evidence collection and later testability only. It does not authorize model fitting/tuning, betting calibration, staking changes, parlay construction, or Champion modification.
