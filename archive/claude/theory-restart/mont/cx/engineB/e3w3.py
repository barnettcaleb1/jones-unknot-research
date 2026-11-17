"""E3c: guided extreme-term search at WIDTH THREE (rho_3, dim 51): annealing over s.l1.l1.l1.W.u2.u2.u2, |W| = n,
objective span(J) + 3 min(|a_2|,10); logs a_2 = 0 configurations with gates (zeta_10, ord_{t+1}); HIT protocol as E3.
usage: e3w3.py N SECONDS SEED"""
import sys, random, time, json, math
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import fastJ3, lp, kcert, e3_search
LET = fastJ3.LET
def inv(L): return ('y' if L[0] == 'x' else 'x') + L[1:]
def ok(W):
    if any(inv(W[i]) == W[i + 1] for i in range(len(W) - 1)): return False
    return fastJ3.is_knot(W)
def main(n, secs, seed):
    rnd = random.Random(seed); t_end = time.time() + secs
    best = {}; evals = 0; hits = []
    while time.time() < t_end:
        while True:
            W = [rnd.choice(LET) for _ in range(n)]
            if ok(W): break
        J = fastJ3.J(W)
        if J is None or J == {0: 1}: continue
        cur = (max(J) - min(J)) + 3 * min(abs(lp.a2(J)), 10)
        steps = 2000
        for s in range(steps):
            if time.time() > t_end: break
            T = 4.0 * (0.05 / 4.0) ** (s / steps)
            W2 = W[:]; mv = rnd.random()
            if mv < 0.5: W2[rnd.randrange(n)] = rnd.choice(LET)
            elif mv < 0.75:
                i = rnd.randrange(n - 1); W2[i], W2[i + 1] = W2[i + 1], W2[i]
            else:
                i = rnd.randrange(n); del W2[i]; W2.insert(rnd.randrange(n), rnd.choice(LET))
            if not ok(W2): continue
            Jn = fastJ3.J(W2); evals += 1
            if Jn is None: continue
            if Jn == {0: 1}:
                hw = fastJ3.halfword(W2); st, why = kcert.certify(hw)
                if st != 'V=1,Delta=1':
                    hits.append(hw); print('HIT-CANDIDATE', hw, why, flush=True)
                    open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/HIT_CANDIDATES.txt', 'a').write(hw + '\tw3 ' + str(why) + '\n')
                continue
            a2 = lp.a2(Jn)
            f = (max(Jn) - min(Jn)) + 3 * min(abs(a2), 10)
            if a2 == 0:
                key = tuple(sorted(Jn.items()))
                if key not in best:
                    best[key] = {'word': fastJ3.halfword(W2), 'span': max(Jn) - min(Jn), 'nnz': len(Jn),
                                 'zeta10': e3_search.z10(Jn), 'ord_t+1': e3_search.ord1(Jn), 'J': key}
            if f <= cur or rnd.random() < math.exp(-(f - cur) / T): W, cur = W2, f
    recs = sorted(best.values(), key=lambda r: (r['span'], r['nnz']))
    res = {'n': n, 'evals': evals, 'distinct_a2zero_J': len(best), 'hits': hits, 'top_a2zero': recs[:40],
           'gated': [r for r in recs if r['zeta10']][:40]}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/e3w3_n%d_s%d.json' % (n, seed), 'w'))
    print('RESULT n', n, 'evals', evals, 'distinct a2=0 J', len(best), 'best spans', [r['span'] for r in recs[:10]],
          'gated spans', [r['span'] for r in recs if r['zeta10']][:10], 'hits', len(hits), flush=True)
if __name__ == '__main__':
    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
