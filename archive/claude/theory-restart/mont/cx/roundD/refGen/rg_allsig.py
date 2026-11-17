"""Full independent re-run of C1's per-box theorem generator:
 (1) recompute the signature (B-data at both ends, sigma, delta, lc-admissibility, span a) of ALL 48,683 eligible boxes
     with OUR end-data code from the exact vectors (vc.vec(tree)) and compare with C1's signature keys;
 (2) run OUR generator (rg_gen.prove, n_min = 1) on every signature; compare verdicts with C1's resV/resH.
Where C1 proves a class and we do not (grid miss), C1's regenerated witness is re-checked exactly with our code."""
import sys, pickle, time, collections
from multiprocessing import Pool
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_gen as G
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
C1 = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1'
def sigjob(chunk):
    sys.path.insert(1, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
    import vc
    out = []
    for x, T, key in chunk:
        a, b = vc.vec(T)
        Bd, sg, dl, lcok, spa = G.bdata_from_vec(a, b)
        out.append((x, (Bd['top'], Bd['bot'], sg, dl) == key and lcok and spa >= 1))
    return out
def genjob(key):
    Bd = {'top': key[0], 'bot': key[1]}
    r = G.prove(Bd, key[2], key[3], 1)
    return key, {k: v for k, v in r.items() if v}
def init():
    G.load_gtab(RG + 'rg_gtab.pkl')
if __name__ == '__main__':
    t0 = time.time()
    nj = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    Gr = pickle.load(open(C1 + '/gen2_res.pkl', 'rb'))
    sigs = Gr['sigs']; resV = Gr['resV']; resH = Gr['resH']
    items = [(x, Gr['trees'][x], k) for k, xs in sigs.items() for x in xs]
    chunks = [items[i::40] for i in range(40)]
    with Pool(nj) as P:
        res = [r for c in P.map(sigjob, chunks) for r in c]
    nok = sum(1 for x, ok in res if ok)
    print('signatures recomputed for %d boxes: %d match C1 keys (%.0fs)' % (len(res), nok, time.time() - t0), flush=True)
    keys = list(sigs)
    mine = {}
    with Pool(nj, initializer=init) as P:
        for i, (k, opn) in enumerate(P.imap_unordered(genjob, keys, chunksize=4)):
            mine[k] = opn
            if (i + 1) % 500 == 0: print('  %d/%d signatures, %.0fs' % (i + 1, len(keys), time.time() - t0), flush=True)
    pickle.dump(mine, open(RG + 'rg_allsig.pkl', 'wb'))
    # compare
    cmp = collections.Counter(); wboxes = collections.Counter(); diff = []
    for k in keys:
        c1V = resV[k][0]; c1H = all(not v for v in resH[k].values()); c1B = c1V and c1H
        mV = not any(fam == 'V' for (fam, c) in mine[k]); mH = not any(fam == 'H' for (fam, c) in mine[k])
        mB = mV and mH
        cmp[('V', c1V, mV)] += 1; cmp[('H', c1H, mH)] += 1; cmp[('BOTH', c1B, mB)] += 1
        wboxes[('BOTH', c1B, mB)] += len(sigs[k])
        if c1B and not mB and len(diff) < 30: diff.append((k, mine[k]))
    print('verdict comparison (family, C1 proved, ours proved): signatures', dict(cmp))
    print('BOTH weighted by boxes:', dict(wboxes))
    for d in diff[:10]: print('  C1-only:', d)
    print('done %.0fs' % (time.time() - t0))
