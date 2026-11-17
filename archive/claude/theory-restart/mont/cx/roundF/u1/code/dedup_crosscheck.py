"""dedup_crosscheck.py -- pairwise cross-check of the full-picture kernel test (tangle_kernel.same_bottom) against the extract
lane's word-level PROOFS of bottom-tangle equality (cert/extract/code: group moves + proved bottom Hilden moves, imported
read-only, exactly as in its s1_botonly.py).  A pair proved equal by word moves but rejected by the kernel test would show
the kernel test is wrong.  usage: dedup_crosscheck.py NPROC OUT.json"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tangle_kernel as TK
from multiprocessing import get_context
EXC = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code'
def freered(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)
def work(item):
    if EXC not in sys.path: sys.path.insert(0, EXC)
    import rules, reduce as R
    R.USE['top'] = False; R.USE['bot'] = True
    dep, u1, u2 = item
    w = freered(rules.inv(rules.enc(u1)) + rules.enc(u2))
    r, m = R.reduce_word(w, budget=3000)
    proved = (len(r) == 0)
    U1 = [x for x in u1.split('.') if x]; U2 = [x for x in u2.split('.') if x]
    return dep, proved, TK.same_bottom(U1, U2)
if __name__ == '__main__':
    nproc, outp = int(sys.argv[1]), sys.argv[2]
    reh = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s1_rehits_d8_s11.json'))['rehits']
    t0 = time.time()
    with get_context('fork').Pool(nproc) as P: res = P.map(work, reh, chunksize=300)
    from collections import Counter
    c = Counter((p, k) for d, p, k in res)
    bad = [reh[i] for i, (d, p, k) in enumerate(res) if p and not k]
    summ = {'pairs': len(res), 'proved_by_words&kernel_equal': c[(True, True)], 'PROVED_BUT_KERNEL_SAYS_DIFFERENT': c[(True, False)],
            'not_proved&kernel_equal': c[(False, True)], 'not_proved&kernel_different': c[(False, False)],
            'contradictions': bad[:20], 'secs': round(time.time() - t0, 1)}
    print(json.dumps(summ)); json.dump(summ, open(outp, 'w'), indent=1)
