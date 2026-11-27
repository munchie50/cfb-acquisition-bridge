"""Measure an unchanged production regression inventory; no production edits."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time

GROUPS = {
    'week8': ['test_cfb_week8_publication.py', 'test_cfb_week8_closed_conditional.py'],
    'week9': ['test_cfb_week9*.py'],
    'frozen': ['test_cfb_week7_accepted_s0_ancestry_audit.py',
               'test_cfb_week7_first_frozen_projection_gate.py',
               'test_cfb_week7_frozen_field_invariant.py', 'test_cfb_accepted_refresh_field_adapter.py'],
    'presentation': ['test_cfb_week7_opening_display_gate.py', 'test_cfb_week7_afternoon_display_gate.py']}
WORKFLOW = '.github/workflows/cfb_qa_hot_sheet_kickoff_section_static_gate.yml'


def inventory(text):
    match = re.search(r'- name: Exercise original Week7 lineage and no-substitution boundaries\n(.*?)- name:', text, re.S)
    if not match: raise ValueError('original regression stage absent')
    patterns = []
    for line in re.findall(r'python -m unittest discover -s scripts -p ([^\n]+)', match[1]):
        parts = shlex.split(line)
        if len(parts) != 1: raise ValueError('unsupported regression invocation')
        patterns.append(parts[0])
    expected = sum(GROUPS.values(), [])
    if patterns != expected or len(set(patterns)) != len(patterns):
        raise ValueError('benchmark groups differ from original checks; qualify new inventory')
    return patterns


def now():
    return datetime.now(timezone.utc).isoformat()


def measure(group, output):
    root = Path(__file__).resolve().parents[1]
    original = inventory((root/WORKFLOW).read_text())
    patterns = original if group == 'serial' else GROUPS[group]
    protected = list((root/'scripts').glob('*.py')) + [root/WORKFLOW,
        root/'evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md']
    protected += [root/'evidence/operational'/n for n in ('CFB_MARKET_MONITOR_STATE.md',
        'CFB_DECISION_WAIT_LEDGER.md', 'CFB_EXECUTION_LEDGER.md', 'CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md')]
    hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in protected}
    bound = hashlib.sha256(json.dumps(hashes,sort_keys=True).encode()).hexdigest()
    output = Path(output); output.mkdir(parents=True, exist_ok=True)
    result = {'schema':'CFB_VALIDATION_TIMING_GROUP_V1','group':group,'started_at_utc':now(),
              'commit':subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True).strip(),
              'protected_inputs_sha256':bound,'original_inventory':original,'runs':[],'status':'INCOMPLETE'}
    start=time.monotonic()
    for number, pattern in enumerate(patterns):
        began=time.monotonic()
        run=subprocess.run([sys.executable,'-m','unittest','discover','-s','scripts','-p',pattern],
                           cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (output/(group+'-'+str(number)+'.log')).write_text(run.stdout)
        print(run.stdout,flush=True)
        counts=re.findall(r'Ran (\d+) tests? in ',run.stdout)
        entry={'pattern':pattern,'returncode':run.returncode,'elapsed_seconds':time.monotonic()-began,
               'tests':int(counts[-1]) if len(counts)==1 else None,
               'skipped':sum(int(n) for n in re.findall(r'OK \(skipped=(\d+)\)',run.stdout))}
        result['runs'].append(entry)
        if run.returncode or entry['tests'] is None or entry['tests']==0:
            break
    result.update(ended_at_utc=now(),elapsed_seconds=time.monotonic()-start)
    if len(result['runs'])==len(patterns) and all(r['returncode']==0 and r['tests'] for r in result['runs']):
        result['status']='PASS_UNCHANGED_REGRESSION_GROUP_ONLY'
    (output/(group+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    return result


def compare(results):
    names=[r['group'] for r in results]
    if set(names) != set(GROUPS)|{'serial'} or len(names)!=len(set(names)):
        raise ValueError('missing or duplicate timing groups')
    if any(r['status']!='PASS_UNCHANGED_REGRESSION_GROUP_ONLY' for r in results):
        raise ValueError('unfinished or failed regression group')
    if len({r['commit'] for r in results})!=1 or len({r['protected_inputs_sha256'] for r in results})!=1:
        raise ValueError('comparisons must use the same exact commit and protected inputs')
    serial=next(r for r in results if r['group']=='serial')
    parallel=[r for r in results if r['group']!='serial']
    def signatures(rows):
        tuples=[(s['pattern'],s['tests'],s['skipped'],s['returncode']) for r in rows for s in r['runs']]
        if len(tuples)!=len({t[0] for t in tuples}): raise ValueError('duplicate regression pattern')
        return sorted(tuples)
    if signatures([serial])!=signatures(parallel):
        raise ValueError('parallel inventory/test counts differ from serial baseline')
    if [r['pattern'] for r in serial['runs']] != serial['original_inventory']:
        raise ValueError('serial baseline omitted original checks')
    span=(max(datetime.fromisoformat(r['ended_at_utc']) for r in parallel)-
          min(datetime.fromisoformat(r['started_at_utc']) for r in parallel)).total_seconds()
    if span<=0: raise ValueError('invalid parallel timing span')
    return {'schema':'CFB_VALIDATION_PARALLEL_COMPARISON_V1','recorded_at_utc':now(),
            'status':'PASS_IDENTICAL_REGRESSION_INVENTORY_ONLY', 'commit':serial['commit'],
            'protected_inputs_sha256':serial['protected_inputs_sha256'],
            'patterns':len(serial['runs']), 'tests':sum(r['tests'] for r in serial['runs']),
            'skipped_tests':sum(r['skipped'] for r in serial['runs']),
            'serial_test_seconds':serial['elapsed_seconds'],'parallel_test_span_seconds':span,
            'parallel_sum_test_seconds':sum(r['elapsed_seconds'] for r in parallel),
            'observed_stage_seconds_saved':serial['elapsed_seconds']-span,
            'limits':['One paired QA measurement; includes runner/network variation and excludes setup/artifact/summary overhead.',
                'Only the original nine-pattern stage is tested here; the complete45step production workflow is unchanged.',
                'No claim of whole-Monitor savings, source freshness, football truth or production acceptance.']}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode',choices=['measure','compare'])
    p.add_argument('--group',choices=['serial',*GROUPS])
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--results',type=Path)
    a=p.parse_args()
    if a.mode=='measure':
        if not a.group:p.error('measure requires group')
        r=measure(a.group,a.output)
    else:
        if not a.results:p.error('compare requires results')
        r=compare([json.loads(p.read_text()) for p in a.results.rglob('*.json')])
        a.output.mkdir(parents=True,exist_ok=True)
        (a.output/'comparison.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r,indent=2))
    raise SystemExit(0 if r['status'].startswith('PASS_') else 2)
