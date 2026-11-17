"""R2 referee library (sections 7-8 of skein_dictionary_arbitrary_boxes.md).
Independent colored-bracket evaluator in the quotient band picture.
Laurent polynomials in A are dicts {exp:int coeff}.  t = A^4.
Conventions copied from tools/flat_search.py (crossing x = A*I + A^-1*e, y = A^-1*I + A*e,
letter doubling of quotient_word), but the closure at the two theta vertices is built here
from the definition of the standard (1,1,2) vertex, not from flat_search's 4-ended tangle."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import alex
import flat_search as fs

# ---------------- Laurent polynomials in A ----------------
def clean(p): return {e: c for e, c in p.items() if c}
def padd(*ps):
    r = {}
    for p in ps:
        for e, c in p.items():
            r[e] = r.get(e, 0) + c
    return clean(r)
def pscale(p, c): return clean({e: c * v for e, v in p.items()})
def pshift(p, k): return {e + k: v for e, v in p.items()}
def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return clean(r)
def mono(e, c=1): return {e: c}
ONE = mono(0)
DELTA = {2: -1, -2: -1}                 # delta = -A^2 - A^-2
DELTA2 = padd(pmul(DELTA, DELTA), {0: -1})   # delta^2 - 1 = A^4 + 1 + A^-4
def tpoly(d):   # polynomial in t given as {t-exp: c}  -> A-poly
    return {4 * e: c for e, c in d.items()}
PHI3 = tpoly({0: 1, 1: 1, 2: 1})
PHI5 = tpoly({0: 1, 1: 1, 2: 1, 3: 1, 4: 1})
def ppow(p, n):
    r = ONE
    for _ in range(n): r = pmul(r, p)
    return r

# ---------------- matchings with optional top endpoints ----------------
# state m: tuple; indices 0..nt-1 are fixed top endpoints, nt.. are current strands left->right;
# m[i] = partner index.
def cap(m, nt, i):
    j = nt + i
    m2 = [(x + 2 if x >= j else x) for x in m]
    m2[j:j] = [j + 1, j]
    return tuple(m2)
def cup(m, nt, i):
    j = nt + i
    p, q = m[j], m[j + 1]
    m = list(m)
    loop = False
    if p == j + 1:
        loop = True
    else:
        m[p] = q; m[q] = p
    del m[j:j + 2]
    m = [(x - 2 if x > j + 1 else x) for x in m]
    return tuple(m), loop

def run(ops, state, nt):
    """ops: list of (c, i); c in 'x','y' (crossing at strands i,i+1), 'l','r' (cap at i), 'u' (cup at i),
    'E' (insert e at i: cup then cap).  state: {matching: poly}."""
    for c, i in ops:
        new = {}
        for m, p in state.items():
            W = len(m) - nt
            if c in 'lr':
                if i > W: raise ValueError('cap out of range')
                k = cap(m, nt, i)
                new[k] = padd(new.get(k, {}), p)
            elif c == 'u':
                if i + 1 >= W: raise ValueError('cup out of range')
                m2, loop = cup(m, nt, i)
                new[m2] = padd(new.get(m2, {}), pmul(p, DELTA) if loop else p)
            elif c == 'E':
                if i + 1 >= W: raise ValueError('E out of range')
                m2, loop = cup(m, nt, i)
                q = pmul(p, DELTA) if loop else p
                k = cap(m2, nt, i)
                new[k] = padd(new.get(k, {}), q)
            elif c in 'xy':
                if i + 1 >= W: raise ValueError('crossing out of range')
                a, b = (1, -1) if c == 'x' else (-1, 1)
                new[m] = padd(new.get(m, {}), pshift(p, a))
                m2, loop = cup(m, nt, i)
                q = pmul(p, DELTA) if loop else p
                k = cap(m2, nt, i)
                new[k] = padd(new.get(k, {}), pshift(q, b))
            else:
                raise ValueError(c)
        state = {m: p for m, p in new.items() if p}
    return state

# ---------------- quotient doubling (same as flat_search.quotient_word, no ends) ----------------
def qletters(half, off=0):
    w = []
    for c, s in half:
        if c in 'xy':
            if s == 0: w += [(c, 0), (c, 1), (c, 1), (c, 0)]
            else: w += [(c, 2 * s), (c, 2 * s - 1), (c, 2 * s + 1), (c, 2 * s)]
        elif c in 'lr': w += [(c, 2 * s - 1), (c, 2 * s)]
        elif c == 'u': w += [(c, 2 * s), (c, 2 * s - 1)]
    return [(c, i + off) for c, i in w]

def parse(word):
    w = word.strip()
    if w.startswith('s.'): w = w[2:]
    return [(tok[0], int(tok[1:])) for tok in w.split('.') if tok]

# ---------------- theta-graph evaluation ----------------
def theta_eval(word, extra=()):
    """Colored theta evaluation <Theta;1,1,2> (axis color 1, arc color 2) of the quotient of 's.'+word,
    built from the definition: position 0 = outside axis edge (through infinity, drawn at far left),
    position 1 = inside axis edge, half strand h = band (2h+2, 2h+3).  Top vertex: band inner strand
    joined to the inside axis edge, band outer strand to the outside edge (nested caps), same at the
    bottom.  One f2 = I - delta^-1 e on the arc right after the top vertex.
    extra: list of (k, pos): after the k-th half letter (k = number of half letters already applied),
    insert an extra f2 on the band whose left strand is at shifted quotient position pos.
    Returns delta^(1+len(extra)) * <Theta>  as an A-poly (to stay polynomial)."""
    half = parse(word)
    # build list of segments: projector slots
    slots = [(0, 2)] + list(extra)
    # assemble op lists for each choice I/E at each slot
    total = {}
    nslot = len(slots)
    for mask in range(1 << nslot):
        ops = [('r', 0), ('r', 1)]           # nested caps 0-3, 1-2
        coeff = ONE
        for si, (k, pos) in enumerate(slots):
            pass
        # interleave
        seq = []
        for k in range(len(half) + 1):
            for si, (kk, pos) in enumerate(slots):
                if kk == k and (mask >> si) & 1:
                    seq.append(('E', pos))
            if k < len(half):
                seq += qletters([half[k]], off=1)
        ops += seq + [('u', 1), ('u', 0)]
        st = run(ops, {(): ONE}, 0)
        if set(st) - {()}: raise ValueError('not closed: %s' % (list(st)[:3],))
        val = st.get((), {})
        # weight: delta^(#I) * (-1)^(#E)
        nE = bin(mask).count('1')
        w = pscale(ppow(DELTA, nslot - nE), (-1) ** nE)
        total = padd(total, pmul(val, w))
    return total, nslot

# ---------------- body state in TL3 ----------------
TL3 = {'I': (3, 4, 5, 0, 1, 2), 'e1': (1, 0, 5, 4, 3, 2), 'e2': (3, 2, 1, 0, 5, 4),
       'e1e2': (1, 0, 3, 2, 5, 4), 'e2e1': (5, 2, 1, 4, 3, 0)}
def body_TL3(body):
    """raw TL3 coefficients of the body tangle (axis = strand 0, band = strands 1,2), top = start of word"""
    half = parse(body)
    ops = qletters(half, off=0)
    st = run(ops, {(3, 4, 5, 0, 1, 2): ONE}, 3)
    inv = {v: k for k, v in TL3.items()}
    out = {}
    for m, p in st.items():
        if m not in inv: raise ValueError('bad final matching %s' % (m,))
        out[inv[m]] = p
    return out
def body_ab(body):
    """returns (delta*a_raw, delta*b_raw) as A-polys:  a = T_I + T_e1*Delta2/delta, b = T_I"""
    T = body_TL3(body)
    TI = T.get('I', {}); Te = T.get('e1', {})
    da = padd(pmul(DELTA, TI), pmul(DELTA2, Te))
    db = pmul(DELTA, TI)
    return da, db

def pdivexact(p, d):
    """exact division of Laurent polys (None if not exact)"""
    p = dict(p); q = {}
    if not p: return {}
    dt = max(d); dc = d[dt]; lo = min(p) - min(d)
    while p:
        e = max(p); c = p[e]; k = e - dt
        if k < lo or c % dc: return None
        q[k] = c // dc
        p = padd(p, pscale(pshift(d, k), -(c // dc)))
    return clean(q)

def to_t(p):
    """A-poly with exponents in one class mod 4 -> (class r, t-poly)"""
    if not p: return 0, {}
    rs = set(e % 4 for e in p)
    if len(rs) != 1: return None
    r = rs.pop()
    return r, {(e - r) // 4: c for e, c in p.items()}
