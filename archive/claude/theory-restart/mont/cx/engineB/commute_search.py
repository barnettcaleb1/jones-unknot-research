"""E1: Bigelow-style commuting-image search.  For g0 in {x1 (half twist sigma_1), x0 (axis full twist tau)} enumerate the
conjugates C_u = rho(u) rho(g0) rho(u)^-1 (u = BFS words; distinct conjugates <-> distinct arcs/curves), deduplicated by the
exact matrix (hash of C_u r for a random r mod p).  Test [C_u, rho(s)] = 0 for s in {x0,x1,x2,x3}.  A commuting pair whose
group elements do NOT commute (exact Artin action on F_5) gives a commutator in ker rho_2 (inserted anywhere: J unchanged).
usage: commute_search.py G0 MAXDEPTH MAXNODES SEED"""
import sys, random, time, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
import rho2, fgroup
P = (1 << 61) - 1
def evt(poly, t):
    return sum(c * pow(t, e % (P - 1), P) for e, c in poly.items()) % P
LET = ['x0', 'y0', 'x1', 'y1', 'x2', 'y2', 'x3', 'y3']
INV = {'x0': 'y0', 'y0': 'x0', 'x1': 'y1', 'y1': 'x1', 'x2': 'y2', 'y2': 'x2', 'x3': 'y3', 'y3': 'x3'}
def mm(A, B):
    n = len(A)
    Bt = list(zip(*B))
    return [[sum(a * b for a, b in zip(A[i], Bt[j])) % P for j in range(n)] for i in range(n)]
def mv(M, v): return [sum(a * b for a, b in zip(row, v)) % P for row in M]
def main(g0, maxdepth, maxnodes, seed):
    rnd = random.Random(seed)
    t = rnd.randrange(2, P - 1)
    MT, VT, PHIT = rho2.normalised()
    M = {L: [[evt(x, t) for x in row] for row in m] for L, m in MT.items()}
    r = [rnd.randrange(P) for _ in range(9)]
    C0 = M[g0]
    seen = {tuple(mv(C0, r))}
    frontier = [((), C0)]
    hits = []; tests = 0; t0 = time.time(); counts = [1]
    S = ['x0', 'x1', 'x2', 'x3']
    Sr = {s: mv(M[s], r) for s in S}
    def check(word, C):
        nonlocal tests
        for s in S:
            tests += 1
            a = mv(C, Sr[s]); b = mv(M[s], mv(C, r))
            if a == b:
                # full check
                if mm(C, M[s]) == mm(M[s], C):
                    c = list(fgroup.inv_word(word)) if False else None
                    cw = [INV[x] for x in reversed(word)] + [g0] + list(word)
                    comm_group = fgroup.group_key(cw + [s]) == fgroup.group_key([s] + cw)
                    if not comm_group:
                        hits.append(('.'.join(cw), s))
                        print('KERNEL-CANDIDATE', '.'.join(cw), 'with', s, flush=True)
                    return comm_group
        return None
    ncomm_geo = 0
    for d in range(1, maxdepth + 1):
        new = []
        for word, C in frontier:
            last = word[-1] if word else None
            for L in LET:
                if last and INV[L] == last: continue
                Li = INV[L]
                # C' = M[L] C M[L]^-1
                h = tuple(mv(M[L], mv(C, mv(M[Li], r))))
                if h in seen: continue
                seen.add(h)
                C2 = mm(M[L], mm(C, M[Li]))
                w2 = word + (L,)
                res = check(w2, C2)
                if res: ncomm_geo += 1
                new.append((w2, C2))
                if len(seen) >= maxnodes: break
            if len(seen) >= maxnodes: break
        frontier = new; counts.append(len(new))
        print('depth', d, 'new conjugates', len(new), 'total', len(seen), 'geometric commuting', ncomm_geo, 'kernel cands', len(hits),
              'time', round(time.time() - t0, 1), flush=True)
        if len(seen) >= maxnodes or not new: break
    res = {'g0': g0, 't': t, 'counts': counts, 'conjugates': len(seen), 'commuting_geometric': ncomm_geo, 'kernel_candidates': hits}
    json.dump(res, open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB/out/commute_%s_d%d.json' % (g0, maxdepth), 'w'))
    print('RESULT', res if len(hits) < 20 else {k: v for k, v in res.items() if k != 'kernel_candidates'})
if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
