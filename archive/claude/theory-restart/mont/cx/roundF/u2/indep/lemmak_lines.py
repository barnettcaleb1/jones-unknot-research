"""u2/indep/lemmak_lines.py -- cert/run's Lemma K (audited tangle_kernel copy) at EVERY reachable cut of every U2 E line:
is the varying block a top or bottom stabiliser anywhere?  (Expected 0: type E = no half stabiliser; a positive would give a
second, half-space proof.)"""
import sys, json
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/indep')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/code')
from multiprocessing import Pool
from collections import Counter
import run
def job(f):
    V, U = run.sp(f['V']), run.sp(f['U'])
    site = 'X1' if tuple(f['d']) == (1, 0) else 'X3'
    W = V + run.tw(f['m0'], f['n0']) + U
    k = run.lemmak_all(W, len(V), site)
    return f['fid'], f['src'], site, bool(k['top'] or k['bottom'])
if __name__ == '__main__':
    fams = [f for f in json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/families.json')) if f['kind'] == 'line']
    with Pool(2) as P: res = P.map(job, fams, chunksize=50)
    c = Counter((r[1], r[2], r[3]) for r in res)
    for k in sorted(c, key=str): print('   (src, site, LemmaK-stabiliser-at-some-cut)', k, c[k])
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/lemmak_lines.json', 'w'))
