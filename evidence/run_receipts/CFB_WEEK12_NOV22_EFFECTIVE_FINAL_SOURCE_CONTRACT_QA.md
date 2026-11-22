# Week12 effective final source contract QA — Nov22

Status: EFFECTIVE_SOURCE_RESOLUTION_VERIFIED / QA_ONLY / CANONICAL_HOLD

## Defect and correction
Original raw CBS provenance for game 401861968 reports Old Dominion 20 at UConn 29, while NCAA official game 6604217 reports 21-29 and corrected effective rows already use 21-29. This was an intentional retained raw observation but lacked a machine-readable precedence contract, risking downstream reversion to CBS 20.

Added `effective_final_source_policy` to evidence/audits/CFB_WEEK12_CBS_FINAL_CANDIDATE_20261122_RESEARCH_ONLY.json: default CBS, unique explicit NCAA official override for game 401861968, and mandatory validation of effective row against override or raw provenance. Kept original raw CBS observation unchanged.

## Executed exact checks
- SHA-guarded source write, commit 336d59fd8a451a7cc8b29063b3fc0d5cff243822, blob 232f0c2d008a77520d78e85f066886fe28d14dfe, independently fetched and exact content matched.
- 70 effective rows, 70 raw provenance entries, 0 duplicate game IDs, 0 effective-source mismatches. Raw ODU=20, effective ODU=21 as intended.
- Rebound scoring QA source_final_candidate_blob to current source blob; commit 9dd9c32396645be0bf9d774098f17a01d393b8c0, blob a48b218b47d2d00629e7de8bd62e03d4b20f4964, readback exact.
- Rebound 13-ticket QA source_final_blob to current source blob; commit c33d430a7dcf7d02f599430c0b14ad6f46b471b5, blob 54cda4146abf0b3db0a07c6b84a828023a6645a1, readback exact.
- No game scores, frozen predictions, exclusions, model metrics, ticket grades or stake changed. Source candidate remains research-only and official per-game corroboration remains pending for other games.

## Next acceptance gates
- Complete independent ESPN/NCAA/school source reconciliation when retrieval capacity available; verify 70 exact game IDs, scores and final status with timestamps and quarantine conflicts.
- Confirm governed Week12 activation/scorecard contract; no canonical append or production mutation from this QA-only fix.
