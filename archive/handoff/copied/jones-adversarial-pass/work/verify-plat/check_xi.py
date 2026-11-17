"""Independent checks of claim (4) for the Long-Paton braid xi.
(a) Artin action on F_6: xi nontrivial in B_6; after imposing x1...x6 = 1 it is inner
    (so trivial in Out(pi_1 S_{0,6}) = Mod(S_{0,6}) by Dehn-Nielsen-Baer type injectivity).
(b) T = (s2 s3 s4 s5)^5 alone: same test (inner on pi_1 of sphere).
(c) TL cell module W(6,0): rho(xi) = I and rho(T) scalar, over F_p at random A.
(d) reduced Burau at random t: xi in kernel (sanity check of the transcription).
Word copied verbatim from work/width6/kernel_words.py (commutator [a,b]=a b a^-1 b^-1).
"""
import random, itertools

def inv(w): return [-s for s in reversed(w)]
def red(w):
    out = []
    for s in w:
        if out and out[-1] == -s: out.pop()
        else: out.append(s)
    return out
def comm(a, b): return red(a + b + inv(a) + inv(b))
def conj(w, p): return red(inv(p) + w + p)
PSI = [-5,-4,5,-3,4,-2,-3,-3,-3,1,1,1,5,4,-3,-2,1]
XI = comm(conj([5], PSI), [2,3,4,5]*5)
TW = [2,3,4,5]*5
N = 6

# ---------- (a),(b) Artin action ----------
# sigma_i: x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i ; letters are +-j for x_j^{+-1}
def gen_aut(g):
    i = abs(g); im = {j: [j] for j in range(1, N+1)}
    if g > 0:
        im[i] = [i, i+1, -i]; im[i+1] = [i]
    else:
        im[i] = [i+1]; im[i+1] = [-(i+1), i, i+1]
    return im
def apply(im, word):
    out = []
    for l in word:
        out += im[l] if l > 0 else inv(im[-l])
    return red(out)
def compose(a, b):  # a o b
    return {j: apply(a, b[j]) for j in b}
def word_aut(w):
    im = {j: [j] for j in range(1, N+1)}
    for g in w:                       # im := im o gen(g)  (right-to-left reading irrelevant, see notes)
        im = compose(im, gen_aut(g))
    return im
def to_sphere(word):  # substitute x6 = (x1..x5)^-1
    out = []
    for l in word:
        if abs(l) == 6:
            out += [-5,-4,-3,-2,-1] if l > 0 else [1,2,3,4,5]
        else:
            out.append(l)
    return red(out)
def is_inner(images):
    """images: dict j->reduced word in F_5 (x1..x5). Return conjugator g with images[j]=g x_j g^-1, or None."""
    w1 = images[1]
    # w1 must be u x1 u^-1 with u reduced and not ending in x1^{+-1} (after cancellation)
    k = (len(w1) - 1)//2
    if len(w1) % 2 == 0 or w1[k] != 1 or red(w1[:k] + [1] + inv(w1[:k])) != w1:
        return None
    u = w1[:k]
    for m in range(-60, 61):
        g = red(u + ([1]*m if m >= 0 else [-1]*(-m)))
        if all(red(g + [j] + inv(g)) == images[j] for j in range(1, 6)):
            return g
    return None

for name, w in [('xi', XI), ('T=(s2s3s4s5)^5', TW)]:
    im = word_aut(w)
    nontriv = any(im[j] != [j] for j in im)
    sph = {j: to_sphere(im[j]) for j in range(1, 6)}
    g = is_inner(sph)
    print(f"{name}: braid length {len(w)}, exponent sum {sum(1 if s>0 else -1 for s in w)}; "
          f"nontrivial in B_6 (Artin): {nontriv}; max image length {max(len(im[j]) for j in im)}; "
          f"inner on pi_1(S_0,6): {g is not None}; conjugator length {None if g is None else len(g)}"
          + ('' if g is None or len(g) > 12 else f" conjugator {g}"))

# ---------- (c) TL cell module W(6,0) over F_p ----------
P = 2**61 - 1
def matchings(n):
    if n == 0: yield (); return
    for k in range(1, n, 2):
        for left in matchings(k-1):
            for right in matchings(n-k-1):
                pairs = [(0, k)] + [(a+1, b+1) for a, b in left] + [(a+k+1, b+k+1) for a, b in right]
                yield tuple(sorted(pairs))
basis = list(matchings(6)); ix = {b: i for i, b in enumerate(basis)}; D = len(basis)
def partner(m, p):
    for a, b in m:
        if a == p: return b
        if b == p: return a
def e_action(i, m):  # e_i on strands i-1,i (0-based i-1,i); returns (new_matching, loop?)
    a, b = i-1, i
    if partner(m, a) == b: return m, True
    pa, pb = partner(m, a), partner(m, b)
    new = [pr for pr in m if a not in pr and b not in pr] + [(a, b), tuple(sorted((pa, pb)))]
    return tuple(sorted(new)), False
def matmul(X, Y):
    return [[sum(X[r][k]*Y[k][c] for k in range(D)) % P for c in range(D)] for r in range(D)]
def gen_mat(g, A):
    Ai = pow(A, P-2, P); delta = (-A*A - Ai*Ai) % P
    s, t = (A, Ai) if g > 0 else (Ai, A)  # sigma = A + A^-1 e ; sigma^-1 = A^-1 + A e
    M = [[0]*D for _ in range(D)]
    for c, m in enumerate(basis):
        M[c][c] = (M[c][c] + s) % P
        nm, loop = e_action(abs(g), m)
        r = ix[nm]
        M[r][c] = (M[r][c] + t*(delta if loop else 1)) % P
    return M
def rho(w, A):
    M = [[int(r == c) for c in range(D)] for r in range(D)]
    for g in w: M = matmul(M, gen_mat(g, A))
    return M
random.seed(1)
for trial in range(3):
    A = random.randrange(2, P-1)
    Mx = rho(XI, A); Mt = rho(TW, A)
    is_id = all(Mx[r][c] == int(r == c) for r in range(D) for c in range(D))
    scal = Mt[0][0]
    is_scalar = all(Mt[r][c] == (scal if r == c else 0) for r in range(D) for c in range(D))
    Am12 = pow(pow(A, P-2, P), 12, P)
    # sanity: braid relation and sigma*sigma^-1
    br = rho([1,2,1], A) == rho([2,1,2], A) and rho([3,-3], A) == [[int(r==c) for c in range(D)] for r in range(D)]
    print(f"W(6,0) trial {trial}: dim {D}; braid rel ok {br}; rho(xi)==I {is_id}; rho(T) scalar {is_scalar}; scalar==A^-12 {scal==Am12}")

# ---------- (d) reduced Burau (unreduced, via Artin/Fox not needed): use standard unreduced Burau ----------
def burau_gen(g, t, n=6):
    i = abs(g)-1
    M = [[int(r == c) for c in range(n)] for r in range(n)]
    ti = pow(t, P-2, P)
    if g > 0:
        M[i][i] = (1 - t) % P; M[i][i+1] = t; M[i+1][i] = 1; M[i+1][i+1] = 0
    else:
        M[i][i] = 0; M[i][i+1] = 1; M[i+1][i] = ti; M[i+1][i+1] = (1 - ti) % P
    return M
def mm(X, Y, n=6): return [[sum(X[r][k]*Y[k][c] for k in range(n)) % P for c in range(n)] for r in range(n)]
t = random.randrange(2, P-1); M = [[int(r == c) for c in range(6)] for r in range(6)]
for g in XI: M = mm(M, burau_gen(g, t))
print("unreduced Burau_6(xi) == I at random t:", all(M[r][c] == int(r == c) for r in range(6) for c in range(6)))
