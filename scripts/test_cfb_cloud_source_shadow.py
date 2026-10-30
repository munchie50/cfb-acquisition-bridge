"""Full-board availability must not conceal missing football material."""
import json
from pathlib import Path
import tempfile
import unittest
from cfb_cloud_source_prepare import digest
import cfb_cloud_source_shadow as module


class RoleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.out = Path(self.tmp.name)
        self.plan = {'schema': 'CFB_CLOUD_SOURCE_INPUT_V1', 'authority_ref': 'synthetic', 'index_blob': 'synthetic',
                     'game_ids': ['one','two'], 'allowed_hosts': ['example.org'],
                     'source_role_coverage': {'status':'READY_FOR_UNREVIEWED_COLLECTION_ONLY',
                         'football_required_game_ids':['one','two'], 'saved_review_boundary_utc':'2026-10-30T02:00:00Z'},
                     'sources': [{'id':'board','url':'https://example.org/board','kind':'market_board','game_ids':['one','two']},
                                 {'id':'one','url':'https://example.org/one','kind':'football_material','game_ids':['one']},
                                 {'id':'two','url':'https://example.org/two','kind':'football_material','game_ids':['two']}]}
        self.failed = None

    def fetch(self,url,hosts):
        if url.endswith('/'+str(self.failed)): raise TimeoutError()
        return url.encode(), {'http_status':200,'final_url':url}

    def run_shadow(self):
        raw=json.dumps(self.plan).encode()
        return module.shadow(raw,digest(raw),self.out,fetch=self.fetch,clock=lambda:'2026-10-30T02:05:00Z')

    def test_full_board_does_not_hide_failed_football_source(self):
        self.failed='two'; r=self.run_shadow()
        self.assertEqual(r['market_raw_linked_games'],2)
        self.assertEqual(r['football_raw_linked_saved_active_games'],1)
        self.assertEqual(r['active_games_without_fetched_football_source'],['two'])
        self.assertEqual(r['status'],'INCOMPLETE_UNREVIEWED_NOT_A_PASS')

    def test_missing_market_stays_incomplete_with_all_football_sources(self):
        self.failed='board';r=self.run_shadow()
        self.assertEqual(r['football_raw_linked_saved_active_games'],2)
        self.assertEqual(r['market_raw_linked_games'],0)
        self.assertEqual(r['status'],'INCOMPLETE_UNREVIEWED_NOT_A_PASS')

    def test_source_role_tamper_and_raw_corruption_rejected(self):
        self.run_shadow(); raw=json.dumps(self.plan).encode()
        result=json.loads((self.out/'manifest.json').read_text())
        original=result['sources'][1]
        (self.out/original['artifact']).write_bytes(b'tampered')
        report=module.role_report(self.plan,raw,result,self.out,'2026-10-30T02:05:00Z')
        self.assertIn(original['id'],report['invalid_or_stale_raw_source_ids'])
        original['kind']='market_board'
        with self.assertRaisesRegex(ValueError,'association changed'):
            module.role_report(self.plan,raw,result,self.out,'2026-10-30T02:05:00Z')

    def test_complete_collection_remains_unreviewed(self):
        r=self.run_shadow()
        self.assertEqual(r['status'],'COMPLETE_UNREVIEWED_COLLECTION_ONLY')
        self.assertEqual(r['football_analysis'],'NOT_PERFORMED')
        self.assertFalse(r['production_publication_or_model_change'])


if __name__=='__main__':unittest.main()
