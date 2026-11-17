#!/usr/bin/env python3
"""My own parser for kht++ chain files (cxBNr-*, cxKhr-*).
Line: 'N) h^H q^Q δ^D  <chain>   [label]'.  Chain: generators ⬮ (b) / ⬯ (c) separated by arrows.
Arrow strings contain '>' (forward: left generator -> right generator) or '<' (backward); '~' = power of S, '—' = power
of D; an explicit exponent '^k' may appear; an unlabelled S-type arrow between equal idempotents is S^2.
For an arrow x -> y of label S^k (D^k): h(y) = h(x)+1, q(y) = q(x)+k (resp. +2k).
A chain ending in an arrow is cyclic: the last arrow joins the last generator and the first."""
import re
from fractions import Fraction as Fr
ANSI = re.compile(r'\x1b\[[0-9;]*[A-Za-z]')
HEAD = re.compile(r'^\s*(\d+)\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S+)(.*)$')
LABEL = re.compile(r'(r|s)(\d*)\(([^)]*)\)\s+q\^(-?[\d/]+)\s+δ[_|]\^(-?[\d/]+)')
def parse_chain(chain, h0, q0):
    gens = []; arrows = []
    i = 0; cur = ''
    for ch in chain:
        if ch in '⬮⬯':
            if gens: arrows.append(cur)
            elif cur: raise ValueError('chain starts with an arrow: %r' % chain)
            cur = ''
            gens.append('b' if ch == '⬮' else 'c')
        else:
            cur += ch
    cyclic = bool(cur)
    if cyclic: arrows.append(cur)
    n = len(gens)
    hq = [None] * n; hq[0] = (h0, q0)
    def step(a, left, right):
        """returns (dh, dq) of right relative to left"""
        fwd = '>' in a; bwd = '<' in a
        if fwd == bwd: raise ValueError('bad arrow %r' % a)
        isS = '~' in a; isD = '—' in a
        if isS == isD: raise ValueError('bad arrow type %r' % a)
        m = re.search(r'\^(\d+)', a)
        if m: k = int(m.group(1))
        elif isS: k = 2 if gens[left] == gens[right] else 1
        else: k = 1
        if isS and (k % 2 == 1) != (gens[left] != gens[right]): raise ValueError('S-power parity inconsistent %r' % a)
        if isD and gens[left] != gens[right]: raise ValueError('D between different idempotents')
        dq = k if isS else 2 * k
        return (1, dq) if fwd else (-1, -dq)
    for j in range(n - 1):
        dh, dq = step(arrows[j], j, j + 1)
        hq[j + 1] = (hq[j][0] + dh, hq[j][1] + dq)
    if cyclic:
        dh, dq = step(arrows[n - 1], n - 1, 0)
        back = (hq[n - 1][0] + dh, hq[n - 1][1] + dq)
        if back != hq[0]: raise ValueError('cyclic chain does not close up: %r' % chain)
    return [(g, h, q) for g, (h, q) in zip(gens, hq)], cyclic
def parse_file(path):
    comps = []
    for l in open(path, encoding='utf-8').read().splitlines():
        l = ANSI.sub('', l)
        if l.startswith('%') or not l.strip(): continue
        m = HEAD.match(l)
        if not m: raise ValueError('cannot parse line %r' % l)
        h0, q0 = int(m.group(2)), int(m.group(3))
        gens, cyclic = parse_chain(m.group(5), h0, q0)
        lab = LABEL.search(m.group(6))
        rec = {'gens': gens, 'cyclic': cyclic}
        if lab:
            rec.update({'type': lab.group(1), 'len': lab.group(2), 'slope': lab.group(3),
                        'q': float(Fr(lab.group(4))), 'delta': float(Fr(lab.group(5)))})
        comps.append(rec)
    return comps
def J_from_BN(comps):
    """sum over b-generators of (-1)^h t^(q/2)"""
    J = {}
    for c in comps:
        for (g, h, q) in c['gens']:
            if g != 'b': continue
            if q % 2: raise ValueError('odd q on a b-generator')
            e = q // 2
            J[e] = J.get(e, 0) + (-1) ** (h % 2)
            if J[e] == 0: del J[e]
    return J
