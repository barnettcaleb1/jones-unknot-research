"""Build explicit generic tables realising a feasible (target,k) from exhaustive.py, and cross-validate
exhaustive.py against the independent brute-force unit detector of wbf.py."""
import random, sys
from fractions import Fraction
from wbf import SECT, IJ, Table, trim, proportional, rand_poly, mono, pmul
from exhaustive import analyse_target, rref_info, BOUND

def construct(m0, n0, Wn, Dco, k, rng):
    sig = {s: 2*IJ[s][0]*m0 + 2*IJ[s][1]*n0 for s in SECT}
    cols = [(s, j) for s in SECT for j in range(Wn+1)]
    lo = min(sig.values()); hi = max(sig.values()) + Wn
    nrow = hi - lo + 1
    A = [[Fraction(0)]*len(cols) for _ in range(nrow)]
    for ci, (s, j) in enumerate(cols):
        A[sig[s]+j-lo][ci] = Fraction(1)
    rhs = [Fraction(0)]*nrow
    for i, c in enumerate(Dco):
        e = k + i
        if not (lo <= e <= hi): return None
        rhs[e-lo] = Fraction(c)
    pivots, R, M, leftnull = rref_info(A, nrow, len(cols))
    if any(sum(y*b for y, b in zip(row, rhs)) != 0 for row in leftnull): return None
    free = [c for c in range(len(cols)) if c not in pivots]
    x = [Fraction(0)]*len(cols)
    for f in free: x[f] = Fraction(rng.randint(-5, 5))
    for i, pc in enumerate(pivots):
        x[pc] = sum(y*b for y, b in zip(M[i], rhs)) - sum(R[i][f]*x[f] for f in free)
    # clear denominators
    from math import lcm
    den = 1
    for v in x: den = lcm(den, v.denominator)
    p = {}
    for s in SECT:
        cs = [int(x[cols.index((s, j))]*den) for j in range(Wn+1)]
        p[s] = trim(0, cs)
    return p

if __name__ == '__main__':
    rng = random.Random(7)
    Dlist = [('1', [1]), ('1+t', [1, 1]), ('1+t+t^2', [1, 1, 1]), ('(1+t^2)(1+t+t^2)', [1, 1, 2, 1, 1]), ('1-t^3', [1,0,0,-1])]
    # (i) positive results realise as genuine units with all six boundary sectors nonzero
    npos = 0; nbad = 0
    for name, Dco in Dlist:
        SD = len(Dco)-1
        for Wn in range(0, 4):
            B = max(1, Wn, SD); Rb = 3*B + 3
            for m0 in range(-Rb, Rb+1):
                for n0 in range(-Rb, Rb+1):
                    if m0 == 0 or n0 == 0: continue
                    ks = analyse_target(m0, n0, Wn, Dco, SD)
                    for k in ks[:2]:
                        for attempt in range(5):
                            p = construct(m0, n0, Wn, Dco, k, rng)
                            if p is not None and all(p[s] is not None for s in BOUND): break
                        D = trim(0, list(Dco))
                        ok = p is not None and all(p[s] is not None for s in BOUND)
                        if ok:
                            T = Table(p, D)
                            ok = T.is_unit(m0, n0) and T.W <= Wn
                        npos += 1
                        if not ok:
                            nbad += 1
                            print('FAILED realisation', name, Wn, (m0, n0), k)
    print('positive results realised:', npos, 'failures:', nbad)
    # (ii) negative results: random tables with supports in [0,W]; every off-axis unit must be predicted feasible
    nunits = 0; miss = 0
    for trial in range(400):
        name, Dco = rng.choice(Dlist); SD = len(Dco)-1
        D = trim(0, list(Dco))
        Wn = rng.randint(0, 3)
        p = {}
        for s in SECT:
            if rng.random() < 0.5:
                p[s] = rand_poly(rng, 0, Wn, 1)
            else:
                p[s] = pmul(D, rand_poly(rng, 0, max(0, Wn-SD), 1)) if Wn >= SD else rand_poly(rng, 0, Wn, 1)
        if rng.random() < 0.3: p['22'] = None
        # adversarial: force wall structure sometimes
        if rng.random() < 0.5 and p['20'] is not None:
            p['42'] = (p['20'][0], [-c for c in p['20'][1]])
        if rng.random() < 0.5 and p['02'] is not None:
            p['24'] = (p['02'][0], [-c for c in p['02'][1]])
        if rng.random() < 0.3 and p['00'] is not None:
            p['44'] = (p['00'][0], [rng.choice([-1, 1])*c for c in p['00'][1]])
        if any(p.get(s) is None for s in BOUND): continue
        T = Table(p, D)
        R = 3*max(1, Wn, SD) + 3
        for m0 in range(-R, R+1):
            for n0 in range(-R, R+1):
                if m0 == 0 or n0 == 0: continue
                if T.is_unit(m0, n0):
                    nunits += 1
                    if not analyse_target(m0, n0, Wn, Dco, SD):
                        miss += 1; print('MISSED', name, Wn, (m0, n0))
    print('random off-axis units found:', nunits, 'missed by exhaustive analyser:', miss)
