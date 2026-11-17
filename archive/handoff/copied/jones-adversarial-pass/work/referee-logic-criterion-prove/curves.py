"""BFS over 3|3 curves g(c) (g braid words), dedupe by the line [v], compute D(R_s) from the line alone."""
import sys, os, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastD import *
T34 = lmul({4: 1, 0: 1, -4: 1}, {6: 1, 2: 1, -2: 1, -6: 1})   # [3][4]
def ldiv_exact(p, q):
    sp, a = to_poly(p); sq, b = to_poly(q)
    r = poly_exact_div(a, b)
    return {sp - sq + i: c for i, c in enumerate(r) if c}
def normkey(v):
    lo = min(e for p in v for e in p)
    w = [{e - lo: c for e, c in p.items()} for p in v]
    for p in w:
        if p:
            if p[max(p)] < 0: w = [{e: -c for e, c in q.items()} for q in w]
            break
    return tuple(tuple(sorted(p.items())) for p in w)
def nvec(v):
    # n_s = bar(v)^T G / (-[3][4])
    out = []
    for j in range(DIM):
        acc = {}
        for i in range(DIM):
            if v[i]: acc = ladd(acc, lmul(lbar(v[i]), GRAM[i][j]))
        out.append(ldiv_exact(lscale(acc, -1), T34) if acc else {})
    return out
KAP = ldiv_exact(ladd({24: 1}, {0: 1}, -1), {4: 1, 0: 1, -4: 1})   # (A^24-1)/[3]
def Rmat(v):
    n = nvec(v)
    M = [[{} for _ in range(DIM)] for _ in range(DIM)]
    for i in range(DIM):
        for j in range(DIM):
            p = lmul(KAP, lmul(v[i], n[j])) if (v[i] and n[j]) else {}
            if i == j: p = ladd(p, ONE)
            M[i][j] = lscale(p, 1, -12)
    return M
def Dexact(M):
    lo = min(e for row in M for p in row for e in p); hi = max(e for row in M for p in row for e in p)
    return hi - lo
if __name__ == '__main__':
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    seen = {normkey(vc): ([], vc)}
    frontier = [([], vc)]
    for dpt in range(depth):
        nf = []
        for g, v in frontier:
            for s in (1, 2, 3, 4, 5, -1, -2, -3, -4, -5):
                w = sigma_vec(s, v); k = normkey(w)
                if k not in seen:
                    seen[k] = ([s] + g, w); nf.append(([s] + g, w))
        frontier = nf
        print('depth', dpt + 1, 'curves so far', len(seen))
    out = []
    for k, (g, v) in seen.items():
        M = Rmat(v)
        out.append((g, Dexact(M), partition(g)))
    from collections import Counter
    print('D(R_s) histogram:', sorted(Counter(d for _, d, _ in out).items()))
    pickle.dump(out, open('curves_d%d.pkl' % depth, 'wb'))
    w24 = [(g, p) for g, d, p in out if d == 24]
    print('well-positioned (D=24):', len(w24))
    for g, p in w24[:40]: print('  ', g, p)
