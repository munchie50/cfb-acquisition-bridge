"""Exact CMU/EMU missed-review recognition; never a reconstructed decision."""
import json
import re
import cfb_neutral_publication_gate as gate

GAME = '401866456'
PRIOR_BLOB = 'b0cd4391b01956aa7232980f53ac1a909da9e4e1'
PRIOR_BYTES = 1981789
KICKOFF = '2026-11-05T00:30:00Z'
NOT_BEFORE = '2026-11-05T00:56:23Z'
REASON = ('MISSED PRE-EVENT REVIEW: CMU/EMU total remained INCONCLUSIVE at its '
          '2026-11-04T23:30:00Z reconciliation deadline and saved kickoff. '
          'Recognized only now; no completed pregame total decision, PASS, '
          'recommendation or execution is reconstructed. Prior partial analysis remains preserved.')


def context(decision, market, decision_tag, market_tag):
    """Authenticate a late recognition against the exact unresolved prior bytes."""
    def packets(content, tag):
        return [json.loads(m[1], object_pairs_hook=gate.unique) for m in re.finditer(
            r'^```' + tag + r'\n(.*?)^```[ \t]*$', content, re.M | re.S)]
    history = packets(decision, decision_tag)
    gap_packets = [p for p in history if any(
        r['game_id'] == GAME and r['state'] == 'HISTORICAL_GAP' for r in p['rows'])]
    if not gap_packets:
        return {}
    raw = decision.encode('utf-8')
    prior = raw[:PRIOR_BYTES].decode('utf-8')
    if gate.blob(prior) != PRIOR_BLOB:
        raise ValueError('missed-review exact prior decision bytes changed')
    old = packets(prior, decision_tag)[-1]
    previous = next(r for r in old['rows'] if r['game_id'] == GAME)
    if (previous['state'] != 'INCONCLUSIVE' or previous['review_ref'] is not None
            or previous['reconciliation_utc'] != '2026-11-04T23:30:00Z'):
        raise ValueError('missed-review prior unresolved state changed')
    origin = gap_packets[0]
    recognized = gate.clock(origin['as_of_utc'])
    if recognized < gate.clock(NOT_BEFORE) or recognized < gate.clock(KICKOFF):
        raise ValueError('missed-review recognition predates authorized elapsed boundary')
    before = [p for p in history if gate.clock(p['as_of_utc']) < recognized]
    if not before or before[-1] != old:
        raise ValueError('missed-review must directly follow exact unresolved prior')
    expected = dict(game_id=GAME, state='HISTORICAL_GAP', reason=REASON,
                    reconciliation_utc=None, planning_cutoff_utc=None,
                    cutoff_authority='UNVERIFIED', acceptable_number=None,
                    execution_window=None, review_ref=None,
                    state_recorded_at_utc=origin['as_of_utc'], state_evidence=origin['cycle_id'])
    sources = {p['cycle_id']: p for p in packets(market, market_tag)}
    for p in gap_packets:
        rows = [r for r in p['rows'] if r['game_id'] == GAME]
        if rows != [expected]:
            raise ValueError('missed-review recognition cannot change or reopen')
        paired = sources.get(p['cycle_id'])
        if paired is None or paired['as_of_utc'] != p['as_of_utc']:
            raise ValueError('missed-review paired source missing')
        source = next(r for r in paired['rows'] if r['game_id'] == GAME)
        if (source['kickoff_utc'] != KICKOFF or source['current'] is not None
                or source['current_availability'] != 'UNAVAILABLE'):
            raise ValueError('missed-review cannot carry current pregame quote or changed kickoff')
    # Every later packet must preserve the recognition, even one trying to hide it.
    for p in history:
        if gate.clock(p['as_of_utc']) >= recognized:
            if [r for r in p['rows'] if r['game_id'] == GAME] != [expected]:
                raise ValueError('missed-review recognition cannot change or reopen')
    return {GAME: {'as_of_utc': origin['as_of_utc'], 'state_evidence': origin['cycle_id']}}
