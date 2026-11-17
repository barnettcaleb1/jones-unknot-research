"""stress_tietze.py -- soundness stress test of the Tietze route on NONTRIVIAL knots with long budgets (many randomised
restarts, neutral moves, Whitehead/Nielsen moves active).  The simplifier must never reach <g | >; if it ever did, the
certificate would also be replayed by replay.check and reported loudly.
Sets: width-one (two-bridge) words s.l1.W.u2, W in {x0,y0,x1,y1}^* with V_K != 1 (2-generator presentations, where
Whitehead reduction is active), and the 24 engineB E3d Alexander-trivial knots + mirrors.
usage: stress_tietze.py NPROC BUDGET OUT.json"""
import sys, json, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/code')
import diagram, wirtinger, tietze, replay, refs
from gen_sets import mirror
from multiprocessing import Pool

BUD = [20.0]

def one(w):
    pd = diagram.pd_from_halfword(w)
    g, r = wirtinger.wirtinger(pd)
    t0 = time.time()
    res = []
    for seed in (1, 2):
        ok, moves, fin, st = tietze.simplify(g, r, seed=seed, time_budget=BUD[0] / 2, restarts=10 ** 6)
        rec = {'seed': seed, 'ok': ok, 'attempts': st['attempts'], 'final': (len(fin[0]), len(fin[1]), tietze.total_len(fin[1]))}
        if ok:
            rec['replay'] = replay.check({'kind': 'tietze', 'halfword': w, 'moves': [list(m) for m in moves]})
        res.append(rec)
    return {'w': w, 'n': pd.n, 'V1': diagram.jones(pd) == {0: 1}, 'runs': res, 'secs': round(time.time() - t0, 1)}

def init(b): BUD[0] = b

if __name__ == '__main__':
    nproc, bud, outp = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
    rnd = random.Random(31)
    ws = []
    while len(ws) < 100:
        W = [rnd.choice(['x0', 'y0', 'x1', 'y1']) for _ in range(rnd.randint(3, 14))]
        w = 's.l1.' + '.'.join(W) + '.u2'
        if not refs.is_knot(w): continue
        pd = diagram.pd_from_halfword(w)
        if diagram.jones(pd) != {0: 1} and w not in ws: ws.append(w)
    e3d = []
    for f in ['e3d_n20_s420.json', 'e3d_n30_s430.json', 'e3d_n40_s440.json']:
        d = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/' + f))
        e3d += [x['word'] for x in d['best']]
    e3d = sorted(set(e3d))
    ws += e3d + [mirror(w) for w in e3d]
    t0 = time.time()
    with Pool(nproc, initializer=init, initargs=(bud,)) as P:
        rows = P.map(one, ws, chunksize=1)
    false = [r for r in rows if any(x['ok'] for x in r['runs'])]
    attempts = sum(x['attempts'] for r in rows for x in r['runs'])
    fin2 = sum(1 for r in rows for x in r['runs'] if x['final'][0] == 2)
    summ = {'knots': len(rows), 'two_bridge': 100, 'alexander_trivial': len(rows) - 100, 'budget_s': bud,
            'total_attempts': attempts, 'final_presentations_with_2_gens': fin2, 'FALSE_UNKNOT_CERTIFICATES': len(false),
            'wall': round(time.time() - t0, 1)}
    json.dump({'summary': summ, 'rows': rows}, open(outp, 'w'))
    print(json.dumps(summ))
    for r in false: print('FALSE', r)
