"""twist_identity.py -- the full-twist word used by rule (R) is the full twist: full_twist_events(m, 'X') equals
(s_0 s_1 ... s_{m-2})^m in the braid group B_m, checked in the Artin representation B_m -> Aut(F_m) (faithful, Artin 1925),
for m = 2..9 (and the 'Y' version equals its inverse)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import translate as TR, gen_kernel as G
def aut_of(seq, m):
    imgs = {i: (i + 1,) for i in range(m)}            # generator a_i <-> symbol i+1
    for typ, j in seq:
        s = G.sigma(j, 1 if typ == 'X' else -1)
        imgs = {i: G.apply_aut(s, w) for i, w in imgs.items()}
    return imgs
ok = True
for m in range(2, 10):
    tw = TR.full_twist_events(m, 'X'); std = [('X', j) for j in range(m - 1)] * m
    a, b = aut_of(tw, m), aut_of(std, m)
    inv_ok = aut_of(TR.full_twist_events(m, 'X') + TR.full_twist_events(m, 'Y'), m) == {i: (i + 1,) for i in range(m)}
    print('m =', m, 'crossings', len(tw), '== (s_0..s_{m-2})^m:', a == b, '| X-twist . Y-twist = id:', inv_ok)
    ok &= (a == b) and inv_ok
print('ALL OK' if ok else 'FAIL')
