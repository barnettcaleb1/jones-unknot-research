"""u2/indep/final.py -- per-family verdict: CERTIFIED iff (upstairs proof passes for every site circle, section 2b/2c) AND every
member point of the family (lines: k = -2..2 + base; planes: 3x3 grid + base) is CERTIFIED_UNKNOT by the audited tool AND that
certificate passed BOTH checkers in the fresh-process re-check.  Else UNRESOLVED."""
import json, gzip
from collections import Counter, defaultdict
O = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/'
fams = {f['fid']: f for f in json.load(open(O + 'families.json'))}
runr = {r['fid']: r for r in json.load(open(O + 'run_results.json'))}
st = {}
with gzip.open(O + 'cert/members.jsonl.gz', 'rt') as fh:
    for line in fh:
        r = json.loads(line); st[r['w']] = (r['status'], r.get('n'), tuple(r.get('kinds') or []))
ver = json.load(open(O + 'cert/verify_members.json'))
failed = set(x['w'] for x in ver.get('records_FAIL', []))
ver_ok = ver['records_pass'] == ver['sampled'] == ver['records_total']
pts = defaultdict(list)
for tag, w in json.load(open(O + 'member_points.json')): pts[tag.split('|')[0]].append(w)
tab = Counter(); out = []; maxn = Counter()
for fid, f in fams.items():
    if not f['u2_target']: continue
    r = runr[fid]
    proof = (r['verdict'] == 'PROVED-up') if f['kind'] == 'line' else (r['verdict'] == 'PROVED-up-both-global')
    down = (r.get('down_ok') if f['kind'] == 'line' else (set(r['down1']) | set(r['down3'])) <= {'T-disc', 'S-trivial', 'H-vertex'})
    mem = [st.get(w, ('MISSING',))[0] for w in pts[fid]]
    certified_members = all(m == 'CERTIFIED_UNKNOT' for m in mem) and not any(w in failed for w in pts[fid]) and ver_ok
    verdict = 'CERTIFIED' if (proof and certified_members) else 'UNRESOLVED'
    key = (f['src'], f['kind'], tuple(f['d']) if f['kind'] == 'line' else 'plane', verdict)
    tab[key] += 1
    out.append({'fid': fid, 'src': f['src'], 'kind': f['kind'], 'V': f['V'], 'U': f['U'], 'd': f['d'], 'm0': f['m0'], 'n0': f['n0'],
                'upstairs_proof': proof, 'downstairs_reimpl': bool(down), 'members': len(pts[fid]),
                'members_certified': sum(m == 'CERTIFIED_UNKNOT' for m in mem), 'verdict': verdict})
for k in sorted(tab, key=str): print('   ', k, tab[k])
print('verification: records_total', ver['records_total'], 'sampled', ver['sampled'], 'pass', ver['records_pass'], 'all pass', ver_ok)
json.dump(out, open(O + 'final_families.json', 'w'))
json.dump([x for x in out if x['verdict'] != 'CERTIFIED'], open(O + 'unresolved.json', 'w'))
print('UNRESOLVED families:', sum(1 for x in out if x['verdict'] != 'CERTIFIED'))
