import unittest
from cfb_hot_sheet_required_outputs_gate import check
class GateTests(unittest.TestCase):
 def test_missing(self):
  self.assertEqual(check('## FRIDAY\n## FULL SLATE')['missing'], ['TOP 10','PARLAY'])
 def test_present(self):
  self.assertEqual(check('## TOP 10\n## PARLAY\n## FULL SLATE')['status'],'PRESENTATION_ONLY_PASS')
 def test_not_acceptance(self):
  self.assertIn('NOT_PRODUCER_ACCEPTANCE',check('TOP 10 PARLAY FULL SLATE')['scope'])
if __name__=='__main__': unittest.main()
