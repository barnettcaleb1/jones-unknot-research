# build-transfer: does the Bharathram-Birman-Brendle proof transfer to W(5,1)?

Lane g2-proof / build-transfer, 2026-11-03. Author: Claude (subagent). The board workspace was only read.

Tags: [PUB] published result; [READ] read this session (BBB arXiv HTML v2, two targeted passes; BMP title and abstract via search); [EL] elementary, proved here; [CHK] checked by one of the two tiny scripts in this folder (each runs in under a second); [BOARD] taken from read-model or the board, not re-derived; [MEM] from memory, a pointer only; [CONJ] conjecture.

Notation. rho_n is unreduced Burau (BBB's convention: braids act on the right). alpha is the arc p1p2, beta*_3 the arc from the boundary basepoint p* to p3, and M_Phi = M(alpha, (beta*_3)Phi) = sum_{i=1..m} eps_i t^{k_i} in unsimplified form (one term per intersection point, m = iota in minimal position). Delta_i is the disk sequence and P(Delta) the set of punctures inside. BI_n is the kernel of Burau at t = -1, the braid (hyperelliptic) Torelli group. For W(5,1), q is the puncture variable of the Lawrence two-point model on the Jones line t = -q^{-1}; q = -1 corresponds to A^4 = -1 (Burau's t corresponds to A^{-4} or A^{4}).

---

## 0. Verdict

**Deliverable (ii): an obstruction.** The obstruction is structural. It applies to BBB's own n = 4 argument, not only to n = 5.

1. **Shadow Lemma [EL].** For arcs with Bigelow data (eps_i, k_i), BBB's parity condition is *equivalent* to |M(-1)| = number of intersection points. So "parity, hence no cancellation, hence L1 norm = iota" computes the value of the pairing at t = -1, which is the algebraic intersection number of the lifts to the double branched cover. Corollary 6.8 compares two such numbers, so it can only ever prove f(Phi) is not in ker(rho_5 at t = -1).
2. **BBB itself [EL + CHK + PUB].** ker(Burau_4 at t = -1) = BI_4 (Brendle-Margalit-Putman 2015) meets Brun_4 nontrivially. An explicit element is Phi0 = [(s1 s2)^6, [[y1,y2],y3]], checked to be the identity at t = -1 and not the identity at t = 2. For every such Phi, no Gamma can satisfy the conclusions of Prop. 6.7. So Lemma 6.3, Prop. 6.7 or the conjugation step of Thm 6.9 fails on Brun_4 ∩ BI_4. Every possible Burau_4 kernel element lies in BI_4, so the argument as written has no content for the faithfulness question. **Burau_4 should be treated as open.** This does not refute Burau_4 faithfulness.
3. **W(5,1) [EL + CHK + PUB].** In the two-point Lawrence model, BBB-type parity is again equivalent to coherence at q = -1. There W(5,1) is projectively trivial on T_c^2, checked at A = e^{i pi/4}, hence trivial on BI_5. Every kernel element of W(5,1) lies in BI_5, by Kasahara's Thm 5.1, and in fact in ker tau_2 = F_2 (Kasahara Cor. 1.2). So the method is blind exactly where a kernel element has to live.
4. **What transfers.** Long's reduction, Moody's one-way criterion, stabilization (W(6,0)|B_5 = W(5,1)), and the free-group conjugation transfer as they stand. A two-point winding lemma and a minimal-position lemma are needed (both routine or moot). Parity, the single-violator taxonomy, the one-push repair and the unequal-count step fail. The last one fails necessarily.
5. **What any replacement needs.** It needs cancellation control that does not factor through a specialization, for example sign coherence of extremal terms only (Bigelow's lexicographic mechanism; read-model's Conjecture LT). That is faithfulness-strength. Section 5 shows that one-sided variants of BBB reduce to the original cancellation problem.

---

## 1. The Shadow Lemma

### 1.1 Statement and proof [EL]

The setting is BBB Section 3. Take arcs alpha (between punctures) and beta (from p* to a puncture). Number the points of alpha ∩ beta as q_1..q_m along beta, with signs eps_i, exponents k_i and disks Delta_1..Delta_{m-1}. Then the following are equivalent:
- (a) **parity**: Delta_i is sign-changing iff |P(Delta_i)| is odd, for every i;
- (b) eps_i (-1)^{k_i} does not depend on i;
- (c) the unsimplified M(alpha,beta)(-t) = sum eps_i (-1)^{k_i} t^{k_i} has all coefficients of one sign;
- (d) |M(alpha,beta)(-1)| = m.

*Proof.* BBB Lemma 3.1 (Bigelow) gives k_{i+1} - k_i = W_i = ±|P(Delta_i)|, so (-1)^{k_{i+1}-k_i} = (-1)^{|P(Delta_i)|}. Condition (a) says eps_{i+1} eps_i = (-1)^{|P(Delta_i)|}, and this is exactly (b). The implications (b) ⇒ (c) ⇒ (d) are immediate. For (d) ⇒ (b): a sum of m signs has absolute value m only if all of them agree. ∎

The definitions were confirmed in the paper [READ]: a disk is sign-changing iff eps_i = -eps_{i+1}; the parity condition reads "sign-changing if and only if |P(Δ)| is odd"; and W_i = ±(number of punctures in Delta_i).

**Corollary 1 (BBB's Lemma 4.2, sharpened).** Parity implies no cancellation, and the L1 norm of M equals |M(-1)| = m.

**Corollary 2 (blindness).** Let X ∈ ker(rho_n at t = -1) and Gamma ∈ B_n. Take any representatives of the arcs (beta*_3)XGamma and (beta*_3)Gamma. If both satisfy parity, they meet alpha in the same number of points.

*Proof.* Each count equals |M(-1)|, by Corollary 1. Also M_{XGamma}(-1) = M_Gamma(-1), because the classes [(beta*_3)XGamma] and [(beta*_3)Gamma] agree mod (t+1) and M is Z[t^±]-linear in the class. ∎

BBB's Corollary 6.8 has this form: "f(Phi)Gamma and Gamma both satisfy parity, the intersection numbers differ, hence M_{f(Phi)Gamma} ≠ M_Gamma". The proof [READ] uses no cancellation in either polynomial, so each sum of absolute values of coefficients equals the intersection number. By Corollary 2, an argument of this form proves the stronger statement f(Phi) ∉ ker(rho_5 at t = -1).

### 1.2 Meaning [EL, classical]

Let Sigma be the double cover of D_n branched over the punctures: Sigma_{1,1} for n = 3, Sigma_{1,2} for n = 4, Sigma_{2,1} for n = 5.
- alpha lifts to a closed curve alpha^, and beta lifts to an arc.
- M(alpha,beta)(-1) is the algebraic intersection number of the two lifts. Parity says that all their intersections have the same sign.
- rho_n at t = -1 is the action of B_n ⊂ SMod(Sigma) on H_1(Sigma, lifts of p*).

So BBB's parity machinery measures the double-cover (symplectic) shadow of the Burau pairing.

### 1.3 Consistency checks [READ]

- **n = 3.** At t = -1, B_3 maps to SL(2,Z) with kernel <Delta^4>, which is central. On a once-holed torus, a simple closed curve and an essential arc in minimal position meet with a single sign. BBB's Thm 4.1 ("every 3-braid satisfies parity") is this classical torus fact, and the parity re-proof of Magnus-Peluso is valid, because the shadow is faithful modulo the centre for n = 3.
- **BBB Section 7.** M_{Phi Gamma} = 2 + t^2 + t^4 - t^3 - t + t^-4 + t^-2. Substituting -t makes all seven coefficients positive, with total 8 = L1. M_Gamma = 2t^-3 - 3t^-2 + 4t^-1 - 5 + 3t - 2t^2 + t^3. Substituting -t makes every coefficient negative, with total 20 = number of terms. Both are as the lemma predicts.

---

## 2. Consequence for BBB's n = 4 argument

This shows a gap in the proof. It does not show that the theorem is false.

### 2.1 The t = -1 kernel meets Brun_4 [PUB + CHK]

- **Published facts.** Brendle-Margalit-Putman, Invent. Math. 200 (2015) 263-310 [READ: title and abstract], identify the kernel of Burau at t = -1 with the hyperelliptic Torelli group BI_n. It is generated by squares of Dehn twists about curves surrounding an odd number of punctures. Brendle-Childers-Margalit show it has cohomological dimension floor(n/2) [ABS via search], so it is large for n ≥ 4. The unreduced kernel lies between the normal closure of (s1 s2)^6 and the reduced kernel, so it is BI_4 as well.
- **The explicit element.** Let c be the curve around {p1,p2,p3} in D_4, so T_c^2 = (s1 s2)^6. Let y_i = A_{i4} be the push of p4 around p_i, and Psi = [[y1,y2],y3].
  - Psi is Brunnian: forgetting p4 kills K_4, and forgetting p_i sets y_i = 1, which kills the double commutator.
  - Phi0 = [T_c^2, Psi] lies in Brun_4 ∩ ker(rho_4 at t = -1), since both are normal subgroups.
- **[CHK] (t_minus1_check.py).** The checks use exact rational arithmetic on a 112-letter word:
  - rho_4((s1 s2)^6) = I at t = -1;
  - rho_4(Phi0) = I at t = -1;
  - rho_4(Phi0) ≠ I at t = 2 and at t = 3/2, so Phi0 ≠ 1.

### 2.2 Proposition [EL]

Let Phi ≠ 1 lie in Brun_4 ∩ ker(rho_4 at t = -1); for example, any B_4-conjugate of Phi0. Then no Gamma ∈ B_5 makes f(Phi)Gamma and Gamma both satisfy parity with different intersection numbers. So Cor. 6.8 is false for Phi, and at least one of the following fails for Phi:
1. the conjugation step of Thm 6.9, which puts Phi in the form Phi'·Gamma_1 with the product proper;
2. Lemma 6.3, which says the only violators are nested 4-disks;
3. Prop. 6.7, which asks for parity of f(Phi)Gamma and of Gamma and for unequal iota;
4. Prop. 5.1 or Lemmas 6.4 and 6.6 as applied.

*Proof.* Observation 2.1 holds at t = -1, since rho_5(f(Phi)) = rho_4(Phi) ⊕ 1. So X = f(Phi) lies in ker(rho_5 at t = -1), and Corollary 2 applies. ∎

### 2.3 Where the text must break

- In my read of Cor. 6.8's proof, the inequality of the two intersection numbers is introduced with "we can assume" [READ, short phrase].
- Prop. 6.7 obtains the inequality by modifying gamma_2 with a loop in the complement of beta, in two figure-driven cases (Figs. 6.9-6.12, which I could not see).
- For Phi in the t = -1 kernel, Corollary 2 says that any such modification either keeps the count fixed or destroys parity of Gamma.
- So that is where a referee should test the argument, on Phi0 or on [T_c^2, Psi'] for any pseudo-Anosov Brunnian Psi'. I did not determine which of items 1-4 fails. One of them must.

### 2.4 Scope

- ker(rho_4) ⊂ ker(rho_4 at t = -1) = BI_4. So every potential kernel element lies in the set where the mechanism is blind.
- Off BI_4, the conclusion "Phi ∉ ker rho_4" is trivial, because rho_4(Phi) is already nontrivial at t = -1. So, as written, the argument says nothing about the faithfulness question.
- BBB never mention t = -1, the double cover or BI_n [READ].
- For the lane: the claim "one step above BBB" should read "implies Burau_4 faithfulness, which is open; BBB's claimed proof has a gap on Brun_4 ∩ BI_4".

---

## 3. Step-by-step transfer to W(5,1)

**Model [PUB via read-model, BOARD].**
- W(5,1) is the submodule of LKB_5 at t = -q^{-1} (Jackson-Kerler, Lemma 12).
- Test objects are product surfaces: cap squares S_C (two disjoint caps), or the 3|3 vectors v_c, against dual tori.
- The pairing is a sum over intersection pairs (x,y) of eps(x,y) (-1)^{b} q^{a-b}. Here a is the sum of the puncture windings of the two coordinate loops, and b = b_m + 2(mutual winding).
- Parked-point form: fixing y, the x-sum is a one-point Burau pairing in D_5 ∪ {y}, with y of weight q^{-2}.

| # | BBB step | W(5,1) | Note |
|---|---|---|---|
| 1 | Long reduction to Brun_n (Prop 1.2); pA input (Whittlesey, Lee-Song) | transfers | Long 1986. The centre acts on W(5,1) by A^-12, so a kernel is noncentral. Whittlesey covers Brun_5. One can shrink further to BI_5 ∩ Brun_5 (Section 4.4). |
| 2 | Moody, Thm 2.3 / Cor 2.4 (one direction) | transfers | Pure linear algebra: a kernel element fixes every matrix coefficient <Y, rho(g)X>. The converse (Moody's equivalence, Thm 2.2) transfers only as read-model's Prop A/B for curves against cap systems. |
| 3 | Obs 2.1, stabilization | transfers | W(6,0)|B_5 = W(5,1), so Phi ∈ ker W(5,1) iff f(Phi) ∈ ker W(6,0) projectively. The new point is the sixth Weierstrass point p6, and pushes of p6 already lie in Stab(p6) = B_5/Z. So stabilization adds geometry (genus two) but no new group elements. Alternative: W(6,2)|B_5 = W(5,1) + W(5,3), which requires intersecting with ker Burau_5 via Long. |
| 4 | Lemma 3.1 / Cor 3.2, winding | needs new lemma (NL1) | Two-point winding lemma with the parked point, below. |
| 5 | Parity condition and Lemma 4.2 | **fails as a method** | Two-point parity is equivalent to coherence at q = -1 (Section 4.1), and the shadow there kills BI_5 (Section 4.2). |
| 6 | Proper products, Prop 5.1, minimal position | needs new lemma (NL2) | Tight position for product surfaces in C_2(D_5). Moot after step 5. |
| 7 | Lemmas 6.1 and 6.3, one nested violator type | fails | Already for one factor in D_5 there are three non-nested violator types: disks with exactly two of p3, p4, p5 (BBB's own end-of-6.3 remark). W(5,1) adds the sector condition NL3. |
| 8 | Lemmas 6.4-6.6, repair by one push | fails | At least two pushes are needed, and parity of the product of pushes is not controlled (BBB's remark). |
| 9 | Prop 6.7 / Cor 6.8, unequal counts | **fails necessarily** | Corollary 2 at q = -1 on BI_5, and every kernel candidate lies in BI_5. |
| 10 | Thm 6.9, conjugation in a free group | transfers (formally) | K_5 ≅ F_4, and I_2 is free (Mess). Moot. |

### New lemmas needed, stated in the smallest case

**NL1 (two-point winding lemma; n = 5, two caps plus a free point) [BOARD-level, routine].**
- Setting: X_1, X_2 and Y_1, Y_2 are pairs of disjoint simple arcs, and (x,y) ∈ (X_1 ∩ Y_{s1}) × (X_2 ∩ Y_{s2}).
- Suppose x, x' are consecutive along X_1, y is fixed, and D is the disk bounded by the X_1-subarc and the Y_{s1}-subarc between x and x'. Then:
  - a(x',y) - a(x,y) = ±|P(D) ∩ {p1..p5}|;
  - b(x',y) - b(x,y) = ±2·[y ∈ D], with the same sign.
- So the exponent jump on the line is ±(|P(D)| - 2[y ∈ D]). Crossing between the two sectors s ∈ S_2 contributes the half-exchange.
- This follows from the board's anchored formulas, a = a_m + sum wind_p(L_x) + sum wind_p(L_y) and b = b_m + 2 wind(L_y around x_m) + 2 wind(L_x around y). I did not re-derive them.
- Unresolved, as read-model §1.2 also notes: whether simple-arc product squares realize the form on W(5,1) rather than on LKB_5, with the right scalars.

**NL2 (tight position) [open].** We need a notion of tight position for product surfaces in C_2(D_5) such that the number of intersection pairs is a lower bound over the isotopy class. The candidate is a product of factor arcs that are pairwise minimal. I do not know whether it is minimal. The board's mixed-sign extrema (U5-MOM) occur in non-tight representatives.

**NL3 (sector coherence) [EL].** At t = 1 the two sectors give the two products of a 2x2 determinant. Coherence across sectors means |det| = n11 n22 + n12 n21 for the counts n_ij = #(X_i ∩ Y_j), which is no cancellation in the determinant.

---

## 4. The obstruction for W(5,1), and where a kernel element must live

### 4.1 Two-point parity is coherence at q = -1 [EL, from the BOARD formula]

On the Jones line each pair contributes eps(x,y) (-1)^b q^{a-b}, so its value at q = -1 is eps(x,y)(-1)^a. Define **two-point parity** as: eps(x,y)(-1)^{a(x,y)} is the same for all pairs. By the argument of Section 1.1 it is equivalent to "no cancellation, with |P(-1)| = number of pairs".

In terms of moves:
- moving x across D flips the sign by the planar rule and changes a by ±|P(D) ∩ {p1..p5}|;
- the parked point y changes b by an even number and drops out.

So two-point parity is BBB parity for each factor in D_5, with the parked point ignored, plus NL3. The parked-point weights q^{-2w} are exactly what separates W(5,1) from Λ^2(Burau_5), and they equal 1 at q = -1, so parity cannot see them.

Concretely, P(-1) = Phi(-1, 1) = -det[<Y_j, X_i> at t = -1], using read-model §1.3, Phi(q,1) = q^-1 det. This is a Λ^2 H_1(Sigma_{2,1}) pairing in the double cover.

### 4.2 The q = -1 shadow of W(5,1) kills BI_5 [CHK + PUB]

- **[CHK] (w51_shadow_check.py).** At A = e^{i pi/4} (A^4 = -1, delta = 0), T_c^2 = (s1 s2)^6 acts on W(5,1) as A^-12·I, with deviation 2e-15. T_c and s1 are not scalar there.
- **Algebraic reason.** The identity T_c = A^-6(1 + (A^12 - 1)P_c) [CHK, read-model] gives T_c^2 = A^-12(1 + (A^24 - 1)P_c), and A^24 = 1. Also lambda_3 - lambda_1 = -4 ≠ 0 there, so P_c is regular.
- **Generation.** BI_5 is normally generated by the T_c^2, with c a 3|3 curve, together with Delta^4 [BMP].
- So W(5,1) at A^4 = -1 is projectively trivial on BI_5. This agrees with Kasahara: the genus-two image is trivial on I_2 at t_Kas = ±1 [READ via read-status].
- This conclusion does not depend on the sign convention: if the parity point were A^4 = +1 instead, the representation factors through S_5, with kernel P_5 ⊃ BI_5.

### 4.3 Theorem (obstruction) [EL]

Let psi ∈ BI_5, Gamma ∈ B_5 (or Mod(S_{0,6})), and any product test surfaces. If the configurations for psi·Gamma and for Gamma both satisfy two-point parity, they have the same number of intersection pairs.

Hence no step of the form "both coherent and different counts" certifies psi ∉ ker W(5,1). Every noncentral normal subgroup N meets BI_5 nontrivially (Long). So the BBB method cannot prove W(5,1) faithful on any N, in particular not on Brun_5, K_5 or I_2.

### 4.4 Where a kernel element would have to live

**(a) In the group.**
- Kasahara Thm 5.1 gives Ker rho = <iota> × (Ker rho ∩ I_2). So a W(5,1) kernel element maps into I_2: it lies in BI_5, up to the index-two coset mapping to -1 in Sp(4,Z). A nontrivial kernel meets BI_5 nontrivially, since B_5 is torsion-free.
- Kasahara Cor. 1.2 (ker tau_2 = F_2) gives Ker rho ∩ I_2 ⊂ F_2 = ker tau_2. This is the third Johnson subgroup M_2(3). In fact it is ⊂ ∩_k F_k, with equality (Kasahara).
- By Long, the kernel also meets BI_5 ∩ N nontrivially for every noncentral normal N.
- The simplest elements of BI_5 ∩ Brun_5 are [T_c^2, Psi], with c a 3|3 curve and Psi Brunnian. These usually have tau_2 ≠ 0. The filtration satisfies [F_i, F_j] ⊂ F_{i+j}, so commutators of two such elements lie in F_2.
- I_2 is free and F_k ⊇ gamma_k I_2. So a kernel element is nontrivial in a free group, lies in every F_k, and lies outside gamma_N for some N: deep in Kasahara's filtration but of finite lower-central depth.

**(b) In BBB's picture.**
- Take psi ∈ BI_5 ∩ Brun_5 and a test pair that is disjoint for the identity, so its pairing is 0.
- The test object moved by psi has pseudo-Anosov-many intersection pairs, but its double-cover signs must sum to 0. So parity violators must occur, and the blocks they cut out must cancel exactly at q = -1.
- Any push Gamma that repairs coherence for psi·Gamma yields a count equal to |P_Gamma(-1)|, which is at most the count for Gamma. So the repair never produces a discrepancy with a coherent Gamma.
- Everything that could distinguish psi from 1 lies in the cancelling, parity-violating part of the sum: the part BBB's method throws away.

**(c) Moments.**
- Under parity, P(-e^h) = c·sum_x e^{h e_x}, the moment generating function of the exponents. This expansion is Kasahara's, around q = -1.
- If psi ∈ F_k, then every comparison of coherent configurations, psi·Gamma against Gamma, has equal moments of order < k. Order 0 is the BBB count, and order 1 is tau_2.
- A kernel element preserves every moment of every coherent configuration.

### 4.5 General no-go for sign laws [EL]

Suppose a no-cancellation lemma has the form "sign of each term = const·chi(exponent)" with chi a character of Z.
- If chi takes values in {±1}, this is coherence at q = chi(1) = ±1, and the L1 norm is |P(±1)|.
  - At q = 1 the representation factors through S_5, so the kernel contains P_5.
  - At q = -1 it factors through Sp(4,Z), so the kernel contains BI_5.
- If chi takes values in roots of unity zeta, the L1 norm is |P(zeta)|. For zeta ≠ ±1 the eigenvalue ratio -A^-4 of s_i is a root of unity, so s_i^N is projectively scalar and the kernel contains <<s_1^N>>.

In every case the kernel is noncentral, so Long's lemma makes it meet every noncentral normal subgroup. Any argument whose only cancellation control is such a law is therefore blind on part of every normal subgroup. The same holds for Burau_n with n ≥ 4.

For Burau_3 the t = -1 kernel is <Delta^4>, which is central. That is exactly why parity works at n = 3 and cannot work at n ≥ 4.

---

## 5. What a working argument would need (beyond BBB)

1. **Non-specializing cancellation control.** Sign coherence of the extremal monomials only, as in Bigelow's Lawrence-Krammer proof (lexicographic leading term). For W(5,1) this is read-model's Conjecture LT. It compares leading terms instead of values at a point, so it is not blind to Torelli.
   - Strength: it implies W(5,1) faithful, hence Burau_4.
   - Known difficulty: on the Jones line q^a t^b collapses, and mixed-sign extrema occur in non-tight position (board U5-MOM).
2. **One-sided BBB [EL].** Suppose parity holds on one side only. For psi ∈ BI, the coherent side's count is |P_other(-1)|, and |P_other(-1)| ≤ L1(P_other) ≤ count(other). So the comparison can only succeed if the coherent side is the smaller one and the other side's L1 norm is bounded below despite cancellation. That is the original cancellation problem, so nothing is gained.
3. **Order by order.** Faithfulness on I_2 is equivalent to ∩_k F_k = 1. Since I_2 is free and F_k ⊇ gamma_k, it would suffice that the h-expansion is "Magnus-faithful", meaning F_k ⊂ gamma_{f(k)} with f(k) → ∞. This is a separate route (zrho lane, Kasahara Problem 6.2).

BBB's architecture therefore contributes the reductions (steps 1-4 and 10) and nothing to the core.

---

## 6. Strength and novelty bookkeeping

- **Strength.** W(5,1) faithful is equivalent to Jones genus two faithful mod iota (read-status 1.3, read-model 3.1). It implies Burau_4 faithful: W(5,1)|B_4 = W(4,0) + W(4,2) = (Burau_3 pulled back) + Burau_4, then Long's lemma (Kasahara Rem. 5.6).
- **Novelty.**
  - The Shadow Lemma is two lines from BBB's own Lemma 3.1.
  - That Burau at t = -1 is the symplectic representation is classical, and its kernel BI_n is BMP 2015.
  - The observation that BBB's comparison is a t = -1 computation, and hence blind on Brun_4 ∩ BI_4, does not appear in BBB, which never mentions t = -1. I did not find it anywhere else. Treat it as new until a referee or the authors say otherwise.
- **Not checked.**
  - I could not see BBB's figures, and I did not determine which of Lemma 6.3, Prop 6.7 or Thm 6.9 fails on Phi0.
  - NL1's normalization is unchecked.
  - "Shadow = Λ^2_0 H_1(Sigma_2)" is used only through the T_c^2 check and BMP generation.

## 7. Files

- `t_minus1_check.py`: unreduced Burau_4 in exact arithmetic. Output:
  `T=(s1 s2)^6 identity at t=-1: True (t=2, 3/2: False); Psi: False at all; Phi0=[T,Psi]: True at t=-1, False at t=2 and 3/2.`
- `w51_shadow_check.py`: W(5,1) at A = e^{i pi/4}. Output: `T_c^2 - A^-12 I: max dev 2e-15; T_c - A^-6 I: 2.0; s1 - A I: 1.0.`

**Sources.**
- BBB arXiv:2607.05283 v2 (HTML; definitions in §§3-4, Prop 6.7, Cor 6.8, Thm 6.9, §7) [READ].
- Brendle-Margalit-Putman, Invent. Math. 200 (2015) [READ: title and abstract].
- Brendle-Childers-Margalit, cohomology of the hyperelliptic Torelli group [ABS].
- Kasahara AGT 2001 and ASPM 52 (2008), via read-status and read-bbb.
- Long 1986; Mess 1992 [MEM].
