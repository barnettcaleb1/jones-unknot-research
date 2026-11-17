#!/usr/bin/env python3
"""Decategorified pairing check for the trefoil quotient tangle (kht++ -q framing).
Basis of the skein module: e0 = ⬮ (1-3 picture: top<->b3, b1<->b2), einf = ⬯ (top<->b1, b2<->b3).
Unshifted Khovanov bracket of an appended crossing on (b1,b2):  y0: e_inf -> e_inf - q e0, e0 -> -q^2 e0;
x0: e_inf -> e0 - q e_inf, e0 -> q^-1 e0.  Closure u1 (join b2,b3): e0 -> 1, e_inf -> q+q^-1.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from khtparse import parse_line, gens_with_gradings, euler_vec, pstr
from collections import defaultdict

def padd(a, b, s=1):
    r = defaultdict(int)
    for e, c in a.items(): r[e] += c
    for e, c in b.items(): r[e] += s*c
    return {e: c for e, c in r.items() if c}
def pmul(a, b):
    r = defaultdict(int)
    for e, c in a.items():
        for f, d in b.items(): r[e+f] += c*d
    return {e: c for e, c in r.items() if c}
Q = {1: 1}; Qi = {-1: 1}; ONE = {0: 1}; D = {1: 1, -1: 1}

def twist(v, kind):
    x0, xi = v
    if kind == 'y':   # e_inf -> e_inf - q e0 ; e0 -> -q^2 e0
        return (padd(pmul(x0, {2: -1}), pmul(xi, {1: -1})), xi)
    else:             # x: e_inf -> e0 - q e_inf ; e0 -> q^-1 e0
        return (padd(pmul(x0, Qi), xi), pmul(xi, {1: -1}))
def close_u1(v): return padd(v[0], pmul(v[1], D))
def close_u0(v): return padd(pmul(v[0], D), v[1])

def read_components(fn):
    comps = []
    for line in open(fn, encoding='utf-8'):
        r = parse_line(line)
        if not r: continue
        h, q, gens, arrows, rest = r
        gl, cyc, ok = gens_with_gradings(h, q, gens, arrows)
        ev = euler_vec(gl)
        comps.append((rest, (ev['⬮'], ev['⬯'])))
    return comps

def chi_of_CKh(fn, mode='Kh'):
    """graded Euler characteristic of reduced Khovanov homology read from a cxCKh file (towers + H^n pairs)."""
    import re
    p = defaultdict(int); tors = []
    for line in open(fn, encoding='utf-8'):
        m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*\S+\s*(\S+)', line)
        if not m: continue
        h, q, chain = int(m.group(1)), int(m.group(2)), m.group(3)
        p[q] += (-1)**(h % 2)
        mm = re.search(r'H(?:\^(\d+))?', chain)
        if mm:
            n = int(mm.group(1) or 1); tors.append(n)
            p[q + 2*n] += (-1)**((h+1) % 2)
    return {e: c for e, c in p.items() if c}, sorted(tors)

def pdiv_qqinv(p):
    """exact division by (q - q^-1); raises if not divisible"""
    # p = (q - q^-1) r  <=>  q p = (q^2 - 1) r ; solve from the bottom: r_e = -(qp)_e + r_{e-2}
    qp = {e+1: c for e, c in p.items()}
    if not qp: return {}
    r = {}; lo, hi = min(qp), max(qp)
    e = lo
    while e <= hi:
        val = -qp.get(e, 0) + r.get(e-2, 0)
        if val: r[e] = val
        e += 1
    # check
    chk = padd(pmul(r, {1: 1, -1: -1}), p, -1)
    assert not chk, 'not divisible by q - q^-1'
    return r

def normalise(p):
    """divide by the lowest monomial and make leading coefficient positive: returns (sign, shift, poly)"""
    if not p: return (1, 0, {})
    e0 = min(p); s = 1 if p[e0] > 0 else -1
    return (s, e0, {e-e0: s*c for e, c in p.items()})

if __name__ == '__main__':
    base = sys.argv[1]   # folder with cxKhr-c2-q of the tangle
    cdir = sys.argv[2]   # folder with closures
    comps = read_components(os.path.join(base, 'cxKhr-c2-q'))
    tot = ({}, {})
    for name, v in comps: tot = (padd(tot[0], v[0]), padd(tot[1], v[1]))
    print('total Khr Euler vector: e0:', pstr(tot[0]), '| einf:', pstr(tot[1]))
    print('closure u1 (slope inf) per component:')
    for name, v in comps: print('   ', name.split()[0], '->', pstr(close_u1(v)))
    for kind, tag in (('y', 'y0'), ('x', 'x0')):
        for n in range(1, 6):
            fn = os.path.join(cdir, 'c_%s%d_u1' % (tag, n), 'cxCKh-c2')
            actual, tors = chi_of_CKh(fn)
            parts = []
            for name, v in comps:
                w = v
                for _ in range(n): w = twist(w, kind)
                parts.append((name.split()[0], pdiv_qqinv(close_u1(w))))
            pred = {}
            for _, p in parts: pred = padd(pred, p)
            sa, ea, na = normalise(actual); sp, ep, np_ = normalise(pred)
            # Kh~ = cone(H) so chi(Kh~ from Khr-curves) should equal chi(actual Kh~) up to +-q^k
            print('\n%s^%d.u1: torsion orders %s' % (tag, n, tors))
            print('   V from kht++ closure  :', pstr(actual))
            print('   Khr-curve pairing /(q-1/q):', pstr(pred))
            print('   agree up to unit?', na == np_, '(unit: sign %+d, q^%d)' % (sa*sp, ea-ep))
            for nm, p in parts:
                print('   contribution of %-7s (same unit applied): %s' % (nm, pstr({e+ea-ep: sa*sp*c for e, c in p.items()})))
