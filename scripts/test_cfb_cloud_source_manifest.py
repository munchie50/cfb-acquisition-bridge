"""Authentic saved populations with deliberately broken binding/coverage inputs."""
import copy
from functools import lru_cache
import json
from pathlib import Path
import re
import subprocess
import unittest
import cfb_cloud_source_manifest as adapter
from cfb_cloud_source_prepare import digest

ROOT = Path(__file__).resolve().parents[1]
INDEX = 'evidence/CFB_ENGINE_CURRENT_RECOVERY_INDEX_v1_245.md'
PATHS = {'lineage': 'evidence/scheduler_qa/CFB_WEEK9_ORIGINAL_ANCESTRY_RECOVERY_20261025.json',
         'research': 'evidence/operational/CFB_WEEK9_POPULATION_RESEARCH_20261026T225722Z.json',
         'revalidation': 'evidence/operational/CFB_MARKET_MONITOR_20261030T010121Z_REVALIDATION.json'}
URL = 'https://www.cbssports.com/college-football/odds/FBS/2026/regular/week-9/'
AT = '2026-10-30T02:30:00Z'  # Synthetic validation clock, not an operational observation.
COMMIT = '8df63ed20c2cc53f41ec93815c6a2895bac06892'


@lru_cache(maxsize=32)
def fixture(path):
    # This is an immutable historical Week9 fixture. The live CLI separately
    # requires fresh connector-observed main; do not advance synthetic clocks
    # whenever navigation-only metadata is appended to production main.
    return subprocess.check_output(['git','-C',str(ROOT),'show',COMMIT+':'+path],text=True)


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.index = fixture(INDEX)
        self.overrides = {}
        self.extra = json.loads((ROOT/'evidence/scheduler_qa/CFB_CLOUD_SOURCE_ASSOCIATIONS_20261030.json').read_text())

    def load(self, path):
        return self.overrides[path] if path in self.overrides else fixture(path)

    def change_frontier(self, change):
        matches = list(re.finditer(r'```cfb-frontier-json\n(.*?)\n```', self.index, re.S))
        m = matches[-1]; r = json.loads(m[1]); change(r)
        self.index = self.index[:m.start(1)]+json.dumps(r, indent=2)+self.index[m.end(1):]

    def replace_input(self, name, change):
        path = PATHS[name]; r = json.loads(self.load(path)); change(r)
        text = json.dumps(r); self.overrides[path] = text
        self.change_frontier(lambda f: [p.update(blob=adapter.blob(text)) for p in f['pointers'] if p['path']==path])
        if name == 'revalidation': self.extra['revalidation_blob'] = adapter.blob(text)

    def build(self, supplement=True, url=URL):
        extra = json.dumps(self.extra).encode() if supplement else None
        return adapter.build(self.index, adapter.blob(self.index), COMMIT, self.load, PATHS,
                             url, AT, extra, digest(extra) if extra else None)

    def test_authentic_population_separates_links_and_never_claims_research_complete(self):
        plan, report = self.build()
        self.assertEqual(report['governed_games'], 56)
        self.assertEqual(report['saved_active_prediction_games'], 35)
        self.assertEqual(report['football_linked_active_games'], 35)
        self.assertEqual(report['status'], 'READY_FOR_UNREVIEWED_COLLECTION_ONLY')
        self.assertTrue(report['source_link_coverage_is_not_football_review_completeness'])
        self.assertEqual(len(plan['sources']), len({s['url'] for s in plan['sources']}))

    def test_global_new_sources_without_game_ids_are_not_silently_ignored(self):
        _, report = self.build(supplement=False)
        self.assertEqual(len(report['new_material_urls_without_explicit_game_links']), 4)
        self.assertEqual(report['status'], 'SOURCE_PLAN_INCOMPLETE_NOT_A_PASS')

    def test_stale_body_cannot_match_frontier(self):
        self.overrides[PATHS['research']] = self.load(PATHS['research'])+' '
        with self.assertRaisesRegex(ValueError, 'stale input'): self.build()

    def test_missing_required_pointer_and_noncurrent_role_are_rejected(self):
        self.change_frontier(lambda f: f.update(pointers=[p for p in f['pointers'] if p['path']!=PATHS['research']]))
        with self.assertRaisesRegex(ValueError, 'missing from accepted'): self.build()
        self.setUp()
        self.change_frontier(lambda f: [p.update(purpose='PRIOR_REVIEW') for p in f['pointers'] if p['path']==PATHS['revalidation']])
        with self.assertRaisesRegex(ValueError, 'explicit current'): self.build()

    def test_population_mismatch_and_duplicate_games_rejected(self):
        self.replace_input('research', lambda r: r['games'].pop())
        with self.assertRaisesRegex(ValueError, 'populations differ'): self.build()
        self.setUp(); self.replace_input('research', lambda r: r['games'].append(copy.deepcopy(r['games'][0])))
        with self.assertRaisesRegex(ValueError, 'duplicate game'): self.build()

    def test_missing_football_source_is_visible_even_with_full_board(self):
        self.replace_input('research', lambda r: next(g for g in r['games'] if g['game_id']=='401862813').update(source_ids=[]))
        _, report = self.build()
        self.assertEqual(report['market_linked_games'], 56)
        self.assertIn('401862813', report['active_games_without_football_links'])
        self.assertEqual(report['status'], 'SOURCE_PLAN_INCOMPLETE_NOT_A_PASS')

    def test_unknown_source_ids_and_duplicate_catalog_ids_rejected(self):
        self.replace_input('research', lambda r: r['games'][0]['source_ids'].append('MISSING'))
        with self.assertRaisesRegex(ValueError, 'unresolved explicit'): self.build()
        self.setUp(); self.replace_input('research', lambda r: r['sources'].append(copy.deepcopy(r['sources'][0])))
        with self.assertRaisesRegex(ValueError, 'duplicate source catalog'): self.build()

    def test_supplement_wrong_authority_unknown_url_and_excluded_game_rejected(self):
        self.extra['authority_commit'] = '0'*40
        with self.assertRaisesRegex(ValueError, 'authority mismatch'): self.build()
        self.setUp(); self.extra['links'][0]['url'] = 'https://example.org/not-declared'
        with self.assertRaisesRegex(ValueError, 'unknown or duplicate'): self.build()
        self.setUp(); self.extra['links'][0]['game_ids'] = ['401858277']
        with self.assertRaisesRegex(ValueError, 'outside eligible'): self.build()

    def test_wrong_market_url_and_new_classification_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'market URL absent'): self.build(url='https://example.org/other')
        self.replace_input('revalidation', lambda r: r['cases'][0].update(classification='NEW_UNKNOWN'))
        with self.assertRaisesRegex(ValueError, 'requires qualification'): self.build()

    def test_future_saved_review_rejected(self):
        self.replace_input('revalidation', lambda r: r.update(as_of_utc='2040-01-01T00:00:00Z'))
        with self.assertRaisesRegex(ValueError, 'future review'): self.build()

    def test_market_pointer_must_match_both_declared_and_actual_capture(self):
        p=json.loads(self.load(PATHS['revalidation']))['source']['path']
        self.change_frontier(lambda f: [q.update(blob='0'*40) for q in f['pointers'] if q['path']==p])
        with self.assertRaisesRegex(ValueError, 'market capture exact'): self.build()

    def test_only_verified_ancestor_associations_survive_metadata_only_main_changes(self):
        extra=json.dumps(self.extra).encode()
        args=(self.index,adapter.blob(self.index),'b'*40,self.load,PATHS,URL,AT,extra,digest(extra))
        with self.assertRaisesRegex(ValueError,'authority mismatch'):adapter.build(*args)
        _,report=adapter.build(*args,approved_association_commits=[COMMIT])
        self.assertEqual(report['status'],'READY_FOR_UNREVIEWED_COLLECTION_ONLY')
        changed=copy.deepcopy(self.extra);changed['revalidation_blob']='0'*40
        raw=json.dumps(changed).encode()
        with self.assertRaisesRegex(ValueError,'authority mismatch'):
            adapter.build(*args[:7],raw,digest(raw),approved_association_commits=[COMMIT])

    def test_explicit_new_material_game_ids_remove_need_for_sidecar(self):
        links={x['url']:x['game_ids'] for x in self.extra['links']}
        self.replace_input('revalidation',lambda r:[s.update(game_ids=links[s['url']]) for s in r['new_material_sources']])
        _,report=self.build(supplement=False)
        self.assertEqual(report['new_material_urls_without_explicit_game_links'],[])
        self.assertEqual(report['status'],'READY_FOR_UNREVIEWED_COLLECTION_ONLY')
        self.replace_input('revalidation',lambda r:r['new_material_sources'][0].update(game_ids=['unknown']))
        with self.assertRaisesRegex(ValueError,'outside eligible'):self.build(supplement=False)


if __name__ == '__main__': unittest.main()
