"""dedup_check.py -- is engineB's MITM deduplication GEOMETRIC?  Every re-hit (a word pruned because its projective rho_2 point
equals that of an earlier class representative) is tested with the EXACT full-picture kernel criterion (tangle_kernel.py):
  BOTTOMS: all re-hit pairs (U1 = stored class word, U2 = new word) of the bottom BFS to depth 8 (cert/extract/data/
           s1_rehits_d8_s11.json, regenerated there from engineB/bottom_orbit.py; the MITM (7,7) uses depth <= 7);
  TOPS:    the top BFS of engineB/mitm.py (imported read-only) re-run to depth DT with every re-hit pair (g1 stored, g2 new).
Also compares with the extract lane's word-level proofs (bottom pairs reduced to the empty word by proved bottom moves).
usage: dedup_check.py DT NPROC OUT.json"""
import sys, os, json, time, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tangle_kernel as TK
from multiprocessing import Pool
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')

def top_rehits(depth, seed=3):
    import mitm, rho2
    P = mitm.P; rnd = random.Random(seed); t = rnd.randrange(2, P - 1)
    MT, VT, PHIT = rho2.normalised()
    M = {L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}
    v = [mitm.evt(x, t) for x in VT['l1.l1']]
    store = {mitm.proj(v): ()}; frontier = [((), v)]; pairs = []; counts = [1]
    for d in range(1, depth + 1):
        new = []
        for word, vec in frontier:
            last = word[-1] if word else None
            for L in mitm.LET:
                if last and mitm.INV[L] == last: continue
                nv = mitm.mv(M[L], vec); h = mitm.proj(nv); w2 = word + (L,)
                if h in store: pairs.append((d, store[h], w2)); continue
                store[h] = w2; new.append((w2, nv))
        frontier = new; counts.append(len(new))
    return pairs, counts

def chk_bot(item):
    d, u1, u2 = item
    U1 = [x for x in u1.split('.') if x]; U2 = [x for x in u2.split('.') if x]
    return d, TK.same_bottom(U1, U2)

def chk_top(item):
    d, g1, g2 = item
    return d, TK.same_top(list(g1), list(g2))

if __name__ == '__main__':
    DT, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    from collections import Counter
    res = {}
    t0 = time.time()
    reh = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s1_rehits_d8_s11.json'))['rehits']
    with Pool(nproc) as P: rb = P.map(chk_bot, reh, chunksize=200)
    cb = Counter((d, ok) for d, ok in rb)
    res['bottom'] = {'pairs': len(rb), 'geometric': sum(1 for d, ok in rb if ok), 'NONGEOMETRIC': sum(1 for d, ok in rb if not ok),
                     'by_depth': {'%d_%s' % k: v for k, v in sorted(cb.items())},
                     'depth_le7_pairs': sum(1 for d, ok in rb if d <= 7), 'depth_le7_geometric': sum(1 for d, ok in rb if d <= 7 and ok),
                     'nongeometric_examples': [reh[i] for i, (d, ok) in enumerate(rb) if not ok][:20], 'secs': round(time.time() - t0, 1)}
    print('bottom', json.dumps({k: v for k, v in res['bottom'].items() if k != 'nongeometric_examples'}), flush=True)
    t1 = time.time()
    pairs, counts = top_rehits(DT)
    with Pool(nproc) as P: rt = P.map(chk_top, pairs, chunksize=200)
    ct = Counter((d, ok) for d, ok in rt)
    res['top'] = {'depth': DT, 'classes_per_depth': counts, 'classes_total': sum(counts), 'pairs': len(rt),
                  'geometric': sum(1 for d, ok in rt if ok), 'NONGEOMETRIC': sum(1 for d, ok in rt if not ok),
                  'by_depth': {'%d_%s' % k: v for k, v in sorted(ct.items())},
                  'nongeometric_examples': [('.'.join(pairs[i][1]), '.'.join(pairs[i][2])) for i, (d, ok) in enumerate(rt) if not ok][:20],
                  'secs': round(time.time() - t1, 1)}
    print('top', json.dumps({k: v for k, v in res['top'].items() if k != 'nongeometric_examples'}), flush=True)
    json.dump(res, open(outp, 'w'), indent=1)
