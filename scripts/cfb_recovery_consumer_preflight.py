"""Read-only recovery pointer preflight for the currently qualified CFB consumers.

Run on a complete proposed index before writing it. Hash bindings do not certify
source freshness, betting decisions, model acceptance or operational completion.
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from cfb_recovery_navigation_reader import read
from cfb_hot_sheet_current_decision_binding_gate import publication, blob, LEDGER
from cfb_money_ledger_guard import binding, PATH as MONEY
from cfb_weekly_carry_forward_gate import bind, R2

LINEAGE = 'evidence/operational/CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json'
HEALTH = 'evidence/scheduler_qa/CFB_DUAL_ENGINE_HEALTH_20261011T215456Z_AUDIT.md'
OPERATIONAL = ('CFB_MARKET_MONITOR_STATE.md', 'CFB_DECISION_WAIT_LEDGER.md',
               'CFB_EXECUTION_LEDGER.md', 'CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md')


def audit(index, loader, as_of):
    pointers = read(index, as_of)['frontier']['pointers']
    by_path = {p['path']: p for p in pointers}
    required = [MONEY, R2, LINEAGE, HEALTH] + ['evidence/operational/' + n for n in OPERATIONAL]
    missing = sorted(set(required) - by_path.keys())
    if missing:
        raise ValueError('missing consumer dependencies: ' + ', '.join(missing))
    for p in pointers:
        if blob(loader(p['path'])) != p['blob']:
            raise ValueError('stale recovery pointer: ' + p['path'])
    binding(index, loader(MONEY), as_of)
    bind(index, loader(R2), loader(LINEAGE), loader(HEALTH), as_of)
    current = publication(index, loader(LEDGER), loader, as_of)
    return {'verdict': 'PASS_CURRENT_RECOVERY_CONSUMER_BINDINGS_ONLY',
            'verified_pointers': len(pointers), 'sheet_path': current['sheet_path'],
            'index_blob': blob(index),
            'scope': 'qualified money/weekly/current-publication navigation bindings; not semantic or operational acceptance'}


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--index', type=Path, required=True)
    p.add_argument('--repository-root', type=Path, default=Path('.'))
    p.add_argument('--as-of', default=None)
    a = p.parse_args()
    root = a.repository_root.resolve()
    def loader(path):
        target = (root / path).resolve()
        if not target.is_relative_to(root):
            raise ValueError('pointer escapes repository')
        return target.read_bytes().decode('utf-8')
    print(json.dumps(audit(a.index.read_text(), loader,
                          a.as_of or datetime.now(timezone.utc).isoformat()), indent=2))
