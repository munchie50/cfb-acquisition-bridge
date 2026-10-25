# Completed Week 5 exact ORIGINAL baseline — 2026-10-25

Status: `PASS_COMPLETED_WEEK5_EXACT_ORIGINAL_RECONCILIATION`

This bounded replay independently joined the 47 governed FBS-vs-FBS predictions from accepted original artifact `10897612260` / SHA-256 `772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf` to the 47 already-governed Week 5 finals in `evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md`. It reused proved evidence and did not reacquire outcomes, reconstruct decisions, or inspect target outcomes during prediction creation.

## Exact reproduced metrics

| Metric | Result |
|---|---:|
| Eligible predictions / joined finals | 47 / 47 |
| Unresolved identities | 0 |
| Margin direction | 32/47 (68.1%) |
| Margin MAE | 15.524849155393 |
| Signed margin error | -1.331971519767 |
| Total MAE | 14.116057728901 |
| Signed total error | -0.620379536169 |
| Home-win Brier | 0.218295900522 |

The results reproduce the accepted rounded Week 5 review: 32/47 direction, margin MAE 15.525, signed margin -1.332, total MAE 14.116, signed total -0.620, and Brier 0.2183.

## Boundaries

- Explicit original exclusions remain outside the denominator and are not converted into predictions.
- The original artifact also contains a modeled non-FBS matchup in this date range; it remains outside this governed FBS-vs-FBS baseline.
- Historical qualified markets, recommendations, closes, Caesars offers, executions, and ROI are not supplied by this replay and remain separately governed or unavailable.
- No Champion, FIRST_FROZEN, REFRESH, Challenger, TIME-HIDDEN, market, decision, execution, money, task, or schedule state changed.

Next completed-batch boundary: Week 6 exact ORIGINAL reconciliation, reusing its existing 49/49 scorecard and accepted review without reconstructing missing pre-event evidence.
