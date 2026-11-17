"""S1 tangle-level check: reduce U1^-1 U2 with group moves and BOTTOM absorptions only (no cap moves).  Reduction to the empty
word proves U1^-1 U2 in H_bot (product of proved bottom stabilisers), i.e. the bottom tangles U1.(cups) and U2.(cups) are
isotopic rel boundary, so V.U1 and V.U2 give isotopic knots for EVERY top V (geometric soundness of mitm.py's bottom dedupe)."""
import sys, json, time, multiprocessing as mp
from collections import Counter
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
import rules, reduce as R
def freered(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return tuple(out)
def work(item):
    R.USE['top'] = False; R.USE['bot'] = True
    dep, u1, u2 = item
    w = freered(rules.inv(rules.enc(u1)) + rules.enc(u2))
    r, m = R.reduce_word(w, budget=3000)
    assert R.replay(w, m) == r
    return dep, len(r) == 0
if __name__ == '__main__':
    d = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s1_rehits_d8_s11.json'))
    t0 = time.time()
    with mp.get_context('fork').Pool(int(sys.argv[1])) as pool: res = pool.map(work, d['rehits'], chunksize=500)
    c = Counter(); cd = Counter()
    for dep, ok in res: c[ok] += 1; cd[(dep, ok)] += 1
    print('bottom-only reduction to empty:', dict(c), 'by depth', sorted(cd.items()), round(time.time() - t0, 1), 's')
    json.dump({'total': len(res), 'empty': c[True], 'by_depth': {'%d_%s' % k: v for k, v in cd.items()}},
              open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s1_bottom_only.json', 'w'), indent=1)
