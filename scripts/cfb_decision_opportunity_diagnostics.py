#!/usr/bin/env python3
"""Read-only, fail-closed opportunity diagnostics for heterogeneous weekly reviews.

Never changes canonical decisions or claims a wager is qualified.
Usage: python scripts/cfb_decision_opportunity_diagnostics.py review.json > diagnostics.json
"""
import argparse
import json
from collections import Counter
from pathlib import Path

MARKETS = ("away_spread", "home_spread", "away_moneyline", "home_moneyline", "over", "under")
ALIASES = {"away_ml": "away_moneyline", "home_ml": "home_moneyline"}
PRICE_WORDS = ("price", "payout", "expensive", "juice", "too steep", "number", "line moved", "at current odds")
FOOTBALL_WORDS = ("quarterback", "qb", "injur", "personnel", "deployment", "uncertain", "matchup", "rotation", "offense", "defense")

def games_from_review(data):
    if not isinstance(data, dict) or not isinstance(data.get("reports"), dict):
        raise ValueError("Expected a reports object; refusing to infer game coverage")
    if not data["reports"]:
        raise ValueError("Empty reports object; refusing to claim zero-game coverage")
    for section, report in data["reports"].items():
        if not isinstance(report, dict):
            raise ValueError("Malformed review section: " + str(section))
        if not any(key in report for key in ("rows", "games")):
            raise ValueError("Review section has no rows or games: " + str(section))
        for key in ("rows", "games"):
            entries = report.get(key, [])
            if not isinstance(entries, list):
                raise ValueError("Malformed review entries: " + str(section) + "." + key)
            for game in entries:
                if not isinstance(game, dict) or not game.get("game_id"):
                    raise ValueError("Unidentified game in review section: " + str(section))
                yield section, game

def normalize_market(value):
    if isinstance(value, dict):
        return str(value.get("state") or value.get("analytical_status") or "UNSPECIFIED").upper(), str(value.get("reason") or "")
    if isinstance(value, str):
        prefix = value.strip().split(None, 1)[0].rstrip(":").upper() if value.strip() else "UNSPECIFIED"
        return (prefix if prefix in {"PASS", "LEAN", "INCONCLUSIVE", "CONDITIONAL", "CONDITIONAL_PROPOSAL"} else "UNSPECIFIED"), value
    return "UNSPECIFIED", ""

def analyze(data):
    rows, seen, duplicates = [], set(), []
    source_shapes = {}
    for section, game in games_from_review(data):
        game_id = str(game["game_id"])
        if game_id in seen:
            duplicates.append({"game_id": game_id, "additional_section": section})
            for prior in rows:
                if prior["game_id"] == game_id:
                    prior["identity_conflict"] = True
                    prior["category"] = "DUPLICATE_IDENTITY_CONFLICT"
                    prior["bet_authorized"] = False
            continue  # Quarantine both interpretations; never treat the first as clean.
        seen.add(game_id)
        market_sources = [key for key in ("six_markets", "six_market_review", "branches")
                          if isinstance(game.get(key), dict)]
        if len(market_sources) != 1:
            raise ValueError("Expected exactly one six-market review source for game " + game_id)
        source_shapes[game_id] = market_sources[0]
        markets = game[market_sources[0]]
        for market in MARKETS:
            raw = markets.get(market)
            if raw is None:
                alias = next((a for a, canonical in ALIASES.items() if canonical == market and a in markets), None)
                raw = markets.get(alias) if alias else None
            if market in {"away_moneyline", "home_moneyline"}:
                alias = "away_ml" if market == "away_moneyline" else "home_ml"
                if market in markets and alias in markets and markets[market] != markets[alias]:
                    raise ValueError("Conflicting market aliases for game " + game_id + ": " + market)
            state, reason = normalize_market(raw)
            lower = reason.lower()
            price_signal = any(word in lower for word in PRICE_WORDS)
            football_signal = any(word in lower for word in FOOTBALL_WORDS)
            # A price mention does not establish price-only causation.
            if raw is None or state == "UNSPECIFIED":
                category = "MARKET_REVIEW_NOT_EXTRACTABLE"
            elif state in {"CONDITIONAL", "CONDITIONAL_PROPOSAL"}:
                category = "PROPOSAL_REQUIRES_QUALIFICATION"
            elif state == "LEAN":
                category = "LEAN_REQUIRES_REVIEW"
            elif state == "QUOTE_UNAVAILABLE":
                category = "QUOTE_UNAVAILABLE_NOT_GRADED"
            elif state in {"SPECIFIC_RECHECK", "RESEARCH_LEAN"}:
                category = "ANALYTICAL_RECHECK_NOT_CANONICAL_DECISION"
            elif state == "PASS_CURRENT_REVIEW":
                category = "ANALYTICAL_PASS_NOT_CANONICAL_DECISION"
            elif state in {"ANALYTICAL_CONDITIONAL", "ANALYTICAL_CONDITIONAL_PROPOSAL"}:
                category = "ANALYTICAL_PROPOSAL_NOT_CANONICAL_DECISION"
            elif state == "INCONCLUSIVE":
                category = "UNRESOLVED"
            elif state == "PASS" and price_signal:
                category = "PASS_WITH_PRICE_FACTOR_NOT_PRICE_ONLY_PROVEN"
            elif state == "PASS":
                category = "PASS_OTHER_OR_UNCLASSIFIED"
            else:
                category = "UNCLASSIFIED_REVIEW"
            rows.append({"game_id": game_id, "section": section, "market": market,
                         "original_state": state, "category": category,
                         "price_factor_mentioned": price_signal,
                         "football_factor_mentioned": football_signal,
                         "reason": reason,
                         "bet_authorized": False})
    if not seen:
        raise ValueError("No identifiable games; refusing zero-game diagnostic")
    counts = Counter(r["category"] for r in rows)
    section_counts = {}
    for row in rows:
        section_counts.setdefault(row["section"], Counter())[row["category"]] += 1
    missing_count = counts.get("MARKET_REVIEW_NOT_EXTRACTABLE", 0)
    conflict_count = counts.get("DUPLICATE_IDENTITY_CONFLICT", 0)
    unclassified_count = counts.get("UNCLASSIFIED_REVIEW", 0)
    quote_unavailable_count = counts.get("QUOTE_UNAVAILABLE_NOT_GRADED", 0)
    reviewed_count = len(rows) - missing_count - conflict_count - unclassified_count - quote_unavailable_count
    return {"schema": "CFB_DECISION_OPPORTUNITY_DIAGNOSTICS_V1",
            "status": "READ_ONLY_NOT_PRODUCTION_NOT_WAGER_AUTHORITY",
            "game_count": len(seen), "market_slots": len(rows),
            "duplicate_identity_conflicts": duplicates,
            "source_review_shapes": dict(sorted(source_shapes.items())),
            "market_slot_counts": dict(sorted(counts.items())),
            "reviewed_nonconflicted_market_slots": reviewed_count,
            "missing_market_slots": missing_count,
            "unclassified_market_slots": unclassified_count,
            "quote_unavailable_market_slots": quote_unavailable_count,
            "conflicted_market_slots": conflict_count,
            "section_market_slot_counts": {k: dict(sorted(v.items())) for k, v in section_counts.items()},
            "method_limitations": [
                "Review-source state is not canonical decision state; analytical_status is retained separately.",
                "Keyword price factors are not proof that price alone caused PASS.",
                "No calibrated probability, EV, quote qualification, or ranking is inferred.",
                "QUOTE_UNAVAILABLE is a source-availability state, not a graded price or betting decision.",
                "Missing or unrecognized market state is not counted as a completed review.",
                "Duplicate game identities mark all retained market slots conflicted and quarantine later rows."
            ], "rows": rows}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("review", type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(json.loads(args.review.read_text())), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
