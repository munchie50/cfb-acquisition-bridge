"""Parse a Covers matchup odds markdown snapshot; never certify an executable offer."""
import json
import re
import sys

# Explicit source naming equivalence, not general fuzzy matching.
COVERS_TEAM_ALIASES = {"Mississippi": "Ole Miss", "Miami (FL)": "Miami"}

def match_canonical_pair(result, baseline):
    """Exact, unique team-pair match; no fuzzy joins or inferred kickoff."""
    teams = result["matchup"].removeprefix("# ").split(" vs ")
    if len(teams) != 2:
        return {"status": "IDENTITY_UNRESOLVED", "game_id": None}
    teams = [COVERS_TEAM_ALIASES.get(team, team) for team in teams]
    rows = [row for row in baseline["rows"]
            if row["away_team"] == teams[0] and row["home_team"] == teams[1]]
    if len(rows) != 1:
        return {"status": "IDENTITY_UNRESOLVED", "game_id": None}
    return {"status": "SHADOW_IDENTITY_MATCH_ONLY", "game_id": rows[0]["game_id"],
            "kickoff_independently_verified": False, "decision_authorized": False}

def reconcile_shadow_moneylines(result, canonical_match, inventory):
    """Count candidate branches only where CBS lacks them; never overwrite CBS."""
    game_id = canonical_match.get("game_id")
    rows = [row for row in inventory["rows"] if row["game_id"] == game_id]
    if canonical_match.get("status") != "SHADOW_IDENTITY_MATCH_ONLY" or len(rows) != 1:
        return {"status": "UNRESOLVED", "new_candidate_branches": 0,
                "decision_authorized": False}
    offers = result["displayed_moneyline_rows"]
    if len(offers) != 2:
        return {"status": "INCOMPLETE_PAIR", "game_id": game_id,
                "new_candidate_branches": 0, "decision_authorized": False}
    missing = [name for name in ("away_ml", "home_ml")
               if rows[0]["branches"][name]["availability"] != "DISPLAYED"]
    return {"status": "UNQUALIFIED_CANDIDATE_ONLY", "game_id": game_id,
            "new_candidate_branches": len(missing), "candidate_branch_names": missing,
            "independent_price_clock": None, "decision_authorized": False}

def discover_dated_matchups(markdown):
    """Discover only dated Nov 6/7 rows, not sidebar or unrelated weeks."""
    found = {}
    for line in markdown.splitlines():
        if not re.match(r"^\| Nov [67],", line):
            continue
        match = re.search(r"/matchup/(\d+)", line)
        if match:
            found[match.group(1)] = {
                "matchup_id": match.group(1),
                "odds_url": "https://www.covers.com/sport/football/ncaaf/matchup/"
                            + match.group(1) + "/odds",
                "status": "DISCOVERED_UNQUALIFIED"}
    return list(found.values())

def inspect(markdown, source_url, observed_at_utc):
    if not re.fullmatch(r"https://www\.covers\.com/sport/football/ncaaf/matchup/\d+/odds", source_url):
        raise ValueError("unsupported matchup source")
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", observed_at_utc):
        raise ValueError("explicit retrieval clock required")
    title = re.search(r"^([^\n]+) Odds$", markdown, re.M)
    if not title:
        raise ValueError("missing matchup identity")
    rows = []
    seen = set()
    for line in markdown.splitlines():
        if not line.startswith("| ") or "sportsbooks/" not in line:
            continue
        if "fanduel_icon.svg" not in line:
            continue
        match = re.search(r"\|\s*([+-]\d{2,5})!\[FanDuel", line)
        if match and int(match.group(1)) not in seen:
            seen.add(int(match.group(1)))
            rows.append({"displayed_moneyline": int(match.group(1)),
                         "book_display": "FanDuel", "source_row": line[:160]})
    return {"status": "UNQUALIFIED_SHADOW_SOURCE_ONLY", "matchup": title.group(1),
            "source_url": source_url, "retrieved_at_utc": observed_at_utc,
            "displayed_moneyline_rows": rows[:2],
            "independent_price_clock": None, "executable_offer_verified": False,
            "decision_authorized": False}

if __name__ == "__main__":
    print(json.dumps(inspect(sys.stdin.read(), sys.argv[1], sys.argv[2]), indent=2))
