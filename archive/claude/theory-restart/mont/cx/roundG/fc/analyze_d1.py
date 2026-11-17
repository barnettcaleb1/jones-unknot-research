"""Analysis of d1.pkl: counts, unimodular fraction, units by type, deficit distribution among UNIMODULAR orbits at candidates,
10 smallest positive deficits with full eigenpairs, pair-criterion cross-check vs direct ideal test, witness verification,
lp.J on unit events (half-words written to d1_units.json for certification)."""
import sys, pickle, collections, random, json, time
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundG/fc')
import fc_core as fc
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import lib, vc, lp
R5 = lib.rational(5)
CH = [fc.chan_from_vc(r[1]) for r in R5]
d = pickle.load(open('d1.pkl', 'rb')); res = d['res']; tab = d['tab']
rng = random.Random(17)
t0 = time.time()
def body(idx, N):
    a = (0, [1]); b = (0, [1])
    for i in idx: a = fc.mul(a, CH[i][0]); b = fc.mul(b, CH[i][1])
    a, c = fc.state_from_channel(a, fc.shift(b, -3 * N))
    return a, c
def tree(idx, N, m):
    kids = [R5[i][2] for i in idx] + ([('w', ('Y' if N > 0 else 'y') * abs(N))] if N else [])
    return ('n', m, kids) if m else ('p', kids)
st = collections.Counter(); keys = set(); ukeys = set()
hist_u = collections.Counter(); hist_n = collections.Counter(); histD_u = collections.Counter()
hist_u_k0 = collections.Counter(); units = []; small = []
by_n = collections.defaultdict(collections.Counter)
for idx, N, uni, kappa, H, cands, key in res:
    n = len(idx)
    if kappa is None: st['scalar'] += 1; continue
    st['orbits'] += 1; by_n[n]['orbits'] += 1
    keys.add(key)
    if uni: st['unimodular'] += 1; by_n[n]['unimodular'] += 1; ukeys.add(key)
    for (m, unit, sf, tau0, tauinf, r0, rinf, Dd, Delta) in cands:
        if sf is None: st['f_zero'] += 1; continue
        if unit:
            units.append((idx, N, m, uni, kappa, H)); st['unit_events'] += 1
            st['unit_m0' if m == 0 else 'unit_m!=0'] += 1
        if uni:
            hist_u[min(sf, 40)] += 1; histD_u[max(min(Dd, 40), -10)] += 1
            if kappa == 0: hist_u_k0[min(sf, 40)] += 1
            if sf > 0: small.append((sf, Dd, kappa, H, tau0, tauinf, idx, N, m))
        else:
            hist_n[min(sf, 40)] += 1
print('DEPTH ONE: orbits %d (scalar %d), distinct eigenpair keys %d, unimodular orbits %d (%.2f%%), distinct unimodular keys %d' % (
    st['orbits'], st['scalar'], len(keys), st['unimodular'], 100.0 * st['unimodular'] / st['orbits'], len(ukeys)))
for n in sorted(by_n): print('  n=%d: orbits %d unimodular %d (%.2f%%)' % (n, by_n[n]['orbits'], by_n[n]['unimodular'], 100.0 * by_n[n]['unimodular'] / by_n[n]['orbits']))
print('unit events at candidates: %d  (m = 0: %d, m != 0: %d); f identically zero: %d' % (st['unit_events'], st['unit_m0'], st['unit_m!=0'], st['f_zero']))
print('unit events on unimodular orbits:', sum(1 for u in units if u[3]), ' on non-unimodular:', sum(1 for u in units if not u[3]))
print('Delta = span f_m at candidates, UNIMODULAR orbits (40 = >=40):', dict(sorted(hist_u.items())))
print('   of which kappa = 0 (two-ended):', dict(sorted(hist_u_k0.items())))
print('D = H - tau0 - tauinf at candidates, UNIMODULAR (clipped [-10,40]):', dict(sorted(histD_u.items())))
print('Delta at candidates, NON-unimodular orbits:', dict(sorted(hist_n.items())))
small.sort()
print('\n10 smallest positive Delta among unimodular depth-one orbits:')
seen = set(); cnt = 0
for sf, Dd, kappa, H, tau0, tauinf, idx, N, m in small:
    a, c = body(idx, N); A, B = fc.eigen(a, c)
    k = fc.okey(A, B)
    if k in seen: continue
    seen.add(k); cnt += 1
    T = tree(idx, N, m)
    print('  Delta=%d D=%d kappa=%d H=%d tau=(%d,%d) body=Y^%d%s m=%d  hw=%s' % (sf, Dd, kappa, H, tau0, tauinf, N, [R5[i][2] for i in idx], m, vc.hw(T)))
    print('     A =', sorted(fc.todict(A).items())); print('     B =', sorted(fc.todict(B).items()))
    if cnt >= 10: break
# unit events: lp.J and halfwords
out = []
for idx, N, m, uni, kappa, H in units:
    T = tree(idx, N, m)
    w = vc.hw(T)
    J = lp.J(w)
    out.append({'w': w, 'idx': idx, 'N': N, 'm': m, 'unimodular': uni, 'kappa': kappa, 'H': H, 'J': sorted(J.items()) if J else None})
json.dump(out, open('d1_units.json', 'w'))
print('\nunit events: %d, lp.J = 1 for %d; kappas %s' % (len(out), sum(1 for o in out if o['J'] == [(0, 1)]), collections.Counter(o['kappa'] for o in out)))
print('  sample:', [(o['w'], o['m']) for o in out[:5]])
# a_i closures of the children at unit events (expect all two-bridge unknots when m = 0)
ch_unit = collections.Counter()
for o in out:
    ch_unit[all(fc.isunit(CH[i][0]) for i in o['idx'])] += 1
print('  unit events whose children all have unit a-channel (connected sum of unknots):', dict(ch_unit))
# cross-check pair criterion vs direct ideal test, and witness verification
def verify_witness(a, c, q, G):
    def rem(f):
        f = [x % q for x in f[1]]
        dg = len(G) - 1
        for i in range(len(f) - 1 - dg, -1, -1):
            co = f[i + dg] % q
            if co:
                for j in range(dg + 1): f[i + j] = (f[i + j] - co * G[j]) % q
        return all(x == 0 for x in f[:dg])
    return rem(a) and rem(c)
cc = collections.Counter()
uni_rows = [r for r in res if r[2] and r[3] is not None]; non_rows = [r for r in res if not r[2] and r[3] is not None]
sample = rng.sample(uni_rows, min(1500, len(uni_rows))) + rng.sample(non_rows, 1500)
for idx, N, uni, *_ in sample:
    a, c = body(idx, N)
    s, info = fc.ideal_test(a, c)
    direct = (s == 'UNIT')
    cc['agree' if direct == uni else 'DISAGREE'] += 1
    if s == 'PROPER':
        cc['witness_ok' if verify_witness(a, c, info[0], info[1]) else 'WITNESS_FAIL'] += 1
    cc['direct_' + s] += 1
print('\npair criterion vs direct ideal test on %d orbits:' % len(sample), dict(cc))
# pair-table witnesses verified directly
wc = collections.Counter()
for (i, j), (ok, s, info) in tab.items():
    if s == 'PROPER': wc['ok' if verify_witness(CH[i][0], CH[j][1], info[0], info[1]) else 'FAIL'] += 1
    else: wc[s] += 1
print('pair table statuses / witness checks:', dict(wc))
print('time %.1f' % (time.time() - t0))
