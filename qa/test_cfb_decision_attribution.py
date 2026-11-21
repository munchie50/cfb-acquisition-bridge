import unittest
from cfb_decision_attribution import attribute
BASE = dict(game_id='1',market='home_spread',as_of_utc='2026-11-20T18:00:00Z',source_ref='saved-review-1',reason='supported but price fails',original_state='PASS',evidence_tags=['FOOTBALL_SUPPORT','PRICE_HOLD'],price_only=True)
class AttributionTests(unittest.TestCase):
    def test_price_only_requires_explicit_evidence(self):
        self.assertTrue(attribute(BASE)['price_only_documented'])
        self.assertFalse(attribute(BASE)['bet_authorized'])
    def test_football_contradiction_prevents_price_only(self):
        with self.assertRaises(ValueError): attribute({**BASE,'evidence_tags':['PRICE_HOLD','FOOTBALL_SUPPORT','FOOTBALL_COUNTERCASE']})
    def test_missing_source_fails(self):
        with self.assertRaises(ValueError): attribute({**BASE,'source_ref':''})
    def test_unknown_tag_fails(self):
        with self.assertRaises(ValueError): attribute({**BASE,'evidence_tags':['UNKNOWN']})
    def test_multiple_causes_allowed(self):
        out=attribute({**BASE,'price_only':False,'evidence_tags':['PRICE_HOLD','FOOTBALL_COUNTERCASE']})
        self.assertFalse(out['price_only_documented'])
    def test_no_inferred_price_only(self):
        out=attribute({**BASE,'price_only':False})
        self.assertFalse(out['price_only_documented'])
if __name__=='__main__': unittest.main()
