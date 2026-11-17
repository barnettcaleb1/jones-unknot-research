"""E4: exhaustive meet-in-the-middle screen of ALL width-two theta-curves  s.l1.l1.G1.G2.u2.u2  with |G1| <= D1, |G2| <= D2
(hence every width-two braid word of length <= D1 + D2), deduplicated by Hilden-type cosets on both sides
(projective point of the top vector rho(G1) v at a generic t; projective point of the bottom covector phi rho(G2)).
Filter: J = 1 forces J_raw(zeta) = +-zeta^k at every root of unity; we test zeta_7 (no a-priori reason to be a unit) and
zeta_10 (= the V_K(zeta_5) gate), mod a prime p = 1 mod 2520.  Every survivor is recomputed exactly (lp.J) and K certified.
usage: mitm.py D1 D2 SEED"""
import sys, random, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/orig')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import rho2, lp
LET = ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
def is_prime(n):
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0: return n == p
    d = n - 1; s = 0
    while d % 2 == 0: d //= 2; s += 1
    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True
def find_prime():
    k = (1 << 61) // 2520
    while True:
        p = 2520 * k + 1
        if is_prime(p): return p
        k -= 1
P = find_prime()
def root_of_unity(m):
    # element of exact order m
    for g in range(2, 1000):
        z = pow(g, (P - 1) // m, P)
        if all(pow(z, m // q, P) != 1 for q in [2, 3, 5, 7] if m % q == 0): return z
    raise ValueError
def evt(poly, t): return sum(c * pow(t, e % (P - 1), P) for e, c in poly.items()) % P
def proj(v):
    for x in v:
        if x:
            ix = pow(x, P - 2, P)
            return tuple((y * ix) % P for y in v)
    return None
def mv(M, v): return [sum(a * b for a, b in zip(row, v)) % P for row in M]
def vm(w, M):
    n = len(w)
    return [sum(w[i] * M[i][j] for i in range(n)) % P for j in range(n)]
ROLE_BOT = {0: 'v', 1: 'u', 2: 'u', 3: 'c'}   # u2.u2 closure: leg0 -> v_bot, legs 1-2 cupped, leg 3 -> c
def top_class(word):
    pos = rho2.perm_of(list(word))
    m = {pos[0]: pos[1], pos[1]: pos[0], pos[2]: pos[3], pos[3]: pos[2]}
    return tuple(m[i] for i in range(4))
def bot_class(word):
    pos = rho2.perm_of(list(word))   # interface position p -> bottom position pos[p]
    inv = {pos[p]: p for p in range(4)}
    role = {}
    for p in range(4):
        b = pos[p]
        if b in (1, 2): role[p] = ('u', inv[3 - b])     # partner of bottom 1 is 2 and vice versa
        else: role[p] = (ROLE_BOT[b], None)
    return tuple(role[p] for p in range(4))
def knot_ok(tc, bc):
    cpos = next(p for p in range(4) if bc[p][0] == 'c')
    j = cpos; seen = 0
    while True:
        q = tc[j]; seen += 2          # up leg j, across the cap to q, down leg q
        r, partner = bc[q]
        if r == 'v': return seen == 4
        if r == 'c': return False
        j = partner
        if seen > 8: return False
def bfs(M_list, start_list, depth, side, gen_index=0):
    """M_list: list of matrix dicts at several t values; start_list: start vectors (or covectors) at those t values.
    side 'top': extend word at the END, v -> M[L] v ; side 'bot': extend word at the FRONT, w -> w M[L].
    dedupe by projective point at t-index gen_index."""
    nodes = [((), start_list)]
    seen = {proj(start_list[gen_index])}
    frontier = nodes[:]
    for d in range(1, depth + 1):
        new = []
        for word, vecs in frontier:
            if side == 'top':
                last = word[-1] if word else None
            else:
                last = word[0] if word else None
            for L in LET:
                if last and INV[L] == last: continue
                if side == 'top':
                    nv = [mv(M[L], v) for M, v in zip(M_list, vecs)]
                    w2 = word + (L,)
                else:
                    nv = [vm(v, M[L]) for M, v in zip(M_list, vecs)]
                    w2 = (L,) + word
                h = proj(nv[gen_index])
                if h in seen: continue
                seen.add(h)
                new.append((w2, nv))
        nodes.extend(new); frontier = new
    return nodes
def main(D1, D2, seed):
    rnd = random.Random(seed)
    tg = rnd.randrange(2, P - 1)
    z7 = root_of_unity(7); z10 = root_of_unity(10)
    MT, VT, PHIT = rho2.normalised()
    ts = [tg, z7, z10]
    Ms = [{L: [[evt(x, t) for x in row] for row in m] for L, m in MT.items()} for t in ts]
    V = [[evt(x, t) for x in VT['l1.l1']] for t in ts]
    # covector includes the normalisation t^2/(1+t)^4 so that pairing = J_raw (up to the units of u, w)
    PH = []
    for t in ts:
        c = t * t % P * pow(pow(1 + t, 4, P), P - 2, P) % P
        PH.append([evt(x, t) * c % P for x in PHIT['u2.u2']])
    t0 = time.time()
    tops = bfs(Ms, V, D1, 'top')
    bots = bfs(Ms, PH, D2, 'bot')
    print('tops', len(tops), 'bottoms', len(bots), 'time', round(time.time() - t0, 1), flush=True)
    U7 = set(pow(z7, k, P) for k in range(7)) | set((-pow(z7, k, P)) % P for k in range(7))
    U10 = set(pow(z10, k, P) for k in range(10))
    # group by class
    from collections import defaultdict
    TG = defaultdict(list); BG = defaultdict(list)
    for w, vecs in tops: TG[top_class(w)].append((w, vecs[1], vecs[2]))
    for w, vecs in bots: BG[bot_class(w)].append((w, vecs[1], vecs[2]))
    npairs = 0; pass7 = []; t1 = time.time()
    for tc, tl in TG.items():
        for bc, bl in BG.items():
            if not knot_ok(tc, bc): continue
            for (wb, b7, b10) in bl:
                b0, b1, b2, b3, b4, b5, b6, b7_, b8 = b7
                for (wt, u7, u10) in tl:
                    s = (b0 * u7[0] + b1 * u7[1] + b2 * u7[2] + b3 * u7[3] + b4 * u7[4] + b5 * u7[5] + b6 * u7[6] + b7_ * u7[7] + b8 * u7[8]) % P
                    if s in U7:
                        s10 = sum(x * y for x, y in zip(b10, u10)) % P
                        pass7.append((wt, wb, s10 in U10))
                npairs += len(tl)
    print('pairs (knots)', npairs, 'pass zeta7', len(pass7), 'pass both', sum(1 for x in pass7 if x[2]), 'time', round(time.time() - t1, 1), flush=True)
    # verification of survivors: certify K first (modular V_K, det, Delta(2), Delta(3)); exact J only when K is nontrivial
    import kcert
    stats = {'presumed_unknot(V=1,det=D2=D3=1)': 0, 'K_nontrivial_J!=1(near miss)': 0, 'HIT': 0, 'unknot_J_checked': 0, 'unknot_J_bad': 0}
    near = []
    for idx, (wt, wb, p10) in enumerate(pass7):
        W = list(wt) + list(wb)
        hw = rho2.halfword('l1.l1', W, 'u2.u2')
        st, why = kcert.certify(hw)
        if st == 'V=1,Delta=1':
            stats['presumed_unknot(V=1,det=D2=D3=1)'] += 1
            if idx % 50 == 0:
                stats['unknot_J_checked'] += 1
                if lp.J(hw) != {0: 1}: stats['unknot_J_bad'] += 1
            continue
        J = lp.J(hw)
        if J == {0: 1}:
            stats['HIT'] += 1
            print('HIT-CANDIDATE', hw, why, flush=True)
            open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/orig_HIT_CANDIDATES.txt', 'a').write(hw + '\t' + str(why) + '\n')
        else:
            stats['K_nontrivial_J!=1(near miss)'] += 1
            if len(near) < 200: near.append((hw, sorted(J.items()), p10, lp.a2(J)))
    res = {'D1': D1, 'D2': D2, 'P': P, 'tops': len(tops), 'bottoms': len(bots), 'knot_pairs': npairs, 'pass7': len(pass7), 'stats': stats,
           'near_misses_zeta7_unit': near}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/regress/out/orig_mitm_%d_%d.json' % (D1, D2), 'w'))
    print('RESULT', {k: v for k, v in res.items() if k != 'near_misses_zeta7_unit'}, flush=True)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
