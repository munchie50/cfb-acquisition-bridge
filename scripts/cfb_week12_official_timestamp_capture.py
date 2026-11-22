#!/usr/bin/env python3
"""Read-only Week12 NCAA source capture: response UTC bounds, bytes, SHA256; never canonical admission."""
import concurrent.futures
import datetime as dt
import hashlib
import json
import pathlib
import urllib.request
from urllib.error import HTTPError, URLError

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "evidence/audits/CFB_WEEK12_NCAA_70_GAME_SOURCE_CROSSWALK_RECONCILED_20261122_QA_ONLY.json"
OUT = ROOT / "week12_official_timestamp_capture.json"
def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="microseconds")
def capture(row):
    start = utc()
    url = row["source_url"]
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; CFB-audit/1.0)", "Accept": "text/html"})
        with urllib.request.urlopen(req, timeout=18) as res:
            body = res.read(2_000_001)
            status = res.status
            final_url = res.url
            truncated = len(body) > 2_000_000
        end = utc()
        html = body.decode("utf-8", errors="replace")
        # A response capture is NOT a verified final unless game ID, scores, and FINAL are all verified.
        return dict(game_id=row["game_id"], ncaa_game_id=row["ncaa_game_id"], url=url, final_url=final_url,
                    request_started_utc=start, response_completed_utc=end, http_status=status,
                    bytes=len(body), sha256=hashlib.sha256(body).hexdigest(), truncated=truncated,
                    game_id_in_response=str(row["ncaa_game_id"]) in html,
                    final_token_in_response="FINAL" in html.upper(),
                    source_status="CAPTURE_ONLY_NOT_SCORE_ADMITTED")
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        return dict(game_id=row["game_id"], ncaa_game_id=row["ncaa_game_id"], url=url,
                    request_started_utc=start, response_completed_utc=utc(), error=type(exc).__name__+":"+str(exc)[:250],
                    source_status="FETCH_FAILED_NOT_ADMITTED")
def main():
    doc=json.loads(SRC.read_text())
    rows=doc["rows"]
    if len(rows)!=70 or len({x["game_id"] for x in rows})!=70 or len({x["ncaa_game_id"] for x in rows})!=70:
        raise SystemExit("FAIL_CLOSED: 70 unique games required")
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results=list(pool.map(capture,rows))
    result=dict(schema="CFB_WEEK12_NCAA_DIRECT_SOURCE_UTC_CAPTURE_QA_V1",
                status="READ_ONLY_RAW_SOURCE_CAPTURE_NOT_CANONICAL",
                recorded_at_utc=utc(),source_crosswalk=str(SRC.relative_to(ROOT)),
                summary=dict(total=len(results),http_200=sum(x.get("http_status")==200 for x in results),
                             failed=sum("error" in x for x in results),admitted=0),
                rows=results)
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print("Week12 direct NCAA capture:",json.dumps(result["summary"],sort_keys=True),flush=True)
    print("Capture artifact:",OUT.name,flush=True)
    if result["summary"]["http_200"]==0:
        raise SystemExit("FAIL_CLOSED: no direct NCAA page fetched; inspect artifact and use established provider workaround")
if __name__=="__main__":
    main()
