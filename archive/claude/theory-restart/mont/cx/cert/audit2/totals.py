"""totals.py -- AUDIT-2 grand totals over all result files."""
import json, glob, collections
tot = collections.Counter(); bad = []
nontriv_unknot = 0
for f in ['res1.jsonl', 'res1b.jsonl', 'res5.jsonl', 'res9.jsonl', 'res9b.jsonl', 'res678.jsonl', 'res_pd.jsonl', 'res_pd2.jsonl']:
    for l in open(f):
        r = json.loads(l)
        e = r.get('expect'); st = r.get('status')
        tot[(e, st)] += 1
        if r.get('bad'): bad.append((f, r.get('label'), r.get('bad')))
        if e == 'nontrivial' and st == 'CERTIFIED_UNKNOT': nontriv_unknot += 1
        for v in (r.get('verify') or []):
            tot[('verify', v[0], v[1])] += 1
        for c in (r.get('certs') or []):
            if c[0] == 'rep': tot[('pd_rep_mycheck', c[2])] += 1
            if c[0] == 'tietze': tot[('pd_tietze_replay_and_mine', bool(c[1] and c[2]))] += 1
tz = collections.Counter(); att = 0
for f in ['tz_A.jsonl', 'tz_B.jsonl', 'tz_C.jsonl'] + glob.glob('tz_gordian_*.jsonl'):
    for l in open(f):
        r = json.loads(l)
        for run in r['runs']:
            tz[(r.get('expect'), run['success'])] += 1; att += run.get('attempts') or 0
for k, v in sorted(tot.items(), key=str): print(k, v)
print('tietze stress runs', dict(tz), 'attempts', att)
print('nontrivial knots CERTIFIED_UNKNOT:', nontriv_unknot)
print('bad rows:', bad)
