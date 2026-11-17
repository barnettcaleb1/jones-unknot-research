"""u2/indep/model_check.py -- validation of the UPSTAIRS group model (up.py conventions) against the certifier's knot.
In the upstairs model K = caps (1,2),(3,4),(5,6),(7,8) + braid W + cups (1,8)big,(2,3),(4,5),(6,7); its plat presentation is
    pi_1(S^3 - K) = F_4 / << psi_W(a2a3), psi_W(a4a5), psi_W(a6a7) >>      (one cup relation is redundant; the big cup is not used),
and pi_1(B~' - T~') of the global-disc test is the same construction without psi_W(a4a5).
CHECK 1 (random knots, |W| = 4..14): #Hom(G, S_3) from this presentation equals 3 + 3^(d+1) with 3 | det <=> d >= 1, where
det = |Delta(-1)| from tools/alex.py (the certifier's definition of K): the model must give #Hom > 6 exactly when 3 | det.
CHECK 2 (every U2 base knot): the relator TRIPLE Whitehead-reduces to single letters (G = Z): an independent unknot proof of the
base knot inside the upstairs model (not used as a certificate; the audited Tietze certificates are)."""
import sys, os, json, random, itertools
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
from multiprocessing import Pool
from collections import Counter
import up
from fg import free_quotient_solver, red
S3 = [p for p in itertools.permutations(range(3))]
def mul(p, q): return tuple(p[q[i]] for i in range(3))          # p o q
def pinv(p):
    r = [0] * 3
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
E = (0, 1, 2)
def ev(img, w):
    g = E
    for a in w: g = mul(g, img[a] if a > 0 else pinv(img[-a]))
    return g
def rels(W):
    return [up.psi_top(W, c) for c in ((up.sym(2), up.sym(3)), (up.sym(4), up.sym(5)), (up.sym(6), up.sym(7)))]
def nhom(R):
    n = 0
    for imgs in itertools.product(S3, repeat=4):
        img = {i + 1: imgs[i] for i in range(4)}
        if all(ev(img, r) == E for r in R): n += 1
    return n
def job1(W):
    import alex
    hw = 's.l1.l1.' + '.'.join(W) + '.u2.u2'
    d = alex.alex_eval(hw, -1)
    if d is None: return None
    n = nhom(rels(W))
    return (d % 3 == 0, n > 6, n, d)
def job2(Wb):
    f, k = free_quotient_solver(4, rels(list(Wb)))
    return f is not None and len(k) == 3
if __name__ == '__main__':
    rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
    LET = ['x0', 'x1', 'x2', 'x3', 'y0', 'y1', 'y2', 'y3']
    Ws = [[rng.choice(LET) for _ in range(rng.randint(4, 14))] for _ in range(4000)]
    with Pool(2) as P: res = [r for r in P.map(job1, Ws, chunksize=50) if r is not None]
    agree = sum(1 for a, b, n, d in res if a == b)
    print('CHECK 1: knots', len(res), 'model #Hom>6 <=> 3|det agreement', agree, 'with 3|det:', sum(1 for r in res if r[0]),
          'hom counts', dict(Counter(r[2] for r in res)))
    fams = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/families.json'))
    bases = sorted(set(tuple(f['base_word']) for f in fams if f['u2_target']))
    with Pool(2) as P: ok = P.map(job2, bases, chunksize=50)
    print('CHECK 2: distinct U2 base words', len(bases), 'model group = Z (triple reduces to 3 letters):', sum(ok))
    json.dump({'check1_knots': len(res), 'check1_agree': agree, 'check1_3divdet': sum(1 for r in res if r[0]),
               'check2_bases': len(bases), 'check2_Z': sum(ok)}, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/model_check.json', 'w'))
