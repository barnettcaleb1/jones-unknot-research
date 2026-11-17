"""E3c: guided extreme-term search at WIDTH THREE (rho_3, dim 51): annealing over s.l1.l1.l1.W.u2.u2.u2, |W| = n,
objective span(J) + 3 min(|a_2|,10); logs a_2 = 0 configurations with gates (zeta_10, ord_{t+1}); HIT protocol as E3.
usage: e3w3.py N SECONDS SEED"""
import sys, random, time, json, math
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/')   # u45: the patched e3_search (z10, ord1 unchanged)
import fastJ3, lp, kcert
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/')
import e3_search
assert e3_search.__file__.startswith('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/')

# ---- u45 patch: store every J = 1 word (kcert once per distinct word, cached) ----
U45_OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u45/e3/out'
J1 = {}
def KC(hw, where, ev):
    e = J1.get(hw)
    if e is None:
        st, why = kcert.certify(hw)
        e = J1[hw] = {'count': 0, 'first_eval': ev, 'where': where, 'kcert': [st, why]}
        if st != 'V=1,Delta=1':
            print('KCERT-SAYS-NONTRIVIAL', where, hw, why, flush=True)
            open(U45_OUT + '/KCERT_NONTRIVIAL_J1.txt', 'a').write(hw + '\t' + where + '\t' + str(why) + '\n')
    e['count'] += 1
    return tuple(e['kcert'])
def BUDGET_OK(evals, restarts=None):
    if MAXE is None: return True
    if evals < MAXE: return True
    return restarts is not None and restarts < MAXR
MAXE = None; MAXR = 0
LET = fastJ3.LET
def inv(L): return ('y' if L[0] == 'x' else 'x') + L[1:]
def ok(W):
    if any(inv(W[i]) == W[i + 1] for i in range(len(W) - 1)): return False
    return fastJ3.is_knot(W)
def main(n, secs, seed, cap=None):
    rnd = random.Random(seed); t_end = time.time() + (cap if cap else secs); tw0 = time.time()
    best = {}; evals = 0; hits = []
    while time.time() < t_end and BUDGET_OK(evals):
        while True:
            W = [rnd.choice(LET) for _ in range(n)]
            if ok(W): break
        J = fastJ3.J(W)
        if J == {0: 1}: KC(fastJ3.halfword(W), 'init', evals)
        if J is None or J == {0: 1}: continue
        cur = (max(J) - min(J)) + 3 * min(abs(lp.a2(J)), 10)
        steps = 2000
        for s in range(steps):
            if time.time() > t_end or not BUDGET_OK(evals): break
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
                hw = fastJ3.halfword(W2); st, why = KC(hw, 'inner', evals)
                if st != 'V=1,Delta=1':
                    hits.append(hw); print('HIT-CANDIDATE', hw, why, flush=True)
                    open(U45_OUT + '/HIT_CANDIDATES.txt', 'a').write(hw + '\tw3 ' + str(why) + '\n')
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
           'gated': [r for r in recs if r['zeta10']][:40],
           'u45': {'max_evals': MAXE, 'cap': cap, 'wall': round(time.time() - tw0, 1), 'budget_reached': not BUDGET_OK(evals), 'n_j1_distinct': len(J1), 'n_j1_probes': sum(e['count'] for e in J1.values())},
           'j1_words': J1}
    json.dump(res, open(U45_OUT + '/e3w3_n%d_s%d.json' % (n, seed), 'w'))
    print('RESULT n', n, 'evals', evals, 'distinct a2=0 J', len(best), 'best spans', [r['span'] for r in recs[:10]],
          'gated spans', [r['span'] for r in recs if r['zeta10']][:10], 'hits', len(hits), flush=True)
if __name__ == '__main__':
    if len(sys.argv) > 4: MAXE = int(sys.argv[4])
    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), cap=(float(sys.argv[5]) if len(sys.argv) > 5 else None))
