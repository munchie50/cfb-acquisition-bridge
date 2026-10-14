import copy,json,re,unittest
from pathlib import Path
import cfb_cbs_full_board_normalizer as gate

FIXTURE=Path('evidence/scheduler_qa/CFB_CBS_FULL_BOARD_TABLES_20261014T225920Z.md')
LINEAGE=Path('evidence/operational/CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json')
AT='2026-10-14T22:59:20Z'
class BoardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.raw=FIXTURE.read_text();cls.lineage=LINEAGE.read_text()
    def run_board(self,raw=None,at=AT):return gate.normalize(self.raw if raw is None else raw,self.lineage,at)
    def reject(self,raw):
        with self.assertRaises(ValueError):self.run_board(raw)
    def test_actual_complete_response(self):
        r=self.run_board();self.assertEqual(r['coverage'],{'governed_games':62,'matched_games':62,'source_team_rows':124,'future_games':60,'future_team_rows':120,'past_or_started_games':2,'missing_game_ids':[]})
        self.assertEqual(sum(v['availability']=='DISPLAYED' for g in r['games'] if g['temporal_status']=='FUTURE_AT_CAPTURE' for t in g['team_offers'] for k,v in t.items() if k!='team'),360)
    def test_85_team_excerpt_rejected(self):
        lines=[];n=0
        for l in self.raw.splitlines():
            if l.startswith('| [![team logo]'):n+=1
            if n>85:break
            lines.append(l)
        self.reject('\n'.join(lines))
    def test_one_missing_team(self):
        row=next(l for l in self.raw.splitlines() if l.startswith('| [![team logo]'));self.reject(self.raw.replace(row,'',1))
    def test_duplicate_game(self):
        first=self.raw.split('\n\n')[0];self.reject(first+'\n\n'+self.raw)
    def test_duplicate_same_team(self):
        ls=self.raw.splitlines();rows=[i for i,l in enumerate(ls) if l.startswith('| [![team logo]')];ls[rows[1]]=ls[rows[0]];self.reject('\n'.join(ls))
    def test_reversed_pair(self):
        ls=self.raw.splitlines();rows=[i for i,l in enumerate(ls) if l.startswith('| [![team logo]')];a,b=rows[:2];ls[a],ls[b]=ls[b],ls[a];self.reject('\n'.join(ls))
    def test_wrong_column_order(self):self.reject(self.raw.replace('| Final | Open | Spread | MLMoneyline | Total |','| Final | Open | Total | MLMoneyline | Spread |',1))
    def test_final_and_open_quarantined(self):
        ls=self.raw.splitlines()
        for i,l in enumerate(ls):
            if l.startswith('| [![team logo]'):
                c=gate.cells(l);c[1]='999999 SOURCE_CONFLICT';c[2]='-9999 -9999 unrelated opening reference';ls[i]='| '+' | '.join(c)+' |'
        a=self.run_board();b=self.run_board('\n'.join(ls));self.assertEqual(a['games'],b['games'])
    def test_nebraska_timezone(self):
        g=next(g for g in self.run_board()['games'] if g['away_team']=='Nebraska');self.assertEqual(g['source_kickoff_utc'],'2026-10-18T03:00:00Z')
    def test_past_tuesday_clock_not_invented(self):
        past=[g for g in self.run_board()['games'] if g['temporal_status']!='FUTURE_AT_CAPTURE'];self.assertEqual(len(past),2);self.assertTrue(all(g['source_kickoff_utc'] is None for g in past))
    def test_date_without_time_not_current_inferred(self):self.reject(self.raw.replace('| Wed Oct 14, 7:30pm<br> <br> Wed 7:30pm |','| Wed Oct 14 |',1))
    def test_bad_weekday(self):self.reject(self.raw.replace('Wed Oct 14, 7:30pm','Thu Oct 14, 7:30pm',1))
    def test_book_icons_never_consensus(self):
        r=self.run_board();ids={v['opaque_book_icon_id'] for g in r['games'] for t in g['team_offers'] for k,v in t.items() if k!='team'};self.assertEqual(ids,{'30','34','35',None});self.assertEqual(r['consensus'],'CONSENSUS_UNAVAILABLE');self.assertEqual(r['caesars'],'UNVERIFIED')
    def test_asymmetric_sides_preserved(self):
        g=next(g for g in self.run_board()['games'] if g['away_team']=='East Carolina');self.assertEqual([t['spread']['line'] for t in g['team_offers']],[-4.5,5.5])
    def test_asymmetric_total_endpoints_preserved(self):
        g=self.run_board()['games'][0];self.assertEqual([t['total']['line'] for t in g['team_offers']],[52.5,53.5])
    def test_bad_price(self):self.reject(self.raw.replace('-112<br> <br>Remove','-12<br> <br>Remove',1))
    def test_truncated_price_pair(self):self.reject(self.raw.replace('-2.5<br> <br> -112','-2.5',1))
    def test_multiple_book_icons(self):
        x='![book logo](https://sports.cbsimg.net/fly/images/books-icons/30.svg)';self.reject(self.raw.replace(x,x+x,1))
    def test_lineage_changed(self):
        with self.assertRaises(ValueError):gate.normalize(self.raw,self.lineage+'\n',AT)
    def test_timezone_unqualified(self):
        with self.assertRaises(ValueError):gate.normalize(self.raw,self.lineage,AT,source_timezone='UTC')
    def test_page_identity_unqualified(self):
        with self.assertRaises(ValueError):gate.normalize(self.raw,self.lineage,AT,source_url=gate.URL.replace('week-7','week-8'))
    def test_naive_capture_time(self):
        with self.assertRaises(ValueError):self.run_board(at='2026-10-14T22:59:20')
    def test_missing_market_remains_null(self):
        self.assertEqual(gate.market('—','total'),{'availability':'UNAVAILABLE','line':None,'price':None,'side':None,'opaque_book_icon_id':None})
    def test_spread_not_total(self):
        with self.assertRaises(ValueError):gate.market('o52.5 -110','spread')
    def test_unknown_ml(self):
        with self.assertRaises(ValueError):gate.market('EVEN','moneyline')

if __name__=='__main__':unittest.main()
