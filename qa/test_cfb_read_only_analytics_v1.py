#!/usr/bin/env python3
"""Isolated deterministic QA for descriptive analytics; no production inputs."""
import sys
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analytics"))
from cfb_read_only_analytics_v1 import analyze, timestamp

def row(status, observed, kind="ENGINE_DECISION", **extra):
    return dict(event_id="game1", observed_at=observed,
                decision_deadline="2026-11-20T19:00:00Z",
                status=status, source_kind=kind, **extra)

as_of = timestamp("2026-11-20T22:00:00Z")
rows = [row("PASS", "2026-11-20T18:00:00Z"),
        row("REJECT", "2026-11-20T20:00:00Z", reason="NO_VENUE_QUOTE"),
        row("PASS", "2026-11-20T18:00:00Z", "CERTIFIED_MARKET", market="spread", side="home", price=-3.5),
        row("PASS", "2026-11-20T21:00:00Z", "CERTIFIED_MARKET", market="spread", side="home", price=-4.0)]
for r in rows:
    r["_observed"] = timestamp(r["observed_at"])
    r["_deadline"] = timestamp(r["decision_deadline"])
result = analyze(rows, [], as_of)
assert result["status"] == "DESCRIPTIVE_ONLY"
assert result["late_engine_decisions"] == 1
assert result["nonpass_reasons"]["NO_VENUE_QUOTE"] == 1
assert result["market_movements"][0]["movement"] == -0.5
assert result["market_movements"][0]["label"] == "OBSERVED_MOVEMENT_NOT_CLV"
assert analyze([], ["MISSING_INPUT"], as_of)["status"] == "INCOMPLETE"
print("QA_PASS: deterministic read-only analytics invariants")
