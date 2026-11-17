"""second batch of the Q5 lp.J run (same job function, seeds 71999 down to 71000; combine with rg_q5_lpJ.pkl by seed)"""
import sys, time, pickle
from multiprocessing import Pool
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_q5_closures as Q
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
if __name__ == '__main__':
    nj = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    args = [(s, 'V' if (s - 70000) % 2 == 0 else 'H') for s in range(71999, 70999, -1)]
    out = []; t0 = time.time()
    with Pool(nj) as P:
        for i, r in enumerate(P.imap_unordered(Q.job_lpJ2, args)):
            out.append(r)
            if (i + 1) % 50 == 0:
                print('  %d done, units %d, disagreements %d, %.0fs' % (i + 1, sum(o['J_unit'] for o in out),
                      sum(not o['agree'] for o in out), time.time() - t0), flush=True)
                pickle.dump(out, open(RG + 'rg_q5_lpJ_b.pkl', 'wb'))
    pickle.dump(out, open(RG + 'rg_q5_lpJ_b.pkl', 'wb'))
    print('batch b done', len(out))
