# Kernel side of the first rung: where a nontrivial element of ker W(5,1) would have to live

Lane g2-proof, label build-kernel. Claude (subagent), 2026-11-03. The Codex workspace was read only and not touched.
Tags: [PUB] published; [LIT] stated in a published source as recorded in a lane read report (file named); [EL] elementary, proved here; [NEW] proved here and not found in any lane report; [CHK] checked by the one computation in this folder; [SK] sketch with a named gap; [MEM] from memory, not re-checked; [CONJ] conjecture.

Conventions (as in read-model/model.md). sigma_i -> A + A^-1 e_i on W = W(6,0), which is W(5,1) on B_5. delta = -A^2 - A^-2, Delta_2 = delta^2 - 1 = A^4 + 1 + A^-4 (= [3]), Delta_3 = delta^3 - 2 delta = -[4]. Basis D1 = (12)(34)(56), D2 = (12)(36)(45), D3 = (14)(23)(56), D4 = (16)(23)(45), D5 = (16)(25)(34) (the rainbow). H(x,y) = xbar^T G y is the invariant Hermitian form (bar: A -> A^-1); it is the "B" of the task. c_0 = the curve around {1,2,3} (in D_5: the round curve around p1, p2, p3), T_{c_0} = (s1 s2)^3, v_0 = v_{c_0}, and v~ := Delta_2 v_0 = (-delta, 1, 1, -delta, Delta_2) in the D-basis. rho is the projective genus-two representation of Mod(S_{0,6}) on W, and Kbar = {g : rho(g) scalar}. SI is the image of the Torelli group I_2 in Mod(S_{0,6}) (Birman-Hilden), BI_5 the braid Torelli group. "q = -1" means A = zeta := e^{i pi/4}: A^4 = -1, delta = 0, Kasahara's t = -1, h = 0. For a 3|3 curve c, gamma_c is its lift (a separating curve in S_2) and P_c, a symplectic plane in H := H_1(S_2; Z), is the homology of one side. So H = P_c (+) P_c^perp; this is "the splitting of c". Throughout, |g| is the word length of a braid in the sigma_i^{+-1}.

---------------------------------------------------------------------------------------------------

## 0. Results in one screen

1. **Location** [LIT + EL]. Kbar lies in SI, which is isomorphic to I_2 (Kasahara 2001 Thm 5.1; reproved in 2.1 from the q = -1 dictionary). In braid terms, ker W(5,1) lies in BI_5 u Delta^2 BI_5, inside the pure braid group, and ker rho cap I_2 is the intersection of all of Kasahara's F_k. Nothing outside Torelli, and nothing that any q = -1 count (BBB parity, determinants) can see.

2. **Theorem A** [NEW; proof uses Kasahara's Lemma 2.1; identity CHK]. For 3|3 curves c, c' the projective invariant r(c,c') = |H(v_c,v_c')|^2 / Delta_3^2 is regular at q = -1, and
       r(c,c')(zeta) = (2D - 1)^2,   D = det(x, y, x', y') in Z,
   for symplectic bases (x,y) of P_c and (x',y') of P_c'. So H(v_c, v_c') is never zero at generic A, for any intersection number. The F6 mechanism (orthogonal spin-3/2 lines give [T_c, T_c'] in the kernel) never fires. The orthogonality mechanism that makes Burau_5 unfaithful has no 3|3 analogue.

3. **Zero-pairing trichotomy** [EL + NEW]. Cap system against cap system (no Jones-Wenzl projector): a 3-bridge link bracket, never zero (read-model 1.4). Curve against curve (two projectors): never zero (Theorem A). Curve against cap system (one projector): the only zeros that can occur. The q = -1 shadow allows H(v_c, S) = 0 exactly when gamma_c is *homologically* a reducing curve of the handlebody V_S, i.e. the meridian Lagrangian splits, L_S = (L_S cap P_c) (+) (L_S cap P_c^perp). Equivalently det plat(S, T_c, S) = 0. A KL(3|C) violation is a curve that is homologically reducing for V_S but not geometrically reducing, with zero pairing.

4. **Theorem B (exact location)** [EL; refines read-model Prop A]. Kbar != 1 iff there is f in SI with f(c_0) != c_0 and rho(f)[v_0] = [v_0]. Then kappa_f := [T_{c_0}, f] = T_{c_0} T_{f c_0}^-1 is a nontrivial kernel element, and every nontrivial kernel produces such a pair. kappa_f always lies in [I_2, I_2] and in F_2. It lies in F_3 iff a linear condition on the class of f in H_1(I_2) holds (2.4). Braid form: f in BI_5 outside <(s1 s2)^6, Delta^4>, and the candidate is [(s1 s2)^3, f].

5. **Certificate** [EL]. One Laurent-polynomial identity settles a candidate f:
       R_f := [rho(f) v~]_{D5} = +-A^m Delta_2,
   that is, R_f(A) R_f(A^-1) = Delta_2^2. The proof is Cauchy-Schwarz on the arc where H is definite. Knot form: the colour-3 network Theta(c_0, f c_0) evaluates like the colour-3 unknot (up to a unit). Pre-filter: |R_f(zeta)| = |2D - 1| must be 1. This is automatic on SI.

6. **Proposition C (depth beats length)** [EL, restatement-level]. For g of exponent sum 0, rho(g) = I iff ord_{A = zeta}(rho(g) - I) > |g|. So the kernel consists exactly of the Torelli elements whose Kasahara depth exceeds their length. All zeros forced at roots of unity draw on one budget of 4|g| zeros per entry: q = -1 (Kasahara, Torelli), q = 1 (pure braids, Drinfeld-Kohno side), and the 5th and 10th roots (the zrho lane). A finite truncation of Kasahara's expansion proves nothing without a length bound.

7. **What follows** [PUB + SK]. A certified kappa_f gives two routes.
   - Ito route (published): an explicit 5-braid knot closure(s1 s2 s3 s4 beta) with V = 1, genus >= N, hyperbolic.
   - Plat route (needs only W(6,0)): 3-bridge knots plat(kappa~^m s2 s4) with V = 1, nontrivial for large m by Hempel distance [SK, MEM].
   Either one refutes T.

8. **Why such a configuration could exist** (Section 6), with the counter-consideration from Theorem A.

Honest strength. Theorem A and the trichotomy are new and proved. The proof is a short q = -1 computation resting on Kasahara's published Lemma 2.1. Theorem B, the certificate and Proposition C are reformulations: read-model Prop A, Kasahara Thm 5.1, and the usual "degree versus order of vanishing" bound. Their value is that they pin the target down. Nothing here proves or refutes faithfulness. Faithfulness of W(5,1) still implies Burau_4 faithfulness, which is open; the transfer lane found a gap in BBB.

---------------------------------------------------------------------------------------------------

## 1. The q = -1 dictionary

**1.1 Input** [LIT: zrho/read-kasahara/kasahara.md, Kasahara 2001 Lemma 2.1 and Lemma 5.4]. At t = -1 the genus-two representation is (Lambda^2 H / omega) (x) sgn, pulled back through Sp(4,Z), and Lambda^2 H/omega is faithful on PSp(4,Z). Over Q, Lambda^2 H/omega is isomorphic to Lambda^2_0 := omega^perp, a subspace of Lambda^2 H_Q of dimension 5, with the wedge pairing <alpha, beta> = alpha ^ beta / vol and omega ^ omega = 2 vol.

**1.2 The form at q = -1** [EL; CHK]. At delta = 0 every Gram entry delta^{loops} vanishes, so H itself dies. B' := H/delta (entries delta^{loops - 1}) is regular. At delta = 0 it is the one-loop meander matrix: ones exactly at the meander pairs {D1,D4}, {D2,D3}, {D2,D5}, {D3,D5}, determinant -2, signature (2,3). It is invariant (by continuity from delta != 0) and nondegenerate. Because the q = -1 representation is irreducible, B'(zeta) is a multiple of the wedge pairing.

**1.3 Dictionary** [EL]. Let Phi: W(zeta) -> Lambda^2_0 (x) C be an isomorphism of projective representations.
- *3|3 curve c.* rho(T_c) = A^-6 (1 + (A^12 - 1) P_c). By rainbow duality P_c = v_c (x) [.]_{rb_c}, which is regular at zeta. So rho_zeta(T_c) = zeta^-6 (1 - 2 P_c(zeta)), a reflection whose special line is [v_c(zeta)], with v_0(zeta) = D5 - D2 - D3. The lift J_c in Sp(4,Z) is -1 on P_c and +1 on P_c^perp. On Lambda^2_0 it is +1 exactly on u_c := omega_{P_c} - omega_{P_c^perp} = 2 x^y - omega, and -1 on P_c (x) P_c^perp. Multiplicity-one eigenlines correspond, so Phi[v_c(zeta)] = [u_c]. Also <u_c,u_c> = -2 = B'(v_c,v_c)(zeta) = (delta^2 - 2)|_{delta=0}.
- *Cap system (cup diagram) S.* Phi[S(zeta)] = [omega_{L_S}]. Here L_S is the span of the lifts of the three arcs, a Lagrangian (the meridian lattice of the handlebody V_S), and omega_L = l1 ^ l2 is a null vector. It is the unique line fixed by the Siegel parabolic Stab(L_S).
- *Arc alpha.* im e_alpha -> a ^ a^perp, an isotropic 2-plane, where a is the lift of alpha. At zeta, sigma_alpha / A = 1 - i e_alpha is unipotent and matches the transvection T_a.
- *Pairings.* <u_c, u_c'> = 4D - 2 with D = det(x,y,x',y'). <u_c, omega_L> = 2 det(x, y, l1, l2). <omega_L, omega_L'> = det(l1, l2, l1', l2'), which is +-1 iff L (+) L' = H; this matches the meander pairs.
Proof of the first pairing: (2x^y - omega) ^ (2x'^y' - omega) = 4 x^y^x'^y' - 2 x^y^omega - 2 omega^x'^y' + omega^omega = (4D - 2 - 2 + 2) vol, because x^y^omega = vol for a symplectic plane. The others are the same computation, using omega ^ omega_L = 0 for L Lagrangian.

---------------------------------------------------------------------------------------------------

## 2. Where the kernel lives

**2.1 Torelli** [LIT + EL]. Let g be in Kbar. Then rho_zeta(g) is scalar, so g maps to +-I in Sp(4,Z), because Lambda^2_0 is faithful on PSp(4,Z). Hence g is in SI. This is Kasahara's Thm 5.1, projectively.
- SI lies in PMod(S_{0,6}). A Torelli element acts trivially on H_1(S_2; F_2), and Sp(4,F_2) = S_6 permutes the Weierstrass points.
- So g fixes p6 and lifts to B_5. In B_5, ker W(5,1) lies in the preimage of {+-I}, which is BI_5 u Delta^2 BI_5 (Delta^2 maps to -I). All of it is pure.

**2.2 Same splitting** [EL]. Suppose [v_c] = [v_c'] at generic A. At zeta this gives [u_c] = [u_c'], so u_c' = +-u_c and c, c' have the same (unordered) splitting.
- Then c' = f(c) for some f in SI. The stabiliser of gamma_c maps onto the stabiliser of {P, P^perp} in Sp(4,Z), which is (SL_2 x SL_2) x| Z/2: use Mod(S_1^1) x Mod(S_1^1) and a handle swap.
- Stab_{SI}(c) = <T_c^2>. An element of I_2 preserving gamma_c restricts to each genus-one side as a Torelli element of Mod(S_1^1), and such an element is a boundary twist.
- Distinct curves with the same splitting have i(c,c') >= 4. Intersection numbers are even, and the unique i = 2 orbit has different splittings: P_{c_0} = <a1,a2>, while P_{s3 c_0} = <a1, a2 + a3>.

**2.3 Theorem B** [EL]. Kbar != 1 iff there is f in SI with f(c_0) != c_0 and rho(f)[v_0] = [v_0]. In that case kappa_f = [T_{c_0}, f] = T_{c_0} T_{f c_0}^-1 is in Kbar and is nontrivial.
*Proof.*
- (<=) rho(T_c) is determined by P_c, which is determined by the line [v_c]. So rho(T_{f c_0}) = rho(f) rho(T_{c_0}) rho(f)^-1 = rho(T_{c_0}). Also kappa_f != 1, since T_c = T_c' iff c = c'.
- (=>) read-model Prop A gives c != c' with [v_c] = [v_c']. Conjugate c to c_0 and apply 2.2. QED
In braids: f is in BI_5 \ <(s1 s2)^6, Delta^4>, and kappa^_f = [(s1 s2)^3, f]. Then rho_{W(5,1)}(kappa^_f) = I exactly: a scalar commutator has determinant 1, and it is trivial at A = 1 because kappa^_f is pure.
Remarks.
- (a) In genus two kappa_f = T_gamma T_{f gamma}^-1 is a difference of two separating twists with the same splitting. In Mess's free basis of I_2 (one separating twist per splitting [MEM: Mess, Topology 31 (1992)]) these are conjugate generators, so kappa_f lies in [I_2, I_2].
- (b) f = T_d^{2m} never works. rho(T_d^{2m}) fixes [v_0] only if P_d P_0 = 0, which Theorem A excludes, or P_d = P_0. So no seed [T_c^a, T_d^b] is a kernel element unless the two lines already coincide.

**2.4 Kasahara's filtration on candidates** [EL]. Expand at t = -e^h.
- *Twist expansion.* For a separating curve gamma with splitting s, Jones's formula gives rho(psi) eigenvalues t^6 (x4) and t^-24 (zrho/read-kasahara). Since P is idempotent, the normalised twist is exactly rho(T_gamma) = exp(-30h (P_gamma(h) - I/5)), and P_gamma(0) = P_{u_s}. So the first-order term depends only on the splitting. This matches Kasahara Cor 1.2 (F_2 = ker tau_2) and Morita's tau_2(T_gamma), a function of omega_P.
- *Notation.* For f in I_2, let n_s(f) be its exponent sum in the Mess generator of splitting s, i.e. its class in H_1(I_2) = Z^(splittings). Write D_s = D(s_0, s); the expression below is unchanged when P_s is swapped with P_s^perp.
- kappa_f is in F_2 always.
- kappa_f is in F_3 iff m(f) := sum_s n_s(f) (2 D_s - 1) u_s lies in Q u_{s_0}.
  *Proof.* rho(kappa_f) - I = (lambda - 1)(P_{c_0} - P_{f c_0})(1 + O(h)) = 30 h^2 [rho_1(f), P_{u_0}] + O(h^3). Here rho_1(f) = -30 sum_s n_s (P_{u_s} - I/5) and [P_u, P_{u_0}] = (<u,u_0>/4)(u (x) u_0^flat - u_0 (x) u^flat). The sum vanishes iff m(f) is parallel to u_0.
  The condition is automatic for f in [I_2, I_2], and nontrivial otherwise, because 2D_s - 1 != 0 (Theorem A).
- For f = [T_{gamma1}, T_{gamma2}], kappa_f is in F_4 iff (2D_{20} - 1) u_1 - (2D_{10} - 1) u_2 lies in Q u_0. In particular the three splitting vectors must be coplanar.
- Beyond this graded level, the conditions involve the curves themselves and not only their splittings, through the h-dependence of P_gamma(h).

**2.5 Proposition C (depth beats length)** [EL].
- *Statement.* Let g have exponent sum 0. The entries of rho(sigma_i^{+-1}) lie in {A^{+-1}, -A^{-+3}, 0}, so the entries of rho(g) - I are Laurent polynomials with integer coefficients and A-degree span at most 4|g|.
- *Proof.* If every entry vanishes to order d at zeta, Galois invariance makes it divisible by Phi_8(A)^d = (A^4 + 1)^d, which has span 4d. Hence rho(g) = I iff d(g) := ord_zeta(rho(g) - I) > |g|.
- *Normalisation.* On exponent-sum-0 elements of I_2, d(g) is Kasahara's depth. For kappa_f the cleaner invariant is r_f - 1 = (R_f Rbar_f - Delta_2^2)/Delta_2^2. If kappa_f is in F_k, it vanishes to order >= 2(k - 1) at zeta, while span(R_f) <= 4|f| + 8. So kappa_f is in F_k with k > |f| + 3 forces kappa_f into the kernel.
- *The budget.* Forced zeros elsewhere on the unit circle count against the same 4|g|: at A = +-1 (pure braids, the Drinfeld-Kohno filtration) and at the 5th and 10th-root points where I_2 acts by scalars (zrho lane).
- *Commutators do not help.* Kasahara depth is at least the lower-central depth, but nontrivial elements of Gamma_k of a free group have length superlinear in k [MEM: Malestein-Putman; Elkasapy-Thom]. A commutator adds contact orders while doubling length.
- *Conclusion.* A kernel element needs the graded kernel to recur at every level (6, R2).

---------------------------------------------------------------------------------------------------

## 3. Theorem A and the zero-pairing trichotomy

**3.1 Theorem A** [NEW]. For 3|3 curves c, c' (c' = g c_0), r(c,c') is regular at zeta, and r(c,c')(zeta) = (2D - 1)^2 = |R_g(zeta)|^2.
*Proof.*
- r = |H(v_c,v_c')|^2 / Delta_3^2 = |B'(v_c,v_c')|^2 / (delta^2 - 2)^2. B' is regular and (delta^2 - 2)(zeta) = -2.
- By 1.2 and 1.3, B'(zeta) = mu <.,.> o Phi and Phi(v_c(zeta)) = eps u_c, with mu eps^2 = 1 (both norms are -2).
- Projective equivariance changes the scalar only by a unit, so r(zeta) = <u_c, u_c'>^2 / 4 = (2D - 1)^2.
- By rainbow duality, H(v_0, rho(g) v~) = Delta_3 R_g, so r = |R_g|^2 / Delta_2^2. Since Delta_2(zeta) = -1, |R_g(zeta)| = |2D - 1|. QED
[CHK] build-kernel/shadow_identity_check.py verifies r(c_0, g c_0)(zeta) = (2D - 1)^2 exactly for 7 braids (D in {-1, 0, 1}), including D = -1 with r = 9. It runs in seconds.

*Corollary A1.* H(v_c, v_c') != 0 in Q(A) for every pair c, c' and every i(c,c'). F6 is vacuous. rho restricted to <T_c, T_c'> is never abelian unless [v_c] = [v_c']. read-model's "F6 needs i >= 4" is superseded: F6 never applies.

*Corollary A2: comparison with Burau.* For Burau_n the rank-one objects are arcs. At t = -1 their pairing is the algebraic intersection omega(a,b) of the lifts, which can vanish. Bigelow's Burau_5 kernel and Long-Paton/Moody for n >= 6 are all witnessed by such orthogonal pairs. For 3|3 curves the t = -1 pairing is 4D - 2, never zero. So a kernel of W(5,1), if one exists, is not produced by any orthogonal rank-one pair. It would be a pure coincidence [v_c] = [v_c'], a kind of kernel not seen in the known unfaithful generic-parameter Jones-type representations.

*Corollary A3: link to the transfer lane.* Any argument that reads the curve-curve pairing at q = -1 sees only the integer 2D - 1. Hence it separates different splittings, which Theorem A already does, and is blind on same-splitting pairs, which is where every kernel element lives (2.2). This is the curve-pair form of the transfer lane's Shadow Lemma.

**3.2 Cap against cap: never zero** [EL, read-model 1.4]. The pairing of braided cup diagrams is the bracket of a 3-bridge link, and V_L(1) = (-2)^{#L - 1} != 0. Hence:
- No two cap planes C_alpha = im e_alpha, C_beta are orthogonal, so the rank-two analogue of F6 for half-twists ([sigma_alpha, sigma_beta] with E_alpha E_beta = 0) is also vacuous.
- A coincidence C_alpha = C_beta with alpha != beta is equivalent to unfaithfulness: if g is in the kernel and moves alpha, then rho(sigma_{g alpha}) = rho(sigma_alpha).
- By 1.3 its shadow forces [a] = +-[b], i.e. homologous lifts.

**3.3 Curve against cap system: the live zeros. Proposition D** [NEW, EL]. For a 3|3 curve c and a cap system S, B'(v_c, S)(zeta) = 2 mu' det(x, y, l1, l2). The following are equivalent:
- (i) this shadow vanishes;
- (ii) L_S cap P_c != 0 (rationally);
- (iii) L_S = (L_S cap P_c) (+) (L_S cap P_c^perp);
- (iv) J_c L_S = L_S;
- (v) det plat(S, T_c, S) = 0, i.e. H_1(Sigma_2(plat(S,T_c,S)); Q) = Q^2, as for U_3.
*Proof.*
- (i) <=> (ii): det = 0 iff P + L != H, iff L cap P != 0.
- (ii) => (iii): if v is in L cap P, the second basis vector of L lies in v^perp = <v> (+) P^perp.
- (iii) <=> (iv): immediate.
- (iv) <=> (v): Sigma_2 of the plat is V_S glued to V_S by the lift of T_c, which acts on H as J_c, so H_1 = H/(L + J_c L). If L is not split, L cap J_c L = 0 and H_1 is finite. QED
*Reading.* A separating curve that bounds a disk in V_S (a reducing curve, the Heegaard lane's Haken(c)) splits L_S. Proposition D says the shadow detects exactly the homological version of this. So a KL(3|C) violation (H(v_c, S) = 0 with no arc of S off c) is a separating curve that is homologically but not geometrically reducing for V_S. By the Heegaard lane's Prop D, each such violation puts T_c in Stab[S] \ Hilden(S). It gives 3-bridge "twisted unlinks" plat(S, T_c^k, S), k != 0, whose Jones polynomial is that of U_3 for all k.

**3.4 What a kernel needs, in this language.** By read-model Prop B, unfaithfulness means H(v_c', D_i) = 0 for the four c_0-adapted cap systems D1, ..., D4, where c' = f(c_0).
- By Proposition D all four vanish at q = -1 automatically when c' has the splitting of c_0: each L_{D_i} is split along P_{c_0}.
- So a kernel is four simultaneous one-projector zeros at a homologically reducing curve.
- Cauchy-Schwarz compresses the four into the single identity of Section 5.

---------------------------------------------------------------------------------------------------

## 4. What a candidate must look like

- **Shape.** A candidate is kappa^_f = [(s1 s2)^3, f], with f in BI_5 and f not in <(s1 s2)^6, Delta^4> (2.3).
- **Passed for free.** Every such f passes the shadow, since |R_f(zeta)| = 1 and D is in {0,1}. Every kappa_f passes the first Kasahara order (F_2).
- **Not one twist.** f is not a power of a single twist (2.3 (b)).
- **The first nontrivial class: f in <T_{d1}^2, T_{d2}^2> = F_2.** Here d1, d2 are 3|3 curves meeting c_0.
  - Let Pi = span(v_{d1}, v_{d2}). The pseudo-reflections R_i = 1 + (lambda - 1) P_{d_i}, with lambda = A^24, preserve Pi and fix Pi^perp pointwise.
  - Write v_0 = w + w^perp with w in Pi. Then w != 0 by Theorem A.
  - So rho(f)[v_0] = [v_0] iff either rho(f)|_Pi fixes w (when w^perp != 0), or v_0 lies in Pi and w is an eigenvector.
  - This is a 2 x 2 problem. In the basis (v_{d1}, v_{d2}), R_1 = [[lambda, (lambda-1) beta], [0, 1]] and R_2 = [[1, 0], [(lambda-1) betabar, lambda]], with beta = H(v_{d1}, v_{d2}) / Delta_3. So |beta|^2 = r(d1, d2), and its q = -1 value is (2D_{12} - 1)^2.
  - If u_0, u_1, u_2 are independent, the F_3 condition (2.4) forces both exponent sums of f to vanish. Then det rho(f)|_Pi = 1, and fixing w != 0 means that rho(f)|_Pi is either the identity (a kernel of the 2 x 2 representation of F_2 itself) or a parabolic whose fixed line is exactly [proj_Pi v_0].
  - So the simplest candidates are commutator-subgroup words in two separating twists whose 2 x 2 image is parabolic (trace identically 2) with a prescribed fixed line. Generic two-generator subgroups of SL_2 have no nontrivial word with trace identically 2 (Horowitz-type [MEM]). Here the parameters lie on the curve A -> (lambda, beta), so the question is genuinely open. Proposition C again says it is decided at a finite order.
- **Several twists.** For f in <T_{d1}^2, ..., T_{dm}^2>, the same reduction gives a word problem in a complex reflection group on span(v_{d_i}). Its data are the Gram matrix H(v_{d_i}, v_{d_j}), the pairings H(v_{d_i}, v_0) (evaluations of Theta-networks), and lambda.

---------------------------------------------------------------------------------------------------

## 5. The certificate and what follows

**5.1 The single identity** [EL]. Given f as a braid word (in B_5, or B_6), compute R_f = [rho(f) (-delta, 1, 1, -delta, Delta_2)^T]_{D5} over Z[A^{+-1}], using the action table of read-model/w60_normalisation_check.py.
**Certificate: R_f = +-A^m (A^4 + 1 + A^-4).**
*Why one identity suffices.*
- W(6,0) is definite on the arc t = e^{i phi}, |phi| < pi/2 (build-heegaard P3 [CHK there]), and rho is H-unitary there.
- On that arc r(c_0, f c_0) = |R_f|^2 / Delta_2^2 <= 1, with equality iff rho(f) v_0 is parallel to v_0.
- R_f Rbar_f = Delta_2^2 makes r identically 1. So the 2 x 2 minors of [v_0 | rho(f) v_0] vanish on an arc, hence identically.
- Conversely, line equality gives R_f = mu Delta_2, with mu an eigenvalue in Z[A^{+-1}]^x = {+-A^m}.
- Unique factorisation (Delta_2 = A^-4 Phi_3 Phi_6 Phi_12, all self-reciprocal) shows that R_f Rbar_f = Delta_2^2 already forces R_f = +-A^m Delta_2.
*Equivalent forms.*
- e_1 rho(f) v~ = e_2 rho(f) v~ = 0, since [v_0] = ker e_1 cap ker e_2.
- H(D_i, rho(f) v_0) = 0 for i = 1..4.
- rho([T_{c_0}, f]) = I_5.
- The colour-3 network Theta(c_0, f c_0) has the evaluation of the colour-3 unknot, Delta_3, up to a unit.
*Cost.* Exact Laurent arithmetic, milliseconds for words of length in the hundreds.
*Nontriviality.* f(c_0) != c_0, i.e. f is not in <(s1 s2)^6, Delta^4>. Check this with any faithful representation, for example Lawrence-Krammer.

**5.2 Ito route** [PUB: Ito, Math. Z. 280 (2015), Thm 1; Long 1986 Lemma 2.1; Bigelow 1999].
- Let kappa^ = [(s1 s2)^3, f] be certified. It is a nontrivial element of ker W(5,1).
- Let beta_B be Bigelow's explicit element of ker Burau_5 = ker W(5,3) [MEM: the commutator [psi1^-1 s4 psi1, psi2^-1 s4 s3 s2 s1^2 s2 s3 s4 psi2] of Bigelow 1999].
- Choose g in B_5 with h := [kappa^, g beta_B g^-1] != 1. This exists by Long: otherwise kappa^ would centralise a noncentral normal subgroup.
- Then h lies in ker W(5,1) cap ker W(5,3) cap [B_5, B_5], i.e. in the kernel of the full TL representation W(5,1) + W(5,3) + W(5,5).
- Let N_h be the normal closure of h, a noncentral normal subgroup. By Ito's Thm 1 there is a pseudo-Anosov pure beta in N_h with beta >_D (s1 s2 s3 s4)^-1 Delta^{2N}.
- Then K = closure(s1 s2 s3 s4 beta) is a knot (beta is pure), V_K = 1 (same TL image and the same writhe, since beta has exponent sum 0), genus >= N, hyperbolic, braid index 5. In particular K is nontrivial and T is false.

**5.3 Plat route** [EL + SK]. This route needs only the W(6,0) kernel, with no Burau_5 and no Long.
- Lift kappa to kappa~ in [B_6, B_6]. Then rho(kappa~) = I.
- Since <plat beta> = H(c, rho(beta) c) for the cup vector c, every 3-bridge knot K_m = plat(kappa~^m s2 s4) has V = V(unknot) = 1, with the same writhe.
- For m large K_m should be nontrivial. Choose kappa (in Kbar, a nontrivial normal subgroup) pseudo-Anosov with laminations off the limit sets of the two handlebody groups; these limit sets have measure zero (Masur; Kerckhoff [MEM]). Then the Hempel distance of the induced genus-two splitting of Sigma_2(K_m) tends to infinity (Hempel 2001, Abrams-Schleimer 2005 [MEM]).
- So the splitting is irreducible, Sigma_2(K_m) != S^3, and K_m != unknot.
- This would refute T_3 (the 3-bridge case) directly. The gap: the existence of such a pseudo-Anosov in Kbar, and the distance theorem, are quoted from memory.

---------------------------------------------------------------------------------------------------

## 6. Why such a configuration could exist, and what argues against it

- **(R1) The shadow is blind exactly there.**
  - On SI, q = -1 is the identity.
  - The first order sees only splittings, so same-splitting pairs agree to first order automatically.
  - Every count at q = -1 is blind on the whole region where kernels must live: BBB's parity count (transfer lane), determinants of the twisted plats (3.3), and the curve-pair integer 2D - 1 (A3).
  - The first real constraint is the order-2 linear condition of 2.4.
- **(R2) The graded data cannot separate.**
  - Gamma_k(I_2)/Gamma_{k+1} has infinite rank, while Kasahara's G_k (inside sl_5, of dimension 14 or 10) is finite. So the associated graded map has an infinite-rank kernel in every degree.
  - If faithfulness is true, it must come from the h-dependence of the spin-3/2 lines P_gamma(h) of curves sharing a splitting. That is a transcendence-type statement, not a Lie-algebra one.
- **(R3) The budget can be beaten in this family.** Burau_5 = W(5,3) is a one-variable Jones-type representation with symplectic shadow at t = -1 and kernel inside BI_5. Its kernel elements beat the bound of Proposition C. So "infinite depth at finite length" is realised one shape over.
- **(R4) Against.** The specific mechanism behind Burau_5 (an orthogonal rank-one pair) is impossible here (Theorem A).
  - The only witnesses left are one-projector zeros at homologically reducing curves. These are 3-bridge twisted unlinks with the unlink's Jones polynomial.
  - Jones-unlink coincidences do occur for links (Thistlethwaite 2001; Eliahou-Kauffman-Thistlethwaite 2003, per build-heegaard), but none is known to be 3-bridge, and a kernel needs four simultaneous ones at a single curve.
  - This removes the only known mechanism. It is not a proof of faithfulness, and I would not call it evidence in any quantitative sense.

**Targets this suggests, by strength.**
- (i) The 2 x 2 parabolic problem of Section 4. Settling it in either direction for the class <T_{d1}^2, T_{d2}^2> is weaker than faithfulness, since it covers only one candidate class.
- (ii) A linear bound "Kasahara depth(kappa_f) <= C |f|". This is equivalent to faithfulness (Proposition C), hence implies Burau_4.
- (iii) KL(3|C) restricted to homologically reducing curves. This is faithfulness-strength, by Proposition D and read-model Theorem D.

---------------------------------------------------------------------------------------------------

## 7. Computation log

- **Script.** build-kernel/shadow_identity_check.py; output in shadow_identity_check.out. Pure Python with exact Gaussian integers at A = zeta (sigma_i / A = 1 - i e_i, delta = 0), and integer symplectic transvections on H_1(S_2) (chain a1, ..., a5 with a5 = -a1 - a3).
- **Identity checked.** r(c_0, g c_0)(zeta) = |[rho(g) v_0]_rb|^2 = (2 D(c_0, g c_0) - 1)^2, for the following braids:
  - g = s3 (i = 2, D = 0);
  - T_e Omega^2, with e around {2,3,4} and Omega = s1...s5 (D = -1, r = 9);
  - Omega^2 (D = 1);
  - T_d^2 with d = s3 c_0 (same splitting, D = 0);
  - (s3 s4^-1)^3;
  - two further products.
  All match.
- **Also checked.** The braid relations at zeta, B'(v_0, v_0) = -2, and B'(v_0, D_i) = (0, 0, 0, 0, -2).
- **Cost.** It is one identity on hand-picked words: no search and no sweep. Runtime under a second.

Sources used: lane reports read-model/model.md, build-transfer/transfer.md, build-heegaard/heegaard.md, zrho/read-kasahara/kasahara.md (Kasahara 2001 Lemma 2.1, Thm 5.1, Cor 1.2, Jones's formula (2.2)), and the read reports quoted in the task. No new web reading was needed.
