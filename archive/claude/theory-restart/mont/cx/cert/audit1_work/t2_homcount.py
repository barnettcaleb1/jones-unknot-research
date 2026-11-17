"""AUDIT-1 test 2: does the CHECKER's Wirtinger presentation (replay.wirtinger_presentation, from alex.diagram)
present pi_1(S^3 - K)?  Compare, per conjugacy class C of G, T(K) = #{phi: phi(meridian) in C u C^-1} computed
(i) from replay's presentation by the auditor's DFS, (ii) from the auditor's OWN plat sweep (exact Artin action on the
Morse word; no arcs, no orientation, no crossing signs).  Sensitivity control: the same comparison after flipping the
exponent sign of ONE crossing relator of replay's presentation (a deliberately planted sign error) must disagree often.
usage: t2_homcount.py SEED COUNT NPROC OUT.json"""
import sys, json, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit1_work')
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import audlib, replay, alex
from multiprocessing import Pool

GS = None
def init():
    global GS
    GS = audlib.groups()

LIMIT = 60000

def one(arg):
    w, ctrl_seed = arg
    full = alex.symmetrize(alex.parse(w))
    P = replay.wirtinger_presentation(w)
    if P is None: return {'w': w, 'skip': 'not a knot'}
    gens, rels = P
    n = len(gens)
    if n == 0: return {'w': w, 'skip': 'no crossings'}
    R = audlib.parse_wirt(gens, rels)
    caps = 1 + sum(1 for c, i in full if c in 'lr')
    # planted sign error at one crossing (control)
    rc = random.Random(ctrl_seed); k = rc.randrange(n)
    Rbad = list(R); out, o, i, s = Rbad[k]; Rbad[k] = (out, o, i, -s)
    res = {'w': w, 'n': n, 'caps': caps, 'cmp': 0, 'agree': 0, 'mism': [], 'ctrl_cmp': 0, 'ctrl_diff': 0,
           'nonab': 0}
    for G in GS:
        for C in G.classes:
            if C == [G.e]: continue
            K, reps, sz = audlib.class_K(G, C)
            if len(K) ** (caps - 1) > LIMIT: continue
            tw = sz * sum(audlib.wirt_count(n, R, G, K, r) for r in reps)
            tp = sz * sum(audlib.plat_count(full, G, K, r) for r in reps)
            res['cmp'] += 1
            if tw == tp: res['agree'] += 1
            else: res['mism'].append((G.name, len(C), tw, tp))
            if tw > len(K) : res['nonab'] += 1        # more than the abelian (cyclic) homs
            tb = sz * sum(audlib.wirt_count(n, Rbad, G, K, r) for r in reps)
            res['ctrl_cmp'] += 1
            if tb != tp: res['ctrl_diff'] += 1
    res['ctrl_detected'] = res['ctrl_diff'] > 0
    return res

if __name__ == '__main__':
    seed, count, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rnd = random.Random(seed); ws = []; seen = set()
    while len(ws) < count:
        w = audlib.rand_halfword(rnd, rnd.randint(2, 12), maxhw=rnd.choice([5, 7]))
        if w in seen or not audlib.is_knot(w): continue
        if audlib.ncaps(w) > 5 or audlib.ncross(w) > 30: continue
        seen.add(w); ws.append((w, rnd.randrange(10**9)))
    t0 = time.time()
    with Pool(nproc, initializer=init) as P:
        rows = P.map(one, ws, chunksize=1)
    rows = [r for r in rows if 'skip' not in r]
    summ = {'knots': len(rows), 'comparisons': sum(r['cmp'] for r in rows), 'agree': sum(r['agree'] for r in rows),
            'mismatch_knots': [r for r in rows if r['mism']][:20],
            'knots_with_nonabelian_counts': sum(1 for r in rows if r['nonab']),
            'control_knots_detected': sum(1 for r in rows if r['ctrl_detected']),
            'control_knots_with_nonab': sum(1 for r in rows if r['nonab']),
            'crossings_range': (min(r['n'] for r in rows), max(r['n'] for r in rows)),
            'secs': round(time.time() - t0, 1)}
    json.dump({'summary': summ, 'rows': rows}, open(outp, 'w'))
    print(json.dumps(summ))
