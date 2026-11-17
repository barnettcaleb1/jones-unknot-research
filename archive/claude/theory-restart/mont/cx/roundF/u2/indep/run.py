"""u2/indep/run.py -- run the independent global-disc tests (up.py = upstairs/full picture, down.py = downstairs re-implementation)
on every U2 family, at EVERY reachable cut (the verdict must be cut-independent: the commuting letters fix the site circles and
the relators psi_0((W^-1)_*(cup)) do not depend on the cut), plus cert/run's Lemma K half-stabiliser test (audited
tangle_kernel copy in u2/code) at every cut for the plane sites, and the plane composition rule (REPORT section 2).
usage: run.py NPROC"""
import sys, os, json, time
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/code')
from multiprocessing import Pool
from collections import Counter
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
def tw(m, n): return (['x1', 'x1'] * m if m > 0 else ['y1', 'y1'] * (-m)) + (['x3', 'x3'] * n if n > 0 else ['y3', 'y3'] * (-n))
def sp(s): return [a for a in s.split('.') if a]
COMM = {'X1': {'x1', 'y1', 'x3', 'y3'}, 'X3': {'x0', 'y0', 'x1', 'y1', 'x3', 'y3'}}
def cutrange(W, j0, site):
    lo = j0
    while lo > 0 and W[lo - 1] in COMM[site]: lo -= 1
    hi = j0
    while hi < len(W) and W[hi] in COMM[site]: hi += 1
    return lo, hi
def site_all(W, j0, site):
    import up, down
    lo, hi = cutrange(W, j0, site)
    ups = []; dns = []
    for i in range(lo, hi + 1):
        ok, det = up.site_test(W[:i], W[i:], site); ups.append(ok)
        dns.append(down.site_test(W[:i], W[i:], site))
    return {'lo': lo, 'hi': hi, 'up': ups, 'down': dns}
def lemmak_all(W, j0, site):
    import tangle_kernel as TK
    lo, hi = cutrange(W, j0, site)
    var = ['x1', 'x1'] if site == 'X1' else ['x3', 'x3']
    top = [i for i in range(lo, hi + 1) if TK.same_top(W[:i], W[:i] + var)]
    bot = [i for i in range(lo, hi + 1) if TK.same_bottom(W[i:], var + W[i:])]
    return {'top': top, 'bottom': bot}
def job(f):
    V, U = sp(f['V']), sp(f['U'])
    out = {'fid': f['fid']}
    if f['kind'] == 'line':
        site = 'X1' if tuple(f['d']) == (1, 0) else 'X3'
        W = V + tw(f['m0'], f['n0']) + U; j0 = len(V)
        r = site_all(W, j0, site)
        out.update({'site': site, 'res': r,
                    'up_ok': all(r['up']), 'up_any': any(r['up']), 'up_cut_indep': len(set(r['up'])) == 1,
                    'down_ok': all(x in ('T-disc', 'S-trivial', 'H-vertex') for x in r['down']),
                    'down_kinds': sorted(set(r['down'])), 'down_cut_indep': len(set(r['down'])) == 1})
        out['verdict'] = 'PROVED-up' if out['up_ok'] else 'NOT-up'
    else:
        W = V + U; j0 = len(V)
        r1 = site_all(W, j0, 'X1'); r3 = site_all(W, j0, 'X3')
        k1 = lemmak_all(W, j0, 'X1'); k3 = lemmak_all(W, j0, 'X3')
        g1 = all(r1['up']); g3 = all(r3['up'])
        # composition rule: global(X) + Lemma-K half stabiliser of the other site Y at a cut compatible with X's range
        def compat(rx, ky):
            # Y bottom stabiliser at cut i: X's circles must sit at or above level i (rx['lo'] <= i);
            # Y top stabiliser at cut i: X's circles at or below level i (rx['hi'] >= i)
            return any(rx['lo'] <= i for i in ky['bottom']) or any(rx['hi'] >= i for i in ky['top'])
        if g1 and g3: v = 'PROVED-up-both-global'
        elif g1 and compat(r1, k3): v = 'PROVED-up-global-X1+LemmaK-X3'
        elif g3 and compat(r3, k1): v = 'PROVED-up-global-X3+LemmaK-X1'
        elif k1['top'] + k1['bottom'] and k3['top'] + k3['bottom']: v = 'LemmaK-both-sites (needs compatibility)'
        else: v = 'NOT-PROVED'
        out.update({'X1': r1, 'X3': r3, 'LK1': k1, 'LK3': k3, 'g1': g1, 'g3': g3,
                    'cut_indep': all(len(set(r['up'])) == 1 and len(set(r['down'])) == 1 for r in (r1, r3)),
                    'down1': sorted(set(r1['down'])), 'down3': sorted(set(r3['down'])), 'verdict': v})
    return out
if __name__ == '__main__':
    nproc = int(sys.argv[1])
    fams = json.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/families.json'))
    t0 = time.time()
    with Pool(nproc) as P: res = P.map(job, fams, chunksize=25)
    byid = {f['fid']: f for f in fams}
    tab = Counter(); disagree = []
    for r in res:
        f = byid[r['fid']]
        key = (f['src'], f['kind'], tuple(f['d']) if f['kind'] == 'line' else f.get('critic_indep'), 'U2' if f['u2_target'] else 'covered', r['verdict'])
        tab[key] += 1
        if f['kind'] == 'line':
            if not r['up_cut_indep'] or not r['down_cut_indep']: tab[('CUT-DEPENDENT!', f['fid'])] += 1
            if r['up_ok'] != r['down_ok']: disagree.append(r['fid'])
        else:
            if not r['cut_indep']: tab[('CUT-DEPENDENT plane!', f['fid'])] += 1
    for k in sorted(tab, key=str): print('   ', k, tab[k])
    print('line up/down disagreements:', len(disagree), disagree[:10])
    print('secs', round(time.time() - t0, 1))
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundF/u2/out/run_results.json', 'w'))
