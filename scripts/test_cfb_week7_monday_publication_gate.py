import unittest
from pathlib import Path
import cfb_week7_monday_publication_gate as gate

class MondayPublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=Path('evidence/operational')
        cls.sheet=(root/'CFB_WEEK7_HOT_SHEET_2026-10-12_1828CT.md').read_text()
        cls.inputs=[(root/p).read_text() for p in ['CFB_MARKET_MONITOR_STATE.md','CFB_DECISION_WAIT_LEDGER.md','CFB_EXECUTION_LEDGER.md','CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md','CFB_WEEK7_HOT_SHEET_2026-10-12_0707CT.md','CFB_WEEK7_ORIGINAL_FIRST_FROZEN_LINEAGE_2026-10-11.json']]
    def reject(self,sheet):
        with self.assertRaises(ValueError):gate.audit(sheet,*self.inputs)
    def test_real_corrected_projection(self):
        r=gate.audit(self.sheet,*self.inputs)
        self.assertEqual((r['games'],r['updated_fallbacks'],r['withheld_conflicts'],r['monday_quote_unavailable']),(62,5,3,7))
    def test_original_readiness_contradiction_rejected(self):
        self.reject(Path('evidence/operational/CFB_WEEK7_HOT_SHEET_2026-10-12_1305CT.md').read_text())
    def test_missing_game(self):self.reject('\n'.join(l for l in self.sheet.splitlines() if not l.startswith('| Tue Oct 13 6:00 PM CT |')))
    def test_duplicate_game(self):
        row=next(l for l in self.sheet.splitlines() if l.startswith('| Tue Oct 13 6:00 PM CT |'))
        self.reject(self.sheet.replace(row,row+'\n'+row))
    def test_wrong_section(self):self.reject(self.sheet.replace('## TUESDAY','## THURSDAY',1))
    def test_unknown_identity(self):self.reject(self.sheet.replace('Delaware @ Middle Tenn.','Another @ Middle Tenn.'))
    def test_frozen_number_change(self):self.reject(self.sheet.replace('Middle Tennessee -1.8 / 50.6','Middle Tennessee -1.9 / 50.6'))
    def test_changed_accepted_price(self):self.reject(self.sheet.replace('FIU +3 -115, ML +120','FIU +3 -116, ML +120'))
    def test_conflict_made_current(self):self.reject(self.sheet.replace('Delaware -2.5 -110, ML -135','Delaware -1.5 -112, ML +102'))
    def test_retained_quote_relabelled_new(self):self.reject(self.sheet.replace('single-book fallback 07:07 CT','single-book fallback 13:05 CT'))
    def test_movement_erasure(self):self.reject(self.sheet.replace('First 07:08 CT:','First 13:05 CT:',1))
    def test_action_invented(self):self.reject(self.sheet.replace('INCONCLUSIVE — Monday afternoon recheck','BET NOW — Monday afternoon recheck',1))
    def test_cutoff_promoted(self):self.reject(self.sheet.replace('CUTOFF_AUTHORITY_UNVERIFIED','VERIFIED_CUTOFF',1))
    def test_consensus_invented(self):self.reject(self.sheet.replace('CONSENSUS_UNAVAILABLE; Caesars UNVERIFIED; DraftKings','QUALIFIED_CONSENSUS; Caesars UNVERIFIED; DraftKings',1))
    def test_caesars_verified(self):self.reject(self.sheet.replace('Caesars UNVERIFIED; DraftKings','Caesars VERIFIED; DraftKings',1))
    def test_saved_clock_label_required(self):self.reject(self.sheet.replace('This is a presentation correction only; quote retrieval remains 13:05 CT','Fresh quotes captured 18:28 CT'))
    def test_new_source_boundary_rejected(self):
        args=self.inputs.copy();args[0]+='\nNew cycle\n'
        with self.assertRaises(ValueError):gate.audit(self.sheet,*args)
    def test_unknown_cycle_rejected(self):self.reject(self.sheet.replace(gate.CYCLE,'CFB_MARKET_MONITOR_20261013T120000Z'))
    def test_binding_stale(self):self.reject(self.sheet.replace(gate.DECISION_SHA,'0'*40))
    def test_execution_invented(self):self.reject(self.sheet.replace('Not established; no executable recommendation','$5 execute now',1))

if __name__=='__main__':unittest.main()
