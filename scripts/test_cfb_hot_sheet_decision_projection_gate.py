import unittest
from unittest.mock import patch
import cfb_hot_sheet_decision_projection_gate as g

GAMES=['Away'+str(i)+' @ '+(['App State','Massachusetts','Fresno State'][i] if i<3 else 'Home'+str(i)) for i in range(38)]
BET='BET NOW CONDITIONAL — CONTROLLED BETA'

def inputs():
    states={game:(BET if i<3 else 'PASS','PASS') for i,game in enumerate(GAMES)}
    ledger=g.MARKER+'\nApp State -10 or better; UMass +4.5 or better; Fresno State +7 or better; each maximum -115\n'
    ledger+=''.join('| '+game+' | '+s+' | '+t+' |\n' for game,(s,t) in states.items())
    cards=[('App State -10','-10 or better'),('UMass +4.5','+4.5 or better'),('Fresno State +7','+7 or better')]
    review=''.join('| Sat noon | '+sel+' | fair | benchmark | '+line+' | -115 | Conditional |\n' for sel,line in cards)
    review_rows=[["time",game,"fair","away","home","total",s,t,"gap"] for game,(s,t) in states.items()]
    sheet='Canonical inputs: market '+'a'*40+'; decision '+g.blob(ledger)+'.\nNO NEW MARKET RETRIEVAL\nUnderlying quote retrieval remains approximately 13:02 CT\n'
    for i,(game,(s,t)) in enumerate(states.items()):
        reason='Caesars offer UNVERIFIED' if i<3 else 'PASS reason'
        cutoff=cards[i][1]+'; max -115; tonight before kickoff; actual Caesars check' if i<3 else 'None / PASS'
        sheet+='| Sat 1:00 PM | '+game+' | fair | quote | move | '+s+' / TOTAL '+t+' | '+reason+' | resolved | '+cutoff+' |\n'
    return sheet,'baseline',review,ledger,review_rows

class ProjectionTests(unittest.TestCase):
    def run_audit(self,transform=lambda x:x):
        data=list(inputs());data=transform(data)
        # Scope is independently checked by its own genuine baseline/38-row suite.
        with patch.object(g,'expected_games',return_value=GAMES),patch.object(g,'check'),patch.object(g,'review_rows',return_value=data[4]):
            return g.audit(*data[:4])
    def test_exact_states_cutoffs_keep_unverified_scope(self):
        r=self.run_audit();self.assertEqual(r['matched_market_verdicts'],76)
        self.assertEqual(r['matched_conditional_cutoffs'],3)
        self.assertIn('unverified',r['scope'])
    def test_stale_inconclusive_rejected(self):
        def change(x):x[0]=x[0].replace(BET+' / TOTAL PASS','INCONCLUSIVE / TOTAL PASS',1);return x
        with self.assertRaisesRegex(ValueError,'stale or changed'):self.run_audit(change)
    def test_total_verdict_drift_rejected(self):
        def change(x):x[0]=x[0].replace('/ TOTAL PASS','/ TOTAL BET NOW',1);return x
        with self.assertRaises(ValueError):self.run_audit(change)
    def test_conditional_label_cannot_be_removed(self):
        def change(x):x[0]=x[0].replace(BET+' / TOTAL PASS','BET NOW / TOTAL PASS',1);return x
        with self.assertRaises(ValueError):self.run_audit(change)
    def test_line_cutoff_cannot_be_loosened(self):
        def change(x):x[0]=x[0].replace('-10 or better; max','-11 or better; max',1);return x
        with self.assertRaisesRegex(ValueError,'cutoff changed'):self.run_audit(change)
    def test_price_cap_cannot_be_loosened(self):
        def change(x):x[0]=x[0].replace('max -115','max -120',1);return x
        with self.assertRaises(ValueError):self.run_audit(change)
    def test_unverified_counter_label_required(self):
        def change(x):x[0]=x[0].replace('Caesars offer UNVERIFIED','Caesars verified',1);return x
        with self.assertRaisesRegex(ValueError,'qualifier missing'):self.run_audit(change)
    def test_old_quote_cannot_claim_refresh(self):
        def change(x):x[0]=x[0].replace('NO NEW MARKET RETRIEVAL','Fresh live quote');return x
        with self.assertRaises(ValueError):self.run_audit(change)
    def test_saved_decision_blob_required(self):
        def change(x):x[0]=x[0].replace(g.blob(x[3]),'f'*40);return x
        with self.assertRaisesRegex(ValueError,'binding'):self.run_audit(change)
    def test_report_cannot_invent_different_canonical_cutoff(self):
        def change(x):x[2]=x[2].replace('App State -10','App State -11').replace('-10 or better','-11 or better');return x
        with self.assertRaisesRegex(ValueError,'canonical decision'):self.run_audit(change)
    def test_later_ledger_block_not_silently_ignored(self):
        data=list(inputs());data[3]+='\n## Later material decisions\nChanged.'
        with self.assertRaisesRegex(ValueError,'later decision block'):g.decisions(data[3],set(GAMES))

if __name__=='__main__':unittest.main()
