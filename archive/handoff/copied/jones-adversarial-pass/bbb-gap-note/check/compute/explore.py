"""Main independent computation for the BBB-GAP note (hostile referee, computation lens)."""
import sys
sys.path.insert(0, '$HOME/jones-adversarial-pass/bbb-gap-note/check/compute')
from braidlib import *

def Aij(i, j):
    """Artin/Birman standard generator: s_{j-1} ... s_{i+1} s_i^2 s_{i+1}^-1 ... s_{j-1}^-1."""
    left = list(range(j - 1, i, -1))
    return left + [i, i] + inv(left)

def linking(w, n):
    """pairwise linking numbers of a pure braid word (sum of crossing signs / 2)."""
    p = list(range(1, n + 1))
    lk = {}
    for a in w:
        k = abs(a)
        s1, s2 = p[k - 1], p[k]
        key = tuple(sorted((s1, s2)))
        lk[key] = lk.get(key, 0) + (1 if a > 0 else -1)
        p[k - 1], p[k] = p[k], p[k - 1]
    return {k: v / 2 for k, v in lk.items() if v}

print("=== 0. generators ===")
A14 = parse("s3 s2 s1 s1 s2^-1 s3^-1")
A24 = parse("s3 s2 s2 s3^-1")
A34 = parse("s3 s3")
for name, w, (i, j) in (("A14", A14, (1, 4)), ("A24", A24, (2, 4)), ("A34", A34, (3, 4))):
    print(name, w, "== Artin/Birman formula word:", w == Aij(i, j),
          "pure:", is_pure(w, 4), "linking:", linking(w, 4),
          "delete 4 trivial:", is_trivial(delete_strand(w, 4, 4), 3))
# deleting a strand not in {i,4} gives the corresponding generator of B_3
print("A14 minus strand 2 == A13 (B3):", same_braid(delete_strand(A14, 4, 2), Aij(1, 3), 3))
print("A14 minus strand 3 == A13 (B3):", same_braid(delete_strand(A14, 4, 3), Aij(1, 3), 3))
print("A24 minus strand 1 == A13 (B3):", same_braid(delete_strand(A24, 4, 1), Aij(1, 3), 3))
print("A24 minus strand 3 == A23 (B3):", same_braid(delete_strand(A24, 4, 3), Aij(2, 3), 3))
print("A34 minus strand 1 == A23 (B3):", same_braid(delete_strand(A34, 4, 1), Aij(2, 3), 3))
print("A34 minus strand 2 == A23 (B3):", same_braid(delete_strand(A34, 4, 2), Aij(2, 3), 3))

X = power([1, 2], 6)
c = comm(A14, A24)
b = comm(c, A34)
Phi0 = comm(X, b)

print("\n=== 1. purity ===")
print("perm(Phi0) =", perm(Phi0, 4), "pure:", is_pure(Phi0, 4))

print("\n=== 2. nontriviality (Artin right action on F_4) ===")
imgs = artin_right(Phi0, 4)
for j in imgs:
    print(f"  x{j} . Phi0 : reduced length {len(imgs[j])}, equals x{j}: {imgs[j] == [j]}")
print("Phi0 trivial?", is_trivial(Phi0, 4))
imgsL = artin_left(Phi0, 4)
print("left-action cross-check, trivial?", all(imgsL[j] == [j] for j in imgsL),
      "lengths", [len(imgsL[j]) for j in imgsL])

print("\n=== 3. strand deletion ===")
for d in (1, 2, 3, 4):
    dw = delete_strand(Phi0, 4, d)
    print(f"  delete strand {d}: word length {len(dw)} (reduced {len(reduce_word(dw))}), trivial in B3: {is_trivial(dw, 3)}")
# b itself
for d in (1, 2, 3, 4):
    print(f"  b: delete strand {d} trivial: {is_trivial(delete_strand(b, 4, d), 3)}")
print("  b nontrivial:", not is_trivial(b, 4))
# inner commutator under deleting strand 3 (note says 'kills ... the inner commutator')
c3 = delete_strand(c, 4, 3)
print("  inner commutator [A14,A24] after deleting strand 3 trivial?", is_trivial(c3, 3))
print("  A34 after deleting strand 3 trivial?", is_trivial(delete_strand(A34, 4, 3), 3))

print("\n=== 4. word lengths ===")
print("  unreduced concatenation length:", len(Phi0))
print("  pieces: X", len(X), "A14", len(A14), "A24", len(A24), "A34", len(A34),
      "c unreduced", len(c), "b unreduced", len(b))
print("  freely reduced: c", len(reduce_word(c)), " b", len(reduce_word(b)), " Phi0", len(reduce_word(Phi0)))
print("  reduced Phi0 word:", ' '.join(('s%d' % a) if a > 0 else ('s%d^-1' % -a) for a in reduce_word(Phi0)))

print("\n=== 8. X = Delta_3^4 ===")
D3 = [1, 2, 1]
print("  (s1 s2)^6 == (s1 s2 s1)^4 :", same_braid(X, power(D3, 4), 4))
print("  (s1 s2)^3 == (s1 s2 s1)^2 :", same_braid(power([1, 2], 3), power(D3, 2), 4))
for conv in ('U', 'UT', 'R', 'RT'):
    M = burau(X, 4, conv)
    print(f"  Burau {conv}(X): I at t=-1: {is_identity_at(M, -1)}, depth {depth(M)}")

print("\n=== 5/6/7. Burau of Phi0 ===")
convs = ('U', 'UT', 'R', 'RT')
for conv in convs:
    M = burau(Phi0, 4, conv)
    print(f"  B4 {conv}: I at -1: {is_identity_at(M, -1)}; == I as Laurent: {meq(M, mid(len(M)))}; "
          f"I at 2: {is_identity_at(M, 2)}; I at 3: {is_identity_at(M, 3)}; depth {depth(M)}")
# mirror convention (sigma_i -> generator inverse), and inverse braid
for conv in convs:
    M = burau(mirror(Phi0), 4, conv)
    print(f"  B4 {conv} mirror: I at -1: {is_identity_at(M, -1)}; depth {depth(M)}")
# stabilisations into B5
stabR = Phi0[:]                         # sigma_i -> sigma_i (new strand 5 on the right)
stabL = [a + (1 if a > 0 else -1) for a in Phi0]   # sigma_i -> sigma_{i+1} (new strand on the left)
for name, w in (("f: s_i->s_i", stabR), ("left: s_i->s_{i+1}", stabL)):
    for conv in convs:
        M = burau(w, 5, conv)
        print(f"  B5 [{name}] {conv}: I at -1: {is_identity_at(M, -1)}; == I: {meq(M, mid(len(M)))}; "
              f"I at 2: {is_identity_at(M, 2)}; depth {depth(M)}")
    print(f"  B5 [{name}] nontrivial (Artin on F_5): {not is_trivial(w, 5)}")

print("\n=== 9. Phi0 == [delta^-2, b],  delta = Delta_3^-2 Delta_4^2 ===")
D3sq = power([1, 2], 3)
D4sq = power([1, 2, 3], 4)
delta = inv(D3sq) + D4sq
print("  Delta_4^2 central:", all(same_braid(D4sq + [i], [i] + D4sq, 4) for i in (1, 2, 3)))
print("  delta pure:", is_pure(delta, 4), " delta in K4 (delete 4 trivial):", is_trivial(delete_strand(delta, 4, 4), 3))
print("  delta == A14 A24 A34:", same_braid(delta, A14 + A24 + A34, 4))
print("  Phi0 == [delta^-2, b]:", same_braid(Phi0, comm(power(delta, -2), b), 4))
print("  Delta_3^2 x Delta_3^-2 == delta^-1 x delta for x in A14,A24,A34:",
      all(same_braid(D3sq + x + inv(D3sq), inv(delta) + x + delta, 4) for x in (A14, A24, A34)))

print("\n=== 10. Phi0 in [K4,K4] ===")
# Free basis a1=A14, a2=A24, a3=A34 of K4. Word of Phi0 = [delta^-2, b], delta = a1 a2 a3.
a1, a2, a3 = [1], [2], [3]
dK = a1 + a2 + a3
cK = comm(a1, a2)
bK = comm(cK, a3)
PhiK = reduce_word(comm(power(dK, -2), bK))
sub = {1: A14, 2: A24, 3: A34}
def to_braid(fw):
    out = []
    for c_ in fw:
        out += sub[abs(c_)] if c_ > 0 else inv(sub[abs(c_)])
    return out
print("  K4-word (A-basis) reduced length:", len(PhiK))
print("  K4-word substituted == Phi0 (Artin):", same_braid(to_braid(PhiK), Phi0, 4))
es = {g: sum((1 if c_ > 0 else -1) for c_ in PhiK if abs(c_) == g) for g in (1, 2, 3)}
print("  exponent sums in A-basis:", es)
# y-basis of Fig 6.13 under the identification y1 = A34, y2 = A24 A34, y3 = A14 A24 A34 (eps = +1),
# or the inverses (eps = -1). Then A34 = y1^eps etc.
for eps in (1, -1):
    if eps == 1:
        ysub = {3: [1], 2: [2, -1], 1: [3, -2]}            # A34=y1, A24=y2 y1^-1, A14=y3 y2^-1
    else:
        ysub = {3: [-1], 2: [-2, 1], 1: [-3, 2]}           # A34=y1^-1, A24=y2^-1 y1, A14=y3^-1 y2
    yw = []
    for c_ in PhiK:
        yw += ysub[abs(c_)] if c_ > 0 else inv(ysub[abs(c_)])
    yw = reduce_word(yw)
    print(f"  y-basis (eps={eps:+d}) reduced length: {len(yw)}; first/last letters {yw[:3]} ... {yw[-3:]}")

print("\n=== extra: Moody polynomial of Phi0 via Fox calculus ===")
# x_3 . Phi0 = w x_3 w^-1 for pure Phi0; M ~ W_1 - t^{+-1} W_2 with W_j = dw/dx_j |_{x=t}
img3 = imgs[3]
# split img3 = w x3 w^-1
L3 = len(img3)
mid_ = L3 // 2
w = img3[:mid_]
assert img3 == reduce_word(w + [3] + inv(w)), "x3 image not of the form w x3 w^-1"
Wr = fox_row(w, 4)
for sgn in (1, -1):
    M = lsub(Wr[0], lmul({sgn: 1}, Wr[1]))
    nterms = sum(abs(v) for v in M.values())
    print(f"  M = W1 - t^{sgn:+d} W2: nonzero {bool(M)}, value at -1: {leval(M, -1)}, "
          f"sum|coeff| {nterms}, span [{min(M) if M else None},{max(M) if M else None}]")
# cross-check against Burau row 3: (B31 - t^s B32) == (1 - t^s) * M
B = burau(Phi0, 4, 'U')
for sgn in (1, -1):
    M = lsub(Wr[0], lmul({sgn: 1}, Wr[1]))
    lhs = lsub(B[2][0], lmul({sgn: 1}, B[2][1]))
    print(f"  (B31 - t^{sgn:+d} B32) == (1 - t^{sgn:+d}) M :", lhs == lmul(lsub(ONE, {sgn: 1}), M))

print("\n=== extra: iterated commutators [X,[X,...,b]] depth ===")
cur = b
for k in range(0, 5):
    M = burau(cur, 4, 'U')
    MT = burau(cur, 4, 'UT')
    print(f"  k={k}: reduced length {len(reduce_word(cur))}, depth U {depth(M)}, depth UT {depth(MT)}, "
          f"nontrivial (Burau != I) {not meq(M, mid(4))}")
    cur = reduce_word(comm(X, cur))
