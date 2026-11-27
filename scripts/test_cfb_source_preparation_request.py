"""A requested source bundle must be exact, timely and still unreviewed."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
import cfb_source_preparation_request as request
from cfb_cloud_source_shadow import shadow
from cfb_cloud_source_prepare import digest


class RequestTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.out=Path(self.tmp.name);self.called=0
        self.plan={'schema':'CFB_CLOUD_SOURCE_INPUT_V1','authority_ref':'a'*40,'index_blob':'c'*40,
                   'game_ids':['one'],'allowed_hosts':['example.org'],
                   'source_role_coverage':{'status':'READY_FOR_UNREVIEWED_COLLECTION_ONLY',
                     'football_required_game_ids':['one'],'saved_review_boundary_utc':'2026-10-30T01:00:00Z',
                     'plan_recorded_at_utc':'2026-10-30T02:00:00Z'},
                   'sources':[{'id':kind,'url':'https://example.org/'+kind,'kind':kind,'game_ids':['one']}
                              for kind in ['market_board','football_material']]}
        self.body={'schema':'CFB_SOURCE_PREPARATION_REQUEST_V1','request_id':'QA_TEST',
                   'created_at_utc':'2026-10-30T02:00:00Z','authority':{'commit':'a'*40,'index_path':'evidence/index.md',
                     'index_blob':'c'*40,'paths':{},'market_url':'https://example.org/market_board'},
                   'plan':copy.deepcopy(self.plan),'plan_sha256':digest(request.plan_bytes(self.plan)),
                   'supplemental_links_text':None,'supplemental_links_sha256':None}
        self.at='2026-10-30T02:05:00Z';self.commit='b'*40

    def raw(self):return (json.dumps(self.body,sort_keys=True,indent=2)+'\n').encode()

    def planner(self,*args,**kw):return self.plan,self.plan['source_role_coverage']

    def collector(self,raw,expected,output):
        self.called+=1
        def fetch(url,hosts):return url.encode(),{'http_status':200,'final_url':url}
        return shadow(raw,expected,output,fetch=fetch,clock=lambda:self.at)

    def run_request(self,planner=None):
        return request.run(self.raw(),'QA_TEST.json',self.out,self.out,self.commit,
                           clock=lambda:self.at,planner=planner or self.planner,collector=self.collector)

    def test_valid_roundtrip_stays_unreviewed_and_requires_matching_commit(self):
        result=self.run_request()
        verified=request.verify_bundle(self.raw(),result,self.out,self.at,self.commit)
        self.assertEqual(verified['status'],'VERIFIED_UNREVIEWED_REQUEST_BUNDLE_ONLY')
        self.assertEqual(verified['football_analysis'],'STILL_REQUIRED')
        self.assertFalse(verified['canonical_mutation'])
        with self.assertRaisesRegex(ValueError,'artifact identity'):
            request.verify_bundle(self.raw(),result,self.out,self.at,'d'*40)

    def test_stale_future_wrong_file_and_extra_fields_rejected_before_fetch(self):
        for at in ['2026-10-30T01:59:00Z','2026-10-30T03:00:00Z']:
            with self.subTest(at=at),self.assertRaisesRegex(ValueError,'future or stale'):
                request.validate_request(self.raw(),'QA_TEST.json',at)
        with self.assertRaisesRegex(ValueError,'identity/file'):
            request.validate_request(self.raw(),'other.json',self.at)
        self.body['unsupported']=True
        with self.assertRaisesRegex(ValueError,'unsupported request fields'):self.run_request()
        self.assertEqual(self.called,0)

    def test_rehashed_unapproved_plan_cannot_bypass_authority_reproduction(self):
        self.body['plan']['sources'][0]['url']='https://example.org/changed'
        self.body['plan_sha256']=digest(request.plan_bytes(self.body['plan']))
        with self.assertRaisesRegex(ValueError,'does not reproduce'):self.run_request()
        self.assertEqual(self.called,0)

    def test_frontier_failure_and_source_plan_digest_stop_fetch(self):
        def changed(*args,**kwargs):raise ValueError('frontier changed')
        with self.assertRaisesRegex(ValueError,'frontier changed'):self.run_request(changed)
        self.body['plan_sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'digest mismatch'):self.run_request()
        self.assertEqual(self.called,0)

    def test_tampered_raw_body_or_report_cannot_be_consumed(self):
        result=self.run_request();changed=copy.deepcopy(result)
        changed['source_roles']['football_raw_linked_saved_active_games']=99
        with self.assertRaisesRegex(ValueError,'source roles'):
            request.verify_bundle(self.raw(),changed,self.out,self.at,self.commit)
        m=json.loads((self.out/'collection/manifest.json').read_text())
        (self.out/'collection'/m['sources'][0]['artifact']).write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError,'source roles'):
            request.verify_bundle(self.raw(),result,self.out,self.at,self.commit)

    def test_duplicate_keys_and_authority_plan_mismatch_are_rejected(self):
        raw=self.raw().replace(b'"request_id": "QA_TEST",',b'"request_id": "QA_TEST", "request_id": "OTHER",')
        with self.assertRaisesRegex(ValueError,'duplicate'):
            request.validate_request(raw,'QA_TEST.json',self.at)
        self.body['authority']['commit']='f'*40
        with self.assertRaisesRegex(ValueError,'authority differs'):self.run_request()


if __name__=='__main__':unittest.main()
