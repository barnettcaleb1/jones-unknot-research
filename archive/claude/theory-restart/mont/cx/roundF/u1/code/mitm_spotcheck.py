"""mitm_spotcheck.py -- coverage check of engineB's (7,7) screen: random junctions (t, b) of ALL top x bottom class
representatives (mitm.bfs, depth 7, knot_ok) are evaluated EXACTLY (lp.J); every J = 1 junction must be among the 685,359
zeta_7 & zeta_10 survivors (s2_survivors_7_7.json).  Junctions are sampled uniformly and also with |t| + |b| <= 6 enriched.
usage: mitm_spotcheck.py N SEED NPROC OUT.json"""
import sys, json, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import mitm, rho2, lp
from multiprocessing import Pool
def one(item):
    a, b = item
    hw = rho2.halfword('l1.l1', list(a) + list(b), 'u2.u2')
    return '.'.join(a), '.'.join(b), lp.J(hw) == {0: 1}
if __name__ == '__main__':
    N, seed, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    P = mitm.P; t = random.Random(3).randrange(2, P - 1)
    MT, VT, PHIT = rho2.normalised()
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}]
    Vv = [[mitm.evt(x, t) for x in VT['l1.l1']]]
    c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
    PH = [[mitm.evt(x, t) * c % P for x in PHIT['u2.u2']]]
    tops = [w for w, _ in mitm.bfs(Ms, Vv, 7, 'top')]; bots = [w for w, _ in mitm.bfs(Ms, PH, 7, 'bot')]
    tc = {a: mitm.top_class(a) for a in tops}; bc = {b: mitm.bot_class(b) for b in bots}
    rng = random.Random(seed); items = []
    small_t = [a for a in tops if len(a) <= 3]; small_b = [b for b in bots if len(b) <= 3]
    while len(items) < N:
        if len(items) % 2: a, b = rng.choice(tops), rng.choice(bots)
        else: a, b = rng.choice(small_t), rng.choice(bots)
        if mitm.knot_ok(tc[a], bc[b]): items.append((a, b))
    surv = set(tuple(x) for x in json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s2_survivors_7_7.json'))['survivors'])
    t0 = time.time()
    with Pool(nproc) as Pl: res = Pl.map(one, items, chunksize=50)
    j1 = [(a, b) for a, b, ok in res if ok]
    missing = [(a, b) for a, b in j1 if (a, b) not in surv]
    summ = {'tops': len(tops), 'bottoms': len(bots), 'sampled_junctions': N, 'J1': len(j1), 'J1_NOT_in_survivors': len(missing),
            'examples_missing': missing[:10], 'secs': round(time.time() - t0, 1)}
    print(json.dumps(summ)); json.dump(summ, open(outp, 'w'), indent=1)
