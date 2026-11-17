"""refGen: INDEPENDENT re-implementation of the C1 theorem generator (own derivation, own code; imports only rg_core).

Setting.  F = S1 + S2,  S1 = w1 * A,  S2 = w2 * t^-3N * B  (A, B = products of the a- resp. b-channels of the box B0 and of
n non-integral rational boxes); horizontal: (w1, w2) = (w_1(mu), w_3(mu)), vertical: (w_1(a), wV(a)).  J is a unit iff
F = c t^e Phi_3.  At an end write s1, s2 for the normalised expansions of S1, S2, X_i = l1(s_i), off = deg S1 - deg S2,
e = lc S2 / lc S1 (= +-1 for admissible boxes).  Unknown rational sums: alpha = sum rho_a, P = sum rho_q, La = sum l2(a),
Lam = sum l2(q).  Then X1 = p1 + ra + alpha, X2 = q1 + rb + alpha + P, l2(s1) = p2 + la + La, l2(s2) = q2 + lb + La + Lam
((p1,p2),(q1,q2) = log-jets of w1, w2 at the end; (ra,la,rb,lb) = log-jets of a_B0, b_B0 at the end).
Weak-end pin: X2 - X1 = s1(Q) - s1(q*) = m_B := sigma(B0) - sigma*  (strong end has r >= 2; rational sigma = 0).
Phi_3 pattern at the weak end: normalised F = 1 + u + u^2 + ...  -> linear equations (see CASES below).
Certificate: y with g = sum_j y_j c_j, s = sup over ALL rational boxes of g . (rho_a, rho_q, l2a, l2q) (exact longest path on
OUR automaton), and   [n free, n >= nmin]: s <= 0 and y.r > nmin s,   [n pinned]: y.r > n s.
"""
import sys, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_core as C
from fractions import Fraction as Fr

KA = 3
_ST, _T = C.build_auto(KA)
# deduplicated edges (s, ns, l1(D), l2(D)) and final vectors FIN[s] = (rho_q, lambda_q)
EDGES = sorted(set((repr(s), repr(ns)) + tuple(C.logjet(Dj[2])[:2]) for (s, m), (Dj, ns) in _T.items()))
SN = sorted(set([e[0] for e in EDGES] + [e[1] for e in EDGES]))
SI = {s: i for i, s in enumerate(SN)}
EI = [(SI[a], SI[b], l1, l2) for a, b, l1, l2 in EDGES]
INIT = SI[repr('init')]
FIN = {}
for s in _ST:
    if s == 'init': continue
    lq = C.logjet(C.q_end(s, KA)[2])
    FIN[SI[repr(s)]] = (lq[0], lq[1])
_cache = {}
def sup(g):
    """exact sup over all non-integral rational boxes of g . (rho_a, rho_q, l2(a), l2(q)); None = +infinity"""
    g = tuple(Fr(x) for x in g)
    if g in _cache: return _cache[g]
    ga, gq, gl, gL = g
    n = len(SN); best = [None] * n; best[INIT] = Fr(0)
    for it in range(n):
        ch = False
        for a, b, l1, l2 in EI:
            if best[a] is None: continue
            v = best[a] + ga * l1 + gl * l2
            if best[b] is None or v > best[b]:
                best[b] = v; ch = True
        if not ch: break
    # one more pass: any improvement means a positive cycle is reachable -> +infinity
    for a, b, l1, l2 in EI:
        if best[a] is not None and (best[b] is None or best[a] + ga * l1 + gl * l2 > best[b]):
            _cache[g] = None; return None
    r = max(best[i] + gq * FIN[i][0] + gL * FIN[i][1] for i in FIN if best[i] is not None)
    _cache[g] = r
    return r

# ---------------- closure twist factors ----------------
def tm(k): return {k: (-1) ** (k % 2)}            # (-t)^k
PHI5 = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
T2P1 = {0: 1, 2: 1}
def w1(x): return C.padd({1: 1}, C.pmul(tm(x), T2P1))                     # t + (1+t^2)(-t)^x
def w3(mu): return C.pmul(T2P1, C.psub({0: 1}, tm(mu)))                    # (1+t^2)(1-(-t)^mu)
def wV(a): return C.padd(C.pshift(tm(a), 1), C.pshift(PHI5, 3 * a - 1))   # (-t)^a t + t^(3a-1) Phi_5
def wjets(p, q):
    """per end: ((p1,p2),(q1,q2)), plus sigma* = sum_ends [l1(p)-l1(q)] and delta* = span p - span q"""
    out = {}
    for end in ('top', 'bot'):
        dp, cp, xp = C.enddata(p, end, 2); dq, cq, xq = C.enddata(q, end, 2)
        out[end] = (C.logjet(xp), C.logjet(xq))
    sig = sum(out[e][0][0] - out[e][1][0] for e in out)
    dstar = (max(p) - min(p)) - (max(q) - min(q))
    return out, sig, dstar
# closure classes: name -> (w-jets per end, sigma*, n-rule) ; n-rule(deltaB) -> ('pin', n) or ('min', n0) for the off=0 case
def vclasses():
    out = {}
    # a = 3, -3 exactly; a >= 5, a <= -5 as classes (stability checked in rg_q3_wdata.py for |a| <= 41)
    for name, a in (('a=3', 3), ('a=-3', -3), ('a>=5', 5), ('a<=-5', -5)):
        o, sg, ds = wjets(w1(a), wV(a))
        assert ds == -abs(a) - 1
        if abs(a) == 3: rule = lambda dB: ('pin', dB + 4)
        else: rule = lambda dB: ('min', dB + 6)
        out[name] = (o, sg, rule)
    return out
def hclasses():
    out = {}
    for name, mu in (('mu=1', 1), ('mu=-1', -1), ('mu=2', 2), ('mu=-2', -2), ('mu=3', 3), ('mu=-3', -3),
                     ('mu>=4', 4), ('mu<=-4', -4)):
        o, sg, ds = wjets(w1(mu), w3(mu))
        out[name] = (o, sg, (lambda ds_: (lambda dB: ('pin', dB - ds_)))(ds))
    return out
VCL = vclasses(); HCL = hclasses()

# ---------------- weak-end cases (own derivation) ----------------
def cases(pw, qw, Bd, mB):
    """pw=(p1,p2), qw=(q1,q2) w-jets at the weak end; Bd=(ra,la,rb,lb); mB = X2 - X1 (weak-end mismatch).
       Returns list of (name, rows, off0) with rows [(c_alpha, c_P, c_La, c_Lam, rhs)], off0 True for offset-0 cases.
       Unknowns (alpha, P, La, Lam).  Always includes the pin row P = P0."""
    p1, p2 = pw; q1, q2 = qw; ra, la, rb, lb = Bd
    K1 = p1 + ra; K2 = q1 + rb; M1 = p2 + la; M2 = q2 + lb
    P0 = mB + K1 - K2                      # from X2 - X1 = K2 + alpha + P - K1 - alpha = mB
    pin = (0, 1, 0, 0, P0)
    H = Fr(1, 2)
    out = []
    # X1 = K1 + alpha ; X2 = K2 + alpha + P ; l2(s1) = M1 + La ; l2(s2) = M2 + La + Lam ; x2 = l2 + l1^2/2
    out.append(('off>=3', [(1, 0, 0, 0, 1 - K1), (0, 0, 1, 0, H - M1), pin], False))
    for e in (1, -1):
        out.append(('off=2 e=%+d' % e, [(1, 0, 0, 0, 1 - K1), (0, 0, 1, 0, 1 - e - H - M1), pin], False))
        X1 = 1 - e                         # X1 + e = 1
        # l2(s1) + X1^2/2 + e*X2 = 1  ->  La + e*alpha + e*P = 1 - M1 - X1^2/2 - e*K2
        out.append(('off=1 e=%+d' % e, [(1, 0, 0, 0, X1 - K1), (e, e, 1, 0, 1 - M1 - Fr(X1 * X1, 2) - e * K2), pin], False))
        X2 = 1 - e                         # X2 + e = 1
        # l2(s2) + X2^2/2 + e*X1 = 1  ->  La + Lam + e*alpha = 1 - M2 - X2^2/2 - e*K1
        out.append(('off=-1 e=%+d' % e, [(1, 1, 0, 0, X2 - K2), (e, 0, 1, 1, 1 - M2 - Fr(X2 * X2, 2) - e * K1), pin], False))
        out.append(('off=-2 e=%+d' % e, [(1, 1, 0, 0, 1 - K2), (0, 0, 1, 1, 1 - e - H - M2), pin], False))
    out.append(('off<=-3', [(1, 1, 0, 0, 1 - K2), (0, 0, 1, 1, H - M2), pin], False))
    # off = 0, e = +1 (no cancellation): X1 + X2 = 2 and x2(s1) + x2(s2) = 2
    X1 = 1 - Fr(mB, 2); X2 = 1 + Fr(mB, 2)
    out.append(('off=0 e=+1', [(2, 1, 0, 0, 2 - K1 - K2), (0, 0, 2, 1, 2 - M1 - M2 - X1 * X1 / 2 - X2 * X2 / 2), pin], True))
    # off = 0, e = -1, r = 1 exactly (mB != 0): x2(s1) - x2(s2) = X1 - X2 = -mB
    #   l2(s1) - l2(s2) + (X1^2 - X2^2)/2 = -mB,  (X1^2-X2^2)/2 = -mB*X1 - mB^2/2,  X1 = K1 + alpha
    #   -> Lam + mB*alpha = mB + M1 - M2 - mB*K1 - mB^2/2
    if mB != 0:
        out.append(('off=0 e=-1 r=1', [(mB, 0, 0, 1, mB + M1 - M2 - mB * K1 - Fr(mB * mB, 2)), pin], True))
    return out

# ---------------- certificate search ----------------
GRID = sorted(set([Fr(x) for x in (0, 1, -1, 2, -2, 3, -3, 5, -5, 10, -10, 100, -100)] +
                  [Fr(1, 2), Fr(-1, 2), Fr(1, 3), Fr(-1, 3), Fr(3, 2), Fr(-3, 2), Fr(2, 3), Fr(-2, 3)]))
def _dirs(m):
    seen = set(); out = []
    for ys in itertools.product(GRID, repeat=m):
        if all(y == 0 for y in ys): continue
        mx = max(abs(y) for y in ys); d = tuple(y / mx for y in ys)
        if d in seen: continue
        seen.add(d); out.append(ys)
    return out
DIRS = {2: _dirs(2), 3: _dirs(3)}
_gtab = {}
def gtable(coeffs):
    """for a coefficient matrix (tuple of 4-vectors), list of (ys, g, s) with finite exact sup, sorted by s"""
    if coeffs in _gtab: return _gtab[coeffs]
    out = []
    for ys in DIRS[len(coeffs)]:
        g = tuple(sum(y * c[j] for y, c in zip(ys, coeffs)) for j in range(4))
        s = sup(g)
        if s is not None: out.append((ys, g, s))
    out.sort(key=lambda x: x[2])
    _gtab[coeffs] = out
    return out
def certify(rows, nrule):
    """nrule: ('min', n0) n >= n0 free  or ('pin', n).  Returns certificate (ys, g, s, yr) or None."""
    coeffs = tuple(tuple(Fr(x) for x in r[:4]) for r in rows); rhs = [Fr(r[4]) for r in rows]
    kind, n0 = nrule
    if kind == 'pin' and n0 < 0:
        return ('impossible n', n0)
    for ys, g, s in gtable(coeffs):
        yr = sum(y * r for y, r in zip(ys, rhs))
        if kind == 'min':
            if s <= 0 and yr > max(n0, 0) * s: return (ys, g, s, yr)
        else:
            if yr > n0 * s: return (ys, g, s, yr)
    return None
def check_cert(rows, nrule, ys):
    """exact re-check of a given multiplier vector ys (e.g. a witness produced by C1's search)"""
    coeffs = [tuple(Fr(x) for x in r[:4]) for r in rows]; rhs = [Fr(r[4]) for r in rows]
    g = tuple(sum(Fr(y) * c[j] for y, c in zip(ys, coeffs)) for j in range(4))
    s = sup(g)
    if s is None: return False
    yr = sum(Fr(y) * r for y, r in zip(ys, rhs))
    kind, n0 = nrule
    if kind == 'min': return s <= 0 and yr > max(n0, 0) * s
    return n0 < 0 or yr > n0 * s

def prove(Bdata, sigB, deltaB, nmin, which=('V', 'H'), want=False):
    """Bdata = {'top': (ra,la,rb,lb), 'bot': (...)}; returns dict class -> list of open cases ([] = proved),
       and (if want) the certificates"""
    res = {}; certs = {}
    for fam in which:
        CL = VCL if fam == 'V' else HCL
        for name, (o, sgs, rule) in CL.items():
            mB = sigB - sgs
            opn = []
            r0 = rule(deltaB)
            # admissible n for the offset-0 cases: both ends coincide -> delta-law
            if r0[0] == 'pin':
                nr0 = ('pin', r0[1]) if r0[1] >= nmin else ('pin', -1)
            else:
                nr0 = ('min', max(nmin, r0[1]))
            if mB == 0:
                # both ends may tie to order >= 2 when both coincide; only possible at the off=0 n
                if not (nr0[0] == 'pin' and nr0[1] < 0):
                    opn.append('mB=0: two-ended tie possible (%s)' % (nr0,))
            for end in ('top', 'bot'):
                pw, qw = o[end]
                for cname, rows, off0 in cases(pw, qw, Bdata[end], mB):
                    nr = nr0 if off0 else ('min', nmin)
                    c = certify(rows, nr)
                    if c is None: opn.append(end + ':' + cname)
                    elif want: certs[(fam, name, end, cname)] = c
            res[(fam, name)] = opn
    return (res, certs) if want else res

def bdata_from_vec(a, b):
    """end data of a (non-rational) box from exact channels a, b: Bdata, sigma, delta, lc-admissible, span a"""
    Bd = {}; lcok = True; s1 = {}
    for end in ('top', 'bot'):
        da, ca, xa = C.enddata(a, end, 2); db, cb, xb = C.enddata(b, end, 2)
        la = C.logjet(xa); lb = C.logjet(xb)
        Bd[end] = (la[0], la[1], lb[0], lb[1])
        if abs(Fr(cb, ca)) != 1: lcok = False
        s1[end] = (db - da, lb[0] - la[0])
    sigma = s1['top'][1] + s1['bot'][1]
    delta = s1['top'][0] - s1['bot'][0]
    return Bd, sigma, delta, lcok, max(a) - min(a)

if __name__ == '__main__':
    import time
    t0 = time.time()
    Z = (Fr(0),) * 4
    ZB = {'top': Z, 'bot': Z}
    print('automaton K=3: %d states, %d deduplicated edges' % (len(SN), len(EI)))
    r = prove(ZB, Fr(0), 0, 2, which=('H',))
    print('SANITY Q-MONT (rational only, n>=2, every mu):', {k: v for k, v in r.items()}, round(time.time() - t0, 1))
    r = prove(ZB, Fr(0), 0, 1, which=('V',))
    print('SANITY V3 (rational only, n>=1, every odd |a|>=3):', r, round(time.time() - t0, 1))
    r = prove(ZB, Fr(0), 0, 1, which=('H',))
    print('NEGATIVE CONTROL (rational only, n>=1, horizontal; units exist at n=1):', r, round(time.time() - t0, 1))

import pickle as _pk
def dump_gtab(path):
    _pk.dump(dict(gtab=_gtab, cache=_cache), open(path, 'wb'))
def load_gtab(path):
    d = _pk.load(open(path, 'rb'))
    _gtab.update(d['gtab']); _cache.update(d['cache'])
