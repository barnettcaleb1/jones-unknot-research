"""Two-site template screen (Codex WIDTH2-FLAT-LINES) over ALL width-two junctions:
template = s.l1.l1.V.(X1^2)^m.(X3^2)^n.U.u2.u2 with V = top word (|V| <= D1), U = bottom word (|U| <= D2), full twists on the leg
pairs (0,1) and (2,3) inserted at the junction.  J_raw(m,n) = sum_ab c_ab u^(e_a m + e_b n), u = t^2, e(0,2,4) = (0,1,3),
c_ab = w_U E_ab u_V.  Rank-one sectors (00,02,20,24,42) factor as (w side)(v side): no accidental zeros there; only c22, c44
(rank two) can vanish accidentally.  An infinite unit line in direction d needs all but one equal-slope group to vanish
identically (Codex theorem); we enumerate NZ patterns and test the offset identities mod p at a generic t, then exactly.
usage: template_screen.py D1 D2 SEED"""
import sys, random, time, json
from collections import Counter, defaultdict
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
import mitm, rho2, sectors
P = mitm.P
SECT = [(0, 0), (0, 2), (2, 0), (2, 2), (2, 4), (4, 2), (4, 4)]
E = {0: 0, 2: 1, 4: 3}
DIRS = [(1, 1), (1, -1), (1, -3), (1, -2), (2, -3), (2, -1), (3, -2), (3, -1), (1, 0), (0, 1), (1, 2), (1, 3), (2, 1), (3, 1), (2, 3), (3, 2)]
def groups_for(d):
    p, q = d; g = defaultdict(list)
    for s in SECT: g[E[s[0]] * p + E[s[1]] * q].append(s)
    return list(g.values())
GROUPS = {d: groups_for(d) for d in DIRS}
def _egcd(a, b):
    if b == 0: return (a, 1, 0)
    g, x, y = _egcd(b, a % b); return (g, y, x - (a // b) * y)
def offsets(d, R=24):
    p, q = d
    g, x, y = _egcd(q, -p) if p or q else (1, 0, 0)
    # q*m0 - p*n0 = r : (m0, n0) = r*(x, y)/g  with q*x + (-p)*y = g
    pts = []
    for r in range(-R, R + 1):
        if r % abs(g): continue
        k = r // g
        pts.append((k * x, k * y))
    return pts
OFFS = {d: offsets(d) for d in DIRS}
def possible(mask_nz, d):
    """can a unit line in direction d exist given the set of nonzero sectors (ignoring offsets)?"""
    gs = [[s for s in g if s in mask_nz] for g in GROUPS[d]]
    gs = [g for g in gs if g]
    singles = [g for g in gs if len(g) == 1]
    if len(gs) <= 1: return 'trivial'      # at most one nonzero group: every line is J(0,0)-like
    if len(singles) >= 2: return False
    return True
def main(D1, D2, seed, R=40):
    rnd = random.Random(seed)
    t = rnd.randrange(2, P - 1); u = t * t % P
    S = sectors.setup(t, P)
    Binv, Bm, blocks = S['Binv'], S['B'], S['blocks']
    MT, VT, PHIT = rho2.normalised()
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}]
    V = [[mitm.evt(x, t) for x in VT['l1.l1']]]
    c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
    PH = [[mitm.evt(x, t) * c % P for x in PHIT['u2.u2']]]
    t0 = time.time()
    tops = mitm.bfs(Ms, V, D1, 'top'); bots = mitm.bfs(Ms, PH, D2, 'bot')
    def tocoords_v(v): return [sum(Binv[i][j] * v[j] for j in range(9)) % P for i in range(9)]
    def tocoords_w(w): return [sum(w[i] * Bm[i][j] for i in range(9)) % P for j in range(9)]
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops: TG[mitm.top_class(w)].append((w, tocoords_v(vecs[0])))
    for w, vecs in bots: BG[mitm.bot_class(w)].append((w, tocoords_w(vecs[0])))
    bl = [blocks[s] for s in SECT]
    maskhist = Counter(); cands = []; npairs = 0
    poss_cache = {}
    upow = {k: pow(u, k % (P - 1), P) for k in range(-4 * R, 4 * R + 1)}
    for tc, tl in TG.items():
        for bc, blist in BG.items():
            if not mitm.knot_ok(tc, bc): continue
            for wb, om in blist:
                for wt, be in tl:
                    cs = []
                    for b in bl:
                        s = 0
                        for k in b: s += om[k] * be[k]
                        cs.append(s % P)
                    nz = frozenset(SECT[i] for i in range(7) if cs[i])
                    maskhist[len(nz)] += 1
                    npairs += 1
                    if len(nz) <= 1: continue
                    key = nz
                    if key not in poss_cache: poss_cache[key] = [d for d in DIRS if possible(nz, d) is True]
                    dl = poss_cache[key]
                    if not dl: continue
                    cd = dict(zip(SECT, cs))
                    for d in dl:
                        gs = [[s for s in g if s in nz] for g in GROUPS[d]]
                        gs = [g for g in gs if g]
                        for (m0, n0) in OFFS[d]:
                            vals = []
                            for g in gs:
                                sm = 0
                                for s in g: sm += cd[s] * upow[E[s[0]] * m0 + E[s[1]] * n0]
                                vals.append(sm % P)
                            if sum(1 for x in vals if x) <= 1:
                                cands.append(('.'.join(wt), '.'.join(wb), d, m0, n0, sorted(nz)))
    # exact unit test of each candidate line at its representative point
    import fastJ, kcert
    verdict = Counter(); kept = []
    for wt, wb, d, m0, n0, nz in cands:
        W = ([x for x in wt.split('.') if x] + (['x1', 'x1'] * m0 if m0 > 0 else ['y1', 'y1'] * (-m0))
             + (['x3', 'x3'] * n0 if n0 > 0 else ['y3', 'y3'] * (-n0)) + [x for x in wb.split('.') if x])
        Jn = fastJ.J('l1.l1', W, 'u2.u2')
        unit = Jn is not None and len(Jn) == 1
        if not unit: verdict['surviving group not a unit'] += 1; continue
        # J is then a unit on the WHOLE line; certify the knots at 5 points of the line
        Vw = [x for x in wt.split('.') if x]; Uw = [x for x in wb.split('.') if x]
        sts = []
        for k in range(-2, 3):
            m, n = m0 + k * d[0], n0 + k * d[1]
            Wk = Vw + (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n)) + Uw
            hwk = rho2.halfword('l1.l1', Wk, 'u2.u2')
            stk, whyk = kcert.certify(hwk)
            sts.append(stk)
            if stk != 'V=1,Delta=1':
                Jk = fastJ.J('l1.l1', Wk, 'u2.u2')
                print('HIT-LINE', hwk, d, whyk, Jk, flush=True)
                open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/orig_HIT_CANDIDATES.txt', 'a').write(hwk + '\tunit-line ' + str(whyk) + ' J=' + str(Jk) + '\n')
        st = 'all 5 points V=1,Delta=1' if all(s == 'V=1,Delta=1' for s in sts) else 'NONTRIVIAL POINT'
        verdict['UNIT LINE, ' + st] += 1
        kept.append((rho2.halfword('l1.l1', W, 'u2.u2'), d, m0, n0, nz, st))
    res = {'D1': D1, 'D2': D2, 'pairs': npairs, 'nz_count_hist': dict(maskhist), 'ncand': len(cands), 'verdict': dict(verdict), 'unit_lines': kept[:300]}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/orig_template_%d_%d.json' % (D1, D2), 'w'), default=str)
    print('RESULT pairs', npairs, 'hist |NZ|', dict(maskhist), 'single-group lines', len(cands), 'verdict', dict(verdict), 'time', round(time.time() - t0, 1), flush=True)
    for x in kept[:10]: print(x)
if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
