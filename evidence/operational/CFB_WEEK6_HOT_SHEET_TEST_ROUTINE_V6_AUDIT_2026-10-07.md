# CFB Week 6 — Test Routine v6 Candidate QA Audit — October 7

Status: EXECUTED QA CHECKS / RESEARCH CANDIDATE ONLY. No production acceptance or Market Monitor RUN_PASS.

## Reproducible static checks
- PASS: rows49
- PASS: unique49
- PASS: sectionSum49
- PASS: thursday3
- PASS: friday5
- PASS: nebraskaExclusion
- PASS: noBetNow

- Canonical modeled rows: 49; distinct game identities: 49.
- Section cardinalities: Tuesday=1, Wednesday=2, Thursday=3, Friday=5, Saturday morning=7, Saturday afternoon=16, Saturday evening/night=15.
- Historical Tue/Wed games are retained for audit, not as fresh pregame opportunities.
- Candidate sourced from October 6 frozen sheet and October 7 CBS crosswalk.

## Material gaps requiring governed correction

1. CBS page has misleading generic `Final` status headers; independent schedule and event status required before labeling future games live/completed.
2. Crosswalk is spread-only. Candidate does NOT show current totals, moneylines, source capture timestamp per quote, movement from first qualified observation, or verified Caesars executable offers.
3. Candidate has no newly earned BET EARLY/BET NOW/PASS decisions for upcoming games. INCONCLUSIVE must receive prospective governed review and cutoff; do not convert raw model-vs-market disagreement to a bet.
4. The canonical decision and market ledgers are not yet updated from this candidate; the 2026-10-07 13:00 scheduled RUN_STARTED remains without verified terminal closure.
5. Nebraska Indiana @ Nebraska remains an explicit frozen exclusion. Separate display is required; do not add it to 49 modeled games.
6. The candidate does not yet include a populated priority watchlist, per-game timing triggers, or qualified parlay layer. These remain presentation acceptance gaps.

## Classification

- BUILT: 49-game research presentation candidate.
- EXECUTED: static row identity, section cardinality and contamination-boundary checks above.
- VERIFIED: candidate persisted/readback in prior commit; this audit will be independently read back.
- ACCEPTED: NO.
- PRODUCTION: NO.

## Next controlled work

Prioritize Thursday then Friday kickoff games: qualify current source quote and game status; reconcile market vs frozen only under governing betting controls; set explicit cutoff or PASS, then work through Saturday. Preserve historical failures and previous snapshots. Do not promote candidate until all acceptance checks pass.

## Subsequent sectioning correction

The original seven static checks did not validate individual kickoff bucket membership. They passed despite Old Dominion at App State (Saturday noon CT) appearing in the evening/night section. The original checks above remain historical evidence, not a current complete sectioning pass.

The research candidate was corrected in commit cc86762024132f78e984d6db842dbea2c01e0841 and independently read back. Revised counts: Tuesday 1, Wednesday 2, Thursday 3, Friday 5, Saturday morning 7, afternoon 17, evening/night 14; 49 total. Each of the 38 Saturday rows was checked against its kickoff-hour bucket. No model, market quote, or decision was changed.

Test Routine lesson: require per-row classification assertions as well as total-count assertions. Candidate remains unaccepted and the scheduled Market Monitor terminal closure remains unproven.


## Automated regression demonstration — October 8

The kickoff-section static gate script and push-triggered GitHub Actions workflow were installed at commits 7ae01d9b3b677402e1eeda05fff05f20c0074d38 and 24856476f564923d7dde5c0bc0a3afcb42130152. GitHub Actions run 37716851551 completed SUCCESS; job 113115183629 and its `Validate kickoff section membership` step both completed SUCCESS. The gate checks all 49 modeled game identities, exact section membership based on CT kickoff, duplicate exclusion, and section counts. This proves the new regression gate executes; it does not accept the research candidate for betting or resolve the ChatGPT Market Monitor scheduled-terminal defect.
