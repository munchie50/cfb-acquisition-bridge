# CFB_WAGER_RESULT_RECONCILIATION_20261009T223030Z terminal candidate

```json
{
  "run_id": "CFB_WAGER_RESULT_RECONCILIATION_20261009T223030Z",
  "execution_class": "USER_DIRECTED_MANUAL_TEST_ROUTINE_V6",
  "boundary_utc": "2026-10-09T22:30:30Z",
  "workload_result": "RUN_PASS",
  "scope": "Bounded eleven-ticket official final-score grade reconciliation only; book settlement and actual redemption/payment excluded.",
  "start": {
    "path": "evidence/run_receipts/CFB_WAGER_RESULT_RECONCILIATION_20261009T223030Z_RUN_STARTED.md",
    "sha": "f0cdba193e99cbf33b148cde96c6c46612757a80"
  },
  "final_result_evidence": {
    "path": "evidence/operational/CFB_ORIGINAL_WAGER_FINAL_RESULT_RECONCILIATION_2026-10-09.json",
    "sha": "c84336516210f55fbd5d130275202da2b8899092",
    "commit": "6de69872d49177c09ca664387e394bcf617b9037"
  },
  "independent_current_branch_readbacks": [
    {
      "path": "evidence/operational/CFB_EXECUTION_LEDGER.md",
      "sha": "8393d8354f461a17739ef245fb47ee33c863699b"
    },
    {
      "path": "evidence/CFB_ENGINE_HOLISTIC_SYSTEM_QA_MAP_2026-09-30.md",
      "sha": "b4e3e745cd087b196d11723769bb40701d807150"
    },
    {
      "path": "evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md",
      "sha": "5a750ad337120f528490996e81435649b452d7df"
    }
  ],
  "append_metadata": [
    {
      "path": "evidence/operational/CFB_EXECUTION_LEDGER.md",
      "operation": "update_file",
      "attempt": 1,
      "baseline_blob_sha": "f56be836e12fa28a737da8f4c70320726be04875",
      "proposed_blob_sha": "8393d8354f461a17739ef245fb47ee33c863699b",
      "proposal_sha256": "08559709bb3dbd61fbe5c9c7a414fe226d8b892de991c8010b74f1a013f60cf1",
      "delta_sha256": "9060f03311491bcb5ecef9ddf888640e6b0fae09c2cfb4daf35dec48e87bf42d",
      "proposal_bytes": 6867,
      "delta_bytes": 2453,
      "proposal_characters": 6861,
      "delta_characters": 2451,
      "all_prior_bytes_preserved": true,
      "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
    },
    {
      "path": "evidence/CFB_ENGINE_HOLISTIC_SYSTEM_QA_MAP_2026-09-30.md",
      "operation": "update_file",
      "attempt": 1,
      "baseline_blob_sha": "d865cca537005c3b07a14bc8af9cd44c2e575bb1",
      "proposed_blob_sha": "b4e3e745cd087b196d11723769bb40701d807150",
      "proposal_sha256": "9469a2ce332ed65027d26cc1afda4f068a2c3988447ec050de340ea89333832c",
      "delta_sha256": "0cdf5c4465d9b25a810d674d591d112b75697f1b1b151733ff1cceb985631ebc",
      "proposal_bytes": 32837,
      "delta_bytes": 1371,
      "proposal_characters": 32777,
      "delta_characters": 1367,
      "all_prior_bytes_preserved": true,
      "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
    },
    {
      "path": "evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md",
      "operation": "update_file",
      "attempt": 1,
      "baseline_blob_sha": "2951492c988fdf78246f92d3ee771f2171058e6e",
      "proposed_blob_sha": "5a750ad337120f528490996e81435649b452d7df",
      "proposal_sha256": "cded71e55d14acd42473d2b15f9ce499fb664269d208831b779cf61905f2072b",
      "delta_sha256": "a8426a773a58f2fdc81a1f76a6e5b063427303d40fc23dc54d0d4f3543b3b263",
      "proposal_bytes": 34468,
      "delta_bytes": 1284,
      "proposal_characters": 34432,
      "delta_characters": 1284,
      "all_prior_bytes_preserved": true,
      "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
    }
  ],
  "reconciliation": {
    "source_ticket_count": 11,
    "unique_ticket_count": 11,
    "exact_official_team_pair_and_date_matches": 11,
    "counts": {
      "WIN": 7,
      "LOSS": 4,
      "PUSH": 0
    },
    "live": {
      "WIN": 1,
      "LOSS": 0,
      "PUSH": 0
    },
    "not_live_labelled": {
      "WIN": 6,
      "LOSS": 4,
      "PUSH": 0,
      "pregame_timing_certification": "UNVERIFIED"
    },
    "original_stake_total_usd": "33.45",
    "signed_comparison_rule": "SPREAD or SPREAD_LIVE: selected-team final points minus opponent final points plus signed accepted line. MONEYLINE: selected-team final points minus opponent final points. Positive=WIN, negative=LOSS, zero=PUSH.",
    "paid_status": "UNVERIFIED",
    "net_cash_profit": "UNVERIFIED"
  },
  "invariants": {
    "original_manifest_unchanged": true,
    "market_unchanged": true,
    "decision_unchanged": true,
    "scorecard_unchanged": true,
    "task_control_fields_preserved": 66,
    "enabled_tasks": 4,
    "prior_ledger_bytes_preserved": true,
    "live_separated": true
  },
  "demonstration": {
    "trigger": "Original execution ledger recovered but outcome fields unverified.",
    "expected": "Exact original ticket to official final identity/date join; signed-line arithmetic; live isolation; preserve missing cash/decision/budget fields.",
    "actual": "Eleven unique ticket identities matched official finals with exact event dates; 7 WIN / 4 LOSS / 0 PUSH under final-score arithmetic; Baylor live +0.5 points after -9.5; no sportsbook payout claimed.",
    "proof_class": "MANUAL_FINAL_RESULT_JOIN_DEMONSTRATED",
    "remaining_debt": [
      "Book settlement/adjudication and actual redemption/payment",
      "Production/sandbox allocation",
      "Receipt timezone and independent timing qualification",
      "Genuine frozen pre-event Champion/decision references",
      "Qualified closing market/CLV",
      "Future scheduled settlement producer demonstration"
    ]
  },
  "scientific_effect": "NONE",
  "champion_effect": "NONE",
  "candidate_own_readback": "Not self-certified; separate closure issued only after independent fetch."
}
```
