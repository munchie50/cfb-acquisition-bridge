# CFB_PRODUCTION_SHEET_GATE_QA_20261009T230338Z terminal candidate

candidate_terminal_state:RUN_PASS
execution_class:USER_DIRECTED_MANUAL_TEST_ROUTINE_V6
prospective_mutation_boundary_utc:2026-10-09T23:03:38Z
start:evidence/run_receipts/CFB_PRODUCTION_SHEET_GATE_QA_20261009T230338Z_RUN_STARTED.md, blob20248ca2819fd5a0e8eee26f948a3de02bbe5338
scope: boundedWeek6productionpresentationgate coverage repair andchanged-file pathtests

Code: scripts/cfb_hot_sheet_production_section_gate.py blobc6f65fe9e2689d9e5d922d8d549a2d8e4b6ba790; tests scripts/test_cfb_hot_sheet_production_section_gate.py latestblob71ee524e372c21d70327ac99173b4985bcc458d2; workflow.github/workflows/cfb_qa_hot_sheet_kickoff_section_static_gate.yml blob1168d8a5e42420dd8fdfb768c30602400104513c commit70478afaf946b967a01a63d3c5253aa60b5e72c4. Exactcommit/currentbranchreadbacks performed; currentcodecontent independentlychecked.
InitialGitHubrun38002507121/job114063665315passed originalcandidate,17regressions,current49rowproduction. Expandedrun38002666488/job114064181099 ata815b0107e8cecc9015f62dcf19ac1c70ba17e33passed20regressions andcurrent49rowproduction. Threeisolatedgitfixturesexercisechangedvalidsheet, changedinvalidsheetfailuredespitegoodbaseline, QAproseexclusion. No syntheticproductionartifact committed. Existingworkflowused; no manualdispatch/newrecurringtask.

Changedcontrol/map/recoveryreadbacks:
[
  {
    "path": "evidence/CFB_HOT_SHEET_DETERMINISTIC_KICKOFF_SECTIONING_CONTRACT_2026-09-30.md",
    "sha": "d11813bb6618e3ffa241d1ee8e7435b7d25c0c03",
    "commit": "dc3f43afe40df920883da026e8d0010e69d2c825",
    "readback": "EXACT_COMMIT_AND_MAIN_PASS"
  },
  {
    "path": "evidence/CFB_ENGINE_HOLISTIC_SYSTEM_QA_MAP_2026-09-30.md",
    "sha": "f226eb70f0664f6545779d38966f6bca1d211800",
    "commit": "fdfb94ef6f32e39d19a966344dd0470ae207e731",
    "readback": "EXACT_COMMIT_AND_MAIN_PASS"
  },
  {
    "path": "evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md",
    "sha": "efbbf774e06760967028162d544e0df06c43f802",
    "commit": "45b3eec61d006fde99f49e873a50a39f08983c2f",
    "readback": "EXACT_COMMIT_AND_MAIN_PASS"
  }
]
Finalreport/map/recoveryreadbacks:
[
  {
    "path": "evidence/scheduler_qa/CFB_WEEK6_PRODUCTION_HOT_SHEET_SECTION_GATE_REPAIR_2026-10-09.md",
    "sha": "65bfde0adeadd123712258244621db13db21271d",
    "commit": "fad03208b5fc3a6091d26765a45eee6ac8726e14",
    "readback": "EXACT_COMMIT_AND_MAIN_PASS"
  },
  {
    "path": "evidence/CFB_ENGINE_HOLISTIC_SYSTEM_QA_MAP_2026-09-30.md",
    "sha": "ba524414a390fc057214320a1aa670f804902920",
    "commit": "447249388c22f7c5e029c51f0286be98e6085627",
    "readback": "EXACT_COMMIT_AND_MAIN_PASS"
  },
  {
    "path": "evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md",
    "sha": "bd8499d452a73bcbcaeded32b63459f1695525b8",
    "commit": "4f05fa52039acb9c382079026b1306bae4ec582b",
    "readback": "EXACT_COMMIT_AND_MAIN_PASS"
  }
]
Appendmetadata:
[
  {
    "path": "evidence/CFB_HOT_SHEET_DETERMINISTIC_KICKOFF_SECTIONING_CONTRACT_2026-09-30.md",
    "baseline_blob": "3d43cc420e5f7cb4a97c687216218091f0f3f3e7",
    "proposed_blob": "d11813bb6618e3ffa241d1ee8e7435b7d25c0c03",
    "proposed_sha256": "429c53b21a82ea94606712dd36f88a459869dfba05b6d3b19357f329155b2914",
    "delta_sha256": "9ca9e2bab77a29f8d7bf2f4eb76ca8bb65616e899014c8698e47b09b614757f9",
    "proposed_bytes": 12223,
    "delta_bytes": 1364,
    "proposed_characters": 12179,
    "delta_characters": 1362,
    "prior_bytes_preserved": true,
    "inventory": [
      "game_identity",
      "provenance"
    ],
    "attempt": 1,
    "operation": "update_file",
    "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
  },
  {
    "path": "evidence/CFB_ENGINE_HOLISTIC_SYSTEM_QA_MAP_2026-09-30.md",
    "baseline_blob": "1cd9a6e2c77cd9129312f78331a873f55aa46c7d",
    "proposed_blob": "f226eb70f0664f6545779d38966f6bca1d211800",
    "proposed_sha256": "755dfd8018cf5f7e0f7c9a00c71f8bf9fcc9df5d28c10a7b88aa9d15815f2bda",
    "delta_sha256": "e77d96aad7c3e4e388d6163cb0549b8d28eea5c627ac000a3f03ef0f738bba72",
    "proposed_bytes": 38590,
    "delta_bytes": 956,
    "proposed_characters": 38516,
    "delta_characters": 954,
    "prior_bytes_preserved": true,
    "inventory": [
      "game_identity",
      "provenance"
    ],
    "attempt": 1,
    "operation": "update_file",
    "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
  },
  {
    "path": "evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md",
    "baseline_blob": "57f98c3f4eef32f83161efc59de980a7e5466c6e",
    "proposed_blob": "efbbf774e06760967028162d544e0df06c43f802",
    "proposed_sha256": "7c2c79ec5d008ea27496929e5c16d5c40b2c62cde26610a9ce92aff027a43e65",
    "delta_sha256": "639612ac14a8b987dc0f082f2558f9beb5e7a2c2ce53b9ebd7105c7353ee54b0",
    "proposed_bytes": 40363,
    "delta_bytes": 1120,
    "proposed_characters": 40327,
    "delta_characters": 1120,
    "prior_bytes_preserved": true,
    "inventory": [
      "game_identity",
      "provenance"
    ],
    "attempt": 1,
    "operation": "update_file",
    "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
  },
  {
    "path": "evidence/scheduler_qa/CFB_WEEK6_PRODUCTION_HOT_SHEET_SECTION_GATE_REPAIR_2026-10-09.md",
    "baseline_blob": "bf9e1f10ea74c74224e07f077b07feba78c1fe27",
    "proposed_blob": "65bfde0adeadd123712258244621db13db21271d",
    "proposed_sha256": "adee3cc21db23005b3ab0f8d1410491e4b690a00c77701d2eda4c22d28a05000",
    "delta_sha256": "f03c33049541926e22faa0efda9394413b791396ae6f65e5f2158f9ca6ed287c",
    "proposed_bytes": 4177,
    "delta_bytes": 907,
    "proposed_characters": 4175,
    "delta_characters": 905,
    "prior_bytes_preserved": true,
    "inventory": [
      "provenance"
    ],
    "attempt": 1,
    "operation": "update_file",
    "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
  },
  {
    "path": "evidence/CFB_ENGINE_HOLISTIC_SYSTEM_QA_MAP_2026-09-30.md",
    "baseline_blob": "f226eb70f0664f6545779d38966f6bca1d211800",
    "proposed_blob": "ba524414a390fc057214320a1aa670f804902920",
    "proposed_sha256": "84c4e71291d479c41de7c0a39a13f41334c22f4c1005856b217476f40e1626d9",
    "delta_sha256": "256b540678ce256e8e094f6687919391b8f4b7d4352529f0a9260fae24d096f7",
    "proposed_bytes": 39289,
    "delta_bytes": 699,
    "proposed_characters": 39213,
    "delta_characters": 697,
    "prior_bytes_preserved": true,
    "inventory": [
      "provenance"
    ],
    "attempt": 1,
    "operation": "update_file",
    "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
  },
  {
    "path": "evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md",
    "baseline_blob": "efbbf774e06760967028162d544e0df06c43f802",
    "proposed_blob": "bd8499d452a73bcbcaeded32b63459f1695525b8",
    "proposed_sha256": "5dce56b5b1ec1fa01034798940de5ba3719a73ee3d3975421a0c6c79bc559d96",
    "delta_sha256": "6b3f2d8ef97f88388757ae6d4f7a2b19a25bc35f1e538a85ee53af96739b05d2",
    "proposed_bytes": 41087,
    "delta_bytes": 724,
    "proposed_characters": 41051,
    "delta_characters": 724,
    "prior_bytes_preserved": true,
    "inventory": [
      "provenance"
    ],
    "attempt": 1,
    "operation": "update_file",
    "status": "PROPOSED_ONLY_NOT_WRITE_SUCCESS"
  }
]
Unchangedoperationalboundaries:
[
  {
    "path": "evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1538CT.md",
    "sha": "eaeded90f81dd1190e0ef77fc52a448f73ea5dca",
    "status": "UNCHANGED"
  },
  {
    "path": "evidence/operational/CFB_MARKET_MONITOR_STATE.md",
    "sha": "bbc222ec291ba1faff3f083f6da132d8e8214cae",
    "status": "UNCHANGED"
  },
  {
    "path": "evidence/operational/CFB_DECISION_WAIT_LEDGER.md",
    "sha": "fcbdc7f48e8518dc6826d0d39c06d864da1a12e9",
    "status": "UNCHANGED"
  },
  {
    "path": "evidence/operational/CFB_EXECUTION_LEDGER.md",
    "sha": "2d2fd10af9bb25ad60b7805b39638dc08f011b8c",
    "status": "UNCHANGED"
  },
  {
    "path": "evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md",
    "sha": "6ae881224fa18b65a4408fa807a2582aebccf6fd",
    "status": "UNCHANGED"
  }
]
Tasks:{"comparisons":66,"inventory":11,"enabled":4,"result":"UNCHANGED"}

HelperPASS ispresentationidentity/sectiononly: pinnedWeek6modeledset, validclock/daybucket, noomitted/duplicate/substitutedgames, explicitunresolvedbucket, mandatoryseparateNebraska. Sourcefreshness/frozennumeric/quote/decision/effectivedeadlinegates remainseparate. CIpostwritechecksdo notreplaceproducerprospectivequalification/two-phaseclosure. NextgenuineMonitorchanged-sheetenforcement andfutureweekacceptedbaselinepending. Existingrawclock403/1010causeinvestigation andhistoricalincompleteclosuresremainOPEN. No currentHotSheet/market/decision/wager/scorecard/model/scientific/clock/deadline/schedulerchange. Candidatecannotcertifyownpersistence; separateclosureafterreadbackrequired.
scientific_effect:NONE
champion_effect:NONE
