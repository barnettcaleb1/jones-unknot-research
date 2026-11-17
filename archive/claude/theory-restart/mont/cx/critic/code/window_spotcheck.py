"""window_spotcheck.py -- coverage check of engineB's window screen (template_window.py 4 4 6, sector formula at zeta_7):
random window theta-curves V.(x1x1)^m.(x3x3)^n.U over ALL (4,4) junctions (mitm.bfs reps, knot_ok) with |m|,|n| <= 6 are
evaluated EXACTLY (lp.J); every J = 1 point must be among the 154,869 J = 1 window configurations (s3a_items.json), i.e. the
sector-formula filter must have no false negatives.  usage: window_spotcheck.py N SEED NPROC OUT.json"""
import sys, json, random, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import mitm, rho2, lp
from multiprocessing import Pool
def blk(letter, k):
    inv = {'x1': 'y1', 'x3': 'y3'}
    return [letter] * (2 * k) if k >= 0 else [inv[letter]] * (-2 * k)
def one(item):
    V, U, m, n = item
    W = list(V) + blk('x1', m) + blk('x3', n) + list(U)
    hw = rho2.halfword('l1.l1', W, 'u2.u2')
    return '.'.join(W), lp.J(hw) == {0: 1}
if __name__ == '__main__':
    N, seed, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    P = mitm.P; t = random.Random(3).randrange(2, P - 1)
    MT, VT, PHIT = rho2.normalised()
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}]
    Vv = [[mitm.evt(x, t) for x in VT['l1.l1']]]
    c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
    PH = [[mitm.evt(x, t) * c % P for x in PHIT['u2.u2']]]
    tops = [w for w, _ in mitm.bfs(Ms, Vv, 4, 'top')]; bots = [w for w, _ in mitm.bfs(Ms, PH, 4, 'bot')]
    pairs = [(a, b) for a in tops for b in bots if mitm.knot_ok(mitm.top_class(a), mitm.bot_class(b))]
    rng = random.Random(seed)
    items = [(*rng.choice(pairs), rng.randint(-6, 6), rng.randint(-6, 6)) for _ in range(N)]
    S = set(W for W, prov in json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s3a_items.json'))['items'])
    t0 = time.time()
    with Pool(nproc) as Pl: res = Pl.map(one, items, chunksize=50)
    j1 = [W for W, ok in res if ok]
    missing = [W for W in j1 if W not in S]
    summ = {'tops': len(tops), 'bottoms': len(bots), 'junctions_knot_ok': len(pairs), 'sampled_points': N, 'J1_points': len(j1),
            'J1_points_NOT_in_window_list': len(missing), 'examples_missing': missing[:10], 'secs': round(time.time() - t0, 1)}
    print(json.dumps(summ)); json.dump(summ, open(outp, 'w'), indent=1)
