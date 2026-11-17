"""geo_bfs.py -- GEOMETRIC re-run of engineB's MITM deduplication (both sides) to depth D, with EXACT checks.
TOPS (words extended at the end, vector rho_2(g) f0) and BOTTOMS (extended at the front, covector PHI rho_2(U)):
  * key = projective point at a random t mod P (engineB/mitm.py arithmetic, imported read-only);
  * a word whose key is already present is PRUNED only if it is (i) GEOMETRICALLY equal to a stored word of that bucket
    (full-picture kernel test, tangle_kernel.py) AND (ii) EXACTLY projectively equal to it (exact Laurent-polynomial
    vectors from rho2.normalised(); ratio checked to be a unit +-t^k);  otherwise it is stored as a NEW class and expanded.
  * Induction (run/REPORT.md section 5): every freely reduced word of length <= D is then geometrically AND exactly
    projectively equal to a stored word, so a junction G1.G2 has the same J (up to a unit) and the same knot as a stored pair.
Output: per side, classes per depth, re-hits (geometric / non-geometric), the MITM representative of every projective class
(first word reaching it in mitm.bfs order) and, for every bucket with several geometric classes, the extra ('missed') words.
usage: geo_bfs.py D OUT.json"""
import sys, os, json, time, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tangle_kernel as TK
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineB')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont')
import mitm, rho2
P = mitm.P; LET = mitm.LET; INV = mitm.INV
MT, VT, PHIT = rho2.normalised()
def padd(p, q, c=1):
    for e, v in q.items():
        nv = p.get(e, 0) + c * v
        if nv: p[e] = nv
        elif e in p: del p[e]
def pmul(p, q):
    r = {}
    for e, c in p.items():
        for f, d in q.items():
            r[e + f] = r.get(e + f, 0) + c * d
    return {e: c for e, c in r.items() if c}
def ex_mv(M, v):           # exact M v
    out = []
    for row in M:
        acc = {}
        for a, b in zip(row, v):
            if a and b: padd(acc, pmul(a, b))
        out.append(acc)
    return out
def ex_vm(w, M):           # exact w M
    n = len(w); out = []
    for j in range(n):
        acc = {}
        for i in range(n):
            if w[i] and M[i][j]: padd(acc, pmul(w[i], M[i][j]))
        out.append(acc)
    return out
def exact_proportional_unit(v1, v2):
    """True iff v2 = +-t^k v1 exactly"""
    i = next((k for k, x in enumerate(v1) if x), None)
    if i is None or not v2[i]: return False
    a, b = v1[i], v2[i]
    # candidate ratio from leading terms
    ea, eb = max(a), max(b)
    if b[eb] not in (a[ea], -a[ea]): return False
    s = b[eb] // a[ea]; k = eb - ea
    for x, y in zip(v1, v2):
        if {e + k: s * c for e, c in x.items()} != y: return False
    return True
def run_side(side, D, t):
    M_t = {L: [[mitm.evt(x, t) for x in row] for row in m] for L, m in MT.items()}
    if side == 'top':
        start_ex = [dict(x) for x in VT['l1.l1']]
        start_t = [mitm.evt(x, t) for x in VT['l1.l1']]
    else:
        start_ex = [dict(x) for x in PHIT['u2.u2']]
        start_t = [mitm.evt(x, t) for x in PHIT['u2.u2']]
    # (1) the MITM's own BFS (mitm.bfs logic): representative of every projective class
    mitm_rep = {mitm.proj(start_t): ()}
    frontier = [((), start_t)]
    for d in range(1, D + 1):
        new = []
        for word, v in frontier:
            last = (word[-1] if side == 'top' else word[0]) if word else None
            for L in LET:
                if last and INV[L] == last: continue
                if side == 'top': nv = mitm.mv(M_t[L], v); w2 = word + (L,)
                else: nv = mitm.vm(v, M_t[L]); w2 = (L,) + word
                h = mitm.proj(nv)
                if h in mitm_rep: continue
                mitm_rep[h] = w2; new.append((w2, nv))
        frontier = new
    # (2) geometric + exact BFS
    same = TK.same_top if side == 'top' else TK.same_bottom
    buckets = {mitm.proj(start_t): [((), start_ex)]}
    frontier = [((), start_t, start_ex)]
    stats = {'classes_per_depth': [1], 'rehits_geometric': 0, 'rehits_NONGEOMETRIC_new_class': 0,
             'rehits_hash_equal_but_NOT_exact_new_class': 0}
    for d in range(1, D + 1):
        new = []
        for word, v, vex in frontier:
            last = (word[-1] if side == 'top' else word[0]) if word else None
            for L in LET:
                if last and INV[L] == last: continue
                if side == 'top':
                    nv = mitm.mv(M_t[L], v); w2 = word + (L,); nex = ex_mv(MT[L], vex)
                else:
                    nv = mitm.vm(v, M_t[L]); w2 = (L,) + word; nex = ex_vm(vex, MT[L])
                h = mitm.proj(nv)
                if h in buckets:
                    pruned = False; any_exact = False
                    for (sw, sex) in buckets[h]:
                        if exact_proportional_unit(sex, nex):
                            any_exact = True
                            if same(list(sw), list(w2)): pruned = True; break
                    if pruned: stats['rehits_geometric'] += 1; continue
                    if any_exact: stats['rehits_NONGEOMETRIC_new_class'] += 1
                    else: stats['rehits_hash_equal_but_NOT_exact_new_class'] += 1
                    buckets[h].append((w2, nex)); new.append((w2, nv, nex))
                else:
                    buckets[h] = [(w2, nex)]; new.append((w2, nv, nex))
        frontier = new; stats['classes_per_depth'].append(len(new))
        print(side, 'depth', d, 'new classes', len(new), stats, flush=True)
    # (3) for each bucket: geometric class of the MITM representative; the other classes are MISSED by the MITM
    missed = []
    for h, lst in buckets.items():
        rep = mitm_rep.get(h)
        if rep is None: missed.append({'key_missing_in_mitm': True, 'words': ['.'.join(w) for w, _ in lst]}); continue
        if len(lst) == 1: continue
        repcls = [i for i, (w, _) in enumerate(lst) if same(list(w), list(rep))]
        for i, (w, _) in enumerate(lst):
            if i not in repcls: missed.append({'mitm_rep': '.'.join(rep), 'missed_word': '.'.join(w), 'depth': len(w)})
    stats['projective_classes'] = len(buckets); stats['geometric_classes'] = sum(len(l) for l in buckets.values())
    stats['mitm_classes'] = len(mitm_rep); stats['missed_geometric_classes'] = len(missed)
    return stats, missed, {('.'.join(w)): ('.'.join(mitm_rep[h]) if h in mitm_rep else None) for h, lst in buckets.items() for w, _ in lst}
if __name__ == '__main__':
    D, outp = int(sys.argv[1]), sys.argv[2]
    t = random.Random(3).randrange(2, P - 1)
    res = {'D': D}
    for side in ('top', 'bottom'):
        t0 = time.time()
        st, missed, word2rep = run_side(side, D, t)
        st['secs'] = round(time.time() - t0, 1)
        res[side] = {'stats': st, 'missed': missed}
        print(side, json.dumps(st), flush=True)
    json.dump(res, open(outp, 'w'), indent=1)
