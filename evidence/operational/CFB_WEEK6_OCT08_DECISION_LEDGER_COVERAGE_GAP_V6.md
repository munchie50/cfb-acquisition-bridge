# Week 6 decision-ledger coverage gap — Test Routine v6

Status: QA FINDING / OPEN EXECUTION DEBT; no betting recommendation or production acceptance.

Readback inputs:
- evidence/operational/CFB_DECISION_WAIT_LEDGER.md (blob 07ede9343706473b37a8b509777d68d3a27beec7)
- evidence/operational/CFB_WEEK6_OCT08_DECISION_WINDOW_AUDIT_TEST_V6.md (blob d87782f19834f4533247aa04cb7a78eeb87e7576)
- evidence/operational/CFB_WEEK6_OCT08_FRIDAY_FIVE_GAME_REQUOTE_QA_V6.md
- evidence/operational/CFB_WEEK6_OCT08_SATURDAY_DK_REQUOTE_DELTA_TEST_V6.md

## Finding
The active decision ledger contains a Sunday October 4 prospective *schedule of review boundaries* for 49 Week 6 modeled games, but its latest Week 6 decision entries still stop at Tuesday October 6 recovery. It does not contain completed prospective Thursday-evening Friday-five decisions or Friday-evening Saturday-morning-seven decisions. The separate research quote and kickoff audits verify source consistency and section membership only; they cannot close the ledger's decision obligation.

Required partition: Friday 5 → Thursday evening review and final practical Friday cutoff; Saturday morning 7 → Friday evening review and practical Saturday pre-kickoff cutoff; Saturday afternoon 17 → Saturday 07:00 CT; Saturday evening 14 → Saturday 13:00 CT. Each unresolved game must transition to a justified actionable state, governed WAIT with trigger and hard cutoff, or PASS. These review times are not themselves hard betting cutoffs.

## Blockers and disposition
No qualified executable Caesars price, accepted minimum-price/line threshold, calibrated EV, or current player/football reconciliation was established by the source QA. No retroactive recommendation is authorized. Do not label all games PASS merely because research evidence is insufficient at an earlier review; preserve INCONCLUSIVE / RUN_INCOMPLETE with explicit future gate until a valid prospective decision window. For games already underway, do not backfill pregame decisions.

This finding does not mutate the canonical decision ledger, Champion/FIRST_FROZEN, market snapshot, Hot Sheet, scheduler configuration, or wager record. Scheduler production closure remains independently OPEN.


## Executed read-only coverage checker — October 8 22:03:34 CT

Trigger: decision obligation remains open while production persistence/dispatch proof is blocked. Test Routine v6 independent sweep selected a deterministic evidence-coverage control, not another equivalent canary.

Reusable bounded QA helper: `scripts/cfb_week6_decision_coverage_audit.py`; committed 453b7ac46a414b5c4201c99775b104996016b0db; exact source readback blob e719b86009bcf474c7b6810e5e994316677ca3e3. This checker is not connected to recurring Health/Monitor execution and does not certify betting decisions.

Input bytes independently matched Git blobs:
- 49-row research slate: 9c2ae1f17bf01bcde2aa82c56c01b1431a1bd6eb; SHA-256 1ec3d91900ca8d59a26e53a18d44939320587ac997fd956e70a4a5c6918a6754.
- canonical decision ledger: 07ede9343706473b37a8b509777d68d3a27beec7; SHA-256 d81d9c73814a51fb0f70d84cede9306b42f206593152f6f98ee9bd37a558eac6.

Executed command:
`python3 scripts/cfb_week6_decision_coverage_audit.py --slate evidence/operational/CFB_WEEK6_HOT_SHEET_RESEARCH_CANDIDATE_2026-10-07.md --ledger evidence/operational/CFB_DECISION_WAIT_LEDGER.md --as-of 2026-10-08T22:03:34-05:00 --week-tuesday 2026-10-06`

Expected versus actual:
- exact unique partition 49 = 1/2/3/5/7/17/14: PASS;
- named per-game records after the Week 6 opening boundary: 3 (Tuesday one, Wednesday two). Presence does not validate decision maturity or closure;
- scheduled kickoff boundary passed: 6. This is not actual-start or final-result certification;
- Friday Thursday review day: 5, all with no named canonical record;
- other/future Saturday review windows: 38. Do not falsely classify Friday-evening Saturday review as already missed on Thursday;
- historical Week 5 records excluded from current named coverage;
- Friday review-day labels use calendar-day evidence, not an invented exact evening deadline. The source ledger does not supply a precise practical hard cutoff for each Friday game.

Friday exceptions:
- Florida State @ Louisville — scheduled Friday 18:00 CT; no named current ledger record.
- Iowa @ Washington — Friday 20:00 CT; absent.
- Washington State @ Utah State — Friday 20:00 CT; absent.
- Wyoming @ San Jose State — Friday 20:00 CT; absent.
- Iowa State @ BYU — Friday 21:15 CT; absent.

Fourteen regression assertions passed: accent and FIU aliases; Thursday review date and subsequent-day transition; both sides of explicit Saturday 07:00 and 13:00 review boundaries; Saturday-morning prior review-day distinction; timezone-equivalent kickoff equality; duplicate matchup rejection; missing Week 6 boundary rejection; naive timestamp rejection; current named-record count. Actual CLI executed with exit 0 after source persistence/readback; local source Git blob matched persisted source exactly.

Scope limits: this is Week 6 prose-aware naming coverage, not a general semantic decision parser. It fails closed on ambiguous duplicate records instead of selecting a latest decision. It cannot establish authoritative slate population independently of the retained research input, validate executable quotes, derive missing hard cutoffs, convert HOLD into WAIT/PASS, or certify decision quality. Existing explicit authority and original evidence remain governing.

Correction state: BUILT / EXECUTED / VERIFIED / SOURCE_PERSISTED_READ_BACK. Automatic producer integration: NOT INSTALLED. Natural production decision closure: OPEN. Before integration into a scheduled producer, its supported input contract and output interpretation require separate verification; no production prompt was changed.

Next prospective priority: qualify Friday market and football/availability evidence, then resolve each game under existing decision authority before its practical execution window. A research-only HOLD row or successful coverage checker cannot satisfy that obligation. No canonical ledger/market/Hot Sheet, task, prediction, wager, outcome or Champion mutation.

## October 9 morning correction — review timing versus default decision deadline

Trigger: QA recovered the canonical ledger's Thursday-evening Friday review obligation, but earlier summaries described Friday decision reconciliation broadly as overdue without composing that ledger with active deadline authority.

Root cause: incomplete authority-boundary composition. The coverage helper consumed slate and ledger only. It did not load evidence/CFB_ENGINE_EARLY_EXPOSURE_AND_LEARNING_CADENCE_CONTROL_v1_237.md, whose accepted September 29 addition supplies default reconciliation clocks. A missing exact Thursday-evening review time is not evidence that Friday has no defined default decision deadline.

Correction to prior summaries: the Thursday review day has passed; the v1.237 default Friday decision-reconciliation clock is Friday 13:00 CT, still future at 2026-10-09 07:27:26 CT. The prior missed review obligation is preserved. An earlier game-specific deadline can supersede the default when kickoff, travel, book access, availability or the portfolio plan requires it. No default or scheduled kickoff is a hard final execution cutoff.

Recovered deadline authority: v1.237 blob 1fdecbe7d873876b6dbe2dd18e23d56256f5117a; exact local input matched its Git blob and SHA-256 3f6de41e2788f7cb497f4bee854fff53d0fdeb5266a0ebcc973c39f0db9af156.

Producer correction:
- scripts/cfb_week6_decision_coverage_audit.py now requires --cadence in addition to --slate, --ledger, --as-of and --week-tuesday.
- Known active authority fragments must be unique and match recovered v1.237; missing, changed or ambiguous authority fails closed for reconciliation instead of supplying a guessed clock.
- Existing review-day timing remains separate from default_reconciliation_deadline_ct / default_deadline_status.
- Saturday-morning deadline remains event-timed: Friday evening availability review, with the contract's last-Friday-Monitor fallback if no evening run applies. No exact hour is invented.
- effective_game_deadline remains NOT_CERTIFIED_EARLIER_CONSTRAINTS_NOT_EXTRACTED. Hard execution cutoff remains NOT_EXTRACTED.
- Scope remains the bounded 49-row Week 6 research population and naming coverage; no semantic decision, source freshness, execution opportunity or current recommendation is certified.

Executed demonstration:
- 18 assertions passed across exact authority bytes, unique active deadline declarations, Friday before/at 13:00 boundaries, equivalent UTC conversion, Saturday before/at 07:00 and 13:00 boundaries, event-timed morning handling, population/naming counts, invalid authority rejection, CLI/direct-result equality and required CLI authority input.
- Actual as-of 2026-10-09T07:27:26-05:00: 49 unique rows; 3 named Week 6 records; 6 scheduled kickoff boundaries passed; Friday five Thursday review days passed with all five default 13:00 decision clocks FUTURE; Saturday-morning seven remain EVENT_TIMED_NOT_CERTIFIED; Saturday afternoon 17 and evening 14 default clocks FUTURE.
- No named Friday-five decision records were found. Defaults do not cure that coverage gap or retroactively complete Thursday review.
- Source update commit e763ceb8e6a615fbdfab1a71c89be84908122487; independent GitHub content readback and executed local source Git blob both fcd95ea762a6857e2eebc8769e2d4398d790c134.
- This helper is manually executed QA; recurring-task invocation of it is not installed or demonstrated.

Expected versus actual: PASS for distinguishing review-day duty, default decision-reconciliation timing and unqualified execution cutoffs. Prior authoritative ledger and deadlines unchanged; prior evidence retained.

Status: CORRECTED / EXECUTED / READ_BACK / BOUNDED_REPLAY_DEMONSTRATED. This is not Friday decision acceptance, a full production Hot Sheet, a natural scheduled RUN_PASS, Test Routine promotion, or closure of the production persistence defect.

Next: prospective Friday review before the applicable genuine cutoff with qualified observations and earned decision state; retain missing Thursday evidence honestly. Do not manufacture thresholds, calibrated EV, final availability or actual executions.
