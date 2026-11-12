# November 12 morning Market Monitor manual catch-up

Outcome: RUN_INCOMPLETE. Scope completed in this user-directed manual invocation: verified runtime, full CBS capture, all five existing conditional spread price screens, and preliminary material scan. This is a prospective checkpoint for the 07:00 CT recovery.

## Runtime and source

- Startup: evidence/run_receipts/CFB_MARKET_MONITOR_TRACE_20261112T132300Z_manual-0700-catchup.md, blob eb751d1653cf9b5050c98d4dc91fd74d21f694da. Scheduled predecessor: evidence/run_receipts/CFB_MARKET_MONITOR_20261112T130402809Z_RUN_CLOSURE.md, blob 8776a9252f664960b0511c6bf87876be89829bfe.
- Full checkout at connector write commit 6faa795f392b32d4c732ac4468f917d06c899ce2, ancestor of origin/main and nonshallow. Verified all 56 retained immutable review references with load_review. Helper blob b13930cb714eb87c8dce6136ffab6fbceeb44898. Recovery index v1.283 blob 5a030e90df65f0261140e36920e3c89d3b0490dc.
- CBS Week 11 FBS live fetch, HTTP 200, response recovered by 2026-11-12T13:23:21.807Z. Exact extracted table bytes at evidence/operational/CFB_WEEK11_CBS_FBS_CAPTURE_20261112T132321Z.md, blob 44c7c68e4f09182b25bd16d2d34a5870095c2c74, commit 397fe77d1b370885f780454d679784e131938beb. Independent exact readback passed. Table SHA-256 5f7947d5dd18d88c3d7d51f14dd036c0ea297093f570f05ae1cec4dee653eed8. Week 11 normalizer passed against lineage blob 3a337e8bdf5cd732fb76697cf2a87b2d74ba8ce9: 67 directed matches, 134 team rows, 61 future, six started or elapsed, zero missing IDs. This is mixed-book display with unknown book update time and unverified venue execution.

## Existing conditional limits

| Game ID | Selection and original floor | CBS display | Price screen |
|---|---|---|---|
| 401856888 | Tennessee -2.5 at -115 or better | -2.5 (-114) | Within |
| 401856858 | Baylor +7.5 at -118 or better | +7.5 (-111) | Within |
| 401870752 | Jacksonville State -7.5 at -105 or better | -7.5 (+100) | Within |
| 401856883 | Georgia -15.5 at -110 or better | -15.5 (-110) | At floor |
| 401862827 | North Texas -2.5 at -105 or better | -1.5 (-110) | Exact registered offer absent, and displayed juice worse. Keep pending exact quote. |

Friday 07:00 CT review and Saturday 07:00 CT maximum validity remain the retained limits, subject to earlier practical cutoffs. A CBS screen does not qualify a same-book pair, venue availability or renewal.

## Material and next review

- Tennessee: initial SEC report as covered by Knoxville News Sentinel reported no new Tennessee injuries. Texas A&M availability and later official report remain due. https://sports.yahoo.com/articles/no-tennessee-football-injuries-sec-011819094.html
- Georgia: AJC reports Georgia DL Joshua Horton questionable and LB Amaris Williams out. Missouri's latest complete official report and later updates remain due. https://www.ajc.com/sports/2026/11/georgia-injury-report-wednesday/
- Baylor: KSL reports BYU RB LJ Martin probable and LB Isaiah Glasker questionable. Both teams' later reports and kickoff weather remain due. https://sports.ksl.com/ncaa/byu-football/byu-baylor-availability-report/578920
- Jacksonville State and North Texas: exact paired offers and current personnel remain open.
- Friday spread screen: Pitt -3.5 (-108), UCLA -10 (-108), Houston -9.5 (-110). Keep all three as research only. Pitt QB Mason Heintschel out and RB Ja'Kyrian Turner questionable in cited availability coverage. Confirm latest official version and both teams' implications before reassessment. UCLA and Houston matchups have third-party injury leads requiring direct corroboration before changing decisions. https://accsports.com/news/acc-injury-report-week-11/ and https://cfbvibes.com/injuries/
- Thursday games still present at capture: Memphis at South Florida and Louisiana at UL Monroe. Keep outside Friday trip card. Reassess only if practical Thursday access remains and genuinely new evidence merits it.

Full current six-market review, venue price and material revalidation, compiler, render, selected CI and canonical publication/readback remain open. Resume from the retained CBS source and verify any later market or report changes before authoring new rows. No new recommendations or accepted Hot Sheet in this checkpoint.
