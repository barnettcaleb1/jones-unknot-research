"""FIXED line census (regression of engineB/template_screen.py; same junctions, same 16 directions, same 49 offsets).
template = s.l1.l1.V.(X1^2)^m.(X3^2)^n.U.u2.u2,  F(m,n) = sum_ab c_ab u^(e_a m + e_b n), u = t^2, e(0,2,4) = (0,1,3).
engineB's possible() returns True / False / 'trivial'; engineB kept only `is True` (offset-specific lines) and skipped
|NZ| <= 1.  Here:
  kind 'offset'  : possible(nz,d) is True  -> engineB's own loop, unchanged (exact fastJ unit test at the representative point)
  kind 'single'  : possible(nz,d) == 'trivial' (all nonzero sectors in ONE equal-slope group) -> F is constant along EVERY
                   line of direction d; each of the 49 offsets is a single-group line; unit test of the group value at the
                   random t:  value in {+-t^k : |k| <= KMAX}  (false positive prob ~1e-12 per test; positives re-checked exactly
                   with fastJ in classify.py)
  kind 'plane'   : |NZ| = 1 (F = c u^(...) on the whole plane); unit iff c in {+-t^k}
Supports Sv (sectors with E_ab V v != 0) and Sw (w E_ab != 0) are recorded for the classification.
usage: census_fixed.py D1 D2 SEED NPROC"""
import sys, random, time, json, pickle
from collections import Counter, defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
import mitm, rho2, sectors
import template_screen as TS          # verbatim engineB definitions: SECT, E, DIRS, GROUPS, OFFS, possible
P = mitm.P
SECT, E, DIRS, GROUPS, OFFS, possible = TS.SECT, TS.E, TS.DIRS, TS.GROUPS, TS.OFFS, TS.possible
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
KMAX = 4000
def setup(D1, D2, seed):
    rnd = random.Random(seed)
    t = rnd.randrange(2, P - 1); u = t * t % P
    S = sectors.setup(t, P)
    Binv, Bm, blocks = S['Binv'], S['B'], S['blocks']
    MT, VT, PHIT = rho2.normalised()
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}]
    V = [[mitm.evt(x, t) for x in VT['l1.l1']]]
    c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
    PH = [[mitm.evt(x, t) * c % P for x in PHIT['u2.u2']]]
    tops = mitm.bfs(Ms, V, D1, 'top'); bots = mitm.bfs(Ms, PH, D2, 'bot')
    def tocoords_v(v): return [sum(Binv[i][j] * v[j] for j in range(9)) % P for i in range(9)]
    def tocoords_w(w): return [sum(w[i] * Bm[i][j] for i in range(9)) % P for j in range(9)]
    bl = [blocks[s] for s in SECT]
    def support(co): return frozenset(SECT[i] for i in range(7) if any(co[k] for k in bl[i]))
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops:
        co = tocoords_v(vecs[0]); TG[mitm.top_class(w)].append((w, co, support(co)))
    for w, vecs in bots:
        co = tocoords_w(vecs[0]); BG[mitm.bot_class(w)].append((w, co, support(co)))
    return t, u, bl, TG, BG, len(tops), len(bots)
def worker(args):
    D1, D2, seed, wid, nproc = args
    import fastJ
    t, u, bl, TG, BG, ntops, nbots = setup(D1, D2, seed)
    R = 160
    upow = {k: pow(u, k % (P - 1), P) for k in range(-4 * R, 4 * R + 1)}
    UNITS = {}
    for k in range(-KMAX, KMAX + 1):
        x = pow(t, k % (P - 1), P); UNITS[x] = k; UNITS[(-x) % P] = k
    maskhist = Counter(); npairs = 0
    poss_cache = {}
    cand_offset = []            # engineB-type candidates (exact test below)
    units = []                  # (kind, wt, wb, d, m0, n0, nz, Sv, Sw)
    planes = []                 # (wt, wb, nz, Sv, Sw, unit?)
    single_lines_tested = Counter(); single_pairs = Counter()
    # distribute top words round-robin over workers (deterministic)
    flat_tops = [(tc, x) for tc, tl in sorted(TG.items()) for x in tl]
    my = defaultdict(list)
    for i, (tc, x) in enumerate(flat_tops):
        if i % nproc == wid: my[tc].append(x)
    t0 = time.time()
    for tc, tl in my.items():
        for bc, blist in BG.items():
            if not mitm.knot_ok(tc, bc): continue
            for wb, om, Sw in blist:
                for wt, be, Sv in tl:
                    cs = []
                    for b in bl:
                        s = 0
                        for k in b: s += om[k] * be[k]
                        cs.append(s % P)
                    nz = frozenset(SECT[i] for i in range(7) if cs[i])
                    maskhist[len(nz)] += 1
                    npairs += 1
                    if len(nz) == 0: continue
                    if len(nz) == 1:
                        cval = next(x for x in cs if x)
                        planes.append(('.'.join(wt), '.'.join(wb), tuple(sorted(nz)), tuple(sorted(Sv)), tuple(sorted(Sw)), cval in UNITS))
                        continue
                    key = nz
                    if key not in poss_cache:
                        pr = {d: possible(nz, d) for d in DIRS}
                        poss_cache[key] = ([d for d in DIRS if pr[d] is True], [d for d in DIRS if pr[d] == 'trivial'])
                    dl, dtriv = poss_cache[key]
                    if not dl and not dtriv: continue
                    cd = dict(zip(SECT, cs))
                    for d in dl:            # engineB's original loop, verbatim logic
                        gs = [[s for s in g if s in nz] for g in GROUPS[d]]
                        gs = [g for g in gs if g]
                        for (m0, n0) in OFFS[d]:
                            vals = []
                            for g in gs:
                                sm = 0
                                for s in g: sm += cd[s] * upow[E[s[0]] * m0 + E[s[1]] * n0]
                                vals.append(sm % P)
                            if sum(1 for x in vals if x) <= 1:
                                cand_offset.append(('.'.join(wt), '.'.join(wb), d, m0, n0, tuple(sorted(nz)), tuple(sorted(Sv)), tuple(sorted(Sw))))
                    for d in dtriv:         # THE FIX: lines of a direction with a single nonzero group
                        single_pairs[d] += 1
                        nzl = list(nz)
                        for (m0, n0) in OFFS[d]:
                            sm = 0
                            for s in nzl: sm += cd[s] * upow[E[s[0]] * m0 + E[s[1]] * n0]
                            sm %= P
                            single_lines_tested[d] += 1
                            if sm in UNITS:
                                units.append(('single', '.'.join(wt), '.'.join(wb), d, m0, n0, tuple(sorted(nz)), tuple(sorted(Sv)), tuple(sorted(Sw))))
    t1 = time.time()
    # exact unit test of engineB-type candidates (exactly as engineB: fastJ at the representative point)
    nonunit_offset = Counter()
    for wt, wb, d, m0, n0, nz, Sv, Sw in cand_offset:
        W = ([x for x in wt.split('.') if x] + (['x1', 'x1'] * m0 if m0 > 0 else ['y1', 'y1'] * (-m0))
             + (['x3', 'x3'] * n0 if n0 > 0 else ['y3', 'y3'] * (-n0)) + [x for x in wb.split('.') if x])
        Jn = fastJ.J('l1.l1', W, 'u2.u2')
        if Jn is not None and len(Jn) == 1:
            units.append(('offset', wt, wb, d, m0, n0, nz, Sv, Sw))
        else: nonunit_offset[d] += 1
    res = {'wid': wid, 'pairs': npairs, 'maskhist': dict(maskhist), 'n_cand_offset': len(cand_offset),
           'nonunit_offset': dict(nonunit_offset), 'single_pairs': dict(single_pairs), 'single_lines_tested': dict(single_lines_tested),
           'time_loop': round(t1 - t0, 1), 'time_exact': round(time.time() - t1, 1), 'ntops': ntops, 'nbots': nbots}
    pickle.dump((res, units, planes), open(OUT + 'census_%d_%d_w%d.pkl' % (D1, D2, wid), 'wb'))
    return res
if __name__ == '__main__':
    import multiprocessing as mp
    D1, D2, seed, nproc = map(int, sys.argv[1:5])
    t0 = time.time()
    with mp.get_context('spawn').Pool(nproc) as pool:
        rs = pool.map(worker, [(D1, D2, seed, w, nproc) for w in range(nproc)])
    print('workers done', round(time.time() - t0, 1), 's', flush=True)
    for r in rs: print(r, flush=True)
