import copy,json,unittest
from pathlib import Path
import cfb_neutral_publication_legacy_replay as replay
import cfb_neutral_publication_gate as gate

class AuthenticReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path('evidence/operational')
        cls.m=replay.historical(root/'CFB_MARKET_MONITOR_STATE.md',replay.MARKET_SHA);cls.d=replay.historical(root/'CFB_DECISION_WAIT_LEDGER.md',replay.DECISION_SHA);cls.l=(root/'CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json').read_text()
        cls.c={r['game_id']:(r['away_team'],r['home_team']) for r in json.loads(cls.l)['rows']}
    def normalized(self):return replay.normalize(self.m,self.d,self.l)
    def row(self,n,pair):return next(r for r in n['market']['rows'] if self.c[r['game_id']]==pair)
    def test_authentic_full62_replay(self):
        r=replay.replay(self.m,self.d,'historical execution','historical scorecard',self.l);self.assertEqual((r['games'],r['current_quotes'],r['historical_retained_only']),(62,55,7))
    def test_conflicted_delaware_not_used(self):
        r=self.row(self.normalized(),('Delaware','Middle Tennessee'));self.assertEqual((r['current']['away_spread'],r['current']['away_ml']),(-2.5,-135));self.assertEqual(r['current']['retrieved_at'],'2026-10-12T12:07:02Z')
    def test_fiu_first_asymmetric_preserved(self):
        r=self.row(self.normalized(),('Florida International','Jacksonville State'));self.assertEqual((r['first']['away_spread'],r['first']['home_spread']),(3.5,-3));self.assertEqual(r['first']['source_type'],'UNIDENTIFIED_MIXED_BOOK_FALLBACK')
    def test_fiu_current_changed_price_preserved(self):
        r=self.row(self.normalized(),('Florida International','Jacksonville State'));self.assertEqual((r['current']['away_spread_price'],r['current']['home_spread_price']),(-115,-105));self.assertEqual(r['current']['retrieval_precision'],'MINUTE')
    def test_central_michigan_canonical_correction_consumed(self):
        r=self.row(self.normalized(),('Western Michigan','Central Michigan'));self.assertEqual((r['current']['away_spread'],r['current']['event_id']),(-7,'34788204'))
    def test_unavailable_not_current(self):
        r=self.row(self.normalized(),('Georgia Southern','Old Dominion'));self.assertIsNone(r['current']);self.assertIsNotNone(r['retained']);self.assertEqual(r['current_availability'],'UNAVAILABLE')
    def test_nebraska_corrected_clock_without_authority_promotion(self):
        n=self.normalized();r=self.row(n,('Nebraska','Oregon'));self.assertEqual(r['kickoff_utc'],'2026-10-18T03:00:00Z');self.assertEqual(r['kickoff_status'],'RETAINED_UNVERIFIED');d=next(x for x in n['decision']['rows'] if x['game_id']==r['game_id']);self.assertEqual((d['planning_cutoff_utc'],d['cutoff_authority']),('2026-10-18T02:00:00Z','UNVERIFIED'))
    def test_replay_mutated_source_rejected(self):
        with self.assertRaises(ValueError):replay.normalize(self.m+'\n',self.d,self.l)
    def test_all_original_source_bytes_remain(self):
        n=self.normalized();m=self.m+replay.packet(n['market'],gate.MARKET_TAG);d=self.d+replay.packet(n['decision'],gate.DECISION_TAG);self.assertTrue(m.startswith(self.m));self.assertTrue(d.startswith(self.d));gate.render(m,d,'execution','scorecard',self.l,replay.AT);gate.bootstrap(m,d,self.l)
    def test_unknown_bootstrap_rejected(self):
        n=self.normalized()
        with self.assertRaises(ValueError):gate.bootstrap('unknown source'+replay.packet(n['market'],gate.MARKET_TAG),self.d+replay.packet(n['decision'],gate.DECISION_TAG),self.l)
    def test_original_first_changed_before_bootstrap_rejected(self):
        n=self.normalized();r=next(r for r in n['market']['rows'] if r['first'] is not None);r['first']['over_price']=-101
        with self.assertRaises(ValueError):gate.bootstrap(self.m+replay.packet(n['market'],gate.MARKET_TAG),self.d+replay.packet(n['decision'],gate.DECISION_TAG),self.l)
    def test_new_first_after_authentic_unavailability_boundary(self):
        from test_cfb_neutral_publication_gate import offer
        n=self.normalized();r=next(r for r in n['market']['rows'] if r['first'] is None);o=offer();o['retrieved_at']='2026-10-13T12:00:00Z';r['first']=o
        gate.bootstrap(self.m+replay.packet(n['market'],gate.MARKET_TAG),self.d+replay.packet(n['decision'],gate.DECISION_TAG),self.l)
        r['first']['retrieved_at']='2026-10-11T12:00:00Z'
        with self.assertRaises(ValueError):gate.bootstrap(self.m+replay.packet(n['market'],gate.MARKET_TAG),self.d+replay.packet(n['decision'],gate.DECISION_TAG),self.l)

if __name__=='__main__':unittest.main()
