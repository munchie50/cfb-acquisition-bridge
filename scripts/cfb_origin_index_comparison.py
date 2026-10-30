"""Same-runner original/candidate QA comparison; never publish operational state."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time
from cfb_validation_timing_qa import inventory, WORKFLOW

GATE = 'scripts/cfb_neutral_publication_gate.py'
BASELINE = 'd4361825d7499f0aace070dbfd092957dc976fc0'


def utc():return datetime.now(timezone.utc).isoformat()


def run_variant(root, label, output, patterns):
    result={'label':label,'started_at_utc':utc(),'runs':[],'status':'INCOMPLETE'}
    env=dict(os.environ,PYTHONPATH=str(root/'scripts'))
    start=time.perf_counter()
    for n,pattern in enumerate(patterns):
        began=time.perf_counter();cpu=resource.getrusage(resource.RUSAGE_CHILDREN)
        p=subprocess.run([sys.executable,'-m','unittest','discover','-s','scripts','-p',pattern],
                         cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        (output/(label+'-'+str(n)+'.log')).write_text(p.stdout)
        print(label,pattern,p.returncode,flush=True)
        counts=re.findall(r'Ran (\d+) tests? in ',p.stdout)
        row={'pattern':pattern,'returncode':p.returncode,'tests':int(counts[0]) if len(counts)==1 else None,
             'skipped':sum(int(x) for x in re.findall(r'OK \(skipped=(\d+)\)',p.stdout)),
             'elapsed_seconds':time.perf_counter()-began,
             'child_cpu_seconds':after.ru_utime+after.ru_stime-cpu.ru_utime-cpu.ru_stime}
        result['runs'].append(row)
        (output/(label+'.json')).write_text(json.dumps(result,indent=2)+'\n')
        if p.returncode or not row['tests']:raise ValueError('regression group failed: '+label+'/'+pattern)
    result.update(ended_at_utc=utc(),elapsed_seconds=time.perf_counter()-start,status='PASS_EXISTING_REGRESSIONS_ONLY')
    (output/(label+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    return result


def compare(baseline, candidate, output):
    baseline=baseline.resolve();candidate=candidate.resolve();output.mkdir(parents=True,exist_ok=True)
    def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args],text=True).strip()
    if git(baseline,'rev-parse','HEAD')!=BASELINE:raise ValueError('wrong original baseline commit')
    paths=git(baseline,'ls-tree','-r','--name-only',BASELINE,'--','scripts','evidence',WORKFLOW).splitlines()
    preserved={}
    for path in paths:
        if path==GATE:continue
        a=(baseline/path).read_bytes();b=(candidate/path).read_bytes()
        if a!=b:raise ValueError('unrelated baseline-tracked input changed: '+path)
        preserved[path]=hashlib.sha256(a).hexdigest()
    gate_hashes={name:hashlib.sha256((root/GATE).read_bytes()).hexdigest() for name,root in
                 [('original',baseline),('candidate',candidate)]}
    patterns=inventory((candidate/WORKFLOW).read_text())
    original=run_variant(baseline,'original',output,patterns)
    optimized=run_variant(candidate,'candidate',output,patterns)
    signature=lambda r:[(x['pattern'],x['tests'],x['skipped'],x['returncode']) for x in r['runs']]
    if signature(original)!=signature(optimized):raise ValueError('regression case/skip signatures differ')
    # Full saved-view equality is tested through existing renderer/audit code,
    # with the SAME explicitly captured QA comparison clock for both variants.
    as_of=utc();audits={}
    names={'sheet':'CFB_WEEK9_HOT_SHEET_2026-10-29_2008CT.md','market':'CFB_MARKET_MONITOR_STATE.md',
           'decision':'CFB_DECISION_WAIT_LEDGER.md','execution':'CFB_EXECUTION_LEDGER.md',
           'scorecard':'CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md'}
    for label,root in [('original',baseline),('candidate',candidate)]:
        args=[sys.executable,str(root/'scripts/cfb_saved_publication_audit.py'),'--profile','WEEK9',
              '--recover-saved-inputs','--as-of',as_of,'--repository-root',str(root)]
        for key,name in names.items():args+=['--'+key,str(root/'evidence/operational'/name)]
        args+=['--lineage',str(root/'evidence/scheduler_qa/CFB_WEEK9_ORIGINAL_ANCESTRY_RECOVERY_20261025.json')]
        p=subprocess.run(args,cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        (output/(label+'-saved-view.stdout')).write_text(p.stdout)
        (output/(label+'-saved-view.stderr')).write_text(p.stderr)
        if p.returncode:raise ValueError('saved publication check failed: '+label)
        audits[label]=json.loads(p.stdout)
    if audits['original']!=audits['candidate']:raise ValueError('saved publication audit outputs differ')
    report={'schema':'CFB_ORIGIN_TEXT_INDEX_COMPARISON_V1','recorded_at_utc':utc(),
            'baseline_commit':BASELINE,'candidate_commit':git(candidate,'rev-parse','HEAD'),
            'preserved_baseline_tracked_files':len(preserved),
            'preserved_inputs_sha256':hashlib.sha256(json.dumps(preserved,sort_keys=True).encode()).hexdigest(),
            'gate_source_sha256':gate_hashes,'original':original,'candidate':optimized,
            'patterns':len(patterns),'tests':sum(r['tests'] for r in original['runs']),
            'skipped':sum(r['skipped'] for r in original['runs']),
            'observed_regression_seconds_saved':original['elapsed_seconds']-optimized['elapsed_seconds'],
            'saved_view_comparison_as_of_utc':as_of,'identical_saved_view_audit':audits['candidate'],
            'status':'PASS_IDENTICAL_REGRESSIONS_AND_SAVED_VIEW_ONLY',
            'limits':['Same cloud job/runner, original first then candidate; one paired measurement, order/cache effects possible.',
                'Only parsing is reused; no acceptance, clock, expiry, source or decision result cached.',
                'Full45step workflow/natural production/model or betting quality not certified. No production publication.']}
    (output/'comparison.json').write_text(json.dumps(report,indent=2)+'\n')
    return report


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--baseline',type=Path,required=True)
    p.add_argument('--candidate',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();print(json.dumps(compare(a.baseline,a.candidate,a.output),indent=2))
