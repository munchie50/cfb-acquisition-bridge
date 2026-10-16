# Full-week typed publication repair — manual QA audit

Cycle: CFB_TYPED_WEEKLY_RECONCILIATION_QA_20261016T023112Z
Presentation correction identity: CFB_PRESENTATION_RECONCILIATION_20261016T023112Z
Publication boundary: 2026-10-16T02:42:37Z
Status: VALIDATED_AND_PERSISTED; EXISTING_CI_PENDING. Separate terminal closure must record independent CI outcome.

## Diagnosis and correction

The current canonical surfaces had valid Tuesday pregame packets followed by untyped operational tails. The pregame-only helper also rejected started games, so merely appending a new V1 packet could not safely close the whole-week publication. Added a separate weekly V2 profile while preserving V1 rejection behavior. Historical PASS rows require proved pre-event evidence; retained prices are explicitly historical. Future neutral rows still require valid future reconciliation. New source compiler accepts a complete fresh response plus all62 producer-earned decisions, writes local proposals only, and never extends deadlines automatically.

The qualified saved-source bootstrap independently binds market05ccbf405bd1d5e35a1842d718c4e45325d7bee7, decision0ed8166d1cbeab88d6e9ec5259a0c033de1f90db and complete capture6ff67e5c57060fde38509d09afbcaaf402cdb77d. It retains Thursday afternoon full-board rows and the newer Friday evening observations/material availability. The entire canonical prefix is preserved. Seven pre-event PASS decisions remain PASS;55 remain INCONCLUSIVE. One source spread/moneyline direction conflict is visible and quarantined, with the prior qualified observation explicitly retained. Three unknown first observations remain unknown; no historical first is invented. Retrieval upper bounds are explicitly RECOVERED_BY, not exact HTTP/bookmaker clocks.

## Verification

-70 local schema/authentic-weekly/advance/mutation tests PASS, plus12 authentic original legacy replay checks and25 complete-board normalizer tests PASS (107 total).
-Whole canonical-source render equality PASS across62 games; original bootstrap PASS.
-Independent accepted archive SHA256772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf recovered and hashed; original51predictions+11exclusions,153numericfields and51favorite directions PASS.
-Current market/decision full proposals validated before writes; each was immediate-fetch/SHA-guarded and independently read back. Initial market read returned the prior version after accepted commit7b55e5451de4c6bb598a9ccd8a2f19d3121429aa. No write repeated: exact-commit and main reads subsequently matched the accepted proposal.
-New Hot Sheet independently read back at7089e9253ce6bca81210f3227e7b0d1e748f78ad. Its original frozen/archive invariant and canonical render passed before publication.
-Existing QA workflow extended in place, no new task/workflow/dispatch. Source compiler/validator/contract independently read back.
-Local harness setup failures (source staging newline, team alias/availability bullet parsing, unsupported missing-first, real source conflict, missing fixture/CWD, V1-history selection in advance) were diagnosed before canonical writes. Strict failures were preserved; no accepted source number, original FIRST_FROZEN value or historical decision was changed to fit the schema.

## Earned limits

This is a prospective presentation repair from previously retained source observations, not a fresh market scan or a scheduled Monitor execution. No previous RUN_INCOMPLETE is upgraded. Natural producer adoption still needs demonstration at the next scheduled Monitor. Full production health, source truth, calibratedEV, consensus, actual Caesars execution, richer actionable/WAIT states and historical closure debt remain separate. Source rows must be fresh and decisions genuinely earned in the next Monitor; tests cannot prove those facts.

Production/sandbox exposure remains0. No prediction/model/Champion/FIRST_FROZEN/REFRESH, execution, scorecard, money or automation lifecycle mutation.

## Exact proposal evidence

```json
{
  "as_of": "2026-10-16T02:42:37Z",
  "cycle": "CFB_PRESENTATION_RECONCILIATION_20261016T023112Z",
  "sheet_path": "evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-15_2142CT.md",
  "bootstrap": "PASS_QUALIFIED_LEGACY_TO_TYPED_FIRST_OBSERVATION_ANCESTRY_ONLY",
  "render": {
    "verdict": "PASS_NEUTRAL_CANONICAL_PRESENTATION_ONLY",
    "games": 62,
    "sheet_blob": "7089e9253ce6bca81210f3227e7b0d1e748f78ad",
    "scope": "typed neutral canonical display only; no source truth/betting/natural-run acceptance"
  },
  "frozen": {
    "verdict": "PASS_ORIGINAL_FROZEN_FIELDS_ONLY",
    "games": 62,
    "predictions": 51,
    "exclusions": 11,
    "numeric_fields": 153,
    "favorite_directions": 51,
    "archive_sha256": "772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf",
    "lineage_census_blob": "d80e26c398de48e7a386ad9a627fe44f4111ac45",
    "sheet_blob": "7089e9253ce6bca81210f3227e7b0d1e748f78ad",
    "scope": "original frozen fields/exclusions only; publication cycle, market/decision/cutoff/current-source truth NOT accepted"
  },
  "proposals": {
    "market": {
      "baseline_blob": "05ccbf405bd1d5e35a1842d718c4e45325d7bee7",
      "proposal_blob": "2daa4415d1c2877fa27af207d1678c41863f5b06",
      "proposal_sha256": "bc0fd12f7e88b5e94fe9e5aafba19f6f01b4164d64767234dba2cfe6de1cb364",
      "delta_sha256": "ca2d43d0d2957c754726375bc65a64d0cbdda552b0417953c61e4cb986af42b6",
      "bytes": 370613,
      "delta_bytes": 108139,
      "prior_bytes_preserved": true
    },
    "decision": {
      "baseline_blob": "0ed8166d1cbeab88d6e9ec5259a0c033de1f90db",
      "proposal_blob": "d09c1cbdb17111fcfa67c0f01df6c2e2bf0d9e46",
      "proposal_sha256": "25c44e26d4971a4151d8e63d02d49109202000977692ae2941923a814703661e",
      "delta_sha256": "813d31eb282a54082a43adb6e709d55852575167e60d2d146060079f18818385",
      "bytes": 158279,
      "delta_bytes": 38098,
      "prior_bytes_preserved": true
    }
  }
}
```
