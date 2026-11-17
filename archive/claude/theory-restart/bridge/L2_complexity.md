# L2: Complexity-theory lens on the Jones unknot conjecture (JC)
(agent notes, 17 Nov 2026; written continuously; newest sections at the bottom)

## 0. Plan
1. Pin down the complexity of JONES-TRIVIAL (JT): upper bound C=P (prove), lower bounds (search).
2. Exact statement of what JC + hardness would collapse (prove).
3. Literature: Kuperberg (approximation #P-hard), Kuperberg-Samperton (coloring invariants coNP/NP-complete for knots), Alagic-Lo (quantum invariants of 3-manifolds and NP vs #P), EKT gadgets, Bigelow/Ito (braid kernels).
4. Develop the best bridge with a proposition + proof or a precise obstruction.

## 1. Definitions (fixed throughout)
- Diagram D with n crossings, writhe w. Kauffman bracket <D> in Z[A^{+-1}], V_D(t) = (-A^3)^{-w} <D> at t = A^{-4}.
- JT  = { D : V_D = V(unlink with c(D) components) }.  KJT = JT restricted to knot diagrams.
- JEQ = { (D1,D2) : V_{D1} = V_{D2} }.
- UNKNOT in NP (Hass-Lagarias-Pippenger 1999) and in coNP (Lackenby 2021; Kuperberg 2014 under GRH).

## 2. The complexity sandwich (Bridge C1). Status: easy; folklore at best, not found in print.

PROP 2.1 (upper bound). JT and KJT are in C=P; JEQ is in C=P.
Proof. <D> = sum_s A^{a(s)-b(s)} (-A^2-A^{-2})^{|s|-1}. Expanding the binomial, the coefficient of A^k is
sum over (state s, j-subset of the |s|-1 factors) of (-1)^{|s|-1} [a(s)-b(s)+2(|s|-1)-4j = k], a GapP function
of (D,k) (witness = state plus subset, sign computable in P). There are O(n) relevant k. With e_k the target
coefficients of the unlink bracket (-A^3)^w delta^{c-1} (computable in P), F(D) = sum_k (c_k(D)-e_k)^2 is in GapP
(GapP is closed under products and poly-bounded sums), and D in JT iff F(D) = 0. Same for JEQ. QED.
(Note: V is NOT a cheap polynomial-identity instance: V has degree <= n, so V = 1 iff V(t_i) = 1 at n+1 points, but
each evaluation is #P-hard except at t in {1, -1, +-i, e^{+-2pi i/3}, e^{+-pi i/3}} (Jaeger-Vertigan-Welsh 1990).
Randomised PIT gives nothing here.)

PROP 2.2 (JC puts KJT in NP cap coNP). Recognising that a diagram is a knot is in P. UNKNOT in NP (Hass-Lagarias-
Pippenger, J. ACM 46 (1999)) and in coNP (Lackenby, Adv. Math. 387 (2021); Kuperberg, Adv. Math. 256 (2014) under GRH).
So JC => KJT = UNKNOT (on knot diagrams) in NP cap coNP. (Lackenby's announced n^{O(log n)} algorithm would also
put it in quasi-P.)

PROP 2.3 (what a hardness theorem would do). Let R be a poly-time many-one reduction.
(a) If UNSAT <=_m KJT via R, then [JC => NP = coNP]. Only HLP (UNKNOT in NP) is needed.
(b) If SAT <=_m KJT, then [JC => NP = coNP]. Only Lackenby (UNKNOT in coNP) is needed.
(c) If KJT is C=P-hard, then JC => C=P in NP cap coNP => coNP in NP (coNP in C=P) and PP in NP^{C=P} in NP,
    so PH and PP collapse into NP = coNP.
(d) (counterexample extraction) If UNSAT <=_m KJT via R and NP != coNP, then infinitely many R(phi) (phi unsat) are
    counterexamples to JC. Proof: if only finitely many were knotted, an NP machine accepts unsat phi by checking
    the finite exception table or guessing an HLP normal-surface disk for R(phi). That puts UNSAT in NP. QED.
    Even a randomised (BPP) reduction gives a contradiction with PH not collapsing (coNP in BPP^{NP} => coNP in
    NP/poly => PH = Sigma_3, Yap 1983).
Reading: under NP != coNP, a hardness reduction to knot Jones-triviality IS a (non-constructive) disproof of JC.
So the counterexample lane could hunt for gadget families (reductions) instead of individual knots. Conversely,
any proof of JC must explain why every candidate hardness gadget fails for knots. Section 4 says what such a
gadget must look like.

PROP 2.4 (the invariant-detection principle, general). For a knot invariant I with I-trivial set
T_I = {K : I(K) = I(unknot)}: if T_I is coNP-hard then (NP != coNP) I does not detect the unknot; if T_I is NP-hard
then (NP != coNP) I does not detect the unknot. Sanity check against a known case: Kuperberg-Samperton
(AGT 21 (2021) 1479-1510, arXiv 1907.05981) prove almost-parsimonious #P-completeness of counting G-colourings of
knots (G nonabelian simple). The parsimonious structure means "only trivial colourings" is coNP-hard, consistent
with the (unconditional) fact that a fixed finite G never detects the unknot.

What is known closest to KJT hardness: Kuperberg, Theory of Computing 11 (2015) 183-219 (arXiv 0908.0512),
Thm 1.2: at a principal non-lattice root of unity t (order r not in {1,2,3,4,6}), deciding |V(L,t)| < a versus
> b (0<a<b) is #P-hard under Cook reductions, AND THIS HOLDS FOR KNOTS. No exact zero test, no C=P statement,
nothing on V = 1 (checked). JT for links: no hardness result found (searches: C=P / coNP / trivial Jones).

## 3. BEST BRIDGE: twist families = an S-unit Skolem problem over the function field C(A)
(TCS side: Skolem's problem for linear recurrences, decidability open over Z (Ouaknine-Worrell programme);
number-theory side: S-unit equations in function fields are EFFECTIVE (Mason-Stothers, Voloch 1985,
Brownawell-Masser, Math. Proc. Camb. Phil. Soc. 100 (1986) 427-434; Zannier, Acta Arith. 64 (1993)).
Recent number theory on exactly this shape: Darsana N - S.S. Rout, "Zeros and S-units in sums of terms of
recurrence sequences in function fields", arXiv 2408.09448 (finiteness for U_{n1}+...+U_{nr} in O_S^*).
No use of this in knot theory found (searches: Mason / S-unit / Skolem + Jones + twisting). Closest knot work:
Champanerkar-Kofman, twisting and Mahler measure (arXiv math/0404236), coefficient blocks stabilise; different.)

### 3.1 Set-up (exact)
Context C with k twist slots; slot i carries n_i half-twists. In TL_2 = R[e]/(e^2 - delta e) a horizontal twist
box is [n] = A^n (1-p) + (-A^{-3})^n p, p = e/delta (eigenvalues A, -A^{-3}); a vertical box has eigenvalues
A^{-1}, -A^{3}. Multilinearity of the bracket in the slots gives, for every n in Z^k,
   <D(n)> = sum_{eps in {0,1}^k} c_eps * s_eps(n) * A^{<l_eps, n>},   s_eps(n) = (-1)^{<eps,n>},
with c_eps in Z[A^{+-1}, 1/delta] = <C with idempotent (1-p) or p in each slot> and l_eps in {1,-3}^k
(horizontal) or {-1,3} (vertical) coordinatewise. For a knot, V = 1 iff <D> = +-A^m for some m
(V(1) = 1 and V'(1) = 0 fix sign and shift), so no writhe bookkeeping is needed. Same for the quotient-tangle
invariant J of Lemma Q (a linear functional of the bracket): J unit iff sum_eps c'_eps s_eps A^{<l_eps,n>} = +-A^m.
Define the UNIT LOCUS U(C) = { n in Z^k : <D(n)> in +-A^Z } (restricted to the parity classes giving knots).

### 3.2 Input from function fields (black box)
BM. (Brownawell-Masser; genus 0 form.) K = C(A), S a finite set of places. If u_1 + ... + u_l = 0 with u_i
S-units and no proper subsum vanishing, then H(u_i/u_j) <= C_l |S| for all i,j, C_l = (l-1)(l-2)/2.
(H = degree of a rational function. Constants differ between sources; any explicit C_l works below.
l = 3 is Mason-Stothers.)

### 3.3 THEOREM S (structure of unit loci). Fix C. Then U(C) = F  union  (b_1 + L_1) u ... u (b_r + L_r), with F
finite and each L_j a sublattice of a rational subspace W_j != 0 of the form
   W_P = { x : <l_eps - l_eps', x> = 0 for all eps, eps' in the same block of a partition P of the terms },
and on each b_j + L_j the bracket is IDENTICALLY a unit: it is a monomial for every point of the lattice coset.
Everything is effective: with N = #{eps : c_eps != 0}, S = {0, infinity} u zeros/poles of the c_eps, and
M = C_{N+1}|S| + 2 max H(c_eps), every n in U lies within distance O(M) (coordinatewise, via the l-differences)
of some W_P, and F, b_j, L_j are computable by finite linear algebra.

Proof. Let n in U, so sum_eps y_eps(n) - u A^m = 0 with y_eps = c_eps s_eps A^{<l_eps,n>}: l = N+1 S-units.
Split this vanishing sum into minimal vanishing subsums (blocks); call the partition P. No block is a singleton
(S-units are nonzero). In a block B, BM gives H(y_eps/y_eps') <= C_{|B|}|S| <= C_{N+1}|S|, and
y_eps/y_eps' = +-(c_eps/c_eps') A^{<l_eps - l_eps', n>}, so |<l_eps - l_eps', n>| <= M (subadditivity of H).
So n lies in the slab Sigma_P = { |<l_eps - l_eps', n>| <= M, eps ~_P eps' }. Finitely many P. If W_P = 0, Sigma_P
is bounded. Otherwise write n = b + w with w in W_P and b in a bounded set, and fix the parity class of w.
On W_P all terms of a block share one exponent l_B, so each block sum equals Q_{B,b}(A) * sign * A^{<l_B,w>},
where Q_{B,b} does not depend on w. Minimality at n forces Q_{B,b} = 0 for every block without the target term,
and Q_{B*,b} = unit monomial for the target block. Both conditions are independent of w, so the WHOLE coset
b + (W_P cap parity lattice) lies in U. Hence the infinite part of U is a finite union of lattice cosets on which
<D> is identically a unit, and the rest is in a bounded set. QED.

COROLLARY S1 (semilinearity / descriptive complexity). For every fixed context, the set of twist vectors giving
Jones-trivial knots (or unit J) is a semilinear (Presburger-definable) set, computable from C.
COROLLARY S2 (complexity). For fixed C, "is D(n) Jones-trivial?" is decidable in time polynomial in log|n|
(n in binary), although D(n) has ~|n| crossings, so V(D(n)) itself has exponential size. The parametric question
"does the family contain a Jones-trivial knot?" is decidable. Contrast: Skolem over Z is open, and unit/zero
problems for general weighted automata over Z are undecidable (mortality, Paterson 1970). The bracket family is
decidable because the bases A, -A^{-3} are S-units of a FUNCTION field.
COROLLARY S3 (where infinite counterexample families must live). If JC fails along a twist family, then either
the failure is sporadic (in the explicit window F) or a whole coset b + L consists of Jones-trivial knots, and on
it the bracket is identically a unit: a "bracket-invisible twist direction" (block sums of eigen-coefficients
vanish identically). In the projective, one-slot case this says: the slot's context functional kills the (1-p)
channel, i.e. <C(T)> = alpha <D(T)> (the context sees the slot only through its denominator closure).

### 3.4 Sanity computation (L2_code/twist2.py): 2-bridge family [n1] then n2 vertical twists, D-closure.
Closed form (derived by hand from the idempotents, matches the code):
 delta^2 <D(n1,n2)> = (delta^2-1)[ -A^{n1-n2} + (-1)^{n1} A^{-3n1-n2} + (-1)^{n2} A^{n1+3n2} ] + (-1)^{n1+n2} A^{3(n2-n1)}.
Grid |n_i| <= 9: monomial brackets at exactly 41 points = the line n1 = 0, the line n2 = 0, and F = {(1,-2),(-1,2),
(2,-1),(-2,1)}. This is the unknot locus n1*n2 in {0,-2} of the fraction (n1 n2 + 1)/n1. Mechanism checks:
on n1 = 0 the terms -A^{n1-n2} and A^{-3n1-n2} cancel identically (block {00,10}), and the rest merges to
delta^2 (-1)^{n2} A^{3n2}: a bracket-invisible direction, here a Reidemeister-I direction. At (1,-2) all five
terms are needed, a non-degenerate 5-term unit relation: delta^2<D> = -A^7 - 2A^3 - A^{-1} = -A^3 delta^2.
Here |S| = 14 (0, infinity, roots of A^8+A^4+1 and A^4+1). The BM window is far from sharp (spread <= ~100
predicted, 12 observed) but it is finite and explicit.

### 3.5 What this gives the program (leverage not available inside quantum topology)
- A uniform, effective replacement for case-by-case finite-window / two-candidate-twist theorems: ALL twist boxes
  of a fixed body configuration (any k, across all nodes of an arborescent tree) at once.
- "Resonance" gets a precise meaning: a vanishing subsum in a function-field unit equation. The resonant
  mirror-type products in the arborescent frontier should be exactly the partitions P with W_P != 0 where some
  block sums vanish identically. That gives a finite linear-algebra test.
- A sub-conjecture of JC that can be tested and is local: TWIST-INVISIBILITY. If a twist direction is
  bracket-invisible on a knot family, then the family is topologically trivial along it (twists cancel or are
  nugatory). A counterexample gives an infinite family of JC counterexamples, so this is the right target for
  the counterexample lane: search for bracket-invisible directions (finite algebra on the c_eps), not for knots.
- Limits (honest): this controls twist parameters only. Bodies that vary non-parametrically (the open
  "interaction between children" problem) are not covered. The BM constants are poor; Mason-Stothers gives sharp
  bounds when N = 2 (the project's one-slot results are presumably this case).

### 3.6 Second sanity check (L2_code/pretzel3.py): pretzel P(n1,n2,n3), |n_i| <= 6, knot parity classes only.
Monomial bracket at 90 points: 72 on the resonance lines {n_i = 1, n_j = -1} (P(1,-1,n): the third box is
bracket-invisible), 6 with a zero entry (permutations of (+-1,+-1,0)), and 12 sporadic points (permutations of
(-1,2,3) and (-3,-2,1)). The sporadic ones are 2-bridge with p = 6(-1+1/2+1/3) = -1, so they are unknots. So the
locus is again finite set + lattice lines, as Theorem S predicts, and every point is an unknot (JC is known here).
Next useful runs (not done; cheap): the project's arborescent bodies with k = 2..4 slots. List the partitions P
with W_P != 0 whose non-target block sums vanish identically, then check each such direction topologically.

## 4. What a hardness reduction would have to look like; the link problem

4.1 Necessary features of any reduction UNSAT -> KJT (knots). Unconditional, with all checks in P:
 (i) R(phi), phi unsat, must pass every polynomial-time consequence of V = 1: det = 1 (V(-1)), Arf = 0 (V(i)),
     a_2 = 0 (V''(1) = -6 a_2), and more generally V == 1 mod (t-1)^k for each FIXED k. Each such jet is a
     finite-type invariant of order <= k, so it has a Gauss-diagram formula with <= k arrows (Goussarov-Polyak-Viro,
     Topology 39 (2000)) and can be evaluated in time n^{O(k)}. So the hardness must live in jets of unbounded order.
     This matches the project's FT-DEEP result (no finite jet at t = -1 detects).
 (ii) Unbounded treewidth: for treewidth <= w the bracket is computable in poly time (Makowsky 2001, bounded-tree-width
     Kauffman brackets), so KJT restricted to bounded treewidth is in P.
 (iii) Not from twist parameters on a fixed context: by Theorem S the parametric unit locus is semilinear and
     decidable in time poly(log|n|). The gadget contexts must therefore grow with phi.
 (iv) The divisibility constraints do NOT limit the algebraic encoding room. Values N(phi) g(t) with g in the
     ideal ((1-t)(1-t^3)) intersected with the evaluation constraints form a full-rank lattice. The real constraint
     is realisability by knots, not arithmetic. (So the answer to "do our divisibility constraints limit the encoding
     room" is: no, not by themselves.)
 Under JC and NP != coNP no such R exists (Prop 2.3), so JC can be read as a NON-EXISTENCE theorem for
 knot gadgets satisfying (i)-(iii).

4.2 Links (open problem, sharpened). Is JT_c (c-component links, c >= 2) coNP-hard or C=P-hard? Not in the
literature that I found. EKT (Topology 42 (2003) 155-169, Prop 2.1'): <H(T,U)> = br(T)^T H br(U), with
H = [[h00,h01],[h01,h11]], h01 = delta^2 and h11 = delta, so JT(H(T,U)) is a BILINEAR test on bracket vectors.
PROP 4.2 (reduction to one gadget). Suppose phi -> T_phi is poly-time, with br(T_phi) = mu_phi((0,1) + N(phi) v)
for a fixed v = (v1,v2), units mu_phi, N a GapP function whose zero set is coNP-hard (e.g. #SAT), and T_phi
connected like the infinity tangle (so that H(T_phi, inf) has 2 components). Put w = v1*delta + v2 and assume w
has a root that is not a root of unity. Then phi -> H(T_phi, inf) reduces UNSAT to JT_2.
Proof: br(inf) = (0,1) and H(0,1)^T = (delta^2, delta), so <H(T_phi,inf)> = mu_phi * delta * (1 + N(phi) w).
JT_2 holds iff 1 + N w = +-A^k. If N = 0 this holds. If N != 0 then N w = +-A^k - 1, whose roots are all roots of
unity, which contradicts the choice of w. QED.
So link hardness reduces to an AFFINE COUNTING TANGLE: an exact encoding of a GapP count into a 2-tangle bracket.
Missing ingredient, stated precisely: brackets are U_q(sl_2)-intertwiners (Temperley-Lieb), so classical gates on
"spin" variables are impossible. An encoding must live in fusion (multiplicity) spaces and needs EXACT synthesis
of a GapP-universal gate set (Toffoli + a Hadamard-like gate, cf. coC=P = NQP, Fenner-Green-Homer-Pruim 1999) by
braids/tangles at generic A. Kuperberg's #P-hardness (2015) uses Solovay-Kitaev, which is approximate, so it cannot
give exact zero tests. Kuperberg-Samperton's exact "zombie" encodings work for finite groups (permutation actions),
not for the linear TL action. This is the precise gap.
Knot contrast: for knots, Sikora (CJM 76 (2024), arXiv 2005.08162) shows JC <=> bracket detects rational tangles.
A knot version of Prop 4.2 would need br(T_phi) = br(rational) iff N(phi) = 0, and rationality is in NP
(normal surfaces), so JC + NP != coNP forbids it. That is the formal sense in which "affine counting tangles cannot
exist for knot closures" under JC.

4.3 The jet filtration (side bridge, quantitative). F_k = {K : V_K == 1 mod (t-1)^k} is in P for fixed k (4.1(i)),
and KJT = F_{n+1} (span V <= n). Vassiliev k-trivial knots (Ohyama, Proc. AMS 123 (1995); Stanford's
lower-central-series braids) lie in F_{k+1}. Their crossing numbers grow like 2^{O(k)} (nested commutators; to be
checked), so detection by jets of order c log n is the best one could hope for. QUESTION (quantitative JC): does
V_K == 1 mod (t-1)^{C log c(K)} force K = unknot? If yes: JC, plus unknot detection in quasi-polynomial time by
finite-type invariants, matching Lackenby's announced n^{O(log n)} bound from a completely different direction.
Cheap test (not run, since there is no Sage or SnapPy bracket here): the maximal ord_{t=1}(V-1) by crossing number
in the knot tables.

## 5. Pointer (not developed): the two ends are the two places 0 and infinity of Q(A) (trees)
Width-two channel matrices and twist operators lie in GL_2(Z[A^{+-1}]) with unit determinant (a twist has
eigenvalues A, -A^{-3}, det = -A^{-2}). After normalising det, g acts on the Bruhat-Tits trees T_0 and T_inf of
SL_2 over C((A)) and C((1/A)), with translation length l_v(g) = -2 min(0, v(tr g)), where v_inf = -topdeg and
v_0 = bottomdeg. So "cancel at the top end" and "cancel at the bottom end" mean small translation length at inf
and at 0. The project's ADDITIVE end invariants look like additivity of translation lengths for products with
coherent axes (ping-pong). Cancelling at both ends at once asks for simultaneous non-hyperbolicity on T_0 x T_inf,
the setting of lattices in products of trees (cf. SL_2(F[A,A^{-1}])). Tools that would come with this: the ping-pong
lemma, Bass-Serre theory, and decidability of 2x2 matrix-semigroup problems (Potapov-Semukhin for SL_2(Z)).
First step: for a few width-two words, compare the project's end invariants with l_0 and l_inf of the channel
products.

## 6. Summary of bridges (status, honest)
B1 Complexity sandwich (Sec. 2). KJT in C=P; under JC in NP cap coNP; a hardness reduction would be a conditional
   disproof. Mostly a restatement with strategic value: hunt gadget families, not knots. Folklore, not in print.
B2 BEST: twist families = S-unit Skolem problem over C(A) (Sec. 3). Theorem S proved modulo Brownawell-Masser:
   unit loci are finite plus bracket-invisible lattice cosets, effective and semilinear. Checked on 2-bridge
   and pretzel families. The application is new; the tools are known number theory.
B3 Link hardness reduces to one affine counting tangle (Prop 4.2, proved). The missing ingredient is exact
   GapP-universal synthesis in Temperley-Lieb at generic A. Open.
B4 Necessary features of knot gadgets (4.1): every fixed-order jet trivial (GPV), unbounded treewidth, not
   parametric (Thm S). Divisibility does not restrict the encoding room.
B5 Quantitative JC via jets of order C log n. Gives quasi-polynomial unknot detection by finite-type invariants.
   Question only.
B6 Two ends = two places, trees (Sec. 5). Pointer only.
Files: L2_code/twist2.py, L2_code/pretzel3.py (run with tools/venv python; twist2 prints its own table on import).
