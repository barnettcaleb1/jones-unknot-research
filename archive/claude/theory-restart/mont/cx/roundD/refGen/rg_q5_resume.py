"""resume Q5: run every seed in 70000..71999 not yet in rg_q5_lpJ.pkl / rg_q5_lpJ_b.pkl / rg_q5_lpJ_c.pkl; save after EVERY result"""
import sys, time, pickle, os
from multiprocessing import Pool
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen')
import rg_q5_closures as Q
RG = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refGen/'
def load(fn):
    try: return pickle.load(open(RG + fn, 'rb'))
    except Exception: return []
if __name__ == '__main__':
    nj = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    have = set(r['seed'] for fn in ('rg_q5_lpJ.pkl', 'rg_q5_lpJ_b.pkl', 'rg_q5_lpJ_c.pkl') for r in load(fn))
    C = load('rg_q5_lpJ_c.pkl')
    todo = [(s, 'V' if (s - 70000) % 2 == 0 else 'H') for s in range(70000, 72000) if s not in have]
    print('already', len(have), 'todo', len(todo), flush=True)
    t0 = time.time()
    with Pool(nj) as P:
        for i, r in enumerate(P.imap_unordered(Q.job_lpJ2, todo)):
            C.append(r)
            pickle.dump(C, open(RG + 'rg_q5_lpJ_c.pkl', 'wb'))
            if (i + 1) % 50 == 0:
                print('  +%d (total %d), units %d, disagreements %d, %.0fs' % (i + 1, len(have) + i + 1,
                      sum(o['J_unit'] for o in C), sum(not o['agree'] for o in C), time.time() - t0), flush=True)
    print('resume done', len(C))
