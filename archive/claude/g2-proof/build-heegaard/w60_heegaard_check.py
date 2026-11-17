"""Sanity checks for build-heegaard (definitions and single identities only, no sweeps).

W(6,0): basis = 5 noncrossing perfect matchings of 6 points (cup diagrams).
e_i joins positions i,i+1 (0-based i = 0..4). sigma_i -> A + A^{-1} e_i.
B(x,y) = sum x_m y_n delta^{loops(m,n)}, delta = -A^2 - A^{-2}, <empty> = 1.
c = (12)(34)(56) is the cup (handlebody) vector; <plat beta> = B(c, rho(beta) c).
"""
import itertools, math, cmath
import numpy as np

N = 6

def nc_matchings(pts):
    if not pts:
        return [dict()]
    out = []
    a = pts[0]
    for k in range(1, len(pts), 2):
        b = pts[k]
        inner, outer = pts[1:k], pts[k + 1:]
        for mi in nc_matchings(inner):
            for mo in nc_matchings(outer):
                m = {a: b, b: a}
                m.update(mi); m.update(mo)
                out.append(m)
    return out

BASIS = [tuple(m[i] for i in range(N)) for m in nc_matchings(list(range(N)))]
IDX = {m: k for k, m in enumerate(BASIS)}
C = (1, 0, 3, 2, 5, 4)
assert C in IDX

def loops(m1, m2):
    seen, cnt = set(), 0
    for s in range(N):
        if s in seen:
            continue
        cnt += 1
        x, use1 = s, True
        while True:
            seen.add(x)
            x = m1[x] if use1 else m2[x]
            use1 = not use1
            if x == s and use1:
                break
            seen.add(x)
    return cnt

def e_act(i, m):
    """returns (power_of_delta, new_matching)"""
    if m[i] == i + 1:
        return 1, m
    a, b = m[i], m[i + 1]
    new = list(m)
    new[i], new[i + 1] = i + 1, i
    new[a], new[b] = b, a
    return 0, tuple(new)

# ---------- Laurent polynomials in A: dict exp -> int ----------
def padd(p, q):
    r = dict(p)
    for k, v in q.items():
        r[k] = r.get(k, 0) + v
        if r[k] == 0:
            del r[k]
    return r

def pmul(p, q):
    r = {}
    for a, x in p.items():
        for b, y in q.items():
            r[a + b] = r.get(a + b, 0) + x * y
    return {k: v for k, v in r.items() if v}

def pscal(p, c, shift=0):
    return {k + shift: v * c for k, v in p.items() if v * c}

DELTA = {2: -1, -2: -1}
def dpow(k):
    r = {0: 1}
    for _ in range(k):
        r = pmul(r, DELTA)
    return r

def vadd(x, y):
    r = dict(x)
    for m, p in y.items():
        r[m] = padd(r.get(m, {}), p)
        if not r[m]:
            del r[m]
    return r

def e_vec(i, x):
    r = {}
    for m, p in x.items():
        k, m2 = e_act(i, m)
        r = vadd(r, {m2: pmul(p, dpow(k))})
    return r

def sigma(i, x, inv=False):
    s = -1 if inv else 1
    a = {m: pscal(p, 1, s) for m, p in x.items()}          # A^{+-1} x
    b = {m: pscal(p, 1, -s) for m, p in e_vec(i, x).items()}  # A^{-+1} e_i x
    return vadd(a, b)

def word(w, x):
    """apply braid word w (list of +-(i+1)), rightmost letter first"""
    for g in reversed(w):
        x = sigma(abs(g) - 1, x, inv=(g < 0))
    return x

def B(x, y):
    r = {}
    for m, p in x.items():
        for n, q in y.items():
            r = padd(r, pmul(pmul(p, q), dpow(loops(m, n))))
    return r

def bar(x):
    return {m: {-k: v for k, v in p.items()} for m, p in x.items()}

def is_scalar_multiple_of_c(x):
    return set(x.keys()) == {C}, x.get(C)

def show(p):
    return " + ".join(f"{v}*A^{k}" for k, v in sorted(p.items())) or "0"

c = {C: {0: 1}}
print("basis:", BASIS)
print("B(c,c) == delta^3:", B(c, c) == dpow(3))

# 1. unknot plat: B(c, rho(s2 s4) c) = A^6 delta
u = word([2, 4], c)
print("B(c, rho(s2 s4)c) == A^6 delta:", B(c, u) == pscal(DELTA, 1, 6), "|", show(B(c, u)))
print("hermitian norm of u == delta^3:", B(bar(u), u) == dpow(3))

# 2. Hilden generators act on c by scalars
for name, w in [("s1", [1]), ("s3", [3]), ("s2 s1 s3 s2 (cap swap)", [2, 1, 3, 2]),
                ("s2 s1^2 s2 (strand around cap)", [2, 1, 1, 2]),
                ("(s1 s2)^3 = twist about {1,2,3}", [1, 2] * 3),
                ("half twist Delta", [1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1])]:
    ok, sc = is_scalar_multiple_of_c(word(w, c))
    print(f"  {name}: scalar on c? {ok}  scalar = {show(sc) if ok else '-'}")
ok, _ = is_scalar_multiple_of_c(word([2, 3] * 3, c))
print("  (s2 s3)^3 = twist about {2,3,4} (contains cap (34), so Hilden) fixes [c]?", ok, "(expected True)")

# ---------- numerics ----------
def gram(delta):
    G = np.zeros((5, 5))
    for i, m in enumerate(BASIS):
        for j, n in enumerate(BASIS):
            G[i, j] = delta ** loops(m, n)
    return G

def detformula(d):
    return d ** 4 * (d * d - 1) ** 4 * (d ** 3 - 2 * d)

print("\nGram determinant vs [2]^4[3]^4[4] formula:")
for d in [0.7, 1.2, 1.5, 1.9, 2.5, 3.3]:
    print(f"  delta={d}: det={np.linalg.det(gram(d)):.6g}  formula={detformula(d):.6g}")

# sign symmetry G(-delta) = -D G(delta) D
a = [(loops(C, m) - 3) % 2 for m in BASIS]
D = np.diag([(-1) ** x for x in a])
consistent = all((loops(m, n) - 3 - a[i] - a[j]) % 2 == 0 for i, m in enumerate(BASIS) for j, n in enumerate(BASIS))
print("loops(m,n) = 3 + a_m + a_n mod 2 for all pairs:", consistent)
print("G(-1.7) == -D G(1.7) D:", np.allclose(gram(-1.7), -D @ gram(1.7) @ D))

print("\nEigenvalues of G(delta):")
for label, d in [("r=4 (sqrt2)", 2 * math.cos(math.pi / 4)), ("r=5", 2 * math.cos(math.pi / 5)),
                 ("r=6", 2 * math.cos(math.pi / 6)), ("r=8", 2 * math.cos(math.pi / 8)),
                 ("delta=1.45", 1.45), ("delta=1.40", 1.40), ("delta=-1.6", -1.6),
                 ("r=3 (delta=1)", 1.0)]:
    ev = np.linalg.eigvalsh(gram(d))
    print(f"  {label:14s}", np.round(ev, 5))

# unitarity at |A| = 1: M^dagger G M = G
def rho_matrix(i, A):
    M = np.zeros((5, 5), dtype=complex)
    d = -A * A - 1 / (A * A)
    for j, m in enumerate(BASIS):
        M[j, j] += A
        k, m2 = e_act(i, m)
        M[IDX[m2], j] += (d ** k) / A
    return M

for theta in [0.3, 1.2]:
    A = cmath.exp(1j * theta)
    d = (-A * A - 1 / (A * A)).real
    G = gram(d)
    ok = all(np.allclose(rho_matrix(i, A).conj().T @ G @ rho_matrix(i, A), G) for i in range(5))
    print(f"theta={theta}: delta={d:.4f}, unitary w.r.t. G: {ok}, G definite: {np.all(np.linalg.eigvalsh(G) > 0) or np.all(np.linalg.eigvalsh(G) < 0)}")

# radical at r=4
print("rank G at r=4:", np.linalg.matrix_rank(gram(math.sqrt(2)), tol=1e-9), " rank at r=3:", np.linalg.matrix_rank(gram(1.0), tol=1e-9))

# 3|3 curve with no cap of c off it: s1 = sigma_2(boundary of {3,4,5}) encloses one endpoint of each cap.
x = word([2, 3, 4, 3, 4, 3, 4, -2], c)
ok, _ = is_scalar_multiple_of_c(x)
print("\nT_{s1}, s1 = sigma_2(round curve about {3,4,5}) (no cap off s1): fixes [c]?", ok, "(expected False)")
print("  B(c, T_{s1} c) =", show(B(c, x)), " vs delta^3 A^k pattern")
