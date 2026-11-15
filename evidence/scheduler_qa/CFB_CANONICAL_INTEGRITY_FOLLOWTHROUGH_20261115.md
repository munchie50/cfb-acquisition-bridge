# CFB canonical integrity follow-through — November 15, 2026

Manual verification of the first outstanding Health integrity check in the [November 14 audit](CFB_HEALTH_20261114T222936611Z_AUDIT.md). Pinned repository commit `e39e0ccea3a5209af4d4eff19b22d54981860b4f` was independently recovered as main from the connected GitHub repository. Read the pinned recursive tree via the connector, fetched genuine Git history to a clean detached worktree, and recomputed the complete byte length and Git SHA-1 from each local file using the `blob <byte-count>\0` header. Every pair matched the connector tree.

| File | Bytes | Git blob |
|---|---:|---|
| `evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_290.md` | 149691 | `f7d4db46ae089d4bd6c7258bc30bdb0f943cbb4a` |
| `evidence/operational/CFB_DECISION_WAIT_LEDGER.md` | 3276343 | `55a9d19f6df452f1625a3f124f8201e04a1a9cf0` |
| `evidence/operational/CFB_EXECUTION_LEDGER.md` | 51144 | `5f098136e7c2719731d49d5bbe98752df0775e9f` |
| `evidence/operational/CFB_MARKET_MONITOR_STATE.md` | 6194481 | `dd59069b767cf563a5c4737b364249ce1d9c8535` |
| `evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md` | 89317 | `4fb855cbfa9beef8f7e33935d9e2bf4aba914c59` |

The November 14 audited commit `278a04241f208d6bdef86e41d9e4d8bc4906b0a5` is a true ancestor. Its recovery index, market, decision and execution bytes exactly match the corresponding current snapshot. Its historical 87,860-byte scorecard independently hashes to `851efb1dc33e6efb044a5c3bdbd358cf28216f2e` and is an exact byte prefix of the current scorecard.

## Semantic checks executed

- Existing Week 11 publication input gate passed at the saved Friday cycle `CFB_MARKET_MONITOR_20261113T212021Z` using the accepted Week 11 lineage. The market and decision ledgers had identical 67-game identity sets with 65 PASS and two CONDITIONAL.
- Execution ledger contains 64 distinct ticket IDs. Exact set equality holds between the 13 November 13 IDs and the scoped official-result grade artifact. This verifies the intake-to-outcome join, not the older placement-time recommendation or settlement joins.
- The 66 official-result IDs plus the one pending Ole Miss–Oklahoma identity equal the entire saved 67-game cohort.
- Health's prior byte/hash verification gap is now covered for these exact snapshots through manual proof. Full historical semantic coverage and financial settlement remain open. The prior scheduled result, Health coverage watermark and natural Monitor proof were left as recorded.

No task, schedule, model, wager, money, market or Hot Sheet changes.
