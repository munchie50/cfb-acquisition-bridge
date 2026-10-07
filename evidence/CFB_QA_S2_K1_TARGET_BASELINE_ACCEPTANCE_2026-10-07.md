# CFB QA — S2_K1 Target-Baseline Acceptance — 2026-10-07

Status: ACCEPTED TARGET-BASELINE SUBSTRATE / S2_K1 REMAINS STUDY-ONLY
Scope: exact same-cutoff target-baseline candidate from natural Tuesday artifact 11423386216.

## Identity
- Natural workflow run: 37485273952
- Candidate artifact: 11423386216
- Parent accepted S0 boundary: `CFB_QA_WEEKLY_REFRESH_ACCEPTANCE_2026-10-07`
- Cutoff: `2026-10-06T15:11:29.838398+00:00`
- Candidate target-baseline SHA-256: `415b96d9b336232094e32f07ce653454f1afa78652b3b996e20f685ad37ea78d`

## Independent audit
The repository's independent target-baseline acceptance logic was executed against the exact natural Tuesday artifact.

Result: `PASS_S2_K1_TARGET_BASELINE_ACCEPTANCE`

Verified:
- 996 target-side rows and exact S0 target-side identity reconciliation;
- 17 frozen baseline features;
- all baseline values independently reconstructed to absolute tolerance 1e-12;
- UTC-calendar-day strict-prior population;
- rest_days reconstructed same-team/same-season;
- candidate file hash reproduced;
- no target rows used as population baseline;
- target outcomes unopened;
- market unjoined;
- wager/execution unjoined;
- protected 2025 TEST unopened;
- no fit or optimization.

## Scientific boundary
This accepts only the S2_K1 target-baseline substrate for this cutoff. It does not produce or accept S2_K1 predictions, does not promote S2_K1, and does not alter Champion v1.193 or production betting authority.
