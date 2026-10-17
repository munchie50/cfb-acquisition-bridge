# CFB Week 7 game-day pre-kickoff QA — 2026-10-17

**Cycle:** CFB_WEEKLY_QA_20261017T135931Z  
**Mode:** Saturday CFB game-day pre-kickoff QA  
**Audit boundary:** 2026-10-17T14:06:02Z  
**Scope:** integrity and decision QA only; not a competing market-monitor or Hot Sheet producer.

## Authority and observability

- Deterministic recovery doorway: `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md`, current blob `6796ba510e20386329c4ece4621ea9e033c37c14`, including the 2026-10-17 complete-betting-review navigation frontier.
- Active cadence: `evidence/CFB_ENGINE_FOOTBALL_WEEK_OPERATING_CADENCE_CONTRACT_v1_247.md`, blob `2a41f5cee71152c9f0a84cc3ee2f634020819dc2`.
- Active persistence procedure: blob `a58839b8551554a4514afad5dbbf8ff34889115e`.
- Active terminal closure contract: blob `9a2f158beddcde783c25fbecfa6d8d66dd8b2ca8`.
- Active consensus / Caesars separation control: blob `c8daffd209ca1575d057b8d73839fa74998ccce6`.
- Active neutral / bounded conditional publication control: blob `b29de141c6b88c205f43e337eb16e14b81ec8323`.
- Invocation RUN_STARTED was independently persisted/read back at `evidence/run_receipts/CFB_WEEKLY_QA_20261017T135931Z_RUN_STARTED.md`, blob `061660131cd390a7f4f6e3db6a2eb403f32737fe`.
- Repository authority tip used for the final validation run: `f39c8efd452f2076f7d0406ea22f4979b5e18023`. The local clone was initially shallow; after a read-only full-history fetch, immutable review commit `0a91623b1fdff37b87d8990dd140e7b1e336a873` was proven to be an ancestor. No authority or record was rewritten.

## Canonical readback

| Surface | Blob | QA finding |
|---|---|---|
| `CFB_MARKET_MONITOR_STATE.md` | `21f22e64f4e31eacddaf63864760f5d56c30b5c8` | Current Week 7 market packets retained; source identity and clock limitations remain explicit. |
| `CFB_DECISION_WAIT_LEDGER.md` | `49f59e2db876e4eab6f0789f0f81591e58afed41` | 61 PASS, 1 CONDITIONAL, 0 INCONCLUSIVE; no overdue open decision at the audit clock. |
| `CFB_EXECUTION_LEDGER.md` | `75caee4052e02ea7d2453d1d37fd3866e13ecc07` | No Week 7 established execution. Recommendations and screenshots were not promoted to execution. |
| `CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md` | `fbea94d5836388d3afd6c571b24409135fe9c6ce` | Prior authoritative joins retained; no outcome-informed reconstruction performed. |
| `CFB_MONEY_LEDGER.md` | `3aebcbdcc535479c29c31f18073cba09f59aab01` | Separate sandbox remains $20 ceiling / $20 available / $0 assigned exposure; funding allocation remains unresolved and was not inferred. |
| Current Hot Sheet | `201ba6e757d478d7a3d03cab200f9a8d0b3934b9` | 62 games exactly once: 61 PASS, 1 CONDITIONAL, 0 INCONCLUSIVE; no unresolved kickoff. |

Accepted FIRST_FROZEN remains 51 predictions plus 11 exclusions at the original cutoff; accepted REFRESH remains separate. No Champion, Challenger, S2, TIME-HIDDEN, or scientific status was mutated. Nebraska remains included in the governed slate and its current canonical disposition is preserved.

## Executable publication checks

The actual invocation had Python 3.12.14 and could run the repository validators. After full ancestry recovery:

- `cfb_hot_sheet_readiness.py`: 62 games, 0 open games, 61 preserved PASS, 1 conditional recommendation, no elapsed-current-quote IDs, no overdue-open-decision IDs, no recommendation blockers; Caesars not required for recommendation.
- `cfb_neutral_publication_gate.py`: `PASS_CONDITIONAL_CANONICAL_PRESENTATION_ONLY`; exact current sheet blob `201ba6e757d478d7a3d03cab200f9a8d0b3934b9`.
- `cfb_hot_sheet_current_decision_binding_gate.py`: `PASS_SUPPLIED_CURRENT_DECISION_BINDING_ONLY`; exact ledger blob `49f59e2db876e4eab6f0789f0f81591e58afed41`.
- Targeted compiler/profile/readiness/binding tests: 110 tests passed.
- These are saved-state integrity checks, not source acquisition, calibrated betting acceptance, execution, or scientific acceptance.

## Current user-facing decision

The sole non-PASS row remains a controlled-Beta **CONDITIONAL** recommendation for Florida State at Miami:

- Engine Prediction (Frozen): Miami -27.7; projected total 60.8; home win probability 0.949.
- Acceptable number: Miami -20.5 or better, price -110 or better.
- Current retained identified reference: DraftKings -20.5 at -105 through ESPN, response recovered by 2026-10-17T13:54:22Z; offer-update time unknown.
- Consensus: unavailable. Caesars: not checked / venue confirmation pending. Neither condition is misrepresented as a current executable offer.
- Reconciliation: 2026-10-17T18:00:00Z. Final practical planning cutoff: 2026-10-17T22:00:00Z, one hour before the qualified 23:00Z kickoff.
- Immutable qualitative review: `evidence/operational/recommendation_reviews/CFB_MIAMI_CONTROLLED_BETA_20261017T135409Z.json`, blob `9c789f9d1c5632adeb256031d3723fa339ea5a9a`.
- Official ACC availability evidence retained in that review: six Miami players OUT, including an offensive lineman; multiple Florida State defensive absences; Desir and Bowling probable. No final healthy claim was made.
- Fresh game-window weather check at this QA boundary indicates likely showers / storms near kickoff, roughly 71–74% precipitation, about 78°F, and light north wind increasing later. This is a material recheck item, not an automatic spread-state mutation. Before any execution, recheck actual weather, material availability/QB news, and the actual posted line/price. If the original line/price limit is unavailable or material conditions invalidate the review, PASS; never chase or extend the cutoff.

## QA disposition

No canonical market, decision, execution, scorecard, money, model, or Hot Sheet mutation was earned by this integrity pass. The conditional row already requires material-news recheck and retains its original limits. This QA therefore records a new prospective weather recheck requirement without changing the current decision state or creating a competing Hot Sheet.

**Persistence plan:** create this new append-only QA artifact through the GitHub contents API, then independently fetch/read it back; follow with a separate terminal candidate and, only after candidate readback, a separate RUN_CLOSURE. Existing governed files are not replaced.

QA_RESULT: PASS_PENDING_DURABLE_TERMINAL_SEQUENCE
