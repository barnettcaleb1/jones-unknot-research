"""(b) targeted test: units planted on axis lines n=n0 (|n0|<=3B) with free parameter |m0| up to and BEYOND the
claimed line bound floor((W+6|n0|+SD)/2); generic realisations via exact linear algebra; full box brute force."""
import random, sys, time
from wbf import SECT, Table, trim, check_table, top
from exhaustive import analyse_target, BOUND
from construct import construct
rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
Dlist = [[1], [1, 1], [1, -1], [1, 1, 1], [1, 0, 1], [1, 0, 0, -1], [1, 1, 2, 1, 1]]
nt = 0; nviol = 0; best = (0, None); feas_beyond = 0; whole_beyond = 0
t0 = time.time()
for Dco in Dlist:
    SD = len(Dco) - 1; D = trim(0, list(Dco))
    for Wn in range(0, 5):
        B = max(1, Wn, SD)
        for n0 in range(-3 * B, 3 * B + 1):
            bnd = (Wn + 6 * abs(n0) + SD) // 2
            for m0 in list(range(1, bnd + 7)) + list(range(-bnd - 6, 0)):
                if abs(m0) < max(1, bnd - 3): continue
                ks = analyse_target(m0, n0, Wn, Dco, SD)
                if not ks: continue
                if abs(m0) > bnd: feas_beyond += 1
                for rep in range(2):
                    p = construct(m0, n0, Wn, Dco, rng.choice(ks), rng)
                    if p is None or any(p[s] is None for s in BOUND): continue
                    for swap in (False, True):   # also the vertical-line version (transpose sectors)
                        if swap:
                            q = {'00': p['00'], '02': p['20'], '20': p['02'], '22': p['22'], '24': p['42'], '42': p['24'], '44': p['44']}
                        else:
                            q = p
                        T = Table(q, D)
                        r = check_table(T)
                        nt += 1
                        if r['viol']:
                            nviol += 1; print('VIOLATION', Dco, Wn, (m0, n0), swap, r['viol'][:4], flush=True)
                        # ratio of the free parameter to the actual-W_line bound on this line
                        axis = 'v' if swap else 'h'
                        g = T.line_groups(axis, n0)
                        if len(g) >= 2:
                            Wl = max(top(v) for v in g.values()) - min(v[0] for v in g.values())
                            ab = (Wl + SD) // 2
                            ratio = abs(m0) / max(1, ab)
                            if ratio > best[0]: best = (ratio, (Dco, Wn, m0, n0, Wl, ab))
                        elif abs(m0) > bnd:
                            whole_beyond += 1
print('tables', nt, 'violations', nviol, 'feasible targets beyond claimed bound', feas_beyond,
      '(realised only as one-group whole lines:', whole_beyond, ')', 'max |m0|/bound(actual W_line) =', best,
      '%.0fs' % (time.time() - t0))
