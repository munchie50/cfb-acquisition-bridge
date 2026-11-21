# Week12 direct Git blob recovery verification — Nov21 2026

Status: READ_ONLY_RECONSTRUCTION_VERIFIED / NOT_CANONICAL_PUBLICATION / NO_BET. This is a material unblock of large-file retrieval, not an accepted production run.

## Actual connector operations
1. GitHub contents fetch of evidence/operational/CFB_DECISION_WAIT_LEDGER.md reported SHA 6862be6a1bd88a3290b1e90a49c33a7a87e92559 but an empty text body. Do not infer empty ledger.
2. GitHub fetch_blob(6862be6a1bd88a3290b1e90a49c33a7a87e92559) returned 3,605,685 characters of full canonical ledger.
3. GitHub fetch_blob(98941e228072e6941b1c33e42d4d8dba570f7182) returned 3,669,052 characters of reconstructed Week12 ledger.
4. Exact string prefix comparison matched all 3,605,685 canonical characters. Reconstructed appended tail is 63,367 characters, beginning with typed ```cfb-week12-decision-v1 packet. The tail parsed as exactly one JSON packet with schema CFB_WEEKLY_CONDITIONAL_DECISION_V3, cycle CFB_MARKET_MONITOR_20261120T204508Z, as_of_utc 2026-11-20T20:50:24.828310+00:00.
5. Parsed 70 rows, 70 unique game_id values, 68 PASS, 2 CONDITIONAL; 66 rows have null planning_cutoff_utc. No prospective decision deadlines inferred or repaired.

## Independent boundary and first remaining failure
The exact reconstructed decision Git blob is already fetchable from GitHub object storage. This is an identity-addressed read, not proof the current canonical file pointer selects it. The paired reconstructed market blob c81855dc8f3ff002082e9c105b2d8d9c2e9bc684 returned GitHub 404 via fetch_blob in this same continuation. Thus the complete paired overlay could NOT be independently reverified from both reconstructed Git objects here. It may be recoverable from retained base and delta sources, but that has not been demonstrated in this invocation.

Canonical decision file still points to 6862be6a1bd88a3290b1e90a49c33a7a87e92559, not reconstructed 98941e228072e6941b1c33e42d4d8dba570f7182. No write to canonical ledger, recovery index, or accepted Hot Sheet was attempted. Existing original binding/selector gates still govern.

## Operational result
Large-file connector workaround VERIFIED for decision ledger. Historical Week12 decision payload integrity/denominator verified. Paired market blob retrieval NOT_EXPOSED from GitHub object API (404), full selector and canonical publication BLOCKED, current six-side venue-qualified offers unavailable, approved wagers 0. Do not equate 68 historical PASS with current executable recommendations. No DNS, new task, model mutation, or retrospective cutoff change.
