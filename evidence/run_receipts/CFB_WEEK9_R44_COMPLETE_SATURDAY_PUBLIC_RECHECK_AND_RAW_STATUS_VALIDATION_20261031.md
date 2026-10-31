# CFB Week 9 R44 — complete 32-case prospective public-market recheck and raw official-status validation
**RUN_INCOMPLETE. No newly qualified Champion six-market decision rows, no qualified 35-case packets, no approved bets, no new Hot Sheet.**

Receipt prepared 2026-10-31T06:13:23.527Z UTC. All quote times below are **scrape response observed-by times**, NOT sportsbook operator price-update times, venue executable-offer timestamps, or conference publication times.

## Authority, last-good / first-bad, controls
- Fresh GitHub main before write `e473d0d2a0ab1734bc068ede3f33b1eff5a40e11` (R43 last commit), R14 accepted frontier blob `757811e4a6a5028e2d274edaf417706f79cac46a` directly read; R24 manual-producer receipt blob `01ef94397d3d38d6a3592700d424ab687df312af` and Oct30T010121Z successful closure blob `fa58881ff423b21d5ae507d38cb42898f668da49` read. Production Routine v5.1, controls v1.132/v1.133.
- Last-good: October29 20:08 CT governed manual comparative-review publication (56 identities, 35 then-future, 210 branches, 32 bounded PASS, three conditionals); selected 45/45 CI previously passed. No missing automated selector is required by this precedent.
- First-bad: no genuinely current **qualified** 56 six-market manual decision rows, no 35 fully certified packets, no user-authenticated executable venue quote/limit, no 900-second fresh full-slate CBS capture. This is missing evidence/authority, **not proven code defect**. Frozen Champion and original limits immutable.
- Current main tree independently enumerated 1,828 entries, untruncated. Protected market blob `69caf5b1184eedccc90be7562e4a3bd7cb8b7375`, decision blob `bb5a9cc83b6a1425dc2972ca84b33aa2bbbf8fa9`, accepted Hot Sheet `f05173046e51ab9634d47b1be5fe90c2a5026c96`, recovery index v245 `57327859afb17ca42451189d3661f4c16fae4f90` confirmed in main tree before write. No canonical mutation.
- All 16 prior materially drift-flagged games retain flags. Three already started games (Tulane/Charlotte, Baylor/UCF, Kent State/Sacramento State) remain EXPIRED_NO_RETROACTIVE_APPROVAL. No normalization or historical preflight rerun.

## Complete one-pass prospective public display recheck
**32/32 still-prospective cases** retrieved from exact previously established FanDuel public team pages with `maxAge=0` by 2026-10-31T06:12:44Z; **29/32** show six public spread/moneyline/total branches (**174 displays**), **3/32** unavailable (Auburn/Ole Miss, Southern Miss/UL Monroe, UTEP/North Dakota State). These are public displays only; no operator update clock, user venue authentication, executable limit, calibrated six-market recommendation, or qualified decision.
Against R26 public-page observations by 03:16:55Z, **four games show ML display differences** (two already established in R40, two newly observed below), **25 populated games unchanged**, and three still unavailable. This is same-public-page *observation delta*, not proof of bookmaker update timing or eligible wager.

| Game ID | Prospective case | Scrape ID | Observed by 2026-10-31 UTC | R26 comparison / blockers |
|---|---|---|---|---|
| 401858278 | SMU @ Syracuse | `01a19096-0176-744f-996c-5fab87552be2` | 06:11:58 | UNCHANGED |
| 401858502 | Wisconsin @ Iowa | `01a19096-0176-7729-ba00-83e98aff7b18` | 06:11:58 | UNCHANGED |
| 401866452 | Bowling Green @ Western Michigan | `01a19096-01d4-72de-afeb-c0a66956421b` | 06:11:58 | UNCHANGED |
| 401858503 | Illinois @ Maryland | `01a19094-f8fc-768b-b036-84ff2be10c77` | 06:10:49 | UNCHANGED; NOT_APPROVED; cutoff 14:00Z |
| 401856735 | Auburn @ Ole Miss | `01a19096-0176-77cd-afe9-65f522015cdc` | 06:11:58 | SIX_MARKETS_UNAVAILABLE |
| 401871096 | Marshall @ Old Dominion | `01a19096-0186-7306-a953-ec91d48a99ad` | 06:11:58 | UNCHANGED |
| 401856846 | Kansas State @ Colorado | `01a19096-095d-771b-a49b-0edd64be3e44` | 06:11:58 | UNCHANGED; QB availability material |
| 401871097 | Louisiana Tech @ South Alabama | `01a19096-0905-725e-ba84-347478f37cbe` | 06:11:58 | UNCHANGED |
| 401861966 | UConn @ Air Force | `01a19096-0949-7779-9934-22542f3c4a39` | 06:11:58 | UNCHANGED; QB replacement not certified |
| 401858283 | Stanford @ Louisville | `01a19096-099a-754c-9cb1-9918dec22439` | 06:11:58 | UNCHANGED |
| 401871095 | Southern Miss @ UL Monroe | `01a19096-0aa4-7299-823c-2f56e9529644` | 06:11:58 | SIX_MARKETS_UNAVAILABLE |
| 401860910 | Colorado State @ Utah State | `01a19096-661a-7472-9263-e8410a43b294` | 06:12:24 | UNCHANGED |
| 401856843 | Arizona State @ BYU | `01a19096-6621-743c-a5c0-68b5fe6c0083` | 06:12:24 | UNCHANGED; QB/RB availability material |
| 401856845 | Kansas @ TCU | `01a19096-6637-723d-8a5c-508c69837be1` | 06:12:24 | UNCHANGED |
| 401864531 | UTEP @ North Dakota State | `01a19096-6643-77d6-b8a3-ccb9dc57fe81` | 06:12:24 | SIX_MARKETS_UNAVAILABLE |
| 401856734 | Florida @ Georgia | `01a19096-661a-73de-9831-c9a53a3c56fa` | 06:12:24 | R40_CONFIRMED: Florida ML +340→+360, Georgia -450→-465; other four unchanged |
| 401864529 | New Mexico @ San José State | `01a19096-6cd7-71b9-bbf4-76fff6ad7098` | 06:12:24 | UNCHANGED |
| 401858508 | Nevada @ UCLA | `01a19096-6cd2-72fe-813e-53a5b45c0c4b` | 06:12:24 | UNCHANGED |
| 401858506 | Purdue @ Penn State | `01a19096-6da7-72e8-824b-6adecdbb801d` | 06:12:24 | UNCHANGED; B10 material availability discrepancies |
| 401856736 | South Carolina @ Oklahoma | `01a19096-6ec2-77e4-a51a-2bdf1dc86292` | 06:12:24 | NEW_SAME_PUBLIC_PAGE_DELTA: South Carolina ML +130→+128; Oklahoma ML -156→-152; other four unchanged |
| 401856737 | Mississippi State @ Texas | `01a19096-6f48-7245-a4b8-25e90818c3df` | 06:12:24 | UNCHANGED; MSU QB material |
| 401858282 | Miami @ North Carolina | `01a19096-7470-7359-b228-4c9dfc25ca83` | 06:12:24 | R40_CONFIRMED: Miami ML -600→-580, UNC +450→+440; other four unchanged |
| 401858509 | Ohio State @ USC | `01a19096-759a-7338-b13b-cf894a06844b` | 06:12:24 | UNCHANGED; U51.5/-115 public only; NOT_APPROVED cutoff 20:00Z |
| 401858284 | Virginia @ Wake Forest | `01a19096-b678-7365-9630-2aca165db0d7` | 06:12:44 | UNCHANGED |
| 401869846 | App State @ Georgia Southern | `01a19096-b67c-73d3-aa4b-cf3e6289df7c` | 06:12:44 | UNCHANGED |
| 401856847 | Oklahoma State @ Iowa State | `01a19096-b67e-740e-8f79-c660d5769857` | 06:12:44 | NEW_SAME_PUBLIC_PAGE_DELTA: Oklahoma State ML -345→-350; Iowa State ML +275→+280; other four unchanged |
| 401860909 | Washington State @ San Diego State | `01a19096-b68b-7119-823a-976e5c8024c2` | 06:12:44 | UNCHANGED |
| 401856733 | Missouri @ Arkansas | `01a19096-b6d8-7222-8194-4efd7bcd1581` | 06:12:44 | UNCHANGED |
| 401858504 | Washington @ Nebraska | `01a19096-bd32-73ea-a6c2-b7cd0f1d412f` | 06:12:44 | UNCHANGED; B10 material availability discrepancies |
| 401860908 | Texas State @ Boise State | `01a19096-bd60-77eb-8da4-deacaee8e9f5` | 06:12:44 | UNCHANGED |
| 401864530 | Northern Illinois @ UNLV | `01a19096-bdb6-7031-a862-d8e280178e6e` | 06:12:44 | UNCHANGED |
| 401860924 | Oregon State @ Fresno State | `01a19096-be11-7048-bffe-bef823afa86f` | 06:12:44 | UNCHANGED |

**Two newly observed ML differences vs R26:** South Carolina +130→+128 and Oklahoma -156→-152 (same FanDuel public page); Oklahoma State -345→-350 and Iowa State +275→+280. **Two R40 changes independently reconfirmed:** Florida +340→+360, Georgia -450→-465; Miami -600→-580, North Carolina +450→+440. All remaining displayed branches unchanged. None is an authenticated executable offer, and none earns approval.

## Official personnel raw-date validation / quality gate
- Fresh official Friday Big Ten report: https://bigten.org/fb/availability-reports/ (raw HTML recovered by 2026-10-31T06:12:08Z, scrape `01a19096-3447-7152-be4e-4e5670c8a102`), **FRIDAY REPORT 10/30/26**. R43 documented 20 Friday-summary versus archive Update1 cross-view discrepancies; do not treat as chronological changes.
- Independently parsed raw HTML **October31-specific** `<tr>` rows from official linked archive https://app.hdintelligence.com/?conf=B10&source=B10&sport=Football&type=archive (scrape `01a19095-810b-740a-bdec-c2fb4a1da97e`, recovered by 2026-10-31T06:11:24Z): Illinois QB Katin Houser DOUBTFUL/DOUBTFUL/-/-; Maryland Sean Williams QUESTIONABLE/DOUBTFUL/-/-; Trevor Szymanski QUESTIONABLE/DOUBTFUL/-/-; Ryan Manning QUESTIONABLE/QUESTIONABLE/-/-; Ohio State Julian Sayin OUT/OUT/-/-; Jay Timmons QUESTIONABLE/QUESTIONABLE/-/-; USC Terrell Anderson OUT/OUT/-/-. These are **archive columns**, not Friday summary statuses.
- **Extraction failure caught:** an automatically generated targeted page answer incorrectly called Sean Williams PROBABLE, Julian Sayin PROBABLE, Terrell Anderson QUESTIONABLE. Raw date-filtered archive and independently accepted R43 Friday summary contradict it. **Discard the generated answer; do not update any player status or certify a review from it.** No source-issued timestamp inferred.
- R43's Friday summary remains the separately labeled view: Houser QUESTIONABLE, Williams OUT, Szymanski OUT, Manning PROBABLE, Sayin OUT, Timmons DOUBTFUL, Anderson OUT. Final game-day columns in independently checked October31 archive remain blank. No personnel-to-Champion recalibration invented.
- Air Force Medders OUT; Johnson/Fisher starter and snap allocation remain unverified. Oct28 published coach reporting remains the last authenticated context recovered; this session found no newer authoritative starter confirmation. No six-market approval.

## Original immutable conditional gates
- Illinois @ Maryland 401858503: **NOT APPROVED**, original **2026-10-31T14:00Z / 09:00 CT** cutoff. Public Maryland +2.5/-102 (FanDuel, observed by 06:10:49Z) meets a numeric price threshold but is **not executable venue evidence**. FIRST_FROZEN Maryland home margin +6.678 vs accepted Oct27 S0 -3.246 (9.924-point reversal); material WR/OL status conflict and qualified model reasoning unresolved. Illinois QB already considered in original review. No automatic bet.
- Ohio State @ USC 401858509: **NOT APPROVED**, original **2026-10-31T20:00Z / 15:00 CT** cutoff. Public Under 51.5/-115 (FanDuel, observed by 06:12:24Z) is not an executable user quote. Frozen Champion total 58.138726 and Oct27 S0 total 56.416633 both exceed 51.5. No calibrated under edge or starter/venue proof. Do not extend cutoff.
- UConn @ Air Force 401861966: public UConn -1.5/-106, Air Force +1.5/-114, ML -113/-106, total 51.5/-110 each, observed by 06:11:58Z; Medders OUT and Johnson/Fisher replacement unresolved. Material saved away-spread flag retained. **NOT_CERTIFIED / NO APPROVAL**.

## Attempt ledger / next authorized action
| Action | Outcome | Exact blocker | Next |
|---|---|---|---|
| Fresh main, R14, R24, last-good closure, R43, canonical blob pointers, five-task status | VERIFIED; four standing enabled and temporary rescue enabled | No new current 56 qualified decisions | Preserve authority; no new selector, QA, or extra task |
| Batch A: 10 earliest prospective cases | 8 populated, two public-unavailable; all prior public quotes unchanged | User venue proof, material personnel, calibrated decision reasoning | Advance independent batch B |
| Batch B: 12 prospective cases including Ohio State/USC | 11 populated, one unavailable; two R40 ML deltas reconfirmed, one new SC/OU ML delta | Same; no operator-update timestamps | Advance independent batch C |
| Batch C: 9 remaining prospective cases | 9 populated, one new Oklahoma State/Iowa State ML delta; all other prices unchanged | Same | Preserve per-case source IDs and blockers |
| Maryland standalone quote and raw Big Ten status date-keyed audit | 1 populated, generated answer rejected, archive vs Friday statuses separated | Model sign reversal, material personnel, venue limit, final report | Revisit only when new official personnel/venue evidence arrives before original 14:00Z cutoff |
| Air Force replacement search | No authoritative named starter recovered | Medders OUT, Johnson/Fisher unresolved | Seek official announcement before practical kickoff window |
| Guarded market→decision→Hot Sheet→audit→index and selected CI | **NOT ATTEMPTED** | 0/56 new qualified current rows, 0/35 newly certified packets; no 900-second CBS full-slate or venue evidence | Only serially publish when all actual contract gates are met |

**Per-case certification frontier:** 32 prospective cases remain NOT_CERTIFIED_NO_APPROVAL (six public branches each are evidence, not earned Champion decisions), three previously elapsed cases EXPIRED_NO_RETROACTIVE_APPROVAL; **0/56 authentic newly qualified decisions, 0/35 newly qualified packets, 0 new approvals**. All 16 material drift flags retained. The accepted Thursday Oct29 Hot Sheet remains the sole accepted publication, not current Saturday execution authority.

**Next entry point:** Original Maryland 14:00Z deadline, then 16:00Z early games and Air Force replacement-QB evidence, then Ohio State/USC original 20:00Z deadline. Use existing manual comparative-review route and new authoritative inputs only; do not repeat the 32 public rechecks unless a fresh trigger, elapsed interval, or cutoff warrants it. Once no useful authorized Week9 work remains, explicitly recommend disabling temporary rescue task; keep four standing schedules intact. **RUN_INCOMPLETE.**

## Independent eligible follow-on after first R44 verification (read-only)
- Primary-source Air Force targeted search by 2026-10-31T06:13:40Z: official goairforcefalcons.com roster and earlier September/October game-note PDFs establish Josh Johnson and Howard Fisher IV as quarterbacks, **not** a confirmed October31 starter or snap allocation. The Oct28 coach report of Medders OUT and two-QB preparation remains the last useful starter-context evidence; **no new certification**. No duplicate player-status inference from a depth-chart/social post.
- Maryland official umterps.com game-center/schedule crosscheck confirms Illinois @ Maryland 2026-10-31 12:00 ET kickoff, **not** earlier than the original 09:00 CT betting-decision deadline. It does not clear the material personnel/model reversal.
- Direct scheduled-task peek: four standing tasks enabled and existing temporary rescue enabled. Market Monitor last run recorded NO_UPDATE 2026-10-30T23:50Z; its displayed last substantive RUN_PASS is an **older October29 afternoon cycle**, not proof of a current Saturday Hot Sheet. Evening Availability last recorded NO_UPDATE 2026-10-31T01:19Z, with its latest substantive receipt RUN_INCOMPLETE and typed handoff unearned. Scheduler state is **not** current production acceptance. No task or schedule changed.
- Follow-on action result: **NO_NEW_AUTHORIZED_DECISION_EVIDENCE**. Next eligible evidence must be official game-day availability/starting QB or user-authenticated executable venue offer/limit before immutable cutoffs, plus governed calibrated manual decision authoring. No new R-number or CI created merely for a no-change search.
