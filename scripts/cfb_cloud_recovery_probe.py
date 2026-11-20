"""Controlled worker SIGTERM and cross-run restore proof, QA only.

The Actions job survives to upload the partial artifact. This does not prove
artifact survival after cancelling or abruptly killing the entire Actions job.
"""
import argparse
import json
import multiprocessing
import os
from pathlib import Path
import signal
import time
from cfb_cloud_source_prepare import (atomic_json, digest, download, prepare,
                                      reusable, utc, validate)


def capture(raw, expected, output, fetch=download, clock=utc):
    spec = validate(raw, expected)
    if len(spec['sources']) < 2:
        raise ValueError('at least two sources required for interrupted-work proof')
    output = Path(output)
    if output.exists():
        raise ValueError('capture must start in a new directory')
    output.mkdir(parents=True)
    partial, marker = output / 'partial', output / 'intentional-stall.json'

    def child():
        def controlled_fetch(url, hosts):
            if url != spec['sources'][0]['url']:
                atomic_json(marker, {'phase': 'BEFORE_SECOND_NETWORK_REQUEST', 'clock': clock()})
                time.sleep(120)  # Parent must terminate this actual worker process.
                raise RuntimeError('parent did not terminate probe')
            return fetch(url, hosts)
        prepare(raw, expected, partial, workers=1, fetch=controlled_fetch, clock=clock)

    process = multiprocessing.get_context('fork').Process(target=child)
    process.start()
    limit = time.monotonic() + 60
    manifest = partial / 'manifest.json'
    try:
        while time.monotonic() < limit and process.is_alive():
            if marker.exists() and manifest.exists():
                state = json.loads(manifest.read_text())
                if len(state['sources']) == 1:
                    if state['sources'][0]['status'] != 'FETCHED_UNREVIEWED':
                        raise ValueError('first source failed; cannot prove completed-work reuse')
                    process.terminate()
                    process.join(10)
                    if process.is_alive() or process.exitcode != -signal.SIGTERM:
                        raise ValueError('actual worker SIGTERM not demonstrated')
                    state = json.loads(manifest.read_text())
                    if state['status'] != 'PREPARATION_INCOMPLETE':
                        raise ValueError('interrupted checkpoint must remain incomplete')
                    row = state['sources'][0]
                    if not reusable(row, spec['sources'][0], partial, clock(), 900):
                        raise ValueError('interrupted checkpoint lacks intact fresh source')
                    result = {'schema': 'CFB_CONTROLLED_WORKER_INTERRUPTION_V1',
                              'recorded_at_utc': clock(), 'input_sha256': expected,
                              'capture_commit': os.environ.get('GITHUB_SHA', 'LOCAL_TEST'),
                              'worker_exitcode': process.exitcode, 'signal': 'SIGTERM',
                              'completed_sources': 1, 'remaining_sources': len(spec['sources'])-1,
                              'original_source': row,
                              'partial_manifest_sha256': digest(manifest.read_bytes()),
                              'scope': 'ACTUAL_WORKER_TERMINATED_JOB_SURVIVED_NOT_WHOLE_JOB_CANCELLATION'}
                    atomic_json(output / 'capture-proof.json', result)
                    return result
            time.sleep(0.05)
        raise ValueError('no usable partial checkpoint before probe deadline')
    finally:
        if process.is_alive():
            process.kill()
        process.join(10)


def restore(raw, expected, output, source_commit, fetch=download, clock=utc):
    spec = validate(raw, expected)
    output = Path(output)
    evidence = json.loads((output / 'capture-proof.json').read_text())
    partial = output / 'partial'
    manifest = partial / 'manifest.json'
    if (evidence['input_sha256'] != expected or evidence['capture_commit'] != source_commit
            or evidence['worker_exitcode'] != -signal.SIGTERM
            or digest(manifest.read_bytes()) != evidence['partial_manifest_sha256']):
        raise ValueError('capture identity, signal or checkpoint digest mismatch')
    saved = evidence['original_source']
    if not reusable(saved, spec['sources'][0], partial, clock(), 900):
        raise ValueError('expired or damaged capture: no cross-run reuse claim permitted')
    result = prepare(raw, expected, partial, workers=4, fetch=fetch, clock=clock)
    row = next(r for r in result['sources'] if r['id'] == saved['id'])
    if (row['status'] != 'REUSED_UNREVIEWED' or row['sha256'] != saved['sha256']
            or row['response_recovered_by_utc'] != saved['response_recovered_by_utc']):
        raise ValueError('saved completed source not exactly preserved')
    proof = {'schema': 'CFB_CLOUD_CROSS_RUN_RESTORE_V1', 'recorded_at_utc': clock(),
             'capture_commit': source_commit, 'restore_commit': os.environ.get('GITHUB_SHA', 'LOCAL_TEST'),
             'input_sha256': expected, 'reused_sources': result['reused_sources'],
             'newly_fetched_sources': result['fetched_sources'], 'failed_sources': result['failed_sources'],
             'status': result['status'], 'original_source_clock_preserved': True,
             'original_source_hash_preserved': True,
             'scope': 'QA_COLLECTION_RECOVERY_ONLY_NOT_FOOTBALL_OR_PRODUCTION_RELIABILITY'}
    atomic_json(output / 'restore-proof.json', proof)
    return proof


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode', choices=['capture', 'restore'])
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--expected-sha256', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--source-commit')
    a = p.parse_args()
    if a.mode == 'capture':
        result = capture(a.input.read_bytes(), a.expected_sha256, a.output)
    else:
        if not a.source_commit: p.error('restore requires exact source-commit')
        result = restore(a.input.read_bytes(), a.expected_sha256, a.output, a.source_commit)
    print(json.dumps(result, indent=2))
    if result.get('failed_sources', 0): raise SystemExit(2)
