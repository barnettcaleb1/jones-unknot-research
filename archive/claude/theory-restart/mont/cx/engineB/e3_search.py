"""E3 / E3b: guided extreme-term search (simulated annealing) over width-two words s.l1.l1.W.u2.u2 of fixed length n,
minimising f = span(J) + 3 min(|a_2|, 10)  (J != 1 implies K nontrivial; J = 1 & K unknot is rejected; J = 1 & K nontrivial = HIT).
Logs the best a_2 = 0 configurations with gates: zeta10 (Phi_10 | J - 1), ord_{t+1}(J - 1), nnz.
usage: e3_search.py N SECONDS SEED"""
import sys, random, time, json, math
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import fastJ, rho2, lp, kcert, vspan
REL = False   # E3b: objective span(J) - span(V_K) (relative flatness)
LET = fastJ.LET
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
def ok(W):
    if any(INV[W[i]] == W[i + 1] for i in range(len(W) - 1)): return False
    return rho2.is_knot('l1.l1', W, 'u2.u2')
def ord1(J):
    """(t+1)-adic order of J - 1"""
    d = dict(J); d[0] = d.get(0, 0) - 1
    d = {e: c for e, c in d.items() if c}
    k = 0
    while d:
        try: d = rho2.tdiv_1pt(d, 1)
        except ArithmeticError: break
        k += 1
        if k > 40: break
    return k
def z10(J):
    # Phi_10 | J - 1  <=>  J(zeta_10) = 1 ; test by reduction mod t^4 - t^3 + t^2 - t + 1
    d = dict(J); d[0] = d.get(0, 0) - 1
    lo = min(d) if d else 0
    poly = [0] * (max(d) - lo + 1) if d else [0]
    for e, c in d.items(): poly[e - lo] += c
    # multiply by t^-lo is a unit; reduce poly mod Phi_10 (monic, deg 4)
    phi = [1, -1, 1, -1, 1]   # coefficients t^0..t^4
    p = poly[:]
    for i in range(len(p) - 1, 3, -1):
        c = p[i]
        if c:
            # t^4 = t^3 - t^2 + t - 1
            p[i] = 0
            p[i - 1] += c; p[i - 2] -= c; p[i - 3] += c; p[i - 4] -= c
    return all(x == 0 for x in p[:4])
def evaluate(W):
    Jn = fastJ.J('l1.l1', W, 'u2.u2')
    if Jn is None: return None
    a2 = lp.a2(Jn)
    return Jn, a2
def score(Jn, a2, W=None):
    if Jn == {0: 1}: return None
    s = (max(Jn) - min(Jn)) + 3 * min(abs(a2), 10)
    if REL and W is not None:
        vs = vspan.vspan(rho2.halfword('l1.l1', W, 'u2.u2'))
        if vs is None: return None
        s -= vs
    return s
def main(n, secs, seed):
    rnd = random.Random(seed)
    t_end = time.time() + secs
    best = {}      # key (J tuple) -> record, for a2 = 0
    bestany = None; evals = 0; hits = []; restarts = 0
    while time.time() < t_end:
        while True:
            W = [rnd.choice(LET) for _ in range(n)]
            if ok(W): break
        r = evaluate(W); cur = score(r[0], r[1], W) if r else None
        if cur is None: continue
        T0 = 4.0; steps = 3000; restarts += 1
        for s in range(steps):
            if time.time() > t_end: break
            T = T0 * (0.05 / T0) ** (s / steps)
            W2 = W[:]
            mv = rnd.random()
            if mv < 0.5: W2[rnd.randrange(n)] = rnd.choice(LET)
            elif mv < 0.75:
                i = rnd.randrange(n - 1); W2[i], W2[i + 1] = W2[i + 1], W2[i]
            else:
                i = rnd.randrange(n); del W2[i]; W2.insert(rnd.randrange(n), rnd.choice(LET))
            if not ok(W2): continue
            r = evaluate(W2); evals += 1
            if r is None: continue
            Jn, a2 = r
            if Jn == {0: 1}:
                hw = rho2.halfword('l1.l1', W2, 'u2.u2')
                st, why = kcert.certify(hw)
                if st != 'V=1,Delta=1':
                    hits.append(hw); print('HIT-CANDIDATE', hw, why, flush=True)
                    open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/HIT_CANDIDATES.txt', 'a').write(hw + '\t' + str(why) + '\n')
                continue
            f = score(Jn, a2, W2)
            if f is None: continue
            if a2 == 0:
                key = tuple(sorted(Jn.items()))
                if key not in best:
                    best[key] = {'word': rho2.halfword('l1.l1', W2, 'u2.u2'), 'span': max(Jn) - min(Jn), 'nnz': len(Jn), 'f': f,
                                 'zeta10': z10(Jn), 'ord_t+1': ord1(Jn), 'J': key}
            if bestany is None or f < bestany[0]: bestany = (f, rho2.halfword('l1.l1', W2, 'u2.u2'), a2)
            if f <= cur or rnd.random() < math.exp(-(f - cur) / T):
                W, cur = W2, f
    recs = sorted(best.values(), key=lambda r: ((r['f'], r['span']) if REL else (r['span'], r['nnz'])))
    res = {'n': n, 'secs': secs, 'seed': seed, 'evals': evals, 'restarts': restarts, 'distinct_a2zero_J': len(best),
           'best_any': bestany, 'hits': hits, 'top_a2zero': recs[:40]}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/e3%s_n%d_s%d.json' % ('b' if REL else '', n, seed), 'w'))
    print('RESULT n', n, 'evals', evals, 'distinct a2=0 J', len(best), 'best a2=0 (f,span)', [(r['f'], r['span']) for r in recs[:10]], 'hits', len(hits), flush=True)
if __name__ == '__main__':
    if len(sys.argv) > 4 and sys.argv[4] == 'rel': REL = True
    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
