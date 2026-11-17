"""check_saved.py -- AUDIT-2 re-check of the BUILDER's saved CERTIFIED_UNKNOT certificates from cert/out/:
replay.check + my own replay on my own presentation + my bracket (V = 1) + my crossing count."""
import sys, json, gzip, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import a2lib, replay
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/out/'
rng = random.Random(2026)
def sample_gz(fn, k, key=None):
    rows = []
    with gzip.open(OUT + fn, 'rt') as f:
        for i, l in enumerate(f):
            if rng.random() < 0.004 or len(rows) < 5: rows.append(json.loads(l))
            if len(rows) > 4 * k: break
    rng.shuffle(rows)
    return rows[:k]
certs = []
for r in sample_gz('mitm77_cert.tietze.jsonl.gz', 400):
    certs.append(('mitm77', r))
big = [c for c in certs if a2lib.morse_diagram(a2lib.full_of(c[1]['halfword']))['n'] > 24][:60]
small = [c for c in certs if c not in big][:10]
sel = big + small
for r in sample_gz('bulk_top_d8.jsonl.gz', 20): sel.append(('bulk_top_d8', r['cert']))
for r in sample_gz('bulk_bottom_d8.jsonl.gz', 20): sel.append(('bulk_bottom_d8', r['cert']))
codex = [json.loads(l) for l in open(OUT + 'final_suiteA2codex.jsonl')]
for r in codex[:20]:
    for c in r['cert']['certificates']:
        sel.append(('suiteA2codex', c))
stats = {}
for src, c in sel:
    hw = c['halfword']
    full = a2lib.full_of(hw); D = a2lib.morse_diagram(full)
    n = D['n']
    v1 = a2lib.jones_unit_test(a2lib.bracket_full(full)) if n > 0 else True
    ok_r, msg = replay.check(c)
    if c['kind'] == 'tietze':
        g, rels = a2lib.wirtinger_from_full(full)
        mine = a2lib.my_replay(g, rels, [tuple(m) for m in c['moves']])[0]
    elif c['kind'] == 'jones24':
        mine = n <= 24 and v1
    else:
        mine = None
    key = (src, c['kind'])
    s = stats.setdefault(key, {'n': 0, 'replay_ok': 0, 'mine_ok': 0, 'V1': 0, 'maxcr': 0})
    s['n'] += 1; s['replay_ok'] += ok_r; s['mine_ok'] += bool(mine); s['V1'] += v1; s['maxcr'] = max(s['maxcr'], n)
    if not (ok_r and mine and v1): print('PROBLEM', src, hw, ok_r, msg, mine, v1)
for k, v in stats.items(): print(k, v)
