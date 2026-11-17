"""Window screen of the two-parameter twist families s.l1.l1.V.(X1^2)^m.(X3^2)^n.U.u2.u2 for |m|,|n| <= R at EVERY junction
(V,U) of the (D1,D2) enumeration: J_raw(m,n) = sum_ab c_ab u^(e_a m + e_b n) evaluated at t = zeta_7 (c_ab from the joint
eigenbasis at zeta_7); unit filter +-zeta_7^k; survivors recomputed exactly (fastJ) and K certified (kcert).
usage: template_window.py D1 D2 R SEED"""
import sys, random, time, json
from collections import defaultdict, Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import mitm, rho2, sectors, fastJ, kcert
P = mitm.P
SECT = [(0, 0), (0, 2), (2, 0), (2, 2), (2, 4), (4, 2), (4, 4)]
E = {0: 0, 2: 1, 4: 3}
def main(D1, D2, R, seed):
    rnd = random.Random(seed)
    tg = rnd.randrange(2, P - 1); z7 = mitm.root_of_unity(7)
    MT, VT, PHIT = rho2.normalised()
    ts = [tg, z7]
    Ms = [{L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()} for t in ts]
    V = [[mitm.evt(x, t) for x in VT['l1.l1']] for t in ts]
    PH = []
    for t in ts:
        c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
        PH.append([mitm.evt(x, t) * c % P for x in PHIT['u2.u2']])
    S = sectors.setup(z7, P)
    Binv, Bm, blocks = S['Binv'], S['B'], S['blocks']
    bl = [blocks[s] for s in SECT]
    u = z7 * z7 % P
    U7 = set(pow(z7, k, P) for k in range(7)) | set((-pow(z7, k, P)) % P for k in range(7))
    t0 = time.time()
    tops = mitm.bfs(Ms, V, D1, 'top'); bots = mitm.bfs(Ms, PH, D2, 'bot')
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops: TG[mitm.top_class(w)].append((w, [sum(Binv[i][j] * vecs[1][j] for j in range(9)) % P for i in range(9)]))
    for w, vecs in bots: BG[mitm.bot_class(w)].append((w, [sum(vecs[1][i] * Bm[i][j] for i in range(9)) % P for j in range(9)]))
    # exponent table: for each (m,n) the 7 powers
    pts = [(m, n) for m in range(-R, R + 1) for n in range(-R, R + 1)]
    pw = [[pow(u, (E[s[0]] * m + E[s[1]] * n) % (P - 1), P) for s in SECT] for (m, n) in pts]
    nfam = 0; npts = 0; surv = []
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
                    nfam += 1
                    c0, c1, c2, c3, c4, c5, c6 = cs
                    for idx, p in enumerate(pw):
                        val = (c0 * p[0] + c1 * p[1] + c2 * p[2] + c3 * p[3] + c4 * p[4] + c5 * p[5] + c6 * p[6]) % P
                        if val in U7: surv.append((wt, wb, pts[idx]))
                    npts += len(pw)
    print('families', nfam, 'points', npts, 'zeta7 survivors', len(surv), 'time', round(time.time() - t0, 1), flush=True)
    stats = Counter(); near = []
    for wt, wb, (m, n) in surv:
        W = list(wt) + (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n)) + list(wb)
        J = fastJ.J('l1.l1', W, 'u2.u2')
        hw = rho2.halfword('l1.l1', W, 'u2.u2')
        if J == {0: 1}:
            st, why = kcert.certify(hw)
            if st == 'V=1,Delta=1': stats['J=1, presumed unknot'] += 1
            else:
                stats['HIT'] += 1; print('HIT-CANDIDATE', hw, why, flush=True)
                open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/HIT_CANDIDATES.txt', 'a').write(hw + '\twindow ' + str(why) + '\n')
        else:
            stats['J!=1 (zeta7 unit)'] += 1
            if len(near) < 50: near.append((hw, sorted(J.items())))
    res = {'D1': D1, 'D2': D2, 'R': R, 'families': nfam, 'points': npts, 'survivors': len(surv), 'stats': dict(stats), 'zeta7_nonunit_examples': near}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/window_%d_%d_R%d.json' % (D1, D2, R), 'w'))
    print('RESULT', {k: v for k, v in res.items() if k != 'zeta7_nonunit_examples'}, flush=True)
if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
