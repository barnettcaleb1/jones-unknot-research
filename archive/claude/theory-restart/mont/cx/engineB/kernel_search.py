"""E1': direct projective-kernel screen.  BFS over the type-B_4 Artin group, elements deduplicated EXACTLY (images of the five
free generators under the Artin action on F_5); hash of rho_2(g) projectively via [rho_2(g) r] for a random vector r mod p.
Two distinct elements with the same hash => rho_2(g1^-1 g2) has r as eigenvector => (generically) scalar: kernel candidate.
usage: kernel_search.py MAXDEPTH MAXNODES SEED"""
import sys, random, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import mitm, rho2, fgroup
P = mitm.P; LET = mitm.LET; INV = mitm.INV
def main(maxdepth, maxnodes, seed):
    rnd = random.Random(seed); t = rnd.randrange(2, P - 1)
    MT, VT, PHIT = rho2.normalised()
    M = {L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}
    r = [rnd.randrange(P) for _ in range(9)]
    gens = tuple((j + 1,) for j in range(5))
    seen = {gens}; hashes = {mitm.proj(r): ()}
    frontier = [((), gens, r)]; cands = []; t0 = time.time(); counts = [1]
    for d in range(1, maxdepth + 1):
        new = []
        for word, key, v in frontier:
            last = word[-1] if word else None
            for L in LET:
                if last and INV[L] == last: continue
                nk = tuple(fgroup.act(L, w) for w in key)
                if nk in seen: continue
                seen.add(nk)
                nv = mitm.mv(M[L], v); h = mitm.proj(nv); w2 = word + (L,)
                if h in hashes:
                    cands.append(('.'.join(w2), '.'.join(hashes[h])))
                    print('KERNEL-CANDIDATE', '.'.join(w2), '|', '.'.join(hashes[h]), flush=True)
                else: hashes[h] = w2
                new.append((w2, nk, nv))
                if len(seen) >= maxnodes: break
            if len(seen) >= maxnodes: break
        frontier = new; counts.append(len(new))
        print('depth', d, 'new elements', len(new), 'total', len(seen), 'candidates', len(cands), 'time', round(time.time() - t0, 1), flush=True)
        if len(seen) >= maxnodes or not new: break
    res = {'counts': counts, 'elements': len(seen), 'candidates': cands}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/kernel_d%d.json' % maxdepth, 'w'))
    print('RESULT', {'counts': counts, 'elements': len(seen), 'ncand': len(cands)}, flush=True)
if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
