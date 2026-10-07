# CFB Scheduler Canary V3 — Reads Complete

- invocation_id: 20261007T113543901Z
- actual_utc_timestamp: 2026-10-07T11:36:17.350Z
- task_id: 6ac4e807aaac8191b3255fae8ab82577
- test_version: V3
- immutable_fixture_ref: aa27d7c07a97f19cfc662156ba7434e4a425cf68
- fixture_interpretation: HISTORICAL_TEST_INPUTS_ONLY

## Fixture reads

- evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md
  - read_result: FETCH_FILE_SUCCEEDED
  - blob_sha: a5268b1d0259a257c3c44c05fbeb61928b103983
- evidence/operational/CFB_MARKET_MONITOR_STATE.md
  - read_result: FETCH_FILE_SUCCEEDED
  - blob_sha: c8616b340917e5db2674ec6c16581dd0d09275a5
- evidence/operational/CFB_DECISION_WAIT_LEDGER.md
  - read_result: FETCH_FILE_SUCCEEDED
  - blob_sha: 07ede9343706473b37a8b509777d68d3a27beec7
- evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-06_0704CT.md
  - read_result: FETCH_FILE_SUCCEEDED
  - blob_sha: 913be01ddc21d78a1b42e92ee0d3f09de52faba8

## NEXT UP table reconciliation

- expected_hot_sheet_sha: 913be01ddc21d78a1b42e92ee0d3f09de52faba8
- actual_hot_sheet_sha: 913be01ddc21d78a1b42e92ee0d3f09de52faba8
- hot_sheet_sha_match: true
- counting_rule: GAME_ROWS_IN_SEVEN_NEXT_UP_TABLES_ONLY; NEBRASKA_PROSE_EXCLUDED
- expected_section_counts: 1,2,3,5,7,17,14
- actual_section_counts: 1,2,3,5,7,17,14
- actual_total_game_rows: 49
- row_count_integrity_match: true
