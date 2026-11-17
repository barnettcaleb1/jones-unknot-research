# read-model: homological and skein model of W(5,1) and of Jones's genus-two representation

Lane: g2-proof / read-model. Author: Claude (subagent), 2026-11-03. Board workspace read only.
Status tags: [PUB] published result, [BOARD] transcribed from the board (not re-derived), [CHK] checked by the one exact computation in this folder, [EL] elementary, proved here, [SK] proof sketch with a named gap, [CONJ] conjecture, [OBS] obstruction (proved unless marked).

Conventions. sigma_i -> A + A^-1 e_i, e_i^2 = delta e_i, delta = -A^2 - A^-2. Delta_k = Chebyshev (Delta_2 = delta^2 - 1 = [3], Delta_3 = delta^3 - 2 delta = -[4] = -(A^6 + A^2 + A^-2 + A^-6)). lambda_j = -A^{2j+2} - A^{-2j-2} (curve operator on a colour-j channel). Board LKB variables (q,t), Jones line t = -q^-1.
H(x,y) = xbar^T G y, G the Graham-Lehrer Gram matrix in the diagram basis, bar: A -> A^-1. H is B_n-invariant [CHK]; it is the "invariant form B" of the task.

---------------------------------------------------------------------------------------------------

## 0. Results in one screen

1. [EL] The first two rungs of F3 coincide: Jones's genus-two representation is projectively faithful on Mod(S_{0,6}) IFF W(5,1) is faithful on B_5 modulo its centre. (Finite index plus "nontrivial normal subgroups of Mod(S_{0,6}) are infinite".) So "W(5,1) faithful" is not a step above genus two; it is the same statement, and it implies Burau_4 faithfulness (BBB). Also: W(6,2) faithfulness (what the board's audit expects KL(6,2) to give, modulo the split-partner and action-kernel lemmas it lists) implies it, since W(6,2)|B_5 = W(5,1) + Burau_5 and Long's lemma applies.
2. [PUB + EL] W(5,1) = pi[3,2] is the SUBmodule of LKB_5 at t = -q^-1 cut out by five explicit linear equations in Krammer's fork basis (Jackson-Kerler Lemma 12 and eq. (67); Bigelow's image of absolute in relative homology); the extension 0 -> W(5,1) -> LKB_5|line -> C_5 -> 0 does not split. The 2-cap squares are explicit vectors there (Section 1.2).
3. [EL] On W(5,1) the form of braided basis diagrams is the Kauffman bracket of a 3-bridge link, hence NEVER zero. Every zero relevant to faithfulness involves a Jones-Wenzl projector. The natural rank-one objects are the 3|3 curves c (3 punctures of D_5 inside c): T_c = A^-6 (1 + (A^12 - 1) P_c), P_c the H-orthogonal projector on the spin-3/2 line v_c [CHK]. No other twist is scalar plus rank one.
4. [EL] Exact Bigelow-type equivalence: W(5,1) (equivalently genus two) is unfaithful IFF there are 3|3 curves c != c' such that H(v_c', S) = 0 for every 2-cap system S having an arc disjoint from c. Then some such S has no arc disjoint from c': zero pairing with essential intersection.
5. [EL + CONJ] Key Lemma KL(3|C): H(v_c, S_C) = 0 iff some arc of C can be isotoped off c. It implies faithfulness of W(5,1) and of genus two (hence Burau_4). It is the (3,3)-tangle analogue of the board's id-coefficient Key Lemma: H(v_c, y) = Delta_3 x (rainbow coefficient of y in the c-adapted diagram basis) [CHK]. The converse direction of Bigelow's theorem does NOT transfer: a violation gives no kernel element, because the objects with rank-one twists (3|3 curves) are never disjoint from each other and the objects with "disjoint => orthogonal" (cap systems) have no rank-one twist. The curve-curve criterion F6 (H(v_c, v_c') = 0, c != c' => [T_c, T_c'] in the kernel) is sufficient only. For i(c,c') = 2 (one orbit) r(c,c') = 1/[3]^2 != 0 [CHK], so an F6 kernel needs i(c,c') >= 4.
6. [OBS] No expansion of H(v_c, v_c') can have its extreme degree controlled by i(c,c'): along a pseudo-Anosov family the degree of H(v_c, v_{g^k c}) grows linearly in k [CHK: spans 20, 36, 44, 52, 60] while i(c, g^k c) grows like 2.618^k. In the skein-algebra state sum over the 2^i resolutions of c cup c', the all-A term has degree >= i + 2 and must cancel against other states. What can survive is a sign-coherence statement with winding exponents (Bigelow type), and on the Jones line that meets the same (q,t) -> q^{a-b} collapse that blocks KL(6,2). Section 4.4 states the precise candidate.

---------------------------------------------------------------------------------------------------

## 1. (a) W(5,1) inside the Lawrence-Krammer representation of B_5

### 1.1 The subquotient [PUB]
LKB_5 = H_2 of the Z^2-cover of C_2(D_5) (unordered two-point configurations), rank C(5,2) = 10, Krammer fork basis F_{ij}, 1 <= i < j <= 5. At the Hecke specialisation it has shape (3,2) + (4,1) + (5), dimensions 5 + 4 + 1.

Jackson-Kerler (arXiv:0912.2114, Lemma 12 and eq. (67)): for n >= 4, after precomposing with sigma_i -> sigma_i^-1, the Temperley-Lieb module pi[n-2,2] is the KERNEL of the B_n-map
    H_{2,n}|_{t = -q^-1}  ->  C_n^dagger(q^-2),   F_{i,j} |-> e_i + q^-1 e_j,
with C_n^dagger(q^-2) the n-dimensional monomial module (sigma_j e_j = e_{j+1}, sigma_j e_{j+1} = q^2 e_j). The sequence 0 -> pi[n-2,2] -> LKB_n|line -> C_n -> 0 does not split for n >= 4 (JK prove non-splitness in their normalisation). In Bigelow's homological picture (Lawrence-Krammer representation, Sec. 6; JK cite Thm 6.3; the board cites "Thm 6.1") pi[n-2,2] is the image of H_2(Y~) in H_2(Y~, nu~), nu~ the configurations with a point at a puncture or the two points together. Lawrence has it as a quotient (cohomological version). For n = 5: pi[3,2] = W(5,1), the TL module with two cups and one through-strand.

Explicitly [EL]: x = sum x_{ij} F_{ij} lies in W(5,1) iff for k = 1..5
    sum_{j>k} x_{kj} + q^-1 sum_{i<k} x_{ik} = 0.
(Five equations on ten coordinates; 10 - 5 = 5 = dim W(5,1).) The five cap-square vectors of 1.2 are linearly independent (each of F12, F45, F15 occurs in only one of them), so they are a basis of this kernel.

### 1.2 Cap squares as fork vectors [EL membership; equivariant normalisation NOT checked]
A 2-cap system C = {(a b), (c d)} with free point f gives the square S_C = alpha_1 x alpha_2 (puncture-relative), in fork coordinates the product of fork differences (F_a - F_b)(F_c - F_d), where a reversed pair (x > y) is rewritten on the line as F_{xy} := q^-1 F_{yx} (= -t F_{yx}, the half-exchange). The five standard basis systems:
    (12)(34)|5 : F13 - F14 - F23 + F24          (the board's z-numerator v for C_0)
    (12)(45)|3 : F14 - F15 - F24 + F25
    (23)(45)|1 : F24 - F25 - F34 + F35
    (14)(23)|5 : F12 - F13 - q^-1 F24 + q^-1 F34
    (25)(34)|1 : F23 - F24 - q^-1 F35 + q^-1 F45
Each satisfies the five equations of 1.1 (hand check). That these are the images of the TL diagrams under a B_5-equivariant isomorphism, with these scalars, is NOT verified here; the reversal weight is forced by membership, the overall scalars are not.

### 1.3 The pairing as a sum over intersection points [BOARD, n = 6 -> 5]
Board conventions (THEORY-width-ladder, nodes U5-LAW-GEO, U5-PARK), unchanged at n = 5 because the derivation (Lawrence fibration, Fadell-Neuwirth) does not use n:
- S_C = puncture-relative square of the caps of C; z_{C'} = absolute torus gamma'_1 x gamma'_2 of the figure-eights around the cups of C'. Phi(C,C') = <S_C, j(z_{C'})>'.
- Phi(C,C') = sum over sigma in S_2, x in c_1 cap gamma'_{sigma(1)}, y in c_2 cap gamma'_{sigma(2)} of eps(x,y) q^{a(x,y)} t^{b(x,y)}, with (anchored at a reference pair m of the matching)
      a(x,y) = a_m + sum_p wind_p(L_x) + sum_p wind_p(L_y),   b(x,y) = b_m + 2 wind_{x_m}(L_y) + 2 wind_y(L_x),
  L_x, L_y closed reference loops, eps the product of local signs (the matching sign cancels the exchange parity on the line).
- Normalisations: Phi = H_tor/(1-q)^2 = q^-2 P/(1-t) (P = Krammer-basis pairing); Phi(q,1) = q^-1 det[<gamma'_j, c_i>] (2x2 Burau determinant); on t = -q^-1 every pair contributes (-1)^b q^{a-b} and Phi = q^-1 J_hat, J_hat the Graham-Lehrer form up to a unit.
- Parked-point form: Phi_TL = sum_{m,y} eps_0 (-1)^{b_0} q^{a_0 - b_0} sum_x eta_x q^{A_x - 2 W_x}: one-point Burau pairings in the six-punctured disk D_5 cup {y}, the parked point y carrying weight q^-2 = t^2.

### 1.4 What is special at width 5 [EL]
- W(5,1) = W(6,0)|_{B_5} (join the free point to a sixth point). For basis diagrams x, y and beta in B_5, G(x, rho(beta) y) is the coefficient of the trivial arc of the (1,1)-tangle cap_x beta cup_y, so delta G(x, rho(beta) y) = <L>, L the plat closure of beta (x) 1 in B_6 with caps x + (f,6) and cups y + (f',6): a 3-bridge link. Since V_L(1) = (-2)^{#L - 1} != 0, these entries never vanish. Contrast W(6,2), where the id-coefficient of a (2,2)-tangle can vanish (the board's whole ladder).
- Hence every zero that matters for faithfulness of W(5,1) is a zero of a pairing involving a Jones-Wenzl projector, i.e. of a coloured evaluation (Section 2).
- Homological picture of v_c (Section 2), [SK]: collapsing the disk D_c to one puncture P of colour 3, the spin-3/2 channel is the one-dimensional highest-weight space of weight 1/2 in V_{3/2} (x) V (x) V, represented by the square of two arcs from P to p_4 and from P to p_5 (two tines sharing the fat puncture). In D_5: the relative square of two disjoint arcs from the curve c to p_4, p_5 in the outer region, with no configuration point inside D_c. This matches the TL formula v_c = p_3 applied to (25)(34)|1. Normalisation of the relative boundary on c is not worked out here.

---------------------------------------------------------------------------------------------------

## 2. The 3|3 curve vectors (skein model) [CHK unless marked]

W(6,0) = Kauffman skein module of B^3 with six marked points, basis D1 = (12)(34)(56), D2 = (12)(36)(45), D3 = (14)(23)(56), D4 = (16)(23)(45), D5 = (16)(25)(34) (the rainbow rb). In W(5,1) language: (12)(34)|5, (12)(45)|3, (14)(23)|5, (23)(45)|1, (25)(34)|1.

A 3|3 curve c of S_{0,6} is the same as a curve of D_5 around three punctures (p_6 = the boundary side). Take c_0 around {1,2,3}.
- v_{c_0} = p_3-coloured rainbow = [-delta D1 + D2 + D3 - delta D4 + (delta^2 - 1) D5]/(delta^2 - 1). It is killed by e_1, e_2, e_4, e_5 and spans ker e_1 cap ker e_2. Equivalent descriptions: (i) a single colour-3 arc joining the fat point {1,2,3} to the fat point {4,5,6}; (ii) the fusion-tree vector with internal colours (2,3,2) on the tree adapted to c; (iii) P_c = (c_hat - lambda_1)/(lambda_3 - lambda_1), a polynomial in the curve operator c_hat (eigenvalues lambda_1 on the four-dimensional colour-1 channel, lambda_3 on the line).
- H(v_c, v_c) = Delta_3 = -[4].
- T_c = (sigma_1 sigma_2)^3 acts as A^-6 on span(D1..D4) and as A^6 on v_c: T_c = A^-6 (1 + (A^12 - 1) P_c). By conjugation this holds for every 3|3 curve. On W(5,1) the twists about curves round 2 or 4 punctures have eigenspaces of ranks 2 and 3; the 3|3 twists are the only scalar-plus-rank-one twists.
- Rainbow duality: H(v_c, y) = Delta_3 [y]_{rb_c} for all y, where [y]_{rb_c} is the coefficient of the c-rainbow in the diagram basis adapted to c. So v_c^perp = span of the four cap systems with a cap inside one side of c, and v_c = Delta_3 G^-1 e_rb in coordinates.
- Pairing of two curves: for c' = g c, H(v_c, v_c') = Delta_3 [rho(g) v_c]_rb = Delta_3^2 (rho(g) G^-1)_{rb,rb}. The Mod-invariant number r(c,c') = tr(P_c P_c') = |H(v_c,v_c')|^2 / Delta_3^2.
- i(c,c') = 2: all such pairs form one Mod(S_{0,6})-orbit (the four complementary regions carry 1,2,2,1 punctures, forced by minimal position) and r(c, sigma_3 c) = 1/[3]^2 exactly. Nonzero.

---------------------------------------------------------------------------------------------------

## 3. (b) The Bigelow-type criterion for W(5,1)

### 3.0 Bigelow's theorem being imitated [PUB]
Bigelow (GT 3, 1999, Thm 1.4): for n >= 3, Burau_n is unfaithful iff there are embedded arcs alpha from q_1 to q_2 and beta from p_0 to q_3 (or from q_3 to q_4) with alpha not homotopic off beta rel endpoints and the Burau pairing of beta and alpha zero. "If": the half twists tau_alpha, tau_beta act as transvections gamma -> gamma + P(t) alpha', so they commute in the image while [tau_alpha, tau_beta] != 1. "Only if": a kernel element psi satisfies pairing(psi(alpha), beta) = 0 for straight disjoint pairs, so (given the hypothesis) psi fixes all straight arcs and is a power of Delta. Both directions need ONE class of objects that both carries rank-one twists and has "disjoint => pairing zero". For Burau the arcs do both.

### 3.1 Genus two and W(5,1) are the same rung [EL]
Let PK_6 = {psi in Mod(S_{0,6}) : rho(psi) scalar} and PK_5 the analogue in B_5. Stab(p_6) = B_5/Z(B_5) has index 6, and PK_6 cap Stab(p_6) = PK_5/Z because W(6,0)|_{B_5} = W(5,1). A finite normal subgroup of Mod(S_{0,6}) is centralised by a finite-index subgroup, hence fixes every curve, hence is trivial; so PK_6 != 1 forces PK_6 infinite and PK_6 cap Stab(p_6) != 1. Conversely restriction. Hence
    Jones genus two projectively faithful  <=>  W(5,1) faithful mod centre  =>  Burau_4 faithful (W(5,1)|B_4 = W(4,0) + Burau_4).
Linear versus projective: if rho(psi) is scalar and psi is not central, some commutator [psi, g] != 1 lies in the honest kernel. Delta_5^2 acts on W(5,1) by A^-12 and Delta_6^2 on W(6,0) by A^-18, so no kernel element is central.
Ito (Math. Z. 2015, Thm 1, Cor. 1, Cor. 2): a nontrivial non-central normal subgroup of B_n contains braids whose closures (with any unknotted alpha) are hyperbolic knots of arbitrarily large genus; the quantum-representation corollary concerns rho_V on V^{(x)n}, i.e. the FULL TL representation (all W(n,k)). F2 is Long's Lemma 2.1 as quoted by Ito. So: ker W(5,1) != 1 => ker W(5,1) cap ker Burau_5 cap ker W(5,5) != 1 (non-central since it sits in ker W(5,1)) => T is false.

### 3.2 The exact equivalence [EL]
Lambda: {3|3 curves} -> P(W(5,1)), c -> [v_c], is B_5-equivariant.
Prop A. W(5,1) is faithful mod centre iff Lambda is injective.
Proof. If [v_c] = [v_c'] with c != c', then T_c and T_c' have the same matrix, so T_c T_c'^-1 is a nontrivial kernel element. If psi in PK_5 is not central, psi moves some 3|3 curve c (a mapping class of S_{0,6} fixing all 3|3 curves centralises the normal subgroup they generate, and centralisers of nontrivial normal subgroups of Mod(S_{0,6}) are trivial); equivariance and rho(psi) scalar give [v_{psi c}] = [v_c].
Prop B (Bigelow form). W(5,1) is unfaithful iff there exist 3|3 curves c != c' with H(v_c', S) = 0 for every 2-cap system S having an arc disjoint from c (equivalently, for the four c-adapted systems).
Proof. H is nondegenerate at generic A and the cap systems with an arc off c span v_c^perp, so the condition says v_c'^perp = v_c^perp, i.e. [v_c'] = [v_c]. Apply Prop A.

### 3.3 Construction lemma and the one-way Key Lemma [EL, curve topology sketched]
Lemma C. If c != c' are 3|3 curves, there is a cap system S (three disjoint arcs pairing the six punctures of S_{0,6}; in D_5 two arcs plus the free point) with an arc disjoint from c and no arc that can be isotoped off c'.
Sketch. If the partitions {X, X^c} and {X', X'^c} differ, choose a side X of c with p in X cap X', p' in X minus X'; take alpha inside D_c from p to p'. It must cross c'. The remaining four punctures are two inside c' and two outside; join them across c' by disjoint arcs. If the partitions agree, one of two arcs alpha_12, alpha_23 spanning D_c meets c' essentially: otherwise, after removing bigons (none contains a puncture), c' misses the tree alpha_12 cup alpha_23, hence its neighbourhood D_c, and then c' = c. Do the same on the other side and join the last two punctures across c'.
Theorem D. KL(3|C): "for every 3|3 curve c and cap system S, H(v_c, S) = 0 implies some arc of S isotopes off c" implies that W(5,1) and Jones's genus-two representation are faithful (strength: implies Burau_4 faithful).
Proof. A kernel element psi gives c' = psi(c) != c with [v_c'] = [v_c]. Lemma C gives S with an arc off c, so H(v_c', S) = lambda H(v_c, S) = 0, and with no arc off c'. Contradiction.
The easy half of KL(3|C) is true: an arc alpha off c joins two punctures on one side, there v_c is in the spin-1 channel of that pair, so e_alpha v_c = 0 and H(v_c, e_alpha x) = H(e_alpha v_c, x) = 0.

### 3.4 Where the analogy with Bigelow breaks [EL]
| | Burau_n (Bigelow 1.4) | W(5,1) / genus two |
|---|---|---|
| objects with rank-one twist | arcs (half twist = transvection) | 3|3 curves only (T_c = A^-6(1 + kappa P_c)) |
| objects with disjoint => pairing 0 | arcs | cap systems vs curves; two distinct 3|3 curves always intersect (i >= 2) |
| violation => kernel element | yes, [tau_alpha, tau_beta] | only curve-curve zeros: H(v_c,v_c') = 0, c != c' => [T_c, T_c'] (F6) |
| kernel => violation | yes | yes for (curve, cap system) pairs (Lemma C) |
| exact equivalence | the arc criterion | Prop A/B (injectivity of Lambda) |
So unfaithfulness is sandwiched: [exists curve-curve zero] => unfaithful <=> [Lambda not injective] => [KL(3|C) fails]. Closing the gap would need a group element acting as scalar plus rank one onto a cap-square line; the board found the same obstruction for W(6,2) (SCAFFOLD U5-W6: E_I = e_{i1} e_{i2} is rank one but no braid acts as scalar + E_I). On W(5,1), e_alpha e_beta for a 2-cap system is rank one with image the cap square, and tau_alpha tau_beta has eigenvalues A^2 (x2), -A^-2 (x2), A^-6 (x1): not scalar plus rank one.
Refinement of F6 [EL]: rho restricted to <T_c, T_c'> (free of rank two when i(c,c') >= 2, Ishida) is A^-6 times (a 2-dimensional representation of F_2 determined by kappa = A^12 - 1 and r(c,c'), plus the identity on the 3-dimensional H-complement of span(v_c, v_c')). Any nontrivial exponent-sum-zero word in the kernel of that 2x2 representation is a kernel element of genus two. r = 0 is the commuting case. Since r = 1/[3]^2 on the unique i = 2 orbit, the F6 criterion needs i(c,c') >= 4.

### 3.5 KL(3|C) as a tangle statement (the width-5 analogue of the board's ladder) [EL + CONJ]
By rainbow duality, H(v_{c_0}, rho(g) S_0) = Delta_3 x [rho(g) S_0]_rb. Bend the six points into three on top (inside c_0) and three below: W(6,0) = TL_3 as a vector space, the rainbow becomes 1, and [.]_rb is the identity coefficient eps: TL_3 -> Z[A^+-1] (e_i -> 0). A cap system S seen with c as equator is a trivial 3-string tangle X_{S,c} in B^3 with the boundary split into two 3-point disks. KL(3|C) reads:
    the identity coefficient of X_{S,c} in TL_3 vanishes iff X_{S,c} has an arc with both ends in one disk that is parallel into that disk.
This is the (3,3) analogue of KL(n,2) ("id-coefficient zero iff split") for the trivial tangles X_{S,c}. Pure-braid-type tangles (S = beta . rainbow, beta in B_3 x B_3) have unit coefficient A^{e(beta)}. Status OPEN; faithfulness strength (it implies genus-two faithfulness, which implies Burau_4 faithful). Relation to the board: W(6,2) faithful (the expected output of KL(6,2), modulo the lemmas listed in the board audit) => (restriction to B_5 is W(5,1) + Burau_5, Long's lemma) W(5,1) faithful. KL(3|C) is a separate, smaller statement in a 5-dimensional module.

---------------------------------------------------------------------------------------------------

## 4. (c) W(6,0): v_c, B(v_c, v_c') in skein/TQFT terms, and leading terms

### 4.1 Expressions [CHK for the formulas of Section 2]
- B(v_c, v_c') = H(v_c, v_c') is the Kauffman evaluation of the closed spin network Theta(c,c') in S^3 = B_+ cup B_-: a colour-3 arc dual to the disk of c in B_+, a colour-3 arc dual to the disk of c' in B_-, joined through the six colour-1 marked points. Expanding the two p_3 boxes in TL_3 writes it as a Z[1/[2],1/[3]]-combination of brackets of 3-bridge plats (the 25 plat closures of g with the five cap systems top and bottom).
- Coordinates: H(v_c, v_{gc}) = Delta_3^2 (rho(g) G^-1)_{rb,rb}; H(v_c, y) = Delta_3 [y]_rb.
- TQFT: v_c is the (2,3,2)-coloured tree vector of the pants tree adapted to c; P_c = (c_hat - lambda_1)/(lambda_3 - lambda_1).

### 4.2 Three expansions
(E1) Skein-algebra state sum over c cup c'. Since c_hat acts on B_+ and c'_hat on B_-, H(P_c x, P_c' y) = <x | (c_hat - lambda_1)(c'_hat - lambda_1) | y>/(lambda_3 - lambda_1)^2, where c_hat c'_hat is the skein product c * c' in K(S_{0,6}). Intrinsically
    (lambda_3 - lambda_1)^2 r(c,c') = tr_W(c * c') - 3 lambda_1^2 - 2 lambda_1 lambda_3,
    c * c' = sum over s in {A,B}^{i(c,c')} of A^{i - 2 k(s)} m_s,
k(s) the number of B-smoothings, m_s the resolved multicurve (trivial components = delta, peripheral = lambda_1). For a multicurve, tr_W(m) = sum over admissible colourings j of a pants decomposition containing m of prod_{gamma in m} lambda_{j(gamma)}; its top degree is max_j sum (2 j_gamma + 2) with nonzero coefficient (-1)^{#m} x (number of maximisers), so it is at least 2 #m > 0.
(E2) Diagrammatic state sum: H(v_c, v_{gc}) = Delta_3 sum_D pi_D sum over Kauffman states of (D on top, braid word g) resolving to the rainbow of A^{a-b} delta^{loops}, pi_D the p_3 coefficients.
(E3) Lawrence expansion: v_c as the relative square of two tines from the fat colour-3 puncture (Section 1.4), paired with the dual torus of the other object: a sum over intersection pairs of eps (-1)^b q^{a-b} with winding exponents, as in 1.3 with one coloured puncture.

### 4.3 The leading-term statement that is true, and why it does not descend [PUB from memory + OBS]
In the skein algebra itself the leading-term lemma holds: for curves in minimal position the top A-degree part of c * c' in the multicurve basis is A^{i(c,c')} times the all-A resolution, with coefficient 1 (the standard lemma behind "skein algebras are domains"; citation from memory, not re-checked). It does NOT descend to W(6,0):
OBS 1 (proved). rho(g^k) has entries of A-degree at most k d(g) + O(1), so the degree span of H(v_c, v_{g^k c}) is O(k). If g is pseudo-Anosov on a subsurface met essentially by c, i(c, g^k c) >= C lambda(g)^k. In (E1) the all-A term has degree at least i(c,c') + 2 (by the trace remark), so for large k the top-degree contributions of different states cancel. Data [CHK], g = sigma_3 sigma_4^-1 (pseudo-Anosov on the disk around {3,4,5}, lambda = 2.618, met by c_0): degree spans of H(v~, rho(g^k) v~) for k = 1..5 are 20, 36, 44, 52, 60 (H(v~,v~) itself has span 20). For the reducible family sigma_3^{2m} (i = 4m) the spans are 32, 40, 48 at i = 4, 8, 12 (affine in i), so twist families cannot detect the problem.
OBS 2. The same argument applies to (E2): the extremal Kauffman states of a braid word have degree comparable to word length, not to i, and the board already found that extremal id-states cancel at the (2,2) level (lens L2 dead). (E2) also carries the denominators of p_3.
OBS 3. The rank-one structure exists only on the Jones line. At generic (q,t) the twist T_c on LKB_5 has a large eigenspace for "no point inside c", so the curve criterion has no two-variable lift in which Bigelow's lexicographic argument could run; and on the line monomials q^a t^b collapse to (-1)^b q^{a-b}.
Conclusion: "the extreme degree of B(v_c, v_c') equals (a function of) i(c,c')" is false for every expansion above. The intersection number can control the NUMBER of terms, not the degree.

### 4.4 The only plausible form, stated precisely [CONJ]
Conjecture LT (sign coherence, coloured Lawrence model). Let c be a 3|3 curve and C a cap system, in minimal position, with every arc of C meeting c essentially. In expansion (E3) of H(v_c, S_C), a sum over intersection pairs (x,y) of the two tines of c with the figure-eight torus of C of eps(x,y) (-1)^{b(x,y)} q^{a(x,y) - b(x,y)} (one coloured puncture of weight q^3 for the disk of c; parked weight q^-2 as in 1.3), the extremal value of a - b over all pairs is attained by pairs of a single sign.
Reason it could hold: it is Bigelow's mechanism (extremal monomial with one sign in tight position), and the exponents are winding numbers that grow linearly, which OBS 1 shows is necessary.
Strength: LT => KL(3|C) => Jones genus two faithful <=> W(5,1) faithful => Burau_4 faithful (BBB). It is faithfulness-strength, so it cannot be cheap.
Known obstruction: on the Jones line the collapsed lines carry (1+qt)-packets and mixed-sign extrema in non-tight representatives (board, width 6: U5-MOM, 23 + 24 parked positions with mixed extrema in the six-letter control). Any proof needs a tightness notion for the coloured model that rules these out. None exists yet. The normalisation of the relative boundary on c in (E3) is also not fixed here.

---------------------------------------------------------------------------------------------------

## 5. Computation log (one exact check, about 2 minutes)
Script: /Users/calebbarnett/jones-lanes/g2-proof/read-model/w60_normalisation_check.py (pure Python Laurent polynomials; output in w60_normalisation_check.out). Checked: braid relations; contravariance G E_i = E_i^T G; invariance of H; e_1, e_2, e_4, e_5 kill v_{c_0}; T_c = A^-6 on span(D1..D4) and A^6 on v_c; H(v_c,v_c) = Delta_3; r(c_0, sigma_3 c_0) = 1/[3]^2; degree spans for sigma_3^k (k <= 6) and (sigma_3 sigma_4^-1)^k (k <= 5). No search, no sweep.

## 6. Sources read this session
- Bigelow, The Burau representation is not faithful for n = 5, GT 3 (1999), arXiv:math/9904100: Thm 1.4 and its proof (Section 3.0 above).
- Jackson-Kerler, arXiv:0912.2114 (Adv. Math. 228, 2011): Lemma 12, eqs. (57)-(68), Section 5 (Temperley-Lieb specialisation, non-split sequence).
- Ito, arXiv:1402.2028 (Math. Z. 280, 2015): Thm 1, Cor. 1-3, Long's Lemma 2.1 as quoted.
- Board: collab/THEORY-width-ladder.md (conventions of 1.3), collab/SCAFFOLD.md (B8, U5-W4, U5-W6), collab/DEAD_ENDS.md.
Not re-read: Bigelow's Lawrence-Krammer survey (theorem number for the image of absolute in relative homology quoted via JK), Jones 1987, Kasahara, BBB, Ishida (free group from two twists with i >= 2), the skein-algebra leading-term lemma.
