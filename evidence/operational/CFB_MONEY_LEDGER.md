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
