#!/usr/bin/env python3
"""QA ONLY: original module selector integration; no repository mutation."""
import argparse, json, sys
from pathlib import Path
from datetime import datetime, timezone
BASE='6862be6a1bd88a3290b1e90a49c33a7a87e92559'
DELTA='646bbe85edba726037e1b98125783ff2cd87a4e8'
EXPECTED='98941e228072e6941b1c33e42d4d8dba570f7182'
PREVIEW='evidence/operational/CFB_WEEK12_20261120_MANUAL_RENDERED_HOT_SHEET_PREVIEW_NOT_ACCEPTED.md'
CANON='evidence/operational/CFB_DECISION_WAIT_LEDGER.md'
CANDIDATE='evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_1450CT.md'
def run(repo, blob_dir=None):
    sys.path.insert(0,str(repo/'scripts'))
    from cfb_overlay_publication_probe import checked_blob,git_blob_sha
    from cfb_hot_sheet_current_decision_binding_gate import audit,publication,blob
    if blob_dir is None:
        base,delta=checked_blob(repo,BASE),checked_blob(repo,DELTA)
    else:
        # Connector-staged immutable UTF-8 blobs: no git, DNS, or checkout required.
        base,delta=(blob_dir/BASE).read_bytes(),(blob_dir/DELTA).read_bytes()
        if git_blob_sha(base)!=BASE or git_blob_sha(delta)!=DELTA:
            raise RuntimeError('staged blob identity mismatch')
    raw=base+delta
    if git_blob_sha(raw)!=EXPECTED:
        raise RuntimeError('actual decision ledger mismatch')
    ledger=raw.decode('utf-8')
    sheet=(repo/PREVIEW).read_bytes().decode('utf-8')
    if audit(sheet,ledger)['verdict']!='PASS_SUPPLIED_CURRENT_DECISION_BINDING_ONLY':
        raise RuntimeError('positive audit did not pass')
    neg_audit={}
    for name,wrong in [('old_base',base.decode('utf-8')),('tampered',ledger+'x')]:
        try:audit(sheet,wrong)
        except ValueError as e:
            if 'stale current publication' not in str(e):
                raise RuntimeError(name+' rejected for unexpected reason: '+str(e)) from e
            neg_audit[name]=str(e)
        else:raise RuntimeError(name+' should reject')
    def ptr(path,digest,purpose):return {'path':path,'blob':digest,'purpose':purpose}
    def idx(pointers):
        record={'schema':'CFB_RECOVERY_NAVIGATION_FRONTIER_V1','as_of_utc':'2026-11-20T21:40:00+00:00','scope':'NAVIGATION_ONLY_NOT_AUTHORITY','claims':['QA-only candidate; not canonical promotion'],'pointers':pointers}
        return '```cfb-frontier-json\n'+json.dumps(record,indent=2)+'\n```\n'
    good=[ptr(CANON,EXPECTED,'CURRENT_DECISION_STATE:QA virtual ledger'),ptr(CANDIDATE,blob(sheet),'CURRENT_HOT_SHEET:QA candidate')]
    def load(path):
        if path!=CANDIDATE:raise ValueError('unexpected path')
        return sheet
    now=max(datetime.now(timezone.utc),datetime.fromisoformat('2026-11-20T21:40:01+00:00')).isoformat()
    positive=publication(idx(good),ledger,load,now)
    if positive['verdict']!='PASS_SUPPLIED_CURRENT_DECISION_BINDING_ONLY':
        raise RuntimeError('positive publication did not pass')
    bad={
        'stale_decision_pointer':[ptr(CANON,BASE,'CURRENT_DECISION_STATE:stale'),good[1]],
        'wrong_sheet_digest':[good[0],ptr(CANDIDATE,BASE,'CURRENT_HOT_SHEET:wrong')],
        'unsupported_provisional_path':[good[0],ptr('evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_MANUAL_PROVISIONAL_RELEASE.md',blob(sheet),'CURRENT_HOT_SHEET:bad path')],
        'duplicate_current_sheet':[good[0],good[1],ptr('evidence/operational/CFB_WEEK12_HOT_SHEET_2026-11-20_1600CT.md',blob(sheet),'CURRENT_HOT_SHEET:duplicate')],
        'missing_decision_pointer':[good[1]],
        'missing_current_sheet':[good[0]],
        'duplicate_pointer_path':[good[0],good[1],ptr(CANDIDATE,blob(sheet),'CURRENT_HOT_SHEET:duplicate path')]
    }
    expected_reasons={
        'stale_decision_pointer':'recovery canonical decision pointer is stale or missing',
        'wrong_sheet_digest':'current publication bytes differ from recovery pointer',
        'unsupported_provisional_path':'unsupported current publication path',
        'duplicate_current_sheet':'one explicit CURRENT_HOT_SHEET pointer required',
        'missing_decision_pointer':'recovery canonical decision pointer is stale or missing',
        'missing_current_sheet':'one explicit CURRENT_HOT_SHEET pointer required',
        'duplicate_pointer_path':'duplicate pointer path',
    }
    neg_publication={}
    for name,pointers in bad.items():
        try:publication(idx(pointers),ledger,load,now)
        except ValueError as e:
            if expected_reasons[name] not in str(e):
                raise RuntimeError(name+' rejected for unexpected reason: '+str(e)) from e
            neg_publication[name]=str(e)
        else:raise RuntimeError(name+' should reject')
    print(json.dumps({'status':'QA_ORIGINAL_MODULE_INTEGRATION_PASS_NOT_PRODUCTION','decision_blob':EXPECTED,'positive':positive['verdict'],'negative_audit':neg_audit,'negative_publication':neg_publication},indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--repo',type=Path,default=Path('.'))
    p.add_argument('--blob-dir',type=Path,help='Offline connector-staged immutable Git blob files named by SHA')
    args=p.parse_args()
    run(args.repo.resolve(),args.blob_dir.resolve() if args.blob_dir else None)
