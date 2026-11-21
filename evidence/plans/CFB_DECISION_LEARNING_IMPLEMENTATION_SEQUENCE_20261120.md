# CFB decision and learning implementation sequence — 2026-11-20
Status: APPROVED FOR READ-ONLY ENGINEERING AND RESEARCH ONLY; no model/rule promotion.
Authority: existing weekly beta learning review contract v1.233, integrated betting intelligence roadmap, existing canonical full-slate/market/decision/execution/official-final records. This document is a navigation checkpoint, not a new governance layer.

## Review and corrections to prior recommendations
1. First build a reliable **pregame opportunity identity + decision attribution join**, not a new confidence scoring formula. Ranking uncalibrated projections as percentages would create false confidence. Preserve original published ranks, timestamps and outcomes separately.
2. **Top 10 is an independent ranked opportunity display, not a quota of qualified wagers.** Separate football ranking, price eligibility, and venue execution. Do not imply a number-only failure is a football rejection; do not make an indicative mixed-book display executable.
3. Full-slate coverage and official-final joins must include **unbet and PASS games**. Count unreviewed/unsupported markets as missing, never assume no-edge. Separate game denominator, six-market denominator, quote-qualified denominator and gradable-result denominator.
4. Learn in this order: reliable joins and denominators; attributable rejection/near misses; paired historical price-and-result replay; confidence/rank calibration when prediction scale is valid; prospective champion/challenger shadow; only then governed threshold promotion.
5. Do not optimize on past winning selections, retrofit confidence or prices after results, claim predictive calibration from small samples, or confuse hypothetical returns with real tickets. Group correlated picks by game/week and report uncertainty.
6. Preserve the user-facing Hot Sheet as short actionable Top 10 + explicit price/number holds and status; deeper shadow reports live in existing weekly learning evidence, not extra user-facing clutter.
7. Maintain Friday 1 PM CT practical decision deadline and 1–2 trip cadence, with existing four scheduled tasks only. Existing Market Monitor handles pregame freeze and Hot Sheet; existing Sunday Weekly QA grades and learns.

## Engineering order / durable resume ledger
A. [STARTED] Read-only market-level diagnostics at scripts/cfb_decision_opportunity_diagnostics.py, regression tests at qa/test_cfb_decision_opportunity_diagnostics.py. Current diagnostic labels price-word mentions, **not price-only causal proof**. One duplicate Week12 identity between Friday and exclusions must be reported/quarantined, not counted twice. Execute tests and pin source audit before treating it as validated.
B. [NEXT] Decision attribution with **explicit evidence tags**: FOOTBALL_SUPPORT, FOOTBALL_COUNTERCASE, PRICE_HOLD, NUMBER_HOLD, QUOTE_GAP, VENUE_GAP, TIMING_GAP, MODEL_GAP, REVIEW_GAP. Multiple tags permitted, causal price-only classification requires a specific documented gate, never keyword matching alone. Every row has game ID, directed market/side, saved timestamp, original status, price/number, cutoff and source provenance.
C. [NEXT] Build matched pre-event opportunity ledger: join immutable prediction, saved rank, source-qualified quote, original decision, official final and actual execution as separate optional sources. Reject identity/clock contradictions; missing fields remain missing. Never promote refresh to original.
D. [NEXT] Generate paired season/week shadow scorecard: gradable market results and hypothetical $2/$5 flat-stake return only where exact pregame odds exist; actual tickets separate; ranks 1–10 versus 11–20 versus full slate; PASS/holds/missed delivery. Include push/void/coverage denominators.
E. [NEXT] Calibration: evaluate Brier/log loss for genuine frozen probability targets, reliability bands with sample counts, rank lift and confidence uncertainty; do not apply ML probabilities to spreads or totals without a qualified mapping.
F. [NEXT] Challenger thresholds and Top 10 display: freeze rules before future games, compare coverage, return, drawdown, rejected opportunity loss and reliability across weeks; do not change production limits without explicit promotion.
G. [NEXT] Integrate only validated read-only artifacts into the existing four tasks; use exact source pins, regression tests, readback and current canonical publication checks.

## Acceptance per component
BUILT means code committed. EXECUTED means original code ran against exact pinned inputs. VERIFIED means independent output/readback and negative tests. ACCEPTED means evidence and authority checks complete. PRODUCTION requires explicit separate approval where selection thresholds or output behavior change. A green repository commit is not an executed engine cycle.

## Avoid duplication
Existing learning contract already owns Sunday scorecards, missed opportunities, season backfill and exposure. Existing roadmap owns historical and prospective challenger research. Append new findings to those records; do not create competing production tasks, duplicate ledgers, or independently rank hypothetical selections after results.
