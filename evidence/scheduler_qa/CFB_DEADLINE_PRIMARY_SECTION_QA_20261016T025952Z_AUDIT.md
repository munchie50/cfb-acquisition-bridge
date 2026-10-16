# Deadline anti-drift and earliest-open-section QA

Cycle: CFB_DEADLINE_PRIMARY_SECTION_QA_20261016T025952Z
Observed start: 2026-10-16T02:59:52Z
Scope: user-directed manual Test Routine; no new source retrieval, decision, wager, model, clock constraint, task or schedule.

## Reproduced gaps

Actual saved canonical V2 fixtures accepted a hypothetical Friday18:01Z INCONCLUSIVE packet after the caller moved all three Friday reconciliation deadlines from18:00Z to19:00Z. No canonical mutation occurred in that replay. The existing future-deadline check alone allowed that bypass. New tests reproduced missing enforcement of later saved cutoff/removal too. Separately, the current primary sheet rendered closed Tuesday/Wednesday/Thursday sections ahead of open Friday, despite the user-facing earliest-active requirement.

Eight new tests were written before correction; seven failed on old code, with the valid earlier-deadline case already passing. The new historical-chain guard rejects later reconciliation while INCONCLUSIVE and removal/extension of a saved planning cutoff. It accepts earlier clocks subject to all existing checks, and adds no automatic PASS or actionable/WAIT permission. Independent cutoff authority stays unverified. V2 presentation now labels/places open sections first, followed by all closed/historical groups. Every governed row stays exactly once; V1 presentation unchanged.

## Pre-write and readback proof

-81 local current/new tests PASS (42prior protocol+39weekly/handoff/deadline/primary cases).
-Existing12authentic legacy and25full-board checks remain in existing CI; final complete CI proof recorded in terminal closure.
-Current market/decision/execution/scorecard freshly fetched with exact expected identities before rendering.
-Whole source-derived render equality and original bootstrap PASS.
-Original accepted archive independently hashed772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf;51predictions+11exclusions,153numericfields/51directions PASS.
-All62complete nine-column game row strings match the prior2142CTsheet exactly by directed game identity. Only section ordering and primary label changed. No quote/deadline/cutoff/prediction/decision rewritten.
-New sheet persisted/read back atd77593db60efe74b483999f90f087fed87e75a14, first governed section FRIDAY.
-Validator6d66c48b7984d94b00a49ad4884802d4a324e024, tests6be347cea655c6c0b7e8c3038fa25c4c046f9fa7, active contracta632393ea02613225eee39c4724a6f2ca9641867 independently read back.

## Scope limits

This closes tested enforcement/presentation gaps, not actual runtime availability or natural scheduled adoption. Saved observations remain their original clocks; no freshness claim. Earlier incomplete cycles and historical primary views remain preserved. Broader source, consensus/Caesars, actionable/WAIT, practical-cutoff authority, historical closure and model acceptance remain separate. Next natural Monitor proof remains Friday07:00CT. Four existing task schedules unchanged.

Exact proposal/validation evidence:
```json
{
  "actual_validation_utc": "2026-10-16T03:01:41Z",
  "sheet_path": "evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-15_2201CT.md",
  "source_market": "2daa4415d1c2877fa27af207d1678c41863f5b06",
  "source_decision": "d09c1cbdb17111fcfa67c0f01df6c2e2bf0d9e46",
  "old_sheet": "7089e9253ce6bca81210f3227e7b0d1e748f78ad",
  "new_sheet": "d77593db60efe74b483999f90f087fed87e75a14",
  "all_62_entire_game_rows_unchanged": true,
  "first_section": "## FRIDAY",
  "render": {
    "verdict": "PASS_NEUTRAL_CANONICAL_PRESENTATION_ONLY",
    "games": 62,
    "sheet_blob": "d77593db60efe74b483999f90f087fed87e75a14",
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
    "sheet_blob": "d77593db60efe74b483999f90f087fed87e75a14",
    "scope": "original frozen fields/exclusions only; publication cycle, market/decision/cutoff/current-source truth NOT accepted"
  }
}
```
