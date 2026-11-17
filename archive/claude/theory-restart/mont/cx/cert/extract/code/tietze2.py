"""Tietze with relator shortening: besides eliminating a generator that occurs once in a relator, replace a relator r_i by
cyc(rot(r_i) * rot(r_j^e)) when this is shorter (a product of r_i with a conjugate of r_j^(+-1): a valid Tietze move, r_j is kept).
Log entries: ('elim', canon(r), g) and ('mul', canon(r_i), canon(r_j), e, a, b) with new = cyc(r_i[a:]+r_i[:a] + s[b:]+s[:b]),
s = r_j if e = 1 else inv(r_j), where r_i, r_j are the stored canonical forms.  replay2() re-checks every step."""
import sys
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/extract/code')
from tietze import red, inv, cyc, canon, subst, presentation, presentation_rev
def best_mul(ri, rj):
    """best (new, e, a, b) with len(new) < len(ri), maximising cancellation; ri, rj cyclically reduced"""
    best = None
    for e, s in ((1, rj), (-1, inv(rj))):
        n, m = len(ri), len(s)
        if m == 0: continue
        # cancellation between the end of rot(ri, a) and the start of rot(s, b): ri[a-1-k] == -s[(b+k) % m]
        for a in range(n):
            for b in range(m):
                k = 0
                while k < min(n, m) and ri[(a - 1 - k) % n] == -s[(b + k) % m]: k += 1
                if 2 * k > m:
                    new = cyc(ri[a:] + ri[:a] + s[b:] + s[:b])
                    if len(new) < n and (best is None or len(new) < len(best[0])): best = (new, e, a, b)
    return best
def elim_step(rels):
    best = None
    for ri, r in enumerate(rels):
        cnt = {}
        for a in r: cnt[abs(a)] = cnt.get(abs(a), 0) + 1
        for g, c in cnt.items():
            if c == 1:
                key = (len(r), sum(1 for s in rels for x in s if abs(x) == g))
                if best is None or key < best[0]: best = (key, ri, g)
    return best
def simplify2(ng, rels, maxiter=400):
    gens = set(range(1, ng + 1)); rels = [canon(cyc(r)) for r in rels if cyc(r)]; log = []
    for _ in range(maxiter):
        rels = sorted(set(r for r in rels if r))
        b = elim_step(rels)
        if b is not None:
            _, ri, g = b; r = rels[ri]
            k = next(j for j, a in enumerate(r) if abs(a) == g)
            u, v = r[:k], r[k + 1:]
            img = red(inv(u) + inv(v)) if r[k] > 0 else red(v + u)
            log.append(('elim', r, g))
            rels = [canon(subst(s, g, img)) for j, s in enumerate(rels) if j != ri]
            gens.discard(g); continue
        # shortening
        bm = None
        for i in range(len(rels)):
            for j in range(len(rels)):
                if i == j: continue
                c = best_mul(rels[i], rels[j])
                if c and (bm is None or len(c[0]) - len(rels[i]) < bm[0]): bm = (len(c[0]) - len(rels[i]), i, j, c)
        if bm is None: break
        _, i, j, (new, e, a, b2) = bm
        log.append(('mul', rels[i], rels[j], e, a, b2))
        rels = [canon(new) if k == i else r for k, r in enumerate(rels)]
    rels = [r for r in rels if r]
    return gens, rels, log
def certify2(word):
    for direction, pres in (('top', presentation), ('bottom', presentation_rev)):
        ng, rels = pres(word)
        gens, rest, log = simplify2(ng, rels)
        if len(gens) == 1 and not rest: return True, {'direction': direction, 'log': log}
    return False, {}
def replay2(word, direction, log):
    ng, rels = (presentation if direction == 'top' else presentation_rev)(word)
    gens = set(range(1, ng + 1)); rels = [canon(cyc(r)) for r in rels if cyc(r)]
    for st in log:
        rels = sorted(set(r for r in rels if r))
        if st[0] == 'elim':
            r, g = tuple(st[1]), st[2]; ri = rels.index(r)
            assert sum(1 for a in r if abs(a) == g) == 1
            k = next(j for j, a in enumerate(r) if abs(a) == g)
            u, v = r[:k], r[k + 1:]
            img = red(inv(u) + inv(v)) if r[k] > 0 else red(v + u)
            rels = [canon(subst(s, g, img)) for j, s in enumerate(rels) if j != ri]; gens.discard(g)
        else:
            ri_, rj_, e, a, b = tuple(st[1]), tuple(st[2]), st[3], st[4], st[5]
            i = rels.index(ri_); assert rj_ in rels and rj_ != ri_
            s = rj_ if e == 1 else inv(rj_)
            new = cyc(ri_[a:] + ri_[:a] + s[b:] + s[:b])
            rels = [canon(new) if k == i else r for k, r in enumerate(rels)]
    rels = [r for r in rels if r]
    return gens, rels
