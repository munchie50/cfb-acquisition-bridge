"""Measure collector time only; never infer whole-Monitor or analytical savings."""
import argparse
import json
from pathlib import Path
from cfb_cloud_source_prepare import prepare, atomic_json


def benchmark(raw, expected, output):
    root = Path(output)
    serial = prepare(raw, expected, root / 'serial', workers=1, max_age=0)
    parallel = prepare(raw, expected, root / 'parallel', workers=4, max_age=0)
    resumed = prepare(raw, expected, root / 'parallel', workers=4, max_age=900)
    good = lambda r: sorted(s['id'] for s in r['sources'] if s['status'] != 'UNAVAILABLE_NOT_A_PASS')
    timings = {k: r['elapsed_seconds'] for k, r in
               [('serial', serial), ('parallel', parallel), ('resumed', resumed)]}
    result = {'schema': 'CFB_CLOUD_SOURCE_TIMING_QA_V1', 'input_sha256': expected,
              'timings_seconds': timings,
              'serial_successful_sources': good(serial), 'parallel_successful_sources': good(parallel),
              'comparable_fetch_statuses': good(serial) == good(parallel),
              'all_sources_fetched_both': serial['failed_sources'] == parallel['failed_sources'] == 0,
              'parallel_speedup_ratio': round(timings['serial']/timings['parallel'], 3)
                  if timings['parallel'] else None,
              'resume_fetched_sources': resumed['fetched_sources'],
              'resume_reused_sources': resumed['reused_sources'],
              'resume_failed_sources': resumed['failed_sources'],
              'limitations': ['One small collector-only measurement; not a production estimate.',
                  'Fixed retained URL fixture is not dynamic current-week discovery or complete football coverage.',
                  'Source contents may change between samples; retrieval does not certify their facts.',
                  'No model, decisions, canonical writes, publication, paid acquisition or schedule mutation.']}
    atomic_json(root / 'benchmark.json', result)
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--expected-sha256', required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    print(json.dumps(benchmark(a.input.read_bytes(), a.expected_sha256, a.output), indent=2))
