# CFB Hot Sheet — Deterministic Kickoff Sectioning Contract — 2026-09-30

Status: ACTIVE OPERATIONAL PRESENTATION CONTROL
Scope: Hot Sheet construction only. No Champion/model/market/decision/execution/outcome authority changes.

## Purpose
Prevent placeholder NEXT UP sections, omitted games, duplicate games, and timezone-driven misclassification.

## Governing time
All kickoff classification is normalized to America/Chicago before section assignment. Source kickoff times must be authoritative schedule data. Do not infer an unknown kickoff.

## Required mutually exclusive sections
1. NEXT UP — THURSDAY: every governed Thursday game.
2. NEXT UP — FRIDAY: every governed Friday game.
3. NEXT UP — SATURDAY MORNING: every governed Saturday game with CT kickoff before 12:00.
4. NEXT UP — SATURDAY AFTERNOON: every governed Saturday game with CT kickoff at or after 12:00 and before 17:00.
5. NEXT UP — SATURDAY EVENING/NIGHT: every governed Saturday game with CT kickoff at or after 17:00.
6. UNRESOLVED KICKOFF: governed game whose authoritative kickoff cannot be established. Never guess a bucket.

## Exactly-once invariant
Every governed relevant-FBS game must appear in exactly one kickoff section. No duplicate membership. Sum of section membership counts, including UNRESOLVED KICKOFF, must equal governed-slate cardinality.

A Hot Sheet may not claim conforming completion when the invariant fails.

## Render requirements
Each populated section must show actual game rows, not a placeholder such as “games remain on the canonical full-slate view.”
Each row should carry, when already governed/available: kickoff CT, game, Frozen Engine, current market, total, and current decision state.
If a section truly has zero governed games, state “No governed [section] games.”
Priority/watchlist views may follow the chronological sections but never substitute for them.

## Contamination boundary
Sectioning consumes existing governed identities, kickoff data, frozen predictions, market observations, and decision states. It must not create/recompute a prediction, market observation, threshold, decision, execution, or outcome.

## Validation
Before persistence:
- normalize kickoff to America/Chicago;
- assign exactly one section;
- assert no duplicate game identity;
- assert union equals governed slate;
- assert section count sum equals governed-slate count;
- fail closed to UNRESOLVED KICKOFF when schedule authority is missing;
- persist and independently read back the Hot Sheet.

## 2026 Week 5 correction note
CBS Week 5 schedule authority establishes Thursday Oct. 1 games Western Kentucky at New Mexico State (8:00 PM ET = 7:00 PM CT) and North Texas at Tulsa (9:00 PM ET = 8:00 PM CT). Friday Oct. 2 establishes Liberty at Delaware and Pittsburgh at Virginia Tech at 7:00 PM ET = 6:00 PM CT, plus Penn State at Northwestern at 8:00 PM ET = 7:00 PM CT. These must render as actual Thursday/Friday rows rather than placeholders.

Installed under Production Routine v5 after the 2026-09-30 Hot Sheet presentation defect was observed.


## 2026-10-04 prospective football-week day coverage correction
Trigger: the Sunday 2026-10-04 07:05 CT Market Monitor recovered authoritative Week 6 Tuesday and Wednesday modeled kickoffs. The prior six-bucket contract could not classify those known kickoffs without omission or false relabeling and correctly failed closed.

This section prospectively supersedes **Required mutually exclusive sections** above for all future Hot Sheets. Historical Hot Sheets and historical RUN_INCOMPLETE receipts are not rewritten.

### Required mutually exclusive sections — superseding set
1. NEXT UP — TUESDAY: every governed Tuesday game.
2. NEXT UP — WEDNESDAY: every governed Wednesday game.
3. NEXT UP — THURSDAY: every governed Thursday game.
4. NEXT UP — FRIDAY: every governed Friday game.
5. NEXT UP — SATURDAY MORNING: every governed Saturday game with CT kickoff before 12:00.
6. NEXT UP — SATURDAY AFTERNOON: every governed Saturday game with CT kickoff at or after 12:00 and before 17:00.
7. NEXT UP — SATURDAY EVENING/NIGHT: every governed Saturday game with CT kickoff at or after 17:00.
8. UNRESOLVED KICKOFF: governed game whose authoritative kickoff cannot be established. Never guess a bucket.

Exactly-once validation now applies across all eight buckets. Known Tuesday/Wednesday kickoffs may not be placed in UNRESOLVED KICKOFF or relabeled into Thursday-Saturday. If a future governed football-week schedule contains a known kickoff on a day not covered by this superseding set, fail closed and amend the presentation authority prospectively rather than omit or misclassify the game.

Decision cadence follows the same principle: Tuesday/Wednesday games require a realistic pre-kickoff reconciliation deadline and final practical execution cutoff based on their actual kickoff window. Do not inherit a Thursday-Saturday deadline mechanically.

Scientific/Champion effect: NONE. Presentation/operational control only.


## 2026-10-08 exact-time source-conflict QA clarification
Trigger: independent primary-source recovery for Iowa at Washington found the official schedule/UW preview at 20:00 CT but Iowa game-week notes at 20:05 CT. Research evidence: `evidence/operational/CFB_WEEK6_OCT08_FRIDAY_PRIMARY_SOURCE_CONTEXT_QA.md`, independently read-back blob 6833796673dfd7a063342ec7d14f43aef744c9d3.

Before treating multiple sources as kickoff-time corroboration:
1. Normalize every observation's explicit date, time and timezone to America/Chicago.
2. Compare exact timestamps, not merely weekday or section labels. Two times in the same section can still conflict.
3. If primary sources conflict, preserve each source/time and mark exact-time qualification unresolved. Do not silently round, average, select the later time or claim an exact match.
4. Where all observations establish the same section, that section may remain established while the exact minute is unresolved. Do not falsely discard known day/section information.
5. Preserve immutable frozen timestamps. Any later operational presentation change requires separately qualified schedule evidence.
6. Do not extend an already-governed practical cutoff based solely on a conflicting later timestamp. No missing cutoff is invented by this control.
7. Sectioning/time QA is independent of final player availability, current market offer qualification and decision completion.

Bounded demonstration: actual Friday source evidence was normalized using Python datetime/ZoneInfo. Five schedule times matched the retained research; the Iowa notes observation differed by exactly +5 minutes. This demonstrates source-conflict detection against this case, not resolution of the conflict or natural production execution.
Producer-consumer demonstration remains pending at the next real Hot Sheet source qualification. Champion/scientific/decision authority is unchanged.


## October 9 canonical row-value fidelity guard — prospective
Before persisting any governed Hot Sheet, reconcile every displayed frozen fair-spread direction/magnitude, total and home-win probability to the accepted frozen source at the declared display precision; use uniquely resolved game identity, preserve explicit exclusions and fail closed on unmatched/ambiguous rows. Where useful, scripts/cfb_hot_sheet_frozen_values_audit.py supplies read-only audit support for the accepted v1.208 combined-column format; a helper PASS is not betting acceptance or source freshness.
Also reconcile each displayed market number/price/source/divergence and observation boundary with the applicable canonical market observation. Never introduce an unrecorded endpoint when rendering a range or collapse asymmetric quotes into an invented consensus. Preserve UNAVAILABLE and unverified executability. If canonical provenance cannot support a display value, correct from governed existing state or report incomplete; do not guess a replacement or silently claim a full presentation PASS.
Motivation: October 9 13:01 UCF total display 52.5–54.5 did not match canonical 53.5/54.5. Prospective 15:38 presentation correction preserved the original snapshot, quote timestamp, frozen values and decisions. Full reconciliation: evidence/scheduler_qa/CFB_OCT09_HOT_SHEET_FROZEN_VALUES_AND_CANONICAL_DISPLAY_RECONCILIATION.md.
Status: GUARDED_REQUIREMENT_INSTALLED; manual artifact/source audit demonstrated; future natural producer enforcement remains pending. No prediction, market observation, betting threshold, task cadence or Champion mutation.

## October 9 frozen-source clock versus operational schedule separation

Audit evidence/scheduler_qa/CFB_WEEK6_FROZEN_VERSUS_OPERATIONAL_CLOCK_AUDIT_2026-10-09.json, blob ddd3e4eedbc828b91fb6d35ba5c6b48511e1a2d9; run CFB_FROZEN_OPERATIONAL_CLOCK_QA_20261009T224139Z.
The original FIRST_FROZEN target start_date is immutable snapshot provenance. It is not automatically current operational kickoff authority. Preserve it alongside separately qualified operational kickoff and each source identity/timezone. Before sectioning, deadline evaluation, future/started classification or dated execution/outcome joins, recover the applicable schedule source and use its earned operational timestamp; never silently substitute a frozen start_date. No prediction rewrite or new snapshot is authorized by a clock difference.
Use exact stable game identity across schedule changes. A local-date difference must be surfaced, not silently dropped by date filtering, repaired through fuzzy matching or resolved by outcome-selected sources. If identity or operational schedule authority is missing/ambiguous, mark that gate unresolved. Preserve an earned current day/section when separately qualified evidence supports it; conflict with an old snapshot clock alone does not require discarding that evidence. Multiple current-primary exact-minute conflicts continue to follow October8rules; no later time extends an earlier practical cutoff.
Manual demonstration:49modeled current-sheet rows map uniquely to original target IDs;18clocks match,31differ, all31original2026-10-10 04:00UTC convert to Oct9 23:00CT. All38Saturday IDs and current operational displays match retainedOct8schedule evidence. This demonstrates immutable-versus-operational separation and historical evidence consistency, not fresh-source verification or the upstream cause of04:00UTC values. EarlierOct8audit labels Frozen kickoff/Frozen schedules referred to the then-saved HotSheet schedule display, not equality with originalv1.208start_date; retain that historical wording and this provenance clarification.
Status: ACTIVE_SEPARATION_REQUIREMENT / MANUAL_COMPARISON_DEMONSTRATED / NATURAL_PRODUCER_ENFORCEMENT_PENDING. Existing operational kickoff/deadline, model, prediction, scorecard, decision and schedule values unchanged.

## Week6 production section validation coverage — October9

evidence/scheduler_qa/CFB_WEEK6_PRODUCTION_HOT_SHEET_SECTION_GATE_REPAIR_2026-10-09.md, blobbf9e1f10ea74c74224e07f077b07feba78c1fe27, records the priorcandidate-only automaticgate gap and repair. scripts/cfb_hot_sheet_production_section_gate.py is read-only support for current9-columnWeek6productionformat, pinned49modeledidentitybaseline, exactdisplayday/time bucket consistency and separateNebraskaexclusion. Use this applicable helper before persistence when computationruntime isavailable; failclosed on itsunsupported/invalidschema or failedidentity/section check. A helperPASS does not qualifycurrentkickoff/sourcefreshness, frozennumericvalues, marketprices, decisionreadiness or practicalcutoffs; separatelyrecover those authorities. No originalfrozenstart_date is used for currentsectioning.
ExistingGitHubQAworkflow now validateschanged datedWeek6productionsheets afterpush, preservingoriginalcandidatecheck and17regressions. Run38002507121/job114063665315passed retainedcurrent49rows andsuite. Post-writeCI is corroboratingpresentationevidence, not a substitute for producerpre-persistencequalification or two-phaseclosure. Nextgenuinechangedproductionfile demonstrationpending; no model/decision/schedule effect. Futureweekidentitybaselines/wiring requireseparatelyacceptedqualification.

## Week6 production frozen-value validation integration — October9

evidence/scheduler_qa/CFB_WEEK6_PRODUCTION_FROZEN_VALUE_GATE_INTEGRATION_2026-10-09.md, blobcd884f1ec5f74c89c3eddbe4039f40d661ed452a. ExistingGitHubQA nowrunsacceptedv1.208archivehashverification andscripts/cfb_week6_production_frozen_gate.py ontheexactfilesselected byproductionsectiongate. Combinedchecks cover49unique modeledrows,147displayednumericfields,49favorite directions andNebraskaexclusionancestry; currentrunner38003229975/job114066003734provedpipelineand20+7regressions. Existingnumerichelper alsoacceptsUNRESOLVEDclockrows toretainknownfrozenvalueswithoutguessingkickoff; separatebucketqualificationrequired. Useapplicablefrozen-valuehelperbeforepersistencewhenruntimeavailable. PostwriteCIcorroboratesfidelity,doesnotreplaceprospectivequalificationorclosure. Week6bounded; nextnaturalMonitorchanged-file/futureweekintegrationpending. Price/sourcefreshness, operationalclock/effectivedeadline/decisiongates remainseparate. No model/taskchange.

## Week6 canonical market-total display coverage — October9

Run CFB_MARKET_TOTAL_DISPLAY_QA_20261009T233832Z; recover evidence/scheduler_qa/CFB_WEEK6_CANONICAL_MARKET_TOTAL_DISPLAY_GATE_2026-10-09.md, blob 10939df20c97ada2266216b5c905d5f5217120de. New read-only scripts/cfb_week6_market_total_display_gate.py checks exactdeclared canonicaltotal endpointsets forqualifiedOct9Week6block/cycle:43modeledFriday/SaturdayplusNebraska, preservesasymmetricpairs andrejectsunsupported/omittedendpoint. Original13:01UCF52.5–54.5rejected;existingcorrected15:3853.5/54.5passes. SourceGitblob recoveredatcanonicalpath, so laterappendsdonot falselyinvalidatehistoricalsheet. Fourteenregressions+existing37checks=51independentlypassed GitHubrun38005583878/job114073492883 at ee4b9f5a7a4b80fd4d25c814a5a82d5ba5490330; current49rows/147frozennumbers/49directions/44totaldisplayspassed. Workflowvalidates exactsection-selectedfiles. Useapplicablehelperbeforepersistencewherecomputationavailable; unknowncycle/schemafailsclosedpendingseparatequalification. This is onlytotal-numberdisplayfidelity:6earlier-weekrows,spreads/prices/ML/sourcewording/freshness/executability/decisionsnotcertified. Existingbroadercanonicalrowfidelityguardstillgoverns. PostwriteCIisnotprospectiveclosure ornaturalproduceruse; naturaldemonstration/futurephasecoveragepending. Currentcanonicalmarket/decision/execution/scorecard/HotSheetand4taskfieldsunchanged; nohistoricreceiptupgrade. Productionv5/Champion/scienceunchanged; earlierdebtspreserved.
