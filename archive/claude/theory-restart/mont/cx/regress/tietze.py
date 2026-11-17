"""(b)-certificates: Wirtinger presentation of pi_1(S^3 - K) from the full symmetric diagram of a halfword (alex.symmetrize +
alex.diagram, the same diagram kauffman/alex use), reduced by VALID Tietze moves:
  ELIM  : a relator containing a generator x exactly once  u x^e v  ->  x := (u^-1 v^-1)^e ... substituted everywhere, x and
          the relator deleted;
  AUT   : a Nielsen change of generators by a Whitehead automorphism (applied to every relator);
  KILL  : a relator that is conjugate to a single generator z^{+-1} -> z := 1 everywhere, z and the relator deleted.
Success = one generator and every relator freely trivial, i.e. <a | >  => K is the unknot (Dehn's lemma).
certify(word) returns (True, steps) or (False, final presentation); replay(word, steps) re-derives the result from scratch."""
import sys, itertools
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a: out.pop()
        else: out.append(a)
    return out
def cyc(w):
    w = red(w)
    while len(w) >= 2 and w[0] == -w[-1]: w = w[1:-1]
    return w
def inv(w): return [-a for a in reversed(w)]
def wirtinger(word):
    full = alex.symmetrize(alex.parse(word))
    if full is None: return None
    cr = alex.diagram(full)
    if cr is None: return None
    if not cr: return 1, []
    uf = alex.UF()
    for x in cr: uf.union(x['ot'], x['ob'])
    arcs = {}
    def arc(e):
        r = uf.find(e)
        if r not in arcs: arcs[r] = len(arcs) + 1
        return arcs[r]
    rels = []
    for x in cr:
        ov = (1, -1) if x['ty'] == 'x' else (-1, -1)
        un = (-1, -1) if x['ty'] == 'x' else (1, -1)
        if not x['od']: ov = (-ov[0], -ov[1])
        if not x['ud']: un = (-un[0], -un[1])
        sign = 1 if ov[0] * un[1] - ov[1] * un[0] > 0 else -1
        o = arc(x['ot']); uin = arc(x['ut'] if x['ud'] else x['ub']); uout = arc(x['ub'] if x['ud'] else x['ut'])
        # sign > 0: uout = o uin o^-1 ; sign < 0: uout = o^-1 uin o   (matches alex.alex_matrix's Fox rows)
        r = [o, uin, -o, -uout] if sign > 0 else [-o, uin, o, -uout]
        rels.append(r)
    return len(arcs), rels
def subst(w, x, img):
    out = []
    for a in w:
        if abs(a) == x: out.extend(img if a > 0 else inv(img))
        else: out.append(a)
    return red(out)
def wh_autos(gens):
    L = [g for g in gens] + [-g for g in gens]
    autos = []
    for a in L:
        others = [y for y in L if abs(y) != abs(a)]
        for k in range(1, len(others) + 1):
            for S in itertools.combinations(others, k):
                A = set(S) | {a}; phi = {}
                for g in gens:
                    if g == abs(a): continue
                    xin, xiin = (g in A), (-g in A)
                    if xin and xiin: phi[g] = [-a, g, a]
                    elif xin: phi[g] = [g, a]
                    elif xiin: phi[g] = [-a, g]
                autos.append(phi)
    return autos
def apply_aut(phi, w):
    out = []
    for a in w:
        g = abs(a)
        img = phi.get(g, [g])
        out.extend(img if a > 0 else inv(img))
    return red(out)
def simplify(n, rels, steps, maxgens_wh=3, max_aut=300, max_total=4000):
    gens = set(range(1, n + 1))
    rels = [cyc(r) for r in rels]; rels = [r for r in rels if r]
    while True:
        changed = False
        # ELIM
        best = None
        for idx, r in enumerate(rels):
            cnt = {}
            for a in r: cnt[abs(a)] = cnt.get(abs(a), 0) + 1
            for x, c in cnt.items():
                if c == 1 and (best is None or len(r) < best[0]): best = (len(r), idx, x)
        if best is not None:
            _, idx, x = best; r = rels[idx]
            k = next(j for j, a in enumerate(r) if abs(a) == x)
            u, e, v = r[:k], (1 if r[k] > 0 else -1), r[k + 1:]
            img = red(inv(u) + inv(v)) if e > 0 else red(v + u)
            steps.append(('ELIM', idx, x, img))
            rels = [cyc(subst(rr, x, img)) for j, rr in enumerate(rels) if j != idx]
            rels = [rr for rr in rels if rr]; gens.discard(x); changed = True
            continue
        # KILL a relator conjugate to a single generator
        for idx, r in enumerate(rels):
            if len(r) == 1:
                z = abs(r[0]); steps.append(('KILL', idx, z))
                rels = [cyc([a for a in rr if abs(a) != z]) for j, rr in enumerate(rels) if j != idx]
                rels = [rr for rr in rels if rr]; gens.discard(z); changed = True; break
        if changed: continue
        # AUT: Whitehead-reduce the shortest relator towards length 1 (bounded effort)
        if not rels or len(gens) > maxgens_wh: break
        if sum(1 for st in steps if st[0] == 'AUT') >= max_aut or sum(len(r) for r in rels) > max_total: break
        G = sorted(gens); autos = wh_autos(G)
        done = False
        for idx in sorted(range(len(rels)), key=lambda j: len(rels[j])):
            r = rels[idx]
            best = None
            for phi in autos:
                r2 = cyc(apply_aut(phi, r))
                if len(r2) < len(r) and (best is None or len(r2) < len(best[1])): best = (phi, r2)
            if best is not None:
                phi = best[0]; steps.append(('AUT', {g: list(v) for g, v in phi.items()}))
                rels = [cyc(apply_aut(phi, rr)) for rr in rels]; rels = [rr for rr in rels if rr]
                done = True; break
        if not done: break
    return gens, rels
def certify(word):
    P = wirtinger(word)
    if P is None: return (False, 'not a knot diagram')
    n, rels = P
    steps = []
    gens, rels = simplify(n, rels, steps)
    ok = (len(gens) <= 1 and not rels)
    return (ok, steps) if ok else (False, (sorted(gens), rels[:3], [len(r) for r in rels]))
def replay(word, steps):
    n, rels = wirtinger(word)
    gens = set(range(1, n + 1)); rels = [cyc(r) for r in rels]; rels = [r for r in rels if r]
    for st in steps:
        if st[0] == 'ELIM':
            _, idx, x, img = st; r = rels[idx]
            assert sum(1 for a in r if abs(a) == x) == 1 and x not in [abs(a) for a in img]
            k = next(j for j, a in enumerate(r) if abs(a) == x)
            u, e, v = r[:k], (1 if r[k] > 0 else -1), r[k + 1:]
            assert img == (red(inv(u) + inv(v)) if e > 0 else red(v + u))
            rels = [cyc(subst(rr, x, img)) for j, rr in enumerate(rels) if j != idx]; gens.discard(x)
        elif st[0] == 'KILL':
            _, idx, z = st; assert len(rels[idx]) == 1 and abs(rels[idx][0]) == z
            rels = [cyc([a for a in rr if abs(a) != z]) for j, rr in enumerate(rels) if j != idx]; gens.discard(z)
        else:
            phi = {int(g): v for g, v in st[1].items()}
            rels = [cyc(apply_aut(phi, rr)) for rr in rels]
        rels = [rr for rr in rels if rr]
    return len(gens) <= 1 and not rels
if __name__ == '__main__':
    for w in sys.argv[1:]:
        ok, st = certify(w)
        print(w, 'CERTIFIED <a|>' if ok else 'not reduced', (len(st) if ok else st), 'replay', replay(w, st) if ok else '-')
