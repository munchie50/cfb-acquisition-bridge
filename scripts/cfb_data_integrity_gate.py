#!/usr/bin/env python3
"""Read-only CFB review integrity gate; never authorizes bets."""
import argparse
import json
from collections import Counter
from pathlib import Path

MARKETS = ("away_spread", "home_spread", "away_moneyline", "home_moneyline", "over", "under")
SOURCES = ("six_markets", "six_market_review", "branches")
KNOWN = {"PASS", "LEAN", "INCONCLUSIVE", "CONDITIONAL", "CONDITIONAL_PROPOSAL",
         "SPECIFIC_RECHECK", "RESEARCH_LEAN", "PASS_CURRENT_REVIEW",
         "ANALYTICAL_CONDITIONAL", "ANALYTICAL_CONDITIONAL_PROPOSAL", "QUOTE_UNAVAILABLE"}
ALIASES = {"away_moneyline": "away_ml", "home_moneyline": "home_ml"}

def state_of(value):
    if isinstance(value, dict):
        state = value.get("state")
        analytical = value.get("analytical_status")
        if state and analytical and str(state).upper() != str(analytical).upper():
            return "CONFLICT"
        return str(state or analytical or "").strip().upper()
    if isinstance(value, str):
        return value.strip().split(None, 1)[0].rstrip(":").upper() if value.strip() else ""
    return ""

def audit(data):
    findings, identities, sections = [], {}, Counter()
    def flag(severity, code, section, game_id=None, market=None):
        findings.append({"severity": severity, "code": code, "section": section,
                         "game_id": game_id, "market": market})
    if not isinstance(data, dict) or not isinstance(data.get("reports"), dict) or not data["reports"]:
        flag("FAIL", "REPORTS_MISSING_OR_INVALID", "root")
    else:
        for section, report in data["reports"].items():
            if not isinstance(report, dict):
                flag("FAIL", "SECTION_INVALID", section)
                continue
            if not any(k in report for k in ("rows", "games")):
                flag("FAIL", "SECTION_WITHOUT_GAMES", section)
            for key in ("rows", "games"):
                games = report.get(key, [])
                if not isinstance(games, list):
                    flag("FAIL", "GAME_LIST_INVALID", section)
                    continue
                for game in games:
                    sections[section] += 1
                    if not isinstance(game, dict) or not game.get("game_id"):
                        flag("FAIL", "GAME_ID_MISSING", section)
                        continue
                    gid = str(game["game_id"])
                    identities.setdefault(gid, []).append(section)
                    shapes = [k for k in SOURCES if isinstance(game.get(k), dict)]
                    if len(shapes) > 1:
                        flag("FAIL", "AMBIGUOUS_MARKET_SOURCE", section, gid)
                    if not shapes:
                        flag("WARN", "MARKET_SOURCE_MISSING", section, gid)
                        continue
                    markets = game[shapes[0]]
                    for market in MARKETS:
                        alias = ALIASES.get(market)
                        if alias and alias in markets and market in markets and markets[alias] != markets[market]:
                            flag("FAIL", "MARKET_ALIAS_CONFLICT", section, gid, market)
                        value = markets.get(market, markets.get(alias) if alias else None)
                        if value is None:
                            flag("WARN", "MARKET_MISSING", section, gid, market)
                            continue
                        state = state_of(value)
                        if state == "CONFLICT":
                            flag("FAIL", "STATUS_FIELD_CONFLICT", section, gid, market)
                        elif not state or state not in KNOWN:
                            flag("WARN", "STATUS_UNRECOGNIZED", section, gid, market)
                        elif state == "QUOTE_UNAVAILABLE":
                            flag("WARN", "QUOTE_UNAVAILABLE", section, gid, market)
    for gid, locations in identities.items():
        if len(locations) > 1:
            flag("FAIL", "DUPLICATE_GAME_ID", ",".join(locations), gid)
    counts = Counter(f["severity"] for f in findings)
    result = "FAIL" if counts["FAIL"] else ("WARN" if counts["WARN"] else "PASS")
    return {"schema": "CFB_DATA_INTEGRITY_GATE_V1", "status": result,
            "scope": "READ_ONLY_SOURCE_STRUCTURE_NOT_BET_AUTHORITY",
            "records": sum(sections.values()), "unique_games": len(identities),
            "section_records": dict(sections), "finding_counts": dict(counts),
            "finding_code_counts": dict(Counter(f["code"] for f in findings)),
            "findings": findings,
            "limitations": ["Structural validity is not predictive accuracy.",
                            "WARN does not prove source corruption.",
                            "FAIL prevents integrity acceptance, not production publication automatically.",
                            "Quote availability and duplicate identity require independent reconciliation."]}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("review", type=Path)
    args = parser.parse_args()
    print(json.dumps(audit(json.loads(args.review.read_text())), indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
