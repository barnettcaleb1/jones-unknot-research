#!/usr/bin/env python3
"""Referee's independent implementation (does not import the report's scripts).

Objects:
  half-diagram word  (kht++ 's.' format, without the 's.')
  band diagram D     (twist-free quotient diagram, built as in Tangle::quotient, read from the C++ source)
  states of D, type b / c, number of closed circles
  half-plane picture Gamma_1 (or Gamma_0), regions, boundary curves, loops
"""
import sys, itertools
from collections import defaultdict

# ---------------------------------------------------------------- parsing
def parse_word(w):
    w = w.strip()
    if w.startswith('s.'):
        w = w[2:]
    out = []
    for tok in w.split('.'):
        tok = tok.strip()
        if not tok:
            continue
        out.append((tok[0], int(tok[1:])))
    return out

# ---------------------------------------------------------------- half-diagram: orientation, signs
def half_info(word):
    """Trace the drawn strand of the half-diagram from the top end to the bottom fixed point.
    Returns dict with: signs (list, one per crossing letter, +1/-1), c, c_axis, c_o, wr, widths.
    Node = (level, pos), level k = between slice k-1 and slice k, pos>=1.  Position 0 = axis (virtual)."""
    L = len(word)
    width = [1]
    for (ch, i) in word:
        w = width[-1]
        if ch in 'xy':
            if i == 0:
                assert w >= 1
            else:
                assert 1 <= i and i + 1 <= w, ("crossing outside half-diagram", ch, i, w)
            width.append(w)
        elif ch in 'lr':
            assert 1 <= i <= w + 1, ("cap position", ch, i, w)
            width.append(w + 2)
        elif ch == 'u':
            assert 1 <= i and i + 1 <= w, ("cup position", ch, i, w)
            width.append(w - 2)
        else:
            raise ValueError(ch)
    assert width[-1] == 1, ("half-diagram must end with one strand", width[-1])
    # adjacency: each node has a 'down' neighbour and an 'up' neighbour (possibly at the same level through cap/cup)
    down = {}  # node at level k (above slice k) -> (node, kind) reached going down through slice k
    up = {}    # node at level k+1 (below slice k) -> (node, kind) reached going up through slice k
    for k, (ch, i) in enumerate(word):
        w = width[k]
        if ch in 'xy':
            for p in range(1, w + 1):
                if i >= 1 and p == i:
                    q = i + 1
                elif i >= 1 and p == i + 1:
                    q = i
                else:
                    q = p
                kind = 'axis' if (i == 0 and p == 1) else 'v'
                down[(k, p)] = ((k + 1, q), kind)
                up[(k + 1, q)] = ((k, p), kind)
        elif ch in 'lr':
            for p in range(1, w + 1):
                q = p if p < i else p + 2
                down[(k, p)] = ((k + 1, q), 'v')
                up[(k + 1, q)] = ((k, p), 'v')
            up[(k + 1, i)] = ((k + 1, i + 1), 'cap')
            up[(k + 1, i + 1)] = ((k + 1, i), 'cap')
        elif ch == 'u':
            for p in range(1, w + 1):
                if p in (i, i + 1):
                    continue
                q = p if p < i else p - 2
                down[(k, p)] = ((k + 1, q), 'v')
                up[(k + 1, q)] = ((k, p), 'v')
            down[(k, i)] = ((k, i + 1), 'cup')
            down[(k, i + 1)] = ((k, i), 'cup')
    # trace
    orient = {}   # node -> +1 if K-orientation points down at that node, -1 if up
    node = (0, 1)
    going_down = True
    flip = 1
    visited = 0
    total_nodes = sum(width)
    while True:
        assert node not in orient, "strand revisits a node"
        orient[node] = (1 if going_down else -1) * flip
        visited += 1
        if going_down:
            if node[0] == L:
                break
            nxt, kind = down[node]
        else:
            assert node[0] > 0, "strand returns to the top"
            nxt, kind = up[node]
        if kind == 'cup':
            going_down = False
        elif kind == 'cap':
            going_down = True
        elif kind == 'axis':
            flip = -flip
        node = nxt
    assert node == (L, 1)
    assert visited == total_nodes, ("half-diagram has closed components or unvisited strands", visited, total_nodes)
    signs = []
    for k, (ch, i) in enumerate(word):
        if ch in 'xy':
            if i == 0:
                s = +1 if ch == 'x' else -1
            else:
                same = (orient[(k, i)] == orient[(k, i + 1)])
                if ch == 'y':
                    s = +1 if same else -1
                else:
                    s = -1 if same else +1
            signs.append(s)
        else:
            signs.append(0)
    c_axis = sum(1 for (ch, i) in word if ch in 'xy' and i == 0)
    c_o = sum(1 for (ch, i) in word if ch in 'xy' and i > 0)
    return dict(signs=signs, c=c_axis + c_o, c_axis=c_axis, c_o=c_o, wr=sum(signs), width=width)

# ---------------------------------------------------------------- band diagram D (twist-free quotient)
def band_word(word):
    """Twist-free quotient word, following Tangle::quotient.  Letters: ('c', i) cap, ('u', i) cup, ('x'|'y', i) crossing.
    Also returns for every crossing of D the pair (block index = index of the letter in the half word, place 0..3)."""
    out = [('c', 1), ('c', 2)]
    tags = [None, None]
    for k, (ch, i) in enumerate(word):
        if ch in 'xy':
            if i == 0:
                idx = [0, 1, 1, 0]
            else:
                idx = [2 * i, 2 * i - 1, 2 * i + 1, 2 * i]
            for place, j in enumerate(idx):
                out.append((ch, j)); tags.append((k, place))
        elif ch in 'lr':
            out.append(('c', 2 * i - 1)); tags.append(None)
            out.append(('c', 2 * i)); tags.append(None)
        elif ch == 'u':
            out.append(('u', 2 * i)); tags.append(None)
            out.append(('u', 2 * i - 1)); tags.append(None)
    out.append(('u', 0)); tags.append(None)
    return out, tags

def eval_state(bword, bits):
    """bits: iterable of 0/1, one per crossing of bword in order.  Returns (circles, type) with type 'b' (top-b3, b1-b2)
    or 'c' (top-b1, b2-b3).  Smoothing convention: x: 0 = e, 1 = id ; y: 0 = id, 1 = e."""
    pos = [0]          # position 0 = the axis strand; label 0 = the arc through the top end
    nxt = 1
    circles = 0
    bi = iter(bits)
    def cup(i):
        nonlocal circles, pos
        a, b = pos[i], pos[i + 1]
        del pos[i:i + 2]
        if a == b:
            circles += 1
        else:
            # merge b into a (keep the smaller label so that label 0 = top survives)
            if b < a:
                a, b = b, a
            pos = [a if z == b else z for z in pos]
    def cap(i):
        nonlocal nxt
        pos.insert(i, nxt); pos.insert(i, nxt)
        nxt += 1
    for (ch, i) in bword:
        if ch == 'c':
            cap(i)
        elif ch == 'u':
            cup(i)
        else:
            bit = next(bi)
            is_e = (bit == 0) if ch == 'x' else (bit == 1)
            if is_e:
                cup(i); cap(i)
    assert len(pos) == 3, pos
    # the top end carries label 0 unless it was merged into... (we always keep the smaller label, so 0 survives)
    if pos[2] == 0 and pos[0] == pos[1]:
        return circles, 'b'
    if pos[0] == 0 and pos[1] == pos[2]:
        return circles, 'c'
    raise AssertionError(("impossible end pattern", pos))

def ncross(bword):
    return sum(1 for (ch, i) in bword if ch in 'xy')

# ---------------------------------------------------------------- transfer matrices over planar matchings
def _canon(pos):
    """canonical relabelling of the tuple pos (label 0 = top stays 0)."""
    m = {0: 0}
    out = []
    for z in pos:
        if z not in m:
            m[z] = len(m)
        out.append(m[z])
    return tuple(out)

def _cup(pos, i):
    a, b = pos[i], pos[i + 1]
    rest = pos[:i] + pos[i + 2:]
    if a == b:
        return rest, 1
    if b < a:
        a, b = b, a
    return tuple(a if z == b else z for z in rest), 0

def _cap(pos, i):
    new = max(pos) + 1 if pos else 1
    return pos[:i] + (new, new) + pos[i:]

def transfer(bword, mode):
    """mode 'poly': weights are Laurent polynomials in q (dict exp->coeff), state weight (-q)^{|s|} (q+1/q)^{circles}.
       mode 'max' : weights (best, count) for f = |s| + circles ; mode 'min': for g = |s| - circles.
       Returns dict type -> weight."""
    if mode == 'poly':
        def add(a, b):
            r = dict(a)
            for e, v in b.items():
                r[e] = r.get(e, 0) + v
                if r[e] == 0:
                    del r[e]
            return r
        def mul_circle(a):
            r = {}
            for e, v in a.items():
                r[e + 1] = r.get(e + 1, 0) + v
                r[e - 1] = r.get(e - 1, 0) + v
            return {e: v for e, v in r.items() if v}
        def mul_one(a):   # times (-q)
            return {e + 1: -v for e, v in a.items()}
        one = {0: 1}
    else:
        sgn = 1 if mode == 'max' else -1
        def add(a, b):
            if a[0] == b[0]:
                return (a[0], a[1] + b[1])
            if mode == 'max':
                return a if a[0] > b[0] else b
            return a if a[0] < b[0] else b
        def mul_circle(a):
            return (a[0] + sgn, a[1])
        def mul_one(a):
            return (a[0] + 1, a[1])
        one = (0, 1)
    cur = {(0,): one}
    for (ch, i) in bword:
        new = {}
        def put(p, w):
            p = _canon(p)
            if p in new:
                new[p] = add(new[p], w)
            else:
                new[p] = w
        for pos, w in cur.items():
            if ch == 'c':
                put(_cap(pos, i), w)
            elif ch == 'u':
                p2, circ = _cup(pos, i)
                put(p2, mul_circle(w) if circ else w)
            else:
                # id smoothing
                # e smoothing
                p2, circ = _cup(pos, i)
                p2 = _cap(p2, i)
                we = mul_circle(w) if circ else w
                wid = w
                if ch == 'x':      # x: 0 = e, 1 = id
                    put(p2, we)
                    put(pos, mul_one(wid))
                else:              # y: 0 = id, 1 = e
                    put(pos, wid)
                    put(p2, mul_one(we))
        cur = new
    res = {}
    for pos, w in cur.items():
        assert len(pos) == 3
        if pos[2] == 0 and pos[0] == pos[1]:
            t = 'b'
        elif pos[0] == 0 and pos[1] == pos[2]:
            t = 'c'
        else:
            raise AssertionError(pos)
        res[t] = add(res[t], w) if t in res else w
    return res

# ---------------------------------------------------------------- polynomial helpers
def poly_eval_i(p):
    """value and derivative of the Laurent polynomial p (dict) at q = i, as complex numbers."""
    val = 0j; der = 0j
    for e, v in p.items():
        val += v * (1j) ** e
        der += v * e * (1j) ** (e - 1)
    return val, der

def poly_shift(p, k):
    return {e + k: v for e, v in p.items()}

def poly_str(p):
    return ' '.join('%+d*q^%d' % (p[e], e) for e in sorted(p))

# ---------------------------------------------------------------- half-plane picture
class UF:
    def __init__(self):
        self.p = {}
    def find(self, x):
        self.p.setdefault(x, x)
        r = x
        while self.p[r] != r:
            r = self.p[r]
        while self.p[x] != r:
            self.p[x], x = r, self.p[x]
        return r
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb
    def same(self, a, b):
        return self.find(a) == self.find(b)
    def classes(self):
        d = defaultdict(list)
        for x in list(self.p):
            d[self.find(x)].append(x)
        return d

def half_plane(word, end=1):
    """Half-plane picture at the given end (1: every crossing 1-smoothed; 0: 0-smoothed).
    Works in the half-plane word  cap(1) + word  (strand 1 = top strand of the half-diagram, last strand = extra strand).
    Returns dict: arcs, loops, regions, curves (number of boundary curves), cut (number of cut hooks),
    bad (list of half-word indices of bad blocks, criteria (i),(ii) of the report), alpha_beta_ok."""
    segs = UF(); sides = UF(); gaps = UF()
    def S(k, p): return ('s', k, p)
    def sd(k, p, s): return ('side', k, p, s)       # p = 0: axis (only side 'R')
    def G(k, g): return ('g', k, g)
    full = [('cap0', 1)] + list(word)
    # level 0: no strands; gap (0,0)
    widths = [0]
    ncut = 0
    arc_ends = 0
    chords = {}   # half-word index -> (sideA, sideB) for the twin chords
    for k, (ch, i) in enumerate(full):
        w = widths[-1]
        hw_index = k - 1
        def straight(shift_from=None, shift=0, skip=()):
            # join strands, sides and gaps of level k to level k+1
            for p in range(1, w + 1):
                if p in skip:
                    continue
                q = p if (shift_from is None or p < shift_from) else p + shift
                segs.union(S(k, p), S(k + 1, q))
                sides.union(sd(k, p, 'L'), sd(k + 1, q, 'L'))
                sides.union(sd(k, p, 'R'), sd(k + 1, q, 'R'))
        if ch in ('cap0', 'l', 'r'):
            straight(shift_from=i, shift=2)
            sides.union(sd(k, 0, 'R'), sd(k + 1, 0, 'R'))
            # new strands i, i+1 at level k+1
            segs.union(S(k + 1, i), S(k + 1, i + 1))
            sides.union(sd(k + 1, i, 'R'), sd(k + 1, i + 1, 'L'))
            sides.union(sd(k + 1, i, 'L'), sd(k + 1, i + 1, 'R'))
            for g in range(0, w + 1):
                if g <= i - 1:
                    gaps.union(G(k, g), G(k + 1, g))
                if g >= i - 1:
                    gaps.union(G(k, g), G(k + 1, g + 2))
            gaps.find(G(k + 1, i))
            widths.append(w + 2)
        elif ch == 'u':
            straight(shift_from=i + 2, shift=-2, skip=(i, i + 1))
            sides.union(sd(k, 0, 'R'), sd(k + 1, 0, 'R'))
            segs.union(S(k, i), S(k, i + 1))
            sides.union(sd(k, i, 'R'), sd(k, i + 1, 'L'))
            sides.union(sd(k, i, 'L'), sd(k, i + 1, 'R'))
            for g in range(0, w + 1):
                if g <= i - 1:
                    gaps.union(G(k, g), G(k + 1, g))
                if g >= i + 1:
                    gaps.union(G(k, g), G(k + 1, g - 2))
            gaps.find(G(k, i))
            widths.append(w - 2)
        else:
            # crossing; which smoothing at this end?
            if ch == 'x':
                is_e = (end == 0)
            else:
                is_e = (end == 1)
            if i >= 1:
                if not is_e:
                    straight()
                    sides.union(sd(k, 0, 'R'), sd(k + 1, 0, 'R'))
                    for g in range(0, w + 1):
                        gaps.union(G(k, g), G(k + 1, g))
                    chords[hw_index] = ('off', sd(k, i, 'R'), sd(k, i + 1, 'L'))
                else:
                    straight(skip=(i, i + 1))
                    sides.union(sd(k, 0, 'R'), sd(k + 1, 0, 'R'))
                    segs.union(S(k, i), S(k, i + 1))
                    sides.union(sd(k, i, 'R'), sd(k, i + 1, 'L'))
                    sides.union(sd(k, i, 'L'), sd(k, i + 1, 'R'))
                    segs.union(S(k + 1, i), S(k + 1, i + 1))
                    sides.union(sd(k + 1, i, 'R'), sd(k + 1, i + 1, 'L'))
                    sides.union(sd(k + 1, i, 'L'), sd(k + 1, i + 1, 'R'))
                    for g in range(0, w + 1):
                        if g != i:
                            gaps.union(G(k, g), G(k + 1, g))
                    gaps.union(G(k, i - 1), G(k, i + 1))
                    gaps.find(G(k, i)); gaps.find(G(k + 1, i))
                    chords[hw_index] = ('off', sd(k, i, 'L'), sd(k + 1, i, 'L'))
            else:
                if not is_e:
                    # pass by
                    straight()
                    sides.union(sd(k, 0, 'R'), sd(k + 1, 0, 'R'))
                    for g in range(0, w + 1):
                        gaps.union(G(k, g), G(k + 1, g))
                    chords[hw_index] = ('pass', sd(k, 0, 'R'), sd(k, 1, 'L'))
                else:
                    # cut
                    ncut += 1
                    arc_ends += 2
                    straight(skip=(1,))
                    segs.find(S(k, 1)); segs.find(S(k + 1, 1))
                    sides.union(sd(k, 1, 'L'), sd(k, 0, 'R'))
                    sides.union(sd(k + 1, 1, 'L'), sd(k + 1, 0, 'R'))
                    sides.union(sd(k, 1, 'R'), sd(k + 1, 1, 'R'))
                    for g in range(1, w + 1):
                        gaps.union(G(k, g), G(k + 1, g))
                    gaps.find(G(k, 0)); gaps.find(G(k + 1, 0))
                    chords[hw_index] = ('cut', None, None)
            widths.append(w)
    Lv = len(full)
    assert widths[-1] == 2, widths[-1]
    # bottom: strand 1 ends at the fixed point f (u0), strand 2 = extra strand, goes to infinity
    sides.union(sd(Lv, 1, 'L'), sd(Lv, 0, 'R'))
    arc_ends += 2
    # make sure every object is registered
    for k in range(0, Lv + 1):
        sides.find(sd(k, 0, 'R'))
        gaps.find(G(k, 0))
        for p in range(1, widths[k] + 1):
            segs.find(S(k, p)); sides.find(sd(k, p, 'L')); sides.find(sd(k, p, 'R')); gaps.find(G(k, p))
    ncomp = len(segs.classes())
    arcs = arc_ends // 2
    loops = ncomp - arcs
    ncurves = len(sides.classes())
    nregions = len(gaps.classes())
    alpha = sides.find(sd(0, 0, 'R'))
    beta = sides.find(sd(Lv, 1, 'R'))
    ok = (sides.find(sd(Lv, 2, 'R')) == alpha) and (sides.find(sd(Lv, 2, 'L')) == beta) and alpha != beta
    bad = []
    for hw, (kind, a, b) in sorted(chords.items()):
        if kind == 'cut':
            continue
        if sides.same(a, b):
            bad.append(hw)
    return dict(arcs=arcs, loops=loops, regions=nregions, curves=ncurves, cut=ncut, bad=bad, alpha_beta_ok=ok,
                k_pred=ncut + ncurves - 2)

# ---------------------------------------------------------------- everything for one word
def analyse(wordstr, brute_limit=0):
    word = parse_word(wordstr)
    info = half_info(word)
    c, wr = info['c'], info['wr']
    bw, tags = band_word(word)
    n = ncross(bw)
    assert n == 4 * c
    res = dict(word=wordstr, c=c, c_axis=info['c_axis'], c_o=info['c_o'], wr=wr, n=n)
    k1, t1 = eval_state(bw, [1] * n)
    k0, t0 = eval_state(bw, [0] * n)
    res.update(k1=k1, t1=t1, k0=k0, t0=t0)
    mx = transfer(bw, 'max'); mn = transfer(bw, 'min')
    res.update(M=mx['b'][0], E1=mx['b'][1], Mc=mx.get('c', (None, 0))[0], m=mn['b'][0], E0=mn['b'][1],
               mc=mn.get('c', (None, 0))[0])
    pol = transfer(bw, 'poly')
    alpha = pol['b']; beta = pol.get('c', {})
    res['alpha'] = alpha; res['beta'] = beta
    # unknot check: alpha + (q+1/q) beta should be q^(2c)
    tot = dict(alpha)
    for e, v in beta.items():
        for d in (1, -1):
            tot[e + d] = tot.get(e + d, 0) + v
    tot = {e: v for e, v in tot.items() if v}
    res['closure'] = tot
    d0 = 2 * c - 4 * wr
    res['d0'] = d0
    J = poly_shift(alpha, -d0)
    res['J'] = J
    res['Jcong'] = poly_eval_i(J)
    # loop chords of s_1 and s_0 (direct, in D)
    for end in (1, 0):
        base = [end] * n
        kk = k1 if end == 1 else k0
        loop = []
        for j in range(n):
            st = list(base); st[j] = 1 - end
            kj, tj = eval_state(bw, st)
            if tj == 'b' and kj == kk + 1:
                loop.append(j)
            else:
                assert (tj == 'c' and kj == kk) or (tj == 'b' and kj == kk - 1), (j, kj, tj, kk)
        # translate to blocks
        cross_tags = [t for t, (ch, i) in zip(tags, bw) if ch in 'xy']
        blocks = defaultdict(list)
        for j in loop:
            blocks[cross_tags[j][0]].append(cross_tags[j][1])
        res['loop%d' % end] = dict(blocks)
        hp = half_plane(word, end)
        res['hp%d' % end] = hp
    return res

if __name__ == '__main__':
    for w in sys.argv[1:]:
        r = analyse(w)
        for k_, v in r.items():
            print(k_, ':', v)
