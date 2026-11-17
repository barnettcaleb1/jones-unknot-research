"""E2: line-stabiliser search for the cap vector v = V[s.l1.l1] = f0  (Bigelow-style coincidence search).
BFS over the projective orbit [rho_2(G) v] mod p (G = type-B_4 Artin group, letters x0,y0,x1..y3), deduplicated by the
projective point itself.  When a new word g2 reaches an already-seen point (seen first via g1), decide EXACTLY whether
g1, g2 define the same 3-D tangle (axis + two caps, i.e. same Hilden-type coset):
   psi_g := psi_0 o g_*^{-1} : F_5 -> F_3 (quotient map of the tangle complement; psi_0: g0->a, g1->b, g2->b^-1, g3->c, g4->c^-1),
   g2 ~ g1  <=>  psi_{g1}(g2_*(c1)) = psi_{g1}(g2_*(c2)) = 1   (c1 = g1 g2, c2 = g3 g4; Hopfian F_3 gives equality of kernels).
A collision with different tangles = NON-GEOMETRIC line stabiliser beta = g1.g2^-1: J(s.l1.l1.beta.u2.u2) is a unit.
usage: orbit_search.py MAXDEPTH MAXNODES SEED"""
import sys, random, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import rho2, fgroup
P = (1 << 61) - 1
def evt(poly, t):
    s = 0
    for e, c in poly.items():
        s += c * pow(t, e % (P - 1), P)
    return s % P
def mats_at(t, prefix='l1.l1'):
    MT, VT, PHIT = rho2.normalised()
    M = {L: [[evt(x, t) for x in row] for row in m] for L, m in MT.items()}
    V = [evt(x, t) for x in VT[prefix]]
    PH = {S: [evt(x, t) for x in ph] for S, ph in PHIT.items()}
    return M, V, PH
def mv(M, v):
    return [sum(a * b for a, b in zip(row, v)) % P for row in M]
def proj(v):
    for x in v:
        if x:
            ix = pow(x, P - 2, P)
            return tuple((y * ix) % P for y in v)
    return None
LET = ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
# inverse-letter images of each generator, as words in F_5 symbols
INVIMG = {L: [fgroup.act(INV[L], (j + 1,)) for j in range(5)] for L in LET}
PSI0 = [(1,), (2,), (-2,), (3,), (-3,)]    # images of g0..g4 in F_3 = <a=1, b=2, c=3>
def subst(images, w):
    out = []
    for s in w:
        img = images[abs(s) - 1]
        out.extend(img if s > 0 else fgroup.inv(img))
    return fgroup.red(out)
def psi_step(psi, L):
    return [subst(psi, INVIMG[L][j]) for j in range(5)]
def same_tangle(psi1, c1b, c2b):
    return not subst(psi1, c1b) and not subst(psi1, c2b)
def enc(w): return bytes((s + 8) for s in w)
def dec(b): return tuple(x - 8 for x in b)
def main(maxdepth, maxnodes, seed, prefix='l1.l1'):
    """memory-lean version: store per point (word, curves as bytes); psi only on the frontier.
    Re-hit test uses psi of the NEW word against the stored curves (symmetric criterion)."""
    rnd = random.Random(seed)
    t = rnd.randrange(2, P - 1)
    M, V, PH = mats_at(t, prefix)
    c1, c2 = (2, 3), (4, 5); psi0 = PSI0
    store = {proj(V): ('', enc(c1), enc(c2))}
    frontier = [((), c1, c2, psi0, V)]
    noncoll = []; geo = 0; t0 = time.time(); depth_counts = [1]
    for d in range(1, maxdepth + 1):
        new = []
        for word, a, b, psi, v in frontier:
            last = word[-1] if word else None
            for L in LET:
                if last and INV[L] == last: continue
                nv = mv(M[L], v)
                h = proj(nv)
                w2 = word + (L,)
                npsi = psi_step(psi, L)
                if h in store:
                    w1, a1, b1 = store[h]
                    if same_tangle(npsi, dec(a1), dec(b1)): geo += 1
                    else:
                        noncoll.append(('.'.join(w2), w1))
                        print('NONGEOMETRIC', '.'.join(w2), '|', w1, flush=True)
                    continue
                na, nb = fgroup.act(L, a), fgroup.act(L, b)
                store[h] = ('.'.join(w2), enc(na), enc(nb))
                new.append((w2, na, nb, npsi, nv))
                if len(store) >= maxnodes: break
            if len(store) >= maxnodes: break
        frontier = new
        depth_counts.append(len(new))
        print('depth', d, 'new points', len(new), 'total', len(store), 'geometric re-hits', geo, 'nongeo', len(noncoll),
              'time', round(time.time() - t0, 1), flush=True)
        if len(store) >= maxnodes or not new: break
    res = {'prefix': prefix, 't': t, 'depth_counts': depth_counts, 'points': len(store), 'geometric_rehits': geo,
           'nongeometric': noncoll}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/orbit_d%d_s%d.json' % (maxdepth, seed), 'w'))
    print('RESULT', {k: v for k, v in res.items() if k != 'nongeometric'}, 'n_nongeo', len(noncoll))
    return res
if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
