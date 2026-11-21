"""Read-only explicit attribution of pregame decisions; never authorizes wagers."""
ALLOWED = frozenset(('FOOTBALL_SUPPORT','FOOTBALL_COUNTERCASE','PRICE_HOLD','NUMBER_HOLD','QUOTE_GAP','VENUE_GAP','TIMING_GAP','MODEL_GAP','REVIEW_GAP'))

def attribute(row):
    if not isinstance(row, dict) or not row.get('game_id') or not row.get('market') or not row.get('as_of_utc'):
        raise ValueError('Missing identity, market or pregame clock')
    tags = row.get('evidence_tags')
    if not isinstance(tags, list) or not tags or any(t not in ALLOWED for t in tags) or len(tags) != len(set(tags)):
        raise ValueError('Explicit unique evidence tags required')
    if not row.get('source_ref') or not row.get('reason'):
        raise ValueError('Evidence provenance and reason required')
    if row.get('price_only') is True and (set(tags) - {'PRICE_HOLD','FOOTBALL_SUPPORT'} or 'PRICE_HOLD' not in tags or 'FOOTBALL_SUPPORT' not in tags):
        raise ValueError('Price-only classification contradicts evidence tags')
    return {'game_id':str(row['game_id']),'market':str(row['market']),'as_of_utc':row['as_of_utc'],
            'original_state':row.get('original_state','UNSPECIFIED'), 'evidence_tags':sorted(tags),
            'price_only_documented':row.get('price_only') is True,
            'source_ref':row['source_ref'],'reason':row['reason'],'bet_authorized':False}
