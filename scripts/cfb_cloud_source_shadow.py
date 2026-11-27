"""QA source-plan shadow collection and separate raw-source role accounting."""
import argparse
import json
from pathlib import Path
from cfb_cloud_source_prepare import (atomic_json, digest, download, prepare,
                                      reusable, utc, validate)


def role_report(plan, raw, result, output, as_of):
    if result['input_sha256'] != digest(raw):
        raise ValueError('worker result is bound to another plan')
    expected = {s['id']: s for s in plan['sources']}
    rows = {s['id']: s for s in result['sources']}
    if len(rows) != len(result['sources']) or rows.keys() != expected.keys():
        raise ValueError('worker result population differs from plan')
    linked = {'market_board': set(), 'football_material': set()}
    invalid, failed = [], []
    for sid, row in rows.items():
        source = expected[sid]
        if any(row.get(k) != source[k] for k in ('url', 'kind', 'game_ids')):
            raise ValueError('worker source association changed')
        if row['status'] == 'UNAVAILABLE_NOT_A_PASS':
            failed.append({'id': sid, 'url': row['url'], 'kind': row['kind'],
                           'game_ids': row['game_ids'], 'error_type': row.get('error_type')})
        elif reusable(row, source, Path(output), as_of, 900):
            linked[row['kind']].update(row['game_ids'])
        else:
            invalid.append(sid)
    required = set(plan['source_role_coverage']['football_required_game_ids'])
    missing = sorted(required-linked['football_material'])
    complete = not failed and not invalid and not missing and linked['market_board'] == set(plan['game_ids'])
    return {'schema': 'CFB_SOURCE_ROLE_SHADOW_QA_V1', 'recorded_at_utc': as_of,
            'input_sha256': digest(raw), 'authority_commit': plan['authority_ref'],
            'index_blob': plan['index_blob'],
            'saved_review_boundary_utc': plan['source_role_coverage']['saved_review_boundary_utc'],
            'status': 'COMPLETE_UNREVIEWED_COLLECTION_ONLY' if complete else 'INCOMPLETE_UNREVIEWED_NOT_A_PASS',
            'planned_sources': len(expected), 'fetched_sources': result['fetched_sources'],
            'reused_sources': result['reused_sources'], 'failed_sources': failed,
            'invalid_or_stale_raw_source_ids': invalid,
            'governed_games': len(plan['game_ids']), 'market_raw_linked_games': len(linked['market_board']),
            'football_required_saved_active_games': len(required),
            'football_raw_linked_saved_active_games': len(required & linked['football_material']),
            'active_games_without_fetched_football_source': missing,
            'collector_elapsed_seconds': result['elapsed_seconds'],
            'football_analysis': 'NOT_PERFORMED', 'quote_or_source_semantic_freshness': 'NOT_CERTIFIED',
            'production_publication_or_model_change': False,
            'limitations': ['HTTP success and role associations do not qualify text, matchup, medical facts or prices.',
                'Saved active game population is as-of the accepted review, not independently re-established current eligibility.',
                'No whole-Monitor timing comparison, analytical quality or natural-production reliability claim.']}


def shadow(raw, expected, output, workers=4, fetch=download, clock=utc):
    plan = validate(raw, expected)
    if plan['source_role_coverage']['status'] != 'READY_FOR_UNREVIEWED_COLLECTION_ONLY':
        raise ValueError('incomplete source plan must be resolved before shadow fetching')
    result = prepare(raw, expected, output, workers=workers, fetch=fetch, clock=clock)
    report = role_report(plan, raw, result, output, clock())
    atomic_json(Path(output)/'role-coverage.json', report)
    return report


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--expected-sha256', required=True)
    p.add_argument('--output', type=Path, required=True)
    p.add_argument('--workers', type=int, default=4)
    a = p.parse_args()
    r = shadow(a.input.read_bytes(), a.expected_sha256, a.output, a.workers)
    print(json.dumps(r, indent=2))
    raise SystemExit(0 if r['status'] == 'COMPLETE_UNREVIEWED_COLLECTION_ONLY' else 2)
