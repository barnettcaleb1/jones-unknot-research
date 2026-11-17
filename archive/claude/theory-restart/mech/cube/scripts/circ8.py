"""Is theta(2,2,2) a bipartite circle graph (4 inside + 4 outside chords)? brute force."""
import itertools
def nc_matchings(pts):
    if not pts: yield []; return
    a = pts[0]
    for k in range(1, len(pts), 2):
        b = pts[k]
        for m1 in nc_matchings(pts[1:k]):
            for m2 in nc_matchings(pts[k + 1:]):
                yield [(a, b)] + m1 + m2
def cross(c, d):
    (a, b), (x, y) = c, d
    return (a < x < b) != (a < y < b)
cnt = 0; hits = []
allp = list(range(16))
for S in itertools.combinations(allp, 8):
    if 0 not in S: continue          # symmetry: point 0 inside
    comp = [p for p in allp if p not in S]
    ins = list(nc_matchings(list(S))); outs = list(nc_matchings(comp))
    for mi in ins:
        for mo in outs:
            M = [[cross(c, d) for d in mo] for c in mi]
            rd = sorted(sum(r) for r in M); cd = sorted(sum(M[i][j] for i in range(4)) for j in range(4))
            if rd != [2, 2, 2, 3] or cd != [2, 2, 2, 3]: continue
            i3 = [i for i in range(4) if sum(M[i]) == 3][0]; j3 = [j for j in range(4) if sum(M[i][j] for i in range(4)) == 3][0]
            if M[i3][j3]: continue
            # remaining: rows != i3 each adjacent to j3 and exactly one other col, a perfect matching
            ok = True; used = set()
            for i in range(4):
                if i == i3: continue
                if not M[i][j3]: ok = False; break
                others = [j for j in range(4) if j != j3 and M[i][j]]
                if len(others) != 1 or others[0] in used: ok = False; break
                used.add(others[0])
            if ok:
                cnt += 1
                if len(hits) < 3: hits.append((mi, mo))
print('realisations of theta(2,2,2) with point 0 inside:', cnt); print(hits)
