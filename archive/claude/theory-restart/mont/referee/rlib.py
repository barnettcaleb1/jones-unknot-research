"""Referee helpers (independent of nest/nlib.py): random bodies, pinning with many closures, exact division."""
import sys, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
from lp import *

def pdiv(p, d):
    """exact Laurent division p/d or None (quotient degrees forced: [min p - min d, max p - max d])"""
    p = dict(p)
    if not p:
        return {}
    if not d:
        return None
    q = {}
    dt = max(d); dc = d[dt]; db = min(d)
    lo = min(p) - db
    while p:
        e = max(p); c = p[e]
        k = e - dt
        if k < lo or c % dc:
            return None
        q[k] = c // dc
        p = sub(p, mul({k: c // dc}, d))
    return clean(q)

def unitmul(s, k, p):
    return {e + k: s * c for e, c in p.items()}

def Xpow(k):
    R = [[ONE, {}], [{}, ONE]]
    M = Xm if k >= 0 else Xi
    for _ in range(abs(k)):
        R = mmul(R, M)
    return R

_DK = {}
def dk(k):
    """e_1^T X^{-k} e_2"""
    if k not in _DK:
        _DK[k] = Xpow(-k)[0][1]
    return _DK[k]

def twist(k):
    return ['y1'] * k if k >= 0 else ['x1'] * (-k)

def neck(k, bodies):
    """body word r2.(y1)^k.B1...Bn.u1 (string, no s.)"""
    toks = ['r2'] + twist(k)
    for b in bodies:
        toks += [t for t in b.split('.') if t]
    toks += ['u1']
    return '.'.join(toks)

def pin(B, ks=(1, -1, 2, -2, 3), cache=None):
    """all candidate vectors v (v1 = J(s.B)) with normalize(e1^T X^-k v) = J(s.neck(k,[B])) for all k in ks.
    returns (cands, Js) ; cands empty if none"""
    a = J('s.' + B)
    if a is None:
        return None, None
    Js = {}
    for k in ks:
        Js[k] = J('s.' + neck(k, [B]))
        if Js[k] is None:
            return None, None
    k0 = ks[0]
    d0 = dk(k0)
    cands = []
    for e in range(-120, 121):
        for s in (1, -1):
            num = sub(unitmul(s, e, Js[k0]), a)
            q = pdiv(num, d0)
            if q is None:
                continue
            v = [a, q]
            ok = True
            for k in ks[1:]:
                if normalize(add(a, mul(dk(k), q))) != Js[k]:
                    ok = False; break
            if ok:
                cands.append(v)
    return cands, Js

def rand_body(rnd, maxlen=12, maxw=5, p_axis=0.3):
    """random body: one half-strand in, one out; letters x_i,y_i (i>=0), l_i/r_i caps, u_i cups."""
    for _ in range(200):
        w = 1; toks = []
        L = rnd.randint(3, maxlen)
        for step in range(L):
            r = rnd.random()
            if w < maxw and r < 0.25:
                i = rnd.randint(1, w + 1)
                toks.append(rnd.choice('lr') + str(i)); w += 2
            elif w >= 3 and r < 0.4:
                i = rnd.randint(1, w - 1)
                toks.append('u' + str(i)); w -= 2
            else:
                if rnd.random() < p_axis or w == 1:
                    i = 0
                else:
                    i = rnd.randint(1, w - 1)
                toks.append(rnd.choice('xy') + str(i))
        while w > 1:
            # close up
            if rnd.random() < 0.5 and w >= 2:
                i = rnd.randint(1, w - 1)
                toks.append(rnd.choice('xy') + str(i))
            i = rnd.randint(1, w - 1)
            toks.append('u' + str(i)); w -= 2
        # reduce trivial cancellations x_i y_i adjacent
        out = []
        for t in toks:
            if out and out[-1][1:] == t[1:] and out[-1][0] in 'xy' and t[0] in 'xy' and out[-1][0] != t[0]:
                out.pop()
            else:
                out.append(t)
        if not any(t[0] in 'xy' for t in out):
            continue
        B = '.'.join(out)
        return B
    return None

def nax(B):
    return sum(1 for t in B.split('.') if t in ('x0', 'y0'))

def eps(v):
    return ev(b_of(v), -1)

def fmt(p):
    if not p:
        return '0'
    return ' '.join(('%+d' % c) + ('t^%d' % e if e else '') for e, c in sorted(p.items()))
