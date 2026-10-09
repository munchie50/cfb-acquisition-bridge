# CFB Market Monitor State

Status: ACTIVE APPEND-ONLY OPERATIONAL SURFACE
Initialized: 2026-09-27

## Recovery semantics
This is the canonical durable recovery surface for qualified CFB market-monitor observations. Append only; never reconstruct an earlier observation from a later quote or outcome.

## Required record fields
- game/market identity
- observation timestamp CT
- source/book/benchmark
- line and price
- FIRST_QUALIFIED_MARKET_OBSERVATION / INTERMEDIATE / EXECUTION / CLOSE / NOT_YET_AVAILABLE
- availability/executability
- provenance/timestamp semantics
- linked Champion snapshot identity where applicable

## Initial state
No historical Sunday observation is backfilled here. Missing earlier observations remain missing rather than being reconstructed after the fact.

## Write-path validation — 2026-09-27 13:03 CT
- Purpose: controlled repair validation for canonical existing-file mutation.
- Governance effect: none; no market observation, decision, execution, prediction, or outcome state created.
- Method: existing file fetched with current blob SHA, then replaced through SHA-guarded repository update.


## Prospective capture — 2026-09-27 13:08 CT
Observation class: FIRST_QUALIFIED_MARKET_OBSERVATION for the records below. These are the earliest qualified observations durably established after the write-path repair; they do not reconstruct the unpersisted 13:00 CT observations.
Source semantics: live web retrieval during this run. ESPN game/odds surfaces identify DraftKings where stated; FanDuel is identified directly where stated. Exact fields not established are omitted rather than inferred.
Champion link: v1.208 FIRST_FROZEN artifact 10897612260 / accepted Beta Champion lineage v1.193.

- Game 401858475 — Maryland at Nebraska, 2026-10-03 15:00 CT. ESPN/DraftKings: Maryland +12.5 (-110); total 52.5 (-110 each side shown); Maryland ML +410. Availability: executable market displayed. Champion FIRST_FROZEN: Nebraska by 10.5205; total 56.0116; Nebraska win 0.733503. Market-vs-Champion: market makes Nebraska a larger favorite than Champion by about 1.98 points; market total about 3.51 below Champion.
- Game 401856707 — Alabama at Mississippi State, 2026-10-03 11:00 CT. ESPN/DraftKings: Alabama -5.5 (-110), Mississippi State +5.5 (-110); total 59.5 (-110); Alabama ML -218, Mississippi State +180. Availability: executable market displayed. Champion FIRST_FROZEN: Mississippi State by 9.8652; total 60.0377; Mississippi State win 0.743319. Market-vs-Champion: major side disagreement; Champion favors Mississippi State outright while market favors Alabama by 5.5. Total nearly aligned.
- Game 401856705 — Vanderbilt at Georgia, 2026-10-03 11:45 CT. ESPN/DraftKings: Vanderbilt +25.5 (-110), Georgia -25.5 (-110); total 53.5 (-110); Vanderbilt ML +1700, Georgia -4500. Availability: executable market displayed. Champion FIRST_FROZEN: Georgia by 24.5805; total 57.5598; Georgia win 0.922243. Market-vs-Champion: side near alignment; market total about 4.06 below Champion.
- Game 401858473 — Ohio State at Iowa, 2026-10-03 14:30 CT. FanDuel: Ohio State -14.5 (+100), Iowa +14.5 (-122); total 43.5 (-110); Ohio State ML -720, Iowa +500. Availability: executable market displayed. Champion FIRST_FROZEN: Iowa by 6.2898; total 51.1058; Iowa win 0.593141. Market-vs-Champion: major side disagreement; Champion favors Iowa outright while market favors Ohio State by 14.5. Market total about 7.61 below Champion.


## Full relevant-FBS slate sweep — 2026-09-27 13:13 CT
- Scope: all 47 FBS-vs-FBS FIRST_FROZEN games in the Oct. 1–3 Week 5 window.
- Broad benchmark: CBS Sports Week 5 FBS scoreboard, retrieved prospectively during this run. Benchmark lines without displayed prices are retained as benchmark observations only; they do not replace the exact-book/price records already captured at 13:08 CT.
- Coverage: benchmark side/total available for 44 of 47; NOT_YET_AVAILABLE for UTSA at Rice, Utah State at Boise State, and Arkansas State at Louisiana.
- Champion comparison source: accepted v1.208 FIRST_FROZEN artifact 10897612260. Full comparison is persisted in the governed Early Board/Hot Sheet created by this run.
- Chronology: this 13:13 sweep does not backfill the failed/unpersisted 13:00 observation boundary.


## Prospective reset capture — 2026-09-29 20:20 CT
Observation class: INTERMEDIATE / NEW_PROSPECTIVE_BOUNDARY. This capture resumes governed monitoring after the unrecoverable 2026-09-28 persistence gap. It does not reconstruct Monday observations.
Source semantics: FantasyData Week 5 consensus odds page retrieved live on 2026-09-29, with direct/cross-source confirmation where noted. Source URL: https://fantasydata.com/ncaa-football/odds
Champion link: v1.208 FIRST_FROZEN artifact 10897612260 / accepted Beta Champion lineage v1.193. Frozen prediction bytes were recovered directly from accepted artifact 10897612260; no model values were recomputed from current market information.

Current priority observations:
- Western Kentucky at New Mexico State: WKU +2.5 (-108), NMSU -2.5 (-112), total 57.5. Champion: NMSU by 26.5495, total 55.5829.
- North Texas at Tulsa: North Texas +1 (-111), Tulsa -1 (-110), total 57.5. Champion: Tulsa by 15.1102, total 56.2123.
- Notre Dame at North Carolina: Notre Dame -21 (-110), UNC +21 (-110), total 47.5. Champion: Notre Dame by 3.1262, total 45.3242.
- Alabama at Mississippi State: Alabama -6 (-110), MSST +6 (-112), total 60.5. Champion: MSST by 9.8652, total 60.0377.
- Syracuse at UConn: Syracuse -6.5 (-110), UConn +6.5 (-110), total 50.5. Champion: UConn by 6.8817, total 55.6316.
- Michigan at Minnesota: Michigan -5.5 (-111), Minnesota +5.5 (-111), total 43.5. Champion: Minnesota by 5.6597, total 45.2986.
- Ohio State at Iowa: Ohio State -14 (-111), Iowa +14 (-111), total 45.5. Champion: Iowa by 6.2898, total 51.1058.
- Memphis at Charlotte: Memphis -20.5 (-112), Charlotte +20.5 (-110), total 53.5. Champion: Memphis by 10.0046, total 61.3418.
- Eastern Michigan at Massachusetts: EMU +6.5 (-112), UMass -6.5 (-109), total 48.5. Champion: UMass by 22.0802, total 49.0269.
- Old Dominion at Georgia State: ODU +1.5 (-110), Georgia State -1.5 (-112), total 50.5. Champion: Georgia State by 11.1151, total 52.7631.
- Marshall at James Madison: Marshall +18.5 (-112), JMU -18.5 (-110), total 55.5. Champion: JMU by 29.5062, total 51.9170.
- Maryland at Nebraska: Maryland +14.5 (-110), Nebraska -14.5 (-112), total 52.0. Champion: Nebraska by 10.5205, total 56.0116. Direct BetMGM cross-check displayed Nebraska -15 and total 52.5 during the same evening research window, confirming meaningful cross-book spread variance rather than a single exact universal line.
- Kentucky at South Carolina: Kentucky +3 (-116), South Carolina -3 (-107), total 53.5. Champion: South Carolina by 13.7709, total 58.7110.
- Texas Tech at Colorado: Texas Tech -13 (-113), Colorado +13 (-109), total 50.5. Champion: Texas Tech by 1.7697, total 53.2790.
- Vanderbilt at Georgia: Vanderbilt +24 (-113), Georgia -24 (-110), total 50.5. Champion: Georgia by 24.5805, total 57.5598.

Coverage repair: current broad Week 5 board now displays qualified lines for the three games that were NOT_YET_AVAILABLE in the 2026-09-27 sweep: UTSA at Rice (UTSA -11.5, total 54.5), Utah State at Boise State (Boise State -20.5, total 51.5), and Arkansas State at Louisiana (Louisiana -6.5, total 47.5). These are current 2026-09-29 observations only; they are not backfilled as Sunday/Monday observations.

Interpretation: current market disagreement remains an investigation/decision-prioritization signal only. No market data entered the frozen Champion. No missing Monday line was reconstructed.


## User-authorized extra prospective capture — 2026-09-30 ~07:12 CT
Observation class: INTERMEDIATE / USER_AUTHORIZED_EXTRA.
Boundary: new prospective observation only; the incomplete 07:01 CT scheduled cycle is not reconstructed.
Source semantics: FantasyData NCAA Football Odds Week 5 consensus board retrieved live during this cycle; CBS Sports Week 5 FBS scoreboard independently cross-checked for broad board presence and selected lines. Champion remains v1.208 FIRST_FROZEN / v1.193 accepted Beta Champion; market information is downstream only.

Full relevant-FBS board coverage: current spread/total consensus was available for all 47 FBS-vs-FBS FIRST_FROZEN Week 5 games. FBS-vs-FCS rows displayed by the source were excluded from this governed relevant-FBS comparison.

Priority/current observations:
- Western Kentucky at New Mexico State: WKU +2.5 (-107), NMSU -2.5 (-113), total 57.5.
- North Texas at Tulsa: North Texas +1.0 (-112), Tulsa -1.0 (-110), total 57.5. CBS broad benchmark displayed Tulsa -1.5.
- Pittsburgh at Virginia Tech: Pitt +3.5 (-117), Virginia Tech -3.5 (-106), total 55.0.
- Liberty at Delaware: Liberty -7.0 (-114), Delaware +7.0 (-108), total 50.0.
- Penn State at Northwestern: Penn State -2.5 (-114), Northwestern +2.5 (-108), total 45.5.
- Alabama at Mississippi State: Alabama -6.0 (-110), Mississippi State +6.0 (-112), total 60.0. CBS broad benchmark displayed Alabama -5.5 / total 60.5 during this research window.
- Michigan at Minnesota: Michigan -5.5 (-111), Minnesota +5.5 (-111), total 43.5.
- Syracuse at UConn: Syracuse -6.5 (-110), UConn +6.5 (-110), total 50.5.
- Notre Dame at North Carolina: Notre Dame -21.0 (-110), North Carolina +21.0 (-110), total 47.0.
- Vanderbilt at Georgia: Vanderbilt +24.5 (-114), Georgia -24.5 (-109), total 51.0.
- Old Dominion at Georgia State: Old Dominion +2.5 (-112), Georgia State -2.5 (-107), total 51.5.
- Memphis at Charlotte: Memphis -20.5 (-110), Charlotte +20.5 (-112), total 52.5.
- Ohio State at Iowa: Ohio State -14.5 (-108), Iowa +14.5 (-115), total 45.5.
- Eastern Michigan at Massachusetts: EMU +6.5 (-111), UMass -6.5 (-109), total 48.5.
- Marshall at James Madison: Marshall +18.5 (-110), JMU -18.5 (-111), total 56.5.
- Maryland at Nebraska: Maryland +14.5 (-110), Nebraska -14.5 (-112), total 52.0.
- Kentucky at South Carolina: Kentucky +3.0 (-115), South Carolina -3.0 (-107), total 53.5.
- Texas Tech at Colorado: Texas Tech -13.0 (-110), Colorado +13.0 (-110), total 50.5.
- UTSA at Rice: UTSA -11.5 (-111), Rice +11.5 (-110), total 55.5.
- Utah State at Boise State: Utah State +20.5 (-111), Boise State -20.5 (-111), total 51.5.
- Arkansas State at Louisiana: Arkansas State +6.5 (-108), Louisiana -6.5 (-113), total 47.5.

The remaining relevant-FBS games were also present on the same current consensus board; this cycle establishes current broad-board availability without inventing exact frozen-model comparisons not recovered into the user-facing render.

No market observation altered Champion/model state.


## User-authorized extra prospective capture — 2026-10-01 ~17:40 CT
Observation class: INTERMEDIATE / USER_AUTHORIZED_EXTRA.
Boundary: new prospective observation only. The incomplete 07:00 CT and missed/incomplete 13:00 CT scheduled cycles are not reconstructed.
Source semantics: CBS Sports 2026 Week 5 betting guide retrieved live during this cycle; displayed spread/total values are retained as broad benchmark observations where exact book/price was not established. Champion remains v1.208 FIRST_FROZEN / v1.193 accepted Beta Champion; market information is downstream only.

Nearest-window benchmark:
- Western Kentucky at New Mexico State: New Mexico State -2.5, total 57.5.
- North Texas at Tulsa: Tulsa -1.5, total 57.5.
- Pittsburgh at Virginia Tech: Virginia Tech -3, total 54.5.
- Liberty at Delaware: Delaware +7, total 50.5.
- Penn State at Northwestern: Northwestern +2.5, total 45.5.
Selected Saturday priority/current benchmark:
- Notre Dame at North Carolina: North Carolina +21, total 47.5.
- Alabama at Mississippi State: Mississippi State +6, total 60.5.
- Syracuse at UConn: UConn +6.5, total 50.5.
- Michigan at Minnesota: Minnesota +5.5, total 43.5.
- Vanderbilt at Georgia: Georgia -24.5, total 50.5.
- Ohio State at Iowa: Iowa +14, total 45.5.
- Memphis at Charlotte: Charlotte +20.5, total 54.5.
- Old Dominion at Georgia State: Georgia State -1.5, total 50.5.
- Eastern Michigan at Massachusetts: Massachusetts -6, total 48.5.
- Marshall at James Madison: James Madison -18.5, total 55.5.
- Maryland at Nebraska: Nebraska -14.5, total 52.5.
- Kentucky at South Carolina: South Carolina -2.5, total 53.5.
- Texas Tech at Colorado: Colorado +13.5, total 50.5.
- UTSA at Rice: Rice +11.5, total 54.5.
- Utah State at Boise State: Boise State -19.5, total 51.5.
- Arkansas State at Louisiana: Louisiana -6.5, total 46.5.

Availability notes from same-day public reporting:
- Thursday slate remains Western Kentucky-New Mexico State and North Texas-Tulsa.
- New Mexico State WR Brodie Malone-Bradford was reported questionable with an undisclosed injury in same-day coverage.
- Tulsa QB availability remained a material uncertainty in same-day preview coverage; no late evidence recovered in this cycle was sufficient to establish a governed actionable threshold.

No observation altered Champion/model state. Exact governed 47-game FIRST_FROZEN identity reconciliation was not recoverable from the current repository render during this cycle, so this capture does not claim full-slate exactly-once completion.


## Evening downstream capture — 2026-10-01 ~20:06 CT
Observation class: INTERMEDIATE / EVENING_AVAILABILITY. Prospective only; no earlier boundary is reconstructed. Champion v1.193 / v1.208 unchanged.

- Thursday games: practical decision boundary passed; existing PASS states remain closed.
- North Texas at Tulsa: same-day reporting confirmed Baylor Hayes as Tulsa's starting quarterback and Dexter Williams II as not starting. This late availability update does not reopen the prior PASS.
- Pittsburgh at Virginia Tech: current public reference Pittsburgh +2.5, Virginia Tech -2.5, total 54.5. Friday 13:00 CT remains the default reconciliation deadline.
- Penn State at Northwestern: current public reference Penn State -2.5, total 46.5. Game 401858476 is an explicit v1.208 FIRST_FROZEN exclusion, so this is market-only/unmodeled evidence.
- Liberty at Delaware: game 401871050 is an explicit v1.208 FIRST_FROZEN exclusion; any observation remains market-only/unmodeled.
- Northwestern availability reporting: two starting defensive backs doubtful, Luke Dehnicke questionable, Ezomo Oratokhai out. Weather reporting: mid/upper 50s, about 9 mph wind, no rain.

No market or availability evidence altered Champion/model state.


## Friday recovery prospective capture — 2026-10-02 ~18:00 CT
Observation class: INTERMEDIATE / USER_AUTHORIZED_FRIDAY_RECOVERY. The incomplete/missed 07:00 and 13:00 CT scheduled cycles remain immutable and are not reconstructed.
Champion link: accepted v1.208 FIRST_FROZEN artifact 10897612260 / v1.193 Champion. Artifact 10897612260 was directly recovered during this cycle; digest and accepted identity match v1.208. Exact Week 5 modeled substrate is recoverable as 47 FBS-vs-FBS frozen predictions; explicit exclusions remain separate/unmodeled.
Current broad benchmark: CBS Sports Week 5 board retrieved Oct. 2. Selected exact-price cross-checks are noted below.

Priority observations:
- Alabama at Mississippi State: broad MSST +6 / 60.5; FanDuel research displayed MSST +5.5 (+100), Alabama -5.5 (-122), total 60.5. Frozen Engine: MSST by 9.8652, total 60.0377, home win 0.743319.
- Syracuse at UConn: broad UConn +6.5 / 50.5; FanDuel research displayed UConn +6.5 (+100). Frozen Engine: UConn by 6.8817, total 55.6316, home win 0.670083.
- Ohio State at Iowa: broad Iowa +14 / 45.5; bet365 displayed Iowa +14.5 (-115), total 45.5. Frozen Engine: Iowa by 6.2898, total 51.1058, home win 0.593141.
- Eastern Michigan at Massachusetts: broad UMass -6 / 48.5; DraftKings displayed UMass -6 (-108). Frozen Engine: UMass by 22.0802, total 49.0269, home win 0.894632. Same-day reporting has UMass 4-0 and expecting a sellout.
- Marshall at James Madison: broad JMU -18.5 / 55.5; cross-book table displayed Caesars JMU -18.5 (-107), DraftKings -18.5 (-105), FanDuel -18.5 (-110). Frozen Engine: JMU by 29.5062, total 51.9170, home win 0.955715.
- Maryland at Nebraska: broad Nebraska -14.5 / 52.5. Frozen Engine: Nebraska by 10.5205, total 56.0116, home win 0.733503. Nebraska WR Jacob Barney Jr. reported questionable. Side remains beyond frozen fair margin; no chase.
- Vanderbilt at Georgia: broad Georgia -24.5 / 50.5. Frozen Engine: Georgia by 24.5805, total 57.5598. Vanderbilt QB Jared Curtis remained a pregame decision after limited practice and Friday walkthrough; availability is decision-relevant to the total.
- Texas Tech at Colorado: broad Colorado +13.5 / 50.5; DraftKings displayed Colorado +13.5 (-115). Frozen Engine: Texas Tech by 1.7697, total 53.2790. Current reporting notes Colorado quarterback instability/player dismissals; preserve as later-window review rather than forcing action.

No market or availability evidence altered frozen Champion predictions. No execution is inferred by this capture.


## Friday evening availability capture — 2026-10-02 ~19:40 CT
Observation class: INTERMEDIATE / USER_AUTHORIZED_EVENING_AVAILABILITY. Downstream of the persisted ~18:00 CT Friday Recovery RUN_PASS; no competing baseline.
- Vanderbilt at Georgia: Vanderbilt QB Jared Curtis remains unresolved tonight. Same-day reporting says he made it through Friday walkthrough without issue and will attempt to play, but the final decision comes after Saturday pregame evaluation. Existing total WAIT remains decision-relevant; no Friday resolution is manufactured.
- Texas Tech at Colorado: Texas Tech backup QB Thomas Castellanos was ruled ineligible Friday afternoon. This is genuinely new late availability information. It does not by itself establish an actionable Colorado threshold or alter the frozen prediction; existing later-window WAIT remains.
- Ohio State at Iowa: current Friday reporting still shows Ohio State -14.5 / Iowa +14.5; weather expected not to materially affect the game. The persisted Iowa cutoff remains available in current public board evidence.
- Eastern Michigan at Massachusetts: current same-day reporting confirms the UMass home game is sold out; no late evidence recovered invalidates the persisted UMass cutoff.
- Kentucky at South Carolina: late search recovered Kentucky LB Alex Afari becoming ineligible after an NCAA appeal, while South Carolina defensive-line availability concerns remain part of the matchup context. Conflicting availability changes do not earn a new Friday action; WAIT remains.
- No sufficiently newer executable-price evidence was recovered to overwrite the ~18:00 exact-price references for Mississippi State, UConn, Iowa, UMass or James Madison. Their established minimum acceptable line/price cutoffs remain authoritative; user should verify the actual Caesars window before execution.
No observation altered Champion/FIRST_FROZEN state. No execution inferred.


## Saturday prospective full-slate capture — 2026-10-03 07:19 CT
Observation class: SCHEDULED MARKET MONITOR / PROSPECTIVE SATURDAY.
Prospective boundary: evidence/run_receipts/CFB_RUN_STARTED_2026-10-03_0719CT_MARKET_MONITOR.md.
Source: FantasyData NCAA Football Odds consensus board retrieved after RUN_STARTED on 2026-10-03; spread/price, moneyline, total/price recorded below. Source semantics are consensus/executable-reference evidence, not a claim of universal book identity. CBS current Week 5 odds was used as a broad cross-check on priority games. Champion remains accepted v1.193 / v1.208 FIRST_FROZEN; no market information alters frozen predictions.

Current Saturday modeled-slate observations:
- Memphis @ Charlotte: MEM -20.5 (-111), CHA +20.5 (-110); ML MEM -2122 / CHA +955; total 52.5 O-108/U-114.
- Alabama @ Mississippi State: ALA -5.5 (-109), MSST +5.5 (-113); ML ALA -217 / MSST +177; total 60.5 O-114/U-108.
- Syracuse @ UConn: SYR -6.5 (-115), UConn +6.5 (-106); ML SYR -264 / UConn +211; total 50.5 O-110/U-112.
- Michigan @ Minnesota: MICH -6.5 (-107), MINN +6.5 (-115); ML MICH -232 / MINN +189; total 43.5 O-110/U-111.
- Notre Dame @ North Carolina: ND -21 (-112), UNC +21 (-110); ML ND -2776 / UNC +1093; total 46.5 O-113/U-107.
- Middle Tennessee @ Kansas: MTSU +20.5 (-108), KU -20.5 (-112); ML MTSU +959 / KU -2083; total 50.5 O-110/U-112.
- Stanford @ Wake Forest: STAN +14.5 (-110), WAKE -14.5 (-110); ML STAN +464 / WAKE -650; total 53.5 O-113/U-109.
- West Virginia @ Iowa State: WVU +3 (-106), ISU -3 (-116); ML WVU +134 / ISU -163; total 53.5 O-115/U-108.
- UCF @ Houston: UCF +11.5 (-112), HOU -11.5 (-112); ML UCF +331 / HOU -443; total 51.0 O-113/U-109.
- Boston College @ SMU: BC +21.5 (-113), SMU -21.5 (-107); ML BC +965 / SMU -1955; total 55.5 O-108/U-114.
- Michigan State @ Wisconsin: MSU +9.5 (-110), WISC -9.5 (-112); ML MSU +281 / WISC -369; total 43.5 O-110/U-112.
- Vanderbilt @ Georgia: VAN +25 (-110), UGA -25 (-112); ML VAN +1471 / UGA -5633; total 50.5 O-114/U-108.
- Western Michigan @ Buffalo: WMU -12.5 (-112), BUF +12.5 (-112); ML WMU -612 / BUF +435; total 46.5 O-109/U-114.
- Toledo @ Ball State: TOL -21 (-107), BALL +21 (-115); ML TOL -3559 / BALL +967; total 51.5 O-113/U-109.
- Akron @ Central Michigan: AKR +7 (-114), CMU -7 (-109); ML AKR +216 / CMU -268; total 47.5 O-108/U-114.
- Ohio @ Kent State: OHIO -3.5 (-109), KENT +3.5 (-113); ML OHIO -174 / KENT +142; total 50.5 O-111/U-111.
- Wyoming @ North Dakota State: WYO +17 (-110), NDSU -17 (-110); ML WYO +695 / NDSU -1150; total 44.5 O-110/U-110.
- Old Dominion @ Georgia State: ODU +2.5 (-110), GAST -2.5 (-112); ML ODU +115 / GAST -140; total 51.5 O-109/U-113.
- Virginia @ Florida State: UVA -1.5 (-110), FSU +1.5 (-110); ML UVA -123 / FSU +101; total 51.5 O-109/U-112.
- Auburn @ Tennessee: AUB +6.5 (-107), TENN -6.5 (-114); ML AUB +205 / TENN -253; total 54.5 O-112/U-112.
- Louisville @ NC State: LOU -3.5 (-104), NCST +3.5 (-119); ML LOU -166 / NCST +136; total 58.0 O-109/U-113.
- Eastern Michigan @ UMass: EMU +5.5 (-111), UMass -5.5 (-109); ML EMU +179 / UMass -222; total 48.5 O-111/U-111.
- Ohio State @ Iowa: OSU -14.5 (-107), IOWA +14.5 (-117); ML OSU -696 / IOWA +477; total 45.5 O-110/U-111.
- Florida @ Missouri: FLA -5.5 (-112), MIZ +5.5 (-110); ML FLA -221 / MIZ +178; total 57.5 O-113/U-109.
- Bowling Green @ Miami (OH): BGSU +12.5 (-110), M-OH -12.5 (-112); ML BGSU +422 / M-OH -591; total 43.0 O-110/U-110.
- Marshall @ James Madison: MAR +18 (-110), JMU -18 (-110); ML MAR +730 / JMU -1280; total 56.5 O-111/U-112.
- UTEP @ New Mexico: UTEP +22.5 (-110), UNM -22.5 (-112); ML UTEP +1170 / UNM -4131; total 48.5 O-112/U-112.
- Maryland @ Nebraska: MD +14.5 (-110), NEB -14.5 (-110); ML MD +503 / NEB -756; total 52.5 O-110/U-110.
- Purdue @ Illinois: PUR +10 (-112), ILL -10 (-110); ML PUR +318 / ILL -422; total 62.5 O-112/U-110.
- Kentucky @ South Carolina: UK +2.5 (-107), SC -2.5 (-115); ML UK +117 / SC -143; total 53.5 O-114/U-108.
- Oregon State @ Colorado State: ORST -6.5 (-113), CSU +6.5 (-110); ML ORST -248 / CSU +201; total 62.5 O-106/U-114.
- UTSA @ Rice: UTSA -13 (-113), RICE +13 (-110); ML UTSA -591 / RICE +424; total 56.0 O-110/U-110.
- Arkansas @ Texas A&M: ARK +14 (-111), TAMU -14 (-111); ML ARK +457 / TAMU -650; total 50.5 O-107/U-113.
- BYU @ TCU: BYU -6 (-111), TCU +6 (-112); ML BYU -233 / TCU +189; total 47.5 O-114/U-108.
- UL Monroe @ South Alabama: ULM +14 (-107), USA -14 (-115); ML ULM +490 / USA -726; total 56.5 O-111/U-111.
- Washington @ USC: WASH +9.5 (-109), USC -9.5 (-113); ML WASH +297 / USC -381; total 58.5 O-108/U-114.
- Texas Tech @ Colorado: TTU -13.5 (-110), COLO +13.5 (-110); ML TTU -572 / COLO +409; total 50.5 O-108/U-115.
- Utah State @ Boise State: USU +19.5 (-112), BOISE -19.5 (-110); ML USU +971 / BOISE -2106; total 51.5 O-111/U-110.
- Arkansas State @ Louisiana: ARKST +6.5 (-109), UL -6.5 (-113); ML ARKST +195 / UL -244; total 48.5 O-107/U-116.
- Fresno State @ Washington State: FRES +2 (-112), WSU -2 (-111); ML FRES +105 / WSU -127; total 45.5 O-110/U-111.
- Texas State @ San Diego State: TXST -9.5 (-113), SDSU +9.5 (-109); ML TXST -392 / SDSU +302; total 57.5 O-110/U-112.
- Baylor @ Arizona State: BAY +3.5 (-108), ASU -3.5 (-115); ML BAY +148 / ASU -180; total 48.5 O-111/U-111.
- Cincinnati @ Arizona: CIN +7 (-117), ARIZ -7 (-106); ML CIN +207 / ARIZ -257; total 55.5 O-111/U-111.
- San Jose State @ Hawai'i: SJSU +3 (-111), HAW -3 (-111); ML SJSU +128 / HAW -155; total 50.5 O-114/U-108.

Priority movement vs Friday persisted references:
- Mississippi State remains +5.5 and price -113: within established +5.5-or-better / max -115 cutoff.
- UConn remains +6.5 and price -106: within established cutoff.
- Iowa remains +14.5 and price -117: within established +14-or-better / max -120 cutoff.
- UMass improved from -6 reference to -5.5 (-109): within established maximum -6.5 / max -115 cutoff.
- James Madison improved from -18.5 reference to -18 (-110): within established cutoff.
- Vanderbilt/Georgia total remains 50.5; Jared Curtis remains pending pregame evaluation, so WAIT trigger remains live.
- Nebraska remains -14.5 / 52.5; side PASS/no-chase remains supported by the frozen fair margin of Nebraska -10.5.
- Texas Tech/Colorado remains TTU -13.5 / 50.5.
- Kentucky/South Carolina remains SC -2.5 / 53.5.

No market observation altered Champion/FIRST_FROZEN state.


## Persistence health probe — 2026-10-03 21:55 CT
Operational-only diagnostic. Existing-file SHA-guarded append path verified after the 13:00 CT rejection. No market, decision, execution, outcome, Champion, FIRST_FROZEN, or scientific state change. PROBE_PASS


## Week 6 opening-board capture — 2026-10-04 ~08:40 CT
Observation class: FIRST_QUALIFIED_MARKET_OBSERVATION where an exact number is listed below; otherwise NOT_YET_AVAILABLE. Source: CBS Week 6 scoreboard retrieved prospectively after manual RUN_STARTED. CBS board was checked across the coming FBS slate; no moneyline/price was treated as established where the recovered board did not display it. Current CBS schedule is used for operational kickoff placement only; frozen prediction bytes remain unchanged.
- Southern Miss @ Troy: Troy -10.5; total 49.5.
- Jacksonville State @ Kennesaw State: Kennesaw State +4.5; total 49.5.
- New Mexico State @ FIU: FIU -4.5; total 47.5.
- Florida State @ Louisville: Louisville -7; total 58.5.
- Iowa @ Washington: Washington -1.5; total 42.5.
- Iowa State @ BYU: BYU -14.5; total 50.5.
- Texas A&M @ Missouri: Missouri -2.5; total 49.5.
- South Carolina @ Florida: Florida -13.5; total 58.5.
- Illinois @ Michigan State: Michigan State +2.5; total 51.5.
- Ole Miss @ Vanderbilt: Vanderbilt +10.5; total 57.5.
- Stanford @ Notre Dame: Notre Dame -35.5; total 55.5.
- Texas @ Oklahoma: Oklahoma +9.5; total 41.5.
- UCLA @ Oregon: Oregon -13; total 61.5.
- Maryland @ Ohio State: Ohio State -34.5; total 55.5.
- Tennessee @ Arkansas: Arkansas +14.5; total 54.5.
- LSU @ Kentucky: Kentucky +10.5; total 52.5.
- Georgia @ Alabama: Alabama +1.5; total 57.5.
- USC @ Penn State: Penn State +2.5; total 55.5.
- Indiana @ Nebraska is an explicit v1.208 exclusion/unmodeled row; current board Indiana -8.5 / 51.5 is preserved only as downstream operational context, not as a modeled disagreement.
Other modeled Week 6 games: exact qualified spread/total not established from the recovered board in this capture; no number is invented. No market observation altered Champion/FIRST_FROZEN state.


## Week 6 Tuesday morning prospective recovery — 2026-10-06 ~07:04 CT
Boundary: manual prospective recovery after repeated scheduled-control start-only failures. Failed scheduled cycles are not reconstructed. Source: current CBS Week 6 odds board retrieved during this manual run; current prices are observational downstream evidence only.

Nearest governed windows:
- Southern Miss @ Troy (Tue 19:00 CT): Southern Miss +10.5 (-111), Troy -10.5 (-108); ML Southern Miss +320 / Troy -410; total 50.5 (Over -105 / Under -110). Sunday first qualified observation remains Troy -10.5 / 49.5; spread unchanged, total +1.0.
- Jacksonville State @ Kennesaw State (Wed 18:00 CT): Jacksonville State -3 (-108), Kennesaw State +3.5 (-124); ML Jacksonville State -148 / Kennesaw State +126; total 50.5 (Over -104 / Under -108). Sunday first qualified observation was Kennesaw State +4.5 / 49.5.
- New Mexico State @ FIU (Wed 18:30 CT): New Mexico State +6.5 (-110), FIU -6 (-112); ML New Mexico State +190 / FIU -230; total 46.5/47.5 market display depending side price (NMSU Over 46.5 -111; FIU Under 47.5 -114). Sunday first qualified observation was FIU -4.5 / 47.5. Preserve the displayed asymmetric total quotes rather than inventing a single consensus number.

Kickoff corroboration: Southern Miss official athletics lists Tue 19:00 CT; New Mexico State official athletics lists Wed 18:30 CT. Champion/FIRST_FROZEN unchanged. No execution inferred.


## Friday prospective benchmark check — 2026-10-09 07:34:26 CT
Run: CFB_MANUAL_FRIDAY_REVIEW_20261009T123613Z. Observation timestamp: 2026-10-09T12:34:26.452Z (retrieval boundary, not bookmaker offer time). Class: INTERMEDIATE_PUBLIC_BENCHMARK. Source: https://www.espn.com/college-football/odds; DraftKings-labelled linked quotes; fresh Firecrawl maxAge=0, scrape 01a120a7-b731-77a0-a31c-0d87b256d146. Executability: NOT_VERIFIED; Caesars offer/accepted price: NOT_ESTABLISHED. Source offer update time: UNAVAILABLE. No outcome/status ingestion; frozen predictions unchanged.
- Florida State @ Louisville (ESPN 401858254; scheduled kickoff 2026-10-09T23:00Z): away spread +3.5 -108; home spread -3.5 -112; total o59.5 -112 / u59.5 -108; moneyline away +150, home -180. Availability: PUBLIC_DISPLAY_OBSERVED_ONLY; execution-book availability UNVERIFIED.
- Iowa @ Washington (ESPN 401858487; scheduled kickoff 2026-10-10T01:00Z): away spread +2.5 -105; home spread -2.5 -115; total o41.5 -105 / u41.5 -115; moneyline away +124, home -148. Availability: PUBLIC_DISPLAY_OBSERVED_ONLY; execution-book availability UNVERIFIED.
- Washington State @ Utah State (ESPN 401860922; scheduled kickoff 2026-10-10T01:00Z): away spread +5.5 -112; home spread -5.5 -108; total o43.5 -115 / u43.5 -105; moneyline away +170, home -205. Availability: PUBLIC_DISPLAY_OBSERVED_ONLY; execution-book availability UNVERIFIED.
- Wyoming @ San Jose State (ESPN 401864519; scheduled kickoff 2026-10-10T01:00Z): away spread +4.5 -112; home spread -4.5 -108; total o42.5 -112 / u42.5 -108; moneyline away +160, home -192. Availability: PUBLIC_DISPLAY_OBSERVED_ONLY; execution-book availability UNVERIFIED.
- Iowa State @ BYU (ESPN 401856826; scheduled kickoff 2026-10-10T02:15Z): away spread +10.5 -112; home spread -10.5 -108; total o46.5 -108 / u46.5 -112; moneyline away +330, home -425. Availability: PUBLIC_DISPLAY_OBSERVED_ONLY; execution-book availability UNVERIFIED.
Comparison to separately preserved Oct 8 benchmark: Iowa +3 (-115)/Washington -3 (-105) is now +2.5 (-105)/-2.5 (-115); Wyoming +4.5 (-108)/SJSU -4.5 (-112) is now +4.5 (-112)/-4.5 (-108). These are cross-retrieval benchmark changes, not independently timestamped book movement or earned betting thresholds. No FIRST_OBSERVED record is overwritten.
