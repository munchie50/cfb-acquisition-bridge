# Rollback snapshot — Market Monitor before alternate transport priority

Task ID: 6ae766e788d881919726d0eeb44450dd
Enabled: true
Schedule: unchanged, Friday 07CT/13CT included
Captured prior to task update on November 20 2026. Restore EXACT text between markers as full automation prompt using mcp__Automations__update, without changing schedule or task ID.

<!-- ORIGINAL PROMPT START -->
## Friday 1:00 p.m. Central Saturday slate review deadline

Effective for the November 20, 2026 placement window and recurring football weeks. The Market Monitor owns full review, publication, and readback of the Saturday slate by Friday 1:00 p.m. America/Chicago. Begin on Thursday and use the Friday 7:00 a.m. Monitor to finish and publish before the placement window. The Friday 1:00 p.m. Monitor is for final market and material changes and delivery verification. It must recover overdue work immediately if the deadline was missed and record the miss.

Account for every Saturday game, including prior PASS, exclusions, and conditional rows. Review applicable spreads, moneylines, totals, and supported derivatives and parlay candidates using qualified pricing and material evidence. A price refresh or retained PASS alone does not satisfy full review. Publish supported plays with exact limits, conditions, and cutoffs. Identify unfinished or blocked games explicitly with reasons and close incomplete if coverage or readback is missing. Evening may feed downstream evidence to Market Monitor. Later updates may address new material information within existing wager cutoffs. This review deadline does not extend or replace previously issued wager limits or execution cutoffs.

SAME-RUN CONTINUATION AND CHECKOUT DIAGNOSIS — Nov 19 CT
After verified RUN_STARTED and fresh authority recovery, when this task needs a real checkout and direct shell is available, make one bounded noninteractive Git HTTPS connectivity check using the normal worker network settings (git ls-remote on the canonical repository). Record proxy presence as a boolean only, without proxy values or credentials, and the exact sanitized failure category and host if it fails. If Git connects, run the accepted exact-byte helper on the authenticated pin, verify full ancestry and required scripts, and immediately continue the applicable work in this same invocation. A passing probe or checkout is an intermediate result. Continue through fresh CBS acquisition, game and market evaluation, compilation, and authorized Hot Sheet publication with independent readback. If the required checkout fails, continue independent authorized work, document the blocked stages, and persist/read back the governed terminal candidate and separate closure. Preserve existing source, decision, ownership and persistence gates.

FIRST ACTION — STARTUP TRACE: Before recovery, external research or production mutation, record observed UTC time, trigger type, task/invocation ID when available, and correlation ID. Immediately attempt append-only RUN_STARTED evidence/run_receipts/CFB_MARKET_MONITOR_TRACE_<UTC>_<ID>.md in GitHub munchie50/cfb-acquisition-bridge main and independently read back the exact file/SHA. Log connector attempt/result and every stage boundary with errors and evidence. Never log credentials. If this fails, report the exact first operation/error and fail closed. No RUN_STARTED means no proven producer startup; scheduler-level logs are required for pre-start no_update.

PRODUCTION RUNTIME ROUTING — DIRECT SHELL, 2026-11-19. This paragraph controls startup routing where the startup revision below assumes a combined cell. Immediately after independent RUN_STARTED readback, check the actual exposed tools. If a direct terminal/shell action is exposed, invoke it directly (outside the connector orchestration cell) once with: printf '%s\n' CFB_DIRECT_SHELL_STARTED; python3 --version; git --version. Capture actual tool identifier, marker, exit and sanitized error, or DIRECT_SHELL_NOT_EXPOSED if the surface does not exist. Independently check whether exec_command is callable inside the connector orchestration cell, using a marker-only command if needed to establish capability. Record the two results separately. A report without executed tool evidence is not a shell PASS. Do not stop after this probe; this is the live production Monitor.

If the combined route is callable, use the verified checkout cell below. If that route is unavailable before helper execution and direct shell passed, use the exact-byte direct fallback below. Get fresh main SHA and helper blob metadata from the authenticated GitHub connector at that exact SHA. If the metadata matches the embedded helper hash and 3,780-byte size, use the entire supplied command in a direct shell call, substituting only the fresh 40-hex SHA for REPLACE_WITH_FRESH_AUTHENTICATED_MAIN_SHA. This transfers the helper in the shell action itself. Do not download the helper from the shell, manually reconstruct Python, or retype its base64. If GitHub reports a changed helper blob, obtain exact base64 from the connector and verify against fresh metadata before execution, or fail closed at HELPER_TRANSFER. Poll any running shell session. Record DIRECT_HELPER_BYTES_VERIFIED separately from checkout. On helper failure record the actual subprocess stage and classified error. On SUPPORTED_GIT_RUNTIME_VERIFIED confirm exact HEAD, full ancestry and current-week producer checks, then immediately continue live Market Monitor work. If runtime remains blocked, preserve the verified handoff and perform independently feasible live work with the existing publication and closure gates. Record manual versus natural trigger.

```sh
expected_size=3780
expected_blob=b13930cb714eb87c8dce6136ffab6fbceeb44898
set -eu
pinned_head='REPLACE_WITH_FRESH_AUTHENTICATED_MAIN_SHA'
case "$pinned_head" in ''|*[!0-9a-f]*) exit 2;; esac
test "${#pinned_head}" -eq 40
if command -v python3 >/dev/null 2>&1; then
  checkout_python=python3
else
  checkout_python=python
fi
"$checkout_python" --version
git --version
printf '%s\n' SHELL_PROBE_PASS
umask 077
scratch=$(mktemp -d)
base64 -d > "$scratch/cfb_runtime_checkout.py" <<'CFB_EXACT_HELPER_B64'
IiIiUHJlcGFyZSBhIHJlYWwsIHBpbm5lZCBDRkIgR2l0IHdvcmt0cmVlIGJlZm9yZSByZXNlYXJj
aDsgbmV2ZXIgcHVibGlzaCBvciB3cml0ZSBiYWNrLiIiIgppbXBvcnQgYXJncGFyc2UKaW1wb3J0
IGpzb24KaW1wb3J0IG9zCmltcG9ydCByZQppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgc3lzCmZy
b20gcGF0aGxpYiBpbXBvcnQgUGF0aAoKUkVQT1NJVE9SWSA9ICdodHRwczovL2dpdGh1Yi5jb20v
bXVuY2hpZTUwL2NmYi1hY3F1aXNpdGlvbi1icmlkZ2UuZ2l0JwpSRVFVSVJFRCA9ICgnY2ZiX3dl
ZWs5X3B1YmxpY2F0aW9uLnB5JywgJ2NmYl9ob3Rfc2hlZXRfcmVhZGluZXNzLnB5JywKICAgICAg
ICAgICAgJ2NmYl9uZXV0cmFsX3B1YmxpY2F0aW9uX2dhdGUucHknLCAnY2ZiX3JlY292ZXJ5X2Nv
bnN1bWVyX3ByZWZsaWdodC5weScpCgoKZGVmIHByZXBhcmUoZGVzdGluYXRpb24sIGV4cGVjdGVk
X2hlYWQpOgogICAgaWYgbm90IHJlLmZ1bGxtYXRjaChyJ1swLTlhLWZdezQwfScsIGV4cGVjdGVk
X2hlYWQpOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoJ2V4YWN0IGNvbm5lY3Rvci1vYnNlcnZl
ZCBtYWluIGNvbW1pdCByZXF1aXJlZCcpCiAgICBkZXN0aW5hdGlvbiA9IFBhdGgoZGVzdGluYXRp
b24pLnJlc29sdmUoKQogICAgaWYgZGVzdGluYXRpb24uZXhpc3RzKCk6CiAgICAgICAgcmFpc2Ug
VmFsdWVFcnJvcignZGVzdGluYXRpb24gbXVzdCBiZSBuZXc7IG5ldmVyIHJlc2V0IGFuIGV4aXN0
aW5nIHdvcmt0cmVlJykKICAgIGVudiA9IGRpY3Qob3MuZW52aXJvbiwgR0lUX1RFUk1JTkFMX1BS
T01QVD0nMCcsIEdDTV9JTlRFUkFDVElWRT0nbmV2ZXInKQogICAgZGVmIGdpdCgqYXJncyk6CiAg
ICAgICAgcmV0dXJuIHN1YnByb2Nlc3MuY2hlY2tfb3V0cHV0KFsnZ2l0JywgKmFyZ3NdLCBlbnY9
ZW52LCBzdGRlcnI9c3VicHJvY2Vzcy5QSVBFLAogICAgICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICB0aW1lb3V0PTE4MCkuZGVjb2RlKCd1dGYtOCcpLnN0cmlwKCkKICAgICMgQSBu
b3JtYWwgZnVsbCBjbG9uZSBwcmVzZXJ2ZXMgZ2VudWluZSBjb21taXQvdHJlZS9ibG9iIGFuY2Vz
dHJ5LiBObyBncmFmdCwKICAgICMgcmVwbGFjZW1lbnQgb2JqZWN0LCBmb3JnZWQgY29tbWl0LCBz
eW50aGV0aWMgcmVmIG9yIHZhbGlkYXRvciBwYXRjaCBpcyB1c2VkLgogICAgZ2l0KCdjbG9uZScs
ICctLW5vLWNoZWNrb3V0JywgUkVQT1NJVE9SWSwgc3RyKGRlc3RpbmF0aW9uKSkKICAgIGdpdCgn
LUMnLCBzdHIoZGVzdGluYXRpb24pLCAnY2F0LWZpbGUnLCAnLWUnLCBleHBlY3RlZF9oZWFkICsg
J157Y29tbWl0fScpCiAgICBnaXQoJy1DJywgc3RyKGRlc3RpbmF0aW9uKSwgJ21lcmdlLWJhc2Un
LCAnLS1pcy1hbmNlc3RvcicsIGV4cGVjdGVkX2hlYWQsICdvcmlnaW4vbWFpbicpCiAgICBnaXQo
Jy1DJywgc3RyKGRlc3RpbmF0aW9uKSwgJ2NoZWNrb3V0JywgJy0tZGV0YWNoJywgZXhwZWN0ZWRf
aGVhZCkKICAgIGlmIGdpdCgnLUMnLCBzdHIoZGVzdGluYXRpb24pLCAncmV2LXBhcnNlJywgJ0hF
QUQnKSAhPSBleHBlY3RlZF9oZWFkOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoJ2NoZWNrb3V0
IEhFQUQgZGlmZmVycyBmcm9tIGNvbm5lY3RvciBhdXRob3JpdHknKQogICAgaWYgZ2l0KCctQycs
IHN0cihkZXN0aW5hdGlvbiksICdyZXYtcGFyc2UnLCAnLS1pcy1zaGFsbG93LXJlcG9zaXRvcnkn
KSAhPSAnZmFsc2UnOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoJ2Z1bGwgYWNjZXB0ZWQgYW5j
ZXN0cnkgcmVxdWlyZWQnKQogICAgZm9yIG5hbWUgaW4gUkVRVUlSRUQ6CiAgICAgICAgaWYgbm90
IChkZXN0aW5hdGlvbiAvICdzY3JpcHRzJyAvIG5hbWUpLmlzX2ZpbGUoKToKICAgICAgICAgICAg
cmFpc2UgVmFsdWVFcnJvcignbWlzc2luZyBnb3Zlcm5lZCBjb21waWxlcjogJyArIG5hbWUpCiAg
ICBzeXMucGF0aC5pbnNlcnQoMCwgc3RyKGRlc3RpbmF0aW9uIC8gJ3NjcmlwdHMnKSkKICAgIGZy
b20gY2ZiX2NvbmRpdGlvbmFsX3JlY29tbWVuZGF0aW9uX3Byb2ZpbGUgaW1wb3J0IGxvYWRfcmV2
aWV3CiAgICAjIFZlcmlmeSBldmVyeSBpbW11dGFibGUgcmVmIGluIHJldGFpbmVkIGNhbm9uaWNh
bCBoaXN0b3J5LCBpbmNsdWRpbmcgY2xvc2VkCiAgICAjIHJldmlld3M7IHRob3NlIG9iamVjdHMg
cmVtYWluIG5lY2Vzc2FyeSB0byB2YWxpZGF0ZSBsYXRlciB0eXBlZCBwYWNrZXRzLgogICAgcmVm
cyA9IHt9CiAgICBsZWRnZXIgPSBkZXN0aW5hdGlvbiAvICdldmlkZW5jZS9vcGVyYXRpb25hbC9D
RkJfREVDSVNJT05fV0FJVF9MRURHRVIubWQnCiAgICBmb3IgYm9keSBpbiByZS5maW5kYWxsKHIn
XmBgYGNmYi1bXlxuXStcbiguKj8pXmBgYFxzKiQnLCBsZWRnZXIucmVhZF90ZXh0KCksIHJlLk0g
fCByZS5TKToKICAgICAgICBwYWNrZXQgPSBqc29uLmxvYWRzKGJvZHkpCiAgICAgICAgZm9yIHJv
dyBpbiBwYWNrZXQuZ2V0KCdyb3dzJywgW10pOgogICAgICAgICAgICByZWYgPSByb3cuZ2V0KCdy
ZXZpZXdfcmVmJykKICAgICAgICAgICAgaWYgcmVmOgogICAgICAgICAgICAgICAgcmVmc1socmVm
Wydjb21taXQnXSwgcmVmWydwYXRoJ10sIHJlZlsnYmxvYiddKV0gPSByZWYKICAgIGlmIG5vdCBy
ZWZzOgogICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoJ25vIGdvdmVybmVkIGltbXV0YWJsZSByZXZp
ZXcgcmVmcyByZWNvdmVyZWQnKQogICAgdmVyaWZpZWQgPSBbXQogICAgZm9yIHJlZiBpbiByZWZz
LnZhbHVlcygpOgogICAgICAgIF8sIGNvbW1pdHRlZCA9IGxvYWRfcmV2aWV3KHJlZikKICAgICAg
ICB2ZXJpZmllZC5hcHBlbmQoZGljdChyZWYsIGNvbW1pdHRlZF9hdD1jb21taXR0ZWQpKQogICAg
cmV0dXJuIHsnc3RhdHVzJzogJ1NVUFBPUlRFRF9HSVRfUlVOVElNRV9WRVJJRklFRCcsICdyZXBv
c2l0b3J5JzogUkVQT1NJVE9SWSwKICAgICAgICAgICAgJ2hlYWQnOiBleHBlY3RlZF9oZWFkLCAn
d29ya3RyZWUnOiBzdHIoZGVzdGluYXRpb24pLAogICAgICAgICAgICAncHl0aG9uJzogc3lzLnZl
cnNpb24uc3BsaXQoKVswXSwgJ2ltbXV0YWJsZV9yZXZpZXdzJzogdmVyaWZpZWQsCiAgICAgICAg
ICAgICdzY29wZSc6ICdydW50aW1lIGFuZCBhbmNlc3RyeSBvbmx5OyBubyByZXNlYXJjaCwgcHVi
bGljYXRpb24gb3IgcnVuIGFjY2VwdGFuY2UnfQoKCmlmIF9fbmFtZV9fID09ICdfX21haW5fXyc6
CiAgICBwID0gYXJncGFyc2UuQXJndW1lbnRQYXJzZXIoZGVzY3JpcHRpb249X19kb2NfXykKICAg
IHAuYWRkX2FyZ3VtZW50KCctLWRlc3RpbmF0aW9uJywgdHlwZT1QYXRoLCByZXF1aXJlZD1UcnVl
KQogICAgcC5hZGRfYXJndW1lbnQoJy0tZXhwZWN0ZWQtaGVhZCcsIHJlcXVpcmVkPVRydWUpCiAg
ICBhID0gcC5wYXJzZV9hcmdzKCkKICAgIHRyeToKICAgICAgICBwcmludChqc29uLmR1bXBzKHBy
ZXBhcmUoYS5kZXN0aW5hdGlvbiwgYS5leHBlY3RlZF9oZWFkKSwgaW5kZW50PTIpKQogICAgZXhj
ZXB0IChWYWx1ZUVycm9yLCBPU0Vycm9yLCBzdWJwcm9jZXNzLlN1YnByb2Nlc3NFcnJvcikgYXMg
ZXhjOgogICAgICAgIHByaW50KGpzb24uZHVtcHMoeydzdGF0dXMnOiAnQ09NUFVUQVRJT05fUlVO
VElNRV9VTkFWQUlMQUJMRScsCiAgICAgICAgICAgICAgICAgICAgICAgICAgJ2Vycm9yX3R5cGUn
OiB0eXBlKGV4YykuX19uYW1lX18sCiAgICAgICAgICAgICAgICAgICAgICAgICAgJ3Njb3BlJzog
J25vIHB1YmxpY2F0aW9uIGF0dGVtcHRlZDsgcHJlc2VydmUgdGFzayBzY2hlZHVsZXMnfSkpCiAg
ICAgICAgc3lzLmV4aXQoMSkK
CFB_EXACT_HELPER_B64
test "$(wc -c < "$scratch/cfb_runtime_checkout.py")" -eq "$expected_size"
test "$(git hash-object "$scratch/cfb_runtime_checkout.py")" = "$expected_blob"
printf '%s\n' DIRECT_HELPER_BYTES_VERIFIED
"$checkout_python" - "$scratch/cfb_runtime_checkout.py" "$pinned_head" "$scratch/checkout" <<'CFB_CHECKOUT_PY'
import json
import runpy
import subprocess
import sys

def report(stage, error, category, **extra):
    print(json.dumps({
        "status": "COMPUTATION_RUNTIME_UNAVAILABLE",
        "stage": stage,
        "error_type": type(error).__name__,
        "failure_category": category,
        **extra,
    }))
    raise SystemExit(1)

def git_stage(error):
    command = error.cmd
    if not isinstance(command, (list, tuple)) or not command or command[0] != "git":
        return "RETAINED_REVIEW_OR_OTHER_SUBPROCESS"
    verb = command[3] if len(command) > 3 and command[1] == "-C" else command[1]
    return {
        "clone": "GIT_CLONE",
        "cat-file": "PINNED_COMMIT_LOOKUP",
        "merge-base": "PINNED_ANCESTRY",
        "checkout": "DETACHED_CHECKOUT",
        "rev-parse": "HEAD_OR_SHALLOW_CHECK",
        "show": "RETAINED_REVIEW_LOOKUP",
    }.get(verb, "OTHER_GIT_SUBPROCESS")

helper, head, destination = sys.argv[1:]
prepare = runpy.run_path(helper)["prepare"]
try:
    result = prepare(destination, head)
except subprocess.CalledProcessError as error:
    stage = git_stage(error)
    stderr = error.stderr or ""
    if isinstance(stderr, bytes):
        stderr = stderr.decode("utf-8", "replace")
    stderr = stderr.casefold()
    signatures = (
        ("DNS_RESOLUTION", ("could not resolve host", "could not resolve proxy", "temporary failure in name resolution")),
        ("AUTHORIZATION", ("authentication failed", "could not read username", "repository not found", "error: 401", "error: 403", "terminal prompts disabled")),
        ("TLS_VERIFICATION", ("certificate problem", "certificate verify failed", "ssl certificate")),
        ("NETWORK_TIMEOUT", ("timed out", "timeout", "connection reset", "could not connect", "failed to connect")),
        ("MISSING_GIT_OBJECT", ("bad object", "not a valid object", "unknown revision")),
    )
    category = next((name for name, terms in signatures if any(term in stderr for term in terms)), None)
    if category is None:
        category = "PIN_NOT_ANCESTOR" if stage == "PINNED_ANCESTRY" and error.returncode == 1 else "UNCLASSIFIED_GIT_FAILURE"
    report(stage, error, category, exit_code=error.returncode, stderr_present=bool(stderr))
except subprocess.TimeoutExpired as error:
    report(git_stage(error), error, "NETWORK_OR_SUBPROCESS_TIMEOUT")
except (ValueError, OSError) as error:
    report("WORKTREE_OR_RETAINED_REVIEW_VALIDATION", error, "VALIDATION_OR_LOCAL_RUNTIME")

print(json.dumps(result))
CFB_CHECKOUT_PY
```

STARTUP REVISION CFB_MONITOR_LIVE_CONNECTOR_SHELL_20261119. After independent RUN_STARTED readback, run the production checkout below as a single connector-to-shell cell. This is the live startup path on every occurrence. Record actual stage results and poll any returned shell session to completion. Use the resulting verified current-main worktree for the existing live Monitor workload and publication gates.

```javascript
const repository_full_name = "munchie50/cfb-acquisition-bridge";
const tip = await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/" + repository_full_name + "/branches/main"});
if (tip.isError || !tip.structuredContent?.content) throw Error("MAIN_CONNECTOR_READ_FAILED");
const pin = JSON.parse(tip.structuredContent.content).commit?.sha;
if (!/^[0-9a-f]{40}$/.test(pin || "")) throw Error("MAIN_PIN_INVALID");
const helper = await tools.mcp__codex_apps__github_fetch_file({repository_full_name,path:"scripts/cfb_runtime_checkout.py",ref:pin});
const file = helper.structuredContent;
if (helper.isError || !/^[0-9a-f]{40}$/.test(file?.sha || "") || typeof file?.content !== "string" || !file.content.length) throw Error("PINNED_HELPER_CONNECTOR_READ_FAILED");
const shell = "set -eu\npinned_head='PINNED_MAIN_SHA'\ncase \"$pinned_head\" in ''|*[!0-9a-f]*) exit 2;; esac\ntest \"${#pinned_head}\" -eq 40\nif command -v python3 >/dev/null 2>&1; then\n  checkout_python=python3\nelse\n  checkout_python=python\nfi\n\"$checkout_python\" --version\ngit --version\nprintf '%s\\n' SHELL_PROBE_PASS\numask 077\nscratch=$(mktemp -d)\nprintf '%s' HELPER_LITERAL > \"$scratch/cfb_runtime_checkout.py\"\ntest \"$(wc -c < \"$scratch/cfb_runtime_checkout.py\")\" -eq \"$expected_size\"\ntest \"$(git hash-object \"$scratch/cfb_runtime_checkout.py\")\" = \"$expected_blob\"\nprintf '%s\\n' CONNECTOR_HELPER_VERIFIED\n\"$checkout_python\" - \"$scratch/cfb_runtime_checkout.py\" \"$pinned_head\" \"$scratch/checkout\" <<'CFB_CHECKOUT_PY'\nimport json\nimport runpy\nimport subprocess\nimport sys\n\ndef report(stage, error, category, **extra):\n    print(json.dumps({\n        \"status\": \"COMPUTATION_RUNTIME_UNAVAILABLE\",\n        \"stage\": stage,\n        \"error_type\": type(error).__name__,\n        \"failure_category\": category,\n        **extra,\n    }))\n    raise SystemExit(1)\n\ndef git_stage(error):\n    command = error.cmd\n    if not isinstance(command, (list, tuple)) or not command or command[0] != \"git\":\n        return \"RETAINED_REVIEW_OR_OTHER_SUBPROCESS\"\n    verb = command[3] if len(command) > 3 and command[1] == \"-C\" else command[1]\n    return {\n        \"clone\": \"GIT_CLONE\",\n        \"cat-file\": \"PINNED_COMMIT_LOOKUP\",\n        \"merge-base\": \"PINNED_ANCESTRY\",\n        \"checkout\": \"DETACHED_CHECKOUT\",\n        \"rev-parse\": \"HEAD_OR_SHALLOW_CHECK\",\n        \"show\": \"RETAINED_REVIEW_LOOKUP\",\n    }.get(verb, \"OTHER_GIT_SUBPROCESS\")\n\nhelper, head, destination = sys.argv[1:]\nprepare = runpy.run_path(helper)[\"prepare\"]\ntry:\n    result = prepare(destination, head)\nexcept subprocess.CalledProcessError as error:\n    stage = git_stage(error)\n    stderr = error.stderr or \"\"\n    if isinstance(stderr, bytes):\n        stderr = stderr.decode(\"utf-8\", \"replace\")\n    stderr = stderr.casefold()\n    signatures = (\n        (\"DNS_RESOLUTION\", (\"could not resolve host\", \"could not resolve proxy\", \"temporary failure in name resolution\")),\n        (\"AUTHORIZATION\", (\"authentication failed\", \"could not read username\", \"repository not found\", \"error: 401\", \"error: 403\", \"terminal prompts disabled\")),\n        (\"TLS_VERIFICATION\", (\"certificate problem\", \"certificate verify failed\", \"ssl certificate\")),\n        (\"NETWORK_TIMEOUT\", (\"timed out\", \"timeout\", \"connection reset\", \"could not connect\", \"failed to connect\")),\n        (\"MISSING_GIT_OBJECT\", (\"bad object\", \"not a valid object\", \"unknown revision\")),\n    )\n    category = next((name for name, terms in signatures if any(term in stderr for term in terms)), None)\n    if category is None:\n        category = \"PIN_NOT_ANCESTOR\" if stage == \"PINNED_ANCESTRY\" and error.returncode == 1 else \"UNCLASSIFIED_GIT_FAILURE\"\n    report(stage, error, category, exit_code=error.returncode, stderr_present=bool(stderr))\nexcept subprocess.TimeoutExpired as error:\n    report(git_stage(error), error, \"NETWORK_OR_SUBPROCESS_TIMEOUT\")\nexcept (ValueError, OSError) as error:\n    report(\"WORKTREE_OR_RETAINED_REVIEW_VALIDATION\", error, \"VALIDATION_OR_LOCAL_RUNTIME\")\n\nprint(json.dumps(result))\nCFB_CHECKOUT_PY";
const make = (pin,sha,body) =>{const q=s=>"'"+s.replaceAll("'","'\\''")+"'";return "expected_size="+unescape(encodeURIComponent(body)).length+"\nexpected_blob="+sha+"\n"+shell.replace("PINNED_MAIN_SHA",pin).replace("HELPER_LITERAL",()=>q(body))};
text(await tools.exec_command({cmd:make(pin,file.sha,file.content),yield_time_ms:10000,max_output_tokens:600}));
```

PRODUCTION ADOPTION — VERIFIED NOVEMBER 18 SCHEDULED REHEARSAL. Evidence: evidence/scheduler_qa/CFB_REHEARSAL_20261118T234623606Z_unknown_RESULT.json at 1b50347cbeb375a87dfa808334dd8fa988af8f6b; closure evidence/scheduler_qa/CFB_REHEARSAL_20261118T234623606Z_unknown_CLOSURE.json at 8c5f27f5b849c3416075b270da245a2fbfff94db. Use the verified connector-to-shell checkout above and the following live source and publication procedure.

For fresh CBS acquisition, use the existing permitted complete-board retrieval. When HTML needs table serialization in the verified runtime, use the available lxml parser and preserve headers, directed team links, all five other columns, and per-cell opaque book icons. Read both th and td cells; use the unchanged identity normalizer to verify completeness against the current accepted population, including two directed team rows per game. Record the raw response SHA-256, byte count, recovery clock, and normalized coverage; persist the exact source capture and independently read it back before binding it to governed proposals. A retrieval clock is not an offer-update clock. Preserve the mixed-book classification. Treat an unavailable or interstitial body as source unavailable even if HTTP returns 200. Continue with other qualified evidence; missing venue confirmation alone does not prevent an analytically supported recommendation.

Use fresh production inputs and the actual run clock. Start with the earliest open decision deadlines and review both spreads, both moneylines, and both totals. Do not carry rehearsal decisions forward as fresh production evidence. Run the current-week compiler and renderer against private proposals, preserve accepted history and production validation, and use the existing sole-publisher path, serialized writes, and independent readback for eligible full or partial publication. Clearly identify freshly reviewed games, carried-forward context, material gaps, and venue status. A partial publication requires the existing incomplete closure rather than RUN_PASS. The rehearsal demonstrated checkout, full CBS capture, focused review, and compiler/render; it did not verify named prices, full live review, or canonical publication.

PRIORITIZE LIVE DECISIONS. As soon as current authority and usable sources are recovered, work in practical decision-deadline order, beginning with Thursday's open games. Complete supported six-market judgments and advance validated partial publication as soon as the existing gates permit. Give the user any supported recommendation with an acceptable line and price, expiry, and separate venue status. If checkout fails, use the existing recovery handoff, continue independent live review, and durably save and read back supported time-sensitive decisions for continuation. Preserve canonical publication gates and report the exact closure status.

AUTHORITY AND COMMAND AUDIT: Fresh-read newest accepted CFB_ENGINE_CURRENT_RECOVERY_INDEX_v*.md, active contracts/controls and exact accepted current-state surfaces. Read evidence/operational/CFB_MARKET_MONITOR_TASK_PROMPT_BACKUP_20261030.md (verbatim original instructions) and obey all operative requirements unless superseded by later accepted repository authority. Before each command/tool action, verify its purpose, correct repository/branch/path, required arguments, available permissions, source qualification, dependency order, expected output, risk, and a falsifiable acceptance check. Do not assume commands ran because they were requested; verify tool response and independent readback. Avoid redundant reads, expensive calls, speculative commands, unauthorized mutations or unsupported tools. Apply established routine: fresh-read → smallest valid delta → write → independent readback → validate → accepted closure. Use independent runners only for truly independent work; serialize authoritative writes.



Trace connector retrieval, shell transfer and integrity, then Git clone independently. On source delivery failure use the accepted immutable REST blob fallback once with proxy-aware defaults and the same pinned byte and blob verification. On actual checkout failure, record the exact failed operation and do not retry equivalent transfers. Preserve default proxy and Git settings. Require SUPPORTED_GIT_RUNTIME_VERIFIED, exact HEAD, nonshallow ancestry, validated retained reviews, matched recovery index and current producer prerequisites. Continue live Monitor work immediately on success.

On exhausted startup failure, preserve the exact first operation/error, which fallback ran and its result, and the last verified stage. If GitHub connector writes are available and the pin and both inputs are verified, create one append-only recovery request at evidence/run_receipts/CFB_MARKET_MONITOR_RUNTIME_HANDOFF_<UTC>_<CORRELATION_ID>.json. Include schema CFB_MONITOR_WORK_MODE_RUNTIME_RECOVERY_v1, observed UTC, observed invocation ID if exposed, correlation ID, repository, branch, pinned_head, inputs (path and full blob for helper and index), helper_bytes, producer, startup receipt pointer, exact sanitized first failure, fallback outcome, and scope=WORK_MODE_RUNTIME_RECOVERY_ONLY. Independently read back the complete exact request at its resulting commit. Link path, commit and blob in the terminal candidate and user-facing result. Reuse only an exact matching existing request on retry. If inputs or persistence fail, report that distinct boundary in the normal closure. A recovery request enables direct Work Mode checkout and does not itself start it or authorize publication. Preserve all existing source, compilation, sole-publisher, independent partial work and two-phase closure rules. A blocked runtime cannot earn RUN_PASS. Never launch another task or Actions as a bypass.

Use the existing structured stage trace. Keep the applicable current profile, actual clocks and distinct scratch input/output paths. Preserve prior canonical bytes, original lineage, immutable decision origins, practical cutoffs and valid price limits.

COMPLETE THE LIVE WORKLOAD: after startup/readback recover current authority and unfinished canonical work. Use the real supported runtime and current-week producer, genuine fresh sources and actual current six-market judgment. Source capture, a previous PASS, a retained fixture, runtime readiness and a status report are not completed current production. Proceed to actual caller-authored rows, valid compiler proposals, full render, serialized canonical writes, current recovery integration, selected existing CI and two-phase closure whenever supported. Preserve the primary Monitor's sole live publication ownership. Do not stop merely because full-slate RUN_PASS is not yet earned: publish independently validated honest partial progress where existing authority permits, naming exact unfinished identities.

FAIL ONLY THE AFFECTED STAGE: record each required stage as executed/pass, failed, blocked or not-yet-executed with exact evidence and next action. On one unavailable source, player report, quote or failed game review, continue independent games/markets with practical windows, including justified prospective reconsideration of PASS. On compute/DNS failure, apply the existing bounded recovery clause; API recovery is not compiler execution. Complete independent permitted research and persistence instead of stopping the entire invocation. Never fabricate acceptance or bypass restrictions. Preserve resume-safe partial decisions/research and their source bindings before the platform boundary; later continuation starts from exact last proved outputs rather than repeating accepted work.

TIMING: preserve actual first worker clock, scheduled clock and exact invocation/result association. Small early/late variation alone is diagnostic, not an automatic RUN_INCOMPLETE condition. Assess actual input availability, deadlines and practical usefulness; genuine missed/expired windows stay explicit and cannot be relaxed. Do not wait to conceal early startup or compensate the recurrence using guessed offsets.

REPLAY/LIVE SEPARATION: qa/cfb_monitor_execution_smoke.py is a proved diagnostic against authentic HISTORICAL fixture clocks; it is NOT a substitute for current football research, new production decisions, live compiler inputs or current publication. Do not make it a mandatory repeated preflight or rerun already-green test suites at the expense of due live work. Use only if a new concrete compiler/runtime contradiction needs bounded diagnosis. A test PASS never qualifies current market offers, guarantees recurring reliability or authorizes wagers.

FINISH: close every feasible independent stage; save/read back exact partial outputs and blockers even when another required stage fails. RUN_PASS still requires all current production obligations, actual saved publication/current-navigation integration and independent terminal proof. Otherwise truthful RUN_INCOMPLETE/RUN_FAIL with successful components and exact next work. No new tasks, self-reschedule, run_now, other-task changes, historical status upgrades, Champion/model changes, wagers or money movements. Preserve the existing daily07/13 America/Chicago schedule.

Use the compiler for the current qualified slate, as bound by the accepted repository profile and original lineage. Resolve the producer for the current week from recovered authority and verify its presence in the pinned worktree. Older week-specific compiler instructions are historical.
USER-DIRECTED NOVEMBER7 SOURCE CORRECTION: Remove the mandatory ESPN summary API attempt. Do not call site.api.espn.com as part of this production Monitor's acquisition path. Acquire the current CBS full board through the existing permitted route and unchanged exact-identity normalizer; preserve actual retrieval clocks and raw source provenance. CBS display remains its honestly qualified mixed-book fallback class, not consensus or executable sportsbook proof. Continue current material/price analysis and supported decision/publication work from usable CBS evidence; absence of an ESPN API response is not a blocker. Independently required kickoff, material, review and market qualifications remain in force and must come from other already permitted qualified evidence; do not fabricate or weaken them. Name any specific unmet field rather than globally terminate. Preserve old ESPN profiles/reviews as historical provenance only; do not rewrite existing records.
Unknown offer_updated_at remains null: this permitted single-book retrieval-only benchmark is NOT consensus, current executable venue proof or an invented book-update clock. Older aggregator displays must not be asserted newer solely because retrieved later. Preserve conflicts and observation/unknown update clocks explicitly.
Separate ANALYTICAL RECOMMENDATION from VENUE EXECUTION. Missing executable sportsbook/Caesars confirmation alone does not block a genuinely earned controlled-Beta CONDITIONAL recommendation or analytical publication through the existing supported route. Require independently earned model/material/market judgment, immutable review, original line/price limits and final cutoff; never invent a recommendation to fit schema. Venue confirmation stays pending and no wager is inferred.
Proceed beyond source capture: author actual current six-market decision rows using recovered manual recipe, execute producer/gates, serialize supported market/decision/sole Hot Sheet/audit/recovery integration and two-phase closure. A remaining full-slate gap prevents full RUN_PASS, but is not by itself a ban on an otherwise validated honest partial working publication under current authority.
Unavailable final reports do not universally require perfect certainty. Record the specific material uncertainty and its effect; if a game is genuinely blocked, continue independent Thursday/Friday/Saturday cases with open practical windows. Do not terminate the entire invocation with only a report when independent authorized production work remains executable. Persist resume-safe partial progress at platform limits.
For previously issued conditions preserve exact original limits and final cutoffs. Reconciliation time and final expiry are different fields; a source-only recheck is not a complete material review or automatic renewal. Follow existing immutable-review renewal path only when genuine new review earns it. No task scheduling/lifecycle, Champion, wager or money changes.

RECOVERY READ FALLBACK (VERIFIED): Discover exact path, blob SHA and nonzero size from fresh main Git tree. If GitHub fetch_file returns empty for a nonempty file, do not classify it missing or repeat the same failing call. Use the connected GitHub dedicated fetch_blob operation with the exact blob SHA from the pinned main tree and independently verify the complete content by recomputing the UTF-8 byte count and Git blob SHA-1 against that same tree entry. Use standard hashing or same-cell connector orchestration without printing raw content or passing large bodies as shell arguments. Use direct REST only as an available bounded fallback; report unavailable verification without weakening the existing gate. This was demonstrated for recovery index v1.245 (~4.23 MB), and prior October 30 market/decision large blobs. If fallback fails, log precise first error and fail closed. Never truncate authoritative input or silently replace current index with older small index.

DECISION PRODUCER GATE (VERIFIED): The applicable current-week compiler consumes caller-authored decision_rows; a historical replay or source capture does not author current decisions. Recover last-good manual authoring recipe and current Champion/source/venue/material evidence. For every prospective game explicitly record six-market qualitative disposition and certification, or exact evidence-constrained WAIT; no inherited stale 56-row/35-case packet represented as current. Do not run publication until current authenticated rows and required packet certifications exist. Distinguish scheduled startup acceptance from producer and publication acceptance.

PRODUCTION: Execute governed CFB Market Monitor across full relevant FBS slate, both spread sides, both moneylines, totals, qualified alternates and bounded parlay review. Preserve FIRST_FROZEN Champion, original price/number limits and cutoffs, prior PASS reassessment on changed market/news, venue/source clocks, ticket/execution separation, 1–2 trip preference and accepted science/risk controls. Do not invent quotes, EV, kickoffs, picks or prices. Rank up to TOP 10 earned opportunities without quota. Respect current local time and expiration; expired historical Week9 reviews are not automatically actionable.

PUBLISH AND CLOSE: Use verified runtime/worktree and applicable current compiler, validator and integration gates. Serialize market → decision → sole Hot Sheet → audit → recovery-index mutations with SHA-guarded updates and independent readback. Publish only fully supported decisions. Record per-stage trace. For every terminal outcome, including missing runtime, first persist a distinct TERMINAL_CANDIDATE with exact executed/blocked/not-executed stages and independently fetch its complete bytes/blob. Only then create the separate RUN_CLOSURE referencing that exact candidate path/blob and the completed readback. A startup trace plus a file named RUN_CLOSURE is not the two-phase protocol. If either write/readback fails, use the existing TERMINAL_PERSISTENCE_UNAVAILABLE envelope without self-certification. RUN_PASS only with accepted current Hot Sheet, complete slate reconciliation, preserved frozen invariants, selected CI and readback. Otherwise preserve previous accepted publication and close RUN_INCOMPLETE/RUN_FAIL with exact blocker and next safe action. Do not change other automations, task schedules, Champion, models, wagers or money; do not create a fifth concurrent production task.

ANTI-DRIFT CURRENT EXECUTION ORDER — November7 reconciliation: At each continuation recover newest accepted recovery frontier, current canonical decisions and original FIRST_FROZEN lineage. Read evidence/operational/CFB_ACCEPTED_PREDICTION_SOURCE_STATE.json; read its live accepted boundary and preserve its independently verified acceptance rule. Weekly REFRESH is separate from the current slate’s original FIRST_FROZEN lineage and execution authority. November2/3 workflow readiness and Ohio–Akron/Buffalo–Miami pregame priorities are HISTORICAL and must not delay current remaining-window work or revive elapsed games. Reconcile later source acceptance only when independently supported; do not rerun already-accepted weekly work merely because its historical instructions remain in backup. Select current prospective cases using actual kickoff/cutoff and reassess material/price changes before reusing PASS. Preserve elapsed decisions and exact issued limits.

EXACT WEEKLY MODEL ACCEPTANCE HANDOFF: Tuesday candidate workflow is .github/workflows/cfb_weekly_tuesday_candidate_freeze.yml, output cfb-weekly-tuesday-candidate-boundary. A successful workflow or candidate manifest remains NOT_ACCEPTED. For qualified new S0, recover exact artifact/raw/fit bytes, independently execute the unchanged scripts/cfb_qa_weekly_refresh_acceptance.py with four arguments (S0 output directory, raw source directory, frozen fit directory, audit output directory); require PASS_WEEKLY_REFRESH_ACCEPTANCE, reproducible raw/output SHA, immutable cutoff and independent readback before considering an accepted prediction-source pointer update. Do not update accepted state from workflow success alone. On Monday verify cfb-weekly-monday-source-readiness artifact manifest and raw hashes first. If no natural run yet, state WAIT_FOR_SCHEDULED_TRIGGER, not failure; proceed with independent source readiness checks only.


STRUCTURED FAILURE TRACE (2026-11-02): On each run, in addition to the existing append-only startup/stage/closure evidence, emit stage-level diagnostic fields timestamp_utc, correlation_id, stage, outcome, failure_category, sanitized_error_excerpt, fallback_attempted, fallback_result, and required_for_this_invocation. Use the read-only repository classifier qa/cfb_runtime_failure_trace_readonly.py when an authenticated execution runtime is available; otherwise apply its exact classification categories manually and mark classifier_execution=NOT_RUN. Distinguish DNS_RESOLUTION from CONNECTOR, GIT_ANCESTRY, MISSING_INPUT, COMPILER, PUBLICATION and NETWORK_TIMEOUT; never store secrets or full environment. Link each failed stage to exact next corrective action. Retain separately due-run completion and future-week readiness. Do not claim this classifier ran merely because the file exists. Do not modify scientific acceptance or publication gates.

CFB DATA GAP FOLLOW-THROUGH — Apply evidence/operational/CFB_DATA_GAP_FOLLOW_THROUGH_20261113.md in this existing run. Bind the exact delivered card and quote evidence, keep Nebraska visible, and name each still-open game, deadline and next owner in closure. Verify the durable receipt before closure.

PRE-TRIP PARLAY RESEARCH: Apply the scheduled M3 section of evidence/plans/CFB_INTEGRATED_BETTING_INTELLIGENCE_ROADMAP_20261111.md. Freeze actual research rank depth (target 30 supported distinct games) and straight-card overlap. For shortlisted 3–5-leg builds, retain exact authentic combined quotes, clocks or explicit gaps. Publish only under existing Hot Sheet authority and keep normal straight-card delivery moving.

FRIDAY NOVEMBER 20 07:00 CT EXECUTION PRIORITY — USER-DIRECTED: This is the live Saturday-slate completion run, not a gate-only rehearsal. After any successful startup, shell, exact-byte helper, checkout, ancestry, or producer gate, immediately execute the next dependent production stage within this SAME invocation; never terminate merely to report a passed gate or ask for permission to proceed. Continue through current CBS acquisition, all Saturday game/six-market reviews, decision-row authoring, current-week compiler, authorized partial/full Hot Sheet publication, independent readback, and two-phase closure. Prioritize delivery before Friday 13:00 CT. On a localized failure, preserve exact evidence, continue every independent permitted game/market and persist verified partial outputs; do not represent a gate PASS as RUN_PASS. If the runtime or a mandatory integrity gate cannot be passed, fail closed only for dependent stages, report the exact boundary, and complete all independent authorized work. Preserve existing authority, risk, deadlines, and four-task limit. This paragraph clarifies execution continuation; it does not relax any gate or authorize invented evidence.

OCTOBER 29 VERIFIED PRODUCTION PATH — RESTORATION PRIORITY (2026-11-19). The October 29 natural scheduled Market Monitor completed real authenticated Git checkout, immutable review ancestry, CBS acquisition, governed compiler/publication, independent readback and two-phase closure. Treat that prior working execution route as the preferred recovery reference, NOT a reason to roll back current governance or assume the current runtime exposes the same tools. At startup, after durable RUN_STARTED and fresh authority, inspect actual available execution tools and recover the Oct 29 run's exact tool/runtime invocation and authoritative receipt if accessible. If its supported authenticated checkout path is exposed, invoke that path directly with the fresh connector-observed main pin and existing governed helper, verify HEAD/full ancestry/required scripts and immutable reviews, then CONTINUE IN THE SAME RUN through live CBS collection, every Saturday game and six-market review, decision rows, current-week compiler, authorized Hot Sheet publication, independent readback and two-phase closure. Do not stop at a bridge/checkout PASS; only full verified outputs justify RUN_PASS. If the Oct 29 route is not actually exposed, do not simulate it or treat historical success as current proof: use existing direct-shell/combined/fallback routing with bounded diagnostics; on a blocked dependent gate, perform all independent authorized work and persist exact terminal/closure evidence. Do not use GitHub Actions scheduled timing as an assumed solution. Preserve the Friday 13:00 CT Saturday-slate deadline, four-task limit, current authority and all fail-closed integrity gates. This is a runtime routing instruction, not proof of restored execution capability.
<!-- ORIGINAL PROMPT END -->
