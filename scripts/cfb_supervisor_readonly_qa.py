#!/usr/bin/env python3
"""Read-only CFB supervisor classifier. Stdlib only; never retries or mutates."""
import argparse
import datetime as dt
import json
from pathlib import Path

def classify(record, now, start_grace=300, finish_grace=900):
    due=dt.datetime.fromisoformat(record["scheduled_for"].replace("Z","+00:00"))
    start=record.get("started_at")
    end=record.get("completed_at")
    status=(record.get("recorded_status") or "").lower()
    artifact=record.get("producer_artifact_verified",False)
    if not start:
        return "MISSING_START" if now >= due+dt.timedelta(seconds=start_grace) else "PENDING"
    began=dt.datetime.fromisoformat(start.replace("Z","+00:00"))
    if not end:
        return "NO_TERMINAL" if now >= began+dt.timedelta(seconds=finish_grace) else "RUNNING"
    if status in ("no_update","failed","error","cancelled","timed_out"):
        return "RUN_FAILURE"
    if status not in ("completed","success","passed"):
        return "UNKNOWN_STATUS"
    return "VERIFIED_PASS" if artifact else "PRODUCER_UNVERIFIED"

def main():
    p=argparse.ArgumentParser()
    p.add_argument("receipts",type=Path)
    p.add_argument("--now",required=True)
    args=p.parse_args()
    now=dt.datetime.fromisoformat(args.now.replace("Z","+00:00"))
    assert now.tzinfo is not None
    for r in json.loads(args.receipts.read_text()):
        result=classify(r,now)
        print(json.dumps({"run_id":r["id"],"classification":result,"needs_attention":result in ("MISSING_START","NO_TERMINAL","RUN_FAILURE","UNKNOWN_STATUS","PRODUCER_UNVERIFIED")},sort_keys=True))
if __name__=="__main__":
    main()
