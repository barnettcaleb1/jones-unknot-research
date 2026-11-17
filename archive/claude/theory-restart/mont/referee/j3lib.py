"""Independent coloured Jones J_3 (spin 1) of the RIGHT-HALF knot K_R of an axis-free half-diagram word, by a Kauffman
bracket sweep of the 2-cable with one Jones-Wenzl f_2 inserted.  Conventions copied from tools/kauffman.py (crossing 'x':
A*[same matching] + A^-1*[cup-cap]; loop factor delta = -A^2 - A^-2).  Only the A-variable bracket is used here; nothing from
flat_search / lp.J.  K_R diagram: closing strand at position 0 on the far left, half-diagram position p -> position p+1."""

def padd(p, q, c=1):
    for e, v in q.items():
        nv = p.get(e, 0) + c * v
        if nv:
            p[e] = nv
        elif e in p:
            del p[e]

def pshift(p, k, c=1):
    return {e + k: c * v for e, v in p.items()}

def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}

DELTA = {2: -1, -2: -1}

def pdelta(p):
    return pmul(p, DELTA)

def cap(m, i):
    m2 = [(x + 2 if x >= i else x) for x in m]
    m2[i:i] = [i + 1, i]
    return tuple(m2)

def cup(m, i):
    p, q = m[i], m[i + 1]
    m = list(m)
    loop = False
    if p == i + 1:
        loop = True
    else:
        m[p] = q; m[q] = p
    del m[i:i + 2]
    m = [(x - 2 if x > i + 1 else x) for x in m]
    return tuple(m), loop

def sweep(ops, init):
    """ops: list of (c, i) with c in 'x','y','cap','cup'; init: dict state->poly. returns final dict"""
    state = dict(init)
    for c, i in ops:
        new = {}
        for m, p in state.items():
            if c == 'cap':
                padd(new.setdefault(cap(m, i), {}), p)
            elif c == 'cup':
                m2, loop = cup(m, i)
                padd(new.setdefault(m2, {}), pdelta(p) if loop else p)
            else:
                a, b = (1, -1) if c == 'x' else (-1, 1)
                padd(new.setdefault(m, {}), pshift(p, a))
                m2, loop = cup(m, i)
                q = pdelta(p) if loop else p
                padd(new.setdefault(cap(m2, i), {}), pshift(q, b))
        state = {m: p for m, p in new.items() if p}
    return state

def parse(word):
    w = word.strip()
    if w.startswith('s.'):
        w = w[2:]
    return [(tok[0], int(tok[1:])) for tok in w.split('.') if tok]

def kr_ops(word):
    """planar Morse ops of K_R (single strands). None if the word has axis letters."""
    ops = []
    for c, s in parse(word):
        if c in 'xy':
            if s == 0:
                return None
            ops.append((c, s))
        elif c in 'lr':
            ops.append(('cap', s))
        elif c == 'u':
            ops.append(('cup', s))
    ops.append(('cup', 0))
    return ops

def double(ops):
    out = []
    for c, j in ops:
        if c in 'xy':
            out += [(c, 2 * j + 1), (c, 2 * j), (c, 2 * j + 2), (c, 2 * j + 1)]
        elif c == 'cap':
            out += [('cap', 2 * j), ('cap', 2 * j + 1)]
        elif c == 'cup':
            out += [('cup', 2 * j + 1), ('cup', 2 * j)]
    return out

def bracket_KR(word):
    ops = kr_ops(word)
    if ops is None:
        return None
    st = sweep(ops, {(1, 0): {0: 1}})
    if set(st) - {()}:
        return None
    return st.get((), {})

def j3_raw(word):
    """delta * <2-cable with f_2> (unnormalised, A-variable)."""
    ops = kr_ops(word)
    if ops is None:
        return None
    dops = double(ops)
    init = {(3, 2, 1, 0): dict(DELTA), (1, 0, 3, 2): {0: -1}}
    st = sweep(dops, init)
    if set(st) - {()}:
        return None
    return st.get((), {})

def pdiv(p, d):
    p = dict(p); q = {}
    if not p:
        return {}
    dt = max(d); dc = d[dt]; db = min(d); lo = min(p) - db
    while p:
        e = max(p); c = p[e]; k = e - dt
        if k < lo or c % dc:
            return None
        q[k] = c // dc
        padd(p, pshift(d, k, -(c // dc)))
    return q

def to_t(pA):
    """A-poly that is (monomial) x poly(A^4) -> dict in t = A^4 (exponent floor), or None"""
    es = sorted(pA)
    r0 = es[0] % 4
    if any((e - r0) % 4 for e in es):
        return None
    return {(e - r0) // 4: c for e, c in pA.items()}

def normalize(J):
    s = sum(c * (-1) ** (e % 2) for e, c in J.items())
    d = sum(e * c * (-1) ** ((e - 1) % 2) for e, c in J.items())
    if s not in (1, -1) or d % s:
        return None
    k = d // s
    sgn = s * (-1) ** (k % 2)
    return {e + k: sgn * c for e, c in J.items()}

def J3(word):
    """normalised J_3(K_R) as a dict in t = A^4 (t <-> 1/t ambiguity left to the caller)"""
    r = j3_raw(word)
    if r is None:
        return None
    d2 = pmul(DELTA, DELTA); padd(d2, {0: 1}, -1)          # Delta_2 = delta^2 - 1
    dd = pmul(DELTA, d2)                                 # divide by delta * Delta_2
    q = pdiv(r, dd)
    if q is None:
        return ('NONDIV', r)
    qt = to_t(q)
    if qt is None:
        return ('NOT_A4', q)
    return normalize(qt)

def jones_KR(word):
    """normalised Jones-type invariant of K_R from the plain bracket (in t = A^4), for identification only"""
    b = bracket_KR(word)
    if b is None:
        return None
    q = pdiv(b, DELTA)
    return to_t(q)

def inv(p):
    return {-e: c for e, c in p.items()}
