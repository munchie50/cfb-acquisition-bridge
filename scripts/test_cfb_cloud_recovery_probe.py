"""Actual process termination over synthetic responses; no external requests."""
import json
from pathlib import Path
import tempfile
import unittest
import cfb_cloud_recovery_probe as probe
from cfb_cloud_source_prepare import digest


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.out = Path(self.tmp.name) / 'capture'
        self.spec = {'schema': 'CFB_CLOUD_SOURCE_INPUT_V1', 'authority_ref': 'synthetic',
                     'game_ids': ['one', 'two'], 'allowed_hosts': ['example.org'],
                     'sources': [{'id': g, 'url': 'https://example.org/' + g,
                                  'game_ids': [g], 'kind': 'football_material'} for g in ('one', 'two')]}
        self.raw = json.dumps(self.spec).encode(); self.sha = digest(self.raw)
        self.calls = []
        self.now = '2026-10-30T02:00:00+00:00'

    def fetch(self, url, hosts):
        self.calls.append(url)
        return url.encode(), {'http_status': 200, 'final_url': url}

    def capture(self):
        return probe.capture(self.raw, self.sha, self.out, fetch=self.fetch, clock=lambda: self.now)

    def restore(self, commit='LOCAL_TEST'):
        return probe.restore(self.raw, self.sha, self.out, commit,
                             fetch=self.fetch, clock=lambda: self.now)

    def test_actual_sigterm_then_restore_fetches_only_unfinished_source(self):
        captured = self.capture()
        self.assertEqual(captured['worker_exitcode'], -15)
        self.assertEqual(captured['remaining_sources'], 1)
        restored = self.restore()
        self.assertEqual(self.calls, ['https://example.org/two'])
        self.assertEqual(restored['reused_sources'], 1)
        self.assertEqual(restored['newly_fetched_sources'], 1)
        self.assertTrue(restored['original_source_clock_preserved'])

    def test_wrong_source_commit_and_modified_manifest_rejected(self):
        self.capture()
        with self.assertRaisesRegex(ValueError, 'mismatch'): self.restore('wrong')
        p = self.out / 'partial/manifest.json'; p.write_text(p.read_text()+' ')
        with self.assertRaisesRegex(ValueError, 'mismatch'): self.restore()

    def test_expired_checkpoint_does_not_prove_recovery(self):
        self.capture(); self.now = '2026-10-30T03:00:00+00:00'
        with self.assertRaisesRegex(ValueError, 'expired or damaged'): self.restore()

    def test_raw_tampering_blocks_reuse_proof(self):
        r = self.capture()
        (self.out / 'partial' / r['original_source']['artifact']).write_bytes(b'tamper')
        with self.assertRaisesRegex(ValueError, 'expired or damaged'): self.restore()


if __name__ == '__main__': unittest.main()
