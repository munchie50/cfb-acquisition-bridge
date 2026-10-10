# CFB Consensus Benchmark / Caesars Execution Control — 2026-10-10

Status: ACTIVE USER-APPROVED DOWNSTREAM MARKET / PRESENTATION CONTROL
Authorization: 2026-10-10 10:33:18 America/Chicago user approved the recommendation: consensus as market benchmark, Caesars as execution check, independent frozen Engine retained.
Parents: v1.236 output, active kickoff presentation contract, v1.226 betting evidence, v1.237 practical deadlines, v1.242 durable evidence.
Scope: market-reference sourcing, display and decision interpretation only. No model promotion, frozen prediction change or independent betting-system replacement.

## Three separate roles
- Engine Prediction (Frozen): accepted immutable fair spread/total/home-win probability; market observations never feed back into this prediction.
- Market Consensus: qualified multi-book market reference, preferred over a single-book/mixed-best-price board as the principal market benchmark.
- Caesars Offer: actual available selection/line/price at the user's execution venue. Public observations or consensus are not a verified executable Caesars offer.

## Consensus qualification and reproducible construction
Use at least three distinct identified sportsbook operators, excluding Caesars from the comparison baseline to avoid comparing Caesars partly with itself. Multiple sites quoting the same operator count once; duplicate skins/feeds do not establish independent books. Collect the same exact game identity, pregame full-game market, selection and period in one bounded collection window. Do not mix alternate lines, halves, live markets or ambiguous game mappings.

Preserve each constituent's source URL, sportsbook, selection, line, paired price, retrieval UTC, underlying update time if supplied, availability and execution qualification. Record collection start/end, oldest known update and source conflicts. Unknown update time stays unknown; retrieval is not an offer-update clock. Stale, unavailable, materially asynchronous or unresolved source observations cannot be claimed as current consensus. A retrieval-only saved reference must be labelled as such.

Default descriptive spread/total reference is the median of the eligible same-selection points, with book count and observed minimum/maximum dispersion shown. An even-count midpoint may not be offered by any book: label it a derived reference, never an executable quote. Keep all constituent line/price pairs; do not average American prices or pair a derived line with invented juice. Show price range only among actual quotes at that exact line, otherwise PRICE_NOT_COMPARABLE. Moneyline observations remain separately displayed by book; no fabricated consensus probability or EV. This method is descriptive, not a calibrated profitable betting rule.

If fewer than three distinct qualified non-Caesars operators are available, or qualification is unresolved, show CONSENSUS_UNAVAILABLE with reason. Preserve existing single-book or mixed-book observations as labelled fallback benchmarks; never rename them consensus or discard their asymmetry. This state does not erase an otherwise governed existing decision.

## Caesars comparison and decision limits
Compare the same selection and market: more points for an underdog or fewer points laid for a favorite is a better spread number; over and under require their correct direction. Evaluate price separately. When one offer has a better line but worse juice, say LINE/PRICE_TRADEOFF rather than declare it better overall without an earned tradeoff rule. Different prices and key-number crossings do not become interchangeable.

A favorable Caesars-versus-consensus difference is an investigation/offer-quality flag, not automatic BET NOW, calibrated edge, ATS probability or profit guarantee. Preserve independent Engine comparison, qualified football/availability evidence, earned recommendation maturity and prospective decisions. Existing acceptable number, maximum price, practical trip deadline and final cutoff remain unchanged; no chasing or threshold relaxation. Only verified actual executions enter the execution ledger.

## Presentation and ownership integration
Each current market cell or accompanying per-game view must distinguish Consensus (with count/dispersion/clock/status), Caesars (paired line/price/verification/clock), and any retained fallback benchmark. These are separate semantic fields; retain the existing qualified nine-column production schema by labelling them within its market cell until a wider schema is separately qualified. No new table layout may bypass current section/frozen/total/decision binding checks.
Keep chronological full-slate coverage, mandatory Nebraska exclusion, frozen values, accepted current decision bindings and exact quote clocks. Before replacing a current sheet, qualify constituent-to-canonical-to-rendered fidelity and append genuinely new observations before rendering them. A display-only change is not new market research or a new decision.

Market Monitor remains sole primary Hot Sheet producer. Evening Availability updates downstream canonical evidence. Health and Weekly QA audit qualification, current output binding and honest unavailable states, without becoming competing market producers. Preserve exactly four enabled production tasks and all schedules; create no extra task or run-now dispatch.

## Installation boundary and honest current state
At adoption the selected Saturday10:15CT sheet contains retained approximately07:03CT CBS mixed-book benchmark values, not a qualified three-operator consensus or verified Caesars execution. All49modeled games plus mandatory Nebraska retain CONSENSUS_UNAVAILABLE / CAESARS_UNVERIFIED until genuine new evidence qualifies them.
This installation does not retroactively validate those observations as consensus, change any existing pick/limit, refresh a quote, settle a wager or reconstruct a failed run. Future genuine multi-book acquisition and scheduled consumer demonstration remain pending; unavailable is a valid honest output, not permission to fabricate data.
