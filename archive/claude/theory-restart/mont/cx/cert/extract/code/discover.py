"""Discovery: all freely reduced words h, |h| <= N, with rho_2(h) f0 ~ f0 (TOP) or PHI rho_2(h) ~ PHI (BOT), mod P at 2 random t.
For each, test whether reduce.py (group rules + only that end's absorption rules) reduces h to the empty word."""
import sys, random, json, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import mitm, rho2, rules, reduce as R
P = mitm.P
N = int(sys.argv[1])
rnd = random.Random(5)
ts = [rnd.randrange(2, P - 1) for _ in range(2)]
MT, VT, PHIT = rho2.normalised()
Ms = [{rules.CODE[L]: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()} for t in ts]
V0 = [[mitm.evt(x, t) for x in VT['l1.l1']] for t in ts]
PH0 = [[mitm.evt(x, t) for x in PHIT['u2.u2']] for t in ts]
p0 = [mitm.proj(v) for v in V0]; q0 = [mitm.proj(v) for v in PH0]
LETS = [1, -1, 2, -2, 3, -3, 4, -4]
res = {'top': [], 'bot': []}
# DFS over words: top: v -> M[a] v (a appended at the end acts last); bot: covector, word extended at the FRONT
def dfs_top(w, vs):
    if w and all(mitm.proj(v) == p for v, p in zip(vs, p0)): res['top'].append(w)
    if len(w) == N: return
    for a in LETS:
        if w and a == -w[-1]: continue
        dfs_top(w + (a,), [mitm.mv(M[a], v) for M, v in zip(Ms, vs)])
def dfs_bot(w, ws):
    if w and all(mitm.proj(v) == p for v, p in zip(ws, q0)): res['bot'].append(w)
    if len(w) == N: return
    for a in LETS:
        if w and a == -w[0]: continue
        dfs_bot((a,) + w, [mitm.vm(v, M[a]) for M, v in zip(Ms, ws)])
t0 = time.time()
dfs_top((), V0); dfs_bot((), PH0)
print('stabilisers |h| <=', N, ': top', len(res['top']), 'bot', len(res['bot']), round(time.time() - t0, 1), 's')
out = {}
for side in ('top', 'bot'):
    R.USE['top'] = side == 'top'; R.USE['bot'] = side == 'bot'
    fails = []
    for h in res[side]:
        r, m = R.reduce_word(h, budget=4000)
        if r: fails.append(rules.dec(h) + '  ->  ' + rules.dec(r))
    out[side] = fails
    print(side, 'not reduced to empty:', len(fails))
    for f in fails[:40]: print('   ', f)
json.dump({'N': N, 'n_top': len(res['top']), 'n_bot': len(res['bot']), 'fails': out}, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/discover_N%d.json' % N, 'w'), indent=1)
