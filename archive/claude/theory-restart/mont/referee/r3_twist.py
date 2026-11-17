"""Referee P3: TWIST-2CH. Direct J(T_n), n = -8..14, vs (i) letter-63 formula, (ii) NEST formula, (iii) necklace word,
(iv) own pinned v_B; span/endpoint claims; non-rationality brute force."""
import sys, itertools
from rlib import *
import alex

def Tn(n):
    tw_ = ['y1'] * n if n > 0 else ['x1'] * (-n)
    return '.'.join(['s', 'r1', 'x2'] + tw_ + 'y0.r2.y0.y1.y0.y1.x2.u3.u1'.split('.'))

B = 'y0.r2.y0.y1.y0.y1.x2.u1'
alpha = mul(mono(-5), P((1, 2), (-1, 1), (1, 0)))
beta = add(mul(mono(2), P((1, 4), (-1, 3), (-1, 0))), mul(mono(-6), P((1, 2), (-1, 1), (1, 0))))
c, Js = pin(B, (1, -1, 2, -2, 3, -3))
print('pin candidates for B:', len(c))
vB = c[0]
print('v_B = (', fmt(vB[0]), ' , ', fmt(vB[1]), ')  n0 =', nax(B), ' eps =', eps(vB))
claimed_v = [P((1, -7), (1, -4), (-1, -3)), P((1, -15), (1, -12), (1, -11), (1, -8), (-1, -6))]
print('matches claimed v_B:', vB == claimed_v)
print('b(v_B) =', fmt(b_of(vB)), ' #terms', len(b_of(vB)))
J31 = J('s.' + B)
print('J(s.B) =', fmt(J31), ' Alexander(s.B) =', alex.alex_poly('s.' + B))
PB = mul(mono(-15), P((1, 2), (-1, 1), (1, 0)))
QB = sub(J31, PB)
# check P_B, Q_B against channel decomposition of e1^T X^-m v
d = [{}, ONE]
v2 = vB[1]
P_chan = add(vB[0], mul(P((1, 0), (-1, 1)), mul(P((1, 0), (1, 2)), v2)))
print('P_B = a + (1-t)(1+t^2) v2 :', P_chan == PB)
ok = {'letter63': 0, 'nest': 0, 'neckword': 0, 'pinned': 0}
tot = 0
rows = []
for n in range(-8, 15):
    w = Tn(n)
    Jw = J(w)
    if Jw is None:
        print(n, 'not a knot'); continue
    tot += 1
    l63 = normalize(add(mul(mono(2 * n), alpha), mul(mono(n, (-1) ** (n % 2)), beta)))
    nest = add(mul(mono(4 * n + 4), PB), mul(mono(3 * n + 3, (-1) ** ((n + 1) % 2)), QB))
    nw = J('s.' + neck(n + 1, [B]))
    pr = normalize(mvec(Xpow(-(n + 1)), vB)[0])
    ok['letter63'] += (l63 == Jw); ok['nest'] += (nest == Jw); ok['neckword'] += (nw == Jw); ok['pinned'] += (pr == Jw)
    rows.append((n, span(Jw), bot(Jw), top(Jw), Jw[bot(Jw)], Jw[top(Jw)]))
print('of', tot, ':', ok)
for r in rows:
    print('n=%3d span %2d  [%d,%d] lc_bot %+d lc_top %+d' % r)
# blocks overlap
for n in range(8, 14):
    print('n', n, 'P-part', (4 * n - 11, 4 * n - 9), 'Q-part', (3 * n - 12, 3 * n), 'overlap' if 4 * n - 11 <= 3 * n else 'separate')

# non-rationality brute force: rational vectors rho(w)e1, words <= 7 over XxYy, with normalised a = J(s.B) or its mirror
def mirror(p): return {-e: c for e, c in p.items()}
found = {}
for L in range(1, 8):
    for w in itertools.product('XxYy', repeat=L):
        w = ''.join(w)
        if any(w[i].lower() == w[i + 1].lower() and w[i] != w[i + 1] for i in range(L - 1)):
            continue
        v = apply(w)
        a = v[0]
        na = normalize(a)
        if na is None:
            continue
        if na == J31:
            # normalise vector by same unit as a
            k = None
            for kk in range(-60, 61):
                for s in (1, -1):
                    if unitmul(s, kk, a) == na:
                        k = (s, kk)
            vv = [unitmul(k[0], k[1], v[0]), unitmul(k[0], k[1], v[1])]
            key = (tuple(sorted(vv[0].items())), tuple(sorted(vv[1].items())))
            found[key] = (w, len(b_of(vv)))
print('distinct normalised rational vectors with a = J(s.B):', len(found), ' b-term counts:', sorted(set(x[1] for x in found.values())))
