"""Boundary tests for QA source preparation; no live source requests."""
import copy
import fcntl
import json
from pathlib import Path
import tempfile
import unittest
import cfb_cloud_source_prepare as worker


class PreparationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.out = Path(self.tmp.name)
        self.now = '2026-10-30T02:00:00+00:00'
        self.spec = {'schema': worker.SCHEMA, 'authority_ref': 'synthetic test only',
                     'game_ids': ['one', 'two'], 'allowed_hosts': ['example.org'],
                     'sources': [{'id': g, 'url': 'https://example.org/' + g,
                                  'kind': 'football_material', 'game_ids': [g]}
                                 for g in ('one', 'two')]}
        self.calls = []

    def fetch(self, url, hosts):
        self.calls.append(url)
        return url.encode(), {'http_status': 200, 'final_url': url, 'content_type': 'text/html'}

    def run_worker(self, **kw):
        raw = json.dumps(self.spec).encode()
        return worker.prepare(raw, worker.digest(raw), self.out, fetch=kw.pop('fetch', self.fetch),
                              clock=lambda: self.now, **kw)

    def test_completed_collection_remains_unreviewed_and_has_full_declared_population(self):
        r = self.run_worker()
        self.assertEqual(r['status'], 'COLLECTION_COMPLETE_UNREVIEWED')
        self.assertEqual(r['games_without_fetched_link'], [])
        self.assertFalse(r['canonical_mutation'])
        self.assertEqual(r['football_analysis'], 'NOT_PERFORMED')

    def test_resume_reuses_verified_bytes_without_changing_original_clock(self):
        first = self.run_worker()
        self.calls.clear(); self.now = '2026-10-30T02:05:00+00:00'
        result = self.run_worker()
        self.assertEqual(self.calls, [])
        self.assertEqual(result['reused_sources'], 2)
        self.assertEqual([r['response_recovered_by_utc'] for r in first['sources']],
                         [r['response_recovered_by_utc'] for r in result['sources']])

    def test_stale_and_future_clocks_are_refetched(self):
        self.run_worker()
        self.calls.clear(); self.now = '2026-10-30T03:00:00+00:00'
        self.assertEqual(self.run_worker()['fetched_sources'], 2)
        self.calls.clear(); self.now = '2026-10-30T02:30:00+00:00'
        self.assertEqual(self.run_worker()['fetched_sources'], 2)

    def test_corrupt_cache_refetches_only_affected_source(self):
        first = self.run_worker(); self.calls.clear()
        (self.out / first['sources'][0]['artifact']).write_bytes(b'tampered')
        result = self.run_worker()
        self.assertEqual(result['fetched_sources'], 1)
        self.assertEqual(result['reused_sources'], 1)

    def test_source_failure_is_checkpointed_and_only_failed_source_retried(self):
        def sometimes(url, hosts):
            if url.endswith('/two'): raise TimeoutError()
            return self.fetch(url, hosts)
        first = self.run_worker(fetch=sometimes)
        self.assertEqual(first['status'], 'PREPARATION_INCOMPLETE')
        self.assertEqual(first['games_without_fetched_link'], ['two'])
        self.calls.clear()
        result = self.run_worker()
        self.assertEqual(self.calls, ['https://example.org/two'])
        self.assertEqual(result['reused_sources'], 1)

    def test_partial_checkpoint_resumes_without_inventing_missing_success(self):
        self.run_worker()
        p = self.out / 'manifest.json'; old = json.loads(p.read_text())
        old['sources'] = old['sources'][:1]; old['status'] = 'PREPARATION_INCOMPLETE'
        p.write_text(json.dumps(old)); self.calls.clear()
        result = self.run_worker()
        self.assertEqual(result['fetched_sources'], 1)
        self.assertEqual(result['reused_sources'], 1)

    def test_changed_approved_input_cannot_mix_with_checkpoint(self):
        self.run_worker(); self.spec['authority_ref'] = 'another boundary'
        with self.assertRaisesRegex(ValueError, 'different approved input'): self.run_worker()

    def test_bad_hash_and_missing_coverage_rejected_before_fetch(self):
        raw = json.dumps(self.spec).encode()
        with self.assertRaisesRegex(ValueError, 'SHA-256'): worker.validate(raw, 'bad')
        self.spec['sources'].pop()
        with self.assertRaisesRegex(ValueError, 'lacks source links'): self.run_worker()
        self.assertEqual(self.calls, [])

    def test_duplicate_ids_urls_and_unknown_population_rejected(self):
        for field, value in [('id', 'one'), ('url', 'https://example.org/one'),
                             ('game_ids', ['unknown'])]:
            original = copy.deepcopy(self.spec)
            self.spec['sources'][1][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError): self.run_worker()
            self.spec = original

    def test_unsafe_urls_and_redirects_rejected(self):
        for url in ('http://example.org/x', 'https://user:pass@example.org/x',
                    'https://localhost/x', 'https://127.0.0.1/x', 'https://example.org:444/x',
                    'https://not-approved.org/x'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                worker.url_host(url, ['example.org', '127.0.0.1', 'localhost'])
        def redirect(url, hosts):
            return b'body', {'http_status': 200, 'final_url': 'https://other.org/'}
        self.assertEqual(self.run_worker(fetch=redirect)['failed_sources'], 2)

    def test_empty_oversized_and_non200_are_failures(self):
        for data, status in ((b'', 200), (b'x'*(worker.LIMIT+1), 200), (b'body', 503)):
            def bad(url, hosts): return data, {'final_url': url, 'http_status': status}
            with self.subTest(status=status, size=len(data)):
                self.assertEqual(self.run_worker(fetch=bad)['status'], 'PREPARATION_INCOMPLETE')

    def test_lock_and_bounds_prevent_competing_or_unbounded_workers(self):
        with (self.out / '.prepare.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaises(BlockingIOError): self.run_worker()
        for args in ({'workers': 5}, {'max_age': 3601}, {'workers': 0}):
            with self.subTest(args=args), self.assertRaises(ValueError): self.run_worker(**args)

    def test_cache_zero_forces_fresh_fetch(self):
        self.run_worker(); self.calls.clear()
        self.assertEqual(self.run_worker(max_age=0)['fetched_sources'], 2)


if __name__ == '__main__': unittest.main()
