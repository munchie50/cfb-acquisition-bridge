"""Execute the unchanged Monitor compiler on authentic retained inputs, in scratch.

This is a repeatable execution test, never a fresh market review or publisher.
"""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import cfb_neutral_publication_gate as gate
import cfb_week10_publication as producer
import cfb_week10_frozen_field_invariant as frozen

FIXTURE = {
    'cycle': 'CFB_MARKET_MONITOR_20261105T012111Z',
    'publication_utc': '2026-11-05T01:48:11.126910+00:00',
    'source_utc': '2026-11-05T01:40:33.495311+00:00',
    'prior_market': '841ec2f36afea32f290ca4d383e2a9b78e33d4b0',
    'prior_decision': '0c389170f46c3bb373e6961a4f55416476f760e5',
    'market': '87c455f1451b26587ac30489562285c0cfe0c9f5',
    'decision': '822bccb7370a5dfbe22c1994bdf525457d17066e',
    'sheet': '10d642137570317017934b8b1b85f8c0345f1f61',
    'execution': 'f6c3147100e21a4ea97dff8423fd70f06c45123c',
    'scorecard': '65d212f05e56ab7bd89244c9f4bccff4763c0077',
    'capture_path': 'evidence/operational/CFB_CBS_WEEK10_TABLE_CAPTURE_20261105T014033Z.md',
    'capture_blob': '48484afff21eda509a80bf26bd90b6c7c68df54f',
    'lineage_path': 'evidence/scheduler_qa/CFB_WEEK10_ORIGINAL_ANCESTRY_RECOVERY_20261104.json',
    'lineage_blob': '47736c0fd9ff49545db7e46b508805658a1c7a92',
}


def blob(digest):
    value = subprocess.check_output(['git', '-C', str(ROOT), 'cat-file', 'blob', digest], timeout=30).decode()
    if gate.blob(value) != digest:
        raise ValueError('authentic fixture blob mismatch')
    return value


def run(first, output):
    output = output.resolve()
    if output.is_relative_to(ROOT) or output.exists():
        raise ValueError('output must be a new directory outside the repository')
    output.mkdir(parents=True)
    result = {'schema': 'CFB_MONITOR_EXECUTION_SMOKE_V1',
              'observed_start_utc': datetime.now(timezone.utc).isoformat(),
              'head': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip(),
              'fixture': FIXTURE, 'stages': [], 'status': 'TEST_INCOMPLETE',
              'scope': 'Authentic retained compiler/render/frozen-field execution only; no fresh quote, live decision, production acceptance or recurring reliability.'}
    try:
        lineage = blob(FIXTURE['lineage_blob'])
        capture = blob(FIXTURE['capture_blob'])
        saved_decision = blob(FIXTURE['decision'])
        saved = gate.selected_block(saved_decision, producer.DECISION_TAG,
                                    gate.CONDITIONAL_DECISION_SCHEMA, gate.clock(FIXTURE['publication_utc']))
        rows = [{k: v for k, v in row.items() if k not in ('state_recorded_at_utc', 'state_evidence')}
                for row in saved['rows']]
        result['stages'].append({'stage': 'AUTHENTIC_INPUTS', 'outcome': 'PASS', 'games': len(rows)})
        market, decision = producer.compile(blob(FIXTURE['prior_market']), blob(FIXTURE['prior_decision']),
                                           capture, lineage, FIXTURE['cycle'], FIXTURE['publication_utc'],
                                           FIXTURE['source_utc'], rows)
        if gate.blob(market) != FIXTURE['market'] or gate.blob(decision) != FIXTURE['decision']:
            raise ValueError('compiler output differs from authentic accepted fixture')
        (output / 'market.md').write_text(market)
        (output / 'decision.md').write_text(decision)
        result['stages'].append({'stage': 'REAL_COMPILER', 'outcome': 'PASS', 'exact_saved_bytes': True})
        sheet = gate.render(market, decision, blob(FIXTURE['execution']), blob(FIXTURE['scorecard']),
                            lineage, FIXTURE['publication_utc'], 'WEEK10')
        if gate.blob(sheet) != FIXTURE['sheet']:
            raise ValueError('render differs from authentic saved sheet')
        (output / 'sheet.md').write_text(sheet)
        result['stages'].append({'stage': 'REAL_RENDER', 'outcome': 'PASS', 'exact_saved_bytes': True})
        invariant = frozen.audit(sheet, lineage, first)
        result['stages'].append({'stage': 'ORIGINAL_ARCHIVE_INVARIANT', 'outcome': 'PASS', 'evidence': invariant})
        result['status'] = 'PASS_RETAINED_MONITOR_EXECUTION_ONLY'
    except Exception as exc:
        result['stages'].append({'stage': 'FIRST_UNPROVED_BOUNDARY', 'outcome': 'FAIL',
                                 'error_type': type(exc).__name__, 'error': str(exc)[:500]})
    result['observed_end_utc'] = datetime.now(timezone.utc).isoformat()
    (output / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--first', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    result = run(args.first, args.output_dir)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['status'] == 'PASS_RETAINED_MONITOR_EXECUTION_ONLY' else 1)
