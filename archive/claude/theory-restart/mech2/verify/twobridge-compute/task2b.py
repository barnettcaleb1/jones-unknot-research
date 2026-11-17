#!/usr/bin/env python3
"""TASK 2 (part B): all normal forms F(n_0,...,n_{k-1}) = (1 0) E Y^{n_{k-1}} E ... E Y^{n_0} (1 0)^T,
n_0 in Z, n_i != 0 (i >= 1), E = rho(Y)^-1 rho(X) = [[1,1-t^4],[-1,-1]], of weight sum|n_i| + k <= W.
Checks: F unit <=> sequence degenerate (empty, (0,1,..,1), (-1,..,-1)); span formula; extreme coefficients +-1."""
import sys, time, collections
from reflib import padd, pshift
W = int(sys.argv[1]) if len(sys.argv) > 1 else 18
def Yp(v1, v2): return v1, pshift(padd(v1, v2), -3)
def Ym(v1, v2): return v1, padd(pshift(v2, 3), v1, -1)
def E(v1, v2): return padd(v1, padd(v2, pshift(v2, 4), -1)), pshift(padd(v1, v2), 0, -1)
def degenerate(seq):
    if not seq: return True
    if all(n == -1 for n in seq): return True
    return seq[0] == 0 and all(n == 1 for n in seq[1:])
def strip(seq):
    seq = list(seq)
    while seq:
        if seq[0] == 0: seq = [seq[1] - 1] + seq[2:] if len(seq) > 1 else []
        elif seq[0] == -1: seq = seq[1:]
        else: break
    return seq
def predicted_span(seq):
    s = 0
    for i, n in enumerate(seq):
        if i == 0: s += 3 * n + 1 if n >= 1 else 3 * abs(n) - 2
        else: s += 3 * abs(n) - 2 + (2 if (n > 0) != (seq[i - 1] > 0) else 0)
    return s
stats = collections.Counter(); problems = []; byw = collections.defaultdict(collections.Counter)
minspan_nondeg = [10**9, None]
def check(seq, v1, weight):
    unit = (len(v1) == 1 and abs(next(iter(v1.values()))) == 1)
    deg = degenerate(seq)
    c = byw[weight]
    c['seqs'] += 1; c['unit'] += unit; c['degenerate'] += deg
    if unit != deg: problems.append(('unit/degenerate', tuple(seq)))
    span = max(v1) - min(v1); ps = predicted_span(strip(seq))
    if span != ps:
        c['spanfail'] += 1
        if len(problems) < 100: problems.append(('span', tuple(seq), span, ps))
    if abs(v1[max(v1)]) != 1 or abs(v1[min(v1)]) != 1:
        c['extremefail'] += 1
        if len(problems) < 100: problems.append(('extreme', tuple(seq)))
    if not deg and span < minspan_nondeg[0]:
        minspan_nondeg[0] = span; minspan_nondeg[1] = tuple(seq)
def rec(seq, v1, v2, weight, first):
    """v = vector after the last E (or the start vector); choose the next exponent n, apply Y^n then E."""
    # n = 0 allowed only for the first block
    rem = W - weight - 1          # weight available for |n|
    if rem < 0: return
    if first:
        e1, e2 = E(v1, v2)
        check(seq + [0], e1, weight + 1)
        rec(seq + [0], e1, e2, weight + 1, False)
    a1, a2 = v1, v2
    for n in range(1, rem + 1):
        a1, a2 = Yp(a1, a2)
        e1, e2 = E(a1, a2)
        check(seq + [n], e1, weight + n + 1)
        rec(seq + [n], e1, e2, weight + n + 1, False)
    a1, a2 = v1, v2
    for n in range(1, rem + 1):
        a1, a2 = Ym(a1, a2)
        e1, e2 = E(a1, a2)
        check(seq + [-n], e1, weight + n + 1)
        rec(seq + [-n], e1, e2, weight + n + 1, False)
t0 = time.time()
sys.setrecursionlimit(10000)
check([], {0: 1}, 0)
rec([], {0: 1}, {}, 0, True)
tot = collections.Counter()
print('weight  seqs  unit  degenerate  spanfail  extremefail')
for w in sorted(byw):
    c = byw[w]; tot.update(c)
    print('%4d %8d %4d %4d %4d %4d' % (w, c['seqs'], c['unit'], c['degenerate'], c['spanfail'], c['extremefail']))
print('TOTAL', dict(tot))
print('smallest span among non-degenerate sequences:', minspan_nondeg)
print('problems:', len(problems))
for p in problems[:40]: print('   ', p)
print('time %.1f s' % (time.time() - t0))
