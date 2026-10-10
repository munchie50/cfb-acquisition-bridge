# Current saved decision projection — October 9 Test Routine QA

Run CFB_HOT_SHEET_DECISION_PROJECTION_QA_20261010T011249Z; started 2026-10-10T01:12:49Z (2026-10-09 20:12:49 CT). Manual downstream presentation/QA scope.

## Defect and correction
The retained 15:38 weekly Hot Sheet still displayed older inconclusive decisions after the canonical 19:53:50 dinner review. The new full weekly view evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_2012CT.md presents all 49 modeled weekly games, all 38 Saturday side/total verdicts, and three conditional controlled-Beta recommendations: App State -10 or better, UMass +4.5 or better, Fresno State +7 or better; maximum price -115 each. Other35 Saturday sides/all38 totals PASS; Nebraska separately unmodeled. Rice/ECU noon CT correction is retained.

This is a new decision presentation, not new market retrieval. Table quotes remain approximately13:02 CT canonical observations; top recommendation benchmarks remain prior19:46–19:53 ESPN/DK retrievals. Offer update times/actual Caesars executability remain unverified. Worse actual line/price means PASS. Full dinner review remains RUN_INCOMPLETE for actual execution/final availability readiness.

## Exact independently recovered inputs/output
- New Hot Sheet blob1575bdc9e386d8cced3a223a875e2d1a81f7f00c; commit734e494179da5e2c29509002017d4ebb28533f52.
- Prior weekly baseline eaeded90f81dd1190e0ef77fc52a448f73ea5dca.
- Canonical market bbc222ec291ba1faff3f083f6da132d8e8214cae; decision6d5f70c5b8c9d0bf49dd8853f581a0357321a497.
- Full dinner report020a377974b8b04edcc607bf0180da9c0666637c.
- New guard scripts/cfb_hot_sheet_decision_projection_gate.py blob b26f63ebb96452e23a7e2c4c8c222bfc5c48b14c; tests blob9e0d810834cf72a36b985aca8ab4a4fa445101d3.
- Existing workflow blob1d671b5e7dbc02b110809f421c1802f4bbfd6bc6, commitf1eeb483b5690e6bf13881bfa67f99f13f7027b2.
Code, tests, sheet and workflow independently fetched at their immutable commits and main with exact content/blob match.

## Executed verification
Prewrite gates PASS: exact38games/76verdicts/3conditional cutoffs;49weekly identities and seven section counts;43modeled Fri/Sat total endpoints plus1unmodeled total;49frozen rows/147numeric values/49favorite directions against authenticated FIRST_FROZEN archive SHA256772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf.

11 local regression tests PASS: stale decisions, total drift, missing conditional qualifier, looser line/price, missing Caesars-unverified label, false quote freshness, wrong decision blob, invented review cutoff and unsupported later ledger block rejected. Scope-unit mocks are complemented by independent authentic full38 coverage and real input projection checks.

Independent GitHub run38012433466/job114095198628 completed SUCCESS at2026-10-10T01:15:14Z on exact workflow commit. All exposed steps succeeded, including new11boundary tests, authentic saved projection, existing16fullscope/16navigation suites, authenticated frozen archive and retained production sheet checks. No raw job-log claim.

## Qualified boundary and remaining work
The helper validates this bounded October9 schema and exact declared canonical decision blob. Historical validation recovers declared bytes from canonical Git history; current publishing must independently reconcile latest canonical state. Unknown later schema/block fails closed pending qualification. This guard proves saved display fidelity, not betting edge, final availability, source truth/freshness or actual Caesars offer.

Exactly four enabled tasks and all retained fields unchanged on private read-only comparison. No dispatch/new task/prompt mutation. Evening19:30–20:30 flexible window remains unexpired at this QA evidence boundary; execution/success is not inferred. Existing workflow is extended, not duplicated. Natural scheduled producer use remains pending.

Active presentation contract/candidatev6/holistic navigation integration and explicit recovery checkpoint are separate append/readback obligations before terminal closure. All prior bytes preserved. Productionv5, Championv1.193, immutable FIRST_FROZENv1.208, S2study-only, protected2025TEST and actual wagers unchanged. Manual QA RUN_PASS, if separately closed, does not upgrade dinner execution readiness or older incomplete runs.
