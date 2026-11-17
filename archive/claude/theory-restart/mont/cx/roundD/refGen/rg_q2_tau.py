"""Q2: tau-law (Lemma S3) for every non-integral rational box:
   (delta, lc_top(q) lc_bot(q), sigma, tau) = (-1, -1, 0, -1),  delta = deg_top q - deg_bot q,
   sigma = l1_top(q) + l1_bot(q), tau = l2_top(q) + l2_bot(q).
(a) own product automaton (state(u), state(u'')) at K = 3 and K = 4, exponents clipped independently (sound by the
    clipping lemma, proved in REPORT), enumerating ALL reachable product states;
(b) direct exact check (no automaton, no R2) on all normal forms of size k + sum|m_i| <= S."""
import sys, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_core as C
from fractions import Fraction as Fr
from collections import Counter
for K in (3, 4):
    M = K + 3
    st, T = C.build_auto(K)
    start = ('init', 'init')
    seen = {start}; todo = [start]; nedges = 0
    while todo:
        s, s2 = todo.pop()
        for m in range(-M - 4, M + 5):
            if m == 0: continue
            if s == 'init':
                if m == -1: continue
                mm = -m - 1
            else:
                mm = -m
            a = T.get((s, C.clip(m, M))); b = T.get((s2, C.clip(mm, M)))
            assert a is not None and b is not None, (s, s2, m, mm)
            nedges += 1
            ns = (a[1], b[1])
            if ns not in seen: seen.add(ns); todo.append(ns)
    vals = Counter()
    for (s, s2) in seen:
        if s == 'init': continue
        assert s2 != 'init'
        d1, c1, x1 = C.q_end(s, K); d2, c2, x2 = C.q_end(s2, K)
        l1 = C.logjet(x1); l2 = C.logjet(x2)
        vals[(d1 - (3 - d2), c1 * c2, l1[0] + l2[0], l1[1] + l2[1])] += 1
    print('K=%d: reachable product states (excl. init) %d; (delta, lc_t*lc_b, sigma, tau) values: %s' % (
        K, len(seen) - 1, dict(vals)))
    if K == 4:
        # third-order sum as a by-product (not claimed by C1)
        v3 = Counter()
        for (s, s2) in seen:
            if s == 'init': continue
            l1 = C.logjet(C.q_end(s, K)[2]); l2 = C.logjet(C.q_end(s2, K)[2])
            v3[l1[2] + l2[2]] += 1
        print('   (by-product) l3_top + l3_bot of q over reachable product states:', dict(v3))
S = int(sys.argv[1]) if len(sys.argv) > 1 else 16
t0 = time.time()
cnt = Counter(); n = 0
for seq in C.normal_forms_size(S):
    a, b = C.chans(C.box(seq))
    dt = {};
    for end in ('top', 'bot'):
        da, ca, xa = C.enddata(a, end, 3); db, cb, xb = C.enddata(b, end, 3)
        lq = C.logjet(C.sdiv(xb, xa))
        dt[end] = (db - da, Fr(cb, ca), lq)
    key = (dt['top'][0] - dt['bot'][0], dt['top'][1] * dt['bot'][1], dt['top'][2][0] + dt['bot'][2][0],
           dt['top'][2][1] + dt['bot'][2][1])
    cnt[key] += 1; n += 1
print('direct exact check, all %d normal forms of size <= %d: values %s (%.1fs)' % (n, S, dict(cnt), time.time() - t0))
