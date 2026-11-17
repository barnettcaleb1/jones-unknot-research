"""Adversarial check of the Tietze certifier: it must NEVER certify a knot with V_K != 1; and should certify most V_K = 1 knots."""
import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
import tietze, kcert, rho2
from multiprocessing import get_context
LET = ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']
def job(seed):
    rnd = random.Random(seed); out = {'nontriv': 0, 'nontriv_certified': 0, 'unknot': 0, 'unknot_certified': 0, 'bad': []}
    n = 0
    while n < 40:
        W = [rnd.choice(LET) for _ in range(rnd.randint(4, 14))]
        if not rho2.is_knot('l1.l1', W, 'u2.u2'): continue
        hw = rho2.halfword('l1.l1', W, 'u2.u2'); n += 1
        st, why = kcert.certify(hw)
        ok, steps = tietze.certify(hw)
        if st == 'nontrivial':
            out['nontriv'] += 1
            if ok: out['nontriv_certified'] += 1; out['bad'].append(hw)
        else:
            out['unknot'] += 1
            if ok:
                out['unknot_certified'] += 1
                assert tietze.replay(hw, steps)
    return out
if __name__ == '__main__':
    with get_context('spawn').Pool(8) as pool: rs = pool.map(job, range(16))
    tot = {}
    for r in rs:
        for k, v in r.items():
            if k != 'bad': tot[k] = tot.get(k, 0) + v
    print(tot, 'bad:', [b for r in rs for b in r['bad']][:5])
