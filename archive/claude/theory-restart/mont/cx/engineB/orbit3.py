"""Width-three version of orbit_search: line stabilisers of the cap vector of s.l1.l1.l1 in rho_3 (dim 51).
Exact 3-D tangle test via F_7 (g0 = axis, g1..g6 = legs), caps c1 = g1g2, c2 = g3g4, c3 = g5g6, psi_0 -> F_4.
usage: orbit3.py MAXDEPTH MAXNODES SEED"""
import sys, random, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import fastJ3, fgroup
P = (1 << 61) - 1
NG = 7
def sig(i, sign):
    a, b = i + 1, i + 2
    return {i: (a, b, -a), i + 1: (a,)} if sign > 0 else {i: (b,), i + 1: (-b, a, b)}
def twice(im):
    first = {j: fgroup.apply_aut(im, (j + 1,)) for j in range(NG)}
    return {j: w for j, w in ((j, fgroup.apply_aut(im, w)) for j, w in first.items()) if w != (j + 1,)}
S = {}
for i in range(1, 6):
    S['x%d' % i] = sig(i, +1); S['y%d' % i] = sig(i, -1)
S['x0'] = twice(sig(0, +1)); S['y0'] = twice(sig(0, -1))
LET = fastJ3.LET
INV = {L: ('y' if L[0] == 'x' else 'x') + L[1:] for L in LET}
INVIMG = {L: [fgroup.apply_aut(S[INV[L]], (j + 1,)) for j in range(NG)] for L in LET}
PSI0 = [(1,), (2,), (-2,), (3,), (-3,), (4,), (-4,)]
def subst(images, w):
    out = []
    for s in w:
        img = images[abs(s) - 1]; out.extend(img if s > 0 else fgroup.inv(img))
    return fgroup.red(out)
def evt(poly, t): return sum(c * pow(t, e % (P - 1), P) for e, c in poly.items()) % P
def proj(v):
    for x in v:
        if x:
            ix = pow(x, P - 2, P); return tuple((y * ix) % P for y in v)
def main(maxdepth, maxnodes, seed):
    rnd = random.Random(seed); t = rnd.randrange(2, P - 1)
    n = fastJ3.n
    SMt = {L: [[(j, evt(fastJ3.MT[L][i][j], t)) for j in range(n) if fastJ3.MT[L][i][j]] for i in range(n)] for L in LET}
    V = [evt(x, t) if x else 0 for x in fastJ3.VT]
    def mv(L, v): return [sum(c * v[j] for j, c in row) % P for row in SMt[L]]
    caps = [(2, 3), (4, 5), (6, 7)]
    store = {proj(V): ((), caps)}
    frontier = [((), caps, PSI0, V)]
    geo = 0; nongeo = []; t0 = time.time(); counts = [1]
    for d in range(1, maxdepth + 1):
        new = []
        for word, cs, psi, v in frontier:
            last = word[-1] if word else None
            for L in LET:
                if last and INV[L] == last: continue
                nv = mv(L, v); h = proj(nv); w2 = word + (L,)
                npsi = [subst(psi, INVIMG[L][j]) for j in range(NG)]
                if h in store:
                    w1, cs1 = store[h]
                    if all(not subst(npsi, c) for c in cs1): geo += 1
                    else:
                        nongeo.append(('.'.join(w2), '.'.join(w1))); print('NONGEOMETRIC', '.'.join(w2), '|', '.'.join(w1), flush=True)
                    continue
                ncs = [fgroup.apply_aut(S[L], c) for c in cs]
                store[h] = (w2, ncs)
                new.append((w2, ncs, npsi, nv))
                if len(store) >= maxnodes: break
            if len(store) >= maxnodes: break
        frontier = new; counts.append(len(new))
        print('depth', d, 'new', len(new), 'total', len(store), 'geometric re-hits', geo, 'nongeo', len(nongeo), 'time', round(time.time() - t0, 1), flush=True)
        if len(store) >= maxnodes or not new: break
    res = {'counts': counts, 'points': len(store), 'geometric_rehits': geo, 'nongeometric': nongeo}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/orbit3_d%d.json' % maxdepth, 'w'))
    print('RESULT', {k: v for k, v in res.items() if k != 'nongeometric'}, 'n_nongeo', len(nongeo), flush=True)
if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
