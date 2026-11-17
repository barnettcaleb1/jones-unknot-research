#!/usr/bin/env python3
"""Parse raw kht++ output files (current build: '⬮' = bullet = idempotent of Q_0, '⬯' = circ = idempotent of Q_inf).
Degree rule: arrow x --a--> y: h(y)=h(x)+1, q(y)=q(x)+deg(a), deg(S^k)=k, deg(D^k)=2k.
Unlabelled '—' arrow is D; unlabelled '~' arrow is S between different idempotents, S^2 between equal ones."""
import re, os, glob, json
from fractions import Fraction

GEN = '⬮⬯'
IDEM = {'⬮': 0, '⬯': 1}   # 0 = bullet (Q_0), 1 = circ (Q_inf)

def parse_line(line):
    m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?[\d/]+)\s*(\S+)(.*)$', line)
    if not m: return None
    h, q, chain, rest = int(m.group(1)), int(m.group(2)), m.group(4), m.group(5).strip()
    toks = re.findall(r'[⬮⬯]|[^⬮⬯]+', chain)
    gens = []; arrows = []
    for t in toks:
        if t in GEN: gens.append(IDEM[t])
        else: arrows.append(t)
    return h, q, gens, arrows, rest

def arrow_info(a, il, ir):
    direction = +1 if a.endswith('>') else -1
    assert a.endswith('>') != a.startswith('<'), a
    m = re.search(r'([SD])(?:\^(\d+))?', a)
    if m:
        kind = m.group(1); power = int(m.group(2) or 1)
    else:
        kind = 'S' if '~' in a else 'D'
        power = 1
        if kind == 'S' and il == ir: power = 2
    if kind == 'D': assert il == ir, (a, il, ir)
    if kind == 'S': assert (il != ir) == (power % 2 == 1), (a, il, ir)
    return direction, kind, power

class Comp:
    """one curve component: idem list, arrows list of (src_index, tgt_index, kind, power), h list, q list, cyclic flag, label"""
    def __init__(self, h, q, gens, arrows, rest):
        n = len(gens)
        self.idem = gens
        self.cyclic = (len(arrows) == n)
        self.label = rest
        self.h = [h]; self.q = [q]
        self.arrows = []
        self.steps = []   # (direction, kind, power) between i and i+1 (cyclically)
        for i in range(len(arrows)):
            j = (i + 1) % n
            d, kind, p = arrow_info(arrows[i], gens[i], gens[j])
            self.steps.append((d, kind, p))
            deg = p if kind == 'S' else 2 * p
            if i < n - 1:
                self.h.append(self.h[-1] + d); self.q.append(self.q[-1] + d * deg)
            else:
                assert self.h[-1] + d == self.h[0] and self.q[-1] + d * deg == self.q[0], "cyclic closure fails"
            if d > 0: self.arrows.append((i, j, kind, p))
            else:     self.arrows.append((j, i, kind, p))
    def word(self):
        """canonical-ish string: idempotents b/c with arrows"""
        s = ''
        n = len(self.idem)
        for i in range(n):
            s += 'bc'[self.idem[i]]
            if i < len(self.steps):
                d, k, p = self.steps[i]
                lab = k + (str(p) if p > 1 else '')
                s += ('-' + lab + '>') if d > 0 else ('<' + lab + '-')
        return s
    def meanq(self): return Fraction(sum(self.q), len(self.q))
    def delta2(self):  # list of 2*delta
        return [q - 2 * h for q, h in zip(self.q, self.h)]

def parse_file(fn):
    comps = []
    for line in open(fn, encoding='utf-8'):
        r = parse_line(line)
        if r: comps.append(Comp(*r))
    return comps

def parse_label(lab):
    """'s4(∞) q^-64 δ_^-29' -> ('s',4,'∞',Fraction(-64),Fraction(-29)) ; 'r(0) q^-120 δ|^-39/2'"""
    m = re.match(r'([rs])(\d*)\(([^)]*)\)\s*q\^(-?[\d/]+)\s*δ[|_]\^(-?[\d/]+)', lab)
    if not m: return None
    return (m.group(1), int(m.group(2) or 1), m.group(3), Fraction(m.group(4)), Fraction(m.group(5)))

def all_tangles(roots=None, suffixes=('qs', 'd')):
    """yield (name, bn_comps, kh_comps) for every folder containing cxBNr-c2-<suffix> and cxKhr-c2-<suffix>"""
    base = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out'
    roots = roots or ['tilt', 'k138', 'dbl', 'comp']
    for root in roots:
        for suf in suffixes:
            for fb in sorted(glob.glob(os.path.join(base, root, '**', 'cxBNr-c2-' + suf), recursive=True)):
                fk = fb.replace('cxBNr', 'cxKhr')
                if not os.path.exists(fk): continue
                name = root + ':' + os.path.basename(os.path.dirname(fb))
                try:
                    yield name, parse_file(fb), parse_file(fk)
                except Exception as e:
                    print('PARSE ERROR', name, e)

if __name__ == '__main__':
    from collections import Counter
    cnt = Counter(); shapes = Counter(); n = 0
    for name, bn, kh in all_tangles():
        n += 1
        for c in bn:
            if c.cyclic: shapes[c.word()] += 1
        cnt[(sum(1 for c in bn if not c.cyclic), )] += 1
    print(n, 'tangles'); print(cnt)
    for w, v in shapes.most_common(): print(v, w)
