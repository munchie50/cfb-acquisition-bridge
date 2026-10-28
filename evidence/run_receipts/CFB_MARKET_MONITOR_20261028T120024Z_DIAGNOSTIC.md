# CFB Market Monitor diagnostic — CFB_MARKET_MONITOR_20261028T120024Z

Recorded UTC: 2026-10-28T12:16:00Z
Run status earned: RUN_INCOMPLETE

## Last proved stage

- Accepted authority: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md`, blob `356b5920ab9cba100baa5669588995161585e48b`; active cadence v1.247.
- RUN_STARTED was persisted and independently read back: `evidence/run_receipts/CFB_MARKET_MONITOR_20261028T120024Z_RUN_STARTED.md`, commit `12da49afd6f230d286987575f4ba06dfb02f5a54`, blob `d5b1fdd1bc335b4135685cad675262ae5d0bbbf0`.
- Fresh complete CBS Week 9 fallback was persisted and read back: `evidence/operational/CFB_CBS_WEEK9_TEXT_TABLE_CAPTURE_20261028T120000Z.md`, commit `d6dc2a3d26ce0d20d7684e65cb622c8f2748bbff`, blob `b55854c08e51602c2e36b92f405f83394cccc0b8`; response recovered by `2026-10-28T12:04:37.444Z`; 56 games / 112 team rows.
- Exact-once candidate assertions passed: 56 unique game rows; section counts retained as TUESDAY 2, WEDNESDAY 2, THURSDAY 2, FRIDAY 3, SATURDAY MORNING 11, SATURDAY AFTERNOON 22, SATURDAY EVENING/NIGHT 14, UNRESOLVED 0.
- Unselected candidate persisted/read back: `evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-28_0700CT.md`, blob `a73692ca20b141ffb830d6b5c17ce8b85df6294e`. It is explicitly diagnostic and did not replace the selected governed sheet.

## Decision and market result

- No material decision change. Pittsburgh remains conditional only at `-6.5 or better / -115 or better`; fresh fallback `-7.5 -108` fails the line cap.
- Boston College remains conditional only at `+7.5 or better / -115 or better`; fresh fallback `+7.5 -124` fails the price cap.
- Applicable official ACC Wednesday availability reports were not yet posted at this boundary. Original noon CT reconciliation and 1:00 PM CT hard cutoff remain unchanged.
- All remaining game rows were checked across both spread sides, both moneylines and over/under after current movements. No new supported state was earned. Alternates/team totals were unavailable/not evaluated. `NO_PREFERRED_PARLAY`.
- `CONSENSUS_UNAVAILABLE`; Caesars and actual execution `UNVERIFIED`. No established execution, stake, money movement, settlement, model change or Champion change.
- Week 9 execution ledger and postgame scorecard remain at independently read-back blobs `1a938f42e9f03e723bd50348f8a78dbd8b7098e9` and `1e8e0a9c3cd34c163c32f6782cdfccf30b9e13d8`. Visible odds-page result cells were quarantined and not used as settlement evidence.

## Compiler / readiness blocker

Actual Python runtime: `3.12.14`.

The current `scripts/cfb_week9_publication.py` and `scripts/cfb_hot_sheet_readiness.py --profile WEEK9` both reached the immutable review loader and failed closed at the required command:

`git -C <repository-root> merge-base --is-ancestor 37f0e3edf5b09afdc4f05e14e5a70b6d4fa91ab3 HEAD`

Observed classification: `IMMUTABLE_REVIEW_ANCESTRY_UNAVAILABLE`. This invocation has connected GitHub contents access but no supported local Git checkout/HEAD containing accepted runtime ancestry. No ancestry was fabricated and no gate was bypassed. Therefore the compiler proposal, readiness output, publication gate, selected publication, recovery-index transfer/preflight, and selected CI integration could not be completed.

A temporary human-readable canonical append attempted before the typed-tail failure was recognized was fully removed. Independent readback proves canonical typed bytes restored exactly:
- market `2110b9167e823b3169335ffd12e6780b4067f1de`
- decision `8b43d28b71a0e70b12a4cbda3d14e886f13fa110`

The prior selected Hot Sheet remains `evidence/operational/CFB_WEEK9_HOT_SHEET_2026-10-27_2050CT.md`, blob `a11e571c9f2eab663b68cc4e0d25283a7da33092`. It is not retimed or represented as fresh.

## Shared Firecrawl budget

Provider cycle: `2026-10-27T17:16:35.203Z` through `2026-11-27T17:16:35.203Z`; plan/remaining `1000/1000`; cycle day `1/31`; cumulative release `32`; observed current-cycle consumption `0`. No chargeable Firecrawl request was issued because a known upper cost was unavailable; the permitted direct CBS browser fallback supplied the complete board.

## Next safe action

At the next prospective Monitor invocation, use a supported authenticated repository checkout whose HEAD contains the accepted review commits, rerun the normal Week 9 compiler/readiness/publication gates with a genuinely fresh source, and serve the noon checkpoint before the original cutoff if still prospective. Do not reconstruct this incomplete run, retime its source, loosen limits, or select this diagnostic candidate.

No task, schedule, ownership, billing, model, wager or automation mutation was made.
