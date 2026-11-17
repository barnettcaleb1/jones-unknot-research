#!/usr/bin/env python3
"""
Referee's code: type D structures over B in curve form, and the first-order (U^2) obstruction to extending them
over B^*[U] (equation (*) of the report):
     mu_2(delta_0, delta_2) + mu_2(delta_2, delta_0) + mu_4(delta_0, delta_0, delta_0, delta_0) = 0.
F_2 coefficients.  Uses only binf.py (my own).
"""
from binf import *
from binf import _add

class TD:
    """generators: list of dicts {idem, h, q, name}; arrows: list (i, j, elt) meaning gen i -> gen j labelled elt."""
    def __init__(self):
        self.gens = []
        self.arrows = []
    def add_gen(self, idem, h, q, name=None):
        self.gens.append({'idem': idem, 'h': h, 'q': q, 'name': name or '%s%d' % (idem, len(self.gens))})
        return len(self.gens) - 1
    def add_arrow(self, i, j, elt):
        assert elt[2] == self.gens[i]['idem'] and elt[3] == self.gens[j]['idem'], (i, j, elt)
        if self.gens[i]['h'] is not None:
            assert self.gens[j]['h'] == self.gens[i]['h'] + 1, 'h-grading'
            assert self.gens[j]['q'] == self.gens[i]['q'] + qdeg(elt), 'q-grading'
        self.arrows.append((i, j, elt))
    def out(self, i):
        return [(j, e) for (a, j, e) in self.arrows if a == i]
    def inc(self, j):
        return [(i, e) for (i, b, e) in self.arrows if b == j]
    def check_d2(self):
        """delta_0^2 = 0 over B."""
        tot = {}
        for (i, j, e) in self.arrows:
            for (k, f) in self.out(j):
                p = mul(f, e)
                if p is not None:
                    _add(tot, (i, k, p))
        return not tot
    def check_curve_form(self):
        """every generator: at most one D-power arrow and at most one S-power arrow."""
        for g in range(len(self.gens)):
            for kind in 'DS':
                n = sum(1 for (i, j, e) in self.arrows if e[0] == kind and (i == g or j == g))
                if n > 1:
                    return False
        return True
    def disjoint_union(self, other, dh=0, dq=0):
        res = TD()
        for g in self.gens:
            res.add_gen(g['idem'], g['h'], g['q'], g['name'])
        off = len(self.gens)
        for g in other.gens:
            res.add_gen(g['idem'], g['h'] + dh, g['q'] + dq, g['name'] + "'")
        res.arrows = list(self.arrows) + [(i + off, j + off, e) for (i, j, e) in other.arrows]
        return res

# ---------------------------------------------------------------------------------------------
# building components from words
def run(n, sign):
    """P_n = S (D S^2)^(n-1) D S as a list of steps (kind, power, direction)."""
    steps = [('S', 1, sign), ('D', 1, sign)]
    for _ in range(n - 1):
        steps += [('S', 2, sign), ('D', 1, sign)]
    steps += [('S', 1, sign)]
    if sign < 0:
        steps = steps[::-1]
    return steps

def word_to_steps(word):
    """word: list of moves; a move is ('D', a, sign), ('P', n, sign) or a raw step ('s', kind, power, sign)."""
    steps = []
    for mv in word:
        if mv[0] == 'D':
            steps.append(('D', mv[1], mv[2]))
        elif mv[0] == 'P':
            steps += run(mv[1], mv[2])
        elif mv[0] == 's':
            steps.append((mv[1], mv[2], mv[3]))
        else:
            raise ValueError(mv)
    return steps

def build(word, compact=False, start_idem=B, h0=0, q0=0, graded=True, prefix=''):
    """Build a component from a word, travelling along the curve.  Step (kind, k, +1): arrow from the current generator to
    the next one; (kind, k, -1): arrow from the next generator to the current one.  Returns TD or None if a compact
    word does not close up (idempotent or grading mismatch) or if the curve form is violated."""
    steps = word_to_steps(word)
    td = TD()
    cur = td.add_gen(start_idem, h0 if graded else None, q0 if graded else None, prefix + start_idem + '0')
    first = cur
    last_kind = None
    for idx, (kind, k, sgn) in enumerate(steps):
        if kind == last_kind:
            return None                       # D-side and S-side must alternate along a curve
        last_kind = kind
        ci = td.gens[cur]['idem']
        ni = ci if (kind == 'D' or k % 2 == 0) else other(ci)
        elt_fwd = (kind, k, ci, ni)
        elt_bwd = (kind, k, ni, ci)
        dq = 2 * k if kind == 'D' else k
        if graded:
            nh = td.gens[cur]['h'] + sgn
            nq = td.gens[cur]['q'] + sgn * dq
        else:
            nh = nq = None
        if compact and idx == len(steps) - 1:
            g = td.gens[first]
            if g['idem'] != ni or (graded and (g['h'] != nh or g['q'] != nq)):
                return None
            if steps[0][0] == kind:
                return None
            nxt = first
        else:
            nxt = td.add_gen(ni, nh, nq, prefix + ni + str(len(td.gens)))
        if sgn > 0:
            td.arrows.append((cur, nxt, elt_fwd))
        else:
            td.arrows.append((nxt, cur, elt_bwd))
        cur = nxt
    assert td.check_curve_form()
    assert td.check_d2()
    return td

# ---------------------------------------------------------------------------------------------
# first-order obstruction
def paths(td, length):
    """all directed paths of delta_0-arrows of the given length: list of (start, end, [labels in path order])."""
    outs = {i: td.out(i) for i in range(len(td.gens))}
    res = []
    def rec(start, cur, labels):
        if len(labels) == length:
            res.append((start, cur, tuple(labels)))
            return
        for (j, e) in outs[cur]:
            labels.append(e)
            rec(start, j, labels)
            labels.pop()
    for i in range(len(td.gens)):
        rec(i, i, [])
    return res

def mu4_term(td):
    """the U^2 coefficient mu_4(delta_0^4): dict {(x, z, basis elt): 1}."""
    tot = {}
    for (x, z, labels) in paths(td, 4):
        for b in mu_path(labels):
            _add(tot, (x, z, b))
    return tot

def candidate_delta2(td, maxpow=12, graded=True):
    """all possible U^2-arrows x -> y with a basis label (including idempotents) of the right bidegree:
       h(y) - h(x) = 3, q(y) - q(x) = 6 + |a|.  In ungraded mode: all labels with power <= maxpow."""
    cands = []
    n = len(td.gens)
    for x in range(n):
        for y in range(n):
            gx, gy = td.gens[x], td.gens[y]
            labels = []
            if gx['idem'] == gy['idem']:
                labels.append(I(gx['idem']))
                labels += [D(k, gx['idem']) for k in range(1, maxpow + 1)]
                labels += [S(2 * k, gx['idem']) for k in range(1, maxpow // 2 + 1)]
            else:
                labels += [S(2 * k + 1, gx['idem']) for k in range(0, (maxpow + 1) // 2)]
            for a in labels:
                if graded:
                    if gy['h'] - gx['h'] != 3 or gy['q'] - gx['q'] != 6 + qdeg(a):
                        continue
                cands.append((x, y, a))
    return cands

def solve_f2(rows, ncols):
    """rows: list of (bitmask over columns, rhs bit).  Returns (solvable, particular solution bitmask, rank)."""
    pivots = {}                       # pivot col -> (mask, rhs)
    for mask, rhs in rows:
        while mask:
            p = mask.bit_length() - 1
            if p in pivots:
                pm, pr = pivots[p]
                mask ^= pm
                rhs ^= pr
            else:
                pivots[p] = (mask, rhs)
                break
        else:
            if rhs:
                return False, None, len(pivots)
    # back substitution: free variables = 0
    sol = 0
    for p in sorted(pivots):
        mask, rhs = pivots[p]
        val = rhs
        rest = mask ^ (1 << p)
        val ^= bin(rest & sol).count('1') & 1
        if val:
            sol |= (1 << p)
    return True, sol, len(pivots)

def first_order(td, maxpow=12, graded=True, verbose=False):
    """Solve (*) for delta_2.  Returns dict with keys solvable, solution (list of arrows), nfree (dimension of the
    solution space when solvable), obstruction (the mu_4 term)."""
    rhs = mu4_term(td)
    cands = candidate_delta2(td, maxpow, graded)
    col = {c: i for i, c in enumerate(cands)}
    eqs = {}                          # (x, z, elt) -> bitmask
    outs = {i: td.out(i) for i in range(len(td.gens))}
    incs = {i: td.inc(i) for i in range(len(td.gens))}
    for (x, y, a), i in col.items():
        for (z, c) in outs[y]:        # x -a(U^2)-> y -c-> z
            p = mul(c, a)
            if p is not None:
                eqs[(x, z, p)] = eqs.get((x, z, p), 0) ^ (1 << i)
        for (w, c) in incs[x]:        # w -c-> x -a(U^2)-> y
            p = mul(a, c)
            if p is not None:
                eqs[(w, y, p)] = eqs.get((w, y, p), 0) ^ (1 << i)
    rows = []
    keys = set(eqs) | set(rhs)
    for k in keys:
        rows.append((eqs.get(k, 0), rhs.get(k, 0)))
    ok, sol, rank = solve_f2(rows, len(cands))
    res = {'solvable': ok, 'obstruction': rhs, 'ncand': len(cands), 'rank': rank}
    if ok:
        res['solution'] = [cands[i] for i in range(len(cands)) if (sol >> i) & 1]
        res['nfree'] = len(cands) - rank
    if verbose:
        print(describe(td, res))
    return res

def gname(td, i):
    return td.gens[i]['name']

def describe(td, res):
    s = []
    s.append('  mu_4 term: ' + ('0' if not res['obstruction'] else
             ', '.join('%s -[%s U^2]-> %s' % (gname(td, x), name(b), gname(td, z)) for (x, z, b) in sorted(res['obstruction']))))
    if res['solvable']:
        s.append('  SOLVABLE; a solution delta_2 = {' + ', '.join('%s -[%s]-> %s' % (gname(td, x), name(a), gname(td, y))
                 for (x, y, a) in res['solution']) + '}; solution space dimension %d (of %d graded candidates)' % (res['nfree'], res['ncand']))
    else:
        s.append('  NOT SOLVABLE (first-order obstruction); %d graded candidates' % res['ncand'])
    return '\n'.join(s)

def show(td):
    out = []
    for (i, j, e) in td.arrows:
        out.append('%s -%s-> %s' % (gname(td, i), name(e), gname(td, j)))
    return '; '.join(out)
