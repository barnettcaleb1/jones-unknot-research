"""S1 regeneration: reproduces engineB/bottom_orbit.py (covector-side BFS, letters LET order, extension at the FRONT,
projective dedup mod P = mitm.P at a random t) WITHOUT certification, recording every re-hit (U1 = stored representative,
U2 = new word) with its depth.  The closure word of a re-hit is s.l1.l1.U1^-1.U2.u2.u2 (as in bottom_orbit.py).
Reproduces: engineB/bottom_orbit.py MAXDEPTH=8 (counts 1,4,18,74,296,1196,4842,19658,79952; re-hits d7 18,930, d8 76,584).
usage: s1_regen.py MAXDEPTH SEED"""
import sys, random, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import mitm, rho2
P = mitm.P; LET = mitm.LET; INV = mitm.INV
def main(maxdepth, seed):
    rnd = random.Random(seed)
    t = rnd.randrange(2, P - 1)
    MT, VT, PHIT = rho2.normalised()
    M = {L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}
    c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
    ph = [mitm.evt(x, t) * c % P for x in PHIT['u2.u2']]
    store = {mitm.proj(ph): ()}
    frontier = [((), ph)]
    rehits = []; counts = [1]; t0 = time.time()
    for d in range(1, maxdepth + 1):
        new = []; nre = 0
        for word, w in frontier:
            first = word[0] if word else None
            for L in LET:
                if first and INV[L] == first: continue
                nw = mitm.vm(w, M[L]); h = mitm.proj(nw); w2 = (L,) + word
                if h in store:
                    U1 = store[h]
                    rehits.append((d, '.'.join(U1), '.'.join(w2))); nre += 1
                    continue
                store[h] = w2
                new.append((w2, nw))
        frontier = new; counts.append(len(new))
        print('depth', d, 'new', len(new), 'total', len(store), 'rehits', nre, 'time', round(time.time() - t0, 1), flush=True)
    return counts, rehits, store
if __name__ == '__main__':
    D = int(sys.argv[1]); seed = int(sys.argv[2])
    counts, rehits, store = main(D, seed)
    out = '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/data/s1_rehits_d%d_s%d.json' % (D, seed)
    json.dump({'counts': counts, 'rehits': rehits, 'n_classes': len(store),
               'reps': ['.'.join(w) for w in store.values()]}, open(out, 'w'))
    print('saved', out, 'rehits', len(rehits))
