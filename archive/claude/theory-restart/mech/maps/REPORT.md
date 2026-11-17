# REPORT: lens MAPS (bigraded replacement maps and triangles)

Author: lens agent MAPS, 15 November 2026. Coefficients F_2 unless said otherwise. Labels: PROVED / DERIVED FROM DATA / CONJECTURED.
"Machine-checked" = exact F_2 linear algebra on explicit type D structures with my own code (scripts/typeD.py), not kht++.
Nothing here proves Lemma Q or the conjecture.

## 0. Verdict

The lens cannot produce TILT, OVERHANG or the extreme-coefficient statement, and it cannot exclude B. The reason is exact:

  (BLINDNESS, Theorem B below, PROVED) On the special curve s4(infinity), each of the three puncture classes D_bullet, D_circ, S^2
  (hence H and every element of the augmentation ideal of the centre of the quiver algebra) is null-homotopic, by explicit homotopies.
  Every replacement map in Alishahi / Iltgen-Lewark-Marino / Lewark-Marino-Zibrowius, in the rational slot or inside T, comes in a
  pair (F, G) whose two composites are homotopic to such a central element times the identity. So these pairs can be taken to be zero
  on every s4-summand, whatever its bigrading. All constraints of this lens are therefore invariant under adding, deleting and
  regrading s4-summands; TILT and OVERHANG are not.

What the lens does give (all PROVED, tested on data): the pawn of K_nu, a dictionary for the position of every special block relative
to the pawn (Theorem C), and a crossing-change lemma for the tangle slot (Lemma T) that constrains the arc of BN~(T) only.
One by-product may matter to other lenses: the non-central morphisms between two specials on adjacent levels exist only in a tilted
window (Section 5).

## 1. Conventions used (all standard; checked against kht++ output)

- Idempotents: b = kht++ "⬮" = KWZ bullet = slope 0; c = "⬯" = circ = slope infinity. a(0) = [b], a(infinity) = [c].
- Centre: D_b (loop at the puncture BL), D_c (loop at TR), S^2 (loop at BR), H = D_b + D_c + S^2. A tangle whose non-special arc misses
  a puncture has that puncture class null-homotopic (LMZ arXiv:2409.05743 Lemma 3.13, from KWZ-linear Lemma 5.11).
  Our T has the connectivity of Q_0: D_c ~ 0 on DD(T). The fillings Q_{-1/nu}, nu even, and Q_infinity have D_b ~ 0. Dots at the four
  ends, as central elements: X_TL = 0, X_TR = D_c, X_BL = D_b, X_BR = D_b + D_c; moving a dot across one crossing along a strand adds H.
- K_nu := T(1/nu), nu even, nu != 0. Sign: nu > 0 means the |nu| crossings of the twist region are POSITIVE for the knot orientation
  (kht++ word T.x0^nu.u1, "slope +1/nu" of lit/kht/REPORT.md); nu < 0 negative (T.y0^|nu|.u1).
- Kh~(K_nu) = H_* Mor(tau_nu, DD_1(T)), tau_nu = [c(-n,-2n) -S-> b(1-n,1-2n) -D-> b -S^2-> b -D-> ... -> b(0,-1)] for nu = n > 0 and its
  mirror for nu < 0; DD_1(T) = H-cone of DD(T) in the NORMALIZED frame (orientation of T induced by the unknot T(infinity)).
- Normalized coordinates of a special printed "s4(inf) q^c delta_^d": (c~, d~) := (c - 24j, d - 4j). In this frame r_1(k) has mean
  quantum grading k(|k|+2)/(|k|+1) and printed level "delta| 1/2", P = sum (-1)^{c~/2 - d~} q^{c~}, the virtual string is at offsets
  4 + 8i (k > 0) or 4 - 8i (k < 0), and TILT/OVERHANG read the same with (c~, d~). Mirror: (c~, d~, k, nu) -> (-c~, 1 - d~, -k, -nu).
  (Checked: 3_1 (14,5), j=1 -> (-10,1); 4_1^1 -> (-2,1), (-8,2); 5_1 -> (-18,1), (-16,1); all confirmed by closures, Section 6.)

## 2. What the maps and triangles say for the family (question 1)

### 2.1 The maps (PROVED; explicit; machine-checked for |nu| <= 4)
For n > 0 even, phi: [c] -> tau_n, c |-> S.b_n and psi: tau_n -> [c], b_n |-> S.c are chain maps of quantum degrees -2 and 0 and
homological degree 0, with psi phi = S^2.id and phi psi ~ S^2.id (homotopy: b_1 |-> S.c_0, b_{2i+1} |-> b_{2i}). For n odd psi is not a
chain map and no such pair exists (machine check n = 3). No pair with composite D_b, D_c or H exists (machine check).
Since D_b ~ 0 on tau_n and D_c ~ 0 on DD(T), S^2 acts as H on every closure complex, so pre-composition gives, for nu > 0,
  f: BN~(K_nu) -> BN~(U) of q-degree -2,  g: BN~(U) -> BN~(K_nu) of q-degree 0,  gf ~ H, fg ~ H,
and the mirror statement (degrees 0, -2) for nu < 0. In the language of LMZ Thm 5.6 the replacement U -> K_nu is a t-bar_{|nu|} move
(|nu| crossings between two antiparallel strands), alpha in {0,1}:  (1,0) in Lambda(K_nu, U) for nu > 0, (0,1) for nu < 0, over Z.
So all K_nu, not only K_{+-2}, carry maps with the crossing-change degrees.

### 2.2 Theorem A (PROVED): over a field the whole content is "unit bars + pawn window"
LMZ Prop 5.20: for a knot K and a field F,
    Lambda(K;F) = { (a,b) : a + b >= u(K;F), a >= s_F(K)/2, b >= -s_F(K)/2 },   u = maximal H-torsion order.
Hence, for each even nu != 0:  [(1,0) resp. (0,1) lies in Lambda(K_nu;F)]  <=>  [u(K_nu;F) <= 1 and s_F(K_nu) in {0, 2 sgn(nu)}].
Nothing else can be extracted from the existence and bidegrees of f, g over a field: the knights carry no positional information
(f = g = 0 on them). LMZ Prop 3.31 (|u_i(K_1) - u_i(K_2)| <= lambda(K_1,K_2) in each homological degree i) gives u_i(K_nu) <= 1 for
all i, which is the same statement.

Pawn formula (PROVED from STRUCTURE + unit bars + pairing; values machine-checked for |k| <= 12, |nu| <= 6 and on data):
the block of r_1(k) in Kh~(K_nu) is the reduced Khovanov homology of the double twist knot Q_k(1/nu), of odd dimension |1 - nu k|,
on one diagonal; every special block has even dimension; unit bars stay on a diagonal; so the pawn lies on the diagonal of the
rational block, and
    s(K_nu) = 2([k > 0] - [nu < 0])  for k != 0,     s(K_nu) = 0  for k = 0.
This is consistent with Thm 5.6 (s in {0, 2 sgn nu}) and is not constrained further by it. For k = 0 the set
Lambda(K_nu;F) = {a + b >= 1, a >= 0, b >= 0} is the same for all even nu != 0 and all non-rational T with k = 0.

### 2.3 Odd slopes (PROVED statement, DERIVED FROM DATA illustration)
All closures T(p/q) with p, q odd are pairwise related by one proper rational replacement. Prop 3.31 gives |u_i - u_i'| <= 1 in every
homological degree between any two of them; if one of them has only unit bars, all have bars of length <= 2. Trefoil: T(-5) = T(2,5)
is thin; every K_n with n odd, |n| <= 9, and every integer closure T(m), -4 < m <= 7, has exactly one H^2 bar (source in homological
degree 4 wherever the list was inspected). Long bars can only come from the pair (arc of BN~(T), filling arc): a compact component that
is an s4-cycle is H-annihilated (Lemma B1) and contributes unit bars to every closure.

### 2.4 Triangles (PROVED: no constraint)
The skein triangle through the twist region relates K_nu, K_{nu+-1} and T(0); the unknot is a smoothing of K_nu only for nu = +-1
(K_{+-1} = T(+-1)); the triangles with the unknot are those of the integer closures (T(m), T(m+1), U) (Watson's inverse system).
All these triangles are induced by morphisms between filling arcs, so they split as direct sums over the components of the multicurve;
on each component the three dimensions are Delta-additive (|1 - (nu+1)k|, |1 - nu k|, |k|; 4|nu+1|, 4|nu|, 4), so every long exact
sequence is short exact on each component and holds for every configuration of linear curves, with any gradings.

## 3. The negative result (questions 2 and 3)

### 3.1 Lemma B1 (PROVED; explicit; machine-checked): the puncture classes die on s4(infinity)
Write s4(infinity) as the cycle g1..g12 with idempotents b,c,c,c,c,b,b,c,c,c,c,b and differential
  g1->g2 (S), g2->g3 (D), g3->g4 (S^2), g4->g5 (D), g5->g6 (S), g6->g7 (D), g8->g7 (S), g9->g8 (D), g10->g9 (S^2), g11->g10 (D),
  g12->g11 (S), g1->g12 (D)      (kht++: ⬮~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—).
Then, exactly (not only up to homotopy), d K + K d = z.id for
  z = D_b:  K_b(g_{13-i}) = g_i, i = 1..6 (reflection of the lower branch onto the upper one);
  z = D_c:  K_c(g3) = g2, K_c(g5) = g4, K_c(g8) = g9, K_c(g10) = g11;
  z = S^2:  K_s(g2) = S g1, K_s(g4) = g3, K_s(g6) = S g5, K_s(g7) = S g8, K_s(g9) = g10, K_s(g11) = S g12.
So D_b ~ D_c ~ S^2 ~ H ~ 0 on s4(infinity), in every grading shift. Contrast (machine check): on r_1(k) and on the arcs of BN~(T),
D_c ~ 0 but D_b and S^2 are not null-homotopic (on r_1(k): D_b ~ S^2 != 0). All 833 compact components of BN~ in the table of 138 are
this same 12-generator cycle (DERIVED FROM DATA), so Lemma B1 applies to every compact component seen so far, in BN~ and in Kh~.
Not checked: longer specials s_2n, n > 1 (none available), and fields other than F_2 (the homotopies are sign-sensitive).

### 3.2 Theorem B (PROVED)
Let N, N' be direct sums of bigrading shifts of s4(infinity), X = X_0 + N, Y = Y_0 + N' type D structures, z a central element without
constant term. If F_0: X_0 -> Y_0, G_0: Y_0 -> X_0 are homogeneous with G_0 F_0 ~ z.id and F_0 G_0 ~ z.id, then F = F_0 + 0, G = G_0 + 0
are homogeneous of the same bidegrees with GF ~ z.id_X, FG ~ z.id_Y. (Immediate from B1.) Consequences:

(a) Rational slot, naturality. The proof of LMZ Lemma 3.17 (maps on tangles induce maps on closures) uses only: the puncture class of the filling's connectivity is
null-homotopic on the fillings, the one of T's connectivity is null-homotopic on DD(T), and centrality. So for EVERY type D structure X
with D_c.id_X ~ 0 the maps phi, psi of 2.1 induce f, g between the closure complexes of X with gf ~ H ~ fg and the same bidegrees as for a
tangle. Moreover the induced maps respect any direct sum decomposition of X, and on a compact summand gamma with HF(a(infinity), gamma) = 0
they are null-homotopic (they factor through an acyclic complex). The maps see the arc of BN~(T) and nothing else.

(b) B. B = a(0) + S + hS has D_c ~ 0 (B1), unknot closure, and its closure maps are (those of the trivial tangle) + 0:
f = id or H on the pawn, zero elsewhere. There is no degree obstruction. Sharper: Lambda(B(1/nu); F_2) = {a + b >= 1, a, b >= 0}
(realized by f = H^a, g = H^b on the pawn and zero elsewhere), and this is the largest value Lambda can take on a non-trivial knot with
s = 0: over a field Lambda(K;F) is contained in it by LMZ Props 5.19 and 5.20, and Lambda(K;Z) is contained in Lambda(K;F). So every
statement "(a,b) in Lambda(K_nu)" that is true for one actual non-rational tangle with k = 0 is true for B, and Lambda(B(1/nu);F_2)
EQUALS Lambda(K_nu;F_2) for every such tangle (2.2). (For other rings the same holds wherever Lemma B1 holds; not checked.)
Machine check (scripts/B_model.py): Kh~(B(infinity)) = F at (0,0); chi(Kh~(B(1/nu))) = 1 for nu = 2, -2, 4; in Kh~(B(1/4)) the top
quantum degree 2 is occupied in homological degrees 0 and 1 (the closure form of the failure of TILT).

(c) Tangle slot. See Lemma T (Section 4.3): crossing changes inside T also have central composites (H, S^2 or D_b), so by B1 they are blind
to s4-summands as well. Machine check: B and a(0) = DD(Q_0) are interleaved by maps of bidegrees (0,0), (0,-2) for each of the composites
H, S^2, D_b; as far as such maps can tell, B is one crossing change away from the trivial tangle.

(d) No implication to TILT or OVERHANG. The class of formal objects satisfying every constraint of the lens is closed under regrading,
adding and deleting s4-summands (parity of q aside). TILT fails on B. OVERHANG fails on B' := (arc of the 5_1 quotient, (k,j) = (-8,1))
+ q^{2m} (its compact component), m >= 1: the two specials move from offsets (-18,-16) to (-18+2m, -16+2m) on level 1 while the bottom of
the virtual string stays at -12; all maps, triangles, unit bars and the unknot closure are unchanged. So neither law, nor the
extreme-coefficient statement, follows from this lens. For OVERHANG carried by arc specials the statement would be about the arc alone
(ARC LAW), which this lens does see; I did not pursue it.

### 3.3 The summands of B occur inside actual tangles (DERIVED FROM DATA)
In the two-bridge run (198 quotients with BN~ data) three tangles contain two compact components gamma, h^{-1} gamma with the same
quantum grading on adjacent levels: b29_26-1 (k,j) = (-16,3), q = 34, levels 13, 14; b35_26-1 (-4,1), q = 10, levels 5, 6;
b35_32-1 (-20,3), q = 28, levels 13, 14 (script scripts/blike2.py). In b35_26-1 the compact components are at q = 10,12,14,16 on level 5
and q = 4,6,8,10 on level 6. None occurs in the table of 138 (there adjacent levels differ by q-shifts -8, -6, -4, -2 only).
So S + hS is realized as a direct summand of an actual BN~(T), next to other components. Any realization input that excludes B must be
non-additive: it has to see the whole configuration (what else is present at the extremes), not a property of single components or of
pairs of components. Constraints coming from natural transformations between pairing functors HF(X, -) are additive, which is a second,
independent reason why this lens fails.

## 4. Positions: the special part relative to the pawn (question 4)

### 4.1 Theorem C (structure PROVED from STRUCTURE with all specials s4, LMZ unit bars, KWZ pairing; the explicit ranges are
machine-checked for |nu| <= 8 (special blocks) and |nu| <= 6, |k| <= 12 (rational blocks) and confirmed by kht++ on 3_1, 4_1^1, 5_1;
the uniform statement in nu is a routine induction over twists that I did not write out)
For nu even, nu != 0, Kh~(K_nu) = R + sum over specials of Block(c~, d~), each summand on one delta-diagonal, all bars of BN~(K_nu) of
length one and inside a diagonal, where
- R (from r_1(k)) lies on delta_R = [k > 0] - [nu < 0] (k != 0), delta_R = 0 (k = 0); it has dimension |1 - nu k| and quantum range
  k < 0: [2k, 2nu] (nu > 0), [2k + 2nu, -2] (nu < 0);   k > 0: [2, 2k + 2nu] (nu > 0), [2nu, 2k] (nu < 0);   k = 0: {0};
  it contains the pawn, at (h,q) = (0, 2 delta_R).
- Block(c~, d~) lies on delta = d~ - [nu < 0], has quantum range [c~ - 4 + min(0, 2nu), c~ + 4 + max(0, 2nu)] and Poincare polynomial
  t^{m}(1 + t^2)(1 + t^3)[|nu|]_t, t^i <-> (h_min + i, q_min + 2i), h_min = q_min/2 - delta. One end of the block is fixed (c~ - 4 for
  nu > 0, c~ + 4 for nu < 0), the other moves with nu.
PAWN LEVEL: the specials on the pawn's diagonal are exactly those of normalized level d~ = [k > 0] (k != 0), resp. d~ = [nu < 0] (k = 0).
Equivalently r_1(k) behaves as a string of virtual specials on level [k > 0] (level "1/2" for k = 0); for k < 0, nu > 0 the block of the
virtual special at offset 4 - 8i is [ -8i, 8 - 8i + 2nu ], i = 1..|k|/4, and their union is the range [2k, 2nu] of R.

### 4.2 The two laws in closure form (PROVED equivalences, given Theorem C)
For k < 0 (mirror for k > 0): OVERHANG <=> for one (equivalently every) even nu != 0, q_min(Kh~(K_nu)) <= 2k - 6 + min(0, 2nu), i.e. the
bottom of Kh~(K_nu) is special and at least 6 below the rational block. TILT at the bottom => Kh~(K_nu) in its lowest quantum degree is
supported in ONE homological degree, of rank the number of specials of minimal offset; then the lowest coefficient of V(K_nu) is +- that
number. Lemma Q needs only: the Euler characteristic of the extreme quantum degree of Kh~(K_nu) is nonzero for one nu. The maps of
Section 2 say nothing about this, since they vanish on all blocks.

### 4.3 Lemma T: crossing changes inside T (PROVED from LMZ Lemma 5.16 + planar-algebra functoriality + basepoint moving (KWZ-linear
Lemma 5.11); tested on three examples)
Let T_-, T_+ be Conway tangles with the connectivity of Q_0, equal outside one crossing, negative in T_- and positive in T_+ for a chosen
orientation of the two strands (same orientation on both). There are chain maps F: DD(T_-) -> DD(T_+) of bidegree (0,0) and
G: DD(T_+) -> DD(T_-) of bidegree (0,-2) with GF and FG both equal to (X_a - X_b).id, a, b the two incoming ends at the crossing
(F = X_a - X_b on the oriented resolution, G = identity on it). Up to homotopy:
  self-crossing of either strand:                 composite ~ H;
  crossing between the two strands, orientation induced by the unknot closure T(infinity):   composite ~ S^2;
  same crossing, one strand reversed (kht++'s printed frame):                              composite ~ D_b.
(Proof of the cases: X_a ~ X_end + (number of crossings between a and the end).H; for a knot the two incoming ends at a crossing are an
odd number of crossings apart; X_TL = 0, X_BL = D_b; reversing a strand replaces an incoming end by the end across the crossing, i.e.
adds H, and S^2 + H ~ D_b on tangles with D_c ~ 0.)
Tests (machine search over all homotopy classes of the stated bidegrees): 4_1^1 quotient at framings 0 and +2 (crossing change y1 -> x1
at the right ends): printed frame: only D_b; unknot frame (shifts h^-8 q^-24, h^-6 q^-18): only S^2. Trefoil quotient with the mixed
crossing at letter 4 changed: same two answers. Trefoil quotient with the self-crossing at letter 5 changed: T' is the rational tangle
Q_{-8} (kht++), and maps with composite H exist. (The third planned test, letter 15, timed out in kht++ and was discarded.)
Use: on arcs D_b, S^2, H are not null-homotopic, so Lemma T constrains how the arc of BN~ (hence (k,j) and the arc specials) changes
under crossing changes of T; on s4-summands it gives nothing (B1). Side observation (DERIVED FROM DATA, one example): under the mixed
crossing change at letter 4 the special of the trefoil quotient moves from printed (14,5) to (12,4).

## 5. What a map-type mechanism would have to use instead (leads; nothing proved beyond the table)

(i) Non-central morphisms. H_* End(s4(infinity)) has dimension 16, in bidegrees (h,q) (machine-checked):
  (-5,-10), (-4,-8), (-3,-6), 2x(-2,-4), (-1,-2), (0,0), (1,2) on delta = 0 and (0,-2), (1,0), (2,2), 2x(3,4), (4,6), (5,8), (6,10) on
  delta = -1; the class in degree (0,-2) is not a central element. Consequently, for two specials S at (c,d) and S' at (c',d'):
    a nonzero homotopy class of degree (0,0) S -> S' exists iff (c' - c, d' - d) is in
        {(-2,0), (0,0), (2,0), (4,0), (6,0), (8,0), (10,0)}  or  {(-10,1), (-8,1), (-6,1), (-4,1), (-2,1), (0,1), (2,1)};
    a nonzero class of degree (1,0) (an extension class, a differential of a twisted complex) S -> S' exists iff (c' - c, d' - d) is in
        {(-10,0), ..., (0,0), (2,0)}  or  {(-2,-1), (0,-1), (2,-1), ..., (10,-1)}; so an extension of an upper-level special by a
        lower-level one exists exactly in the same window as the degree (0,0) maps from the lower to the upper level.
  So morphisms from level d to level d + 1, and extensions of level d + 1 by level d, exist only when the upper special sits at an offset
  between 10 below and 2 above the lower one. All TILT steps seen (2, 4, 6, 8 downwards) lie in this window; the window alone gives
  max_{d+1} <= max_d + 2 only if consecutive levels are known to be joined by a nonzero morphism, which is a realization statement I
  cannot prove. B sits at (0,1): S + hS is the split form of Cone(id_S) ~ 0. CONJECTURED lead for the Fukaya/cube lenses: actual
  BN~(T), before splitting into components, carries a filtration (by crossings of T) whose connecting maps between specials of adjacent
  levels are these non-central classes; TILT would be a statement about which of them are nonzero at the extremes.
(ii) Over Z the complexes BN~(K_nu; Z[G]) need not split and Lambda(K_nu; Z) may be smaller than its field versions; since B is
  Lambda-maximal this can never exclude B, but it could carry information about actual tangles. Not examined.
(iii) Lemma T applied along an unknotting sequence of T controls the arc. Whether it proves the ARC LAW is open; obstruction: the
  composites multiply to zero as soon as both S^2 and D_b occur, and (S^2)^2, D_b^2 need separate treatment.

## 6. Tests on data

- Central elements: s4(infinity) all four null-homotopic (explicit homotopies verified exactly); r_1(-4): D_b, S^2 not null-homotopic;
  BN~ arcs of 3_1, 4_1^1 quotients: D_b, S^2, H not null-homotopic, D_c null-homotopic. (scripts/test_basic.py, end_table.py)
- Rational-slot maps: tau_{+-2}, tau_{+-4} versus [c]: exactly one pair, composite S^2, degrees (0,-2)/(0,0) switching with the sign;
  tau_{+-3}: none. (scripts/rational_slot.py)
- Theorem C and the pawn formula: trefoil quotient, nu = +-2, +-4: my pairing computation reproduces the kht++ closure files
  lit/kht/out/closures31/c_{x,y}0{2,4}_u1 generator by generator. New kht++ runs: 4_1^1 quotient (k = 0, j = 1) at nu = +-2 and 5_1
  quotient (k = -8, j = 1, one compact component) at nu = +-2: pawn, diagonals and quantum ranges of all blocks as predicted
  (kht/examples/mine/q41p2, q41m2, q51p2, q51m2). Pawn values: 3_1: 0 / -2; 4_1^1: 0 / 0; 5_1: 0 / -2 for nu > 0 / nu < 0.
- Lemma T: Section 4.3 (scripts/interleave*.py; kht/examples/mine/t31selfS, t31mixed, q41a).
- B: scripts/B_model.py. B-like pairs in actual data and pair statistics: scripts/blike.py, blike2.py, pairhist.py.
- kht++ runs used: 9 of 20 (q41a, q41p2, q41m2, q51a, q51p2, q51m2, t31selfS, t31selfO [timeout, discarded], t31mixed).

## 7. Not checked / limits

- Lemma B1 for longer specials s_2n(infinity), n > 1, and over fields other than F_2 or over Z (signs).
- Theorem B covers maps whose composites are central. Cobordism maps that do not come in such pairs (saddles inside T, i.e. the cube of
  resolutions of T) are outside it; in the rational slot they are still additive over components (Section 2.4).
- The identification of LMZ's normalized slope p/q for the replacement U -> K_nu was not carried out symbolically; the bidegrees were
  obtained from the explicit maps of 2.1 instead, and agree with alpha in {0,1}.
- The planar-algebra step of Lemma T (tensoring the local maps with the identity of the rest of T and delooping) is standard but I did
  not write out signs; over F_2 there are none. The parity argument for the composite was tested on three examples only.
- Theorem C assumes all specials are s4 (true in all data); for a longer special the block is the sum of its n expanded blocks.
- The window of Section 5(i) is a statement about the abstract curve; no claim that actual tangles realize any particular class.

## 8. Files
- Report: /Users/calebbarnett/jones-lanes/theory-restart/mech/maps/REPORT.md
- Code: /Users/calebbarnett/jones-lanes/theory-restart/mech/maps/scripts/{typeD.py, test_basic.py, end_table.py, closures.py,
  rational_blocks.py, special_blocks.py, rational_slot.py, B_model.py, interleave.py, interleave2.py, interleave3.py, interleave4.py, trace.py,
  blike.py, blike2.py, pairhist.py}
- kht++ inputs and outputs: /Users/calebbarnett/jones-lanes/theory-restart/mech/maps/kht/examples/mine/
- Sources read: lit/bn-torsion/src/search/2409.05743/sections/{3-lambda,5-Lambda_set}.tex (LMZ), lit/*/REPORT.md, the Codex notes.
