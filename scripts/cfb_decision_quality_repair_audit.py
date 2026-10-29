"""Read-only retained-evidence diagnostic; never issues or certifies a decision."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


def blob(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def clock(value):
    result = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if result.tzinfo is None:
        raise ValueError('timezone-aware evidence boundary required')
    return result


def cases(packet):
    rows = packet['cases']
    result = {r['game_id']: r for r in rows}
    if len(result) != len(rows):
        raise ValueError('duplicate game identity')
    if len(result) != packet['source_coverage']['governed_games']:
        raise ValueError('incomplete evidence population')
    return result


def branch_values(row):
    branches = row.get('branches', [])
    result = {b['branch']: (b['line'], b['price']) for b in branches}
    if len(result) != len(branches):
        raise ValueError('duplicate market branch')
    return result


def audit(prior, current):
    if clock(prior['as_of_utc']) >= clock(current['as_of_utc']):
        raise ValueError('comparison must advance evidence boundary')
    old, new = cases(prior), cases(current)
    if old.keys() != new.keys():
        raise ValueError('comparison populations differ')
    counts, findings = Counter(), []
    for gid, row in new.items():
        classification = row['classification']
        if classification == 'ORIGINAL_EXCLUSION_NO_RECOMMENDATION':
            category = 'original_exclusion'
        elif row['temporal_status'] != 'FUTURE_AT_CAPTURE':
            category = 'elapsed_history'
        elif classification in ('EXPIRED_UNPUBLISHED_NO_REOPEN', 'EXPIRED_CONDITIONAL_HISTORY_ONLY'):
            category = 'closed_review_history'
        elif row['state'] == 'PASS':
            category = 'future_pass_recorded_not_semantically_certified'
        else:
            category = 'other_requires_individual_review'
        counts[category] += 1
        if category != 'future_pass_recorded_not_semantically_certified':
            continue
        previous = old[gid]
        before, after = branch_values(previous), branch_values(row)
        if len(after) != 6 or before.keys() != after.keys():
            raise ValueError('six comparable main-market branches required')
        changed = [key for key in after if before[key] != after[key]]
        explanation = row.get('current_value_judgement', '').strip()
        if not explanation:
            findings.append({'game_id': gid, 'game': row['away_team'] + ' @ ' + row['home_team'],
                             'finding': 'MISSING_VALUE_JUDGEMENT_REVIEW_REQUIRED'})
        elif changed and explanation == previous.get('current_value_judgement', '').strip():
            findings.append({'game_id': gid, 'game': row['away_team'] + ' @ ' + row['home_team'],
                             'finding': 'UNCHANGED_EXPLANATION_CHANGED_PRICES_REVIEW_REQUIRED',
                             'changed_branches': {key: {'prior': before[key], 'current': after[key]}
                                                  for key in changed},
                             'retained_explanation': explanation})
    return {'status': 'DIAGNOSTIC_COMPLETE_REPAIR_AND_SEMANTIC_REVIEW_PENDING',
            'prior_boundary': prior['as_of_utc'], 'current_evidence_boundary': current['as_of_utc'],
            'population': len(new), 'separated_counts': dict(counts), 'findings': findings,
            'limitations': [
                'A repeated explanation at changed prices is a review flag, not proof the PASS is wrong.',
                'No flag does not certify football facts, comparative judgment or value.',
                'This retained replay does not refresh markets, reopen windows, or qualify a wager.',
                'No production files, tasks, limits, models or money are changed.',
                'The automated job stops after diagnostics; coding and human/agent review remain pending.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prior', type=Path, required=True)
    parser.add_argument('--current', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.resolve() in (args.prior.resolve(), args.current.resolve()):
        parser.error('output must not overwrite evidence')
    before, after = args.prior.read_bytes(), args.current.read_bytes()
    result = audit(json.loads(before), json.loads(after))
    result['input_bindings'] = [{'path': str(path), 'git_blob': blob(raw)}
                                for path, raw in ((args.prior, before), (args.current, after))]
    result['recorded_at_utc'] = datetime.now(timezone.utc).isoformat()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'population': result['population'],
                      'counts': result['separated_counts'], 'review_flags': len(result['findings'])}))


if __name__ == '__main__':
    main()
