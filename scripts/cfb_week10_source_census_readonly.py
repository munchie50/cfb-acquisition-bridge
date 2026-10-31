"""Strict read-only Week10 CBS board census; observed identities, not authoritative IDs."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

from cfb_cbs_full_board_normalizer import cells, plain

URL = "https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-10/"
HEADER = re.compile(r"^\| (Tue|Wed|Thu|Fri|Sat|Sun|Mon) [A-Z][a-z]{2} \d{1,2}(?:,|\s)")
TEAM = re.compile(r"(?<!!)\[([^\]]+)\]\(https://www\.cbssports\.com/college-football/teams/[^)]+\)")


def census(markdown, *, source_url=URL):
    if source_url != URL or "# Odds - Week 10" not in markdown:
        raise ValueError("unqualified Week10 page")
    result, pending, teams, total_team_rows = [], None, [], 0
    def finish():
        nonlocal pending, teams
        if pending is None:
            return
        if len(teams) != 2 or teams[0] == teams[1]:
            raise ValueError("partial/duplicate-team game")
        result.append({"source_header": pending, "away_team_observed": teams[0],
                       "home_team_observed": teams[1], "game_id": None,
                       "identity_qualified": False})
        pending, teams = None, []
    for line in markdown.splitlines():
        if not line.startswith("|"):
            continue
        c = cells(line)
        if HEADER.match(line):
            finish()
            if len(c) != 6 or list(map(plain, c[1:])) != ["Final", "Open", "Spread", "MLMoneyline", "Total"]:
                raise ValueError("unsupported market columns")
            pending = plain(c[0])
            continue
        names = TEAM.findall(c[0]) if c else []
        if not names:
            continue
        total_team_rows += 1
        if pending is None or len(c) != 6 or len(teams) >= 2:
            raise ValueError("unscoped/malformed team row")
        teams.append(names[-1])
    finish()
    pairs = [(r["away_team_observed"], r["home_team_observed"]) for r in result]
    if not result or len(set(pairs)) != len(pairs) or total_team_rows != 2 * len(result):
        raise ValueError("incomplete/duplicate observed slate")
    return {"status": "WEEK10_OBSERVED_SOURCE_CENSUS_ONLY",
            "source_url": source_url, "observed_games": len(result),
            "observed_team_rows": total_team_rows,
            "independent_identity_baseline_verified": False,
            "market_qualification": "NOT_PERFORMED",
            "publication_authorized": False, "games": result}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--capture", required=True, type=Path)
    a = p.parse_args()
    print(json.dumps(census(a.capture.read_text()), indent=2))
