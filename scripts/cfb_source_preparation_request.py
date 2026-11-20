"""Request/hash-bound read-only source worker; no new timer or publisher.

QA push events select exactly one newly added request. Runtime rechecks the
accepted frontier and regenerates the plan before fetching unreviewed sources.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
from cfb_cloud_source_manifest import snapshot_plan
from cfb_cloud_source_prepare import atomic_json, digest, timestamp, utc
from cfb_cloud_source_shadow import shadow, role_report
from cfb_recovery_navigation_reader import unique

DIRECTORY='evidence/source_preparation_qa_requests'


def plan_bytes(plan):
    return (json.dumps(plan,indent=2,sort_keys=True)+'\n').encode()


def validate_request(raw,filename,as_of):
    r=json.loads(raw,object_pairs_hook=unique)
    if set(r)!={'schema','request_id','created_at_utc','authority','plan','plan_sha256',
                'supplemental_links_text','supplemental_links_sha256'}:
        raise ValueError('unsupported request fields')
    if r['schema']!='CFB_SOURCE_PREPARATION_REQUEST_V1':raise ValueError('unsupported request schema')
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,100}',r['request_id']) or Path(filename).stem!=r['request_id']:
        raise ValueError('request identity/file mismatch')
    age=(timestamp(as_of)-timestamp(r['created_at_utc'])).total_seconds()
    if not 0<=age<=1800:raise ValueError('future or stale preparation request')
    if digest(plan_bytes(r['plan']))!=r['plan_sha256']:
        raise ValueError('source plan digest mismatch')
    if r['plan']['source_role_coverage']['plan_recorded_at_utc']!=r['created_at_utc']:
        raise ValueError('request must preserve its actual plan preparation clock')
    a=r['authority']
    if set(a)!={'commit','index_path','index_blob','paths','market_url'}:
        raise ValueError('unsupported authority fields')
    if a['commit']!=r['plan']['authority_ref'] or a['index_blob']!=r['plan']['index_blob']:
        raise ValueError('request authority differs from source plan')
    if r['supplemental_links_text'] is not None:
        if digest(r['supplemental_links_text'].encode())!=r['supplemental_links_sha256']:
            raise ValueError('supplemental source association digest mismatch')
    elif r['supplemental_links_sha256'] is not None:
        raise ValueError('missing supplemental association bytes')
    return r


def run(raw,filename,root,output,request_commit,clock=utc,planner=snapshot_plan,collector=shadow):
    r=validate_request(raw,filename,clock())
    a=r['authority'];extra=r['supplemental_links_text']
    plan,coverage=planner(root,a['commit'],a['index_path'],a['index_blob'],a['paths'],
        a['market_url'],r['created_at_utc'],extra.encode() if extra else None,
        r['supplemental_links_sha256'],require_current_head=False)
    if plan_bytes(plan)!=plan_bytes(r['plan']) or coverage['status']!='READY_FOR_UNREVIEWED_COLLECTION_ONLY':
        raise ValueError('request source plan does not reproduce from accepted authority')
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    (output/'request.source.json').write_bytes(raw)
    atomic_json(output/'request.json',r)
    atomic_json(output/'source-plan.json',plan)
    roles=collector(plan_bytes(plan),r['plan_sha256'],output/'collection')
    result={'schema':'CFB_SOURCE_PREPARATION_REQUEST_RESULT_V1','request_id':r['request_id'],
            'request_commit':request_commit,'worker_git_head':request_commit,
            'request_sha256':digest(raw),'plan_sha256':r['plan_sha256'],
            'authority_commit':a['commit'],'index_blob':a['index_blob'],
            'request_created_at_utc':r['created_at_utc'],'completed_at_utc':clock(),
            'status':roles['status'],'source_roles':roles,
            'canonical_mutation':False,'football_analysis':'NOT_PERFORMED',
            'consumer_rule':'Verify request/run/artifact identity, raw hashes and per-source age before football review. Raw collection is never a betting decision.'}
    atomic_json(output/'request-result.json',result)
    return result


def verify_bundle(request_raw,result,output,as_of,expected_request_commit):
    """Consumer rechecks identity and raw bytes; never returns a football PASS."""
    request=json.loads(request_raw,object_pairs_hook=unique)
    r=validate_request(request_raw,request['request_id']+'.json',as_of)
    if (result['schema']!='CFB_SOURCE_PREPARATION_REQUEST_RESULT_V1'
            or result['request_commit']!=expected_request_commit
            or result['worker_git_head']!=expected_request_commit
            or result['request_id']!=r['request_id'] or result['request_sha256']!=digest(request_raw)
            or result['plan_sha256']!=r['plan_sha256']
            or result['authority_commit']!=r['authority']['commit']
            or result['index_blob']!=r['authority']['index_blob'] or result['canonical_mutation'] is not False):
        raise ValueError('artifact identity differs from requested worker invocation')
    output=Path(output)
    if (output/'request.source.json').read_bytes()!=request_raw:
        raise ValueError('artifact request bytes differ')
    manifest=json.loads((output/'collection/manifest.json').read_text(),object_pairs_hook=unique)
    roles=role_report(r['plan'],plan_bytes(r['plan']),manifest,output/'collection',as_of)
    fields=('status','planned_sources','fetched_sources','reused_sources','failed_sources',
            'invalid_or_stale_raw_source_ids','governed_games','market_raw_linked_games',
            'football_required_saved_active_games','football_raw_linked_saved_active_games',
            'active_games_without_fetched_football_source')
    if any(roles[k]!=result['source_roles'][k] for k in fields):
        raise ValueError('artifact source roles, raw hashes or ages no longer verify')
    return {'status':'VERIFIED_UNREVIEWED_REQUEST_BUNDLE_ONLY','source_roles':roles,
            'request_id':r['request_id'],'request_commit':expected_request_commit,
            'football_analysis':'STILL_REQUIRED','canonical_mutation':False}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--before',required=True)
    p.add_argument('--after',required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    if any(not re.fullmatch('[0-9a-f]{40}',x) or set(x)=={'0'} for x in (a.before,a.after)):
        p.error('exact nonempty before/after commits required')
    changed=subprocess.check_output(['git','diff','--name-status',a.before,a.after,'--',DIRECTORY],text=True).splitlines()
    if len(changed)!=1 or not changed[0].startswith('A\t'):
        raise ValueError('one new immutable request per source worker invocation required')
    path=changed[0].split('\t')[1]
    if not re.fullmatch(DIRECTORY+r'/[A-Za-z0-9_-]+\.json',path):raise ValueError('unsupported request path')
    raw=subprocess.check_output(['git','show',a.after+':'+path])
    if subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()!=a.after:
        raise ValueError('worker checkout differs from request event commit')
    result=run(raw,path,Path('.'),a.output,a.after)
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['status']=='COMPLETE_UNREVIEWED_COLLECTION_ONLY' else 2)
