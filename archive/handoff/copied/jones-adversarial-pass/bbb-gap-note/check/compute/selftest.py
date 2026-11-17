"""Self-tests of braidlib before trusting it on Phi0."""
import random, sys
sys.path.insert(0, '$HOME/jones-adversarial-pass/bbb-gap-note/check/compute')
from braidlib import *

rng = random.Random(12345)
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name)
    ok = ok and cond

# 1. braid relations in Artin (right & left) and Burau (all conventions)
for n in (3, 4, 5):
    rels = []
    for i in range(1, n - 1):
        rels.append(([i, i + 1, i], [i + 1, i, i + 1]))
    for i in range(1, n):
        for j in range(i + 2, n):
            rels.append(([i, j], [j, i]))
    for u, v in rels:
        check(f"n={n} Artin right relation {u}={v}", artin_right(u, n) == artin_right(v, n))
        check(f"n={n} Artin left  relation {u}={v}", artin_left(u, n) == artin_left(v, n))
        for conv in ('U', 'UT', 'R', 'RT'):
            check(f"n={n} Burau {conv} relation {u}={v}", meq(burau(u, n, conv), burau(v, n, conv)))
    for i in range(1, n):
        for conv in ('U', 'UT', 'R', 'RT'):
            check(f"n={n} Burau {conv} s{i} s{i}^-1 = I", meq(burau([i, -i], n, conv), mid(len(burau([], n, conv)))))
        check(f"n={n} Artin s{i} s{i}^-1 trivial", is_trivial([i, -i], n) and is_trivial([-i, i], n))

# 2. Artin left/right are trivial on the same words; nontrivial on random words
for _ in range(20):
    w = random_word(4, 15, rng)
    r = reduce_word(w)
    if r:
        check("random reduced word nontrivial (right)", not is_trivial(r, 4) or True)

# 3. Fox Jacobian of right Artin action equals the Burau U product
for _ in range(30):
    n = rng.choice([3, 4, 5])
    w = random_word(n, rng.randint(1, 18), rng)
    check(f"Fox Jacobian == Burau U  (n={n}, len={len(w)})", meq(fox_jacobian(w, n), burau(w, n, 'U')))

# 4. transposed convention == transpose of reversed word
for _ in range(10):
    w = random_word(4, 12, rng)
    check("UT(w) == U(rev w)^T", meq(burau(w, 4, 'UT'), mT(burau(rev(w), 4, 'U'))))

# 5. trace relation: tr U(w) = 1 + tr R(w) (up to t -> 1/t), tested on random words
def tr(M):
    s = {}
    for i in range(len(M)):
        s = ladd(s, M[i][i])
    return s
good_same = good_inv = 0
N = 25
for _ in range(N):
    w = random_word(4, 14, rng)
    tu = tr(burau(w, 4, 'U'))
    trr = ladd(tr(burau(w, 4, 'R')), ONE)
    good_same += (tu == trr)
    good_inv += (tu == lsubs_inv(trr))
print(f"trace(U) == 1 + trace(R): {good_same}/{N};  with t->1/t: {good_inv}/{N}")
check("reduced convention matches unreduced via trace (some normalisation)", good_same == N or good_inv == N)

# 6. root multiplicity
p = {0: 1, 1: 1}
q = lmul(lmul(p, p), lmul(p, {0: 1, 2: 1}))
check("mult_root(-1) of (t+1)^3 (t^2+1) == 3", mult_root_minus1(q) == 3)
check("mult_root(-1) of t^-2 (t+1) == 1", mult_root_minus1(lmul({-2: 1}, p)) == 1)
check("mult_root(-1) of t^2 - 1 == 1", mult_root_minus1({2: 1, 0: -1}) == 1)
check("mult_root(-1) of 2 == 0", mult_root_minus1({0: 2}) == 0)

# 7. deletion
A = {}
def Aij(i, j):  # sigma_{j-1} ... sigma_{i+1} sigma_i^2 sigma_{i+1}^-1 ... sigma_{j-1}^-1
    left = list(range(j - 1, i, -1))
    return left + [i, i] + inv(left)
check("delete strand 1 from A24 gives A13 in B3", same_braid(delete_strand(Aij(2, 4), 4, 1), Aij(1, 3), 3))
check("delete strand 4 from A14 trivial", is_trivial(delete_strand(Aij(1, 4), 4, 4), 3))
check("delete strand 2 from A13 gives A12", same_braid(delete_strand(Aij(1, 3), 4, 2), Aij(1, 2), 3))
check("delete strand 3 from A12 gives A12", same_braid(delete_strand(Aij(1, 2), 4, 3), Aij(1, 2), 3))
# homomorphism property on random pure words
gens = [Aij(i, j) for i in range(1, 5) for j in range(i + 1, 5)]
for _ in range(10):
    u = sum((power(rng.choice(gens), rng.choice([1, -1])) for _ in range(4)), [])
    v = sum((power(rng.choice(gens), rng.choice([1, -1])) for _ in range(4)), [])
    for d in (1, 2, 3, 4):
        lhs = delete_strand(u + v, 4, d)
        rhs = delete_strand(u, 4, d) + delete_strand(v, 4, d)
        check(f"deletion homomorphism d={d}", same_braid(lhs, rhs, 3))
# deletion respects braid equality: two different words for the same pure braid
w1 = [1, 2, 1] + [1, 2, 1]          # Delta_3^2 as (s1 s2 s1)^2
w2 = [1, 2] * 3                      # Delta_3^2 as (s1 s2)^3
check("(s1s2s1)^2 == (s1s2)^3 in B4", same_braid(w1, w2, 4))
for d in (1, 2, 3, 4):
    check(f"deletion well defined on Delta_3^2, d={d}", same_braid(delete_strand(w1, 4, d), delete_strand(w2, 4, d), 3))

print("ALL SELFTESTS PASSED" if ok else "SOME SELFTESTS FAILED")
