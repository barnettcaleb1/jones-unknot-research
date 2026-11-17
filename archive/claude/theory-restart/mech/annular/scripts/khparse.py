#!/usr/bin/env python3
"""Parse kht++ chain files (cxBNr / cxKhr) into generator lists and first-order arrows.
Degree rule (lit/kht/REPORT.md 2.4): arrow x --a--> y: h(y)=h(x)+1, q(y)=q(x)+deg a, deg S^k = k, deg D^k = 2k.
Unlabelled '—>' is D; unlabelled '~>' is S between different idempotents, S^2 between equal ones.
Idempotents (current kht++ build): '⬮' = Q_0 (horizontal), '⬯' = Q_inf (vertical)."""
import re, glob, os
from collections import Counter

GEN = '⬮⬯'
def parse_line(line):
    m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(\S+)(.*)$', line)
    if not m: return None
    h, q, chain, rest = int(m.group(1)), int(m.group(2)), m.group(4), m.group(5).strip()
    toks = re.findall(r'[⬮⬯]|[^⬮⬯]+', chain)
    gens = [t for t in toks if t in GEN]; arrows = [t for t in toks if t not in GEN]
    return h, q, gens, arrows, rest

def arrow_info(a, il, ir):
    direction = +1 if a.endswith('>') else -1
    assert a.endswith('>') != a.startswith('<'), a
    m = re.search(r'\(?-?([SDH])\)?(?:\^(\d+))?', a)
    if m:
        kind = m.group(1); power = int(m.group(2) or 1)
    else:
        kind = 'S' if '~' in a else 'D'
        power = 2 if (kind == 'S' and il == ir) else 1
    return direction, kind, power

def component(h, q, gens, arrows):
    """returns dict: gens=[(idem,h,q)], arrows=[(src_index,dst_index,kind,power)], cyclic, ok"""
    n = len(gens)
    out = [(gens[0], h, q)]
    arr = []
    cyclic = (len(arrows) == n)
    for i in range(n - 1):
        d, kind, p = arrow_info(arrows[i], gens[i], gens[i+1])
        deg = p if kind == 'S' else 2*p
        _, hh, qq = out[-1]
        out.append((gens[i+1], hh + d, qq + d*deg))
        arr.append((i, i+1, kind, p) if d == 1 else (i+1, i, kind, p))
    ok = True
    if cyclic:
        d, kind, p = arrow_info(arrows[n-1], gens[n-1], gens[0])
        deg = p if kind == 'S' else 2*p
        _, hh, qq = out[-1]
        ok = (hh + d == out[0][1]) and (qq + d*deg == out[0][2])
        arr.append((n-1, 0, kind, p) if d == 1 else (0, n-1, kind, p))
    return dict(gens=out, arrows=arr, cyclic=cyclic, ok=ok)

def parse_file(fn):
    comps = []
    for line in open(fn, encoding='utf-8'):
        r = parse_line(line)
        if not r: continue
        h, q, gens, arrows, rest = r
        c = component(h, q, gens, arrows)
        c['label'] = rest
        comps.append(c)
    return comps

def label_info(label):
    """parse 's4(∞) q^54 δ_^13' or 'r(-8) q^568/9 δ|^25/2'"""
    from fractions import Fraction
    m = re.match(r'([rs])(\d*)\(([^)]*)\)\s*q\^(-?[\d/]+)\s*δ[_|]\^(-?[\d/]+)', label)
    if not m: return None
    return dict(type=m.group(1), len=m.group(2), slope=m.group(3), q=Fraction(m.group(4)), delta=Fraction(m.group(5)))

def W_of(comps, idem='⬯'):
    """multiset of (h,q) of generators at idem"""
    c = Counter()
    for comp in comps:
        for (i, h, q) in comp['gens']:
            if i == idem: c[(h, q)] += 1
    return c
