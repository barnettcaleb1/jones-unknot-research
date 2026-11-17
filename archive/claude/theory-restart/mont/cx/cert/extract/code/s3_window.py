"""S3a regeneration: reproduces engineB/template_window.py D1 D2 R (= 4 4 6): every junction (V,U) of the (D1,D2) enumeration
with the double twist site X1^{2m} X3^{2n} inserted, |m|,|n| <= R; J_raw(m,n) = sum c_ab u^(e_a m + e_b n) at t = zeta_7
(joint eigenbasis, engineB/sectors.py); zeta_7 unit filter; survivors -> exact J (engineB/fastJ.py); keep J = 1.
usage: s3_window.py D1 D2 R SEED NPROC"""
import sys, random, time, json, multiprocessing as mp
from collections import defaultdict, Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import mitm, rho2, sectors, fastJ
P = mitm.P
SECT = [(0, 0), (0, 2), (2, 0), (2, 2), (2, 4), (4, 2), (4, 4)]
E = {0: 0, 2: 1, 4: 3}
G = {}
def twist(m, n):
    return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def setup(D1, D2, R, seed):
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
    tops = mitm.bfs(Ms, V, D1, 'top'); bots = mitm.bfs(Ms, PH, D2, 'bot')
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops: TG[mitm.top_class(w)].append((w, [sum(Binv[i][j] * vecs[1][j] for j in range(9)) % P for i in range(9)]))
    for w, vecs in bots: BG[mitm.bot_class(w)].append((w, [sum(vecs[1][i] * Bm[i][j] for i in range(9)) % P for j in range(9)]))
    u = z7 * z7 % P
    pts = [(m, n) for m in range(-R, R + 1) for n in range(-R, R + 1)]
    G.update(dict(TG=TG, BG=BG, bl=[blocks[s] for s in SECT], pts=pts,
                  pw=[[pow(u, (E[s[0]] * m + E[s[1]] * n) % (P - 1), P) for s in SECT] for (m, n) in pts],
                  U7=set(pow(z7, k, P) for k in range(7)) | set((-pow(z7, k, P)) % P for k in range(7))))
def job(bc):
    TG, BG, bl, pts, pw, U7 = G['TG'], G['BG'], G['bl'], G['pts'], G['pw'], G['U7']
    nfam = 0; npts = 0; surv = []
    for tc, tl in TG.items():
        if not mitm.knot_ok(tc, bc): continue
        for wb, om in BG[bc]:
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
                    if val in U7: surv.append(('.'.join(wt), '.'.join(wb), pts[idx]))
                npts += len(pw)
    return nfam, npts, surv
def exact(item):
    wt, wb, (m, n) = item
    W = [x for x in wt.split('.') if x] + twist(m, n) + [x for x in wb.split('.') if x]
    J = fastJ.J('l1.l1', W, 'u2.u2')
    return item, J == {0: 1}
if __name__ == '__main__':
    D1, D2, R, seed, nproc = map(int, sys.argv[1:6])
    t0 = time.time(); setup(D1, D2, R, seed)
    ctx = mp.get_context('fork')
    with ctx.Pool(nproc) as pool:
        res = pool.map(job, list(G['BG']))
        nfam = sum(r[0] for r in res); npts = sum(r[1] for r in res); surv = [s for r in res for s in r[2]]
        print('families', nfam, 'points', npts, 'zeta7 survivors', len(surv), 'time', round(time.time() - t0, 1), flush=True)
        ex = pool.map(exact, surv, chunksize=500)
    J1 = [it for it, ok in ex if ok]
    print('J = 1:', len(J1), ' J != 1 (zeta7 unit):', len(ex) - len(J1), 'time', round(time.time() - t0, 1), flush=True)
    json.dump({'D1': D1, 'D2': D2, 'R': R, 'families': nfam, 'points': npts, 'zeta7_survivors': len(surv), 'J1': J1},
              open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s3_window_%d_%d_R%d.json' % (D1, D2, R), 'w'))
