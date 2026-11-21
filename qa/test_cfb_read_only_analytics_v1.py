#!/usr/bin/env python3
"""Isolated deterministic QA for descriptive analytics; no production inputs."""
import sys
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analytics"))
from cfb_read_only_analytics_v1 import analyze, timestamp, load

def require(condition, message):
    if not condition:
        raise RuntimeError("QA_FAILURE: " + message)

def row(status, observed, kind="ENGINE_DECISION", **extra):
    if kind == "ENGINE_DECISION":
        extra.setdefault("decision_at", observed)
    if kind == "CERTIFIED_MARKET":
        extra.setdefault("source_path", "evidence/market/verified.json")
        extra.setdefault("source_blob", "a" * 40)
    return dict(event_id="game1", observed_at=observed,
                decision_deadline="2026-11-20T19:00:00Z",
                status=status, source_kind=kind, **extra)

as_of = timestamp("2026-11-20T22:00:00Z")
rows = [row("PASS", "2026-11-20T18:00:00Z"),
        row("REJECT", "2026-11-20T20:00:00Z", reason="NO_VENUE_QUOTE"),
        row("PASS", "2026-11-20T18:00:00Z", "CERTIFIED_MARKET", market="spread", side="home", book="BOOK_A", price_unit="points", quote_type="spread", price=-3.5),
        row("PASS", "2026-11-20T21:00:00Z", "CERTIFIED_MARKET", market="spread", side="home", book="BOOK_A", price_unit="points", quote_type="spread", price=-4.0)]
for r in rows:
    r["_observed"] = timestamp(r["observed_at"])
    r["_deadline"] = timestamp(r["decision_deadline"])
result = analyze(rows, [], as_of)
require(result["status"] == "DESCRIPTIVE_ONLY", "result[\"status\"] == \"DESCRIPTIVE_ONLY\"")
require(result["late_engine_decisions"] == 1, "result[\"late_engine_decisions\"] == 1")
require(result["status"] == "DESCRIPTIVE_ONLY", "result[\"status\"] == \"DESCRIPTIVE_ONLY\"")
require(result["nonpass_reasons"]["NO_VENUE_QUOTE"] == 1, "result[\"nonpass_reasons\"][\"NO_VENUE_QUOTE\"] == 1")
require(result["market_movements"][0]["movement"] == -0.5, "result[\"market_movements\"][0][\"movement\"] == -0.5")
require(result["market_movements"][0]["label"] == "OBSERVED_MOVEMENT_NOT_CLV", "result[\"market_movements\"][0][\"label\"] == \"OBSERVED_MOVEMENT_NOT_CLV\"")
require(analyze([], ["MISSING_INPUT"], as_of)["status"] == "INCOMPLETE", "analyze([], [\"MISSING_INPUT\"], as_of)[\"status\"] == \"INCOMPLETE\"")
other = row("PASS", "2026-11-20T21:30:00Z", "CERTIFIED_MARKET", market="spread", side="home", book="BOOK_B", price_unit="points", quote_type="spread", price=-9.0)
other["_observed"] = timestamp(other["observed_at"])
other["_deadline"] = timestamp(other["decision_deadline"])
require(len(analyze(rows + [other], [], as_of)["market_movements"]) == 1, "len(analyze(rows + [other], [], as_of)[\"market_movements\"]) == 1")
require(analyze(rows + [other], [], as_of)["market_movements"][0]["movement"] == -0.5, "analyze(rows + [other], [], as_of)[\"market_movements\"][0][\"movement\"] == -0.5")
import tempfile, json
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "market.jsonl"
    invalid = row("PASS", "2026-11-20T18:00:00Z", "CERTIFIED_MARKET", market="spread", side="home", book="BOOK_A", price_unit="points", quote_type="spread", price=-3.5)
    del invalid["source_blob"]
    p.write_text(json.dumps(invalid), encoding="utf-8")
    loaded, errors = load(p, as_of)
    require(not loaded and errors and "provenance missing" in errors[0], "not loaded and errors and \"provenance missing\" in errors[0]")
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / "decision.jsonl"
    invalid = row("PASS", "2026-11-20T18:00:00Z")
    del invalid["decision_at"]
    p.write_text(json.dumps(invalid), encoding="utf-8")
    loaded, errors = load(p, as_of)
    require(not loaded and "decision_at required" in errors[0], "not loaded and \"decision_at required\" in errors[0]")
conflict = row("PASS", "2026-11-20T21:00:00Z", "CERTIFIED_MARKET", market="spread", side="home", book="BOOK_A", price_unit="points", quote_type="spread", price=-8.0)
conflict["_observed"] = timestamp(conflict["observed_at"])
conflict["_deadline"] = timestamp(conflict["decision_deadline"])
conflicted = analyze(rows + [conflict], [], as_of)
require(conflicted["status"] == "INCOMPLETE", "conflicted[\"status\"] == \"INCOMPLETE\"")
require(not conflicted["market_movements"], "not conflicted[\"market_movements\"]")
print("QA_PASS: deterministic read-only analytics invariants")
