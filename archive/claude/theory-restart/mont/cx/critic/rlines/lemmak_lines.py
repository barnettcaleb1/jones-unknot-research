"""critic: INDEPENDENT second proof (cert/run's Lemma K line test, lines_family.line_ok, exact kernel test in the full B_10
picture; no re-cuts) for every NON-axis-free S1/S2/J1/J2 unit line of regress's (6,6) census and of the census-missed lines.
(Axis-free lines already have the swap-sum proof.)  E lines are not half-stabiliser lines and are skipped."""
import sys, json, pickle, time
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines')
from multiprocessing import Pool
from collections import Counter
from axisfree2 import typ, family, axis_free
OUT = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/'
def job(chunk):
    sys.dont_write_bytecode = True
    sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/code')
    import lines_family as LF
    out = []
    for lab, wt, wb, d, m0, n0 in chunk:
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        r = LF.line_ok(V, U, tuple(d), (m0, n0))
        out.append((lab, bool(r)))
    return out
if __name__ == '__main__':
    d2 = pickle.load(open(OUT + 'classify2_6_6.pkl', 'rb')); r3 = pickle.load(open(OUT + 'classify3_6_6.pkl', 'rb'))
    lines = d2['lines']; items = []
    for (i, c, ex, nc, pt, Wb, cert) in d2['res']:
        t = typ(c, r3.get(i)); kind, wt, wb, d, m0, n0 = lines[i][:6]
        if kind == 'plane' or t not in ('S1-cap', 'S2-cup', 'J1-axis-split', 'J2-band-clasp'): continue
        V = [a for a in wt.split('.') if a]; U = [a for a in wb.split('.') if a]
        if axis_free(family(V, U, d, m0, n0)): continue
        items.append(((t, d), wt, wb, d, m0, n0))
    for r in json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/missed/missed66_classified.json')):
        if r['kind'] == 'plane': continue
        V = [a for a in r['V'].split('.') if a]; U = [a for a in r['U_missed'].split('.') if a]; d = tuple(r['d'])
        if axis_free(family(V, U, d, r['m0'], r['n0'])): continue
        items.append((('MISSED-' + r['type'][3], d), r['V'], r['U_missed'], d, r['m0'], r['n0']))
    print('lines to test', len(items), flush=True)
    chunks = [items[k:k + 500] for k in range(0, len(items), 500)]
    tot = Counter(); ok = Counter(); t0 = time.time()
    with Pool(3) as P:
        for j, res in enumerate(P.imap_unordered(job, chunks)):
            for lab, g in res: tot[lab] += 1; ok[lab] += g
            if j % 20 == 0: print('progress', sum(tot.values()), sum(ok.values()), round(time.time() - t0), flush=True)
    for k in sorted(tot, key=str): print('   ', k, 'tested', tot[k], 'Lemma-K stabiliser', ok[k])
    print('TOTAL', sum(tot.values()), 'PROVED by Lemma K', sum(ok.values()), 'secs', round(time.time() - t0), flush=True)
    json.dump({str(k): [tot[k], ok[k]] for k in tot}, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/critic/rlines/lemmak66.json', 'w'), indent=0)
