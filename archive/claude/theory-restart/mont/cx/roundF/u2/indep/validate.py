"""u2/indep/validate.py -- FALSIFICATION test of the two global-disc implementations (up.py, down.py) and of their conventions.
Random two-site templates s.l1.l1.V.U.u2.u2 (|V|,|U| <= 6, letters x0..x3,y0..y3), one site X1 or X3 at the cut V|U (re-cuts
allowed).  If a test says 'disc', every member K_k (twist X^(2k) inserted at the cut, k = -2..2) must be the SAME knot; we check an
invariant fingerprint (|Delta(-1)|, |Delta(2)|, |Delta(3)|, tools/alex.py = the certifier's definition of K).  A disc verdict
on a family with a non-constant fingerprint would REFUTE the implementation.  Negative control: the same with a deliberately
wrong convention (pull-up and push-down exchanged) must produce violations, i.e. the check has power.
usage: validate.py N SEED NPROC OUT.json"""
import sys, os, json, random
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
from multiprocessing import Pool
from collections import Counter
LET = ['x0', 'x1', 'x2', 'x3', 'y0', 'y1', 'y2', 'y3']
def blk(site, k):
    L = 'x1' if site == 'X1' else 'x3'; Li = 'y1' if site == 'X1' else 'y3'
    return [L, L] * k if k >= 0 else [Li, Li] * (-k)
def fp(V, U, site, k):
    import alex
    W = V + blk(site, k) + U
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2' if W else 's.l1.l1.u2.u2'
    r = tuple(alex.alex_eval(hw, t) for t in (-1, 2, 3))
    return None if any(x is None for x in r) else r
def job(item):
    import up, down
    V, U, site, wrong = item
    if wrong:   # deliberately wrong convention: exchange the directions of the Artin action
        up.pull_up, up.push_down = up.push_down.__wrapped__ if hasattr(up.push_down, '__wrapped__') else WRONG_UP[0], WRONG_UP[1]
    W = V + U; j0 = len(V)
    ui, _ = up.family_test(W, j0, site, up.COMM[site])
    di, dr, _ = down.family_test(W, j0, site)
    fps = [fp(V, U, site, k) for k in range(-2, 3)]
    if any(f is None for f in fps): return None
    return (ui is not None, di is not None, len(set(fps)) == 1, '.'.join(V), '.'.join(U), site)
WRONG_UP = [None, None]
def init(wrong):
    if wrong:
        import up
        pu, pd = up.pull_up, up.push_down
        def wrong_pull(Ls, w): return pd(list(reversed(Ls)), w) if False else pd(Ls, w)
        def wrong_push(Ls, w): return pu(Ls, w)
        up.pull_up, up.push_down = wrong_pull, wrong_push
        import down
        dpu, dpd = down.pull_up, down.push_down
        down.pull_up, down.push_down = (lambda Ls, w: dpd(Ls, w)), (lambda Ls, w: dpu(Ls, w))
def job2(item):
    import up, down
    V, U, site = item
    W = V + U; j0 = len(V)
    ui, _ = up.family_test(W, j0, site, up.COMM[site])
    di, dr, _ = down.family_test(W, j0, site)
    if ui is None and di is None and random.random() > 0.15: return ('skip',)
    fps = [fp(V, U, site, k) for k in range(-2, 3)]
    if any(f is None for f in fps): return None
    return (ui is not None, di is not None, len(set(fps)) == 1, '.'.join(V), '.'.join(U), site)
if __name__ == '__main__':
    N, seed, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    wrong = len(sys.argv) > 5 and sys.argv[5] == 'WRONG'
    rng = random.Random(seed)
    items = []
    for _ in range(N):
        V = [rng.choice(LET) for _ in range(rng.randint(0, 6))]
        U = [rng.choice(LET) for _ in range(rng.randint(1, 6))]
        items.append((V, U, rng.choice(['X1', 'X3'])))
    with Pool(nproc, initializer=init, initargs=(wrong,)) as P: res = P.map(job2, items, chunksize=20)
    res = [r for r in res if r is not None and r[0] != 'skip']
    tab = Counter((r[0], r[1], r[2]) for r in res)
    viol_up = [r for r in res if r[0] and not r[2]]; viol_dn = [r for r in res if r[1] and not r[2]]
    summ = {'N': N, 'seed': seed, 'wrong_convention_control': wrong, 'knots_evaluated': len(res),
            'table (up_disc, down_disc, fingerprint_constant)': {str(k): v for k, v in tab.items()},
            'up_disc': sum(1 for r in res if r[0]), 'down_disc': sum(1 for r in res if r[1]),
            'agree_up_down': sum(1 for r in res if r[0] == r[1]),
            'VIOLATIONS_up': len(viol_up), 'VIOLATIONS_down': len(viol_dn),
            'violation_examples': (viol_up + viol_dn)[:10],
            'nonconstant_families_examined': sum(1 for r in res if not r[2])}
    json.dump(summ, open(outp, 'w'), indent=1)
    print(json.dumps(summ))
