# November 10 weekly S0 refresh acceptance

PASS_WEEKLY_REFRESH_ACCEPTANCE for the November 10 S0 REFRESH_SNAPSHOT. Independently audited 2026-11-11T02:09:36.167Z under the established production routine.

Natural Tuesday candidate run 42902388202 succeeded. Exact artifact 13801939868, 69,862,170 bytes, SHA-256 baef80458c9c57707eefadbcce674bf38b4e7c324e2f1c4de507bff76b4ff871. The candidate manifest accounts for all 17 payload files and their SHA-256 digests. The unchanged independent auditor blob fec94be67c2390a651e43e630440dd0020ca7aa6 ran against the retained source and S0 files and the frozen fit from artifact 10895838069, ZIP SHA-256 3a2cabfcd37e0bcf0cae85efc77eaa6755ffb12734d1e48c4c582ed1de375587.

```json
{
  "artifact_hashes_reproduced": true,
  "chronology_rows": 404,
  "cutoff_utc": "2026-11-10T21:10:34.773942+00:00",
  "eligible_predictions": 201,
  "excluded_games": 2,
  "fit_or_optimization_performed": false,
  "market_joined": false,
  "pbp_sha256": "5e0a79bb2fb8bfb4d9efe7aa5b8a253504d1f7e12ff71d5a139612df1826b008",
  "predictions_independently_recomputed": true,
  "schedule_sha256": "64f462842449332d63aab2713ebc45f51f90b079586f4a02920e22eadea4c8dc",
  "snapshot_type": "REFRESH_SNAPSHOT",
  "status": "PASS_WEEKLY_REFRESH_ACCEPTANCE",
  "strict_chronology": true,
  "target_games": 203,
  "target_outcomes_opened": false,
  "team_side_ledger_rows": 406
}
```

The exact candidate passed population, source hash and chronology checks. The frozen fit reproduced margin, total and win outputs within 1e-12. This acceptance covers the S0 refresh source boundary. Context and target-baseline companions retain their candidate status. FIRST_FROZEN remains the governing original prediction for decision and outcome history. Live Monitor delivery and Friday revalidation remain open.
