#!/usr/bin/env python3
"""Type-b cube of the kht++ quotient diagram of a strong inversion (lens STATES).

Conventions (kht++ source, Tangles.cpp): a Morse word read top to bottom; letters x<i>, y<i> (crossings between
positions i,i+1), l<i>/r<i> (cap creating positions i,i+1), u<i> (cup joining positions i,i+1).
Smoothings:  x: 0 = e (turnback, cup-cap), 1 = id (two vertical arcs);   y: 0 = id, 1 = e.
1-3 tangle: one top end (special end), bottom ends b1,b2,b3.  Type b: top--b3 and b1--b2.  Type c: top--b1, b2--b3.
"""
import sys, re, itertools, collections

def parse_word(w):
    w = w.strip()
    out = []
    for tok in w.split('.'):
        tok = tok.strip()
        if not tok or tok == 's':
            continue
        out.append((tok[0], int(tok[1:])))
    return out

def read_kht(path):
    lines = [l.strip() for l in open(path) if l.strip() and not l.strip().startswith('%')]
    word = lines[0]
    orient = 1
    if len(lines) > 1:
        m = re.findall(r'[01]', lines[1])
        if m:
            orient = int(m[-1])
    sym = word.startswith('s.')
    return parse_word(word), orient, sym

# ---------------------------------------------------------------- half diagram: writhe (kht++ Tangle::writhe)
def half_writhe(half):
    """Follow the single strand of the symmetric half diagram (position 0 = virtual axis strand).
    Returns (writhe, list of signs per crossing letter (0 for non-crossings))."""
    # nodes: (level, pos); build adjacency
    L = len(half)
    widths = [2]
    for (c, i) in half:
        w = widths[-1]
        if c in 'lr':
            widths.append(w + 2)
        elif c == 'u':
            widths.append(w - 2)
        else:
            widths.append(w)
    adj = collections.defaultdict(list)
    flipedge = set()
    def join(a, b, flip=False):
        adj[a].append(b); adj[b].append(a)
        if flip:
            flipedge.add((a, b)); flipedge.add((b, a))
    for lev, (c, i) in enumerate(half):
        w = widths[lev]
        if c in 'xy':
            if i == 0:
                join((lev, 1), (lev + 1, 1), True)
                for j in range(2, w):
                    join((lev, j), (lev + 1, j))
            else:
                for j in range(1, w):
                    if j == i:
                        join((lev, i), (lev + 1, i + 1))
                    elif j == i + 1:
                        join((lev, i + 1), (lev + 1, i))
                    else:
                        join((lev, j), (lev + 1, j))
        elif c in 'lr':
            join((lev + 1, i), (lev + 1, i + 1))
            for j in range(1, w):
                join((lev, j), (lev + 1, j if j < i else j + 2))
        elif c == 'u':
            join((lev, i), (lev, i + 1))
            for j in range(1, w):
                if j == i or j == i + 1:
                    continue
                join((lev, j), (lev + 1, j if j < i else j - 2))
    # traverse from (0,1)
    bit = {}
    cur = (0, 1); prev = None
    b = 1  # orientation bit of the top end; the writhe does not depend on it
    bit[cur] = b
    while True:
        nxts = [n for n in adj[cur] if n != prev]
        if not nxts:
            break
        if prev is None and len(adj[cur]) > 1:
            raise ValueError('top end not an end')
        nxt = nxts[0]
        # bit changes: if the edge stays on the same level (cap or cup) the vertical direction reverses -> flip
        if nxt[0] == cur[0]:
            b ^= 1
        if (cur, nxt) in flipedge:
            b ^= 1
        bit[nxt] = b
        prev, cur = cur, nxt
        if cur[0] == L and len(adj[cur]) == 1:
            break
    wr = 0
    signs = []
    for lev, (c, i) in enumerate(half):
        if c in 'xy':
            changer = -1 if c == 'x' else 1
            if i == 0:
                s = -changer
            else:
                same = (bit[(lev, i + 1)] == bit[(lev + 1, i + 1)])
                s = changer if same else -changer
            wr += s
            signs.append(s)
        else:
            signs.append(0)
    return wr, signs

def quotient_word(half, with_twists=True):
    """kht++ Tangle::quotient. Returns (list of letters, list of block labels) ; block label = (kind, index in half word)."""
    out = [('r', 1), ('r', 2)]
    lab = [('top', -1), ('top', -1)]
    for n, (c, i) in enumerate(half):
        if c in 'xy':
            if i == 0:
                out += [(c, 0), (c, 1), (c, 1), (c, 0)]
                lab += [('hook', n)] * 4
            else:
                out += [(c, 2 * i), (c, 2 * i - 1), (c, 2 * i + 1), (c, 2 * i)]
                lab += [('band', n)] * 4
        elif c in 'lr':
            out += [(c, 2 * i - 1), (c, 2 * i)]
            lab += [('cap', n)] * 2
        elif c == 'u':
            out += [('u', 2 * i), ('u', 2 * i - 1)]
            lab += [('cup', n)] * 2
    out.append(('u', 0)); lab.append(('u0', -1))
    wr, _ = half_writhe(half)
    if with_twists:
        t = 'x' if wr > 0 else 'y'
        for _ in range(abs(wr)):
            out += [(t, 1), (t, 1)]
            lab += [('twist', -1)] * 2
    return out, lab, wr

# ---------------------------------------------------------------- matchings
def step_cap(conn, i):
    new = []
    for j, p in enumerate(conn):
        if j == i:
            new += [i + 1, i]
        new.append(p if p < i else p + 2)
    if i == len(conn):
        new += [i + 1, i]
    return tuple(new)

def step_e(conn, i):
    """turnback at i,i+1. returns (new conn, number of circles closed)"""
    a, b = conn[i], conn[i + 1]
    c = list(conn)
    k = 0
    if a == i + 1:
        k = 1
    else:
        if a == -1:
            c[b] = -1
        elif b == -1:
            c[a] = -1
        else:
            c[a] = b; c[b] = a
    c[i] = i + 1; c[i + 1] = i
    return tuple(c), k

def step_cup(conn, i):
    a, b = conn[i], conn[i + 1]
    c = list(conn)
    k = 0
    if a == i + 1:
        k = 1
    else:
        if a == -1:
            c[b] = -1
        elif b == -1:
            c[a] = -1
        else:
            c[a] = b; c[b] = a
    new = []
    for j, p in enumerate(c):
        if j == i or j == i + 1:
            continue
        new.append(p if p < i else p - 2)
    return tuple(new), k

def final_type(conn):
    if len(conn) != 3:
        return '?'
    if conn[2] == -1 and conn[0] == 1:
        return 'b'
    if conn[0] == -1 and conn[1] == 2:
        return 'c'
    return '?'

def crossings_of(word):
    return [n for n, (c, i) in enumerate(word) if c in 'xy']

def one_is_e(letter):
    return letter == 'y'   # y: 1-smoothing = e ; x: 1-smoothing = id

# ---------------------------------------------------------------- DP: bracket of the b-part
def padd(P, Q, shift=0, sign=1):
    for e, v in Q.items():
        P[e + shift] = P.get(e + shift, 0) + sign * v
def pmul_circle(Q):
    R = {}
    for e, v in Q.items():
        R[e + 1] = R.get(e + 1, 0) + v
        R[e - 1] = R.get(e - 1, 0) + v
    return R

def b_bracket(word, typ='b'):
    """sum over states of the given type of (-q)^{|s|} (q+1/q)^{circles}; returns dict exponent->coeff"""
    cur = {(-1,): {0: 1}}
    for (c, i) in word:
        new = {}
        if c in 'lr':
            for conn, P in cur.items():
                nc = step_cap(conn, i)
                padd(new.setdefault(nc, {}), P)
        elif c == 'u':
            for conn, P in cur.items():
                nc, k = step_cup(conn, i)
                padd(new.setdefault(nc, {}), pmul_circle(P) if k else P)
        else:
            for conn, P in cur.items():
                # id smoothing
                bit_id = 0 if one_is_e(c) else 1
                padd(new.setdefault(conn, {}), P, shift=bit_id, sign=(-1) ** bit_id)
                nc, k = step_e(conn, i)
                bit_e = 1 - bit_id
                padd(new.setdefault(nc, {}), pmul_circle(P) if k else P, shift=bit_e, sign=(-1) ** bit_e)
        cur = new
    res = {}
    for conn, P in cur.items():
        if final_type(conn) == typ:
            padd(res, P)
    return {e: v for e, v in res.items() if v}

# ---------------------------------------------------------------- DP: extreme states
NEG = -10 ** 9
def extreme_states(word, typ='b', slack=0, sign=+1, maxstates=2000000):
    """States of final type typ maximising  |s| + sign*circles ... for sign=+1 maximise |s|+k (top quantum degree),
    for sign=-1 minimise |s|-k (bottom).  Returns (M, list of (bits tuple over crossings, |s|, k)) for all states with
    value >= M - slack (top) resp <= M + slack (bottom)."""
    L = len(word)
    # forward reachable matchings per level
    levels = [set([(-1,)])]
    for (c, i) in word:
        new = set()
        for conn in levels[-1]:
            if c in 'lr':
                new.add(step_cap(conn, i))
            elif c == 'u':
                new.add(step_cup(conn, i)[0])
            else:
                new.add(conn); new.add(step_e(conn, i)[0])
        levels.append(new)
    # backward: fut[lev][conn] = best future gain (sign=+1: max of ones+circles ; sign=-1: max of -(ones) + circles)
    fut = [dict() for _ in range(L + 1)]
    for conn in levels[L]:
        fut[L][conn] = 0 if final_type(conn) == typ else NEG
    for lev in range(L - 1, -1, -1):
        c, i = word[lev]
        for conn in levels[lev]:
            if c in 'lr':
                v = fut[lev + 1][step_cap(conn, i)]
            elif c == 'u':
                nc, k = step_cup(conn, i)
                v = fut[lev + 1][nc] + k
            else:
                bit_id = 0 if one_is_e(c) else 1
                g_id = bit_id if sign > 0 else -bit_id
                v1 = fut[lev + 1][conn] + g_id
                nc, k = step_e(conn, i)
                g_e = (1 - bit_id) if sign > 0 else -(1 - bit_id)
                v2 = fut[lev + 1][nc] + g_e + k
                v = max(v1, v2)
            fut[lev][conn] = v
    M = fut[0][(-1,)]
    res = []
    # DFS
    stack = [(0, (-1,), 0, 0, ())]   # lev, conn, ones, circles, bits
    while stack:
        lev, conn, ones, circ, bits = stack.pop()
        if lev == L:
            res.append((bits, ones, circ))
            if len(res) > maxstates:
                raise RuntimeError('too many states')
            continue
        c, i = word[lev]
        val = (ones + circ) if sign > 0 else (-ones + circ)
        if c in 'lr':
            stack.append((lev + 1, step_cap(conn, i), ones, circ, bits))
        elif c == 'u':
            nc, k = step_cup(conn, i)
            stack.append((lev + 1, nc, ones, circ + k, bits))
        else:
            bit_id = 0 if one_is_e(c) else 1
            # id
            g = bit_id if sign > 0 else -bit_id
            if val + g + fut[lev + 1][conn] >= M - slack:
                stack.append((lev + 1, conn, ones + bit_id, circ, bits + (bit_id,)))
            nc, k = step_e(conn, i)
            be = 1 - bit_id
            g = be if sign > 0 else -be
            if val + g + k + fut[lev + 1][nc] >= M - slack:
                stack.append((lev + 1, nc, ones + be, circ + k, bits + (be,)))
    if sign > 0:
        return M, res
    else:
        return -M, res     # minimum of |s| - k

# ---------------------------------------------------------------- F2 linear algebra
def rank_f2(rows):
    """rows: list of python ints (bitmasks). returns rank"""
    piv = {}
    r = 0
    for v in rows:
        while v:
            h = v.bit_length() - 1
            if h in piv:
                v ^= piv[h]
            else:
                piv[h] = v
                r += 1
                break
    return r

def extreme_homology(states):
    """states: list of (bits, ones, circ), all of the same value. complex with basis the states, d = sum over
    single 0->1 flips staying in the set.  Returns dict ones -> betti."""
    idx = {}
    byh = collections.defaultdict(list)
    for (bits, ones, circ) in states:
        byh[ones].append(bits)
    for h in byh:
        for n, b in enumerate(byh[h]):
            idx[b] = n
    ranks = {}
    for h in sorted(byh):
        rows = []
        if h + 1 in byh:
            for b in byh[h]:
                v = 0
                for j in range(len(b)):
                    if b[j] == 0:
                        b2 = b[:j] + (1,) + b[j + 1:]
                        if b2 in idx and len(byh[h + 1]) and sum(b2) == h + 1:
                            v |= 1 << idx[b2]
                rows.append(v)
            ranks[h] = rank_f2(rows)
        else:
            ranks[h] = 0
    betti = {}
    for h in sorted(byh):
        betti[h] = len(byh[h]) - ranks[h] - ranks.get(h - 1, 0)
    return betti, {h: len(byh[h]) for h in byh}

if __name__ == '__main__':
    path = sys.argv[1]
    half, orient, sym = read_kht(path)
    word, lab, wr = quotient_word(half)
    print('half', half, 'writhe', wr)
    print('quotient', '.'.join('%s%d' % t for t in word))
    P = b_bracket(word)
    print('b-bracket', sorted(P.items()))
    M, st = extreme_states(word)
    print('top: M =', M, 'states', len(st), extreme_homology(st))
    m, st = extreme_states(word, sign=-1)
    print('bottom: m =', m, 'states', len(st), extreme_homology(st))
