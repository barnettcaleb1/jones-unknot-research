"""Q1(a): build my own automaton at K = 2,3,4 and compare with engineC1/jauto.py (imported read-only) state by state."""
import sys, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_core as C
from fractions import Fraction as Fr
sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
import jauto
def conv_j(key):
    if isinstance(key, str): return key
    d, j = key
    return (d, (j[0],) + tuple(Fr(x) / j[0] for x in j[1:]))
for K in (2, 3, 4):
    t0 = time.time()
    st, T = C.build_auto(K)
    js, jt = jauto.build(K, verbose=False)
    mine = set(st); theirs = set(conv_j(k) for k in js)
    print('K=%d: mine %d states %d transitions; jauto %d states %d transitions; state sets equal: %s (%.1fs)' % (
        K, len(st), len(T), len(js), len(jt), mine == theirs, time.time() - t0))
    bad = 0
    for (s, m), (Dj, ns) in jt.items():
        cs = conv_j(s)
        mDj, mns = T[(cs, m)]
        d, lc, x = Dj[0], Dj[1][0], tuple(Fr(v) / Dj[1][0] for v in Dj[1][1:])
        if (d, lc, x) != mDj or conv_j(ns) != mns:
            bad += 1
    print('   transitions compared: %d, mismatches %d' % (len(jt), bad))
    # all states have deg r = -1 or <= -4 (clipping-lemma hypothesis)
    degs = sorted(set(k[0] for k in st if not isinstance(k, str)))
    print('   state degrees of r:', degs, ' special:', [k for k in st if isinstance(k, str)])
    # clipping check by direct computation for m = M..M+8 and -M..-M-8
    M = K + 3; cbad = 0
    for s in st:
        for sg in (1, -1):
            base = C.trans(s, sg * M, K)
            for e in range(1, 9):
                r = C.trans(s, sg * (M + e), K)
                if r is None or base is None:
                    continue
                if (r[0][1:], r[1]) != (base[0][1:], base[1]):   # normalised D jet (lc, x) and next key; deg D may shift
                    cbad += 1
    print('   clipping: outputs (lc, normalised D-jet, next key) for |m| = M..M+8 identical from every state: bad =', cbad)
