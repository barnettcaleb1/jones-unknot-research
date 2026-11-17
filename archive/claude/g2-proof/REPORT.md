# Genus-two lane: report

3 November 2026. Question: is W(5,1), the 5-dimensional Temperley-Lieb module of B_5 (shape (3,2)), faithful, or equivalently Jones's genus-two representation modulo the hyperelliptic involution iota? Sources: the read-, build- and ref- folders beside this file.

**Bottom line.** Nothing here proves or refutes faithfulness. Three things changed. The 2026 proof that Burau_4 is faithful (Bharathram-Birman-Brendle, "BBB") has a gap exactly where kernel elements would live, so the bottom rung is open again. Spin-3/2 lines are never orthogonal, so a W(5,1) kernel, if one exists, is a coincidence of two such lines deep in the Torelli group. And the stabilizer of the handlebody vector is the question whether V detects the 3-component unlink U_3 among 3-bridge links.

## 1. What the lane established

**TRUSTED** (each survived its referee)

1. *The ladder is published.* Ito 2015 needs a kernel of the full TL representation, and Long's Lemma 2.1 (1986) reduces that to each summand W(n,k), k < n. With Bigelow's Burau_5 kernel, W(5,1) unfaithful implies T false. W(5,1) faithful is equivalent to genus-two faithful mod iota and implies Burau_4 faithful (Kasahara 2008, arXiv:0803.0304, Cor 4.1, Thm 5.1, Rem 5.6). So F1 to F5 restate published results (F4 Kasahara 2001, F5 Jones 1987 Note 13.19); rho(iota) = I.
2. *F6, first half.* T_c acts as a scalar times 1 + kappa P_c, and faithfulness is equivalent to injectivity of c -> [v_c].
3. *Location.* Kernel elements lie in Torelli (in B_5, in BI_5 or Delta^2 BI_5) and in every term F_k of Kasahara's filtration.
4. *Shadow Lemma* (restatement of Bigelow's winding lemma). BBB's parity condition holds exactly when |M(-1)| equals the number of intersection points, so their count is the Burau pairing at t = -1.
5. *Theorem A* (kernel lane, new). For 3|3 curves c, c' (three points on each side), r(c,c') = |H(v_c,v_c')|^2/Delta_3^2 equals (2D-1)^2 at A = e^{i pi/4}, with D an integer determinant of homology classes. So H(v_c,v_c') never vanishes. Only curve-against-cap pairings can vanish, and at that root of unity they vanish exactly on homologically reducing curves (Prop D, new).
6. *Theorem B and the certificate* (reformulations). The kernel is nontrivial iff some Torelli f moves c_0 and fixes the line [v_{c_0}]; then [T_{c_0}^2, f] is in the kernel. One Laurent identity, R_f(A)R_f(1/A) = Delta_2^2, decides a candidate.
7. *Heegaard lane.* rho(beta)c is a unit multiple of the cup vector c iff V(plat beta) equals V(U_3) up to a unit (restatement-level; Jones 1987 Prop 15.6). Not found in the literature: Stab[c] equals the Hilden group iff U holds (V detects U_3 among 3-bridge links); U implies faithfulness; U implies the hard half of KL(3|C); T for 3-bridge knots (T_3) implies faithfulness (sketch).

**DAMAGED** (with the repair)

8. *"Burau_4 is faithful (BBB)".* Their Cor 6.8 compares two t = -1 values, so it cannot separate any element of BI_4 from 1, and every Burau_4 kernel element lies in BI_4. Brun_4 ∩ BI_4 contains Phi0 = [(s1 s2)^6, [[y1,y2],y3]], the identity at t = -1 and not at t = 2. If their other lemmas hold, the failure is the "Furthermore" clause of Prop 6.7. Repair: Burau_4 is open, and W(5,1) faithfulness implies it. No published critique exists; ask the authors before relying on this. Sharpened in BBB-GAP.md: an explicit conjugate of Phi0 meets every hypothesis of Prop 6.7 and Cor 6.8, the Thm 6.9 reduction is repairable, so the failure lies in Prop 6.7, Prop 5.1 or the proper-product criterion for Gamma_1.
9. *Transfer lane, "BBB's method is dead".* With parity on both sides nothing cancels, so the exponent multiset survives, and comparing m exponents is blind only on F_{m+1}. Repair: the obstruction is graded, and BBB's architecture keeps an open crux (compare multisets or spans).
10. *Kernel lane, the form [(s1 s2)^3, f].* Its lift is a half-twist, which shifts every depth claim by one. Repair: use [(s1 s2)^6, f] = T_gamma T_{f gamma}^{-1}, which lies in [I_2, I_2], and in F_3 iff m(f) is a rational multiple of u_0 (a tau_2 condition).
11. *Forms.* The invariant form is the Hermitian H(x,y) = B(xbar,y); use H wherever the Heegaard lane used B. Nothing breaks. KL(3|C) must be stated for tangles, and "KL implies faithful" rests on Lemma C, which is a sketch.

**DEAD**

12. F6 as a source of kernel elements: no orthogonal pair exists.
13. A BBB-type step "parity on both sides, counts differ" for W(5,1): blind on BI_5.
14. "The extreme degree of H(v_c,v_c') is controlled by i(c,c')": the degree grows linearly, the intersection exponentially.
15. Kernel candidates built from one twist, seeds [T_c^a, T_d^b], or single commutators of separating twists with distinct splittings.
16. One-sided BBB, and "Kasahara depth at most C|f|" as a target: both restate faithfulness.
17. Cauchy-Schwarz equality as a route to the unknot: it occurs only at the unlink value.

## 2. Strongest open target

**Twisted-unlink rigidity** (the hard half of KL(3|C), stated for tangles). Put U_3 in standard 3-bridge position and let c be a 3|3 curve on the bridge sphere. If one full twist along c gives a link whose V equals V(U_3) up to a unit, then c bounds a disk meeting the link once, and the twisted link is U_3. In the module: H(v_c, S) = 0 forces c to be reducing for S. Equal V forces determinant 0, so only homologically reducing curves are at stake, and there the q = -1 shadow says nothing.

*Strength.* It implies genus-two faithfulness (read-model Thm D, given Lemma C for tangles), hence W(5,1) and Burau_4 faithful, so a proof would contain a proof for Burau_4. With the Heegaard lane's Haken-curve lemma (V_K = 1 forces the genus-two splitting of the double branched cover to be reducible) it gives T_3. U implies it.

*Why it should hold.* The four analyses meet here: a kernel is four such zeros at one homologically reducing curve, every q = -1 argument is blind there, and U forces the statement. A failure is a 3-bridge link other than U_3 with the polynomial of U_3, shared by all its k-fold twists; the known 3-component examples (Eliahou-Kauffman-Thistlethwaite) are not 3-bridge, and U holds for alternating, adequate and closed 3-braid links. Against: Burau_5 has its kernel inside BI_5, where its t = -1 shadow is blind.

*Next step.* Prove Lemma C for tangles: for distinct 3|3 curves c, c' with the same splitting, some trivial 3-tangle has c reducing and c' not. A twist along a 2|4 curve disjoint from c and meeting c', with Masur's limit set, looks sufficient (unchecked). In parallel, settle the floor: confirm the BBB gap and try the multiset form of their Prop 6.7.

## 3. Kernel side

A counterexample to T through this rung needs a nontrivial kernel element of W(5,1), and then one of the form [T_{c_0}^2, f], with f in Torelli moving a 3|3 curve c_0 to another curve of the same homology splitting while fixing [v_{c_0}]. It lies in every F_k, so every finite truncation and every q = -1 statistic misses it. f must meet the tau_2 condition of item 10, and candidates inside one 4-punctured disk belong to the Burau_4 question. The smallest open class is f in <T_{d1}^2, T_{d2}^2>: a commutator word acting on span(v_{d1}, v_{d2}) as the identity or as a parabolic fixing the projection of v_{c_0}. A certified candidate gives explicit hyperbolic 5-braid knots with V = 1 (Ito, with Bigelow's Burau_5 element and Long) and 3-bridge plats with V = 1 (nontrivial by a Hempel-distance argument quoted from memory).

For a kernel: the shadow is blind there, and Burau_5, one shape over, has its kernel in BI_5. Against: Theorem A removes the only known mechanism for such kernels at generic parameter. Neither is a proof. Kasahara's Problem 6.2 (is Z_rho finite?) is being worked in zrho/. If Burau_4 is unfaithful, T fails one rung lower (Ito Cor 3).


## 4. Peer results from the breakthrough chat (3:50 pm)

- **Independent checks.**
  - Φ0 (112 letters): unreduced Burau is I at t = -1, not I as a Laurent matrix or at t = 2, and its (t+1)-adic depth is exactly 1.
  - Theorem A: |N(zeta_8)| is an odd integer on 3000 random words (93% equal 1).
  - That chat agrees with the BBB gap logic.
  - Scripts live in that session's scratchpad (/private/tmp/claude-501/-Users-calebbarnett/325b8760-550e-4462-b594-d76cd953b342/scratchpad/jones-adv/peer-checks/, may be cleared).
- **Dead: Schottky inequalities in Mess word length.** The bound D(rho(w)) >= 24 sum|e_j| - 16(L-1) fails on an explicit F_4 word, with D(B^4) = 200 < 208. A conjugated letter keeps pair overlap <= 8, so D tracks the pair geometry of the curves actually multiplied. Basis-free versions restate KL.
- **Dead as a method: soft constraints for span N >= 12.** The formal value N = 2A^4 + A^-4 satisfies every Hermitian, integrality and root-of-unity constraint. N is not sign-coherent for 38% of partition-preserving pairs, so extremal states cancel. A proof needs exact extremal-coefficient control or an A-adic argument.
- **Known in substance.**
  - H has signature (4,1) for 1 < delta < sqrt2.
  - Funar (arXiv:2009.05961, section 2.6) puts the genus-two representation in PU(1,4) at A = e^{7 pi i/20}.
  - At transcendental theta the image is dense, so complex hyperbolic geometry gives no discreteness.
  - N(beta)(zeta_16) = zeta_16^{e(beta)}.
- **Open, small.** The half-twist criterion e_d v_c = 0 is the collision L_c = L_{tau_d c} (kernel.md 5.1). For length-2 Torelli words T_V^a T_{k c_V}^b with k in ker(B_4 -> B_3), everything reduces to one scalar identity in Burau_4 data: Phi = kappa_b h_W + kappa_a h_V + kappa_a kappa_b h_W h_VW = 0. A probe of 594 pairs x 64 exponent pairs found no zero.
