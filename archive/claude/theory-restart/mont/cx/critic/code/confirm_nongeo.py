"""confirm_nongeo.py -- independent confirmation of the kernel test's verdicts on bottom re-hit pairs with the boundary
representation sets S_T(G) of tangle_reps.py (G = S3, then S4 if S3 does not separate):  different sets CERTIFY different
tangles; equal kernels must give equal sets.  usage: confirm_nongeo.py NPROC NGEO_SAMPLE OUT.json"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tangle_kernel as TK, tangle_reps as TR
from multiprocessing import Pool
S3 = TR.sym_elements(3); S4 = None
def work(item):
    global S4
    dep, u1, u2, kernel_same = item
    U1 = [x for x in u1.split('.') if x]; U2 = [x for x in u2.split('.') if x]
    w1, w2 = TR.psi_words_bottom(U1), TR.psi_words_bottom(U2)
    a, b = TR.boundary_set(w1, S3), TR.boundary_set(w2, S3)
    sep = 'S3' if a != b else None
    if sep is None and not kernel_same:
        if S4 is None: S4 = TR.sym_elements(4)
        if TR.boundary_set(w1, S4) != TR.boundary_set(w2, S4): sep = 'S4'
    return dep, u1, u2, kernel_same, sep
if __name__ == '__main__':
    nproc, nsamp, outp = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    reh = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s1_rehits_d8_s11.json'))['rehits']
    items = []
    for dep, u1, u2 in reh:
        ks = TK.same_bottom([x for x in u1.split('.') if x], [x for x in u2.split('.') if x])
        items.append((dep, u1, u2, ks))
    ng = [x for x in items if not x[3]]
    rng = random.Random(9); geo = rng.sample([x for x in items if x[3]], nsamp)
    t0 = time.time()
    with Pool(nproc) as P: res = P.map(work, ng + geo, chunksize=4)
    ng_res = [r for r in res if not r[3]]; geo_res = [r for r in res if r[3]]
    summ = {'nongeometric_pairs': len(ng_res), 'separated_by_S3': sum(1 for r in ng_res if r[4] == 'S3'),
            'separated_by_S4': sum(1 for r in ng_res if r[4] == 'S4'), 'NOT_SEPARATED': [r[:3] for r in ng_res if r[4] is None][:30],
            'n_not_separated': sum(1 for r in ng_res if r[4] is None),
            'geometric_sample': len(geo_res), 'geometric_but_sets_differ_CONTRADICTION': sum(1 for r in geo_res if r[4] is not None),
            'nongeometric_depth_le7': sum(1 for r in ng_res if r[0] <= 7), 'secs': round(time.time() - t0, 1)}
    print(json.dumps(summ)); json.dump({'summary': summ, 'nongeometric': [list(r) for r in ng_res]}, open(outp, 'w'), indent=1)
