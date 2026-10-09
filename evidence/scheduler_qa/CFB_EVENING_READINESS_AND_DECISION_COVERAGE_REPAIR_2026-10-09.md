# Evening readiness and decision naming coverage repair — October 9, 2026

Run: CFB_EVENING_READINESS_QA_20261009T231915Z
Prospective boundary: 2026-10-09T23:19:15Z / 18:19:15 America/Chicago.
Scope: user-directed bounded test routine; no production engine rerun.

## Reproduced issue and repair
The prior decision coverage helper accepted only the eight-column research slate and rejected repeated named ledger references as ambiguous. A read-only reproduction against the original research slate and current append-only ledger failed with ValueError: ambiguous named ledger record. Current production has nine columns.
The corrected helper accepts consistent eight- or nine-column schemas and known research/production section headings, resets section context on unknown headings, and retains repeated references as naming coverage with named_ledger_occurrences. It does not select the latest decision or certify a hard cutoff. Duplicate slate identities, mixed schemas and invalid bucket counts fail closed.

## Demonstration
Ten local and independently observed GitHub regression tests passed: both schemas, repeated/conflicting history as naming-only, missing names, future defaults, naive timestamp rejection, missing authority, duplicate identities, bucket counts and mixed-schema rejection.
GitHub push run 38003899594, job 114068171172 at commit a34fbfa1674cdd16c28cfb67a0755ff6606b012d completed success. Independently fetched job logs show 20 presentation/diff tests, 10 naming coverage tests and 7 frozen-value tests passed, plus original research gate and current production audit: 49 modeled rows, 147 frozen numeric values and 49 favorite directions. Accepted archive SHA256 772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf verified on runner. This is post-write repository QA, not natural production closure or fresh market validation.
Workflow: https://github.com/munchie50/cfb-acquisition-bridge/actions/runs/38003899594

## Read-only current audit at prospective boundary
The nine-column current slate has 49 rows, 15 named ledger records and five games with repeated named references. All 31 later-Saturday default deadlines are future: 17 afternoon games default October 10 07:00 CT; 14 evening games default October 10 13:00 CT. Earlier game-specific execution/travel cutoffs remain unextracted and unverified; these defaults cannot override them.
Timing counts: 7 saved scheduled kickoff boundaries passed; 4 Thursday review days passed; 7 Friday review days with no exact invented deadline; 31 other/future windows. These counts neither establish actual starts/results nor select latest decisions.
Current ledger closes five Friday and seven Saturday morning games PASS; later 31 remain INCONCLUSIVE. The 15 named record count is only helper naming coverage, not complete ledger decision reconciliation or 15 qualified decisions. No new BET/WAIT, wager or extra casino trip is earned.

## Evening readiness
Exactly four enabled production schedules remain. Market Monitor 07:00/13:00 CT; Evening Availability Wednesday/Thursday/Friday 19:30 CT flexible start window through 20:30; Health daily 16:30 flexible; Weekly QA Saturday/Sunday/Tuesday 09:00 exact. Tonight's evening task is not due at the measured boundary and cannot be called late before its window ends. Future execution/success is not guaranteed.
Today's natural Health cycle CFB_DUAL_ENGINE_HEALTH_20261009T221353Z has independently observed separate RUN_PASS closure. That does not prove tonight's availability cycle or repair older missing/failed cycles. October 9 morning Monitor STARTED-only/reported failure and October 8 failures remain historical gaps. Opaque production write rejection cause remains OPEN.

## Exact inputs and installed outputs
- Hot Sheet evidence/operational/CFB_WEEK6_HOT_SHEET_2026-10-09_1538CT.md: eaeded90f81dd1190e0ef77fc52a448f73ea5dca; underlying market retrieval about 13:02 CT, not fresh at this QA time.
- Decision ledger: fcbdc7f48e8518dc6826d0d39c06d864da1a12e9.
- Cadence v1.237: 1fdecbe7d873876b6dbe2dd18e23d56256f5117a.
- Helper scripts/cfb_week6_decision_coverage_audit.py: a0585239ffd72a289d30523e7563e96ec694f107.
- Tests scripts/test_cfb_week6_decision_coverage_audit.py: 2d9b85185c223fd908332f0c551a1342b3e29b33.
- Existing QA workflow: ab768c50cf7c434283f2b83c4a654e13f120baeb.
All code writes independently read back at returned commits; terminal closure requires current-main verification and applicable evidence readback. Full audit JSON is companion CFB_EVENING_READINESS_COVERAGE_2026-10-09.json.

## Boundaries
Production Routine v5 remains active; v6 remains candidate. Champion v1.193 and FIRST_FROZEN v1.208 unchanged; S2 study-only; 2025 TEST unopened. Original raw/preflight artifact 403/1010 clock-cause investigation remains RUN_INCOMPLETE; no alternate access attempted. Frozen-vs-operational clock separation remains governing.
No source freshness, execution prices/thresholds, settlement, latest-state decision selection, natural Monitor changed-sheet enforcement or future-week wiring is certified. No canonical market/decision/execution/scorecard/Hot Sheet, task prompt/schedule or scientific state changed. Installation and bounded repository QA demonstrated; natural production use remains pending.
