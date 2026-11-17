#!/usr/bin/env python3
"""TASK 2 (part A): all freely reduced words in X, Y, x=X^-1, y=Y^-1 up to a given length.
For each word: g(w) = (1 0) rho(w) (1 0)^T exactly (first letter applied first);
  U(w): g(w) is a unit +-t^n;
  D(w): det K_w = 1 (2x2 integer matrices validated in detcheck.py against the full symmetric diagram);
  N(w): my own normal form in Z/2 * Z = <e> * <Y> (X = e.Y, x = y.e in word order, e.e = 1), trailing Y-power dropped,
        is 'degenerate': empty, (0,1,...,1) or (-1,...,-1)   [= w in <X><Y> modulo the centre];
  span formula of Theorem B on the stripped normal form, and the extreme coefficients.
Reports every word where U, D, N disagree, and every failure of the span formula / extreme coefficients."""
import sys, time, collections
from reflib import padd, pshift
MAXLEN = int(sys.argv[1]) if len(sys.argv) > 1 else 12
INVL = {'X': 'x', 'x': 'X', 'Y': 'y', 'y': 'Y'}
def act(letter, v1, v2):
    if letter == 'Y': return v1, pshift(padd(v1, v2), -3)
    if letter == 'y': return v1, padd(pshift(v2, 3), v1, -1)
    if letter == 'X': return padd(v1, padd(v2, pshift(v2, 4), -1)), pshift(v2, 1, -1)
    return padd(v1, padd(pshift(v2, -1), pshift(v2, 3), -1)), pshift(v2, -1, -1)
def normal_form(word):
    seq = [0]
    def put_e():
        if seq[-1] == 0 and len(seq) >= 2: seq.pop()
        else: seq.append(0)
    for L in word:
        if L == 'Y': seq[-1] += 1
        elif L == 'y': seq[-1] -= 1
        elif L == 'X': put_e(); seq[-1] += 1
        else: seq[-1] -= 1; put_e()
    return seq[:-1]
def degenerate(seq):
    if not seq: return True
    if all(n == -1 for n in seq): return True
    if seq[0] == 0 and all(n == 1 for n in seq[1:]): return True
    return False
def strip(seq):
    seq = list(seq)
    while seq:
        if seq[0] == 0:
            seq = [seq[1] - 1] + seq[2:] if len(seq) > 1 else []
        elif seq[0] == -1:
            seq = seq[1:]
        else: break
    return seq
def predicted_span(seq):
    """seq stripped: seq[0] not in {0,-1}"""
    s = 0
    for i, n in enumerate(seq):
        if i == 0:
            s += 3 * n + 1 if n >= 1 else 3 * abs(n) - 2
        else:
            s += 3 * abs(n) - 2 + (2 if (n > 0) != (seq[i - 1] > 0) else 0)
    return s
stats = collections.Counter(); bylen = collections.defaultdict(collections.Counter)
problems = []
def visit(word, v1, v2, a, b):
    L = len(word)
    unit = (len(v1) == 1 and abs(next(iter(v1.values()))) == 1)
    det1 = (abs(a) == 1)
    seq = normal_form(word)
    deg = degenerate(seq)
    c = bylen[L]
    c['words'] += 1; c['unit'] += unit; c['det1'] += det1; c['degenerate'] += deg
    if not (unit == det1 == deg):
        problems.append(('U/D/N disagree', word, unit, det1, deg))
    st = strip(seq)
    span = max(v1) - min(v1)
    ps = predicted_span(st)
    if span != ps:
        c['span formula fails'] += 1
        if len(problems) < 200: problems.append(('span', word, tuple(seq), tuple(st), span, ps))
    if abs(v1[max(v1)]) != 1 or abs(v1[min(v1)]) != 1:
        c['extreme coefficient not +-1'] += 1
        if len(problems) < 200: problems.append(('extreme', word, v1[max(v1)], v1[min(v1)]))
    if L == MAXLEN: return
    last = word[-1] if word else ''
    for nx in 'XYxy':
        if last and nx == INVL[last]: continue
        w1, w2 = act(nx, v1, v2)
        if nx == 'Y': a2, b2 = a, b - a
        elif nx == 'y': a2, b2 = a, b + a
        elif nx == 'X': a2, b2 = a - 2 * b, b
        else: a2, b2 = a + 2 * b, b
        visit(word + nx, w1, w2, a2, b2)
t0 = time.time()
sys.setrecursionlimit(10000)
visit('', {0: 1}, {}, 1, 0)
tot = collections.Counter()
print('len  words   unit   det1   degenerate  spanfail  extremefail')
for L in sorted(bylen):
    c = bylen[L]; tot.update(c)
    print('%3d %7d %6d %6d %6d %6d %6d' % (L, c['words'], c['unit'], c['det1'], c['degenerate'], c['span formula fails'], c['extreme coefficient not +-1']))
print('TOTAL', dict(tot))
print('problems:', len(problems))
for p in problems[:60]: print('   ', p)
print('time %.1f s' % (time.time() - t0))
