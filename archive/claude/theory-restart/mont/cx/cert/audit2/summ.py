"""summ.py OUT.jsonl -- summarise a results file."""
import sys, json, collections
rows = [json.loads(l) for l in open(sys.argv[1])]
by = collections.defaultdict(collections.Counter)
bad = []
secs = collections.defaultdict(list)
for r in rows:
    lab = r.get('label', '').split(':')[0]
    by[lab][r.get('status')] += 1
    secs[lab].append(r.get('secs') or 0)
    if r.get('bad'): bad.append(r)
    for v in r.get('verify', []) or []:
        by[lab]['verify_' + v[0] + ('_ok' if v[1] else '_FAIL')] += 1
    t = r.get('tietze')
    if t: by[lab]['tietze_success' if t.get('success') else 'tietze_fail'] += 1
for lab in sorted(by):
    s = sorted(secs[lab]); med = s[len(s)//2] if s else 0
    print(lab, dict(by[lab]), 'median %.2fs max %.2fs' % (med, max(s) if s else 0))
print('BAD rows:', len(bad))
for r in bad[:20]: print(' ', r.get('label'), r.get('hw', '')[:100], r.get('status'), r.get('bad'), r.get('notes'))
