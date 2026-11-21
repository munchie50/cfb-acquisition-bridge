#!/usr/bin/env python3
"""Read-only, point-in-time CFB analytics. Inputs are separately certified JSONL exports.
No betting advice, source mutation, gate relaxation or model training.
"""
import argparse
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REQUIRED = ("event_id", "observed_at", "decision_deadline", "status", "source_kind")
STATUSES = {"PASS", "CONDITIONAL", "INCONCLUSIVE", "REJECT", "RUN_INCOMPLETE"}
def timestamp(s):
    d = datetime.fromisoformat(s.replace("Z", "+00:00"))
    if d.tzinfo is None:
        raise ValueError("timezone required")
    return d.astimezone(timezone.utc)
def load(path, as_of):
    rows, errors = [], []
    if not path or not Path(path).exists():
        return [], ["MISSING_INPUT"]
    for line_number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            for k in REQUIRED:
                if k not in row:
                    raise ValueError("missing " + k)
            if row["status"] not in STATUSES:
                raise ValueError("unknown status")
            observed = timestamp(row["observed_at"])
            deadline = timestamp(row["decision_deadline"])
            if observed > as_of:
                continue
            if row["source_kind"] not in ("CERTIFIED_MARKET", "ENGINE_DECISION", "SCHEDULER_RECEIPT", "EXECUTION"):
                raise ValueError("unapproved source kind")
            if row.get("actual_wager") and row["source_kind"] != "EXECUTION":
                raise ValueError("execution evidence boundary")
            row["_observed"] = observed
            row["_deadline"] = deadline
            rows.append(row)
        except (ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
            errors.append("line %d: %s" % (line_number, exc))
    return rows, errors
def analyze(rows, errors, as_of):
    by_status = Counter(r["status"] for r in rows)
    by_source = Counter(r["source_kind"] for r in rows)
    by_reason = Counter(r.get("reason", "UNSPECIFIED") for r in rows if r["status"] != "PASS")
    late = sum(r["_observed"] > r["_deadline"] for r in rows if r["source_kind"] == "ENGINE_DECISION")
    # Only pair certified, contemporaneous quotes for the same event, market and side.
    quotes = defaultdict(list)
    for r in rows:
        if r["source_kind"] == "CERTIFIED_MARKET" and r.get("market") and r.get("side") and isinstance(r.get("price"), (int, float)) and math.isfinite(r["price"]):
            quotes[(r["event_id"], r["market"], r["side"])].append(r)
    movement = []
    for key, observations in sorted(quotes.items()):
        observations.sort(key=lambda r: r["_observed"])
        if len(observations) < 2:
            continue
        first, last = observations[0], observations[-1]
        movement.append({"event_id": key[0], "market": key[1], "side": key[2],
                         "first": first["price"], "last": last["price"],
                         "movement": round(last["price"] - first["price"], 4),
                         "first_at": first["observed_at"], "last_at": last["observed_at"],
                         "label": "OBSERVED_MOVEMENT_NOT_CLV"})
    return {"schema": "CFB_READ_ONLY_ANALYTICS_V1", "as_of": as_of.isoformat(),
            "status": "INCOMPLETE" if errors or not rows else "DESCRIPTIVE_ONLY",
            "row_count": len(rows), "counts_by_status": dict(by_status),
            "counts_by_source": dict(by_source), "nonpass_reasons": dict(by_reason),
            "late_engine_decisions": late, "market_movements": movement,
            "missing_or_invalid": errors,
            "not_computed": ["CLV_without_verified_closing_quote_and_executable_entry",
                             "ROI_without_separate_actual_execution_and_outcome",
                             "calibration_without_frozen_probability_and_certified_outcome",
                             "counterfactual_without_point_in_time_replay"],
            "learning_boundary": "DESCRIPTIVE_ONLY_NO_AUTOMATIC_MODEL_UPDATE"}
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="certified point-in-time JSONL export")
    p.add_argument("--as-of", required=True, help="timezone-aware ISO timestamp")
    p.add_argument("--output", help="optional analytics JSON path; never write source inputs")
    a = p.parse_args()
    result = analyze(*load(a.input, timestamp(a.as_of)), timestamp(a.as_of))
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if a.output:
        Path(a.output).write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    if result["status"] == "INCOMPLETE":
        raise SystemExit(2)
if __name__ == "__main__":
    main()
