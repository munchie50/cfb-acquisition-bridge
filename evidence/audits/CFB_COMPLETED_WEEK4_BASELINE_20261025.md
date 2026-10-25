# Completed-week baseline — Week4 numerical reconciliation

Recorded at actual observed checkpoint 2026-10-25T04:22:10Z.
Existing action: CFB_QA_LEARNING_FOLLOW_THROUGH_20261023, linked to CFB_QA_QUALIFICATION_LIMITS_REVIEW_20261023.
Status: WEEK4 PREDICTION/FINAL NUMERICAL BASELINE EXECUTED AND VERIFIED AT THIS SCOPE.
This is a downstream retrospective QA batch, not a new forecast, weekly-review replacement, model acceptance, historical recommendation or profitability claim.

## Sources and population

The original accepted FIRST_FROZEN ZIP (GitHub artifact10897612260) was recovered in this invocation. Its SHA256 is772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf, and all5 manifest member hashes were verified before evaluation. Original cutoff2026-09-26T03:47:37.497112+00:00 and all original predictions/exclusions are unchanged.

Fresh postgame source: https://www.cbssports.com/college-football/scoreboard/FBS/2026/regular/4/
Full response recovered by filesystem write bound 2026-10-25T04:16:35.973458+00:00; SHA2564d7a9374a2fbb4352ce5d25e005d284d470beda29045698565e1e4e20cf65f9f. This is today's outcome retrieval, never a reconstructed September27 capture or pregame research clock. The web renderer rejected the oversized scoreboard; ordinary direct public retrieval succeeded without Firecrawl expenditure. A separately readable CBS schedule corroborated displayed outcomes; no other source entered scoring.

The retained score-card-only HTML contains all71 final cards from that response. Its replay produces exactly the same53 governed rows, metrics and population as the full response. Stored Git blobf46dd4e6d78b11674afd4e5e534413ec448ef0d7. Images/news/navigation are irrelevant to scoring; extraction uses only scoped postgame cards, team links, date identities, period scores and final totals.

Population accounting:
- 71 CBS week games.
- 65 targets in this original snapshot:60 predictions and5 exclusions.
- 53 modeled FBS-vs-FBS games form the existing governed scoring denominator.
- 7 modeled non-FBS games are retained separately, not added to the53 denominator.
- 6 Thursday/Friday source games predate this original snapshot's cutoff and are outside its target set. Their absence here is not a new model exclusion or proof there was no earlier opinion elsewhere. Do not describe the53-game scorecard as evaluation of the entire71-game weekly slate.

Joins use original ordered team pairs and explicit named aliases, with UTC source schedules converted to America/New_York calendar dates. CBS game IDs are retained separately from original engine IDs; they are not presumed identical. The initial raw-UTC-date join correctly stopped on Tulsa/Arkansas crossing midnight; explicit timezone conversion resolved that calendar mismatch. No kickoff or frozen source timestamp was edited.

## Independently recomputed figures

| Measure | Exact replay | Prior reported figure | Result |
|---|---:|---:|---|
| Governed modeled games matched | 53/53 | 53/53 | Matches |
| Winner by predicted margin sign | 36/53 | 36/53 | Matches |
| Margin mean absolute error | 14.780825682279444 | 14.781 | Matches rounding |
| Total mean absolute error | 11.071212108762104 | 11.071 | Matches rounding |
| Signed home-margin error, actual minus prediction | -0.9250484613300394 | -0.925 | Matches rounding |
| Signed total error, actual minus prediction | -1.804872122647301 | -1.805 | Matches rounding |
| Frozen home-win Brier score | 0.21427521592358498 | Not stated in Week4 review | Newly reproduced |
| Winner by frozen probability threshold | 37/53 | Separate classifier | Do not relabel36/53 |

Three games have opposite margin-sign and probability-threshold directions: SamHouston/TexasTech, SouthernMiss/Tulane and AppState/NCState. The two outputs are separately fitted; disagreement alone is not an implementation defect. Preserve both rather than selecting the better result after outcomes. One-week average bias is descriptive and does not authorize subtracting an offset from production forecasts.

## Narrow source-grounded correction to old diagnostic prose

Source evidence/CFB_QA_WEEK4_OUTLIER_DIAGNOSTIC_BATCH_A_2026-09-27.md at4b41a69a33eab37f0a37feaad64d4d23cedd7aa5 and evidence/CFB_QA_WEEK4_CONTROL_CHECK_2026-09-27.md ateef7fde8f5227bf0e825b66528db0d34d950c2d0 remain preserved.

| Game | Old diagnostic wording | Exact original home-margin semantics |
|---|---|---|
| Tulsa @ Arkansas | Arkansas by12.635 | Arkansas home margin-12.635365106336145: Tulsa favored by12.635365106336145 |
| SamHouston @ TexasTech | TexasTech by0.567; old control says same direction as market favorite | TexasTech home margin-0.5670932723121679: SamHouston favored by0.5670932723121679 |

Their old absolute errors40.635 and35.567 are consistent with the negative original home margins. Correct those direction descriptions prospectively; do not change the forecast or recomputed aggregate. The earlier control's signed explanation must not be used as evidence the model agreed with the TexasTech favorite. The later full-slate control's reported35.07-point separation is consistent with the correct sign; this batch does not invalidate unrelated control calculations or independently revalidate its44 archived lines.

## Useful learning and ranked follow-through

1. Demonstrated evaluation defect: signed numeric predictions were narrated in the wrong direction. Future diagnostic prose should be generated from explicitly labelled home-margin values and checked against the immutable source. This batch's replay supplies those labelled values. No new production gate or model formula was added.
2. Reuse the existing opponent-strength/small-sample study rather than open another model redesign. Across the53 scored games,106 retained team-sides have qualified-prior counts102×3,3×4 and1×2. That limited variation cannot establish a stable within-week maturity effect. Existing S2 work already addresses the relevant hypothesis; prospective scoring remains separately authorized.
3. Treat side and total mechanisms separately. The five largest margin misses average7.073 points of total error, below this week's11.071 overall total error. This selected, postgame diagnostic slice is not a prospective betting rule or significance claim; it shows why a side miss alone cannot justify changing the total model.
4. Historical pregame price/decision/close coverage remains incomplete. The separately saved44-game archived-market control is diagnostic evidence recovered later, not canonical FIRST_QUALIFIED quotes, current offers or proof of executable profit. It must be source-replayed before relying on its numeric buckets. No odds, CLV, hypothetical stakes or ROI were invented here.

## Verification, persistence and resume boundary

Replay script: evidence/audits/cfb_completed_week4_baseline_replay_20261025.py, Git blob5c60ceea7157a57bb8ec64acfe544ae9512eec4a.
Full row/metric result: evidence/audits/CFB_COMPLETED_WEEK4_BASELINE_20261025.json, Git blob9519abb4325b455f5f63298be1b6674a90192443.
Retained final cards: evidence/audits/CFB_CBS_WEEK4_FINAL_SCORECARDS_CAPTURE_20261025.html.
Replay command from a checkout with Python/lxml: python evidence/audits/cfb_completed_week4_baseline_replay_20261025.py --archive ORIGINAL_ACCEPTED_ZIP --html evidence/audits/CFB_CBS_WEEK4_FINAL_SCORECARDS_CAPTURE_20261025.html --output /tmp/week4_replay.json
The reduced capture's input hash will differ from the full-response hash in the saved result; all governed scored rows and metrics were independently compared equal.

Executed verification: ZIP digest/all member hashes; complete unique original target/prediction/exclusion accounting;71 unique final source cards; scoped final status; period-total equality; explicit ordered-pair/date joins;53-row aggregate rounding checks; full/reduced response replay equality; six corruptions rejected (changed archive, period/final disagreement, nonfinal status, duplicate identity, duplicate source card, omitted modeled final). No model code was changed, so the broader production CI was not redundantly rerun for this read-only batch.

All three evidence payloads were transferred in bounded exact chunks, independently checked for full outgoing Git blob/byte equality, written serially and independently read back in full at the reported hashes. No original scorecard, review, market, decision, execution or frozen archive was rewritten.

DONE: Week4 governed prediction/final numerical baseline and narrow two-case diagnostic-sign correction.
NEXT: completed Week5 exact ORIGINAL prediction/final reconciliation, retaining known source-calendar conflicts explicitly and reusing accepted proof. Carry Week4 archived-market reconstruction as a separate missing-data/evidence limitation rather than blocking numerical work on later weeks.
OPEN: cross-week matched comparisons, causal error diagnosis, actual profitable-edge evidence, challenger outcome-scoring authority and natural scheduled use.
Benefit demonstrated: original Week4 aggregate figures corroborated and two misleading sign narratives isolated before hypothesis evaluation. Cost: retained-source recovery and one fresh public outcome response; zero Firecrawl credits, no training/refit. Predictive/financial benefit remains UNKNOWN.
