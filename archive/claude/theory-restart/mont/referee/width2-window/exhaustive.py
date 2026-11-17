"""Exhaustive adversarial test of the WIDTH2-WINDOW theorem over ALL coefficient tables.

For fixed support width Wn (all p_s supported in [0,Wn]), fixed D and fixed target (m0,n0) we decide EXACTLY
(linear algebra over Q) whether there exists a table with
    sum_s p_s t^(sigma_s(m0,n0)) = t^k D     for some integer k,
in which all six boundary sectors 00,02,20,24,42,44 are nonzero (22 free, may vanish).
The solution set for fixed k is an affine space; a generic point has every boundary p_s != 0 unless that
p_s is forced to vanish on the whole space (a vector space is not a finite union of proper subspaces).
Scanning Wn upward, the first Wn at which a target becomes feasible is the minimal actual width (translation
invariance), so B = max(1,Wn,span D) is the theorem's B for the extremal tables.
"""
import sys
from fractions import Fraction
from wbf import SECT, IJ

BOUND = ['00', '02', '20', '24', '42', '44']


def rref_info(A, nrow, ncol):
    """A: list of rows (Fractions). Returns (pivots, R, Mx, leftnull) where after elimination
    R = M A in RREF, Mx = M; leftnull = rows of M annihilating A."""
    R = [list(r) for r in A]
    M = [[Fraction(int(i == j)) for j in range(nrow)] for i in range(nrow)]
    pivots = []
    row = 0
    for col in range(ncol):
        piv = None
        for i in range(row, nrow):
            if R[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        R[row], R[piv] = R[piv], R[row]
        M[row], M[piv] = M[piv], M[row]
        pv = R[row][col]
        if pv != 1:
            R[row] = [x / pv for x in R[row]]
            M[row] = [x / pv for x in M[row]]
        for i in range(nrow):
            if i != row and R[i][col] != 0:
                f = R[i][col]
                R[i] = [a - f * b for a, b in zip(R[i], R[row])]
                M[i] = [a - f * b for a, b in zip(M[i], M[row])]
        pivots.append(col)
        row += 1
        if row == nrow:
            break
    rank = len(pivots)
    leftnull = M[rank:]
    return pivots, R, M, leftnull


def analyse_target(m0, n0, Wn, Dco, SD):
    """Dco: integer coeff list of D (lowest exponent 0). Returns list of feasible k (each gives a table
    family with all six boundary sectors nonzero) -- empty if none."""
    sig = {s: 2 * IJ[s][0] * m0 + 2 * IJ[s][1] * n0 for s in SECT}
    # clusters of overlapping windows [sig, sig+Wn]
    order = sorted(SECT, key=lambda s: sig[s])
    clusters = []
    cur = [order[0]]
    hi = sig[order[0]] + Wn
    for s in order[1:]:
        if sig[s] <= hi:
            cur.append(s)
            hi = max(hi, sig[s] + Wn)
        else:
            clusters.append(cur)
            cur = [s]
            hi = sig[s] + Wn
    clusters.append(cur)
    cinfo = []
    for cl in clusters:
        lo = min(sig[s] for s in cl)
        h = max(sig[s] for s in cl) + Wn
        if len(cl) == 1:
            cinfo.append((cl, lo, h, None))
            continue
        # unknowns: (s, j) j=0..Wn ; rows: exponents lo..h
        cols = [(s, j) for s in cl for j in range(Wn + 1)]
        nrow = h - lo + 1
        A = [[Fraction(0)] * len(cols) for _ in range(nrow)]
        for ci, (s, j) in enumerate(cols):
            A[sig[s] + j - lo][ci] = Fraction(1)
        pivots, R, M, leftnull = rref_info(A, nrow, len(cols))
        free = [c for c in range(len(cols)) if c not in pivots]
        # null-space support per sector: sector s undetermined if some free col belongs to s,
        # or some pivot col of s has nonzero R entry in a free column
        undet = set()
        for f in free:
            undet.add(cols[f][0])
        for i, pc in enumerate(pivots):
            if any(R[i][f] != 0 for f in free):
                undet.add(cols[pc][0])
        cinfo.append((cl, lo, h, (cols, pivots, M, leftnull, undet)))
    allsig = list(sig.values())
    kmin = min(allsig) - SD
    kmax = max(allsig) + Wn
    feas = []
    for k in range(kmin, kmax + 1):
        dsupp = {k + i: c for i, c in enumerate(Dco) if c}
        # D must lie inside the union of cluster ranges
        ok = True
        for e in dsupp:
            if not any(lo <= e <= h for (_, lo, h, _) in cinfo):
                ok = False
                break
        if not ok:
            continue
        for (cl, lo, h, info) in cinfo:
            rhs = [Fraction(dsupp.get(e, 0)) for e in range(lo, h + 1)]
            if info is None:
                s = cl[0]
                if s in BOUND and not any(rhs):
                    ok = False
                    break
                continue
            cols, pivots, M, leftnull, undet = info
            if any(sum(y * b for y, b in zip(row, rhs)) != 0 for row in leftnull):
                ok = False
                break
            # particular solution (free vars = 0)
            xpart = {}
            for i, pc in enumerate(pivots):
                xpart[pc] = sum(y * b for y, b in zip(M[i], rhs))
            for s in cl:
                if s not in BOUND or s in undet:
                    continue
                # s fully determined: must be nonzero
                if all(xpart.get(ci, 0) == 0 for ci, (ss, j) in enumerate(cols) if ss == s):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            feas.append(k)
    return feas


def run(Wmax, Dlist, extra=3, verbose=True):
    results = []
    for name, Dco in Dlist:
        SD = len(Dco) - 1
        found_min_W = {}
        for Wn in range(0, Wmax + 1):
            B = max(1, Wn, SD)
            Rb = 3 * B + extra
            for m0 in range(-Rb, Rb + 1):
                for n0 in range(-Rb, Rb + 1):
                    if (m0, n0) in found_min_W:
                        continue
                    if m0 == 0 or n0 == 0:
                        continue  # axis points: trivially inside the window
                    f = analyse_target(m0, n0, Wn, Dco, SD)
                    if f:
                        found_min_W[(m0, n0)] = (Wn, f[:3])
        # evaluate the window for each feasible target at its minimal width
        worst = None
        viol = []
        for (m0, n0), (Wn, ks) in found_min_W.items():
            B = max(1, Wn, SD)
            r = min(abs(m0), abs(n0)) / B
            if worst is None or r > worst[0]:
                worst = (r, (m0, n0), Wn, B)
            if abs(m0) > 3 * B and abs(n0) > 3 * B:
                viol.append(((m0, n0), Wn, B))
        res = dict(D=name, SD=SD, nfeasible_offaxis=len(found_min_W), worst=worst, violations=viol)
        results.append(res)
        if verbose:
            print(res, flush=True)
    return results


if __name__ == '__main__':
    Wmax = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    Dlist = [('1', [1]), ('1+t', [1, 1]), ('1-t', [1, -1]), ('1+t^2', [1, 0, 1]), ('1+t+t^2', [1, 1, 1]),
             ('1-t^3', [1, 0, 0, -1]), ('(1+t^2)(1+t+t^2)', [1, 1, 2, 1, 1]), ('1+t^4', [1, 0, 0, 0, 1]),
             ('1-t^5', [1, 0, 0, 0, 0, -1])]
    sel = sys.argv[2].split(',') if len(sys.argv) > 2 else None
    if sel:
        Dlist = [d for d in Dlist if d[0] in sel]
    run(Wmax, Dlist)
