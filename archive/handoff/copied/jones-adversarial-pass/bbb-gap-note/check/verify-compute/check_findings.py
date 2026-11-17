# verify-compute: independent checks of the compute-lens findings on BBB-GAP.md
# Run: python3 -I check_findings.py
# Design: every braid identity is checked with SHORT words in the (faithful) Artin action;
# long words are handled by group theory from those short identities, plus Burau as a
# consistency check (Burau is a homomorphism, so Burau(X) != I proves X != 1).
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from braidcore import *  # noqa

T0 = time.time()
def say(*a):
    print(*a, flush=True)

say("=== 0. sanity of the toolkit ===")
for n in (3, 4, 5):
    for i in range(1, n - 1):
        assert equal_in_Bn(n, [i, i + 1, i], [i + 1, i, i + 1])
    for i in range(1, n):
        for j in range(i + 2, n):
            assert equal_in_Bn(n, [i, j], [j, i])
        assert is_trivial(n, [i, -i]) and is_trivial(n, [-i, i])
        assert mmul(burau_gen(n, i), burau_gen(n, i, True)) == meye(n)
for i in range(1, 3):
    assert burau(4, [i, i + 1, i]) == burau(4, [i + 1, i, i + 1])
assert burau(4, [1, 3]) == burau(4, [3, 1])
assert not is_trivial(4, [1, 1])
# diagrammatic deletion agrees with the Artin-quotient deletion on short pure words
for w in ([1, 1], [2, 2], [3, 3], [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [1, 2, 2, 1], [2, 1, 1, 2, 3, 3]):
    if is_pure(4, w):
        for d in range(1, 5):
            assert artin(3, delete_strand_diagram(4, w, d)) == delete_strand(4, w, d)
say("braid relations (Artin, Burau) ok; the two strand-deletion methods agree on test words")

A14, A24, A34 = A(1, 4), A(2, 4), A(3, 4)
a = [1, 2] * 6
c = comm(A14, A24)
b = comm(c, A34)
phi0 = comm(a, b)

say("\n=== 1. word lengths (finding '4': 112 vs reduced) ===")
say("A14, A24, A34 as sigma-words:", A14, A24, A34)
say("unreduced sigma-word lengths: a", len(a), " c", len(c), " b", len(b), " Phi0", len(phi0))
say("freely reduced sigma-word lengths: a", len(fred(a)), " c", len(fred(c)), " b", len(fred(b)),
    " Phi0", len(fred(phi0)))

D3 = [1, 2, 1]
D4 = [1, 2, 3, 1, 2, 1]
assert equal_in_Bn(4, a, D3 * 4)
say("(s1 s2)^6 == Delta_3^4 in B_4: True")
delta = finv(D3 * 2) + D4 * 2
cands = {
    "A14 A24 A34": A14 + A24 + A34, "A34 A24 A14": A34 + A24 + A14,
    "A24 A14 A34": A24 + A14 + A34, "A14 A34 A24": A14 + A34 + A24,
    "A24 A34 A14": A24 + A34 + A14, "A34 A14 A24": A34 + A14 + A24,
}
hits = [k for k, w in cands.items() if equal_in_Bn(4, delta, w)]
say("delta = Delta_3^-2 Delta_4^2 equals:", hits)
assert hits == ["A14 A24 A34"]
for i in (1, 2, 3):
    assert equal_in_Bn(4, D4 * 2 + [i], [i] + D4 * 2)
for g in (A14, A24, A34):
    assert equal_in_Bn(4, D3 * 2 + g + finv(D3 * 2), finv(delta) + g + delta)
say("Delta_4^2 central; Delta_3^2 g Delta_3^-2 == delta^-1 g delta for g = A14, A24, A34: ok")
say("=> since b lies in K_4 = <A14,A24,A34>, Phi0 = [Delta_3^4, b] = [delta^-2, b] with delta = A14 A24 A34")

dA = [1, 2, 3]                     # letters: 1 = A14, 2 = A24, 3 = A34
cA = comm([1], [2])
bA = comm(cA, [3])
phi0A = comm(finv(dA) * 2, bA)     # [delta^-2, b]
Aw = {1: A14, 2: A24, 3: A34}
def a2s(w):
    out = []
    for x in w:
        out += Aw[abs(x)] if x > 0 else finv(Aw[abs(x)])
    return out
# consistency check (necessary condition): equal Burau matrices
assert burau(4, a2s(phi0A)) == burau(4, phi0)
say("consistency: Burau([delta^-2,b] as sigma-word) == Burau(Phi0 sigma-word): True")
say("reduced A-basis lengths: c", len(fred(cA)), " b", len(fred(bA)), " Phi0", len(fred(phi0A)))
say("reduced A-word of Phi0 (1=A14,2=A24,3=A34):", fred(phi0A))

def to_y(wA, m):
    out = []
    for x in wA:
        out += m[abs(x)] if x > 0 else finv(m[abs(x)])
    return fred(out)
convs = {
    "y1=A34, y2=A24A34, y3=A14A24A34": {3: [1], 2: [2, -1], 1: [3, -2]},
    "y1=A34, y2=A34A24, y3=A34A24A14": {3: [1], 2: [-1, 2], 1: [-2, 3]},
}
for name, m in convs.items():
    w = to_y(phi0A, m)
    es = {k: sum((1 if x > 0 else -1) for x in w if abs(x) == k) for k in (1, 2, 3)}
    say(f"y-basis [{name}]: reduced length of Phi0 = {len(w)}; first {w[0]}, last {w[-1]}; exponent sums {es}")
    say("   word:", w)
for m2 in ([2, -1], [-1, 2]):
    for m1 in ([3, -2], [-2, 3]):
        say("   mixed identification A24->", m2, " A14->", m1, " length", len(to_y(phi0A, {3: [1], 2: m2, 1: m1})))
# the note's free-reduction step: y1^m Phi0 y1^-m starts with y1 and ends with y1^-1 once m > |Phi0|
for name, m in convs.items():
    w = to_y(phi0A, m)
    for mm in (len(w) + 1, len(w) + 5):
        conj = fred([1] * mm + w + [-1] * mm)
        assert conj[0] == 1 and conj[-1] == -1
    # smallest m that works, for information
    mmin = next(mm for mm in range(0, 200) if (lambda v: v and v[0] == 1 and v[-1] == -1)(fred([1] * mm + w + [-1] * mm)))
    say(f"   [{name}] smallest m with y1^m Phi0 y1^-m starting y1 and ending y1^-1: {mmin}")

say("\n=== 2. Brunnian property and finding T1 (deleting strand 3) ===")
say("pure: a", is_pure(4, a), " A14", is_pure(4, A14), " A24", is_pure(4, A24), " A34", is_pure(4, A34))
for i in range(1, 5):
    dc = delete_strand_diagram(4, c, i)
    db = delete_strand_diagram(4, b, i)
    da = delete_strand_diagram(4, a, i)
    dphi = delete_strand_diagram(4, phi0, i)
    say(f"  delete strand {i}: c=[A14,A24] -> trivial? {is_trivial(3, dc)};"
        f"  b -> trivial? {is_trivial(3, db)};  (s1s2)^6 -> trivial? {is_trivial(3, da)};"
        f"  Phi0 -> trivial? {is_trivial(3, dphi)}")
d3c = delete_strand_diagram(4, c, 3)
A13, A23 = A(1, 3), A(2, 3)
say("delete strand 3 from c, as a word:", d3c, " fred:", fred(d3c))
say("equals [A13, A23] in B_3?", equal_in_Bn(3, d3c, comm(A13, A23)),
    "   [A13, A23] trivial in B_3?", is_trivial(3, comm(A13, A23)))
say("delete strand 3: A14 -> A13?", equal_in_Bn(3, delete_strand_diagram(4, A14, 3), A13),
    " A24 -> A23?", equal_in_Bn(3, delete_strand_diagram(4, A24, 3), A23),
    " A34 -> 1?", is_trivial(3, delete_strand_diagram(4, A34, 3)))
say("cross-check with the Artin-quotient method on c and strand 3: nontrivial?",
    not all(v == [j] for j, v in delete_strand(4, c, 3).items()))

say("\n=== 3. Burau checks of Phi0 (supporting) ===")
for n in (4, 5):
    M = burau(n, phi0)
    I = meye(n)
    at = {tv: all(pev(M[i][j], tv) == (1 if i == j else 0) for i in range(n) for j in range(n))
          for tv in (-1, 2, 3)}
    D = [[padd(M[i][j], {0: -1} if i == j else {}) for j in range(n)] for i in range(n)]
    d1 = all(pder_at(D[i][j], -1) == 0 for i in range(n) for j in range(n))
    say(f"B_{n}: Laurent identity? {M == I}; identity at t=-1? {at[-1]}, t=2? {at[2]}, t=3? {at[3]};"
        f" depth >= 2 (all (M-I)'(-1) = 0)? {d1}")
say(f"\nelapsed {time.time() - T0:.1f}s")
