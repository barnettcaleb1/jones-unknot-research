# Digest: Boyle-Spyropoulos, "Myopic Tutte polynomials and Khovanov homology in RP^3"

Source read: arXiv:2609.40122v1 [math.GT, math.CO], submitted 30 Sep 2026 (only version), 43 pp.
The identifier on the board is correct. Statements were read from the TeX source
(src/tex/MyopicTutte.tex); numbering and page numbers are from the v1 PDF (src/paper.txt).
Announced as a talk: K. Boyle, "The myopic Tutte polynomial and link diagrammatics in RP^2",
SMRI / AGTW, 19 Aug 2026 (abstract: a new strategy toward unknot detection via the "local crossing
number", plus thinness of Kh for alternating links in RP^3).
Auxiliary sources read for section 5: Dasbach-Lowrance arXiv:1604.03501v2; Lowrance-Spyropoulos
arXiv:1707.05443v2 (the board's "Lowrance-Spyropoulos" paper; note 1707.01210 is NOT it).

STATUS: complete.

Marking convention: [BS] = stated in the paper; [DIGEST] = my own derivation or judgement, not in the paper.

## 0. Bottom line

1. The paper is mainly about alternating nullhomologous links in RP^3: a Tutte-type polynomial psi_G for
   graphs in RP^2, a Thistlethwaite-type spanning tree formula for Drobotukhina's Jones polynomial,
   a Kauffman-Murasugi-Thistlethwaite (KMT) breadth theorem for each of the two "halves" of the Jones
   polynomial, and thinness of F_2-Khovanov homology for non-local alternating links.
2. The "strategy toward T" is a 1.5-page subsection (1.1, pp. 4-5). It consists of ONE conjectural
   inequality, Conjecture 1.1(2): for a knot K in S^3 regarded as a local knot in RP^3,
   breadth(V_K) >= beta_Re(K), where beta_Re(K) = min over ALL diagrams D of K in RP^2 of
   c(D) - alpha_Re(D). The implication "Conj 1.1(2) => T" is rigorous (uses Theorem 5.3(1)).
3. Nothing is proved toward the conjecture for non-alternating local knots, and no example is given
   of a classical knot with a non-local diagram that beats its classical crossing number.
   [DIGEST] The J = 1 instance of the conjecture is logically equivalent to T (so this is a
   strengthening of T, not a reduction), and the hard step is entirely open. Two of the authors'
   own open questions (Question 5.4(1),(3)), if answered "yes" for local links, would refute
   Conjecture 1.1(2) on 8_19. As literally stated, both inequalities of Conjecture 1.1 fail on
   easy examples outside the knot case (section 4.4).
4. The paper does not mention Turaev genus, Dasbach-Lowrance, or Lowrance-Spyropoulos at all
   (zero occurrences; Lowrance is only thanked).
5. [DIGEST] Useful dictionary for the tangle programme: for a Conway tangle T with bracket vector
   [T] = x id + y e, the "antipodal closure" a(T) in RP^3 has Drobotukhina bracket x + y, and the
   paper's splitting J = J^Re + J^Im is exactly the splitting into x and y. Upsilon_n = a(Q_n).
   See section 7.

## 1. Conventions

- RP^3 minus a point = twisted I-bundle over RP^2; a diagram D lives in RP^2, drawn in the disk model
  (disk with antipodal boundary identification). Reidemeister-type moves Omega_1..Omega_5
  (Drobotukhina); Omega_4, Omega_5 push an arc, resp. a crossing, through the boundary circle (p. 8-9).
- L is local if contained in a 3-ball; nullhomologous ("class 0") if [L] = 0 in H_1(RP^3) = Z/2;
  nullhomologous <=> checkerboard-colourable diagram (p. 2). A graph G in RP^2 is local if contained
  in a disk; "cellular" = connected and non-local (p. 15).
- Kauffman bracket (Def. 2.1, p. 8): <crossing> = A<A-res> + A^{-1}<B-res>; <D u O> = (-A^2 - A^{-2})<D>
  for a crossingless class-0 circle; <class-0 unknot> = 1; <class-1 unknot> = theta. For class-0 links
  <D> lies in Z[A, A^{-1}] (Lemma 2.2 = Manolescu-Willis Lemma 2.3).
- Jones polynomial (eq. (4), p. 8): J_L(t) = (-A^3)^{-w(D)} <D> at A = t^{-1/4}; unknot = 1;
  mirror: t^{1/2} <-> t^{-1/2}.
- For nullhomologous L: J_L = J_L^Re + J_L^Im = (integer-exponent part) + (half-integer-exponent part)
  (p. 4). J_L(-1) = +-det_Re(L) +- det_Im(L) i defines the real and imaginary determinants (p. 9).
  For local L one summand is zero. For alternating L the notation J^+, J^- is used for the summands
  attached to the Tait graphs G_+, G_- (all edges positive, resp. negative).
- Unnormalised: \hat J_K(q) = (q + q^{-1}) J_K at q = -t^{1/2} (p. 2).
- Khovanov homology (sec. 2.3, pp. 12-14; splitting remark p. 39): F = Z/2 coefficients, Asaeda-Przytycki-Sikora theory.
  i = #B-resolutions, j = i + #(1) - #(X), global shift [-n_-, n_+ - 2n_-]; merge m and split Delta
  as usual; the new edge type, the "1-1 bifurcation" (resolutions with the same number of circles),
  is assigned the ZERO map. Differential of bidegree (1,0). Reduced theory normalised so that
  the unknot sits in bigrading (0,-1); Kh^{i,j} = Kh~^{i,j-1} + Kh~^{i,j+1} over F.
  Because 1-1 bifurcations act by zero, the complex of a non-local diagram of a nullhomologous
  link splits into two summands (p. 39).
- Signatures: sigma_(D,kappa) = sig(Goeritz matrix of checkerboard colouring kappa) - mu(D,kappa)
  (Gordon-Litherland type, sec. 2.2, pp. 10-12); for alternating D, sigma_+, sigma_- from G_+, G_-.
- Typos to be aware of: the displayed J_K on p. 2 is wrong (correct value in Example 2.3:
  J = 1 - t^{-1} + t^{-2} + t^{1/2} - t^{-1/2} for Drobotukhina's 3_1); Theorem 1.1 writes "J_L^+(L)";
  k_+- is defined with different signs in Theorem 1.2 and in Proposition 6.8.

## 2. Definitions

**Alternating (p. 2).** A diagram D in RP^2 is alternating if over/under passes alternate along it,
where an arc between successive crossings counts as "alternating" iff it misses the boundary circle
or meets it in 4k points. Alternating links are nullhomologous by definition.

**Myopic Tutte polynomial psi_G in Z[x,y], G embedded in RP^2 (Def. 3.1, p. 15).**
Deletion-contraction: psi_G = psi_{G-e} + psi_{G/e} for e regular (neither bridge nor loop);
psi_G = x psi_{G/e} for a bridge; psi_G = y psi_{G-e} for a loop with [e] = 0 in H_1(RP^2);
psi_G = psi_{G-e} for a loop with [e] = 1; psi = 1 for edgeless G.
State sum (Prop. 3.3, p. 16): psi_G(x,y) = sum over LOCAL spanning subgraphs H of
(x-1)^{b_0(H)-b_0(G)} (y-1)^{b_1(H)} ("myopic": non-local subgraphs are dropped).
Spanning trees (Prop. 3.5, p. 18): for connected G with ordered edges,
psi_G = sum_T x^{i(T)} y^{j(T)}, i = internal activity, j = LOCAL external activity (externally active
edges e with [Cyc(T,e)] = 0); "projectively externally active" edges ([Cyc(T,e)] = 1) get weight 1.

**Projective rank (p. 3).** alpha(G) = min{|E| : E a set of edges with G - E local}.
alpha^+-(D) = alpha(G_+-(D)).

**Signed spanning tree polynomial Psi_D (Def. 4.1, p. 23).** For a diagram D of a nullhomologous link
with signed, ordered Tait graphs G_1, G_2: Psi_D = Psi_{G_1} + Psi_{G_2}, Psi_G = sum_T prod_e mu(e,T),
weights (Table 2): L -> -A^{-3}, D -> A, l_loc -> -A^3, l_pro -> A^{-1}, d -> A^{-1}, and the inverse
monomials for negative edges (L = internally active, D = internally inactive, l = externally active
(local/projective), d = externally inactive).

**Local crossing number (Def. 1.6, p. 4).** For a nullhomologous L, eps in {Re, Im}, and a diagram D,
alpha_eps(D) = projective rank of the Tait graph of D that contributes to J^eps (via Prop. 4.4). Then
  alpha_eps(L) = min_D alpha_eps(D)        ("eps projective crossing number"),
  beta_eps(L)  = min_D [c(D) - alpha_eps(D)]  ("eps local crossing number"),
minima over ALL diagrams D in RP^2 of L. Remark (p. 4): alpha_eps(D) counts crossings whose
smoothing (in the direction compatible with that checkerboard surface) makes the surface local.
Trivially 0 <= alpha_eps, beta_eps <= c(L); "we don't know of any relationship between alpha and beta".
[DIGEST] For a local diagram, both Tait graphs are local, so alpha = 0 and c(D) - alpha(D) = c(D):
hence beta_Re(K) <= c(K) for a classical knot K, with strict inequality only if a NON-local diagram
of K does better. For a non-local diagram D of a local knot, the A-exponents of all tree weights of
one Tait graph lie in one class mod 4 and the two graphs differ by 2 mod 4 (checked from Table 2),
so one graph has Psi = <D> and the other has Psi = 0; the first is "G_Re".

**Families (Thm 5.3, Fig. 14).** Upsilon_n: two strands through the cross-cap with n crossings
(|n| = crossing number; knot for n even, 2-component link for n odd; Upsilon_0 = unknot);
its Tait graphs are a single vertex with n projective loops, and its dual.
J_{Upsilon_n} = (-1)^n ( t^{n/2} + sum_{i=0}^{n-1} (-1)^i t^{(n+1)/2 + i} ) for the orientation with
w = n (Example 2.4, p. 9; bracket in eq. (5)). V_n, W_n, X_n, Y_n, Z_n: further twist families (figures only).

## 3. Main theorems (exact statements, v1 numbering)

**Theorem 1.1 (p. 2; proof p. 41).** If L is a non-local alternating link in RP^3, then Kh(L; Z/2) is
supported on exactly four diagonals j - 2i = -sigma_+-(L) +- 1, and it is equivalent to the data
{J_L = J_L^+ + J_L^-, sigma_+(L), sigma_-(L)}.

**Theorem 1.2 (p. 2; proof p. 26).** If D is a connected, reduced, alternating diagram of a non-split,
non-local alternating link L, with checkerboard graphs G_+, G_-, then there are k_+, k_- in (1/2)Z
(the paper writes Z[1/2]) with k_+ - k_- = 1/2 and
  J_L(t) = (-1)^{w(D)} ( t^{k_+} psi_{G_+}(-t, -t^{-1}) + t^{k_-} psi_{G_-}(-t^{-1}, -t) ).
Explicitly k_+ = (3w - k_+')/4, k_- = (3w + k_-')/4, k_+-' = 2(n_+- - 1) - m, m = c(D),
n_+- = #vertices of G_+-.

**Theorem 1.3 (p. 3) = Props 3.11, 3.12 (p. 22).** For G connected non-local in RP^2, the generalised
Krushkal polynomial satisfies K_G(x,y,0,1) = psi_G(x,y) and
K_G(x,y,A,B) = sqrt(B) psi_G(x,y) + sqrt(A) psi_{G*}(y,x). Corollary 3.13:
chi_G(x,y) = psi_G(x,y) + (y-1) psi_{G*}(y,x) for the ordinary Tutte polynomial chi_G.

**Theorem 1.4 (p. 3; proof p. 28).** L non-split, non-local, alternating, D connected reduced
alternating. Then d_max J_L^+- - d_min J_L^+- = c(L) - alpha^+-(D); in particular alpha^+-(D) are
invariants of L. (Mechanism, Lemma 5.1: psi_G has x-degree n-1 with unique top term x^{n-1}, and
y-degree m-n+1-alpha(G) with a positive coefficient on y^{m-n+1-alpha} when G has no bridges or
local loops.)

**Theorem 1.9 (Drobotukhina 1990, quoted p. 5).** L non-split, non-local: d_max J_L - d_min J_L <=
c(L) - 1/2, with equality for alternating L.

**Proposition 4.4 (p. 24).** L nullhomologous with diagram D. (i) If D is local then Psi_{G_1} =
Psi_{G_2} = <D>. (ii) If D is non-local then Psi_D = <D>. Remark (p. 26): Psi_D computes the
bracket of a local link exactly when the diagram used is non-local.

**Theorem 5.3 (p. 29).** L non-split, nullhomologous, prime. (1) If beta_eps(L) = 0 for some eps, then
L = Upsilon_n for some n. (2) If beta_eps(L) = 1, then L is in the family V_n. (3) If beta_eps(L) = 2,
then L is in one of W_n, X_n, Y_n, Z_n or is the (local) Hopf link. Proof: hand enumeration of connected
graphs in RP^2 with e(G) - alpha(G) <= 2 (such a graph has at most beta+1 vertices), then all
crossing assignments, with duplicates removed by Jones polynomial. Stated consequence (caption of
Fig. 14): the only other non-split links with beta_eps <= 2 are Upsilon_n # Hopf.

**Theorem 1.5 (p. 3; proof p. 32).** For L in the set {Upsilon_n, V_n, W_n, mW_n}_n u {Z_n}_{n != -1} and
L' alternating, J_L = J_{L'} implies L = L' as unoriented links. (Detection among alternating
links only.)

**Corollaries.** 1.10: non-local alternating knots are not amphichiral. 1.11: self-dual Tait graphs
(G_+ = G_-) force amphichirality and at least two components. 4.5/4.6: det_Re, det_Im = numbers of
spanning trees of the two Tait graphs = |det| of the two Goeritz matrices (alternating case).
Prop. 2.6: sigma_+-(L) = s_A(D^+-) - n_+(D) - 1 = 1 + n_-(D) - s_B(D^+-), where D^+- are the two planar
"plat-like" closures of the disk picture.

**Section 6 (spanning tree complex).** Lemma 6.2: spanning trees of the two Tait graphs <-> twisted
unknots of D. Prop. 6.8, Thms 6.10, 6.12 (pp. 37-39): for a non-local diagram D of a nullhomologous
link there is a complex C(D) = C_+(D) + C_-(D) generated by the spanning trees of G_+ and G_-,
bigraded by (u,v), with differentials of bidegree (-1,-1) on C_+ and (1,1) on C_-, which is a
deformation retract of the reduced Khovanov complex; and a Champanerkar-Kofman spectral sequence
with E_1 = C(D) converging to Kh~(L; F), collapsing by page c(D). The proofs are declared to be
"completely derivative" of Champanerkar-Kofman and are illustrated by examples rather than written out.

**Question 5.4 (p. 30).** For L_1 nullhomologous in RP^3 and L_2 in S^3: (1) is beta_eps(L_1 # L_2) =
beta_eps(L_1) + c(L_2)? (2) is alpha_eps(L_1 # L_2) = alpha_eps(L_1)? (3) is alpha_eps(L_1) +
beta_eps(L_1) = c(L_1)? (4) are beta_eps or alpha_eps bounded over all nullhomologous links?

## 4. The strategy toward T

### 4.1 What is stated [BS, pp. 4-5]

Two candidate generalisations of Theorem 1.4 to non-alternating links are shown to be FALSE
(Examples 1.7, 1.8), both on the non-alternating amphichiral 2-component link 4_3^2
(Drobotukhina's table): breadth J^Im = 3 > 2 = beta_Im, so "breadth J^eps <= beta_eps" fails; and
"(breadth J - breadth J^eps) + 1/2 >= alpha_eps" fails. The reversed inequalities are then proposed:

**Conjecture 1.1 (p. 5).** Let L in RP^3 be nullhomologous, eps in {Re, Im}. Then
  (1)  (d_max J_L - d_min J_L) - (d_max J_L^eps - d_min J_L^eps) + 1/2 <= alpha_eps(L).
  Furthermore, if L is local, suppose that L is a knot and eps = Re. Then
  (2)  d_max J_L^eps - d_min J_L^eps >= beta_eps(L).

The only wording of motivation is one sentence: "Interestingly, reversing each of the inequalities
in the examples above gives plausible statements."

**Implication (p. 5).** (2) => T. If K in S^3 has J_K = 1, view K as a local knot in RP^3;
(2) gives beta_Re(K) = 0, i.e. some diagram D of K in RP^2 has c(D) = alpha_Re(D); by Theorem 5.3(1)
the only such diagrams are those of the family Upsilon_n (one-vertex Tait graph, all loops
projective; mixed signs cancel by Reidemeister II), and J distinguishes the Upsilon_n, so K =
Upsilon_0 = unknot. The authors add that Conjecture 1.1 would give detection of every Upsilon_n.
Remark (p. 5): the restriction to knots among local links is forced by the
Thistlethwaite / Eliahou-Kauffman-Thistlethwaite links with trivial Jones polynomial.

### 4.2 What is proved, what is conjectured

Proved: Theorem 1.4 (equality breadth J^+- = c - alpha^+- for non-local alternating links, which
gives (2) for those since beta_eps <= c(D) - alpha_eps(D)); classical KMT gives (2) for local
alternating knots (breadth = c(K) >= beta_Re(K)); Theorem 5.3(1) (beta = 0 forces Upsilon_n).
Conjectured: (2) for every non-alternating knot. No partial result, no computation, no worked
non-alternating local example. The talk abstract's "partial results" are the alternating theorems.

### 4.3 Where the hard step lies [DIGEST]

- Equivalent form of the needed statement. Because of Theorem 5.3(1), "J_K = 1 => beta_Re(K) = 0"
  is equivalent to T itself (unknot has beta = 0; beta_Re = 0 and local forces unknot). So the
  conjecture does not reduce T to a weaker or structurally different statement; it embeds T as the
  n = 0 case of a family of statements "breadth V_K <= n => K has an RP^2 diagram whose Re Tait
  graph becomes local after deleting all but n edges".
- The geometric content: K has a diagram D in RP^2 and a set of alpha crossings whose smoothing
  gives a local (classical) diagram with c(D) - alpha <= breadth(V_K) crossings. For J = 1: K is the
  boundary of a disk with only "projective" half-twisted bands attached. A lower bound on the Jones
  breadth by a geometric complexity is exactly what is missing in every approach to T; the RP^2
  setting supplies a new complexity (beta) but no new mechanism for the bound. In Theorem 1.4 the
  mechanism is Thistlethwaite's: no cancellation among spanning trees of an alternating graph. For
  non-alternating diagrams cancellation is the whole difficulty, as in S^3.
- The strategy needs non-local diagrams of classical knots to be strictly more efficient than
  classical ones. For a non-alternating prime knot breadth(V_K) < c(K), so (2) forces
  beta_Re(K) < c(K). First test cases: 8_19 (V = t^3 + t^5 - t^8, breadth 5, c = 8), 8_20 and 8_21
  (breadth 6). The paper contains no example of a local knot with beta_Re(K) < c(K).
- Tension with the authors' own questions. If Question 5.4(3) (alpha + beta = c) or 5.4(1) (with
  L_1 the unknot, or L_1 = Upsilon_2) has a positive answer for local L_2 = 8_19, then beta_Re(8_19)
  = 8 > 5 (resp. beta_eps(Upsilon_2 # 8_19) = 8 > 5 = breadth of the corresponding half), which
  contradicts (2). So Conjecture 1.1(2) and affirmative answers to Question 5.4(1),(3) cannot both
  hold. The paper does not notice this.
- A consequence one can test: a diagram with c - alpha_eps <= n has a Tait graph with at most n+1
  vertices, hence boundedly many twist regions (O(n) by an Euler characteristic count on RP^2), so
  by Lackenby-type bounds (lift to the double cover S^2 x I) the simplicial volume of the knot
  complement is O(n). Thus (2) would imply vol(S^3 - K) <= C (breadth V_K + 1) for all hyperbolic K
  with a universal C. I have not checked the constants; no such bound is known, and I know of no
  counterexample. This is stronger than T and is a natural place to look for a refutation.

### 4.4 Defects of Conjecture 1.1 as literally stated [DIGEST]

- Inequality (1) fails for every local knot with eps = Re: J = J^Re, so the left side is 1/2, while
  alpha_Re(K) = 0 (take a local diagram). (1) must be read for non-local L only (it is modelled on
  Theorem 1.9, which assumes non-local).
- Inequality (2) fails for non-local composite links with a trivial-Jones local summand. Let L_2 be
  a nontrivial 2-component link in S^3 with V = -t^{1/2} - t^{-1/2} (the links used in the paper's own
  Remark) and L = Upsilon_2 # L_2. Then J_L = (t + t^{3/2} - t^{5/2})(-t^{1/2} - t^{-1/2}) =
  (-t + t^3) + (-t^{1/2} - t^{3/2}), so one half has breadth 1; L is non-local with 2 components.
  By the enumeration proving Theorem 5.3 (which for beta <= 1 does not use primeness), links
  with beta_eps <= 1 are Upsilon_m (one half of J is a monomial) or V_m (knots); L is neither. So
  beta_eps(L) >= 2 > 1 = breadth. This is the paper's own Remark applied to a non-local link; the
  exclusion clause in (2) covers only local links. A repaired statement needs "prime" or an
  equivalent hypothesis. The knot case used for T is not affected, but the example shows that the
  inequality is false as soon as trivial-Jones summands are allowed, i.e. its truth for knots is
  not explained by any mechanism that is insensitive to T.

## 5. Relation to the Turaev genus one results

The paper does not cite or discuss them. The comparison below is mine.

**Dasbach-Lowrance, arXiv:1604.03501v2, Theorem 1.3.** For L almost alternating or of Turaev genus
one with V_L = a_m t^m + ... + a_M t^M (a_m, a_M nonzero): |a_m| = 1 or |a_M| = 1.
Mechanism (Lemma 4.2 and proof, sec. 4): take an almost alternating diagram D with dealternator x
and alternating tangle R with N(R), D(R) reduced; <D> = A<D(R)> + A^{-1}<N(R)>. By Dasbach-Lin, an
alternating bracket begins (-1)^{v-1}A^{c+2v-2} + (-1)^{v-2}(e-v+1)A^{c+2v-6} + ... (v = vertices of the
all-A state graph, e = edges after removing multiple edges), and symmetrically at the other end.
The all-A graph of D(R) is that of N(R) with the two faces u_1, u_2 at the dealternator identified,
so v drops by 1: the leading +-1 terms cancel, and the next coefficient is
alpha_0 = +-(1 - adj(u_1,u_2)), where adj(u_1,u_2) = number of faces in R adjacent to both u_1 and u_2
(= number P of length-two paths u_1 - u_2 in the simplified checkerboard graph: these become
parallel edges after identification, lowering the circuit rank). Likewise at the other end
alpha_k = +-(1 - adj(v_1,v_2)) for the two faces v_1, v_2 on the other colour. Planar duality:
adj(u_1,u_2) >= 3 forces adj(v_1,v_2) = 0; and adj(u_1,u_2) = adj(v_1,v_2) = 1 allows a move to an
almost alternating diagram with two fewer crossings. So for a crossing-minimal almost
alternating diagram one of adj(u_1,u_2), adj(v_1,v_2) lies in {0,2}, and that end's first
potential coefficient is a genuine extreme coefficient equal to +-1. Which end is not determined
in general: the A-degree-maximal end (lowest t-degree, since t = A^{-4}) when P = adj(u_1,u_2) is
0 or 2, the other end when P-bar = adj(v_1,v_2) is 0 or 2. Turaev genus one follows because every
Turaev genus one link is mutant to an almost alternating link (Armond-Lowrance) and mutation
preserves V.

**Lowrance-Spyropoulos, arXiv:1707.05443v2 (NYJM 23 (2017)).** Theorem 1.1: for an l-component
almost alternating or Turaev genus one link, V_L != t^k (-t^{1/2} - t^{-1/2})^{l-1} for all k; in
particular T holds for Turaev genus one knots. Theorem 1.2: either |a_0| = 1 and a_0 a_1 <= 0, or
|a_n| = 1 and a_{n-1} a_n <= 0. Theorem 3.1: for a strongly reduced almost alternating
diagram with c crossings, <D> = sum_{i=0}^{c-3} alpha_i A^{c+2v-8-4i} with alpha_0 = (-1)^v (P - 1),
alpha_{c-3} = (-1)^{v-bar}(P-bar - 1), and explicit graph-theoretic formulas for alpha_1, alpha_{c-4}
(circuit rank, counts of 2-paths, 3-paths and K_4 subgraphs through the dealternator faces).
Mechanism for nontriviality: one extreme coefficient is +-1 (as above), and V = t^k would require
alpha_0 = alpha_1 = alpha_{c-4} = 0 at the other positions; this forces P = 1 and P-bar in {0,2} (Lemma 3.4 gives one of P, P-bar in {0,2}),
and the resulting graphs fall into seven explicit families (Lemmas 4.2, 4.3) which are
semi-adequate (then Stoimenow's theorem, quoted as Theorem 4.1, applies) or alternating. For l >= 2 the sign statement (Theorem 1.2) suffices.

**Comparison with Boyle-Spyropoulos [DIGEST].** The Turaev genus one results are unconditional and
work by controlling the first two coefficients at each end after a single skein resolution into
alternating diagrams; they do not give, and do not use, a lower bound on breadth by a crossing-
number-type quantity. Conjecture 1.1(2) is a breadth inequality and is not implied by them even for
Turaev genus one knots (there breadth <= c - 3 for almost alternating diagrams, so (2) would require
non-local diagrams with c(D) - alpha_Re(D) <= c - 3; nothing of the kind is shown). Conversely the
paper offers no extreme-coefficient statement for non-alternating links in RP^3. The two lines of
work share an author and the spanning-tree / checkerboard-graph toolkit, nothing more.

## 6. Claim checks

- **C1** (the paper reduces T, or a class of cases of T, to a statement about links in RP^3):
  MODIFIED. The paper states that Conjecture 1.1(2) (p. 5), for nullhomologous links in RP^3 and
  in particular for local knots: breadth J_K >= beta_Re(K), implies T; the implication is proved
  (p. 5, via Theorem 5.3(1), p. 29). It is a sufficient condition, not an equivalence and not a
  reduction of a class of cases; the J = 1 instance of the conjecture is equivalent to T.
- **C2** (Khovanov homology of alternating links in RP^3 is thin in their sense): CONFIRMED with
  precise scope. Theorem 1.1 (p. 2): for non-local alternating L, Kh(L; Z/2) (APS theory, 1-1
  bifurcations acting by zero) is supported on exactly four diagonals j - 2i = -sigma_+-(L) +- 1 and
  is determined by J^+, J^-, sigma_+, sigma_-; equivalently each of the two parity summands of
  reduced Kh lies on one diagonal. Only F_2 coefficients; local alternating links are the classical
  case; "thin in RP^3" is not given a formal definition, and the spanning-tree-complex proofs
  (sec. 6) are sketched by reference to Champanerkar-Kofman.
- **C3** (the strategy covers Turaev genus two or higher only conditionally): MODIFIED / not
  addressed by the source. The paper never mentions Turaev genus. Its strategy is conditional on
  Conjecture 1.1(2) for every non-alternating knot, including Turaev genus one; unconditional
  coverage of Turaev genus one comes from Lowrance-Spyropoulos 2017, by a different mechanism,
  not from this paper.

## 7. Translation into Conway tangle language [DIGEST, not in the paper]

A nullhomologous diagram meets the boundary circle of the disk model in 2m points with m even.
The first non-classical case m = 2 is exactly a Conway tangle diagram T in the disk with ends at
NE, NW, SE, SW, closed by the antipodal identification (NE ~ SW, NW ~ SE). Call the result a(T).

- Bracket level (rigorous, elementary). The two crossingless tangles id, e close antipodally to a
  single class-0 circle each, with bracket 1. Hence if [T] = x id + y e (closed circles evaluated
  to -A^2 - A^{-2}), then <a(T)> = x + y. The A-exponents of x and of y lie in classes differing by
  2 mod 4, so the splitting J = J^Re + J^Im of the paper is the splitting into x and y, and
  Psi_{G_1}, Psi_{G_2} are x and y. Checks: Upsilon_n = a(Q_n), and the paper's formula (5),
  <Upsilon_n> = A^n + sum_{i<n} (-1)^i A^{n-2-4i}, is the bracket vector of the n-twist tangle;
  Drobotukhina's 3_1 is a(T) for a 3-crossing rational tangle with (x,y) = (-A^{-5} + A^{-1},
  -A^5 + A - A^{-3}), determinants (2,3), and the paper's two "plat-like closures" D^+- (Hopf link
  and trefoil, p. 12) are N(T) and D(T). Corollary 3.13, chi_G = psi_G + (y-1) psi_{G*}, is the
  identity <N(T)> = x + delta y in graph form.
- So the RP^3 Jones polynomial of a(T) records x and y separately, where S^3 closures record
  x + delta y and delta x + y. Theorem 1.4 for a(T) is a KMT statement for x and y separately, and
  the projective rank alpha measures how far the top/bottom degrees of x (resp. y) fall short of
  the alternating maximum.
- If a(T) is a LOCAL knot K, then one of x, y vanishes and the other is, up to a unit, V_K.
  (Example: T = the trivial tangle with knots tied in the strands.) The double cover S^3 -> RP^3
  lifts a(T) to the union of T with its antipodal image, a two-tangle decomposition of a link in
  S^3; a(T) is local iff that lift is the split link K u K.
- Khovanov level (unverified suggestion). The APS complex of a(T) over F_2 is obtained from the
  Bar-Natan tangle complex of T by sending both crossingless tangles to the reduced unknot and
  every saddle between them (a 1-1 bifurcation) to zero. In KWZ terms this should be the homology
  of BN~(T) after killing the S-type arrows, splitting by idempotent; Theorem 1.1 then says this
  is "thin per idempotent" for alternating T. I have not checked gradings or the reduced/unreduced
  bookkeeping.
- For m > 2 the same holds with the Temperley-Lieb skein module of the disk with 2m points and
  the antipodal closure functional (each crossingless matching closes to a union of class-0
  circles), again Z/2-graded.

## 8. What the source proves and does not prove

Proves (modulo sketched parts of sec. 6): Theorems 1.1-1.5, 5.3, Prop. 4.4, Cor. 1.10, 1.11,
4.5, 4.6 as stated above; all positive results concern alternating links, or the classification
of links with beta <= 2 (hand enumeration, figures only for the families).
Does not prove: any case of Conjecture 1.1 beyond alternating links; any statement about
non-alternating classical knots; any relation between beta_Re(K) and classical invariants
(crossing number, Turaev genus, volume); that beta_Re(K) < c(K) ever happens for a classical knot.
Does not contain: Turaev genus, Dasbach-Lowrance, Lowrance-Spyropoulos, tangles, branched double
covers (explicitly postponed, p. 10), or any Floer-theoretic input. Forthcoming items mentioned:
Boyle-Spyropoulos "L-spaces and quasi-alternating links in RP^3" (in preparation);
Spyropoulos-Zhang, claimed detection of Upsilon_{2k} by reduced Khovanov homology (work in progress,
p. 7).

## 9. Open questions

1. Is there a classical knot K with beta_Re(K) < c(K)? In particular is beta_Re(8_19) <= 5, as
   Conjecture 1.1(2) requires? (Finite search: enumerate signed graphs in RP^2 with e - alpha <= 5
   and identify the local knots among the resulting diagrams.)
2. Does Conjecture 1.1(2) survive the consequence vol(K) <= C (breadth V_K + 1)?
3. Is the Khovanov-level dictionary of section 7 correct, i.e. is the APS homology of a(T) the
   homology of the KWZ type D structure of T with the S-arrows deleted?
4. Which Conway tangles T have a(T) local? (Equivalently: T union antipodal(T) is a split link of
   two isotopic knots.) For these, x(T) y(T) = 0, which is a strong constraint on [T].

## Files

- src/tex/MyopicTutte.tex, src/tex/MyopicTutte.bib, src/2609.40122.pdf, src/paper.txt (the paper, v1)
- src/tex_1604.03501/ (Dasbach-Lowrance v2), src/tex_1707.05443/ (Lowrance-Spyropoulos v2), with PDFs/txt
