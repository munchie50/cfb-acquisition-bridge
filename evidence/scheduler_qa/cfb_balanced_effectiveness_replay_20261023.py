"""Read-only replay of the October23 balanced audit; no live/model/write path.

Run from the repository root. Historical snapshots are Git blobs, never current
mutable bytes silently used as historical evidence. Original image inspection
is human/model visual evidence in the intake manifest, not certified by this
numerical replay. No outcome is used to select a recommendation reference.
"""
import copy
import hashlib
import json
import re
import subprocess
from decimal import Decimal
from pathlib import Path

MANIFEST = 'evidence/operational/CFB_OCT17_ORIGINAL_TICKET_INTAKE_2026-10-23.json'
SCORE = 'evidence/operational/CFB_POSTGAME_FIRST_FROZEN_SCORECARD.md'
REVIEW = 'evidence/operational/CFB_WEEK7_COMPLETE_MULTI_MARKET_REVIEW_20261017T155337Z.json'
BASE_EXEC = '75caee4052e02ea7d2453d1d37fd3866e13ecc07'
EXPECTED_IDS = {'401858266', '401858490', '401856723', '401856722',
                '401858492', '401856831', '401858264', '401864524', '401856721'}


def blob(raw):
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def historical(sha):
    if not re.fullmatch('[0-9a-f]{40}', sha):
        raise ValueError('invalid Git blob')
    raw = subprocess.check_output(['git', 'cat-file', 'blob', sha])
    if blob(raw) != sha:
        raise ValueError('historical identity mismatch')
    return raw


def check(ok, message):
    if not ok:
        raise ValueError(message)


def audit(manifest):
    check(manifest['schema'] == 'CFB_OCT17_ORIGINAL_TICKET_INTAKE_V1', 'manifest schema')
    inputs = {p: historical(s) for p, s in manifest['input_blobs'].items()}
    check(manifest['input_blobs']['evidence/operational/CFB_EXECUTION_LEDGER.md'] == BASE_EXEC,
          'original execution boundary')
    review = json.loads(inputs[REVIEW])
    check(len(review['rows']) == 40 and review['counts']['core_ranked_games'] == 5,
          'qualified pre-event comparison population')
    prior = {r['game_id']: r for r in review['rows']}
    finals = {}
    for line in inputs[SCORE].decode().splitlines():
        c = [s.strip() for s in line.split('|')[1:-1]]
        if len(c) == 11 and c[0] in EXPECTED_IDS:
            check(c[0] not in finals, 'duplicate final identity')
            finals[c[0]] = c
    check(set(finals) == EXPECTED_IDS, 'complete exact final identity join')
    wagers = manifest['wagers']
    check(len(wagers) == 9 and {r['game_id'] for r in wagers} == EXPECTED_IDS, 'ticket population')
    check(len({r['execution_id'] for r in wagers}) == 9, 'duplicate ticket intake')
    check(len({r['image_sha256'] for r in wagers}) == 9, 'duplicate original image')
    check(len({r['source_library_file_id'] for r in wagers}) == 9, 'duplicate original source')
    out = []
    for r in wagers:
        check(r['execution_id'] not in inputs['evidence/operational/CFB_EXECUTION_LEDGER.md'].decode(),
              'ticket already in original ledger')
        check(r['classification'] == 'ACTUAL_REAL_MONEY' and r['budget_class'] == 'UNASSIGNED'
              and r['receipt_timezone'] == 'UNSPECIFIED', 'unearned ticket qualification')
        c = finals[r['game_id']]
        check(c[1] == r['game'] == prior[r['game_id']]['game'], 'game pair mismatch')
        away, home = c[1].split(' @ ')
        check(r['selection'] in (away, home), 'selection not in game')
        check(r['issued_time_printed'].startswith('2026-10-17 '), 'ticket date mismatch')
        check(r['receipt_event_time_printed'].startswith('2026-10-17 '), 'event date mismatch')
        a, h = map(int, c[5].split('-'))
        margin = h - a if r['selection'] == home else a - h
        check(r['market'] in ('SPREAD', 'MONEYLINE'), 'unsupported market')
        check((r['line'] is None) == (r['market'] == 'MONEYLINE'), 'line/market mismatch')
        signed = Decimal(margin) + (Decimal(str(r['line'])) if r['line'] is not None else 0)
        grade = 'WIN' if signed > 0 else 'LOSS' if signed < 0 else 'PUSH'
        stake = Decimal(r['stake_usd'])
        check(stake > 0 and Decimal(r['printed_max_payout_usd']) > stake, 'invalid ticket amounts')
        returned = Decimal(r['printed_max_payout_usd']) if grade == 'WIN' else stake if grade == 'PUSH' else Decimal(0)
        p = prior[r['game_id']]
        ref = p['review_ref']
        comparison = 'OUTSIDE_FINAL_FIVE_RECOMMENDATIONS'
        detail = {'side_state': p['side']['state'], 'side_reason': p['side']['rationale']}
        if ref:
            v = json.loads(historical(ref['blob']))
            check(v['game_id'] == r['game_id'], 'immutable recommendation identity')
            limit = v['acceptable_number']
            check(v['market'] == r['market'] and v['selection'] == ('home' if r['selection'] == home else 'away'),
                  'recommendation market/side mismatch')
            line_ok = r['line'] is None or Decimal(str(r['line'])) >= Decimal(str(limit['line']))
            price_ok = r['american_odds'] >= limit['minimum_price']
            comparison = 'WITHIN_RECORDED_LIMITS' if line_ok and price_ok else 'OUTSIDE_RECORDED_PRICE_LIMIT'
            detail = {'review_ref': ref, 'limit': limit, 'line_within_limit': line_ok,
                      'price_within_limit': price_ok}
        # Frozen direction is context only, never an inferred recommendation.
        frozen_margin, frozen_total, home_p = map(float, c[2:5])
        check(0 <= home_p <= 1 and frozen_total > 0, 'invalid saved model display')
        model_cushion = (frozen_margin if r['selection'] == home else -frozen_margin)
        if r['line'] is not None:
            model_cushion += r['line']
        out.append({'execution_id': r['execution_id'], 'game_id': r['game_id'], 'game': r['game'],
                    'selection': r['selection'], 'market': r['market'], 'line': r['line'],
                    'american_odds': r['american_odds'], 'stake_usd': r['stake_usd'],
                    'final_away_home': c[5], 'selected_final_margin': margin,
                    'signed_grade_comparison': str(signed), 'final_score_grade': grade,
                    'printed_payout_based_result_return_usd': f'{returned:.2f}',
                    'printed_payout_based_result_net_usd': f'{returned-stake:.2f}',
                    'saved_frozen_display_cushion': round(model_cushion, 3),
                    'frozen_display_cushion_scope': 'ROUNDED_ORIGINAL_DISPLAY_NOT_EV_OR_RECOMMENDATION',
                    'recommendation_comparison': comparison, 'comparison_detail': detail,
                    'causal_recommendation_attribution': 'UNVERIFIED',
                    'book_settlement_redemption_payment': 'UNVERIFIED',
                    'execution_chronology': 'UNVERIFIED_RECEIPT_TIMEZONE'})
    def totals(rows):
        st = sum((Decimal(r['stake_usd']) for r in rows), Decimal(0))
        ret = sum((Decimal(r['printed_payout_based_result_return_usd']) for r in rows), Decimal(0))
        return {'tickets': len(rows), 'stake_usd': f'{st:.2f}',
                'grades': {g: sum(r['final_score_grade'] == g for r in rows) for g in ('WIN', 'LOSS', 'PUSH')},
                'printed_payout_based_result_return_usd': f'{ret:.2f}',
                'printed_payout_based_result_net_usd': f'{ret-st:.2f}'}
    week7 = inputs[SCORE].decode().split('## Week 7 Tuesday')[1].split('## Week 8')[0]
    scored = []
    for line in week7.splitlines():
        c = [x.strip() for x in line.split('|')[1:-1]]
        if len(c) == 11 and c[0].isdigit():
            c = c[1:]
        if len(c) == 10 and ' @ ' in c[0]:
            scored.append(c)
    check(len(scored) == 51 and len({c[0] for c in scored}) == 51, 'Week7 modeled census')
    flags = sum(int(c[-1]) for c in scored)
    margin_direction = sum((float(c[1]) > 0) == (float(c[5]) > 0) for c in scored)
    check(flags == margin_direction == 32, 'Week7 independent margin-direction reconciliation')
    metric_reconciliation = {
        'modeled_games': 51, 'unique_games': 51,
        'sum_of_existing_su_correct_flags': flags, 'independent_display_margin_sign_correct': margin_direction,
        'existing_summary_claim_correct': 31, 'existing_summary_claim_inconsistent': True,
        'corrected_margin_direction_fraction': '32/51',
        'probability_classifier_correct_from_rounded_display': sum((float(c[3]) > .5) == (float(c[5]) > 0) for c in scored),
        'probability_scope': 'Distinct probability-threshold diagnostic; not margin direction and not added to 32.',
        'rounded_row_margin_mae': sum(abs(float(c[7])) for c in scored) / 51,
        'rounded_row_total_mae': sum(abs(float(c[8])) for c in scored) / 51,
        'scope': 'Existing 51 immutable displayed rows; no full-precision raw-archive metric recomputation. Published margin MAE12.89 remains unreconciled against rounded-row12.8431; no exact replacement inferred.'}
    return {'verdict': 'PASS_BOUNDED_ORIGINAL_TICKET_AND_HISTORICAL_COMPARISON_REPLAY',
            'source_blobs': manifest['input_blobs'], 'rows': out, 'totals': totals(out),
            'week7_metric_reconciliation': metric_reconciliation,
            'comparison_groups': {k: totals([r for r in out if r['recommendation_comparison'] == k])
                                  for k in sorted({r['recommendation_comparison'] for r in out})},
            'current_engine_financial_effectiveness': 'NOT_ESTABLISHED',
            'scope': 'Original intake plus saved-final diagnostics; no causal attribution, paid cash, CLV, refit, model promotion or natural scheduled reliability.'}


if __name__ == '__main__':
    manifest = json.loads(Path(MANIFEST).read_text())
    result = audit(manifest)
    # Actual boundary mutations demonstrate rejection; they are not live tickets.
    rejected = []
    for name, change in [
        ('duplicate_execution', lambda m: m['wagers'][1].update(execution_id=m['wagers'][0]['execution_id'])),
        ('duplicate_image', lambda m: m['wagers'][1].update(image_sha256=m['wagers'][0]['image_sha256'])),
        ('wrong_game', lambda m: m['wagers'][0].update(game='North Dakota @ Duke')),
        ('invented_timezone', lambda m: m['wagers'][0].update(receipt_timezone='America/Chicago')),
        ('invented_sandbox_allocation', lambda m: m['wagers'][0].update(budget_class='SANDBOX')),
        ('missing_ticket', lambda m: m['wagers'].pop()),
    ]:
        mutated = copy.deepcopy(manifest)
        change(mutated)
        try:
            audit(mutated)
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError('mutation accepted: ' + name)
    result['rejection_demonstrations'] = rejected
    print(json.dumps(result, indent=2))
