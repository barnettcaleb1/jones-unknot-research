# Independent re-check of the note's facts about Phi0 = [(s1 s2)^6, [[A14,A24],A34]].
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lp import *

I = lambda n: [[int(i == j) for j in range(n)] for i in range(n)]

def A(i, j):  # standard pure braid generator A_ij = s_{j-1}...s_{i+1} s_i^2 s_{i+1}^-1 ... s_{j-1}^-1
    up = list(range(j - 1, i, -1))
    return up + [i, i] + finv(up)

# --- sanity of the Artin action and of the chain-rule Fox matrices
assert act(4, [1, 2, 1]) == act(4, [2, 1, 2]) and act(4, [1, 3]) == act(4, [3, 1])
assert is_trivial(4, [2, -2]) and is_trivial(4, [-3, 3])
for i in (1, 2, 3):
    assert act_word([i], [4, 3, 2, 1]) == [4, 3, 2, 1]   # ccw boundary loop fixed
for w in ([1, 2, -1, 3, 3, -2], [2, 2, 1, -3, -1, 2, 3]):
    assert fox_burau(4, w) == fox_burau_direct(4, w)     # chain rule agrees with direct Fox calculus
assert fox_burau(4, [1, 2, 1]) == fox_burau(4, [2, 1, 2])
assert burau(4, [1, 2, 1]) == burau(4, [2, 1, 2])

s = [1, 2] * 6
b = fcomm(fcomm(A(1, 4), A(2, 4)), A(3, 4))
phi0 = fcomm(s, b)
print("word length of Phi0 in sigmas:", len(phi0))

for name, rep in (("standard unreduced Burau ", lambda n, br: burau(n, br)),
                  ("homological (Fox) Burau  ", lambda n, br: fox_burau(n, br))):
    for n in (4, 5):
        R = rep(n, phi0)
        D = msub(R, meye(n))
        nz = [x for r in D for x in r if x]
        depth = min(tplus1_adic(x) for x in nz) if nz else None
        print(f"{name} B{n}: ==I as Laurent matrix? {mis_eye(R)}; (t+1)-adic depth of rho-I = {depth}; "
              f"at t=-1 ==I? {meval(R,-1)==I(n)}; at t=2 ==I? {meval(R,2)==I(n)}; at t=3 ==I? {meval(R,3)==I(n)}")
    R3 = rep(4, s)
    print(f"   rho((s1s2)^6) at t=-1 ==I? {meval(R3,-1)==I(4)}; as Laurent ==I? {mis_eye(R3)}")
    R2 = rep(3, [1, 2] * 3)
    print("   rho_3((s1s2)^3) =", [[dict(sorted(x.items())) for x in r] for r in R2])

# --- nontrivial & Brunnian.  B_3 Burau is faithful (Magnus-Peluso), so it certifies triviality in B_3.
print("permutation of Phi0:", perm(phi0, 4), "(pure iff identity)")
for k in range(1, 5):
    w3, _ = delete_strand(phi0, k, 4)
    print(f"delete strand {k}: deleted word length {len(w3)}; Burau_3 of it == I (=> trivial in B3)? {mis_eye(burau(3, w3))}")
w3b, _ = delete_strand(b, 4, 4)
print("b pure?", perm(b, 4) == [1, 2, 3, 4], " b nontrivial (Burau_4(b) != I)?", not mis_eye(burau(4, b)))

# --- Phi0 in K4 and Phi0 = [delta^-2, b], delta = Delta_3^-2 Delta_4^2 (all short words: Artin action OK)
D3sq = [1, 2] * 3
D4sq = [1, 2, 3] * 4
for i in (1, 2, 3):
    assert act(4, D4sq + [i]) == act(4, [i] + D4sq)   # Delta_4^2 central
delta = finv(D3sq) + D4sq
d3w, _ = delete_strand(delta, 4, 4)
print("delta pure?", perm(delta, 4) == [1, 2, 3, 4], "; forget p4 gives trivial (delta in K4)?", is_trivial(3, d3w))
for order in ([1, 2, 3], [3, 2, 1]):
    w = sum((A(i, 4) for i in order), [])
    print(f"delta == A_{order[0]}4 A_{order[1]}4 A_{order[2]}4 ?", act(4, delta) == act(4, w))
# conjugation by Delta_3^2 on K4 equals conjugation by delta^-1 (test on the generators A_i4)
for i in (1, 2, 3):
    lhs = D3sq + A(i, 4) + finv(D3sq)
    rhs = finv(delta) + A(i, 4) + delta
    assert act(4, lhs) == act(4, rhs)
print("conj by Delta_3^2 == conj by delta^-1 on A_14, A_24, A_34: yes  =>  Phi0 = [delta^-2, b]")
