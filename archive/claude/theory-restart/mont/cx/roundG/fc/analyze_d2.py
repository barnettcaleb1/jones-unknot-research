"""Analysis of d2_S1.pkl / d2_S2.pkl (+ d2_S3.pkl if present): deficit distributions, ideal tests (pair criterion) on the S2/S3
low tail and on the uniform sample, smallest positive deficits with full eigenpairs and half-words."""
import sys, pickle, collections, random, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundG/fc')
import fc_core as fc
import run_d2 as R
from multiprocessing import Pool
import vc, lp
t0 = time.time()
def chan_child(x): return R.child(*x)
def body_S1(x, Np):
    (a, b), T = R.child(*x)
    a_, c = fc.state_from_channel(a, fc.shift(b, -3 * Np))
    A, B = fc.eigen(a_, c)
    Tb = ('p', [T, ('w', ('Y' if Np > 0 else 'y') * abs(Np))])
    return a_, c, A, B, Tb
def body_S2(C, i, j, Np):
    (a1, b1), T1 = R.child(*C[i]); (a2, b2), T2 = R.child(*C[j])
    a = fc.mul(a1, a2); b = fc.shift(fc.mul(b1, b2), -3 * Np)
    a_, c = fc.state_from_channel(a, b)
    A, B = fc.eigen(a_, c)
    kids = [T1, T2] + ([('w', ('Y' if Np > 0 else 'y') * abs(Np))] if Np else [])
    return a_, c, A, B, ('p', kids)
def pair_uni(args):
    C, i, j = args
    (a1, b1), _ = R.child(*C[i]); (a2, b2), _ = R.child(*C[j])
    s1, _ = fc.ideal_test(a1, b2); s2, _ = fc.ideal_test(b1, a2)
    return (i, j, s1 == 'UNIT' and s2 == 'UNIT')
def hw_closure(Tb, m):
    kids = Tb[1]
    return vc.hw(('n', m, kids))
def show(tag, rows, getbody, k=10):
    seen = set(); cnt = 0; lines = []
    for r in rows:
        a_, c, A, B, Tb = getbody(r)
        key = fc.okey(A, B)
        if key in seen: continue
        seen.add(key); cnt += 1
        sf, Dd, kappa, H, tau0, tauinf = r[:6]; m = r[-1]
        w = hw_closure(Tb, m)
        J = lp.J(w) if len(w) < 400 else None
        Jspan = (max(J) - min(J)) if J else None
        lines.append('  %s Delta=%d D=%d kappa=%d H=%d tau=(%d,%d) m=%d  span(lp.J)=%s\n     hw=%s\n     A=%s\n     B=%s' % (
            tag, sf, Dd, kappa, H, tau0, tauinf, m, Jspan, w, sorted(fc.todict(A).items()), sorted(fc.todict(B).items())))
        if cnt >= k: break
    return lines
if __name__ == '__main__':
    s1 = pickle.load(open('d2_S1.pkl', 'rb'))
    h = s1['hist']
    hu = collections.Counter(); hk0 = collections.Counter()
    for (sf, k0), v in h.items():
        hu[sf] += v
        if k0: hk0[sf] += v
    print('S1 (Y^N\' c, single child, all UNIMODULAR): bodies %d, candidates %d, units %d' % (len(s1['S1C']) * 8, sum(hu.values()), len(s1['units'])))
    print('  Delta histogram (40 = >=40):', dict(sorted(hu.items())))
    print('  kappa = 0 part:', dict(sorted(hk0.items())))
    o1 = sorted(s1['out'])
    print('  D <= 0 events among Delta <= 12 records:', sum(1 for r in o1 if r[1] <= 0), collections.Counter((r[0], r[1], r[2]) for r in o1 if r[1] <= 0).most_common(8))
    print('\n  smallest positive Delta (S1):')
    for L in show('S1', o1, lambda r: body_S1(r[6], r[7])): print(L)
    print('time %.1f' % (time.time() - t0), flush=True)
    for name in ('d2_S2.pkl', 'd2_S3.pkl'):
        try: s2 = pickle.load(open(name, 'rb'))
        except FileNotFoundError: continue
        C = s2['S2C']
        h = s2['hist']; hall = collections.Counter(); hk0 = collections.Counter()
        for (sf, k0), v in h.items():
            hall[sf] += v
            if k0: hk0[sf] += v
        print('\n%s: children %d, pairs %d, candidates %d, units %d' % (name, len(C), len(C) * (len(C) + 1) // 2, sum(hall.values()), len(s2['units'])))
        print('  Delta histogram, ALL bodies (40 = >=40):', dict(sorted(hall.items())))
        # ideal tests: low tail + sample
        pairs = sorted({(r[6], r[7]) for r in s2['out']} | {(r[6], r[7]) for r in s2['sample']})
        with Pool(9) as P:
            U = {(i, j): u for i, j, u in P.map(pair_uni, [(C, i, j) for i, j in pairs], chunksize=50)}
        smp = s2['sample']
        su = [r for r in smp if U[(r[6], r[7])]]
        print('  uniform sample: %d candidate events, unimodular %d (%.2f%%)' % (len(smp), len(su), 100.0 * len(su) / max(1, len(smp))))
        hsu = collections.Counter(min(r[0], 40) for r in su)
        print('  Delta histogram, UNIMODULAR sample:', dict(sorted(hsu.items())))
        low = sorted(s2['out'])
        lowu = [r for r in low if U[(r[6], r[7])]]
        print('  Delta <= 12 records: %d, of which unimodular %d; Delta values (all): %s; unimodular: %s' % (
            len(low), len(lowu), dict(collections.Counter(r[0] for r in low)), dict(collections.Counter(r[0] for r in lowu))))
        print('  smallest positive Delta, UNIMODULAR (%s):' % name)
        for L in show(name[3:5], lowu, lambda r: body_S2(C, r[6], r[7], r[8])): print(L)
        print('  smallest positive Delta, NON-unimodular (%s):' % name)
        for L in show(name[3:5], [r for r in low if not U[(r[6], r[7])]], lambda r: body_S2(C, r[6], r[7], r[8]), k=3): print(L)
        print('time %.1f' % (time.time() - t0), flush=True)
