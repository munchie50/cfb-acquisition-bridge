import copy
import json
import unittest
import cfb_recovery_navigation_reader as reader

BASE={'schema':reader.SCHEMA,'as_of_utc':'2026-10-10T00:17:55Z','scope':'NAVIGATION_ONLY_NOT_AUTHORITY',
      'claims':['Historical morning gap stays incomplete; afternoon proof is separate.'],
      'pointers':[{'path':'evidence/run_receipts/example.md','blob':'a'*40,'purpose':'independently recover evidence'}]}
NOW='2026-10-10T00:20:00Z'
def block(r):return '\n```cfb-frontier-json\n'+json.dumps(r)+'\n```\n'

class NavigationTests(unittest.TestCase):
    def test_later_dinner_prose_cannot_be_silently_ignored(self):
        tail='\n## October 9 19:53:50 CT dinner update\nThree conditional recommendations.\n'
        with self.assertRaisesRegex(ValueError,'uncheckpointed trailing content'):
            reader.read(block(BASE)+tail,NOW)
    def test_unclocked_tail_is_not_assumed_immaterial(self):
        for tail in ['Pending consumer correction.','<!-- changed state -->','## Historical clarification']:
            with self.subTest(tail=tail), self.assertRaisesRegex(ValueError,'uncheckpointed trailing content'):
                reader.read(block(BASE)+tail,NOW)
    def test_intervening_prose_requires_new_final_checkpoint(self):
        later=copy.deepcopy(BASE);later['as_of_utc']='2026-10-10T00:18:55Z'
        result=reader.read(block(BASE)+'\nMaterial dinner change.\n'+block(later),NOW)
        self.assertEqual(result['frontier'],later)
        self.assertEqual(result['checkpoint_count'],2)
        self.assertEqual(result['pointer_readback'],'NOT_PERFORMED')
    def test_trailing_whitespace_is_allowed(self):
        self.assertEqual(reader.read(block(BASE)+' \t\r\n\n',NOW)['frontier'],BASE)
    def test_crlf_fences_preserve_tail_detection(self):
        text=block(BASE).replace('\n','\r\n')
        self.assertEqual(reader.read(text,NOW)['frontier'],BASE)
        with self.assertRaisesRegex(ValueError,'uncheckpointed trailing content'):
            reader.read(text+'New update',NOW)
    def test_final_checkpoint_does_not_certify_claims(self):
        later=copy.deepcopy(BASE);later['as_of_utc']='2026-10-10T00:18:55Z'
        later['claims']=['Unverified offer remains unverified.']
        result=reader.read(block(BASE)+'\nSource limit.\n'+block(later),NOW)
        self.assertEqual(result['status'],'NAVIGATION_ONLY_NOT_AUTHORITY')
        self.assertEqual(result['frontier']['claims'],later['claims'])
        self.assertEqual(result['pointer_readback'],'NOT_PERFORMED')
    def test_stale_top_does_not_win(self):
        r=reader.read('## Current frontier — morning\nAfternoon pending.\n'+block(BASE),NOW)
        self.assertEqual(r['frontier'],BASE)
        self.assertEqual(r['pointer_readback'],'NOT_PERFORMED')
    def test_last_explicit_record(self):
        later=copy.deepcopy(BASE);later['as_of_utc']='2026-10-10T00:18:55Z'
        self.assertEqual(reader.read(block(BASE)+block(later),NOW)['frontier'],later)
    def test_no_explicit_checkpoint(self):
        with self.assertRaises(ValueError):reader.read('Latest PASS claimed in prose',NOW)
    def test_truncated_checkpoint(self):
        with self.assertRaises(ValueError):reader.read(block(BASE)+'\n```cfb-frontier-json\n{}',NOW)
    def test_future_clock(self):
        with self.assertRaises(ValueError):reader.read(block(BASE),'2026-10-10T00:16:00Z')
    def test_clock_requires_zone(self):
        bad=copy.deepcopy(BASE);bad['as_of_utc']='2026-10-10T00:17:55'
        with self.assertRaises(ValueError):reader.read(block(bad),NOW)
    def test_duplicate_or_reversed_clock(self):
        old=copy.deepcopy(BASE);old['as_of_utc']='2026-10-10T00:16:55Z'
        for tail in [BASE,old]:
            with self.assertRaises(ValueError):reader.read(block(BASE)+block(tail),NOW)
    def test_claimed_authority_rejected(self):
        bad=copy.deepcopy(BASE);bad['scope']='PRODUCTION_AUTHORITY'
        with self.assertRaises(ValueError):reader.read(block(bad),NOW)
    def test_duplicate_key(self):
        text=block(BASE).replace('"schema":','"schema":"duplicate", "schema":')
        with self.assertRaises(ValueError):reader.read(text,NOW)
    def test_invalid_pointer_or_duplicate_path(self):
        for change in ['traversal','hash','duplicate']:
            bad=copy.deepcopy(BASE)
            if change=='traversal':bad['pointers'][0]['path']='evidence/../secrets'
            elif change=='hash':bad['pointers'][0]['blob']='not-a-blob'
            else:bad['pointers'].append(copy.deepcopy(bad['pointers'][0]))
            with self.assertRaises(ValueError):reader.read(block(bad),NOW)

if __name__=='__main__':unittest.main()

