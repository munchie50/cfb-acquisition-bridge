"""Read-only producer acceptance classifier; QA branch only."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    authority_read: bool
    scheduler_status: str
    chat_ref: str | None
    invocation_id: str
    startup_run_id: str | None
    closure_run_id: str | None
    readback_run_id: str | None
    qualified_publication: bool

def classify(e: Evidence) -> str:
    if not e.authority_read:
        return "STARTUP_UNVERIFIED"
    if not e.invocation_id or e.startup_run_id != e.invocation_id:
        return "DISPATCH_OR_HANDOFF_UNVERIFIED"
    if e.closure_run_id != e.invocation_id or not e.qualified_publication:
        return "PRODUCER_INCOMPLETE"
    if e.readback_run_id != e.invocation_id:
        return "ACCEPTANCE_UNVERIFIED"
    if e.scheduler_status != "completed":
        return "SCHEDULER_PRODUCER_CONFLICT"
    return "RUN_PASS_ELIGIBLE"

def self_test() -> None:
    good = dict(authority_read=True, scheduler_status="completed", chat_ref="chat",
                invocation_id="run1", startup_run_id="run1", closure_run_id="run1",
                readback_run_id="run1", qualified_publication=True)
    cases = [
        ({"authority_read": False}, "STARTUP_UNVERIFIED"),
        ({"startup_run_id": None, "scheduler_status": "no_update", "chat_ref": None}, "DISPATCH_OR_HANDOFF_UNVERIFIED"),
        ({"startup_run_id": "run2"}, "DISPATCH_OR_HANDOFF_UNVERIFIED"),
        ({"closure_run_id": None}, "PRODUCER_INCOMPLETE"),
        ({"closure_run_id": "run2"}, "PRODUCER_INCOMPLETE"),
        ({"qualified_publication": False}, "PRODUCER_INCOMPLETE"),
        ({"readback_run_id": None}, "ACCEPTANCE_UNVERIFIED"),
        ({"readback_run_id": "run2"}, "ACCEPTANCE_UNVERIFIED"),
        ({"scheduler_status": "no_update", "chat_ref": None}, "SCHEDULER_PRODUCER_CONFLICT"),
        ({"scheduler_status": "failed"}, "SCHEDULER_PRODUCER_CONFLICT"),
        ({"scheduler_status": "in_progress"}, "SCHEDULER_PRODUCER_CONFLICT"),
        ({"scheduler_status": "unknown"}, "SCHEDULER_PRODUCER_CONFLICT"),
        ({}, "RUN_PASS_ELIGIBLE"),
    ]
    for changes, expected in cases:
        assert classify(Evidence(**(good | changes))) == expected, (changes, expected)

if __name__ == "__main__":
    self_test()
    print("13 linked-run QA fixtures PASS")
