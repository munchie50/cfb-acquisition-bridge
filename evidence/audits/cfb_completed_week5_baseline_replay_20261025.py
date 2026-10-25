#!/usr/bin/env python3
"""Reproduce the completed Week 5 FIRST_FROZEN numerical baseline.

Reads only the accepted original prediction artifact and the already-governed
postgame scorecard. It does not acquire data, mutate predictions, or infer
missing market/decision/execution evidence.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
import zipfile
from pathlib import Path


EXPECTED_ZIP_SHA256 = "772b8683365ebf62d35fc3813beb138688b84af4172a0b261fd9218691d5adcf"
PREDICTION_MEMBER = "challenger_b_2026_fair_predictions_v1_206.csv"


def _number(value: str) -> float:
    return float(value.strip())


def _normalize_team(value: str) -> str:
    value = value.lower().replace("connecticut", "uconn")
    return re.sub(r"[^a-z0-9]", "", value)


def _load_predictions(artifact: Path) -> list[dict[str, str]]:
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    if digest != EXPECTED_ZIP_SHA256:
        raise ValueError(f"artifact SHA-256 mismatch: {digest}")
    with zipfile.ZipFile(artifact) as archive:
        raw = archive.read(PREDICTION_MEMBER).decode("utf-8")
    rows = list(csv.DictReader(io.StringIO(raw)))
    week = [
        row
        for row in rows
        if row["population_class"] == "FBS_VS_FBS"
        and "2026-09-29" <= row["start_date"][:10] < "2026-10-05"
    ]
    if len(week) != 47:
        raise ValueError(f"expected 47 Week 5 predictions, found {len(week)}")
    return week


def _load_finals(scorecard: Path) -> dict[tuple[str, str], tuple[int, int]]:
    text = scorecard.read_text(encoding="utf-8")
    section = text.split("## Week 5 partial final-result join", 1)[1].split(
        "## Week 6 authoritative postgame join", 1
    )[0]
    results: dict[tuple[str, str], tuple[int, int]] = {}
    pattern = re.compile(
        r"^- (.*?) @ (.*?) — .*?Realized .*?margin ([+-]?\d+); "
        r"(?:realized )?total (\d+)",
        re.MULTILINE,
    )
    for away, home, margin, total in pattern.findall(section):
        key = (_normalize_team(away), _normalize_team(home))
        if key in results:
            raise ValueError(f"duplicate final identity: {away} @ {home}")
        results[key] = (int(margin), int(total))
    if len(results) != 47:
        raise ValueError(f"expected 47 Week 5 finals, found {len(results)}")
    return results


def build(artifact: Path, scorecard: Path) -> dict:
    predictions = _load_predictions(artifact)
    finals = _load_finals(scorecard)
    output_rows = []
    for row in predictions:
        key = (_normalize_team(row["away_team"]), _normalize_team(row["home_team"]))
        if key not in finals:
            raise ValueError(f"missing final: {row['away_team']} @ {row['home_team']}")
        actual_margin, actual_total = finals[key]
        pred_margin = _number(row["pred_margin"])
        pred_total = _number(row["pred_total"])
        pred_win = _number(row["pred_win"])
        home_win = 1 if actual_margin > 0 else 0
        output_rows.append(
            {
                "game_id": str(row["game_id"]),
                "away_team": row["away_team"],
                "home_team": row["home_team"],
                "pred_margin": pred_margin,
                "pred_total": pred_total,
                "pred_home_win": pred_win,
                "actual_home_margin": actual_margin,
                "actual_total": actual_total,
                "margin_error": actual_margin - pred_margin,
                "total_error": actual_total - pred_total,
                "margin_direction_correct": int((pred_margin > 0) == (actual_margin > 0)),
                "home_win_outcome": home_win,
                "brier_component": (pred_win - home_win) ** 2,
            }
        )
    if len({row["game_id"] for row in output_rows}) != 47:
        raise ValueError("duplicate game identity")

    def mean(values: list[float]) -> float:
        return math.fsum(values) / len(values)

    summary = {
        "predictions": 47,
        "finals_joined": 47,
        "unresolved": 0,
        "margin_direction_correct": sum(row["margin_direction_correct"] for row in output_rows),
        "margin_mae": mean([abs(row["margin_error"]) for row in output_rows]),
        "signed_margin_error": mean([row["margin_error"] for row in output_rows]),
        "total_mae": mean([abs(row["total_error"]) for row in output_rows]),
        "signed_total_error": mean([row["total_error"] for row in output_rows]),
        "home_win_brier": mean([row["brier_component"] for row in output_rows]),
    }
    expected = {
        "margin_direction_correct": 32,
        "margin_mae": 15.525,
        "signed_margin_error": -1.332,
        "total_mae": 14.116,
        "signed_total_error": -0.620,
        "home_win_brier": 0.2183,
    }
    for key, value in expected.items():
        actual = summary[key]
        if isinstance(value, int):
            if actual != value:
                raise ValueError(f"reported aggregate mismatch: {key}={actual}")
        elif round(actual, 4 if key == "home_win_brier" else 3) != value:
            raise ValueError(f"reported aggregate mismatch: {key}={actual}")
    return {
        "status": "PASS_COMPLETED_WEEK5_EXACT_ORIGINAL_RECONCILIATION",
        "scope": "WEEK5_FBS_VS_FBS_FIRST_FROZEN_ONLY",
        "artifact_id": 10897612260,
        "artifact_sha256": EXPECTED_ZIP_SHA256,
        "scorecard_path": str(scorecard),
        "summary": summary,
        "rows": output_rows,
        "market_decision_close_execution_reconstruction": False,
        "scientific_or_champion_effect": "NONE",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--scorecard", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()
    result = build(args.artifact, args.scorecard)
    args.json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    s = result["summary"]
    markdown = f"""# Completed Week 5 exact ORIGINAL baseline — 2026-10-25

Status: `PASS_COMPLETED_WEEK5_EXACT_ORIGINAL_RECONCILIATION`

This bounded replay independently joined the 47 governed FBS-vs-FBS predictions from accepted original artifact `10897612260` / SHA-256 `{EXPECTED_ZIP_SHA256}` to the 47 already-governed Week 5 finals in `evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md`. It reused proved evidence and did not reacquire outcomes, reconstruct decisions, or inspect target outcomes during prediction creation.

## Exact reproduced metrics

| Metric | Result |
|---|---:|
| Eligible predictions / joined finals | 47 / 47 |
| Unresolved identities | 0 |
| Margin direction | {s['margin_direction_correct']}/47 ({100*s['margin_direction_correct']/47:.1f}%) |
| Margin MAE | {s['margin_mae']:.12f} |
| Signed margin error | {s['signed_margin_error']:.12f} |
| Total MAE | {s['total_mae']:.12f} |
| Signed total error | {s['signed_total_error']:.12f} |
| Home-win Brier | {s['home_win_brier']:.12f} |

The results reproduce the accepted rounded Week 5 review: 32/47 direction, margin MAE 15.525, signed margin -1.332, total MAE 14.116, signed total -0.620, and Brier 0.2183.

## Boundaries

- Explicit original exclusions remain outside the denominator and are not converted into predictions.
- The original artifact also contains a modeled non-FBS matchup in this date range; it remains outside this governed FBS-vs-FBS baseline.
- Historical qualified markets, recommendations, closes, Caesars offers, executions, and ROI are not supplied by this replay and remain separately governed or unavailable.
- No Champion, FIRST_FROZEN, REFRESH, Challenger, TIME-HIDDEN, market, decision, execution, money, task, or schedule state changed.

Next completed-batch boundary: Week 6 exact ORIGINAL reconciliation, reusing its existing 49/49 scorecard and accepted review without reconstructing missing pre-event evidence.
"""
    args.markdown.write_text(markdown, encoding="utf-8")
    print(json.dumps({"status": result["status"], "summary": s}, sort_keys=True))


if __name__ == "__main__":
    main()
