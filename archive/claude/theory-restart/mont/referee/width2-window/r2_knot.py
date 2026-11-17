"""Independent plat-diagram toolkit (does not use alex.py / flat_search.py).
Ops (top to bottom): ('cap',i) new arc at positions i,i+1; ('X',i,s) crossing of positions i,i+1, s=+1: strand TL->BR over,
s=-1: strand TR->BL over; ('cup',i) join positions i,i+1.
Provides: Kauffman bracket by a TL sweep, coloring (det) matrix, Alexander polynomial by Fox calculus."""
import sympy as sp
A, T = sp.symbols('A T')

class UF:
    def __init__(s): s.p = {}
    def f(s, a):
        s.p.setdefault(a, a)
        while s.p[a] != a:
            s.p[a] = s.p[s.p[a]]; a = s.p[a]
        return a
    def u(s, a, b): s.p[s.f(a)] = s.f(b)

def build(ops):
    uf = UF(); nid = [0]
    def new():
        nid[0] += 1; uf.f(nid[0]); return nid[0]
    pos = []; cr = []
    for op in ops:
        if op[0] == 'cap':
            i = op[1]; e = new(); pos[i:i] = [e, e]
        elif op[0] == 'cup':
            i = op[1]; uf.u(pos[i], pos[i + 1]); del pos[i:i + 2]
        else:
            _, i, s = op
            a, b = pos[i], pos[i + 1]; c, d = new(), new(); pos[i], pos[i + 1] = c, d
            cr.append({'TL': a, 'TR': b, 'BL': c, 'BR': d, 's': s})
    assert not pos, 'unclosed positions'
    for x in cr:
        for k in ('TL', 'TR', 'BL', 'BR'): x[k] = uf.f(x[k])
    return cr

def components(cr):
    """number of link components (via strand continuation through crossings)"""
    uf = UF()
    for x in cr:
        uf.u(x['TL'], x['BR']); uf.u(x['TR'], x['BL'])
    return len(set(uf.f(x[k]) for x in cr for k in ('TL', 'TR', 'BL', 'BR')))

def bracket_sweep(ops):
    """Kauffman bracket <D> (A-variable), plain state sum by a TL sweep; delta = -A^2-A^-2."""
    delta = -A**2 - A**-2
    st = {(): sp.Integer(1)}
    def cap(m, i):
        m2 = [x + 2 if x >= i else x for x in m]
        m2[i:i] = [i + 1, i]
        return tuple(m2)
    def cup(m, i):
        p, q = m[i], m[i + 1]; loop = (p == i + 1)
        m = list(m)
        if not loop: m[p] = q; m[q] = p
        del m[i:i + 2]
        return tuple(x - 2 if x > i + 1 else x for x in m), loop
    for op in ops:
        new = {}
        for m, p in st.items():
            if op[0] == 'cap':
                k = cap(m, op[1]); new[k] = new.get(k, 0) + p
            elif op[0] == 'cup':
                k, loop = cup(m, op[1]); new[k] = new.get(k, 0) + (p * delta if loop else p)
            else:
                _, i, s = op
                # s=+1 (TL->BR over): A-smoothing = horizontal (cup-cap), B = vertical (identity)
                wa, wb = (A, A**-1) if s == 1 else (A**-1, A)
                new[m] = new.get(m, 0) + wb * p
                m2, loop = cup(m, i); m3 = cap(m2, i)
                new[m3] = new.get(m3, 0) + wa * (p * delta if loop else p)
        st = {k: sp.expand(v) for k, v in new.items() if sp.expand(v) != 0}
    assert list(st.keys()) in ([()], []), st.keys()
    # every closed loop (including the last) was weighted by delta; standard <D> uses delta^(loops-1)
    return sp.factor(sp.cancel(st.get((), 0) / delta))

def orient(cr):
    """traverse the knot; returns for each crossing (over_dir, under_dir) as +1 (downward) / -1 (upward), and the arc data"""
    # slots: (c, key). edges: each edge label appears in exactly two slots.
    occ = {}
    for ci, x in enumerate(cr):
        for k in ('TL', 'TR', 'BL', 'BR'): occ.setdefault(x[k], []).append((ci, k))
    assert all(len(v) == 2 for v in occ.values()), 'edge degree'
    through = {'TL': 'BR', 'BR': 'TL', 'TR': 'BL', 'BL': 'TR'}
    dirs = {}
    ci, k = 0, 'TL'; steps = 0
    while True:
        # enter crossing ci at slot k, exit at through[k]
        out = through[k]
        strand = 'a' if k in ('TL', 'BR') else 'b'   # a: TL-BR strand, b: TR-BL strand
        dirs[(ci, strand)] = (+1 if k in ('TL', 'TR') else -1)   # entering from top => moving downward
        e = cr[ci][out]
        (c1, k1), (c2, k2) = occ[e]
        nxt = (c2, k2) if (c1, k1) == (ci, out) else (c1, k1)
        ci, k = nxt; steps += 1
        if (ci, k) == (0, 'TL'): break
        assert steps <= 4 * len(cr)
    assert len(dirs) == 2 * len(cr), 'not a knot (multiple components)'
    return dirs

def arcs_and_rows(cr):
    """over-arc structure: for each crossing (over_arc, under_in_arc, under_out_arc, sign)"""
    dirs = orient(cr)
    uf = UF()
    for x in cr:
        if x['s'] == 1: uf.u(x['TL'], x['BR'])
        else: uf.u(x['TR'], x['BL'])
    labels = {}
    def arc(e):
        r = uf.f(e)
        if r not in labels: labels[r] = len(labels)
        return labels[r]
    rows = []
    for ci, x in enumerate(cr):
        if x['s'] == 1:
            ov = 'a'; un = 'b'; o = arc(x['TL'])
            d_un = dirs[(ci, 'b')]
            uin, uout = (x['TR'], x['BL']) if d_un == 1 else (x['BL'], x['TR'])
        else:
            ov = 'b'; un = 'a'; o = arc(x['TR'])
            d_un = dirs[(ci, 'a')]
            uin, uout = (x['TL'], x['BR']) if d_un == 1 else (x['BR'], x['TL'])
        # geometric direction vectors (x right, y up): strand a downward = (1,-1); strand b downward = (-1,-1)
        vec = {'a': (1, -1), 'b': (-1, -1)}
        vo = tuple(dirs[(ci, ov)] * c for c in vec[ov]); vu = tuple(dirs[(ci, un)] * c for c in vec[un])
        cross = vo[0] * vu[1] - vo[1] * vu[0]
        sign = 1 if cross > 0 else -1
        rows.append((o, arc(uin), arc(uout), sign))
    return rows, len(labels)

def det_coloring(cr):
    rows, n = arcs_and_rows(cr)
    Mx = sp.zeros(len(rows), n)
    for r, (o, ui, uo, s) in enumerate(rows):
        Mx[r, o] += 2; Mx[r, ui] -= 1; Mx[r, uo] -= 1
    return abs(Mx[:-1, :-1].det()), Mx

def alexander(cr):
    rows, n = arcs_and_rows(cr)
    Mx = sp.zeros(len(rows), n)
    for r, (o, ui, uo, s) in enumerate(rows):
        if s == 1:
            Mx[r, o] += 1 - T; Mx[r, ui] += T; Mx[r, uo] += -1
        else:
            Mx[r, o] += T - 1; Mx[r, ui] += 1; Mx[r, uo] += -T
    d = sp.factor(Mx[:-1, :-1].det(method='berkowitz'))
    return d, Mx

def writhe(cr):
    rows, n = arcs_and_rows(cr)
    return sum(s for *_, s in rows)

# ---- half word -> full symmetric (strongly invertible) diagram, written from the kht++ description ----
def symmetric_ops(half):
    """half: list of (c,s). Full positions: axis between hw-1 and hw; right half-strand j at hw+j, mirror at hw-1-j.
    s.<...>: start with one arc across the axis (positions 0,1); x/y_s (s>=1): crossings on right (hw+s-1) and mirror (hw-s-1),
    same type; x/y_0: one crossing on the axis at hw-1; l_s: cap at right half (s-1,s) and mirror; u_s: cup at right half
    (s-1,s) and mirror; final cup across the axis."""
    hw = 1; ops = [('cap', 0)]
    for c, s in half:
        if c in 'xy':
            sg = 1 if c == 'x' else -1
            if s == 0: ops.append(('X', hw - 1, sg))
            else: ops += [('X', hw + s - 1, sg), ('X', hw - s - 1, sg)]
        elif c in 'lr':
            ops.append(('cap', hw + s - 1))       # right: new positions hw+s-1, hw+s
            ops.append(('cap', hw - s + 1))       # mirror (inserted left of the axis; right side shifts by 2)
            hw += 2
        elif c == 'u':
            ops.append(('cup', hw + s - 1)); ops.append(('cup', hw - s - 1)); hw -= 2
    ops.append(('cup', 0))
    return ops

def parse(word):
    w = word.strip()
    if w.startswith('s.'): w = w[2:]
    return [(tok[0], int(tok[1:])) for tok in w.split('.') if tok]

def pd_bracket(pd):
    """Kauffman bracket of a PD code [[i,j,k,l],...] (i incoming under, counterclockwise). A-smoothing joins (i,j),(k,l)."""
    delta = -A**2 - A**-2
    n = len(pd); tot = 0
    import itertools
    for st in itertools.product((0, 1), repeat=n):
        uf = UF()
        for x in pd:
            for e in x: uf.f(e)
        na = 0
        for s, (i, j, k, l) in zip(st, pd):
            if s == 0: uf.u(i, j); uf.u(k, l); na += 1
            else: uf.u(i, l); uf.u(j, k)
        loops = len(set(uf.f(e) for x in pd for e in x))
        tot += A**(na - (n - na)) * delta**(loops - 1)
    return sp.expand(tot)
