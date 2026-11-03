# Week10 early candidate independent structural audit

Source: GitHub Actions 41551746133, artifact 13193176113, ZIP 18 entries. Produced cutoff 2026-11-03T00:17:26.895461+00:00. This is after Monday 2026-11-02 19:06Z scheduled closure and cannot retroactively change that result.

Independent local artifact extraction, JSON/CSV inspection, and SHA256 reproduction:
- All 17 package-manifest file hashes reproduced, zero mismatches.
- S0 manifest six output SHA256 values reproduced.
- Target ledger: 266 unique future targets; 264 eligible fair prediction rows; 2 excluded, disjoint and exhaustive; 532 team-side ledger rows; 530 chronology rows.
- Exclusions 401856750 and 401856746 both away_opening_no_prior.
- Every target kickoff after frozen cutoff; predictions finite, win probabilities within [0,1].
- Context manifest: 4272 context, 1244 derived and 1244 mechanical rows. Baseline: 532 target-side rows. Producer manifests remain EXECUTED_NOT_ACCEPTED; package explicitly states scientific_acceptance false, market_joined false, S2 predictions false.

Disposition: PASS_BOUNDED_STRUCTURAL_AUDIT_ONLY. Full independent scientific acceptance is **NOT EXECUTED**: governed acceptance script scripts/cfb_qa_weekly_refresh_acceptance.py additionally requires pinned fit coefficients/scaling and independent recomputation, not present inside candidate ZIP. Do not promote accepted prediction pointer, freeze Champion, authorize market decisions, publish Hot Sheet, or mark Monday Market Monitor RUN_PASS on structural results.

Next exact dependency: recover independently pinned Champion fit artifact and run full scripts/cfb_qa_weekly_refresh_acceptance.py against extracted s0/, raw/, fit/; inspect its output and independently verify acceptance before pointer promotion. Then current material/venue/offer qualification and guarded six-market decision/publication.
