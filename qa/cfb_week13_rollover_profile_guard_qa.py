"""Read-only regression test: preserve Week12 and register the approved Week13 boundary."""
import ast
from datetime import datetime
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / "scripts/cfb_monitor_collection.py"
tree = ast.parse(SOURCE.read_text())
profiles = next(n.value for n in tree.body if isinstance(n, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == "PROFILES" for t in n.targets))
entries = []
for item in profiles.elts:
    if not isinstance(item, ast.Call) or len(item.args) < 3:
        raise AssertionError("unexpected profile constructor")
    name = ast.literal_eval(item.args[0])
    def clock(arg):
        if not isinstance(arg, ast.Call) or len(arg.args) != 1:
            raise AssertionError("unexpected profile clock")
        return datetime.fromisoformat(ast.literal_eval(arg.args[0]))
    entries.append((name, clock(item.args[1]), clock(item.args[2])))
assert entries == [
    ("WEEK11", datetime.fromisoformat("2026-11-10T00:00:00-06:00"),
     datetime.fromisoformat("2026-11-16T00:00:00-06:00")),
    ("WEEK12", datetime.fromisoformat("2026-11-16T00:00:00-06:00"),
     datetime.fromisoformat("2026-11-23T00:00:00-06:00")),
    ("WEEK13", datetime.fromisoformat("2026-11-23T00:00:00-06:00"),
     datetime.fromisoformat("2026-11-30T00:00:00-06:00")),
], "profile boundary or accepted profile set changed: independently review authority"
active = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "active_profile")
assert isinstance(active.body[-1], ast.Raise)
assert "NO_ACCEPTED_COLLECTION_PROFILE" in ast.literal_eval(active.body[-1].exc.args[0])
print("PASS: Week12 expires and approved Week13 window is registered")
