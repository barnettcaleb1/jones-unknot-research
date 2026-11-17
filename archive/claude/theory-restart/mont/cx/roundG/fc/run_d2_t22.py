"""DEPTH-TWO nests (size bound stated in REPORT section 4):
 S1 (literal F-C, k = 1): Y^N' c, c = F_m(Y^N P) any UNIMODULAR depth-one body of the library (all n, |N| <= 4, 1 <= |m| <= 7),
    N' in +-1..+-4  (Y^N' preserves the ideal: all unimodular; N' = 0 is the depth-one orbit itself).
 S2 (two children): Y^N' (c1 c2), c_i = F_m(Y^N u u') UNIMODULAR depth-one bodies with u, u' in R(5) (n = 2), |N| <= 1,
    1 <= |m| <= 3; all unordered pairs (c1 = c2 allowed), N' in {-1, 0, 1}.
 Per body: exact eigenpair, candidates, unit test, Delta (= span f_m) and D = H - tau0 - tauinf.  Ideal test (pair criterion
 (a1,b2) = (b1,a2) = Lambda, PROVED) on every S2 body with min Delta <= 12 and on a uniform sample; units are recorded at once."""
import sys, pickle, time, collections, random, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundG/fc')
import fc_core as fc
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import lib, vc
from multiprocessing import Pool
R5 = lib.rational(5)
d1 = pickle.load(open('d1.pkl', 'rb'))['res']
UNI = sorted({(idx, N) for idx, N, uni, kappa, *_ in d1 if uni and kappa is not None})
def child(idx, N, m):
    p = vc.starall([R5[i][1] for i in idx])
    if N: p = vc.Ypow(N, p)
    v = vc.F(m, p)
    T = ('n', m, [R5[i][2] for i in idx] + ([('w', ('Y' if N > 0 else 'y') * abs(N))] if N else []))
    return fc.chan_from_vc(v), T
S1C = [(idx, N, m) for idx, N in UNI for m in range(-7, 8) if m]
S2C = [(idx, N, m) for idx, N in UNI if len(idx) == 2 and abs(N) <= 1 for m in (-3, -2, -1, 1, 2, 3)]
CH1 = None; CH2 = None
def init():
    global CH1, CH2
    CH2 = [child(*x)[0] for x in S2C]
def rec(a, b, Np):
    a_, c = fc.state_from_channel(a, fc.shift(b, -3 * Np))
    A, B = fc.eigen(a_, c)
    if not B[1]: return None
    return fc.analyze(A, B)
def work1(chunk):
    out = []; hist = collections.Counter(); units = []
    for x in chunk:
        (a, b), T = child(*x)
        for Np in (-4, -3, -2, -1, 1, 2, 3, 4):
            r = rec(a, b, Np)
            if r is None: continue
            kappa, H, cands = r
            for c_ in cands:
                m, unit, sf, tau0, tauinf, r0, rinf, Dd, Delta = c_
                if sf is None: continue
                hist[(min(sf, 40), kappa == 0)] += 1
                if unit: units.append((x, Np, c_))
                if sf <= 12: out.append((sf, Dd, kappa, H, tau0, tauinf, x, Np, m))
    return out, hist, units
def work2(rows):
    out = []; hist = collections.Counter(); units = []; samp = []
    rng = random.Random(rows[0])
    for i in rows:
        a1, b1 = CH2[i]
        for j in range(i, len(CH2)):
            a2, b2 = CH2[j]
            a = fc.mul(a1, a2); b = fc.mul(b1, b2)
            best = None
            for Np in (-1, 0, 1):
                r = rec(a, b, Np)
                if r is None: continue
                kappa, H, cands = r
                for c_ in cands:
                    m, unit, sf, tau0, tauinf, r0, rinf, Dd, Delta = c_
                    if sf is None: continue
                    hist[(min(sf, 40), kappa == 0)] += 1
                    if unit: units.append((i, j, Np, c_))
                    if sf <= 22: out.append((sf, Dd, kappa, H, tau0, tauinf, i, j, Np, m))
                    if rng.random() < 0.002: samp.append((sf, Dd, kappa, H, tau0, tauinf, i, j, Np, m))
    return out, hist, units, samp
if __name__ == '__main__':
    t0 = time.time()
    print('unimodular depth-one orbits', len(UNI), 'S1 children', len(S1C), 'S2 children', len(S2C), flush=True)
    with Pool(9, initializer=init) as P:
        res1 = [([], collections.Counter(), [])]
        out1 = []; h1 = collections.Counter(); u1 = []
        for o, h, u in res1: out1 += o; h1.update(h); u1 += u
        print('S1 done: bodies %d, candidates %d, units %d, Delta<=12 records %d, time %.1f' % (len(S1C) * 8, sum(h1.values()), len(u1), len(out1), time.time() - t0), flush=True)
        pickle.dump({'S1C': S1C, 'out': out1, 'hist': h1, 'units': u1}, open('d2_S1.pkl', 'wb'))
        n = len(S2C); rows = list(range(n))
        # balance: row i has n - i pairs
        chunks = [rows[k::360] for k in range(360)]
        out2 = []; h2 = collections.Counter(); u2 = []; s2 = []; done = 0
        for o, h, u, s in P.imap_unordered(work2, chunks):
            out2 += o; h2.update(h); u2 += u; s2 += s; done += 1
            if u: print('UNIT EVENT', u[:3], flush=True)
            if done % 60 == 0: print('  S2 chunks', done, '/360, time %.1f' % (time.time() - t0), flush=True)
        print('S2 done: pairs %d, bodies %d, candidates %d, units %d, Delta<=12 records %d, sample %d, time %.1f' % (
            n * (n + 1) // 2, 3 * n * (n + 1) // 2, sum(h2.values()), len(u2), len(out2), len(s2), time.time() - t0), flush=True)
        pickle.dump({'S2C': S2C, 'out': out2, 'hist': h2, 'units': u2, 'sample': s2}, open('d2_S3.pkl', 'wb'))
    print('saved', flush=True)
