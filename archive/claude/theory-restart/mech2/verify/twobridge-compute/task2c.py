#!/usr/bin/env python3
"""Extra checks on the statements around Theorem B (exact arithmetic):
 (1) the automaton of the proof: maxdeg F = sum of gains, mindeg F = 4k - sum of gains of the mirrored sequence
     (-n_0-1, -n_1, ..., -n_{k-1}), leading coefficients +-1; all normal forms of weight <= W;
 (2) the literal reading of the span formula (index rule c_i for i >= 1 applied to the UNSTRIPPED sequence): where it fails;
 (3) positive words Y^a1 X^b1 ... Y^an X^bn (all exponents > 0): top term (-1)^B t^B, bottom term t^(-3A), span 3A+B;
 (4) one-block formula and mirror identity J_{w^-}(t) = J_w(1/t)  (exact, no unit);
 (5) identity F(n)(1/t) = t^(-4k) F(-n_0-1,-n_1,...)(t)."""
import sys, itertools, collections, random
from reflib import padd, pshift, pmul, pflip, J_matrix, pstr
W = int(sys.argv[1]) if len(sys.argv) > 1 else 16
def Yp(v1, v2): return v1, pshift(padd(v1, v2), -3)
def Ym(v1, v2): return v1, padd(pshift(v2, 3), v1, -1)
def E(v1, v2): return padd(v1, padd(v2, pshift(v2, 4), -1)), pshift(padd(v1, v2), 0, -1)
def F(seq):
    v1, v2 = {0: 1}, {}
    for n in seq:
        for _ in range(abs(n)):
            v1, v2 = (Yp if n > 0 else Ym)(v1, v2)
        v1, v2 = E(v1, v2)
    return v1
def gains(seq):
    """sum of gains along the automaton of the proof (states P, Q_m, U_m, degenerate r=0 / r=-1)."""
    total = 0
    state = 'zero'      # value of r before applying Y^n: exact 0 at the start
    for n in seq:
        # state in {'zero' (r = 0 exactly), 'minus1' (r = -1 exactly), 'R', 'S'}
        if state == 'zero':
            if n == 0: total += 0; state = 'minus1'; continue          # r = 0 before E: gain 0, then r = -1
            if n == -1: total += 4; state = 'zero'; continue           # r = -1 before E: gain 4, then r = 0
            if n >= 1: total += 1; state = 'R'; continue               # P
            m = -n; total += 3 * m + 1; state = 'S'; continue          # Q_m, m >= 2
        if state == 'minus1':
            if n == 1: total += 0; state = 'minus1'; continue          # r = 0 again
            if n >= 2: total += 1; state = 'R'; continue               # P
            m = -n; total += 3 * (m + 1) + 1; state = 'S'; continue    # r = -[m] - t^(3m): deg 3m = Q_(m+1)
        if state == 'R':
            if n >= 1: total += 1; state = 'R'; continue
            m = -n; total += 3 * m + 3; state = 'S'; continue          # U_m
        if state == 'S':
            if n >= 1: total += 1; state = 'R'; continue
            m = -n; total += 3 * m + 1; state = 'S'; continue          # Q_m
    return total
def literal_span(seq):
    """the theorem's formula read literally on the unstripped normal form: degenerate steps contribute 0, a generic
    step i >= 1 contributes 3|n_i| - 2 + 2[sign n_i != sign n_{i-1}] (sign(0) taken as +), step 0 by the c_0 rule."""
    s = 0; deg = True
    for i, n in enumerate(seq):
        if deg:
            if i == 0 and n in (0, -1): continue
            if i > 0 and ((seq[0] == 0 and n == 1) or (seq[0] == -1 and n == -1)): continue
            deg = False
        if i == 0: s += 3 * n + 1 if n >= 1 else 3 * abs(n) - 2
        else: s += 3 * abs(n) - 2 + (2 if (n > 0) != (seq[i - 1] >= 0) else 0)
    return s
def seqs(W):
    def rec(seq, weight):
        yield seq
        rem = W - weight - 1
        if rem < 0: return
        rng = list(range(-rem, rem + 1))
        for n in rng:
            if n == 0 and seq: continue
            yield from rec(seq + [n], weight + abs(n) + 1)
    yield from rec([], 0)
st = collections.Counter(); ex = collections.defaultdict(list)
for seq in seqs(W):
    k = len(seq)
    f = F(seq)
    st['normal forms'] += 1
    g = gains(seq); mir = [-seq[0] - 1] + [-n for n in seq[1:]] if seq else []
    gm = gains(mir)
    if max(f) != g: st['maxdeg != sum of gains'] += 1; ex['max'].append(tuple(seq))
    if min(f) != 4 * k - gm: st['mindeg != 4k - mirror gains'] += 1; ex['min'].append(tuple(seq))
    if abs(f[max(f)]) != 1 or abs(f[min(f)]) != 1: st['extreme coefficient'] += 1
    # (5)
    if pflip(f) != pshift(F(mir), -4 * k): st['mirror identity fails'] += 1; ex['mirror'].append(tuple(seq))
    # (2)
    if literal_span(seq) != max(f) - min(f):
        st['literal span formula fails'] += 1
        if len(ex['literal']) < 12: ex['literal'].append((tuple(seq), 'true span', max(f) - min(f), 'literal', literal_span(seq)))
        pre = 'prefix' if seq and seq[0] in (0, -1) else 'no prefix'
        st['literal fails, ' + pre] += 1
print('(1),(2),(5) normal forms of weight <=', W, ':', dict(st))
for k, v in ex.items(): print('   examples', k, v[:12])
# (3) positive words
st3 = collections.Counter()
def blocks(total):
    # compositions of total into an even number of positive parts a1,b1,...,an,bn
    def rec(rem, parts):
        if rem == 0:
            if parts and len(parts) % 2 == 0: yield parts
            return
        for p in range(1, rem + 1):
            yield from rec(rem - p, parts + [p])
    yield from rec(total, [])
for L in range(2, 17):
    for parts in blocks(L):
        w = ''.join(('Y' if i % 2 == 0 else 'X') * p for i, p in enumerate(parts))
        A = sum(parts[0::2]); B = sum(parts[1::2])
        f = J_matrix(w)
        st3['positive words Y..X'] += 1
        if max(f) != B or f[max(f)] != (-1) ** B: st3['top term wrong'] += 1
        if min(f) != -3 * A or f[min(f)] != 1: st3['bottom term wrong'] += 1
        if max(f) - min(f) != 3 * A + B: st3['span wrong'] += 1
print('(3) positive words up to length 16:', dict(st3))
# (4)
bad4 = 0
def geo(n, z):   # [n]_z as dict in t, z = (sign, exponent)
    s, e = z
    return {e * i: s ** i for i in range(n)}
for a in range(1, 8):
    for b in range(1, 8):
        f = J_matrix('Y' * a + 'X' * b)
        rhs = padd({0: 1}, pmul(pmul({-3: 1}, geo(a, (1, -3))), pmul({0: 1, 4: -1}, geo(b, (-1, 1)))))
        if f != rhs: bad4 += 1
print('(4) one-block formula, a,b <= 7: failures', bad4)
random.seed(1); bad5 = 0
inv = {'X': 'x', 'x': 'X', 'Y': 'y', 'y': 'Y'}
for _ in range(20000):
    w = ''.join(random.choice('XYxy') for _ in range(random.randint(0, 14)))
    if pflip(J_matrix(w)) != J_matrix(''.join(inv[c] for c in w)): bad5 += 1
print('(4) mirror identity J_{w^-}(t) = J_w(1/t), 20000 random words of length <= 14: failures', bad5)
