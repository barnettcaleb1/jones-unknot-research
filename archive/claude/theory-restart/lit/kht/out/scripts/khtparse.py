#!/usr/bin/env python3
"""Parse kht++ chain strings (cxBNr / cxKhr / cxCKh lines) into generator lists with (idempotent, h, q).

Degree rule (calibrated in REPORT.md section 2): an arrow x --a--> y has h(y)=h(x)+1 and
q(y)=q(x)+d(a) with d(S^k)=k, d(D^k)=2k, d(H^k)=2k.  Unlabelled '—>' is D, '~>' is S; except that in the
Khr/BNr output only D, S and S^2 labels are suppressed, so an unlabelled '~>' between equal idempotents is S^2.
"""
import re, sys
from fractions import Fraction
from collections import defaultdict

GEN = '⬮⬯'
def parse_line(line):
    m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(\S+)(.*)$', line)
    if not m: return None
    h, q, chain, rest = int(m.group(1)), int(m.group(2)), m.group(4), m.group(5).strip()
    # tokenise chain into generators and arrows
    toks = re.findall(r'[⬮⬯]|[^⬮⬯]+', chain)
    gens = []; arrows = []  # arrows[i] between gens[i] and gens[i+1] (or wrap-around)
    for t in toks:
        if t in GEN: gens.append(t)
        else: arrows.append(t)
    return h, q, gens, arrows, rest

def arrow_info(a, src_idem_left, idem_right):
    """return (direction, kind, power). direction +1: left->right, -1: right->left."""
    direction = +1 if a.endswith('>') else -1
    assert (a.endswith('>')) != (a.startswith('<')), a
    kind = None; power = 1
    m = re.search(r'\(?-?([SDH])\)?(?:\^(\d+))?', a)
    if m:
        kind = m.group(1); power = int(m.group(2) or 1)
    else:
        if '~' in a: kind = 'S'
        elif '—' in a: kind = 'D'
        else: raise ValueError(a)
        if kind == 'S' and src_idem_left == idem_right: power = 2
    return direction, kind, power

def gens_with_gradings(h, q, gens, arrows):
    out = [(gens[0], h, q)]
    n = len(gens)
    cyclic = (len(arrows) == n) and n > 0
    for i in range(n-1):
        d, kind, p = arrow_info(arrows[i], gens[i], gens[i+1])
        deg = p if kind == 'S' else 2*p
        _, hh, qq = out[-1]
        out.append((gens[i+1], hh + d, qq + d*deg))
    ok = True
    if cyclic:
        d, kind, p = arrow_info(arrows[n-1], gens[n-1], gens[0])
        deg = p if kind == 'S' else 2*p
        _, hh, qq = out[-1]
        ok = (hh + d == out[0][1]) and (qq + d*deg == out[0][2])
    return out, cyclic, ok

def euler_vec(gl):
    """returns dict idem -> Laurent poly {qexp: coeff}"""
    v = {'⬮': defaultdict(int), '⬯': defaultdict(int)}
    for idem, h, q in gl:
        v[idem][q] += (-1)**(h % 2)
    return {k: {e: c for e, c in sorted(d.items()) if c} for k, d in v.items()}

def pstr(p):
    if not p: return '0'
    return ' '.join(('%+d' % c) + ('·q^%d' % e) for e, c in sorted(p.items()))

if __name__ == '__main__':
    for fn in sys.argv[1:]:
        print('#', fn)
        for line in open(fn, encoding='utf-8'):
            r = parse_line(line)
            if not r: continue
            h, q, gens, arrows, rest = r
            gl, cyc, ok = gens_with_gradings(h, q, gens, arrows)
            ev = euler_vec(gl)
            print('  component:', rest or '(non-compact)' if not cyc else rest, '| gens', len(gl), '| cyclic', cyc, '| closes consistently', ok,
                  '| mean q', Fraction(sum(g[2] for g in gl), len(gl)))
            print('    gens:', ' '.join('%s(h%d,q%d)' % g for g in gl))
            print('    chi[⬮] =', pstr(ev['⬮']))
            print('    chi[⬯] =', pstr(ev['⬯']))
