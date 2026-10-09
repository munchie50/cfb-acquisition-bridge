# Canonical market-total display QA integration — October 9, 2026

Run: CFB_MARKET_TOTAL_DISPLAY_QA_20261009T233832Z
Prospective boundary: 2026-10-09T23:38:32Z.
Scope: user-directed test routine; read-only display validation and existing GitHub QA coverage repair.

## Finding
The natural October 9 13:01 Monitor has separate STARTED/candidate/closure records. Independent history reads show receipt commits d9016e8237779887db319dc5094014f2596810ab at18:02:28Z, 9624aa941a165c0b2389787b7c960ae623b0c6a8 at18:05:16Z, and f57e511cbe24276169241f1f069d81395d635a60 at18:05:40Z; closure is direct child of candidate. Five canonical/output blobs independently match at closure parent. Persistence structure is corroborated; a receipt's RUN_PASS does not itself certify every display number.
The original 13:01 frozen-value audit independently retained PASS for49rows/147numericfields. The separate known presentation defect was its UCF market-total range52.5–54.5 versus canonical53.5/54.5; the15:38corrected view already repaired it. Previous automatic QA covered sections/frozen values and naming, not canonical market totals. No historical receipt or original snapshot is rewritten by this work.

## Correction and demonstration
New read-only scripts/cfb_week6_market_total_display_gate.py checks exact total-number endpoint sets for the qualified October9canonical block:43modeled Friday/Saturday quotes plus mandatory unmodeledNebraska. Uses declared market Gitblob and cycle, unique ordered identities, explicit AppalachianState/AppState and Massachusetts/UMass aliases, accent normalization and exact43+1source/display union. Reads column4marketquote only; no frozen/movement/first-observation/ML/odds numbers become totals. Both asymmetric endpoints must survive; no averaged consensus or unsupported extra endpoint.
When no explicit snapshot is supplied, resolves the declared blob through the canonical market path in local Git history, then hashes exact recovered bytes. Later canonical appends do not invalidate an older retained sheet by comparing it to the wrong head. No network, mutation or credentials are used by the helper.
Local execution reproduced rejection of original13:01range52.5–54.5 and PASS of corrected15:38sheet. Fourteen regressions passed, including original defect, asymmetric endpoint omission, extra endpoint, mismatched source bytes, missing/unknown cycle/source, duplicates, missingNebraska, odds/first-observed isolation, immutable-source recovery after laterappend and wrong-pathblob rejection.
Independent GitHub push run38005583878/job114073492883 at commit ee4b9f5a7a4b80fd4d25c814a5a82d5ba5490330 completed success. Retrieved logs show20presentation/diff+10naming+14total-display+7frozen tests=51 passed; originalresearchgate and current49row/147numeric/49direction/44total-display checks passed. AcceptedarchiveSHA256 verified. No manual dispatch or new recurring task.
https://github.com/munchie50/cfb-acquisition-bridge/actions/runs/38005583878

Installed outputs independently read back:
- scripts/cfb_week6_market_total_display_gate.py: 5bbb8b110f1e17295e2a31093c3e083dd9dcf242.
- scripts/test_cfb_week6_market_total_display_gate.py: 42a00ea0b9521fc2131d51871f594770cecb5b2c.
- Existing workflow: 2f75ae708cf58c8f9c0f44e393e5162547868f36.
The workflow tests the helper and runs it on exact files selected by the production-section gate.

## Material limits
This parser is deliberately qualified for the October9Week6 canonical block/cycle/schema. Unknown source/cycle/schema fails closed and requires separately qualified parser/coverage before a full PASS; it is not general future-week support. Source path/bytes membership does not qualify source truth or bookmaker offer time.
Coverage:43modeled plus1unmodeled total-number displays; six completed Tuesday–Thursday rows are outside this sourceblock and not total-certified. Spreads/line direction, prices, moneylines, source/divergence wording, freshness, practical execution and decisions require separate gates. Matching endpoint sets is not a sportsbook consensus or calibrated betting rule. A helper or post-writeCI PASS does not replace pre-persistence producer qualification or separate terminal closure.
Source remains marketblobbbc222ec291ba1faff3f083f6da132d8e8214cae, retrievalapproximately13:02CT, not refreshed by QA. Current15:38sheet eaeded90f81dd1190e0ef77fc52a448f73ea5dca unchanged. Existing canonical requirement covers broader row-value fidelity; this helper only automates its bounded totals subset.
No market/decision/execution/scorecard/HotSheet/wager/model/Champion or ChatGPT taskconfiguration mutation. ProductionRoutinev5,Championv1.193,FIRST_FROZENv1.208,v6candidate,S2study-only,2025TESTunopened. Originalrawclock403/1010cause, historicalfailuregaps, wagercausal/timinglinks and naturalchanged-artifact enforcement remainopen. Tonight19:30–20:30CT future at this QA boundary; no execution/success inferred.

## Lifecycle
INSTALLED / LOCAL_AND_REPOSITORY_QA_DEMONSTRATED. Natural producer enforcement and broader quote-field/future-cycle qualification remain pending. Active kickoffcontract, holistic map and recovery integration plus terminalcandidate/separateclosure are required for bounded repair completion.
Scientific/Champion effect:NONE.
