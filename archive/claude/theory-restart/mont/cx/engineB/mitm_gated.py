"""E4b: doubly-gated near misses in the exhaustive width-two screen.  Same top/bottom enumeration as mitm.py; filter
J_raw(zeta_10) in {+-zeta_10^k} (i.e. V_K(zeta_5) a unit root; N2 requires = 1), then exact J (fastJ) and keep a_2 = 0, J != 1.
Records: span, nnz, Phi_10 | J-1, ord_{t+1}(J-1), word.   usage: mitm_gated.py D1 D2 SEED"""
import sys, random, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import mitm, rho2, lp, fastJ, e3_search
from collections import defaultdict, Counter
P = mitm.P
def main(D1, D2, seed):
    rnd = random.Random(seed)
    tg = rnd.randrange(2, P - 1); z10 = mitm.root_of_unity(10)
    MT, VT, PHIT = rho2.normalised()
    ts = [tg, z10]
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()} for t in ts]
    V = [[mitm.evt(x, t) for x in VT['l1.l1']] for t in ts]
    PH = []
    for t in ts:
        c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
        PH.append([mitm.evt(x, t) * c % P for x in PHIT['u2.u2']])
    t0 = time.time()
    tops = mitm.bfs(Ms, V, D1, 'top'); bots = mitm.bfs(Ms, PH, D2, 'bot')
    U10 = set(pow(z10, k, P) for k in range(10))
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops: TG[mitm.top_class(w)].append((w, vecs[1]))
    for w, vecs in bots: BG[mitm.bot_class(w)].append((w, vecs[1]))
    npairs = 0; passers = []
    for tc, tl in TG.items():
        for bc, bl in BG.items():
            if not mitm.knot_ok(tc, bc): continue
            for wb, b in bl:
                for wt, u in tl:
                    s = sum(x * y for x, y in zip(b, u)) % P
                    if s in U10: passers.append((wt, wb))
                npairs += len(tl)
    print('knots', npairs, 'pass zeta10', len(passers), 'time', round(time.time() - t0, 1), flush=True)
    stats = Counter(); recs = {}
    for wt, wb in passers:
        W = list(wt) + list(wb)
        Jn = fastJ.J('l1.l1', W, 'u2.u2')
        if Jn == {0: 1}: stats['J=1'] += 1; continue
        a2 = lp.a2(Jn)
        if a2 != 0: stats['a2!=0'] += 1; continue
        stats['a2=0'] += 1
        key = tuple(sorted(Jn.items()))
        if key in recs: recs[key]['mult'] += 1; continue
        recs[key] = {'word': rho2.halfword('l1.l1', W, 'u2.u2'), 'span': max(Jn) - min(Jn), 'nnz': len(Jn),
                     'zeta10': e3_search.z10(Jn), 'ord_t+1': e3_search.ord1(Jn), 'J': key, 'mult': 1}
    best = sorted(recs.values(), key=lambda r: (r['span'], r['nnz']))
    res = {'D1': D1, 'D2': D2, 'knots': npairs, 'pass_zeta10': len(passers), 'stats': dict(stats), 'distinct_a2zero_J': len(recs),
           'best': best[:60], 'span_hist': dict(Counter(r['span'] for r in recs.values()))}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/mitm_gated_%d_%d.json' % (D1, D2), 'w'))
    print('RESULT', {k: v for k, v in res.items() if k not in ('best',)}, flush=True)
    for r in best[:10]: print(r['span'], r['nnz'], r['zeta10'], r['ord_t+1'], r['mult'], r['word'], r['J'])
if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
