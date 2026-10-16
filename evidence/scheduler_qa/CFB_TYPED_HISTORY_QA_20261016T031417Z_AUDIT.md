# Typed history continuity QA

Cycle: CFB_TYPED_HISTORY_QA_20261016T031417Z
Start: 2026-10-16T03:14:17Z
Execution: USER_DIRECTED_MANUAL_TEST_ROUTINE; synthetic transition fixtures and authentic saved-source regressions only.

## Finding and correction

The existing deadline/PASS transition guard compared adjacent packets but only validated the latest decision identity union. Omitting a game from an intermediate packet erased its immediately prior deadline/PASS constraint; a later complete packet could extend the deadline or reopen PASS. Duplicate and unknown historical identities could also pass without being accepted current identities.

Seven three-cycle regressions were written before correction. Six expected-rejection cases failed on the original code; complete history control passed. Corrected selected_block now checks every packet's string identity uniqueness and accepted census union before dictionaries and transition comparisons. Both market and decision, V1 and V2 histories are covered. Omission/duplication/unknown history is rejected even when the latest packet restores62 games. No record is reconstructed or silently discarded.

## Executed evidence

- 61 protocol/authentic legacy tests,39weekly tests,25full-board tests:125local affected checks PASS.
- Current2201CTsheet whole-source render/bootstrap and current-decision binding PASS; exact sheet d77593db60efe74b483999f90f087fed87e75a14 remains selected.
- Code persisted/read back: scripts/cfb_neutral_publication_gate.py @d7df4f29ee9074449f529e4397ef57ca890a8835.
- Regressions persisted/read back: scripts/test_cfb_neutral_publication_gate.py @18680bd34928dd3d32505bca86aadd8e44af2900.
- Active contract @f4c9ac0f396908fe90ef1a012969c9a358d35777; candidate routine section23 @390e1b148784ef85835776af4904a8d082ea7a0f; exact independent readbacks matched proposals.
- Existing CI38844639525/job116792263342 at e5164d3b40517eedf230ae3a5c6e90c986432075 completed SUCCESS; decoded logs independently read, including125affected checks, original accepted-archive hash/invariant and selected current sheet whole-render/current binding. This is independent structural CI, not a natural scheduled Monitor.

## Integration and remaining work

Existing workflow already consumes these files/tests; no workflow/task/prompt/schedule change. Four recurring production tasks observed enabled, retired/canary tasks disabled. This patch requires no new producer instructions because the existing compiler/renderer calls the corrected shared validator.

No canonical market, decision, deadline, cutoff, current sheet, execution, scorecard, money, frozen-model or accepted prediction source was mutated. Existing62 games/55INCONCLUSIVE+7PASS remain; consensus unavailable/Caesars unverified. Production Routine v5 remains active; Test Routine v6 candidate.

Natural actual-invocation runtime and producer adoption remain pending at next Friday07:00CT Monitor. Friday13:00CT reconciliation and recorded hard-cutoff constraints remain governing. Unsupported richer/arbitrary tails remain blocked; generic adaptation, qualified actionable/WAIT/consensus/executable offers and historical completion debts remain separate. Previous incomplete cycles stay incomplete. This manual enforcement repair earns only its own scoped closure after applicable readbacks and terminal candidate readback.
