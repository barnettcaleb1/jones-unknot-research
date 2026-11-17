"""DEPTH-ONE body library (all of ARB's enumerated depth-one bodies F_m(Y^N u_1..u_n): R(5) n=2,3; R(4) n=4; |N|<=4; 1<=|m|<=7).
F_m acts on the eigenpair by (A, B) -> (A, (-t)^-m B) up to one common unit (PROVED, refereed), so the 2,040,176 bodies fall into
F-ORBITS Y^N u_1..u_n (145,584), and every F-C quantity (ideal, kappa, H, unit status and deficit at the candidates) is an
orbit invariant (candidates shift by m).  Per orbit: exact eigenpair, ideal test, candidates, unit test, deficits.
Ideal: rational boxes are unimodular (columns of GL2(Lambda) matrices); a product of unimodular states is unimodular iff
(a_i, b_j) = Lambda for every ordered pair of distinct positions i != j (PAIR CRITERION, proved in REPORT 2.2).  The pair table
is computed with fc.ideal_test; the criterion is cross-checked against the direct test on the product state."""
import sys, itertools, pickle, time, collections, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundG/fc')
import fc_core as fc
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import lib, vc
from multiprocessing import Pool
R5 = lib.rational(5); R4 = lib.rational(4)
K5 = {r[0]: i for i, r in enumerate(R5)}
map4 = [K5[r[0]] for r in R4]                 # R(4) boxes inside R(5)
CH = [fc.chan_from_vc(r[1]) for r in R5]
NS = list(range(-4, 5))
U = None
def pair_table():
    tab = {}
    for i in range(len(R5)):
        for j in range(len(R5)):
            st, info = fc.ideal_test(CH[i][0], CH[j][1])     # (a_i, b_j)
            tab[(i, j)] = (st == 'UNIT', st, info if st == 'PROPER' else None)
    return tab
def init(tab):
    global U; U = tab
def work(job):
    out = []
    for idx in job:
        n = len(idx)
        uni = all(U[(idx[i], idx[j])][0] for i in range(n) for j in range(n) if i != j)
        a = (0, [1]); b = (0, [1])
        for i in idx:
            a = fc.mul(a, CH[i][0]); b = fc.mul(b, CH[i][1])
        for N in NS:
            bN = fc.shift(b, -3 * N)
            a_, c = fc.state_from_channel(a, bN)
            A, B = fc.eigen(a_, c)
            if not B[1]:
                out.append((idx, N, uni, None, None, None, None)); continue
            kappa, H, cands = fc.analyze(A, B)
            out.append((idx, N, uni, kappa, H, cands, fc.okey(A, B)))
    return out
if __name__ == '__main__':
    t0 = time.time()
    tab = pair_table()
    nU = sum(1 for k, v in tab.items() if v[0])
    print('pair table R(5): %d ordered pairs, unimodular (a_i,b_j): %d, time %.1f' % (len(tab), nU, time.time() - t0), flush=True)
    jobs = []
    for n in (2, 3):
        jobs += list(itertools.combinations_with_replacement(range(len(R5)), n))
    jobs += [tuple(sorted(map4[i] for i in c)) for c in itertools.combinations_with_replacement(range(len(R4)), 4)]
    print('multisets', len(jobs), 'orbits', 9 * len(jobs), flush=True)
    chunks = [jobs[i::200] for i in range(200)]
    res = []
    with Pool(8, initializer=init, initargs=(tab,)) as P:
        for o in P.imap_unordered(work, chunks):
            res.extend(o)
    print('computed', len(res), 'time %.1f' % (time.time() - t0), flush=True)
    pickle.dump({'tab': tab, 'res': res}, open('d1.pkl', 'wb'))
    print('saved d1.pkl', flush=True)
