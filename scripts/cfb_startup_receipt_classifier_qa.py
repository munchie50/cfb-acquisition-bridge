"""Read-only CFB producer receipt classifier. QA only; no external calls."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    authority_read: bool
    scheduler_status: str
    chat_ref: str | None
    producer_started: bool
    producer_closed: bool
    independent_readback: bool

def classify(e: Evidence) -> str:
    if not e.authority_read:
        return "STARTUP_UNVERIFIED"
    if not e.producer_started:
        return "DISPATCH_OR_HANDOFF_UNVERIFIED"
    if not e.producer_closed:
        return "PRODUCER_INCOMPLETE"
    if not e.independent_readback:
        return "ACCEPTANCE_UNVERIFIED"
    if e.scheduler_status == "no_update":
        return "SCHEDULER_PRODUCER_CONFLICT"
    return "RUN_PASS_ELIGIBLE"

def self_test() -> None:
    cases = [
        (Evidence(False, "no_update", None, False, False, False), "STARTUP_UNVERIFIED"),
        (Evidence(True, "no_update", None, False, False, False), "DISPATCH_OR_HANDOFF_UNVERIFIED"),
        (Evidence(True, "completed", "chat", True, False, False), "PRODUCER_INCOMPLETE"),
        (Evidence(True, "completed", "chat", True, True, False), "ACCEPTANCE_UNVERIFIED"),
        (Evidence(True, "completed", "chat", True, True, True), "RUN_PASS_ELIGIBLE"),
        (Evidence(True, "no_update", None, True, True, True), "SCHEDULER_PRODUCER_CONFLICT"),
    ]
    for e, expected in cases:
        assert classify(e) == expected, (e, expected)

if __name__ == "__main__":
    self_test()
    print("6 QA receipt-classification fixtures PASS")
