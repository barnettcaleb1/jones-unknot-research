"""Q1(b): EXACT end-to-end test of the jet automaton on ALL rational boxes of size <= L (size = crossing number of the word:
reduced words of length <= L in X, x, Y, y with leftmost letter X/x, i.e. R(L) before dedup), at BOTH ends.
For each word: exact channel vector (own matrices), own R0 rewriting to normal form Y^n u(m_0..m_{k-1}), then compare
 top:    log-jets of a (order K), deg/lc/log-jet of q, log-jet of b  <->  automaton on u
 bottom: same at t = 0 (computed DIRECTLY from the exact polynomials) <->  automaton on the mirror u'' (notie R2)
for K = 3 (the automaton used by the certificate generator) and K = 4.  Also checks the R0 rewriting exactly
(v(word) = +-t^j * Y^n u(nf)) on every word."""
import sys, time, pickle
from multiprocessing import Pool
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_core as C
from fractions import Fraction as Fr

L = int(sys.argv[1]) if len(sys.argv) > 1 else 12
INV = {'X': 'x', 'x': 'X', 'Y': 'y', 'y': 'Y'}
# matrices on TH-2BR vectors
def apX(v):   # X = [[1, 1-t^4],[0,-t]]
    return (C.padd(v[0], C.pmul(C.ONEMT4, v[1])), C.pneg(C.pshift(v[1], 1)))
def apx(v):   # X^-1 = [[1, t^-1 - t^3],[0, -t^-1]]
    return (C.padd(v[0], C.pmul({-1: 1, 3: -1}, v[1])), C.pneg(C.pshift(v[1], -1)))
def apY(v): return C.Ymul(v, 1)
def apy(v): return C.Ymul(v, -1)
AP = {'X': apX, 'x': apx, 'Y': apY, 'y': apy}

def normal_form(word):
    """R0 rewriting: X = Y E, x = t^-4 E Y^-1.  Returns (n_k, (m_0..m_{k-1})) with v(word) = unit * Y^{n_k} u(m)."""
    groups = [0]          # Y-exponent groups, left to right; E separates groups
    for ch in word:
        if ch == 'Y': groups[-1] += 1
        elif ch == 'y': groups[-1] -= 1
        elif ch == 'X': groups[-1] += 1; groups.append(0)          # Y E
        elif ch == 'x': groups.append(-1)                           # E Y^-1   (unit t^-4)
    g = groups[::-1]      # g[0] = m_0 (acts first), ..., g[k] = n_k
    changed = True
    while changed:
        changed = False
        k = len(g) - 1
        for i in range(1, k):          # interior zero: E Y^0 E = t^4
            if g[i] == 0:
                g = g[:i - 1] + [g[i - 1] + g[i + 1]] + g[i + 2:]
                changed = True; break
        if changed: continue
        if k >= 1 and g[0] == 0:       # E e_1 = Y^-1 e_1
            g = [g[1] - 1] + g[2:]; changed = True; continue
        if k >= 1 and g[0] == -1:      # E Y^-1 e_1 = t^4 e_1
            g = [g[1]] + g[2:]; changed = True; continue
    return g[-1], tuple(g[:-1])

def unit_equal(v, w):
    """v == +-t^j w componentwise (same j and sign)"""
    if not w[0]: return False
    j = max(v[0]) - max(w[0]); s = v[0][max(v[0])] // w[0][max(w[0])]
    if s not in (1, -1): return False
    return all(C.padd(vi, C.pneg({e + j: s * c for e, c in wi.items()})) == {} for vi, wi in zip(v, w))

AUT = {}
def auto(K):
    if K not in AUT: AUT[K] = C.build_auto(K)
    return AUT[K]
def predict(seq, n, K):
    st, T = auto(K)
    out = {}
    for end, s in (('top', seq), ('bot', C.mirror(seq))):
        key, la, _ = C.run_auto(s, K, T)
        dq, lcq, xq = C.q_end(key, K)
        lq = C.logjet(xq)
        if end == 'top': dqw = dq - 3 * n
        else: dqw = (3 - dq) - 3 * n
        out[end] = (la, dqw, lcq, lq, tuple(x + y for x, y in zip(la, lq)))
    return out
def exact(v, K):
    a, b = C.chans(v)
    out = {}
    for end in ('top', 'bot'):
        da, ca, xa = C.enddata(a, end, K); db, cb, xb = C.enddata(b, end, K)
        la = C.logjet(xa); lb = C.logjet(xb); lq = C.logjet(C.sdiv(xb, xa))
        out[end] = (la, db - da, Fr(cb, ca), lq, lb)
    return out

def work(suffix):
    """DFS over reduced words whose rightmost part is `suffix` (letters prepended); returns stats"""
    stats = dict(words=0, integral=0, bad3=0, bad4=0, badR0=0, maxk=0, ex=[])
    v0 = (C.ONE, {})
    for ch in reversed(suffix): v0 = AP[ch](v0)
    stack = [(suffix, v0)]
    while stack:
        w, v = stack.pop()
        if w[0] in 'Xx':
            stats['words'] += 1
            n, nf = normal_form(w)
            if not nf:
                stats['integral'] += 1
                if len(v[0]) != 1: stats['badR0'] += 1
            else:
                stats['maxk'] = max(stats['maxk'], len(nf))
                if not unit_equal(v, C.Ymul(C.box(nf), n)): stats['badR0'] += 1
                for K, nm in ((3, 'bad3'), (4, 'bad4')):
                    if exact(v, K) != predict(nf, n, K):
                        stats[nm] += 1
                        if len(stats['ex']) < 5: stats['ex'].append((w, n, nf, K))
        if len(w) < L:
            for ch in 'XxYy':
                if INV[ch] == w[0]: continue
                stack.append((ch + w, AP[ch](v)))
    return stats

if __name__ == '__main__':
    t0 = time.time()
    sufs = []
    for a in 'XxYy':
        for b in 'XxYy':
            if INV[b] == a: continue
            sufs.append(b + a)          # length-2 suffixes (rightmost two letters)
    # words of length 1 handled separately
    tot = dict(words=0, integral=0, bad3=0, bad4=0, badR0=0, maxk=0, ex=[])
    for w in ('X', 'x'):
        st = work(w) if False else None
    with Pool(10) as P:
        res = P.map(work, sufs)
    for r in res:
        for k in ('words', 'integral', 'bad3', 'bad4', 'badR0'): tot[k] += r[k]
        tot['maxk'] = max(tot['maxk'], r['maxk']); tot['ex'] += r['ex']
    # length-1 words X, x
    for w in ('X', 'x'):
        v = AP[w]((C.ONE, {}))
        n, nf = normal_form(w); tot['words'] += 1
        if not nf: tot['integral'] += 1
        else:
            if not unit_equal(v, C.Ymul(C.box(nf), n)): tot['badR0'] += 1
            for K, nm in ((3, 'bad3'), (4, 'bad4')):
                if exact(v, K) != predict(nf, n, K): tot[nm] += 1
    print('L <= %d: reduced words with leftmost X/x: %d (integral %d, non-integral %d), max k = %d' % (
        L, tot['words'], tot['integral'], tot['words'] - tot['integral'], tot['maxk']))
    print('R0 rewriting exact (v(word) = +-t^j Y^n u(nf)) failures:', tot['badR0'])
    print('automaton K=3 mismatches (top+bottom, a/b/q log-jets, deg q, lc q):', tot['bad3'])
    print('automaton K=4 mismatches:', tot['bad4'])
    print('examples:', tot['ex'][:5])
    print('time %.1fs' % (time.time() - t0))
