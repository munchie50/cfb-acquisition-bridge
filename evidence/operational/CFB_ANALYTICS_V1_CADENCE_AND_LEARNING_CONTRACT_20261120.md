# CFB read-only analytics v1 — candidate implementation and learning contract

**Status:** BUILT / GITHUB-PERSISTED, not yet runtime-executed, independently reconciled or production-accepted. This is not a Hot Sheet, a source acquisition system, a scoring update, or a replacement for the original selector QA.

## Input and output
Run `python analytics/cfb_read_only_analytics_v1.py --input <certified-point-in-time-export.jsonl> --as-of <ISO8601-with-timezone> --output <noncanonical-analytics.json>`.
Each JSONL observation requires `event_id`, `observed_at`, `decision_deadline`, `status`, `source_kind`; allowed kinds are `CERTIFIED_MARKET`, `ENGINE_DECISION`, `SCHEDULER_RECEIPT`, `EXECUTION`. For market movement also require `market`, `side`, numeric `price`. This is an **adapter contract**; existing Week12 Markdown and ledger artifacts are NOT asserted to be converted or certified. No automatic backfill from arbitrary text. Absent/invalid input exits nonzero, never emits invented CLV, ROI or calibration. Raw rows are not written into model features.

## Cadence / ownership within the existing four tasks
- Market Monitor, 07 and 13 CT: after its own primary run, only if an independently certified point-in-time export already exists, produce descriptive movement and decision-lateness evidence; if absent, record `ANALYTICS_INPUT_UNAVAILABLE` and keep the main run's own status unchanged.
- Evening Availability, existing Wed/Thu/Fri schedule: inspect timing, quote freshness and unreviewed/rejected reasons, without creating competing market recommendations or changing Friday decision deadlines.
- Engine Health, daily: audit analytics input freshness, missingness, source boundary and stage completion; do not run expensive replays or block the monitor on an optional analytics report.
- Weekly Engine QA, Sat/Sun: independently reconcile weekly status/rejection/timing trends; run deterministic QA, review outcome and CLV eligibility, document proposed hypotheses. Champion and gates remain unchanged absent separate controlled backtest, independent validation and authorization.

## Learning loop
Every week maintain: hypothesis, evidence window and immutable input refs, measured effect with denominator and uncertainty, potential leakage/selection bias, independent verification, decision KEEP/TEST/REJECT, owner and next review. Prefer out-of-sample time-ordered evaluation. Do not automatically train on execution slips, outcome-derived hindsight, or Yahoo/other contaminated observations. Require certified actual executions, closing quotes, and outcomes before CLV/ROI claims. Never equate prediction improvement with guaranteed betting returns.

## Verification stages
BUILT = source committed; EXECUTED = actual Python exit/stdout captured; VERIFIED = exact input/output digests and independent readback; ACCEPTED = governed contract and QA passed; PRODUCTION = demonstrated in natural scheduled run. No stage skipping.

## Nov20 market-movement isolation correction

The first analytics implementation risked combining prices from different sportsbooks or incompatible quote units. Corrected source commit `b0913d1dc0bab8d7949a229cd732c9e1d7de917f` groups by event, market, side, book, price_unit and quote_type, and requires these fields for movement observations. Updated isolated QA commit `e222804baceaeb5af8530c0913ed2879cddec552` adds a different-book contamination case. This is **CORRECTED / PERSISTED** only, not EXECUTED or accepted. Existing JSONL adapters must supply these fields and a genuine certified provenance reference before any movement claim. Do not silently aggregate incompatible odds, lines, venue quotes, or snapshots.
