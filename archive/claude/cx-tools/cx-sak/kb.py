#!/usr/bin/env python3
"""
kb.py -- exact Kauffman bracket / Jones polynomial by planar contraction.
Written for the cx-sak task (independent of cx-tools/bracket.py).

PD convention (Knot Atlas / spherogram): crossing [a,b,c,d] lists the four edge
labels counterclockwise starting from the INCOMING UNDER edge; a->c is the under
strand, {b,d} the over strand.  Edge labels are consecutive along each oriented
component (with wraparound), so the over strand runs d->b iff b == next(d).

Bracket: <X> = A <A-smoothing> + A^-1 <B-smoothing>, <D u O> = delta <D>,
delta = -A^2 - A^-2, <O> = 1 (one crossingless circle has bracket 1).
A-smoothing of [a,b,c,d] joins (a,b) and (c,d); B-smoothing joins (a,d) and (b,c).
Crossing sign +1 iff over strand runs d->b.
V(t) = (-A^3)^(-w) <D>, t^(1/2) = A^(-2).  Jones polynomials are dicts
{k: coeff} meaning sum coeff * t^(k/2).

Validated in validate_kb.py against Knot Atlas data (trefoil, figure-eight, ...)
and geometric Hopf / unlink diagrams.
"""
from collections import defaultdict

# ---------------- Laurent polynomials in A: dict exp -> int ----------------

def padd(p, q):
    r = dict(p)
    for e, c in q.items():
        v = r.get(e, 0) + c
        if v:
            r[e] = v
        else:
            r.pop(e, None)
    return r

def pshift(p, k):
    return {e + k: c for e, c in p.items()}

def pmul(p, q):
    r = defaultdict(int)
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            r[e1 + e2] += c1 * c2
    return {e: c for e, c in r.items() if c}

DELTA = {2: -1, -2: -1}

def pmul_delta_pow(p, n):
    for _ in range(n):
        p = pmul(p, DELTA)
    return p

# ---------------- PD utilities ----------------

def pd_edges(pd):
    cnt = defaultdict(int)
    for x in pd:
        for e in x:
            cnt[e] += 1
    bad = [e for e, c in cnt.items() if c != 2]
    if bad:
        raise ValueError("edges not appearing exactly twice: %s" % bad[:10])
    return set(cnt)

def components_from_pd(pd):
    """Return (comps, succ, over_dir).  comps: list of edge-label lists along the
    orientation.  succ: successor map.  over_dir[i] = +1 if the over strand of
    crossing i runs d->b (positive crossing), -1 if it runs b->d.
    Orientation of the under strand is a->c; over-strand directions are resolved
    by propagation of the constraint that every edge has exactly one successor and
    one predecessor (each successor relation is attributed to one crossing)."""
    succ = {}
    pred = {}
    for a, b, c, d in pd:
        if a in succ or c in pred:
            raise ValueError("inconsistent under strands")
        succ[a] = c
        pred[c] = a
    over = [(b, d) for a, b, c, d in pd]
    over_dir = [0] * len(pd)
    unresolved = list(range(len(over)))
    changed = True
    while unresolved and changed:
        changed = False
        rest = []
        for i in unresolved:
            b, d = over[i]
            opt1_ok = (d not in succ) and (b not in pred)   # d->b
            opt2_ok = (b not in succ) and (d not in pred)   # b->d
            if opt1_ok and not opt2_ok:
                succ[d] = b; pred[b] = d; over_dir[i] = +1; changed = True
            elif opt2_ok and not opt1_ok:
                succ[b] = d; pred[d] = b; over_dir[i] = -1; changed = True
            elif not opt1_ok and not opt2_ok:
                raise ValueError("inconsistent PD at crossing %d" % i)
            else:
                rest.append(i)
        unresolved = rest
    while unresolved:
        # components that never pass under anything: fix ONE crossing of such a
        # component by the consecutive-label convention (labels increase along the
        # orientation), preferring a non-wraparound crossing, then propagate.
        cand = [i for i in unresolved if abs(over[i][0] - over[i][1]) == 1] or unresolved
        i = cand[0]
        b, d = over[i]
        if b == d + 1:
            succ[d] = b; pred[b] = d; over_dir[i] = +1
        else:
            succ[b] = d; pred[d] = b; over_dir[i] = -1
        unresolved.remove(i)
        changed = True
        while unresolved and changed:
            changed = False
            rest = []
            for j in unresolved:
                b, d = over[j]
                opt1_ok = (d not in succ) and (b not in pred)
                opt2_ok = (b not in succ) and (d not in pred)
                if opt1_ok and not opt2_ok:
                    succ[d] = b; pred[b] = d; over_dir[j] = +1; changed = True
                elif opt2_ok and not opt1_ok:
                    succ[b] = d; pred[d] = b; over_dir[j] = -1; changed = True
                elif not opt1_ok and not opt2_ok:
                    raise ValueError("inconsistent PD at crossing %d" % j)
                else:
                    rest.append(j)
            unresolved = rest
    edges = set(succ)
    comps = []
    seen = set()
    for e in sorted(edges, key=lambda x: (str(type(x)), x)):
        if e in seen:
            continue
        comp = []
        x = e
        while x not in seen:
            seen.add(x)
            comp.append(x)
            x = succ[x]
        comps.append(comp)
    return comps, succ, over_dir

def crossing_signs(pd):
    return components_from_pd(pd)[2]

def writhe(pd):
    return sum(crossing_signs(pd))

# ---------------- planar contraction ----------------

def greedy_order(pd):
    n = len(pd)
    # edge -> crossings containing it
    e2c = defaultdict(list)
    for i, x in enumerate(pd):
        for e in x:
            e2c[e].append(i)
    done = [False] * n
    open_edges = set()
    order = []
    # start from crossing 0 (or any); then always pick crossing minimizing new boundary size
    for _ in range(n):
        best = None
        for i in range(n):
            if done[i]:
                continue
            x = pd[i]
            # multiplicity-aware: each occurrence of an edge in x is an endpoint
            newopen = set(open_edges)
            for e in x:
                if e in newopen:
                    newopen.discard(e)
                else:
                    newopen.add(e)
            # kinks: edge appearing twice in x toggles twice -> net unchanged; handle:
            cnt = defaultdict(int)
            for e in x:
                cnt[e] += 1
            for e, c in cnt.items():
                if c == 2:
                    newopen.discard(e)
            score = (len(newopen), -sum(1 for e in x if e in open_edges))
            if best is None or score < best[0]:
                best = (score, i, newopen)
        _, i, newopen = best
        done[i] = True
        open_edges = newopen
        order.append(i)
    return order

def cutwidth(pd, order):
    """Maximum number of open edges along the absorption order (cheap state-space estimate)."""
    open_edges = set()
    worst = 0
    for i in order:
        x = pd[i]
        cnt = defaultdict(int)
        for e in x:
            cnt[e] += 1
        for e, c in cnt.items():
            if c == 2:
                continue
            if e in open_edges:
                open_edges.discard(e)
            else:
                open_edges.add(e)
        worst = max(worst, len(open_edges))
    return worst

def _absorb(M, arcs):
    """M: dict open edge -> partner (symmetric).  arcs: list of (e,f) new arcs.
    Returns (newM, loops)."""
    M = dict(M)
    loops = 0
    for e, f in arcs:
        if e == f:
            if e in M:
                # edge e: its other end was absorbed before and now both ends here?? impossible
                raise ValueError("edge appears thrice?")
            loops += 1
            continue
        ein = e in M
        fin = f in M
        if ein and fin:
            pe = M.pop(e)
            if pe == f:
                M.pop(f, None)
                loops += 1
            else:
                pf = M.pop(f)
                M[pe] = pf
                M[pf] = pe
        elif ein:
            pe = M.pop(e)
            M[pe] = f
            M[f] = pe
        elif fin:
            pf = M.pop(f)
            M[pf] = e
            M[e] = pf
        else:
            M[e] = f
            M[f] = e
    return M, loops

def _key(M):
    return tuple(sorted((min(e, f), max(e, f)) for e, f in M.items() if e < f or (e == f)))

def kauffman_bracket(pd, order=None, verbose=False):
    """Exact Kauffman bracket of the PD (closed diagram, every component has crossings)."""
    pd = [tuple(x) for x in pd]
    pd_edges(pd)
    if order is None:
        order = greedy_order(pd)
    # states: dict key(matching) -> (matching dict, poly)
    states = {(): ({}, {0: 1})}
    maxstates = 0
    for step, i in enumerate(order):
        a, b, c, d = pd[i]
        new_states = {}
        for key, (M, poly) in states.items():
            for arcs, shift in (([(a, b), (c, d)], 1), ([(a, d), (b, c)], -1)):
                M2, loops = _absorb(M, arcs)
                p2 = pshift(poly, shift)
                if loops:
                    p2 = pmul_delta_pow(p2, loops)
                k2 = _key(M2)
                if k2 in new_states:
                    new_states[k2] = (M2, padd(new_states[k2][1], p2))
                else:
                    new_states[k2] = (M2, p2)
        states = {k: v for k, v in new_states.items() if v[1]}
        maxstates = max(maxstates, len(states))
        if verbose and step % 20 == 0:
            print("  step %d/%d states %d" % (step, len(order), len(states)))
    assert len(states) == 1 and () in states, "diagram did not close up: %s" % list(states)[:3]
    poly = states[()][1]
    # the last loop closure gave a factor delta for every component; <O>=1 normalisation:
    # Our convention counted every closed loop as delta, so bracket of unknot diagram = delta * (...)?
    # Correct: a single crossingless circle should be 1, but our contraction multiplies delta for
    # every closed loop, including the final one(s).  Divide by one delta.
    return _div_delta(poly), maxstates

def _div_delta(p):
    """Divide Laurent polynomial p by delta = -(A^2 + A^-2) exactly."""
    # p = q * (-A^2 - A^-2)  ->  q = -p / (A^2 + A^-2). Do polynomial long division in A^2.
    if not p:
        return {}
    p = dict(p)
    q = {}
    # multiply by A^2: p*A^2 = q*(-A^4 - 1)  -> q = -(p A^2)/(A^4+1)
    pp = pshift(p, 2)
    # division by (A^4 + 1): treat as polynomial in A; highest degree first
    pp = {e: -c for e, c in pp.items()}
    res = {}
    while pp:
        emax = max(pp)
        cmax = pp[emax]
        # term cmax * A^(emax-4) in quotient
        res[emax - 4] = res.get(emax - 4, 0) + cmax
        pp = padd(pp, {emax: -cmax, emax - 4: -cmax})
        if any(e < -10**6 for e in pp):
            raise ValueError("division by delta failed")
    return {e: c for e, c in res.items() if c}

def jones_from_pd(pd, verbose=False, signs=None, order=None):
    pd = [tuple(x) for x in pd]
    if signs is not None:
        w = sum(signs)
        w_inf = writhe(pd)
        if w_inf != w:
            print("WARNING: PD-inferred writhe %d differs from explicit writhe %d "
                  "(orientation of an all-over component is not encoded in the PD)" % (w_inf, w))
    else:
        w = writhe(pd)
    br, mx = kauffman_bracket(pd, order=order, verbose=verbose)
    # V = (-A^3)^(-w) <D> ; A^e -> t^{-e/4} -> exponent of t^(1/2) is -e/2
    sign = (-1) ** (w % 2)
    V = {}
    for e, c in br.items():
        ee = e - 3 * w
        assert ee % 2 == 0
        V[-ee // 2] = V.get(-ee // 2, 0) + sign * c
    return {k: c for k, c in V.items() if c}, w, mx

def jones_str(V):
    if not V:
        return "0"
    terms = []
    for k in sorted(V):
        c = V[k]
        if k == 0:
            s = "%d" % c
        else:
            if k % 2 == 0:
                mon = "t^%d" % (k // 2) if k // 2 != 1 else "t"
            else:
                mon = "t^(%d/2)" % k
            if c == 1:
                s = mon
            elif c == -1:
                s = "-" + mon
            else:
                s = "%d*%s" % (c, mon)
        terms.append(s)
    out = " + ".join(terms)
    return out.replace("+ -", "- ")

def jones_to_snape_q(V):
    """Snape/Khovanov normalisation: J(q) = V(t) at t^(1/2) = -q.  Returns dict q-exponent -> coeff."""
    J = {}
    for k, c in V.items():
        J[k] = J.get(k, 0) + c * ((-1) ** (k % 2))
    return {k: c for k, c in J.items() if c}

def poly_str_q(J, var="q"):
    terms = []
    for k in sorted(J):
        c = J[k]
        mon = "" if k == 0 else (var if k == 1 else "%s^%d" % (var, k))
        if mon == "":
            s = "%d" % c
        elif c == 1:
            s = mon
        elif c == -1:
            s = "-" + mon
        else:
            s = "%d*%s" % (c, mon)
        terms.append(s)
    return (" + ".join(terms)).replace("+ -", "- ") if terms else "0"

def mirror(V):
    return {-k: c for k, c in V.items()}

UNLINK2 = {1: -1, -1: -1}   # -t^(1/2) - t^(-1/2)
