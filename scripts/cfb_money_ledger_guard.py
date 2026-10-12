"""Read-only qualified ADD20 funding integrity; not a cash-balance/payment auditor."""
import argparse,json,re
from datetime import datetime,timezone
from decimal import Decimal
from pathlib import Path
from cfb_hot_sheet_current_decision_binding_gate import blob
from cfb_recovery_navigation_reader import read

EXECUTION_SHA='75caee4052e02ea7d2453d1d37fd3866e13ecc07'
PATH='evidence/operational/CFB_MONEY_LEDGER.md'
FID='CFB_ORIGINAL_ADD20_FUNDING_001'
KEY='ORIGINAL_USER_INSTRUCTION_ALSO_ADD_20_TO_MONEY_LEDGER'
FIELDS={'schema','funding_id','idempotency_key','transaction_type','amount_usd','status','budget_class','funding_event_time','recorded_at_utc','source','related_execution_ids','execution_reference','is_wager','is_wager_return','changes_sandbox_ceiling','cash_balance'}

def unique(pairs):
    out={}
    for k,v in pairs:
        if k in out:raise ValueError('duplicate JSON key')
        out[k]=v
    return out

def dollars(value):
    if not isinstance(value,str) or not re.fullmatch(r'\d+\.\d{2}',value):raise ValueError('USD two-decimal amount required')
    return Decimal(value)

def audit(money,execution,as_of):
    if blob(execution)!=EXECUTION_SHA:raise ValueError('execution reference snapshot not qualified')
    markers=re.findall(r'^```cfb-funding-json\s*$',money,re.M)
    bodies=re.findall(r'^```cfb-funding-json\s*\n(.*?)^```\s*$',money,re.M|re.S)
    if not bodies or len(markers)!=len(bodies):raise ValueError('missing/incomplete funding record')
    rows=[json.loads(b,object_pairs_hook=unique) for b in bodies]
    if any(not isinstance(r,dict) or set(r)!=FIELDS for r in rows):raise ValueError('unsupported funding schema')
    for field in ('funding_id','idempotency_key'):
        values=[r[field] for r in rows]
        if not all(isinstance(v,str) and v.strip() for v in values) or len(values)!=len(set(values)):raise ValueError('duplicate/invalid '+field)
    if len(rows)!=1:raise ValueError('additional funding requires separately qualified source boundary')
    r=rows[0]
    if (r['schema'],r['funding_id'],r['idempotency_key'])!=('CFB_FUNDING_TRANSACTION_V1',FID,KEY):raise ValueError('qualified original instruction identity mismatch')
    amount=dollars(r['amount_usd'])
    if amount!=Decimal('20.00') or r['transaction_type']!='BANKROLL_FUNDING':raise ValueError('funding amount/type changed')
    if r['status']!='POSTED_USER_CONFIRMED_ALLOCATION_UNASSIGNED' or r['budget_class']!='UNASSIGNED':raise ValueError('allocation authority not earned')
    if any(r[k] is not False for k in ('is_wager','is_wager_return','changes_sandbox_ceiling')):raise ValueError('funding/wager/payout/risk conflation')
    if r['cash_balance']!='NOT_COMPUTABLE_FROM_CURRENT_ALLOCATED_EVIDENCE' or r['funding_event_time']!='UNSPECIFIED':raise ValueError('cash balance/funding clock inferred')
    now=datetime.fromisoformat(as_of.replace('Z','+00:00'));at=datetime.fromisoformat(r['recorded_at_utc'].replace('Z','+00:00'))
    if now.tzinfo is None or at.tzinfo is None or at>now:raise ValueError('recording clock invalid/future')
    if r['source']!={'original_instruction':'Also add 20 to money ledger','clarification':'New money added, separate from the four $5 bets','evidence_type':'DIRECT_USER_CLARIFICATION'}:raise ValueError('qualified user clarification changed')
    if r['execution_reference']!={'path':'evidence/operational/CFB_EXECUTION_LEDGER.md','blob':EXECUTION_SHA}:raise ValueError('execution reference mismatch')
    events={};active=False
    for line in execution.splitlines():
        if line.startswith('| Execution ID |'):active='Issued date/time as printed' in line
        if active and line.startswith('| CFB_'):
            cells=[c.strip() for c in line.split('|')[1:-1]]
            if cells[0] in events:raise ValueError('duplicate intake execution')
            events[cells[0]]=dollars(cells[6].removeprefix('$'))
    related={'CFB_OCT09-01','CFB_OCT09-02','CFB_OCT09-03','CFB_OCT09-04'}
    if not isinstance(r['related_execution_ids'],list) or len(r['related_execution_ids'])!=4 or set(r['related_execution_ids'])!=related or not related<=events.keys():raise ValueError('related execution identity mismatch')
    if len(events)!=15 or sum(events.values())!=Decimal('53.45') or sum(events[k] for k in related)!=Decimal('20.00'):raise ValueError('execution snapshot stake reconciliation failed')
    table=[]
    for line in money.splitlines():
        if line.startswith('| CFB_'):
            cells=[c.strip() for c in line.split('|')[1:-1]]
            if len(cells)!=6:raise ValueError('unsupported funding display')
            table.append(cells)
    if len(table)!=1 or table[0][0]!=FID or table[0][2]!='+$20.00' or table[0][3]!='UNASSIGNED production/sandbox' or table[0][4]!='Unspecified':raise ValueError('funding table/source disagreement')
    if 'Confirmed funding recorded in this ledger: **+$20.00**, one transaction.' not in money:raise ValueError('declared funding total/count mismatch')
    return {'verdict':'PASS_QUALIFIED_ADD20_FUNDING_RECORD_ONLY','funding_transactions':1,'funding_usd':'20.00',
            'historical_execution_count':15,'historical_stake_usd':'53.45','related_four_stake_usd':'20.00',
            'allocation':'UNASSIGNED','cash_balance':'NOT_COMPUTABLE','money_blob':blob(money),'execution_snapshot_blob':EXECUTION_SHA,
            'scope':'qualified funding record/table/deduplication/reference only; no bank transfer, paid-out return, available bankroll or new allocation/risk authority'}

def binding(index,money,as_of):
    pointers=read(index,as_of)['frontier']['pointers']
    selected=[p for p in pointers if p['purpose'].startswith('CURRENT_MONEY_LEDGER:')]
    if len(selected)!=1 or selected[0]['path']!=PATH or selected[0]['blob']!=blob(money):raise ValueError('missing/ambiguous/stale current money selector')
    return {'current_money_blob':blob(money),'navigation_scope':'binding only'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('money','execution','index'):p.add_argument('--'+n,required=True,type=Path)
    a=p.parse_args();now=datetime.now(timezone.utc).isoformat();money=a.money.read_text()
    result=audit(money,a.execution.read_text(),now);result.update(binding(a.index.read_text(),money,now))
    print(json.dumps(result,indent=2))
