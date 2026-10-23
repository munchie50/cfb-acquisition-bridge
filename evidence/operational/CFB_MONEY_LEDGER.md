# CFB Money Ledger

Status: ACTIVE APPEND-ONLY CAPITAL / FUNDING SURFACE
Initialized at observed UTC: 2026-10-12T01:24:34Z
Authority: direct user funding instruction/clarification; controlled-capital contract v1.238.
Scope: bankroll funding and its allocation, separate from actual-wager execution records.
Scientific / Champion effect: NONE.

## Confirmed funding

| Funding ID | Transaction | Amount USD | Allocation | Funding event time | Evidence |
|---|---|---:|---|---|---|
| CFB_ORIGINAL_ADD20_FUNDING_001 | New bankroll money added | +$20.00 | UNASSIGNED production/sandbox | Unspecified | User clarified the earlier “Also add 20 to money ledger” instruction meant new money, separate from the four $5 bets |

This posts the original pending instruction exactly once. The later clarification resolves its meaning; it is not a second +$20 transaction. Earlier pending-clarification statements in execution/Health/review evidence stay preserved as historical-at-the-time records and are superseded on funding-versus-stake meaning only.

```cfb-funding-json
{
  "schema": "CFB_FUNDING_TRANSACTION_V1",
  "funding_id": "CFB_ORIGINAL_ADD20_FUNDING_001",
  "idempotency_key": "ORIGINAL_USER_INSTRUCTION_ALSO_ADD_20_TO_MONEY_LEDGER",
  "transaction_type": "BANKROLL_FUNDING",
  "amount_usd": "20.00",
  "status": "POSTED_USER_CONFIRMED_ALLOCATION_UNASSIGNED",
  "budget_class": "UNASSIGNED",
  "funding_event_time": "UNSPECIFIED",
  "recorded_at_utc": "2026-10-12T01:24:34Z",
  "source": {
    "original_instruction": "Also add 20 to money ledger",
    "clarification": "New money added, separate from the four $5 bets",
    "evidence_type": "DIRECT_USER_CLARIFICATION"
  },
  "related_execution_ids": [
    "CFB_OCT09-01",
    "CFB_OCT09-02",
    "CFB_OCT09-03",
    "CFB_OCT09-04"
  ],
  "execution_reference": {
    "path": "evidence/operational/CFB_EXECUTION_LEDGER.md",
    "blob": "75caee4052e02ea7d2453d1d37fd3866e13ecc07"
  },
  "is_wager": false,
  "is_wager_return": false,
  "changes_sandbox_ceiling": false,
  "cash_balance": "NOT_COMPUTABLE_FROM_CURRENT_ALLOCATED_EVIDENCE"
}
```

Confirmed funding recorded in this ledger: **+$20.00**, one transaction. Production/sandbox allocation and actual funding event date/time are not inferred.

## Execution reference snapshot — not another cash transaction

Source: evidence/operational/CFB_EXECUTION_LEDGER.md at75caee4052e02ea7d2453d1d37fd3866e13ecc07, independently recovered at this recording boundary.

- 15 distinct established actual wagers; $53.45 cumulative historical stake.
- The four October9-issued tickets total $20.00 staked.
- Those four tickets have arithmetic return $14.55 and net P/L -$5.45 from recorded finals; sportsbook redemption/payment remains unverified.
- These figures are existing execution/result evidence. The +$20 funding is separate; it does not add another wager, duplicate a $20 stake debit, record a payout, or change result grades.

Opening production/combined bankroll and wager/funding bucket allocation are unresolved, so a combined cash balance is not computed. The separately authorized sandbox state/ceiling remains $20.00, available $20.00, assigned exposure $0.00 under unchanged v1.238; this unassigned funding does not raise the sandbox ceiling to $40 or classify existing wagers as sandbox.

## Append / deduplication control

Before a future funding append, recover this complete ledger and direct source evidence. Require a unique funding_id and idempotency_key; a clarification/repeated mention of the same instruction updates its interpretation prospectively and never creates another credit. Keep contributions, wager stakes, expected/result-grade returns, confirmed payouts, withdrawals and budget transfers distinct. Append new evidence; preserve earlier entries. Compute a bucket balance only after its opening state, funding/execution allocation and relevant cash movements are established. User-confirmed funding is bookkeeping evidence; no bank transfer is performed by this workflow.

No current Hot Sheet, model, decision, execution record, result, allocation, risk limit, task or schedule is changed by this funding entry.


## Complete user-confirmed betting-pot baseline — October23

Run: CFB_BACKLOG_20261023T231844Z. Source: private CFB_Wager_Record_2026-10-23.md, version2, Library identity libfile_8bd8ada1560c8191989440c6f7ddf97f. User confirmed $61.30 is all money wrapped up at this boundary. Baseline event is October23 after the printed 15:57 voucher issuance; receipt timezone remains unspecified, exact user-clarification time is not inferred. This record is a prospective opening snapshot, not a funding transaction, payout, deposit or historical P/L reconciliation.

```cfb-bankroll-snapshot-json
{
  "schema": "CFB_USER_CONFIRMED_BANKROLL_BASELINE_V1",
  "baseline_id": "CFB_COMPLETE_POT_BASELINE_20261023",
  "idempotency_key": "USER_CONFIRMED_COMPLETE_61_30_OCT23_V2",
  "transaction_type": "OPENING_SNAPSHOT_NOT_CASH_FLOW",
  "total_usd": "61.30",
  "available_voucher_usd": "25.30",
  "open_stakes_at_cost_usd": "36.00",
  "additional_historical_holdings_included": false,
  "uncollected_prior_returns_added_usd": "0.00",
  "source_library_file_id": "libfile_8bd8ada1560c8191989440c6f7ddf97f",
  "source_version": "2",
  "execution_ids": [
    "CFB_OCT23-01",
    "CFB_OCT23-02",
    "CFB_OCT23-03",
    "CFB_OCT23-04",
    "CFB_OCT23-05",
    "CFB_OCT23-06",
    "CFB_OCT23-07",
    "CFB_OCT23-08"
  ],
  "execution_reference": {
    "path": "evidence/operational/CFB_EXECUTION_LEDGER.md",
    "blob": "218189ae917ad3c3e79461ae7c6fe6d28c2a2278"
  },
  "is_deposit": false,
  "is_profit": false,
  "changes_sandbox_ceiling": false,
  "budget_class": "UNASSIGNED",
  "lifetime_profit_loss": "UNRESOLVED"
}
```

At the user-confirmed baseline: $25.30 available voucher + $36.00 open stakes at cost + $0.00 additional historical uncollected returns = $61.30 total. Cashable voucher identifiers remain private. No settlement, redemption or collection is inferred. The historical +$20 funding remains posted once and is already contained in the user's complete holdings, so it is NOT added to $61.30. Prior stakes/results likewise are not rebooked. Historical opening/cash-flow reconciliation remains unresolved; this baseline supersedes the earlier inability to compute the complete current pot only prospectively. It does not assign production/sandbox buckets or raise the separate sandbox ceiling.

Prospective arithmetic: total pot = available cash/vouchers + open stakes at cost + established uncollected returns. P/L since this baseline = total pot - $61.30 - new deposits + withdrawals. A new wager transfers stake from available funds to open exposure exactly once. Established settlement removes the open stake and recognizes the actual return once as funds or an uncollected claim; score-derived expected returns stay distinct until book settlement is established. Collecting/reinserting a recognized ticket or voucher transfers holdings and is not new funding/profit. Cash retained in the pot after redemption is not a withdrawal. At each new observed holdings update, reconcile the observed amount and retain unexplained differences explicitly. This is accounting implementation, not a money transfer, staking change, prediction, promotion or new schedule.
