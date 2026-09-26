# CFB Engine — Challenger B Historical Membership Authority Recovery v1.154

Status: 2017-2025 MEMBERSHIP AUTHORITY RECOVERED EXACTLY / 2016 REMAINS SEPARATE
Parent: v1.153
No fitting or scoring.

## Recovery correction
A full deterministic Library enumeration located the previously referenced package:
CFB_ENGINE_WORKING_STATE_2026-09-23_SCHEDULE_ACQUISITION_v0_22.zip
Library file_id: file_000000004d2881f583fc7b2027b1aaa5
library_file_id: libfile_2aaa08e0ad608191a12190847bb6cfcb
Materialized size: 2,845,626 bytes.

This supersedes the earlier current-state statement that the package/raw schedule bytes were not currently recovered. They were present deeper in Library pagination and are now directly recovered.

## Exact recovered membership artifacts
Inside the package:
- CFB_V2_PHASE4_CBS_2026_FBS_ANCHOR_v0_1.json
  SHA-256 54615ed756f0cf03249c41f04c32e2b1249366b132197dc12de2175d89c529d3
  status QUALIFIED_IDENTITY_ANCHOR; 138/138 unique identities.
- CFB_V2_PHASE4_CBS_MEMBERSHIP_TRANSITION_LEDGER_v0_1.json
  SHA-256 17a051f519782239158c37f1c440307e59cc13a974fc20caed0dec90f78e2ad3
  status QUALIFIED_FOR_MEMBERSHIP_RECONSTRUCTION.
- CFB_V2_PHASE4_CBS_HISTORICAL_FBS_SEASON_MAPS_v0_1.json
  SHA-256 2ec2dbbb50184c02634a16da954b5f11fe43ccb588c08ede098581928751689d
  status QUALIFIED_FOR_POPULATION_CLASSIFICATION.
- CFB_V2_PHASE4_CBS_MEMBERSHIP_ANCHOR_COMPLETION_CHECKPOINT_2026-09-23.md
  SHA-256 bc8556f2db585cf404f48191d29cbb2e1d83c104e964200001bd8a2090ae9365.
- schedule_population_audit_2017_2025.json
  SHA-256 b0ed4a88dcf3d4143ff218d2927724f47c9563a78774f0638650b970c702afc3.
- population_ledger_2017_2025_pre_scope.json
  current recovered byte SHA-256 94a6346ba9d86d50ebbe12f458b6289c8d62255145155016439e4018fb146172.

The season maps reproduce the frozen CBS membership counts:
2017 130; 2018 130; 2019 130; 2020 130; 2021 130; 2022 131; 2023 133; 2024 134; 2025 136; 2026 138.

## Important historical ledger note
schedule_population_audit records an internal ledger_sha256 value 3d0fff8457664467ac548a3f831826dd450d98f26c06a08240698b146ea82ac3, while the directly recovered packaged population_ledger bytes hash to 94a6346b.... Do not silently equate these. The exact membership maps themselves are independently recovered and qualified; the ledger-hash discrepancy is a bounded artifact-integrity question for the legacy population ledger, not a reason to discard recovered membership authority.

## Authority consequence
v1.153's 2017-2025 membership-authority blocker is CLOSED. Do not reacquire or substitute provider division labels for those seasons.

The package's own Population Execution Readiness checkpoint explicitly says:
- 2017-2025 season membership maps were deterministically reconstructed and count-checked;
- membership identity prerequisite closed;
- 2016 remains a separate source-retention boundary.

Therefore the corrected Challenger-B population can use exact recovered CBS membership maps for 2017-2025, but 2016 must be resolved separately before a full 2016-2025 population PASS.

## Next dependency
1. recover 2016 FBS membership/population authority from persisted ancestry;
2. independently reconcile the legacy ledger hash discrepancy enough to determine whether it affects game membership evidence;
3. then build the corrected full relevant-FBS schedule using recovered SportsDataverse schedule bytes plus season membership authority.

Locks unchanged: no fitting; no scoring; 2025 protected; no market join; production v1 unchanged.
