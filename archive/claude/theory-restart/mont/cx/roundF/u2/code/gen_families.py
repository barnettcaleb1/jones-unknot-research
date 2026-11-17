"""gen_families.py -- the explicit J = 1 families of engineB section 2 (regenerated here; engineB code imported read-only).
 TOP re-hits (line stabilisers of the cap vector): BFS over words g (first letter acts first), projective point of
   rho_2(g) v mod p at a random t; a re-hit g2 of the class of g1 gives W = g2 . g1^-1 with rho(W) v = lambda v, so
   s.l1.l1.W.u2.u2 has J a unit; engineB showed (exact Artin-action test, depth <= 10) that all such re-hits are the
   SAME trivial tangle, so these knots are unknots geometrically (that argument is engineB's; here they are test input).
 BOTTOM re-hits (covector side): phi rho(U2) = lambda phi rho(U1) gives s.l1.l1.U1^-1.U2.u2.u2 with J a unit
   (engineB: 'presumed unknots', V = Delta = 1).
 CODEX family: s.l1.l1.x2.x1.x1^(2m).y3^(2m).x1.u2.u2 (msgs/20261117-020642-codex.md), J = 1 for every m.
usage: gen_families.py DEPTH_TOP DEPTH_BOT MAXPER SEED OUT.json"""
import sys, json, random
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import mitm, rho2, lp
P = mitm.P; LET = mitm.LET; INV = mitm.INV


def inv_word(w): return [INV[x] for x in reversed(w)]


def hw(W): return rho2.halfword('l1.l1', list(W), 'u2.u2')


def top_rehits(depth, maxn, t):
    MT, VT, PHIT = rho2.normalised()
    M = {L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}
    v = [mitm.evt(x, t) for x in VT['l1.l1']]
    store = {mitm.proj(v): ()}; frontier = [((), v)]; out = []
    for d in range(1, depth + 1):
        new = []
        for word, vec in frontier:
            last = word[-1] if word else None
            for L in LET:
                if last and INV[L] == last: continue
                nv = mitm.mv(M[L], vec); h = mitm.proj(nv); w2 = word + (L,)
                if h in store:
                    g1 = store[h]
                    W = list(w2) + inv_word(g1)
                    if rho2.is_knot('l1.l1', W, 'u2.u2'): out.append(hw(W))
                    continue
                store[h] = w2; new.append((w2, nv))
        frontier = new
    return out


def bottom_rehits(depth, maxn, t):
    MT, VT, PHIT = rho2.normalised()
    M = {L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}
    c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
    ph = [mitm.evt(x, t) * c % P for x in PHIT['u2.u2']]
    store = {mitm.proj(ph): ()}; frontier = [((), ph)]; out = []
    for d in range(1, depth + 1):
        new = []
        for word, w in frontier:
            first = word[0] if word else None
            for L in LET:
                if first and INV[L] == first: continue
                nw = mitm.vm(w, M[L]); h = mitm.proj(nw); w2 = (L,) + word
                if h in store:
                    U1 = store[h]
                    W = inv_word(U1) + list(w2)
                    if rho2.is_knot('l1.l1', W, 'u2.u2'): out.append(hw(W))
                    continue
                store[h] = w2; new.append((w2, nw))
        frontier = new
    return out


def codex_family(mrange):
    out = []
    for m in mrange:
        mid = (['x1'] * (2 * m) + ['y3'] * (2 * m)) if m >= 0 else (['y1'] * (-2 * m) + ['x3'] * (-2 * m))
        out.append((m, hw(['x2', 'x1'] + mid + ['x1'])))
    return out


if __name__ == '__main__':
    dt, db, maxper, seed, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    rnd = random.Random(seed); t = rnd.randrange(2, P - 1)
    T = top_rehits(dt, maxper, t); B = bottom_rehits(db, maxper, t)
    # keep the longest words (most crossings) but sample across lengths
    def pick(L):
        L = sorted(set(L), key=lambda w: (-len(w.split('.')), w))
        rnd.shuffle(L)
        L = sorted(L, key=lambda w: -len(w.split('.')))
        return L[:maxper]
    T2, B2 = pick(T), pick(B)
    CF = codex_family(range(-10, 11))
    # sanity: J = 1 on a sample (exact lp.J)
    samp = rnd.sample(T2, min(40, len(T2))) + rnd.sample(B2, min(40, len(B2))) + [w for m, w in CF]
    bad = [w for w in samp if lp.J(w) != {0: 1}]
    json.dump({'top': T2, 'bottom': B2, 'codex': CF, 'n_top_all': len(T), 'n_bot_all': len(B), 'J_sample_bad': bad}, open(outp, 'w'))
    print('top rehit knots', len(T), 'kept', len(T2), '| bottom', len(B), 'kept', len(B2), '| codex', len(CF), '| J!=1 in sample', len(bad))
