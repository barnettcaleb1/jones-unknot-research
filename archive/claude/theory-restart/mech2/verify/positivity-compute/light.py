#!/usr/bin/env python3
"""Lighter state sum for the type-b part of a 1-3 tangle diagram: Euler characteristic polynomial, and the extreme values
of |s| + k (max) and |s| - k (min) over type-b states with the number of states attaining them."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sidiag as S
TOP = S.TOP

def _mulq(p, shift, sign):
    return {e + shift: sign * v for e, v in p.items()}

def _loop(p):
    r = {}
    for e, v in p.items():
        r[e + 1] = r.get(e + 1, 0) + v
        r[e - 1] = r.get(e - 1, 0) + v
    return r

def _acc(new, key, poly, mx, mn):
    t = new.get(key)
    if t is None:
        new[key] = [dict(poly), mx, mn]
        return
    tp = t[0]
    for e, v in poly.items():
        nv = tp.get(e, 0) + v
        if nv:
            tp[e] = nv
        elif e in tp:
            del tp[e]
    a = t[1]
    if mx[0] > a[0]:
        t[1] = mx
    elif mx[0] == a[0]:
        t[1] = (a[0], a[1] + mx[1])
    a = t[2]
    if mn[0] < a[0]:
        t[2] = mn
    elif mn[0] == a[0]:
        t[2] = (a[0], a[1] + mn[1])

def cube_light(word):
    state = {(TOP,): [{0: 1}, (0, 1), (0, 1)]}
    for (c, i) in word:
        new = {}
        if c in ('cap', 'l', 'r'):
            for m, (p, mx, mn) in state.items():
                _acc(new, S._cap(m, i), p, mx, mn)
        elif c == 'u':
            for m, (p, mx, mn) in state.items():
                m2, loop = S._cup(m, i)
                if loop:
                    _acc(new, m2, _loop(p), (mx[0] + 1, mx[1]), (mn[0] - 1, mn[1]))
                else:
                    _acc(new, m2, p, mx, mn)
        else:
            vert1 = (c == 'x')      # vertical smoothing is the 1-smoothing for x
            for m, (p, mx, mn) in state.items():
                # vertical
                if vert1:
                    _acc(new, m, _mulq(p, 1, -1), (mx[0] + 1, mx[1]), (mn[0] + 1, mn[1]))
                else:
                    _acc(new, m, p, mx, mn)
                # turnback
                m2, loop = S._cup(m, i)
                m3 = S._cap(m2, i)
                ds = 0 if vert1 else 1
                q = _mulq(p, 1, -1) if ds else p
                if loop:
                    _acc(new, m3, _loop(q), (mx[0] + ds + 1, mx[1]), (mn[0] + ds - 1, mn[1]))
                else:
                    _acc(new, m3, q, (mx[0] + ds, mx[1]), (mn[0] + ds, mn[1]))
        state = new
    return state

def typeb(word):
    st = cube_light(word)
    for v in st.values():
        v[0] = {e: c for e, c in v[0].items() if c}
    return st.get(S.TYPE_B), st.get(S.TYPE_C)

if __name__ == '__main__':
    import time
    for w in sys.argv[1:]:
        half = S.parse(w)
        t0 = time.time()
        b, c = typeb(S.band_word(half, 0))
        t1 = time.time()
        cnt = S.cube_counts(S.band_word(half, 0))[S.TYPE_B]
        t2 = time.time()
        P = S.euler_from_counts(cnt)
        M = max(a + k for a, k in cnt); m = min(a - k for a, k in cnt)
        E1 = sum(v for (a, k), v in cnt.items() if a + k == M); E0 = sum(v for (a, k), v in cnt.items() if a - k == m)
        print(w, 'light %.3fs full %.3fs' % (t1 - t0, t2 - t1), 'agree:', P == b[0], (M, E1) == b[1], (m, E0) == b[2], S.unit_of(b[0]), b[1], b[2])
