#!/usr/bin/env python3
"""CFB scheduler handoff diagnostic. Offline, read-only, standard library only.

Usage: python scripts/cfb_scheduler_diagnose.py observations.json
Input: {"runs":[{"id":"...","task":"...","status":"no_update",
"started_at":"ISO UTC","completed_at":"ISO UTC","chat_ref":null,
"startup_marker":false,"connector_attempt":null,"publication":false,
"closure":false}]}.
Unknown evidence must be null or omitted, NEVER guessed false.
"""
import json
import sys
from datetime import datetime

LAYERS = [
    ("invocation", "Scheduler recorded an invocation"),
    ("conversation", "Execution conversation/worker created"),
    ("startup_marker", "Producer startup marker independently verified"),
    ("connector_attempt", "First connector call attempted"),
    ("publication", "Governed publication independently verified"),
    ("closure", "Terminal receipt independently verified"),
]

def elapsed(run):
    try:
        a = datetime.fromisoformat(run["started_at"].replace("Z", "+00:00"))
        b = datetime.fromisoformat(run["completed_at"].replace("Z", "+00:00"))
        return round((b - a).total_seconds(), 3)
    except (KeyError, ValueError, TypeError):
        return None

def assess(run):
    status = run.get("status", "unknown")
    observed = {"invocation": bool(run.get("id"))}
    observed["conversation"] = True if run.get("chat_ref") else (False if "chat_ref" in run else None)
    for key, _ in LAYERS[2:]:
        observed[key] = run.get(key)
    verified = [key for key, _ in LAYERS if observed[key] is True]
    first_unknown = next((key for key, _ in LAYERS if observed[key] is not True), None)
    contradiction = any(observed[key] is True and any(observed[earlier] is False for earlier, _ in LAYERS[:i])
                        for i, (key, _) in enumerate(LAYERS))
    return {
        "id": run.get("id"), "task": run.get("task"), "status": status,
        "duration_seconds": elapsed(run),
        "verified_layers": verified, "first_unverified_layer": first_unknown,
        "contradictory_evidence": contradiction,
        "classification": ("EVIDENCE_CONFLICT" if contradiction else
            "NO_INVOCATION_EVIDENCE" if not observed["invocation"] else
            "PRE_PRODUCER_STARTUP_UNPROVEN" if observed["startup_marker"] is not True else
            "PRODUCER_STARTED_CLOSURE_UNPROVEN" if observed["closure"] is not True else
            "CLOSURE_VERIFIED"),
        "next_test": ("Reconcile contradictory source records before mutation" if contradiction else
            "Obtain scheduler invocation/worker creation logs" if observed["conversation"] is not True else
            "Check first producer write/readback and connector access logs" if observed["startup_marker"] is not True else
            "Inspect first missing governed stage and its error/receipt" if observed["closure"] is not True else
            "Compare accepted publication and scheduler terminal status"),
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/cfb_scheduler_diagnose.py observations.json")
    with open(sys.argv[1], encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data.get("runs"), list):
        raise SystemExit("Input must contain runs array")
    results = [assess(run) for run in data["runs"]]
    successful = [r for r in results if r["classification"] == "CLOSURE_VERIFIED"]
    failed = [r for r in results if r["classification"] != "CLOSURE_VERIFIED"]
    print(json.dumps({
        "schema": "cfb.scheduler.diagnostic.v1",
        "read_only": True,
        "runs": results,
        "comparison": {"verified_closure_runs": len(successful),
                       "unverified_closure_runs": len(failed),
                       "cross_task_pattern": len({r["task"] for r in failed if r["task"]}) > 1},
        "caution": "No inferred platform root cause. no_update alone does not prove a connector or producer failure. Missing evidence remains unknown. This tool cannot access internal scheduler logs.",
    }, indent=2))

if __name__ == "__main__":
    main()
