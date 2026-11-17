"""Covector-side (bottom) coincidence search.  BFS over the projective orbit [phi rho(U)] (U extended at the FRONT), deduplicated
projectively.  A re-hit U2 of a class first reached by U1 means phi rho(U2) = lambda phi rho(U1): then the knot
s.l1.l1.(U1^-1).U2.u2.u2 has J = lambda = unit (exactly, by construction).  We certify that knot (kcert); a nontrivial K is a HIT.
Second test: for 3 random tops V (vectors rho(V) v), compare V_K of V.U1 and V.U2 mod p (geometric equivalence of the
bottoms predicts equality).  This also validates the bottom deduplication used by mitm.py.
usage: bottom_orbit.py MAXDEPTH MAXNODES SEED"""
import sys, random, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import mitm, rho2, kcert
P = mitm.P
LET = mitm.LET; INV = mitm.INV
def main(maxdepth, maxnodes, seed):
    rnd = random.Random(seed)
    t = rnd.randrange(2, P - 1)
    MT, VT, PHIT = rho2.normalised()
    M = {L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}
    c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
    ph = [mitm.evt(x, t) * c % P for x in PHIT['u2.u2']]
    store = {mitm.proj(ph): ()}
    frontier = [((), ph)]
    # random tops for test 2
    tops = []
    while len(tops) < 3:
        V = tuple(rnd.choice(LET) for _ in range(rnd.randint(3, 6)))
        tops.append(V)
    stats = {'rehits': 0, 'U1^-1U2 unknot': 0, 'U1^-1U2 not a knot': 0, 'HIT': 0, 'VK-mismatch': 0, 'VK-tests': 0}
    t0 = time.time(); counts = [1]; hits = []; mism = []
    for d in range(1, maxdepth + 1):
        new = []
        for word, w in frontier:
            first = word[0] if word else None
            for L in LET:
                if first and INV[L] == first: continue
                nw = mitm.vm(w, M[L]); h = mitm.proj(nw); w2 = (L,) + word
                if h in store:
                    stats['rehits'] += 1
                    U1 = store[h]
                    Wt = [INV[x] for x in reversed(U1)] + list(w2)
                    if not rho2.is_knot('l1.l1', Wt, 'u2.u2'): stats['U1^-1U2 not a knot'] += 1
                    else:
                        st, why = kcert.certify(rho2.halfword('l1.l1', Wt, 'u2.u2'))
                        if st == 'V=1,Delta=1': stats['U1^-1U2 unknot'] += 1
                        else:
                            stats['HIT'] += 1; hw = rho2.halfword('l1.l1', Wt, 'u2.u2'); hits.append(hw)
                            print('HIT-CANDIDATE', hw, why, flush=True)
                            open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/HIT_CANDIDATES.txt', 'a').write(hw + '\tbottom-collision ' + str(why) + '\n')
                    if stats['rehits'] % 7 == 0:
                        for V in tops:
                            W1 = list(V) + list(U1); W2 = list(V) + list(w2)
                            if not (rho2.is_knot('l1.l1', W1, 'u2.u2') and rho2.is_knot('l1.l1', W2, 'u2.u2')): continue
                            stats['VK-tests'] += 1
                            a = kcert.VK_mod(rho2.halfword('l1.l1', W1, 'u2.u2'), 1234567)
                            b = kcert.VK_mod(rho2.halfword('l1.l1', W2, 'u2.u2'), 1234567)
                            if a != b:
                                stats['VK-mismatch'] += 1
                                if len(mism) < 20: mism.append(('.'.join(U1), '.'.join(w2), '.'.join(V)))
                    continue
                store[h] = w2
                new.append((w2, nw))
                if len(store) >= maxnodes: break
            if len(store) >= maxnodes: break
        frontier = new; counts.append(len(new))
        print('depth', d, 'new', len(new), 'total', len(store), stats, 'time', round(time.time() - t0, 1), flush=True)
        if len(store) >= maxnodes or not new: break
    res = {'counts': counts, 'points': len(store), 'stats': stats, 'hits': hits, 'VK_mismatch_examples': mism}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/bottom_orbit_d%d.json' % maxdepth, 'w'))
    print('RESULT', res, flush=True)
if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
