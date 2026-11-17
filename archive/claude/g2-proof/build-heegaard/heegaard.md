# Heegaard / handlebody angle on T for 3-bridge links

Lane: g2-proof / build-heegaard, 2026-11-03.
Check script (single identities and normalisations only, no sweeps): `w60_heegaard_check.py`, output `w60_heegaard_check.out`, both in this folder.

Tags: [PROVED] proof given here. [STD] standard result, cited from memory unless marked "read". [SKETCH] argument outlined from standard inputs. [CHK] verified by the script. [CONJ] conjecture. [READ-x] taken from the read-x lane report.

Notation. W = W(6,0), basis = the 5 noncrossing perfect matchings of 6 points, e_i joins i,i+1, sigma_i -> A + A^{-1} e_i. B(x,y) = sum x_m y_n delta^{loops(m,n)} is the bilinear diagram form, delta = -A^2 - A^{-2}, <empty> = 1, <O> = delta. c = (12)(34)(56) is the cup (handlebody) vector Z_H. For beta in B_6, <plat beta> = B(c, rho(beta) c), and V_L(t) = (-A^3)^{-w} <D> / delta at A = t^{-1/4}, so V(U_k) = delta^{k-1}. "x ≐ y" means equality up to a unit, ±A^n for brackets and ±t^{m/2} for V. H = Hilden subgroup of B_6, H-bar its image in Mod(S_{0,6}) = Mod(S_2)/<iota> (Birman-Hilden), which is the genus-two handlebody group H_2 mod iota. F = "Jones's genus-two representation is projectively faithful on Mod(S_{0,6})", which is equivalent to W(5,1) faithful mod centre [READ-status] and implies Burau_4 faithful.

---

## 0. Answers in one screen

**(1) Unlink equality: TRUE, proved (Theorem A).** If a 3-bridge link L = plat(beta) has V_L ≐ V(U_3), then rho(beta)c = ±A^n c in W over Z[A^{±1}], hence also at every unitary level (in the TQFT quotient when r = 3, 4). Normalisations are benign: W(6,0) needs no quotient and carries a definite invariant Hermitian form for every t = e^{iφ} with |φ| < π/2, which contains all t = e^{±2πi/r}, r >= 5. This is the equality case of Jones's own positivity argument (plat analogue of Jones 1987 Cor 14.5). It is restatement-level, not new.

**(2) Stabilizer.** By Theorem A, Stab_{B_6}[c] = {beta : V(plat beta) ≐ V(U_3)} exactly. So "Stab[c] = H" is equivalent to **U: the Jones polynomial detects the 3-component unlink among 3-bridge links** (using that the 3-bridge sphere of U_3 is unique). U is not in the literature as far as I can find. It is **at least faithfulness-strength**: U => F (the normal core of the handlebody group is trivial), and U => the hard half of the model lane's KL(3|C) (rank-one twists). It is a priori **strictly stronger** than F: F says core(Stab[c]) = 1, U says Stab[c] = H. It is not Thistlethwaite's theorem (3-bridge links need not be alternating). For links in general the analogue is FALSE (Thistlethwaite 2001, Eliahou-Kauffman-Thistlethwaite 2003), but the known 3-component examples do not appear to be 3-bridge.

**(3) Unknot gap: no positivity mechanism can reach the unknot**, for three precise reasons (Section 4): (i) for any unitary realisation of beta -> <plat beta>, equality in Cauchy-Schwarz occurs only where |<plat beta>| = delta^3, the unlink value, and the unknot value delta is strictly smaller; (ii) a deficit invariant b - #components is additive under every construction whose Jones polynomial is determined by V_K, and Cauchy-Schwarz bites only at deficit 0, while a knot in 3-bridge position has deficit 2; (iii) band moves and a second handlebody vector are one mechanism, and it needs the Jones polynomial of a band-moved link, which V_K does not determine. **Best mechanism: use the spin-3/2 line for orthogonality, not for Cauchy-Schwarz.** This gives the Haken-curve lemma HC (Section 4.6): T_3 => HC, and HC + U (or HC + KL) => T_3. HC is T_3 restated as "V_K = 1 forces the genus-2 splitting of Sigma_2(K) to be reducible". It has no positivity proof.

| Statement | Status | Strength |
|---|---|---|
| Theorem A (unlink equality => rho(beta)c ≐ c) | PROVED | restatement of Jones's positivity |
| Stab[c] = {V ≐ V(U_3)} | PROVED | same |
| U (V detects U_3 among 3-bridge links) <=> Stab[c] = H | equivalence PROVED mod uniqueness of U_3's bridge sphere [STD] | U is OPEN |
| U => F => W(5,1) faithful => Burau_4 faithful | SKETCH (standard inputs) | U is at least faithfulness-strength |
| U => KL(3|C) hard half | PROVED mod the twist-extension criterion [STD] | links this lane to read-model |
| T_3 => F (plat chain) | SKETCH (Hempel distance) | T_3 is at least faithfulness-strength |
| T_3 => HC; HC + U => T_3; HC + KL => T_3 | PROVED mod Otal/Waldhausen [STD] | HC is T_3 restated |
| No-go theorems for positivity on the unknot | PROVED | rules out the four proposed mechanisms as positivity arguments |

---

## 1. Setup and normalisations

### 1.1 Plats, Hilden group, Birman-Hilden
- plat(beta) is the closure of beta in B_6 by 3 caps on top and 3 cups below; <plat beta> = B(c, rho(beta)c).
- The Hilden subgroup H is the set of braids whose action on the 6-punctured disk extends over the lower 3-ball preserving the trivial 3-tangle T_c. Two plats with braids in the same double coset H beta H are the same link with the same bridge sphere [STD: Birman 1976].
- Under Birman-Hilden, Mod(S_{0,6}) = Mod(S_2)/<iota>, H-bar = H_2/<iota>, and plat(beta) lifts to the genus-2 Heegaard splitting Sigma_2(plat beta) = V ∪_{φ_beta} V. The double coset H beta H corresponds to H_2 φ H_2. The identity coset gives U_3 and #_2 S^1xS^2; the coset H sigma_2 sigma_4 H gives the unknot and S^3 [STD: Birman-Hilden 1975, Birman-Gonzalez-Acuna-Montesinos 1976].
- [CHK] Hilden elements act on c by scalars: sigma_1 -> -A^{-3}; cap swap sigma_2 sigma_1 sigma_3 sigma_2 -> 1; strand around a cap sigma_2 sigma_1^2 sigma_2 -> 1; half twist Delta -> -A^{-9}; twist (sigma_1 sigma_2)^3 about the reducing curve ∂{1,2,3} -> A^{-6} (this matches the model lane's T_c = A^{-6}(1 + (A^12 - 1)P_c) on c ⊥ v_c). The twist about s_1 = sigma_2(∂{3,4,5}), a 3|3 curve meeting every cap, does NOT fix [c].

### 1.2 Positivity facts for W(6,0)
- (P1) Gram determinant [CHK, numerically at 6 values]: det G(delta) = delta^4 (delta^2 - 1)^4 (delta^3 - 2 delta) = [2]^4 [3]^4 [4], with [2] = delta, [3] = delta^2 - 1, [4] = delta^3 - 2delta. This is the m = 3 case of the Di Francesco-Golinelli-Guitter meander determinant. Its zeros are delta in {0, ±1, ±√2}.
- (P2) Sign symmetry [CHK]: loops(m,n) ≡ 3 + a_m + a_n mod 2 with a_m = loops(c,m) - 3. Hence G(-delta) = -D G(delta) D with D = diag((-1)^{a_m}).
- (P3) Definite region: G is positive definite for delta > √2 (no zero of det on (√2, ∞), and definite for large delta). By (P2) it is negative definite for delta < -√2. Write t = e^{iφ}. Then |delta| = 2|cos(φ/2)|, so **W(6,0) is definite exactly on the open arc |φ| < π/2 (mod 2π)** [CHK: eigenvalues at delta = 1.45 all positive, at 1.40 one negative].
- (P4) Unitarity: for |A| = 1 the Hermitian form h(x,y) = B(x̄, y) (bar: A -> A^{-1} coefficientwise) is rho-invariant. Indeed e_i is B-symmetric with a real matrix, so rho(sigma_i)* = A^{-1} + A e_i = rho(sigma_i)^{-1} [CHK at two values of A].
- (P5) Roots of unity and the TQFT quotient, t = e^{±2πi/r}:
  - r >= 5: inside the arc. W(6,0) is nondegenerate and definite, the TQFT space is all of W(6,0), and there are **no negligible vectors**. The dimension 5 equals the number of Dyck paths of length 6 with height <= r-2.
  - r = 4 (|delta| = √2): rank 4 [CHK]. The radical is the line where the spin-3/2 channel dies ([4] = 0). By the model lane's rainbow duality, B(v_s, ·) = Delta_3 · (rainbow coefficient) vanishes, so every v_s lies in this line [READ-model]. The form on W(6,0) is positive semidefinite with this 1-dimensional radical, and the 4-dimensional quotient carries a positive definite form.
  - r = 3 (|delta| = 1): G is the all-ones matrix up to signs, rank 1 [CHK]. The quotient is spanned by c̄, so the information is vacuous (V(e^{2πi/3}) identities).
  - r = 2 (delta = 0): c itself is negligible.
- (P6) Image of Z_H: c̄ ≠ 0 for r >= 3, with h(c,c) = delta^3 = <U_3>. Since c is real, h(c, rho(beta)c) = B(c, rho(beta)c) = <plat beta>.
- (P7) Phase of A. Replacing A by iA flips the sign of delta (and of t^{1/2}); by (P2) the form stays definite. Only the arc condition on t matters. Galois conjugates t = e^{2πik/r} with |2πk/r| > π/2 give indefinite forms, for example signature (1,4). This is consistent with Funar's PU(1,4) at a 10th root of unity [READ-status], presumably the conjugate k = 3 (argument 108°). The argument below never uses those points.

---

## 2. Task 1: the unlink equality theorem

**Theorem A** [PROVED]. Let beta be in B_6 and L = plat(beta). The following are equivalent.
- (i) V_L ≐ V(U_3) (up to ±t^{m/2}).
- (ii) |<plat beta>(A)| = |delta(A)|^3 for all A in some subset of {|A| = 1, |arg t| < π/2} with an accumulation point; for example at t = e^{2πi/r} for infinitely many r >= 5.
- (iii) rho(beta)c = ±A^n c in W(6,0) over Z[A^{±1}].

Moreover (i) implies rho_r(beta) c̄ ∥ c̄ in the TQFT quotient at every unitary level r >= 3.

*Proof.* (i) => (ii): <D> = (-A^3)^w delta V_L ≐ delta^3, so |<D>| = |delta|^3 on |A| = 1.

(ii) => (iii): at each such A, h is definite (P3) and rho unitary (P4). So |h(c, rho(beta)c)| <= h(c,c)^{1/2} h(rho(beta)c, rho(beta)c)^{1/2} = |delta|^3, with equality iff rho(beta)c is parallel to c. Because c is a basis vector, parallelism means the four coordinates y_m(A), m ≠ c, of rho(beta)c vanish there. These are Laurent polynomials vanishing on a set with an accumulation point, so they vanish identically. Hence rho(beta)c = y_c(A) c. Applying the same to rho(beta^{-1}) rho(beta) c = c shows y_c^{-1} is also a coordinate of an integral vector, so y_c is a unit ±A^n.

(iii) => (i): <plat beta> = ±A^n delta^3. For the last claim, the bracket is a polynomial identity, and Cauchy-Schwarz holds in the semidefinite quotient for r = 3, 4, where c̄ ≠ 0 by (P6). ∎

Remarks.
- **What is new: nothing of substance.** This is the equality case of Jones's positivity (Jones 1987: Cor 14.5 for closed braids, Section 15 for plats and bridge number [READ-status]). The inequality form, for a 3-bridge L, is |V_L(t)| <= |t^{1/2} + t^{-1/2}|^2 = 2 + 2cos φ for |φ| < π/2.
- **General b (used in Section 4).** By the meander determinant, W(2b,0) is definite for |delta| > 2cos(π/(b+1)), that is |φ| < 2π/(b+1). There, a plat presentation with b bridges gives |V_L(t)| <= |delta|^{b-1}. If L has k components and V_L ≐ V(U_k), then |V_L| = |delta|^{k-1}, which is strictly less than the bound when k < b. So Cauchy-Schwarz gives information exactly when **deficit := b - k = 0**.
- "Generic A" in the task's sense is (iii): an identity in W(6,0) ⊗ Z[A^{±1}].

---

## 3. Task 2: the stabilizer of [Z_H]

### 3.1 Stabilizer = unlink detection
**Proposition B.**
- (a) [PROVED] Stab_{B_6}[c] = {beta : V(plat beta) ≐ V(U_3)}. One inclusion is Theorem A; the converse is (iii) => (i).
- (b) [PROVED mod Lemma B.1] Stab[c] = H iff **U**: every 3-bridge link with V ≐ V(U_3) is U_3.

**Lemma B.1** [STD/SKETCH]. Every 3-bridge presentation of U_3 is Hilden-equivalent to the identity plat. Sketch: the presentation lifts to a genus-2 splitting of #_2 S^1xS^2. Such splittings are standard (Haken's lemma reduces to genus-1 splittings of S^1xS^2, which are unique; Waldhausen). Standard means φ is in H_2, that is beta is in H.

*Proof of (b).* (=>) If V(plat beta) ≐ V(U_3), then beta is in Stab = H and plat(beta) = U_3. (<=) If beta is in Stab, then V(plat beta) ≐ V(U_3), so U gives plat(beta) = U_3, and Lemma B.1 gives beta in H. ∎

### 3.2 U implies faithfulness
**Proposition C** [SKETCH]. U => F.

*Proof.* Let PK = {g in Mod(S_{0,6}) : rho(g) is scalar}. PK is normal and PK ⊂ Stab[c] = H-bar, so PK ⊂ core(H-bar), the intersection of all conjugates. It suffices to show core(H_2) = {1, iota} in Mod(S_2).
- Suppose N ⊂ H_2 is normal and not central. Then N contains a pseudo-Anosov f [STD: Ivanov; Long 1986].
- For any meridian m, f^n(m) is a meridian, and f^n(m) -> λ_f^+ in PML. So λ_f^+ lies in the closure Λ of the disk set.
- Every conjugate g f g^{-1} is also in N, so g λ_f^+ is in Λ for every g. The orbit of λ_f^+ is dense in PML (minimality), so Λ = PML.
- This contradicts Masur 1986 / Kerckhoff 1990: Λ is a proper closed subset of measure zero.
- Hence N is central. ∎

Consequences: U => F => W(5,1) faithful (mod centre) [READ-status] => Burau_4 faithful, which is what BBB claim to prove independently.

*Remark (U versus F)* [SKETCH]. F is equivalent to core(Stab[c]) = 1. An element fixing every line of the orbit rho(Mod)[c] is diagonalisable with the orbit inside a finite union of eigenspaces. If the identity component of the Zariski closure of rho(Mod) acts irreducibly, which is expected, the element is scalar. So:
- F: the **core** of the stabilizer is trivial;
- U: the stabilizer **is** the handlebody group.

No implication F => U is known. A 3-bridge 3-component link L ≠ U_3 with V ≐ V(U_3) would refute U without touching F or T.

### 3.3 U implies the hard half of KL(3|C) (link to the model lane)
**Lemma D.1** [PROVED, sketch level]. For a 3|3 curve s on the boundary of (B_-, T_c), the following are equivalent:
- (a) s bounds a disk meeting T_c in one point (s is *reducing*; write s in Haken(c));
- (b) some shadow system of the tangle T_c has an arc disjoint from s;
- (c) T_s is in H-bar.

Proof:
- (a) => (b): the disk cuts off a ball containing a whole cap. Take its bridge disk there and complete it to a shadow system.
- (b) => (a): collapse the neighbourhood N of the disjoint arc to a point p. In 3D, p is free: pushing a cap around a loop is a Hilden move. After the collapse, s encloses {p, x} with x an endpoint of a second cap. All arcs from p to x are related by point-pushes of p (Birman exact sequence, transitivity on arcs), so all such s lie in one H-orbit, which contains a standard reducing curve.
- (a) <=> (c): (=>) is clear. For (<=), T_s lifts to a map whose square is T_ŝ with ŝ separating. A nonzero power of a twist extends over a handlebody iff the curve bounds a disk [STD: McCullough 1985, Oertel 2002]. An iota-invariant separating disk meets the branch set once, so it descends to a disk bounded by s meeting T_c once.

Normalisation warning for the model lane: the cap-system vector depends only on the tangle (projectively). So KL(3|C) must be read with "some arc of S isotopes off c" in the tangle-invariant form (b), meaning *some* shadow system of the same tangle. For a fixed arc system the right side is not obviously invariant under Hilden moves.

**Proposition D** [PROVED mod Lemma D.1]. U => (B(v_s, c) = 0 => s in Haken(c)). This is the hard half of KL(3|C) in tangle form.

*Proof.* By F6 and the model lane, T_s = A^{-6}(1 + (A^{12} - 1) P_s) with P_s the rank-one projector onto [v_s]. If B(v_s, c) = 0 then T_s c = A^{-6} c, so T_s is in Stab[c] = H-bar, and Lemma D.1 gives s in Haken(c). ∎

The easy half (s in Haken(c) => B(v_s, c) = 0) is diagrammatic: a cap inside s is killed by p_3. So under U, Stab[c] already contains every rank-one twist that the spin-3/2 structure allows, and U says there are no others outside H.

### 3.4 How T_3 constrains the stabilizer
**Proposition E** [PROVED mod Otal]. T_3 => Stab[c] = (Stab[c] ∩ H^♭)·H, where H^♭ := (sigma_2 sigma_4)^{-1} H (sigma_2 sigma_4) is the Hilden group of the dual cap system.

*Proof.* Let s be in Stab[c]. By (a), plat(s) has 3 components, so the matching of s fixes {12, 34, 56}, and plat(sigma_2 sigma_4 s) is a knot. Its V ≐ V(unknot), and for knots this forces V = 1 exactly (V(1) = 1, V'(1) = 0). T_3 makes it the unknot. Otal 1982 (every bridge presentation of the unknot is standard) gives sigma_2 sigma_4 s in H sigma_2 sigma_4 H, so s is in H^♭ H. ∎

H ∩ H^♭ is the genus-two Goeritz group of S^3 (mod iota) [STD: Akbas 2008, Cho 2008]. So **under T_3, U is equivalent to: Stab[c] ∩ H^♭ = Goeritz group.**

### 3.5 Is any of this known?
- **U itself:** not found. Known special cases:
  - Alternating 3-bridge links: a non-split reduced alternating diagram has span V = crossing number >= 4 for 3 components, against span V(U_3) = 2.
  - Adequate links: same argument.
  - Closed 3-braids, which are 3-bridge: Jones Cor 14.5 + TL_3 faithful (Burau_3) + Birman-Menasco's unlink theorem [STD, recalled].
- **Unlink detection fails in general:** Thistlethwaite 2001 (2-component, 15 crossings); Eliahou-Kauffman-Thistlethwaite, Topology 42 (2003) [read pp. 155-158, 164-166]: for every k >= 2, infinitely many prime k-component links with V = V(U_k).
  - Their links are Hopf-link satellites H(T,U), formed by clasping the numerators of two tangles.
  - The 3-component family is LLL(n) = H(T, -3). On my reading of their conventions (horizontal integer tangles, numerator closure along the loop), the U-part is the closure of a 2-braid with 3 crossings, a trefoil component. Since b(L) >= Σ b(components), that gives b >= 2 + 1 + 1 = 4, so no conflict with U. Check this reading before relying on it.
  - Their general Theorem 3.3 construction also gives Hopf satellites; I did not determine those bridge numbers.
- **Necessary conditions for a counterexample to U** [PROVED]: all three components unknotted, and every 2-component sublink 2-bridge (a bridge sphere restricts to sublinks), hence alternating or U_2. Also non-split, non-alternating, non-adequate, and not a closed 3-braid. This is the cheapest falsification filter for U.
- **TQFT literature:**
  - At a fixed root of unity, rho(sigma_i) has eigenvalue ratio -A^4, a root of unity, so sigma_i^{2r} acts by a scalar. The level-r stabilizer is therefore far larger than H-bar, and only infinitely many levels together (as in Theorem A) can see U.
  - Handlebody-vector results (BHMV; Gilmer-Masbaum integral lattices; Andersen's asymptotic faithfulness) concern the closed-surface TQFT V_r(S_2), whose dimension grows with r. It meets Jones's 5-dimensional representation only at r = 5 (Funar) [READ-status]. I found no stabilizer theorem.
  - A plausible but unchecked asymptotic analogue for the closed-surface TQFT [CONJ]: the intersection over r of Stab_r[Z_r(V)] equals H_2. It would follow from Andersen-type concentration of Z_r(V) on the Lagrangian of flat SU(2) connections extending over V, plus the classical fact that a homeomorphism of ∂V extends iff it preserves ker(π_1 ∂V -> π_1 V) and that free groups are residually SU(2). It would not transfer to the generic-A 5-dimensional representation.

### 3.6 Verdict on (2)
- The stabilizer statement is equivalent to U.
- It is at least as strong as faithfulness (U => F => W(5,1) => Burau_4), and also gives the KL(3|C) hard half.
- It is a priori strictly stronger than F.
- It is not known, not a restatement of Thistlethwaite, and the general-link version is false.
- Its only support is faithfulness-type intuition.

---

## 4. Task 3: the unknot gap

### 4.1 The unknot coset
- plat(sigma_2 sigma_4) is the unknot. Let u := rho(sigma_2 sigma_4)c. Then B(c,u) = A^6 delta and h(u,u) = delta^3 [CHK].
- By Otal 1982 (or Waldhausen for genus-2 splittings of S^3), plat(beta) is the unknot iff beta is in H sigma_2 sigma_4 H.
- The "fidelity" |h(c,x)|^2 / (h(c,c) h(x,x)) of the unknot is delta^{-4}. For the unlink it is 1, and for a general knot it lies in [0,1].

### 4.2 No-go 1: the supremum sits at the identity [PROVED]
Fix t in the definite arc and let f(beta) = <plat beta>. Suppose f(beta) = <x, π(beta) y> for all beta, for **any** unitary representation π of B_6 and any vectors x, y. This covers W(6,0) with another vector, the doubled representation rho ⊗ rho-bar (which realises |f|^2), tensor powers, and induced representations. Then
- ||x|| ||y|| >= |f(1)| = delta^3 > |delta| = |f(unknot)|.

So the unknot is never a Cauchy-Schwarz equality case for the function f, in any realisation. Equality can only happen where |f| reaches its supremum delta^3, which is the unlink stabilizer.

### 4.3 No-go 2: the deficit [PROVED]
For a plat presentation P of a k-component link with b bridges, set def(P) = b - k >= 0.
- By the Section 2 remark, the hypothesis V ≐ V(U_k) yields an equality case iff def(P) = 0.
- Every construction whose Jones polynomial is determined by V_K is deficit-additive:
  - split union with a fixed presented link: b and k both add;
  - connected sum at a bridge point: b -> b + b' - 1 and k -> k + k' - 1;
  - mirror image;
  - mutation along a Conway sphere meeting the bridge sphere in one circle.
- A knot in 3-bridge position has def = 2, so every such construction stays at def >= 2.
- Hence **positivity can certify only presentations that are already deficit 0**, and for a knot that means 1-bridge, which is already the unknot.
- Constructions that do lower the deficit (band moves, destabilisation, cabling) have Jones polynomials not determined by V_K.

### 4.4 Remark: a single level cannot isolate the unknot [recalled, not re-checked]
- At r = 5 (and generally r >= 5, r ≠ 6, 10), the Freedman-Larsen-Wang density theorem for irreducible summands of the Jones representation applies to W(6,0) and gives dense image in PU(5).
- The knot cosets (preimages of a permutation pattern) have the same closure.
- So the knot values of <plat beta> are dense in the disk of radius delta^3, and the unknot value is an interior point.
- No inequality at one level can single out the unknot; only the full polynomial identity V_K = 1 can.

### 4.5 The four proposed mechanisms
- **(a) Band move and (b) second handlebody vector: one mechanism.** By unitarity, h(rho(gamma)c, rho(beta)c) = <plat(gamma^{-1} beta)>.
  - With gamma = h sigma_2 sigma_4 (h in H): K = plat(beta) is the unknot <=> there is h in H with [rho(beta)c] = [rho(h)u]. Direction <= uses U.
  - That condition is the Cauchy-Schwarz equality case for the pair (rho(h)u, rho(beta)c), that is V(plat(sigma_4^{-1} sigma_2^{-1} h^{-1} beta)) ≐ V(U_3).
  - That link is K after two band moves along bands compatible with the bridge sphere. Its Jones polynomial is not a function of V_K: the skein expansion of the two band crossings brings in three other links.
  - So this mechanism reduces T_3 to a *transfer lemma*: "|<plat beta>| ≐ delta for a knot => [rho(beta)c] is in rho(H)[u]". That is T_3 in vector form, and positivity says nothing about level sets below the maximum.
- **(c) Doubled representation:** realises |f|^2 and is covered by No-go 1. Its plat version (K ⊔ K-bar or K # K-bar in W(12,0)) is covered by No-go 2.
- **(d) Spin-3/2 line as a Cauchy-Schwarz vector:** h(v_s, rho(beta)v_s) and h(v_s, rho(beta)c) are brackets of plats with p_3 inserted along s. These are coloured invariants not determined by V_K. Also v_s is fixed by the stabilizer of the curve s, not by H, so it does not see the Heegaard double coset.

### 4.6 Best mechanism: spin-3/2 orthogonality, i.e. the Haken-curve lemma
The useful property of v_s is not its norm but its **orthogonality**: B(v_s, cap system) = 0 exactly detects reducing curves (Proposition D under U; the easy half always). The unknot's splitting of S^3 is reducible, and this is visible spectrally.

**HC (Haken-curve lemma)** [CONJ]. If K = plat(beta) is a knot with V_K = 1, then some s in Haken(c) has B(v_s, rho(beta)c) = 0.

Equivariance note: B(v_s, x) = 0 is equivalent to P_s x = 0, where P_s is the rank-one part of T_s = A^{-6}(1 + (A^{12} - 1)P_s). Since P_{gs} rho(g) = rho(g) P_s, every statement of the form "P_s x = 0" transports along Mod(S_{0,6}). This is what "by H-equivariance" means below.

**Theorem F.**
- (i) T_3 => HC [PROVED mod Otal]. For beta = sigma_2 sigma_4 and s = ∂{1,2,3}: every term of u = A^2 c + e_2 c + e_4 c + A^{-2} e_2 e_4 c has a cap, (12) or (23), inside s, so B(v_s, u) = 0, and s is in Haken(c). By H-equivariance this holds on the whole coset H sigma_2 sigma_4 H.
- (ii) HC + KL(3|C) => T_3, and in particular HC + U => T_3 [PROVED mod KL]. KL applied to the cap system rho(beta)c shows s is reducing for the second tangle as well. Then s bounds disks D_± meeting K once each, so D_+ ∪ D_- is a decomposing sphere. It splits the presentation as K = K_1 # K_2 with 2-bridge presentations (3 + 1 points on each side). Then V_{K_1} V_{K_2} = 1 forces V_{K_i} = 1, and 2-bridge knots are alternating, so both are unknots.

Strength and honesty:
- HC is T_3 rewritten modulo faithfulness-strength input (KL or U).
- Its content is "V_K = 1 forces the genus-two Heegaard splitting of Sigma_2(K) to be reducible".
- There is no positivity reason for HC. It asks two linear functionals to vanish simultaneously, B(v_s, c) and B(v_s, x), whereas V_K = 1 only fixes B(c, x).
- It is still the right target: it isolates the Heegaard content of the unknot case, and it uses the same rank-one structure (F6) that the curve-criterion lanes already study.

### 4.7 Homology-sphere reformulation [SKETCH]
- V_K = 1 gives det K = |V_K(-1)| = 1, so Sigma_2(K) is a Z-homology sphere of Heegaard genus <= 2.
- By Waldhausen, Sigma_2(K) = S^3 iff K is the unknot. So **T_3 <=> no 3-bridge knot with V = 1 has Sigma_2(K) a homology sphere ≠ S^3.**
- If Sigma_2(K) is Seifert fibred, K is Montesinos (this includes the torus knots that occur) [STD: orbifold theorem, Boileau-Zimmermann]. There V ≠ 1 for nontrivial K [STD: Lickorish-Thistlethwaite 1988].
- The open part of T_3 is therefore 3-bridge knots whose double branched cover is a non-Seifert homology sphere of Heegaard genus 2 (hyperbolic, or toroidal graph manifolds).
- HC says such splittings never arise when V_K = 1.

---

## 5. Strength summary
- Theorem A: proved; restatement of Jones's positivity; implies nothing new.
- U <=> Stab[c] = H: open. U => F => W(5,1) faithful => Burau_4 faithful (BBB), and U => KL(3|C) hard half. A priori strictly stronger than F. The general-link analogue is false (EKT), but no 3-bridge counterexample is known.
- T_3 (T for 3-bridge knots): open, and a new theorem if proved.
  - T_3 => F (plat chain; sketch: a nontrivial projective kernel contains a pseudo-Anosov f whose laminations, after conjugation, avoid the disk-set limit sets. Then plat(sigma_2 sigma_4 f^k) for pure f^k has V = 1 and bridge distance -> ∞ [Hempel 2001; Abrams-Schleimer 2005], so it is a nontrivial knot).
  - T_3 => HC; HC + U => T_3; HC + KL => T_3; T_3 => (U <=> Stab[c] ∩ H^♭ = Goeritz).
- Nothing in this lane proves a new case of T. The positive content is: three no-go theorems that rule out positivity for the unknot, the exact equivalence of the stabilizer question with 3-bridge unlink detection, its implication to F and KL, and the identification of HC (reducibility) as the residual Heegaard statement.

## 6. Cheapest next moves (no sweeps)
1. **Falsify U cheaply:** look for a 3-component link with V = V(U_3), unknotted components and 2-bridge 2-component sublinks (Section 3.5 filter). Start by re-reading the EKT construction (Theorem 3.3 with k = 2 input) for its bridge numbers. One example refutes U, but not F or T.
2. **Fix the KL normalisation** with the model lane: state KL(3|C) for tangles (Lemma D.1(b)), not for fixed arc systems.
3. **Test HC in the toroidal case:** 3-bridge knots with an essential Conway sphere, where Sigma_2 is a genus-2 graph manifold, as the first class beyond Montesinos.

## References (status)
- Jones, Ann. of Math. 126 (1987), Sections 10, 13.19, 14 (Cor 14.5), 15 [READ-status].
- Eliahou, Kauffman, Thistlethwaite, Infinite families of links with trivial Jones polynomial, Topology 42 (2003) 155-169 [read pp. 155-158, 164-166; UIC copy].
- Thistlethwaite, Links with trivial Jones polynomial, JKTR 10 (2001) [MEM].
- Di Francesco, Golinelli, Guitter, meander determinant (1997) [MEM; m = 3 case CHK].
- Birman-Hilden 1973/1975; Birman 1976 (plats, stable equivalence); Birman-Gonzalez-Acuna-Montesinos 1976 [MEM].
- Otal 1982 (bridge presentations of the trivial knot); Waldhausen 1968 (splittings of S^3); Haken's lemma [MEM].
- Masur 1986 (limit set of the handlebody group); Kerckhoff 1990 (measure zero); Ivanov, Long 1986 (pA in normal subgroups) [MEM].
- McCullough 1985, Oertel 2002 (twists extending over handlebodies) [MEM].
- Akbas 2008, Cho 2008 (genus-2 Goeritz group) [MEM].
- Hempel 2001, Abrams-Schleimer 2005 (distance of splittings) [MEM].
- Lickorish-Thistlethwaite, Comment. Math. Helv. 63 (1988) (Montesinos links) [MEM]; Birman-Menasco, closed braids V: the unlink [MEM].
- Freedman-Larsen-Wang 2002 (density) [MEM]; Funar 2021 [READ-status]; Andersen 2006 [READ-status].
