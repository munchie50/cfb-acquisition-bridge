# CFB_EXECUTION_RECOVERY_20261009T215917Z terminal candidate

```json
{
  "run_id": "CFB_EXECUTION_RECOVERY_20261009T215917Z",
  "execution_class": "USER_DIRECTED_MANUAL_TEST_ROUTINE_V6",
  "boundary_utc": "2026-10-09T21:59:17Z",
  "workload_result": "RUN_PASS",
  "scope": "Original ticket recovery, downstream execution canonical handoff and procedural reconciliation only; excludes settlement, evaluation joins and natural scheduler certification.",
  "start": {
    "path": "evidence/run_receipts/CFB_EXECUTION_RECOVERY_20261009T215917Z_RUN_STARTED.md",
    "sha": "db575c2265ac807caae37805bb6a011c4013e224"
  },
  "source_audit": {
    "path": "evidence/operational/CFB_ORIGINAL_TICKET_EXECUTION_RECOVERY_2026-10-09.json",
    "sha": "2ea1f35c353665c373eb19961aa52692f680dbea"
  },
  "canonical": {
    "path": "evidence/operational/CFB_EXECUTION_LEDGER.md",
    "sha": "f56be836e12fa28a737da8f4c70320726be04875"
  },
  "control_readbacks": [
    {
      "path": "evidence/CFB_ENGINE_ADAM_SCREENSHOT_INGESTION_BOUNDARY_v1_224.md",
      "sha": "214d899d7213ec07024b1b303a799b65125ef5d3"
    },
    {
      "path": "evidence/CFB_ENGINE_HOLISTIC_SYSTEM_QA_MAP_2026-09-30.md",
      "sha": "d865cca537005c3b07a14bc8af9cd44c2e575bb1"
    },
    {
      "path": "evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md",
      "sha": "1c4ea311ad20e29d351fe2d1c74bdbe86fd4adbb"
    }
  ],
  "reconciliation": {
    "original_images": 12,
    "actual_wagers": 11,
    "excluded_market_boards": 1,
    "stake_cents": 3345,
    "unique_image_hashes": 12,
    "unique_ticket_identities_visually_checked": 11
  },
  "planned_append_metadata": [
    {
      "operation": "update_file",
      "target": "evidence/operational/CFB_EXECUTION_LEDGER.md",
      "attempt": 1,
      "baseline_blob_sha": "b2ecc4f277ce97bea8caf204a406b8073e3d6e9a",
      "proposed_blob_sha": "f56be836e12fa28a737da8f4c70320726be04875",
      "proposal_sha256": "1dbcfa90337c5bd32f292a17066d8e07abe06521405d2c8bc912a53b3592a0c7",
      "delta_sha256": "99ad87abd836e15cb386ca1a7c29598dc51ebacd0fb82dd025e009f3944cb506",
      "proposal_bytes": 4414,
      "delta_bytes": 3094,
      "proposal_characters": 4410,
      "delta_characters": 3092,
      "all_prior_bytes_preserved": true,
      "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
    },
    {
      "target": "evidence/CFB_ENGINE_ADAM_SCREENSHOT_INGESTION_BOUNDARY_v1_224.md",
      "operation": "update_file",
      "attempt": 1,
      "baseline_blob_sha": "f0caf9ca6dc2ba7fb0a155212b9c7588d6f1ef2f",
      "proposed_blob_sha": "214d899d7213ec07024b1b303a799b65125ef5d3",
      "proposal_sha256": "28640df9131414e83abfd2cd1b647a9df157a76da9bcfa0ade2ac5b3fc491493",
      "delta_sha256": "45d4ea26e8631a9e444a65036047f4bb98b929c7bbafb21ec7b4cbe66b635664",
      "proposal_bytes": 9243,
      "delta_bytes": 1597,
      "proposal_characters": 9237,
      "delta_characters": 1597,
      "all_prior_bytes_preserved": true,
      "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
    },
    {
      "target": "evidence/CFB_ENGINE_HOLISTIC_SYSTEM_QA_MAP_2026-09-30.md",
      "operation": "update_file",
      "attempt": 1,
      "baseline_blob_sha": "932cb69afde2639e12a66adebccf3dfbb8d28fbf",
      "proposed_blob_sha": "d865cca537005c3b07a14bc8af9cd44c2e575bb1",
      "proposal_sha256": "addce967120f5424c58771eb708d7da37e5291dd1905072d0479a9b18baf0830",
      "delta_sha256": "8ba7a3a22e849c3bac1b11f7004e64c579247588bcc65926f90b84d825d5647e",
      "proposal_bytes": 31466,
      "delta_bytes": 1863,
      "proposal_characters": 31410,
      "delta_characters": 1859,
      "all_prior_bytes_preserved": true,
      "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
    },
    {
      "target": "evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md",
      "operation": "update_file",
      "attempt": 1,
      "baseline_blob_sha": "9da35f5fff6597687a974fcad385de91740a94dd",
      "proposed_blob_sha": "1c4ea311ad20e29d351fe2d1c74bdbe86fd4adbb",
      "proposal_sha256": "89a25b053c22f1e046da280271631d4d80055751368f63f64024b0aa730c6c92",
      "delta_sha256": "b51349511af93cd40f91bf9541a04363eb7841d80b51b5e0ec62cd2aaa60d3b3",
      "proposal_bytes": 30327,
      "delta_bytes": 1618,
      "proposal_characters": 30291,
      "delta_characters": 1618,
      "all_prior_bytes_preserved": true,
      "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
    }
  ],
  "topology_readback": {
    "all_task_controls_preserved": true,
    "enabled_count": 4,
    "task_count": 11,
    "health_last_run": "2026-10-08T21:42:54.461403+00:00"
  },
  "repository_integrity": {
    "baseline_tip": "0e64f5c4db1ecc98330fc983b684dcf657bcfda8",
    "current_tip": "54aa1f144fa587af812a8a41daf7662e8ea92d43",
    "changed_paths": [
      {
        "path": "evidence/CFB_ENGINE_ADAM_SCREENSHOT_INGESTION_BOUNDARY_v1_224.md",
        "sha": "214d899d7213ec07024b1b303a799b65125ef5d3"
      },
      {
        "path": "evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md",
        "sha": "1c4ea311ad20e29d351fe2d1c74bdbe86fd4adbb"
      },
      {
        "path": "evidence/CFB_ENGINE_HOLISTIC_SYSTEM_QA_MAP_2026-09-30.md",
        "sha": "d865cca537005c3b07a14bc8af9cd44c2e575bb1"
      },
      {
        "path": "evidence/operational/CFB_EXECUTION_LEDGER.md",
        "sha": "f56be836e12fa28a737da8f4c70320726be04875"
      },
      {
        "path": "evidence/operational/CFB_ORIGINAL_TICKET_EXECUTION_RECOVERY_2026-10-09.json",
        "sha": "2ea1f35c353665c373eb19961aa52692f680dbea"
      },
      {
        "path": "evidence/run_receipts/CFB_EXECUTION_RECOVERY_20261009T215917Z_RUN_STARTED.md",
        "sha": "db575c2265ac807caae37805bb6a011c4013e224"
      }
    ],
    "unexpected_changes": [],
    "model_scientific_paths_changed": false
  },
  "test_routine_demonstration": {
    "trigger": "Health natural window pending; H3 ledger empty despite prior wager evidence.",
    "expected": "WAIT sweep finds genuinely independent work; recover original source ancestry, classify/deduplicate and persist exact downstream facts without inventing missing evaluation fields.",
    "actual": "12 original images reconciled to 11 actual wagers plus one excluded board; exact ticket values and $33.45 stake matched canonical readback; one explicit live ticket excluded from pregame evaluation.",
    "result": "MANUAL_ANCESTRY_AND_CANONICAL_HANDOFF_DEMONSTRATED",
    "natural_intake_producer": "DEMONSTRATION_PENDING"
  },
  "remaining_debt": [
    "production/sandbox classification",
    "exact receipt timezone",
    "independent kickoff classification for non-live-labelled tickets",
    "genuine pre-event Champion/decision linkage",
    "authoritative settlement and CLV where eligible",
    "future screenshot intake producer demonstration"
  ],
  "health": "No new completion evidence at snapshot; start window still open until 17:30 CT.",
  "terminal_candidate_self_readback": "Not certified here; separate closure required after independent fetch.",
  "scientific_effect": "NONE",
  "champion_effect": "NONE"
}
```
