# CFB Engine — Legacy Population Ledger Integrity Reconciliation v1.156

Status: BOUNDED DISCREPANCY / MEMBERSHIP AUTHORITY UNAFFECTED
Parent: v1.155
No fitting or scoring.

## Exact recovered ledger
Recovered v0.22 package contains population_ledger_2017_2025_pre_scope.json:
- 6,441 rows;
- season counts: 2017 736, 2018 733, 2019 734, 2020 508, 2021 732, 2022 734, 2023 750, 2024 752, 2025 762;
- direct packaged-byte SHA-256: 94a6346ba9d86d50ebbe12f458b6289c8d62255145155016439e4018fb146172.

Canonical JSON reserialization with sorted keys + indent=2 + terminal newline reproduces the same 94a6346b... hash.

## Stale embedded hash
schedule_population_audit_2017_2025.json reports:
- ledger_rows: 6,441;
- embedded ledger_sha256: 3d0fff8457664467ac548a3f831826dd450d98f26c06a08240698b146ea82ac3.

Search of the entire recovered package finds that 3d0fff... only in the audit JSON and the complete-schedule checkpoint; no packaged object has been recovered with that hash.

Therefore the embedded ledger hash is classified STALE/UNREPRODUCED rather than evidence that the recovered 6,441-row ledger is byte-corrupt.

## Impact
This discrepancy does not invalidate the independently recovered CBS membership authority:
- exact 2026 anchor recovered;
- exact transition ledger recovered;
- exact 2017-2025 season maps recovered;
- anchor-completion checkpoint independently identifies those maps as qualified for population classification.

Nor may the legacy 6,441-row FBS-vs-FBS ledger be used as Challenger-B population authority; Challenger B must rebuild v1.124's broader relevant-FBS population.

The discrepancy remains preserved as legacy artifact-integrity debt, but it is not on the corrected-population critical path unless a later reconciliation depends on exact old ledger bytes.

## Current membership state
2016: prospectively resolved by v1.155.
2017-2025: exact historical CBS membership authority recovered by v1.154.
Membership identity prerequisite for corrected population construction: CLOSED.

Next: construct corrected relevant-FBS schedule and machine-check class conformance before feature work.

Locks unchanged.
