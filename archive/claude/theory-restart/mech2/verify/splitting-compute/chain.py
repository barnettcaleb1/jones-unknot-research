#!/usr/bin/env python3
"""Referee's own parser for kht++ chain files (cxBNr-*, cxKhr-*, cxCKh-*).  Written from scratch."""
import re
from fractions import Fraction

B, C = '⬮', '⬯'   # ⬮ (b = Q_0), ⬯ (c = Q_infinity)

def parse_line(line):
    """returns (h, q, [(symbol, h, q), ...], cyclic) for a chain line 'n) h^a q^b δ^c <chain>   [label]'"""
    m = re.match(r'\s*\d+\)\s*h\^\s*(-?\d+)\s*q\^\s*(-?\d+)\s*δ\^\s*(-?\d+(?:/\d+)?)\s*(\S+)(.*)$', line)
    if not m:
        raise ValueError('cannot parse: %r' % line)
    h0, q0 = int(m.group(1)), int(m.group(2)); delta = Fraction(m.group(3))
    chain = m.group(4); rest = m.group(5).strip()
    # split into symbols and arrows
    toks = re.findall('[%s%s]|[^%s%s]+' % (B, C, B, C), chain)
    syms = []; arrows = []
    assert toks[0] in (B, C), toks
    i = 0
    while i < len(toks):
        assert toks[i] in (B, C)
        syms.append(toks[i])
        if i + 1 < len(toks):
            arrows.append(toks[i + 1])
        i += 2
    cyclic = (len(arrows) == len(syms))
    def decode(a, x, y):
        # direction
        if a.endswith('>') and not a.startswith('<'):
            fwd = True
        elif a.startswith('<') and not a.endswith('>'):
            fwd = False
        else:
            raise ValueError('bad arrow %r' % a)
        mm = re.search(r'([SDH])(?:\^(\d+))?', a)
        if mm:
            letter = mm.group(1); k = int(mm.group(2) or 1)
        else:
            if '~' in a and '—' not in a:
                letter = 'S'; k = 2 if x == y else 1
            elif '—' in a and '~' not in a:
                letter = 'D'; k = 1
            else:
                raise ValueError('bad arrow %r' % a)
        if letter == 'S':
            assert (k % 2 == 0) == (x == y), (a, x, y)
            dq = k
        elif letter == 'D':
            assert x == y, (a, x, y)
            dq = 2 * k
        else:  # H^k in CKh files
            dq = 2 * k
        return fwd, letter, k, dq
    gens = [(syms[0], h0, q0)]
    arrs = []
    for j, a in enumerate(arrows):
        x = syms[j]; y = syms[(j + 1) % len(syms)]
        fwd, letter, k, dq = decode(a, x, y)
        hx, qx = gens[j][1], gens[j][2]
        if fwd: hy, qy = hx + 1, qx + dq
        else:   hy, qy = hx - 1, qx - dq
        arrs.append((j, (j + 1) % len(syms), fwd, letter, k))
        if j + 1 < len(syms):
            gens.append((y, hy, qy))
        else:
            # cyclic closure must be consistent
            if (hy, qy) != (gens[0][1], gens[0][2]):
                raise ValueError('cyclic chain does not close up: %r' % line)
    # consistency of the printed delta: delta = q/2 - h of the first generator
    if Fraction(q0, 2) - h0 != delta:
        raise ValueError('delta mismatch in %r' % line)
    return dict(h=h0, q=q0, gens=gens, arrows=arrs, cyclic=cyclic, label=rest)

def read_chains(path):
    out = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('%') or not line.strip():
            continue
        out.append(parse_line(line))
    return out

def b_generators(path):
    """(h,q) of all b-generators of a BN~ chain file"""
    return sorted((h, q) for ch in read_chains(path) for (s, h, q) in ch['gens'] if s == B)

def kh_of_knot(path):
    """Kh~ of a link from a cxCKh file: list of (h,q) (homology with H = 0: tower -> 1 generator, H^n piece -> 2)"""
    out = []
    for ch in read_chains(path):
        for (s, h, q) in ch['gens']:
            out.append((h, q))
        assert len(ch['gens']) in (1, 2)
        if len(ch['gens']) == 2:
            assert ch['arrows'][0][3] == 'H' and ch['arrows'][0][2], ch
    return sorted(out)

if __name__ == '__main__':
    import sys
    for p in sys.argv[1:]:
        print(p)
        for ch in read_chains(p):
            print('  ', 'cyclic' if ch['cyclic'] else 'arc', [(('b' if s == B else 'c'), h, q) for s, h, q in ch['gens']], ch['label'])
