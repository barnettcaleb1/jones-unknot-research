"""validate_group.py -- independent check that the Wirtinger presentation used by the CHECKER (replay.wirtinger_presentation,
built from alex.diagram) and the PLAT presentation (wirtinger.plat: exact Artin action on free groups, Morse sweep) present
isomorphic groups: |Hom(pi, G)| must agree for G = S3, S4, A5.
Counting: both presentations are reduced by eliminations / relator multiplications (group-preserving).  Surviving Wirtinger
generators are meridians; surviving plat generators are meridians^(+-1) (sign = abelianisation exponent).  Since all
meridians are conjugate, Hom(pi, G) = disjoint union over conjugacy classes C of G of the assignments meridian -> C,
so |Hom| = sum_C #{assignments of the survivors into C (resp. C^-1) satisfying all reduced relators}.
usage: validate_group.py SEED COUNT NPROC OUT.json"""
import sys, json, time, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert')
import replay, wirtinger, diagram, reps, refs, tietze
from multiprocessing import Pool

GROUPS = {'S3': reps.sym_group(3), 'S4': reps.sym_group(4), 'A5': reps.alt_group(5)}
CL = {}
for name, gg in GROUPS.items():
    els = reps.group_closure(gg)
    seen = set(); classes = []
    for x in els:
        if x in seen: continue
        C = reps.conj_class(x, gg); seen.update(C); classes.append(C)
    CL[name] = classes


def count_homs(G, R, sgn, classes, cap=400000):
    """sgn[g] = +1 or -1 (image class C or C^-1)"""
    k = len(G); total = 0
    d = len(classes[0][0]); e = tuple(range(d))
    for C in classes:
        Ci = [reps.pinv(c) for c in C]
        opts = [C if sgn[g] > 0 else Ci for g in G]
        size = 1
        for o in opts: size *= len(o)
        if size > cap: return None
        for combo in itertools.product(*opts):
            img = dict(zip(G, combo))
            ok = True
            for r in R:
                acc = e
                for a in r:
                    x = img[abs(a)]
                    acc = reps.pmul(acc, x if a > 0 else reps.pinv(x))
                if acc != e: ok = False; break
            if ok: total += 1
    return total


def one(w):
    P1 = replay.wirtinger_presentation(w)
    full = diagram.morse_word(w)
    P2 = wirtinger.plat(full)
    ab2 = wirtinger.abelianisation(*P2)
    G1, R1, _ = reps.reduce_for_reps(*P1, time_budget=3)
    G2, R2, _ = reps.reduce_for_reps(*P2, time_budget=3)
    s1 = {g: 1 for g in G1}
    s2 = {g: ab2[g] for g in G2}
    if any(abs(v) != 1 for v in s2.values()): return {'w': w, 'skip': 'ab'}
    out = {'w': w, 'k1': len(G1), 'k2': len(G2), 'n': len(P1[0])}
    for name in ('S3', 'S4', 'A5'):
        a = count_homs(G1, R1, s1, CL[name]); b = count_homs(G2, R2, s2, CL[name])
        out[name] = (a, b)
    return out


if __name__ == '__main__':
    seed, count, nproc, outp = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    ws = refs.random_halfwords(seed, count, minlen=4, maxlen=14, width2_frac=0.5, w2len=(2, 10))
    t0 = time.time()
    with Pool(nproc) as P:
        rows = P.map(one, ws, chunksize=2)
    stats = {}
    for name in ('S3', 'S4', 'A5'):
        both = [r[name] for r in rows if name in r and r[name][0] is not None and r[name][1] is not None]
        stats[name] = {'compared': len(both), 'agree': sum(1 for a, b in both if a == b),
                       'nontrivial_counts': sum(1 for a, b in both if a == b and a > len(CL[name]) and True),
                       'distinct_values': sorted(set(a for a, b in both))[:20]}
    summ = {'count': len(rows), 'stats': stats, 'secs': round(time.time() - t0, 1)}
    json.dump({'summary': summ, 'rows': rows}, open(outp, 'w'))
    print(json.dumps(summ))
    for r in rows:
        for name in ('S3', 'S4', 'A5'):
            if name in r and r[name][0] is not None and r[name][1] is not None and r[name][0] != r[name][1]:
                print('MISMATCH', r)
