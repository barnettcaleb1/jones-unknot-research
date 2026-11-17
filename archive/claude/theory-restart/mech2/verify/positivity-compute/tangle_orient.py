#!/usr/bin/env python3
"""Crossing signs of the quotient 1-3 tangle diagram (band word, with framing twists) for a prescribed orientation of
its two strands alpha (top - b3) and beta (b1 - b2).  kht++ orients the -q tangle so that b2 and b3 both carry the
orientation of the top end of the half-diagram (Tangle::quotient, the two flip_orient_at_index calls).
Also: signs in the unknot closure D(inf) (b2 joined to b3)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sidiag as S

OPP = {'TL': 'BR', 'BR': 'TL', 'TR': 'BL', 'BL': 'TR'}
VEC = {'TL': (1, -1), 'TR': (-1, -1), 'BL': (1, 1), 'BR': (-1, 1)}

def build(word):
    """1-3 tangle word -> crossings with edge ids, the top edge and the three bottom edges."""
    uf = S.UF(); cnt = [0]
    def new():
        cnt[0] += 1; return cnt[0]
    top = new()
    pos = [top]
    cr = []
    for (c, i) in word:
        if c in 'xy':
            a, b = pos[i], pos[i + 1]
            cc, d = new(), new()
            pos[i], pos[i + 1] = cc, d
            cr.append(dict(type=c, TL=a, TR=b, BL=cc, BR=d))
        elif c in ('cap', 'l', 'r'):
            e = new(); pos[i:i] = [e, e]
        elif c == 'u':
            uf.union(pos[i], pos[i + 1]); del pos[i:i + 2]
    assert len(pos) == 3
    for x in cr:
        for k in ('TL', 'TR', 'BL', 'BR'):
            x[k] = uf.find(x[k])
    return cr, uf.find(top), [uf.find(p) for p in pos]

def walk(cr, ends, start_edge, start_from_boundary=True):
    """follow the strand starting on boundary edge start_edge into the tangle; returns list of (crossing, entry corner) and
    the boundary edge where it leaves."""
    path = []
    e = start_edge
    prev = None
    while True:
        att = [a for a in ends.get(e, []) if a != prev]
        if prev is None:
            # boundary edge: exactly one crossing corner attached (or none: strand without crossings)
            if len(ends.get(e, [])) == 0:
                return path, e
            assert len(ends[e]) == 1, 'boundary edge with %d corners' % len(ends[e])
            ci, corner = ends[e][0]
        else:
            if len(att) == 0:
                return path, e      # reached a boundary edge
            assert len(att) == 1
            ci, corner = att[0]
        path.append((ci, corner))
        out = OPP[corner]
        e = cr[ci][out]
        prev = (ci, out)

def signs(word, alpha_from, beta_from):
    """alpha_from in {'top','b3'}: boundary point where alpha starts; beta_from in {'b1','b2'}.
    returns (n_plus, n_minus, n_plus_mixed, n_minus_mixed) and the list of signs."""
    cr, top, bots = build(word)
    ends = {}
    for ci, x in enumerate(cr):
        for k in ('TL', 'TR', 'BL', 'BR'):
            ends.setdefault(x[k], []).append((ci, k))
    name = {'top': top, 'b1': bots[0], 'b2': bots[1], 'b3': bots[2]}
    pa, ea = walk(cr, ends, name[alpha_from])
    pb, eb = walk(cr, ends, name[beta_from])
    other_a = 'b3' if alpha_from == 'top' else 'top'
    other_b = 'b2' if beta_from == 'b1' else 'b1'
    assert ea == name[other_a] and eb == name[other_b], 'connectivity is not type b'
    entry = {}
    comp = {}
    for (ci, corner) in pa:
        entry[(ci, frozenset((corner, OPP[corner])))] = corner; comp[(ci, frozenset((corner, OPP[corner])))] = 'a'
    for (ci, corner) in pb:
        entry[(ci, frozenset((corner, OPP[corner])))] = corner; comp[(ci, frozenset((corner, OPP[corner])))] = 'b'
    assert len(entry) == 2 * len(cr), 'closed components present'
    out = []
    npl = nmi = mp = mm = 0
    for ci, x in enumerate(cr):
        if x['type'] == 'x':
            over, under = frozenset(('TL', 'BR')), frozenset(('TR', 'BL'))
        else:
            over, under = frozenset(('TR', 'BL')), frozenset(('TL', 'BR'))
        o = VEC[entry[(ci, over)]]; u = VEC[entry[(ci, under)]]
        sg = 1 if o[0] * u[1] - o[1] * u[0] > 0 else -1
        mixed = comp[(ci, over)] != comp[(ci, under)]
        out.append((sg, mixed))
        if sg > 0:
            npl += 1; mp += mixed
        else:
            nmi += 1; mm += mixed
    return npl, nmi, mp, mm, out

if __name__ == '__main__':
    for w in sys.argv[1:]:
        hs = S.half_signs(w); half = S.parse(w)
        full = S.band_word(half, hs['wr'])
        # kht++ orientation: b2 up and b3 up, i.e. alpha starts at b3, beta starts at b2
        print(w, 'kht orientation (n+, n-, mixed+, mixed-):', signs(full, 'b3', 'b2')[:4],
              ' unknot orientation, twist-free D:', signs(S.band_word(half, 0), 'top', 'b2')[:4])
