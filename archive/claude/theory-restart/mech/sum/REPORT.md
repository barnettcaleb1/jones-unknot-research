# Lens SUM: closure of the laws under equivariant connected sum

Status: COMPLETE (15 November 2026). Coefficients F = F_2 throughout. Markers: PROVED / DERIVED FROM DATA / CONJECTURED.
Nothing here proves Lemma Q or the conjecture.

## 0. Summary

1. **Sum rule (PROVED for factors whose specials are all s4, one step computer-assisted; verified on all 45 computed composites).**
   In centred coordinates (section 1) the specials of T_1 # T_2 are

       S_12 = (S_1 + (2k_2, 0)) ⊎ (S_2 + (2k_1, 0)) ⊎ { (c_1+c_2+4, d_1+d_2-1/2), (c_1+c_2-4, d_1+d_2+1/2) : s_i in S_i },

   with k and j additive. No cancellation occurs. The number n of specials satisfies 1 + 2 n_12 = (1 + 2 n_1)(1 + 2 n_2).
2. **Why (PROVED).** The operation is Bar-Natan's planar tensor product for the horizontal tangle sum; Q_0 (kht++ ⬮, written •) is
   its unit. Theorem A: the bigraded count G_•(T) of •-generators of the reduced type D structure BN~(T) is multiplicative under
   tangle sum, for all Conway tangles and all formal objects. G_• is a lift of J without signs: J = sum over •-generators of
   (-1)^h q^q, suitably normalised. The sum rule is Theorem A read through STRUCTURE.
3. **Closure (PROVED).** OVERHANG is closed under sum. TILT + OVERHANG is not closed as a property of the data (S, k, j): there is
   an explicit formal counterexample satisfying TILT, OVERHANG and the classical Euler constraints. The closed law is **J-TILT**:
   TILT for the J-set 𝒥(T) = bigradings of the •-generators of BN~(T) = {(2k, 0)} ⊎ (S + {(4, -1/2), (-4, +1/2)}).
   J-TILT is closed under sum, and the package {TILT, J-TILT, CENTRAL ANCHOR, OVERHANG} is closed.
4. **J-TILT (DERIVED FROM DATA: 249 distinct tangles, 0 failures)** implies non-flatness directly, with no "all specials are s4"
   hypothesis, no "4 | k" hypothesis and without OVERHANG. B violates it.
5. **Negative result (PROVED).** The sum structure is blind to realisability. Theorem A holds for every object of the category, B
   included; B ⊗ BN~(T) is again a formal object with the properties and the defect of B (checked with kht++ for the trefoil
   quotient). The extreme-coefficient property is closed and co-closed under sum. So closure reduces J-TILT and Lemma Q for
   equivariant sums to the sum-prime factors and gives nothing for a sum-prime tangle. The ~60 composites in the evidence list
   are consequences of their factors, not independent evidence.

## 1. Definitions

T is a Conway tangle with T(∞) = U, Seifert framed; Kh~(T) = r_1(k) + specials (STRUCTURE); j from qr = 24j + k(|k|+2)/(|k|+1).
kht++ prints a special as (c, d) = (q-offset, δ-level), d an integer.

**Centred coordinates.** c'' = c - 24j, d'' = d - 4j - 1/2 (a half-integer). This is the grading in which T(∞) = U sits in
bidegree (0, 0), with levels measured from the rational component (its printed δ| equals 4j + 1/2 in all 121 table entries;
DERIVED FROM DATA). Mirror: (c'', d'') -> (-c'', -d''), k -> -k. The sign of a special in P is (-1)^{c''/2 - d'' - 1/2}, and

    J = q^{2k} - (q^4 - q^-4) P''(q),     P'' = sum over specials of (-1)^{c''/2 - d'' - 1/2} q^{c''}.          (1.1)

PROVED from the brief: J = 1 + q^{-24j-4}(1 - q^8) P_tot, and q^{-24j-4}(1 - q^8) times the virtual string is 1 - q^{2k}.
The virtual string of r_1(k) is |k|/4 points on the single level d'' = +1/2 (k > 0; offsets 4, 12, ..., 2k-4) or d'' = -1/2
(k < 0; offsets -4, ..., 2k+4), with the sign a genuine special would have there.

**J-set.** E := {e_+, e_-}, e_+ = (4, -1/2), e_- = (-4, +1/2). Define the multiset in 2Z x Z

    𝒥(T) := {ρ} ⊎ (S'' + E),      ρ = (2k, 0).                                                               (1.2)

Then J = sum over (C, D) in 𝒥(T) of (-1)^{C/2 - D} q^C (immediate from (1.1)).

**Intrinsic meaning (PROVED for s4 specials; verified on 428 records, script a9.py).** Let BN~(T) be the reduced type D structure
over the Bar-Natan algebra B (no identity components; unique up to isomorphism). 𝒥(T) is the multiset of (q, δ) of its generators
in the idempotent • = Q_0 (kht++ ⬮), in the unknot-normalised grading (kht++ `-q` output minus (24j, 4j)).
Proof. cone(H) on a reduced structure is reduced (H = D + S^2 has no identity part), so the •-generators of Kh~(T) are those of
BN~(T) tensored with {q^{+1}, h^{-1}q^{-1}}. An s4(∞) at (c, d) has four •-generators, at q = c + {-5, -3, 3, 5} with
δ = d + {1/2, 1/2, -1/2, -1/2} (read off the chain); this is {(c-4, d+1/2), (c+4, d-1/2)} ⊗ {q, h^-1 q^-1}. r_1(k) has two. ∎
In kht++ (uncentred) labels: 𝒥 = {(24j + 2k, 4j)} ⊎ {(c+4, d-1), (c-4, d) : (c, d) special}.

**Laws.** TILT(S) and OVERHANG as in the brief. New:
- **J-TILT**: the levels D of 𝒥(T) are consecutive, and max C and min C on a level both strictly decrease from D to D+1.
- **CENTRAL ANCHOR**: the lowest occupied special level d'' is <= 1/2 and the highest is >= -1/2.
- **EXT**: the •-generators of BN~(T) of maximal q lie in one homological parity; same for minimal q. J-TILT implies EXT.

## 2. The sum rule: data

Factors from k138.jsonl (mirror: (c, d) -> (-c, 1-d), (k, j) -> (-k, -j)); composites from comp4.jsonl and comp5.jsonl
(65 records, 45 distinct; factors 3_1, 4_1^{1,2}, 5_1, 5_2^{1,2} and mirrors, so k_i in {0, ±4, ±8}).

DERIVED FROM DATA (script a2.py): k and j are additive and the multiset S_12 equals the rule of section 0 in **45 of 45** cases.
Uncentred form, for kht++ labels:

    S_12 = (S_1 + (24j_2 + 2k_2, 4j_2)) ⊎ (S_2 + (24j_1 + 2k_1, 4j_1)) ⊎ { (c_1+c_2+4, d_1+d_2-1), (c_1+c_2-4, d_1+d_2) }.

Example 3_1 # 3_1: S = {(14, 5)}, k = -4, j = 1 gives {(30, 9), (30, 9), (32, 9), (24, 10)}, as computed.
Compact form: **𝒥(T_1 # T_2) = 𝒥(T_1) + 𝒥(T_2)** (Minkowski sum of multisets). At the BN~ level with homological gradings: the
bigraded multiset of •-generators in the stored cxBNr file of the composite is the product of those of the factors in
**54 of 54** files, with no grading shift (script a5.py).

## 3. Derivation

### 3.1 The operation
The quotient tangle of an equivariant sum is the horizontal tangle sum T_1 + T_2: the double cover glues the two knot exteriors
along a meridional annulus, the ∞-closures connect-sum, the longitudes add. Bar-Natan's bracket is a planar algebra morphism
(Bar-Natan, Khovanov's homology for tangles and cobordisms, Theorem 2; cited from memory), so

    BN~(T_1 + T_2) ≃ BN~(T_1) ⊗ BN~(T_2),    • ⊗ • = •,   • ⊗ ◦ = ◦ ⊗ • = ◦,   ◦ ⊗ ◦ = q^{+1} ◦ ⊕ q^{-1} ◦ ,

with • = Q_0 the unit. No reduced/unreduced issue arises: B is the full endomorphism algebra of Q_0 ⊕ Q_∞ in Cob_/l
(KWZ arXiv:1910.14584 section 4, TeX labels def:Cobl, obs:delooping, thm:OmegaFullyFaithful). Over F_2 the element H is "a handle
anywhere", hence central and bilinear for ⊗, so Kh~(T_1 + T_2) = BN~(T_1) ⊗ Kh~(T_2). The orientations induced by the unknot
closures are compatible in the sum, so there is no grading shift.

kht++ `--sum` implements the vertical stacking, whose unit is ⬯. The rotation by π about the TL-BR diagonal fixes the special end,
exchanges Q_0 and Q_∞ and turns the horizontal sum into the vertical one; on chain files it swaps the symbols ⬮ and ⬯. So

    BN~(T_1 # T_2) = flip( ksum( flip BN~(T_1), flip BN~(T_2) ) ).

Checked (kht++ run 1, kht/run1.log): for T_1 = T_2 = trefoil quotient this reproduces the stored BN~ of 3_1 # 3_1 exactly
(the arc and the compact component at h^4 q^26), absolute gradings included.

### 3.2 Theorem A (PROVED)
Let ε: B -> F be the algebra map killing ι_◦ and all elements of negative quantum degree. For a type D structure X = (N, d) put
Φ_•(X) = (ι_• N, (ε ⊗ 1) d), a bigraded complex with differential of degree (1, 0), functorial up to homotopy, and
N_•(X) := H(Φ_•(X)). If X is reduced, N_•(X) is the span of its •-generators. G_•(X) := Poincaré series of N_•(X).

**Theorem A.** Φ_•(X ⊗ Y) = Φ_•(X) ⊗_F Φ_•(Y). Hence N_•(X ⊗ Y) = N_•(X) ⊗ N_•(Y) and G_•(X ⊗ Y) = G_•(X) G_•(Y).
In particular G_•(BN~(T_1 + T_2)) = G_•(BN~(T_1)) G_•(BN~(T_2)) for all Conway tangles T_1, T_2.

Proof. The generators of X ⊗ Y in idempotent • are the pairs (•, •); delooping touches only the pairs (◦, ◦). The components of
the differential between such pairs are a ⊗ id_{Q_0} and id_{Q_0} ⊗ a with a in End(Q_0). The maps a -> a ⊗ id and a -> id ⊗ a
are unital degree-preserving ring endomorphisms of End(Q_0) (functoriality of the planar operation; Q_0 + Q_0 = Q_0; the Euler
characteristic is unchanged by gluing on a product), and the degree-zero part of End(Q_0) is F·id. So they commute with ε.
Apply ε and use Künneth. ∎

Remarks. (i) The proof is characteristic-free up to signs; only F_2 was tested. (ii) It uses no property of tangles: it holds
for B and for any formal object. (iii) In kht++'s normalisation χ(N_•(BN~(T))) = q^{24j} J (the coefficient of [Q_0] in the
bracket vector), so Theorem A lifts J_12 = J_1 J_2 (Codex) to a statement without signs. (iv) The statement 𝒥_12 = 𝒥_1 + 𝒥_2,
with 𝒥 defined as the •-generators of BN~, needs no hypothesis on the specials.

### 3.3 Corollary: the sum rule (PROVED when all specials are s4)
(a) k is additive: Kh~(T_1 + T_2) contains BN~(T_1) ⊗ r_1(k_2) = Kh~(T_1 + Q_{k_2}), the image of Kh~(T_1) under k_2 twists fixing
∞ (KWZ mapping class group naturality), which contains r_1(k_1 + k_2); the rational component is unique.
(b) j is additive: y = q^{24j} J is multiplicative and j = i·y'(i)/24, because J ≡ 1 mod (1+q^2)^2.
(c) By Theorem A and section 1, 𝒥_12 = 𝒥_1 + 𝒥_2. Removing ρ_12 = ρ_1 + ρ_2 gives
S_12 + E = (S_1 + ρ_2 + E) ⊎ (S_2 + ρ_1 + E) ⊎ (S_1 + S_2 + E + E). Division by the generating function of E in the group ring
Z[Z^2] (a domain) is unique. This is the rule. ∎

Second derivation, which also shows that the sum has only s4 specials (PROVED modulo three kht++ `--sum` outputs, runs 2-4).
Kh~(T_1 + T_2) = BN~(T_1) ⊗ r_1(k_2) ⊕ ⊕_{s in S_2} BN~(T_1) ⊗ s. The first summand is the twisted Kh~(T_1). For a special s,
H·id_s ≃ 0 (KWZ arXiv:2202.01460 Lemma 5.2), so cone(H) on Y_s := BN~(T_1) ⊗ s is Y_s ⊗ (q ⊕ h^-1 q^-1); it also equals
Kh~(T_1) ⊗ s = (twisted s) ⊗ (q ⊕ h^-1 q^-1) ⊕ ⊕_{s'} s' ⊗ s. kht++ gives s4(∞) ⊗ s4(∞) = four s4(∞): for both factors at
(c, d) = (14, 5) the output is (31, 9.5), (33, 9.5), (23, 10.5), (25, 10.5) = {(32, 9), (24, 10)} ⊗ (q ⊕ h^-1 q^-1); and
BN~(T_31) ⊗ s = s ⊗ BN~(T_31) = specials at (30, 9), (32, 9), (24, 10). Krull-Schmidt gives Y_s. So "all specials are s4" and
"4 | k" are closed under sum.

Consequences (PROVED). n_•(T) := number of •-generators of BN~(T) = 1 + 2·#specials is multiplicative:
#specials_12 = n_1 + n_2 + 2 n_1 n_2, and the constant D of the rank-growth formula satisfies 1 + D_12/2 = (1 + D_1/2)(1 + D_2/2).

## 4. Closure of TILT and OVERHANG

**4.1 OVERHANG is closed (PROVED, given 3.3).** Let k = k_1 + k_2 > 0. Some k_i > 0, say k_1. Then S_1 + (2k_2, 0) ⊂ S_12 has
maximum M_1 + 2k_2 >= 2k_1 + 2 + 2k_2 = 2k + 2. The case k < 0 is the mirror; k = 0 is empty.

**4.2 TILT + OVERHANG is not closed as a property of (S, k, j) (PROVED by example; script a12.py).**
S = {(106, 1/2), (100, 3/2)}, k = 0 (the special set of 4_1^1 translated by 108). TILT holds, OVERHANG is empty,
P'' = q^100 (1 + q^6) satisfies the classical divisibility, J ≡ 1 mod (1+q^2)^2. The rule gives for S "+" S the levels
1/2: {106, 106, 216}; 3/2: {100, 100, 208, 210, 210}; 5/2: {202, 202, 204}; 7/2: {196}. The minimum rises from 100 to 202:
TILT fails. So a proof of closure must use where the specials sit relative to the rational component, which TILT and OVERHANG
do not record. This is a formal datum, not a tangle; it violates J-TILT.

**4.3 Lemma M (PROVED; Codex's Minkowski lemma, for multisets).** If X, Y are finite multisets in Z x Z or Z x (Z + 1/2) with
consecutive levels and strictly decreasing level-maxima and level-minima, then so is X + Y.
Proof. Level sets add. For the maximum at a non-bottom level D+1 take a maximising pair (D_1, D_2) with D_1 + D_2 = D + 1; one of
the D_i is not the bottom level of its set; lowering it by one gives a strictly larger value at level D. Symmetric for minima. ∎

**4.4 J-TILT is closed (PROVED).** 𝒥_12 = 𝒥_1 + 𝒥_2 and Lemma M.

**4.5 The package is closed (PROVED).** If T_1 and T_2 satisfy TILT(S), J-TILT and CENTRAL ANCHOR, then so does T_1 # T_2
(and OVERHANG by 4.1).
Proof. As sets, S_12 = (S_1 + 𝒥_2) ∪ (S_2 + 𝒥_1), because S_i + 𝒥_{3-i} = (S_i + ρ_{3-i}) ⊎ (S_1 + S_2 + E). Each is a Minkowski
sum of two tilted sets, hence tilted. If S_i has levels [a_i, b_i], CENTRAL ANCHOR makes the levels of 𝒥_i equal to
[a_i - 1/2, b_i + 1/2], so both sets have the level interval [a_1 + a_2 - 1/2, b_1 + b_2 + 1/2]. The union of two tilted sets
with the same level interval is tilted. The new interval again satisfies CENTRAL ANCHOR. ∎
Check: the rule applied to all 111,628 unordered pairs from the 472 data tangles and mirrors with at most 40 specials gives no
failure of any of the four laws (script a10.py). This tests the proof; it is not new evidence.

**4.6 Data (DERIVED FROM DATA; scripts a4.py, a10.py).** On the 249 distinct (k, S) in k138, run_3_45, doubles, comp4, comp5
(391 parsed records; one of the 249 is the trivial tangle): TILT 249/249, OVERHANG 249/249, **J-TILT 249/249**,
**CENTRAL ANCHOR 249/249**.
Logical relations (PROVED): J-TILT is not implied by TILT + OVERHANG (4.2). J-TILT does not imply TILT(S): the formal set
S = {(4, -1/2), (14, -1/2), (-4, 1/2), (-12, 3/2), (-4, 3/2)}, k = 0 satisfies J-TILT and has equal maxima on two adjacent levels
(it has a step of 18). Given TILT(S), J-TILT is equivalent to: the levels of S + E together with 0 are consecutive, and 2k lies
strictly between min(S+E on level +1) and max(S+E on level -1) whenever those levels are occupied.

**4.7 J-TILT implies non-flatness (PROVED implication).** Under J-TILT the largest C occurs only on the lowest level, hence with
one sign: the top coefficient of J is ±(multiplicity) ≠ 0; likewise the bottom. If max C > min C then J has two monomials. If
max C = min C then 𝒥 lies on one level and J = ±m q^C with m = #𝒥. So J = 1 forces 𝒥 = {(0, 0)}: BN~(T) has one •-generator,
Kh~(T) has two, those of r_1(k); T has no special (an s4 has four •-generators; for longer specials this needs their •-content,
not checked here) and is trivial. Only EXT is used. Compared with the brief's reduction, neither "all specials are s4" nor
"4 | k" nor OVERHANG is needed: the virtual string is absorbed in the single point ρ = (2k, 0) on level 0.

**4.8 Grid form.** Put u = (C + 8D)/2. A special is a vertical domino {(u, D), (u, D+1)}; a compact component of BN~ is a unit
square; ρ = (k, 0); the sign is (-1)^{u+D}. J-TILT says: levels consecutive, and u_max and u_min increase by at most 3 per level
(data: u_max by 0..3, u_min by -1..3). Equivalently: on consecutive δ-diagonals the largest and the smallest homological degree
of the •-generators drop by at least 2. B has two unit squares displaced by (Δu, ΔD) = (4, 1), that is the same q in adjacent h:
a drop of exactly 1. Actual configurations chain squares along (1, 1), e.g. 9_46^1: point (0, 0) and squares with lower-left
corners (-4, -2), (-3, -1).

## 5. What closure gives and does not give for Lemma Q

Inputs: J_12 = J_1 J_2, J ≡ 1 mod δ^2, J a unit iff J = 1 (Codex, tilt_sum_attack.md); Theorem A.

Gives (PROVED):
- A flat equivariant sum has flat factors (Codex); now also the structural version: J-TILT, TILT, CENTRAL ANCHOR, OVERHANG,
  "only s4" and "4 | k" pass from factors to sums. A minimal failure of J-TILT or of Lemma Q is sum-prime.
- EXT(T_1 # T_2) holds iff EXT(T_1) and EXT(T_2): the top-q part of a Minkowski sum is the sum of the top-q parts.
- The composites in the evidence list carry no information beyond their factors.
- A reformulation: Lemma Q follows from EXT for the bigraded vector space N_•(BN~(T)), whose Euler characteristic is q^{24j} J.

Does not give (PROVED negative):
- Nothing for sum-prime tangles. Theorem A, Lemma M and 4.1-4.5 use only the monoidal structure and hold verbatim for formal objects.
- B is not excluded. For every T, B ⊗ BN~(T) has one arc, the unknot pairing of T, the Euler class of T and H-null extra
  summands, and it violates EXT, J-TILT and TILT, because EXT is co-closed. kht++ run 5 (kht/run_B_t31.log): B ⊗ BN~(T_31) is
  the arc of T_31 plus six compact s4-shaped components, three of them the h-shifts of the other three; 27 = 9·3 •-generators.
  So no statement built from sums can be the realisation input.
- Inversions of a composite knot that exchange the summands (the doubled-strand tangles T_K) are not sums; the rule is silent there.

## 6. Structure behind the J-set (context)

- (COMPUTED by standard homological algebra; multiplicative structure and formality NOT CHECKED.) The thick subcategory generated
  by ◦ = BN~(Q_∞) is a ⊗-ideal. In the quotient, End(•) has cohomology F[D] ⊕ ⊕_{m>=1} F·w_m, where
  w_m = [S|D|S^2|D|...|D|S] spans Tor_{2m-1} over ι_◦ B ι_◦ = F[D, s]/(Ds). An arrow labelled w_m raises (h, q) by (2m+1, 4m),
  an arrow D by (1, 2); S^2 dies. So the image of BN~(T) is a complex over a ring of the shape F[D, W]/(DW), the shape of a
  knot Floer complex over F[U, V]/(UV).
- (DERIVED FROM DATA: 403 stored BN~ files, 2555 components; script a6.py.) Consecutive •-generators along a curve are always
  joined by D (873 + 4304 times; D^2 once, in 9_46^2) or by the ◦-chain S, D, S^2, D, S realising w_2 (874 + 4304 times).
  Every compact component is a square (D, w_2, D, w_2). In the 121 table entries every arc is a monotone staircase in the
  (u, D) grid whose shape depends only on (k, j) (34 values; the one exception is 9_46^2; script a11.py). This is the ARC LAW of
  the brief in grid form.
- (CONJECTURED.) The image of BN~(T_1 # T_2) is the tensor product over F[D, W]/(DW) of the images, as for knot Floer
  complexes of connected sums. By hand: staircase(3_1) ⊗ staircase(3_1) = the staircase with steps (w_2, D, w_2, D) plus one
  square, which is the stored BN~(3_1 # 3_1).

## 7. Not checked, caveats

- Bar-Natan's theorem and Drinfeld's quotient construction are cited from memory. KWZ items in 3.1 are given by TeX label.
- Fields other than F_2 were not tested; `--sum` is documented as wrong there.
- Longer specials s_{4n}(∞), n > 1: none occur. Theorem A and J-TILT do not need them; 3.3(c) and the last step of 4.7 do.
- ρ = (2k, 0) was verified only for 4 | k (all data).
- Lewark-Zibrowius arXiv:2208.13612: Lemma 3.12 concerns satellites as tangle unions; the statement about sums is Proposition
  6.12 (the arc of T + R equals the arc of Q_σ + R for R of connectivity ∞). It does not cover the sum of two tangles of
  connectivity 0 treated here.
- Data note: 29 records of run_3_45.jsonl have no special component. They are unknot diagrams written by `-qNAME:p/q`
  (e.g. b11_4-1: the stored cxCKh is the unknot); tools/tilt_analyze.py already counts them as trivial.
- kht++ runs used: 5 of 20 (all `--sum`, each under 1 second).

## 8. Files (under /Users/calebbarnett/jones-lanes/theory-restart/mech/sum)

- scripts/load.py, scripts/chains.py: loaders and chain parser.
- scripts/a2.py: sum rule on composites. a5.py: Theorem A on stored BN~ files. a9.py: 𝒥 from Kh~ equals •-generators of BN~.
  a4.py: J-TILT on all data. a10.py: CENTRAL ANCHOR and virtual sums. a12.py: formal examples of 4.2, 4.6.
  a6.py, a11.py: segments between •-generators, arc shapes, squares. a7.py, a8.py: grid pictures and statistics.
- kht/run1.log (BN~(3_1) ⊗ BN~(3_1)), kht/run_s4_s4.log, kht/run_t31_s4.log, kht/run_s4_t31.log, kht/run_B_t31.log;
  inputs in kht/examples/mine/.
