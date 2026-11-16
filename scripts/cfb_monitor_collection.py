"""Collect and verify the active weekly Monitor input. Read-only for engine state."""

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from zipfile import ZipFile

from lxml import html

import cfb_week11_publication as week
from cfb_cbs_full_board_normalizer import WEEK12_LINEAGE_SHA, WEEK12_URL, normalize

ROOT = Path(__file__).resolve().parents[1]
MARKET = ROOT / "evidence/operational/CFB_MARKET_MONITOR_STATE.md"
PERSONNEL_URL = "https://kickoffstatus.com/"
MAX_BYTES = 8_000_000
# CBS kept both event IDs after the SEC moved the same Week 11 game.
# https://soonersports.com/news/2026/11/14/ou-ole-miss-football-game-moved-to-sunday-at-noon
OLE_MISS_OKLAHOMA_ORIGINAL = ("50028715", "NCAAF_20261114_MISS@OKLA")
OLE_MISS_OKLAHOMA_RESCHEDULED = ("50051570", "NCAAF_20261115_MISS@OKLA")


@dataclass(frozen=True)
class CollectionProfile:
    name: str
    start: datetime
    end: datetime
    url: str
    lineage: Path
    lineage_blob: str

    @property
    def schema(self):
        return f"CFB_{self.name}_MONITOR_COLLECTION_V1"


PROFILES = (
    CollectionProfile(
        "WEEK11", week.gate.clock("2026-11-10T00:00:00-06:00"),
        week.gate.clock("2026-11-16T00:00:00-06:00"), week.WEEK11_URL,
        ROOT / "evidence/audits/CFB_WEEK11_ORIGINAL_ANCESTRY_RECOVERY_20261109.json",
        week.WEEK11_LINEAGE_SHA,
    ),
    CollectionProfile(
        "WEEK12", week.gate.clock("2026-11-16T00:00:00-06:00"),
        week.gate.clock("2026-11-23T00:00:00-06:00"), WEEK12_URL,
        ROOT / "evidence/audits/CFB_WEEK12_CBS_ORIGINAL_LINEAGE_PREFLIGHT_20261115.json",
        WEEK12_LINEAGE_SHA,
    ),
)


def active_profile(observed):
    for profile in PROFILES:
        if profile.start <= observed < profile.end:
            return profile
    raise ValueError("no accepted collection profile at this clock")


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()


def utc():
    return datetime.now(timezone.utc)


def acquire(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=20) as response:
        if response.geturl() != url:
            raise ValueError("unexpected source redirect")
        payload = response.read(MAX_BYTES + 1)
    if not 0 < len(payload) <= MAX_BYTES:
        raise ValueError("source response outside byte bounds")
    return payload, utc().isoformat()


def board_projection(payload):
    def text(node):
        return " ".join(node.text_content().split())

    def event(table):
        return table.get("data-game-id"), table.get("data-game-abbrev")

    output = []
    tables = html.fromstring(payload).xpath("//table")
    events = [event(table) for table in tables]
    # Drop only the corroborated obsolete record when both exact records occur
    # once. Preserve archived single-record captures and let any other duplicate
    # reach the normalizer's identity gate. The artifact retains the raw HTML.
    has_reschedule_pair = (
        events.count(OLE_MISS_OKLAHOMA_ORIGINAL) == 1
        and events.count(OLE_MISS_OKLAHOMA_RESCHEDULED) == 1
    )
    for table, identity in zip(tables, events):
        if has_reschedule_pair and identity == OLE_MISS_OKLAHOMA_ORIGINAL:
            continue
        rows = table.xpath(".//tr")
        header = [text(cell) for cell in rows[0].xpath("./th|./td")]
        if header[1:] != ["Final", "Open", "Spread", "ML Moneyline", "Total"]:
            raise ValueError("unexpected CBS table headings")
        output.append("| " + " | ".join(header[:4] + ["MLMoneyline", header[5]]) + " |")
        for row in rows[1:3]:
            cells = row.xpath("./td|./th")
            if len(cells) != 6:
                raise ValueError("unexpected CBS team row")
            links = [a for a in cells[0].xpath(".//a[@href]") if text(a)]
            if not links:
                raise ValueError("CBS team identity absent")
            name = links[-1]
            team = f"[{text(name)}]({urljoin('https://www.cbssports.com', name.get('href'))})"
            offers = []
            for cell in cells[3:]:
                icons = [url for url in cell.xpath(".//img/@src") if "/books-icons/" in url]
                offers.append(" ".join([text(cell)] + [f"![book]({url})" for url in icons]))
            output.append("| " + " | ".join([team, text(cells[1]), text(cells[2]), *offers]) + " |")
    return "\n".join(output) + "\n"


def inspect(payload, recovered_by):
    observed = week.gate.clock(recovered_by)
    profile = active_profile(observed)
    capture = board_projection(payload)
    elapsed = {}
    if profile.name == "WEEK11":
        prior = week.gate.selected_block(MARKET.read_text(), week.MARKET_TAG,
                                         week.gate.WEEKLY_MARKET_SCHEMA, observed)
        elapsed = {r["game_id"]: r["kickoff_utc"] for r in prior["rows"]
                   if r["kickoff_utc"] and week.gate.clock(r["kickoff_utc"]) < observed}
    board = normalize(capture, profile.lineage.read_text(), recovered_by,
                      source_url=profile.url, profile=profile.name,
                      retained_elapsed_kickoffs=elapsed)
    missing = {g["game_id"]: [f"{t['team']}:{k}" for t in g["team_offers"]
                            for k in ("spread", "moneyline", "total")
                            if t[k]["availability"] == "UNAVAILABLE"]
               for g in board["games"] if g["temporal_status"] == "FUTURE_AT_CAPTURE"}
    return capture, board["coverage"], {k: v for k, v in missing.items() if v}


def digest(payload):
    return {"bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()}


def collect(out, run, attempt, event):
    profile = active_profile(utc())
    raw, recovered_by = acquire(profile.url)
    if active_profile(week.gate.clock(recovered_by)) != profile:
        raise ValueError("source acquisition crossed the collection profile boundary")
    capture, coverage, gaps = inspect(raw, recovered_by)
    files = {"cbs.html": raw, "capture.md": capture.encode()}
    personnel = {"url": PERSONNEL_URL, "status": "UNAVAILABLE", "recovered_by": None}
    try:
        report, personnel_at = acquire(PERSONNEL_URL)
        label = profile.name.replace("WEEK", "Week ")
        if label not in html.fromstring(report).text_content():
            raise ValueError(f"personnel page does not identify {label}")
        files["personnel.html"] = report
        personnel.update(status="RAW_REPORT_REQUIRES_GAME_LEVEL_REVIEW", recovered_by=personnel_at)
    except (OSError, ValueError) as exc:
        personnel["reason"] = str(exc)[:200]
    manifest = dict(schema=profile.schema, profile=profile.name, producer_head=git("rev-parse", "HEAD"),
                    run_id=run, run_attempt=attempt, event=event, source_url=profile.url,
                    recovered_by=recovered_by, lineage_blob=profile.lineage_blob,
                    coverage=coverage, missing_markets=gaps, personnel=personnel,
                    files={name: digest(data) for name, data in files.items()})
    out.mkdir()
    for name, data in files.items():
        (out / name).write_bytes(data)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")


def verify(archive, output, run, attempt, head, event):
    with ZipFile(archive) as package:
        members = package.infolist()
        names = [m.filename for m in members]
        required = {"manifest.json", "cbs.html", "capture.md"}
        if (len(names) != len(set(names)) or not required <= set(names)
                or set(names) - required - {"personnel.html"}
                or sum(m.file_size for m in members) > 3 * MAX_BYTES):
            raise ValueError("invalid artifact member set or size")
        manifest = json.loads(package.read("manifest.json"), object_pairs_hook=week.gate.unique)
        now = utc()
        profile = active_profile(now)
        expected = (profile.schema, profile.name, run, attempt, head, event,
                    profile.url, profile.lineage_blob)
        fields = ("schema", "profile", "run_id", "run_attempt", "producer_head",
                  "event", "source_url", "lineage_blob")
        if tuple(manifest[k] for k in fields) != expected:
            raise ValueError("artifact identity differs from trusted run metadata")
        observed = week.gate.clock(manifest["recovered_by"])
        if not 0 <= (now - observed).total_seconds() <= 900:
            raise ValueError("collection package stale or future-dated")
        if active_profile(observed) != profile:
            raise ValueError("artifact observed in a different collection profile")
        subprocess.run(["git", "-C", str(ROOT), "merge-base", "--is-ancestor", head,
                        "HEAD"], check=True)
        files = {name: package.read(name) for name in names if name != "manifest.json"}
    if {name: digest(data) for name, data in files.items()} != manifest["files"]:
        raise ValueError("artifact member digest mismatch")
    capture, coverage, gaps = inspect(files["cbs.html"], manifest["recovered_by"])
    if (capture.encode() != files["capture.md"] or coverage != manifest["coverage"]
            or gaps != manifest["missing_markets"]):
        raise ValueError("artifact board does not reproduce from source bytes")
    output.mkdir()
    for name, data in files.items():
        (output / name).write_bytes(data)
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"status": "PASS_COLLECTION_PACKAGE_ONLY", **manifest}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="mode", required=True)
    for mode in ("collect", "verify"):
        cmd = commands.add_parser(mode)
        cmd.add_argument("--output", type=Path, required=True)
        cmd.add_argument("--run", type=int, required=True)
        cmd.add_argument("--attempt", type=int, required=True)
        cmd.add_argument("--event", choices=("schedule", "push", "workflow_dispatch"), required=True)
    verifier = commands.choices["verify"]
    verifier.add_argument("--archive", type=Path, required=True)
    verifier.add_argument("--head", required=True)
    args = parser.parse_args()
    if args.mode == "collect":
        collect(args.output, args.run, args.attempt, args.event)
    else:
        verify(args.archive, args.output, args.run, args.attempt, args.head, args.event)


if __name__ == "__main__":
    main()
