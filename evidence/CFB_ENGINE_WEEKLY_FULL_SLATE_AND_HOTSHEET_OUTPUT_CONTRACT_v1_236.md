# CFB Engine - Weekly Full-Slate and Hot Sheet Output Contract v1.236

Status: ACTIVE OUTPUT / PRESENTATION CONTROL
Date: 2026-09-26
Parents: v1.224, v1.226, v1.227, v1.233, v1.235

## Purpose
Separate complete weekly football visibility from the shorter actionable Hot Sheet.

## Full Weekly Slate
Produce a compact sportsbook-board-style weekly view covering every governed relevant-FBS game for which the Beta Champion has an accepted prediction or an explicit exclusion/unavailable state. This is an engine output, not a copy of sportsbook predictions.

For every game show, as available:
- kickoff in Central Time;
- away and home teams;
- Beta Champion fair spread;
- Beta Champion projected total;
- Beta Champion win probability;
- prediction lineage/status (FIRST_FROZEN, REFRESH, EXCLUDED/UNAVAILABLE as applicable);
- concise market comparison only when qualified market observations exist, kept separate from Champion prediction.

The full-slate presentation should be visually compact and scannable, inspired by a printed sportsbook board: many games visible together, consistent columns, minimal prose. It may be rendered as a document/table/image-style board as supported, but exact numbers must come from authoritative engine evidence rather than image-generation inference.

Nebraska must always be included and visually easy to locate whenever Nebraska has a game in the covered week, regardless of Hot Sheet rank or actionable status.

## Hot Sheet
The Hot Sheet is a separate shorter opportunity view, normally approximately the top 20 actionable or decision-relevant games rather than all games. Nebraska is always included when playing even if it falls outside the normal cutoff; label it as the Nebraska inclusion rather than falsely implying rank.

The Hot Sheet should evaluate available betting expressions under the governed betting layer, including spread, total and moneyline where supported. It should surface BET EARLY, BET NOW, WAIT, PASS or INCONCLUSIVE with reason, minimum acceptable number/price and timing trigger where available. Do not invent calibrated EV or probabilities that have not been earned.

## Parlays
Include a dedicated parlay section on the Hot Sheet only under the applicable parlay-layer authority. Until a qualified parlay contract/calibration exists, label combinations as experimental/candidate structures rather than production engine recommendations. Do not multiply marginal probabilities or assume independence to manufacture parlay EV. Preserve correlation, price and exposure questions for the dedicated layer.

## Separation
Full Weekly Slate answers: What does our Beta Champion think about every game?
Hot Sheet answers: Where are the most decision-relevant betting opportunities and what should we do with them?
Weekly Beta Learning Review answers: What did reality teach us and what happens because of it?

These outputs must remain distinct even when packaged together.

Scientific effect: none. This contract changes presentation and required coverage only; it does not modify Champion predictions, features, calibration, betting authority or market-source qualification.

## Daily refresh requirement — 2026-09-29
For an active football week, the user-facing Hot Sheet is a living downstream decision surface. Refresh it each operating day Tuesday through Saturday against the same accepted frozen Engine snapshot. Show material market movement, current qualified line/price, decision-state changes, WAIT trigger status, minimum acceptable number/price where established, and execution timing when governed evidence supports it.
Append changes with timestamps/provenance; never overwrite earlier observations or decisions. A daily Hot Sheet refresh is presentation/market/decision work only and has no scientific/model effect.


## Chronological Next-Up presentation — 2026-09-29
The Hot Sheet must prioritize what requires attention next without hiding the rest of the slate.

At the top of every active-week Hot Sheet, render chronological NEXT-UP sections using America/Chicago kickoff time:
1. THURSDAY — all governed relevant games scheduled Thursday, regardless of normal Hot Sheet rank;
2. FRIDAY — all governed relevant games scheduled Friday, regardless of normal Hot Sheet rank;
3. SATURDAY MORNING — all governed Saturday games with kickoff before 12:00 CT;
4. SATURDAY AFTERNOON — all governed Saturday games with kickoff from 12:00 through 16:59 CT;
5. SATURDAY EVENING/NIGHT — all governed Saturday games with kickoff at or after 17:00 CT.

Within each section, order by kickoff then game identity. Show at minimum: kickoff CT; Engine Prediction (Frozen) fair spread; frozen projected total and win probability when earned; current qualified market/price; movement from first qualified observation when available; current decision state; pending information/reason; reconciliation deadline; established acceptable number/price if any; and realistic execution window.

The earliest still-active chronological section is visually the primary NEXT-UP section. Completed/started games must leave active decision sections and may move to historical/settlement presentation; never re-decide them.

After the chronological NEXT-UP sections, retain a PRIORITY WATCHLIST for the most decision-relevant opportunities regardless of kickoff day, then retain the complete FULL WEEKLY SLATE. A game may appear in both NEXT-UP and PRIORITY WATCHLIST for usability, but both displays must reference the same canonical decision/market state rather than create duplicate baselines.

Use the label **Engine Prediction (Frozen)** instead of ambiguous shorthand such as **Frozen Engine** where practical. This means the Engine's locked fair prediction, never the first/current sportsbook line.

This presentation change must not change Hot Sheet ownership, model inputs, prediction values, market chronology, or scientific authority.
