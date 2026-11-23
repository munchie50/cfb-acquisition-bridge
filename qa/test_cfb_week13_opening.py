"""Replay the retained CBS board through the opening path with QA-only clocks."""
import hashlib
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from unittest.mock import patch
from zipfile import ZipFile

import cfb_hot_sheet_readiness as readiness
import cfb_saved_publication_audit as saved
import cfb_week13_publication as week
from cfb_cbs_full_board_normalizer import WEEK13_LINEAGE_PATH, week13_census
from cfb_hot_sheet_current_decision_binding_gate import publication
from cfb_monitor_collection import active_profile, inspect
from cfb_neutral_publication_gate import blob, clock, render

AS_OF = '2026-11-23T19:00:00Z'


def check(archive):
    root = Path(__file__).resolve().parents[1]
    with ZipFile(archive) as z:
        raw = z.read('cbs-week13-raw.html')
    assert hashlib.sha256(raw).hexdigest() == 'f2319f9354cc3fd5dac23edd328740fb62fb24e98fd75b20e1dfda38d0a6b695'
    assert active_profile(clock(AS_OF)).name == 'WEEK13'
    capture, coverage, _ = inspect(raw, AS_OF)
    assert coverage['matched_games'] == 69 and coverage['source_team_rows'] == 138
    lineage = (root / WEEK13_LINEAGE_PATH).read_text()
    originals = week13_census(lineage)
    states = {'ARCHIVE_PREDICTION': 'INCONCLUSIVE', 'ARCHIVE_EXCLUSION': 'PASS',
              'OBSERVATION_ONLY': 'OBSERVATION_ONLY'}
    rows = [
        dict(game_id=gid, state=states[row['status']], reason='QA fixture only',
             reconciliation_utc='2026-11-24T18:00:00Z' if row['status'] == 'ARCHIVE_PREDICTION' else None,
             planning_cutoff_utc=None, cutoff_authority='UNVERIFIED',
             acceptable_number=None, execution_window=None)
        for gid, row in originals.items()
    ]
    with TemporaryDirectory() as directory:
        local = Path(directory)
        path = local / 'evidence/operational/replay.md'
        path.parent.mkdir(parents=True)
        path.write_text(capture)
        source = dict(path=str(path.relative_to(local)), blob=blob(capture), recovered_by=AS_OF)
        market, decision = '# QA market\n', '# QA decision\n'
        cycle = 'CFB_MARKET_MONITOR_20261123T190000Z'
        with patch.multiple(week, ROOT=local, MARKET_PARENT=blob(market), DECISION_PARENT=blob(decision)):
            m, d = week.compile(market, decision, source, lineage, cycle, AS_OF, rows)
            args = (m, d, 'QA execution', 'QA scorecard', lineage, AS_OF, 'WEEK13')
            sheet = render(*args)
            assert sheet.count('| OBSERVATION_ONLY |') == 4
            assert saved.audit(sheet, *args)['integrity']['games'] == 69
            assert readiness.audit(m, d, lineage, AS_OF, 'WEEK13')['evaluation_coverage']['counts']['OBSERVATION_ONLY'] == 4
            target = 'evidence/operational/CFB_WEEK13_HOT_SHEET_2026-11-23_1300CT.md'
            index = dict(schema='CFB_RECOVERY_NAVIGATION_FRONTIER_V1', as_of_utc=AS_OF,
                         scope='NAVIGATION_ONLY_NOT_AUTHORITY', claims=['QA fixture'],
                         pointers=[
                             dict(path='evidence/operational/CFB_DECISION_WAIT_LEDGER.md',
                                  blob=blob(d), purpose='CURRENT_DECISION_STATE: QA'),
                             dict(path=target, blob=blob(sheet), purpose='CURRENT_HOT_SHEET: QA'),
                         ])
            result = publication('```cfb-frontier-json\n' + json.dumps(index) + '\n```\n',
                                 d, {target: sheet}.__getitem__, AS_OF)
            assert result['sheet_path'] == target
            refresh_at = '2026-11-23T19:01:00Z'
            refreshed = dict(source, recovered_by=refresh_at)
            m2, d2 = week.compile(m, d, refreshed, lineage, 'CFB_MARKET_MONITOR_20261123T190100Z',
                                  refresh_at, rows)
            assert m2.startswith(m) and d2.startswith(d)
            args2 = (m2, d2, 'QA execution', 'QA scorecard', lineage, refresh_at, 'WEEK13')
            assert saved.audit(render(*args2), *args2)['integrity']['games'] == 69
            try:
                week.compile(m, d, source, lineage, 'CFB_MARKET_MONITOR_20261123T190100Z',
                             refresh_at, rows)
            except ValueError as error:
                assert 'new capture' in str(error)
            else:
                raise AssertionError('reissued opening capture passed continuation')
            for state, replacement in [('OBSERVATION_ONLY', {'state': 'PASS'}),
                                       ('INCONCLUSIVE', {'reconciliation_utc': '2026-11-24T20:00:00Z'})]:
                bad = [dict(row) for row in rows]
                next(row for row in bad if row['state'] == state).update(replacement)
                try:
                    week.compile(market, decision, source, lineage, cycle, AS_OF, bad)
                except ValueError:
                    pass
                else:
                    raise AssertionError('invalid flex state or Tuesday deadline accepted')


if __name__ == '__main__':
    check(Path(sys.argv[1]))
    print('PASS: Week13 opening replay, 69 rows, four observation-only, saved audit and selector')
