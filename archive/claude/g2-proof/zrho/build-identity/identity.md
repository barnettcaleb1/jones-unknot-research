# Mullins-Morita identity on the genus-two Torelli group

Lane: build-identity (zrho). Date: 2026-11-03.
Companion script: `check/sanity.py` (exact rational arithmetic, runs in under a second).

Tags used below:
- [LIT] read in the source by this lane.
- [LIT-2] read in the source today by a sibling lane (read-kasahara, read-casson). Not re-read here.
- [STD] standard background.
- [DER] derived here, with a proof sketch.
- [CHK] verified by `check/sanity.py`.
- [CONV] a convention.

---

## 0. Results at a glance

**Notation.**
- N := Ker rho ∩ I_2.
- d^ : I_2 -> Z is the exponent sum in Mess's basis. So d^(T_c) = 1 for every separating twist, with the twist direction fixed in 1.4.
- L(phi) := V'(-1)/V(-1), where V = V_{K_phi}.
- a_2 is the second Conway coefficient.

**Theorem (Section 5).** For every phi in I_2:

    sigma(K_phi)/8 - L(phi)/12  =  lambda(M_phi)  =  -d^(phi)/10 + q(tau_2(phi))

and therefore

    4 d^(phi) + 5 sigma(K_phi)  =  (10/3) L(phi) + 40 q(tau_2(phi))  =:  G(rho(phi)).      (*)

Here q is the linear functional on tau_2(I_2) ⊗ Q fixed by

    q(tau_2(T_c)) = 1/10 - a_2(K_c),

where K_c is the knot type in S^3 of the separating curve c on the Heegaard surface. Both L and q∘tau_2 are explicit functions of rho(phi): see Section 4 and input (I5).

**The brief's normalisation.** Define d := 24 × (the M_2-invariant part of lambda) = -(12/5) d^. This is -d_1 in Kasahara's convention lambda = -d_1/24 + q. Then (*) reads

    d(phi) = 3 sigma(K_phi) + F(rho(phi)),   with F = -2 L - 24 q∘tau_2.

So the brief's coefficient "3" is right, but only for this d:
- This d takes the non-integral value -12/5 on a separating twist.
- It is not Morita's bounded core, which is 0 on genus-one separating twists of S_{2,1}.
- With the integral generator d^, the coefficient of sigma is -5/4.

**Consequences (Section 6).**
- (a) If kappa is in N, then V_{K_kappa} = 1, sigma(K_kappa) = -(4/5) d^(kappa), and lambda(Sigma_2 K_kappa) = -d^(kappa)/10.
- (b) Z_rho ≅ Z/d^(N). The following are equivalent:
  - Z_rho is finite;
  - some kappa in N has d^(kappa) ≠ 0;
  - some K_kappa with kappa in N, a Jones-trivial 3-bridge knot, has nonzero signature.

  In that case |Z_rho| = (5/4)·min{ |sigma(K_kappa)| > 0 }, a multiple of 10.
- (c) The following are equivalent:
  - Z_rho ≅ Z;
  - d^ factors through rho on I_2;
  - sigma(K_phi) is a function of rho(phi) on I_2;
  - lambda(M_phi) is a function of rho(phi) on I_2.
- (d) T implies Z_rho ≅ Z. This uses neither Ito's theorem nor the normal-intersection lemma.

**Strength.** Everything here is a proof sketch resting on six classical inputs:
- Birman-Hilden;
- Mess;
- Morita's homomorphism theorem and his tau_2 formula;
- Casson's surgery formula;
- Mullins's formula;
- Kasahara's Cor 1.2.

The exact constant -1/10 is derived here from the Seifert form of the Heegaard surface by invariant theory [DER, CHK]. It agrees with read-casson's derivation from Faes-Massuyeau's normalisation of Morita's closed core.

Nothing here decides Kasahara's Problem 6.2. The identity (*) only translates it into a question about the signatures of the knots K_kappa, kappa in N.

---

## 1. The identification M_phi = Sigma_2(K_phi)

**1.1 Birman-Hilden [STD].** S_2 -> S^2 is the double cover branched over P = {p_1, ..., p_6}, with deck involution iota.
- Every mapping class of S_2 has a representative commuting with iota (Birman-Hilden; Haas-Susskind).
- M_2/<iota> ≅ Mod(S^2, P) =: Mod(S_{0,6}), the mapping classes of the sphere that preserve P setwise.
- iota acts by -1 on H_1. So I_2 ∩ <iota> = 1, and I_2 injects into Mod(S_{0,6}).

**1.2 Handlebodies [STD].** Let T = (B^3, three unknotted arcs) be a trivial tangle with endpoint set P.
- Sigma_2(B^3, T) = H is a genus-two handlebody with boundary S_2.
- iota extends over H as the deck transformation.
- An arc in S^2 that cobounds a disk with a strand of T lifts to a meridian of H.

**1.3 Definition.** Attach the strands of T at the pairs {12, 34, 56}.
- Fix f_0 in Homeo(S^2, P) so that the second copy of T is attached at {23, 45, 61}. Then T ∪_{f_0} T is the 3-bridge unknot: the trace 1-6-5-4-3-2-1 is a single component.
- Let iota_0 be a symmetric lift of f_0. Then H ∪_{iota_0} H = Sigma_2(unknot) = S^3, the standard genus-two splitting (Waldhausen).
- For phi in M_2 with image phibar in Mod(S_{0,6}), set

      M_phi := H ∪_{iota_0 phi} H,        K_phi := T ∪_{f_0 phibar} T.

**Lemma 1 [DER, standard].** Sigma_2(K_phi) ≅ M_phi, orientation-preservingly.

*Proof.* Glue two tangles along (S^2, P). The double branched cover of the result is the union of the two covers, glued along a lift of the gluing map. iota_0 phi lifts f_0 phibar. The other lift is iota_0 phi iota, which differs by iota, and iota extends over H. ∎

**Braid description.** Suppose beta in B_6 maps to phibar. Then K_phi is the plat of beta, capped by {12, 34, 56} at the bottom and by {23, 45, 61} at the top.
- Changing beta by the kernel of B_6 -> Mod(S_{0,6}) does not change the link. That kernel is normally generated by Delta^2 and sigma_1...sigma_5 sigma_5...sigma_1.
- K_phi depends only on the double coset of phibar modulo the two Hilden subgroups.

**K_phi is a knot.** For phi in I_2, H_1(M_phi) = 0. So det K_phi = |H_1(Sigma_2 K_phi)| = 1. A link with two or more components has even determinant, so K_phi is a knot.

Conversely, every 3-bridge knot of determinant 1 is K_phi for some phi in I_2 [STD]. The handlebody group surjects onto the stabiliser of its Lagrangian, so any ZHS gluing can be moved into iota_0·I_2. This is not needed below.

**1.4 Twist sign [CONV].** Let c be a separating curve on ∂H.
- Inserting T_c^{±1} into the gluing is ∓1 surgery on c ⊂ S^3 with the surface framing.
- The surface framing equals the Seifert framing, because c bounds a subsurface F_c of the Heegaard surface.
- We orient twists so that M_{T_c^n} = S^3_{-1/n}(c).

All signs below use this convention. The opposite convention flips the sign of d^ relative to sigma, L and lambda, and changes nothing else.

---

## 2. Inputs

**(I1) Mess [LIT-2].**
- I_2 is free on separating twists, one for each splitting of H_1(S_2) into two orthogonal symplectic planes.
- H_1(I_2) = Z[splittings].
- Sp(4,Z) acts transitively on splittings.

**Lemma 2 [DER; the first part is in Kasahara 2001 §6].** Let d^ : I_2 -> Z be the exponent sum in Mess's basis. Then:
- d^(T_c) = 1 for every separating twist;
- d^ is M_2-invariant and spans Hom(I_2, Q)^{M_2};
- Ker d^ = [M_2, I_2];
- Z_rho = rho(I_2)/rho([M_2, I_2]) ≅ I_2/(N·[M_2, I_2]) ≅ Z/d^(N).

*Proof.* I_2/[M_2, I_2] = H_1(I_2)_{M_2} = Z[splittings]_{Sp(4,Z)} = Z, and the isomorphism is d^. ∎

In Morita's closed normalisation d^(T_h) = h(g - h). So d^ is his closed core at g = 2 [LIT-2: Faes-Massuyeau §3.1, citing Morita Thm 5.7].

**(I2) Morita, Topology 30 (1991) [LIT-2, via Massuyeau-Meilhan §7.1].**
- lambda(M_phi), restricted to the Johnson kernel, is a homomorphism.
- It equals an invariant core plus a term that factors through tau_2.
- tau_2 of a separating twist is, up to a fixed nonzero scalar, omega_c ⊗ omega_c. Here omega_c in Λ^2 H is the symplectic class of one side of c.

In genus two:
- K_2 = I_2, because tau_1 lands in Λ^3 H / H = 0.
- For the closed surface, tau_2(I_2) ⊗ Q is the 14-dimensional irreducible [22] (Kasahara's Gamma_{0,2}). In particular it has no Sp-invariant vector.
- tau_2(T_c) is proportional to pi_22(omega_c ⊗ omega_c), which is the same for both sides of c.

**(I3) Casson's surgery formula [STD].**
- lambda(S^3_{1/n}(K)) = n a_2(K), normalised by lambda(Sigma(2,3,5)) = -1.
- For a genus-one Seifert matrix V, a_2 = det V, because ∇ = 1 + (det V) z^2.

Let theta(u, v) = lk(u, v^+) be the Seifert form of the Heegaard surface. Then

    lambda(M_{T_c}) = lambda(S^3_{-1}(K_c)) = -a_2(K_c) = -Λ^2theta(omega_c, omega_c),

where Λ^2theta(x∧y, x'∧y') = theta(x,x') theta(y,y') - theta(x,y') theta(y,x').

**(I4) Mullins, Topology 32 (1993), Thm 5.1 [LIT-2].** This is quoted via Eisermann. read-casson checked the normalisation on T(3,5), T(3,7), T(3,11), T(3,13) and the trefoil. For a knot K with Sigma_2(K) a ZHS:

    lambda(Sigma_2 K) = sigma(K)/8 - V_K'(-1) / (12 V_K(-1)).

Conventions: V(right trefoil) = t + t^3 - t^4 and sigma(right trefoil) = -2.

**(I5) Kasahara 2001, Cor 1.2 [LIT-2].** tau_2 factors through rho. Concretely, in Kasahara's variable put t = -e^h. For phi in I_2:
- rho(phi) = I + h Delta_1(phi) + O(h^2). At t = -1, rho is sgn ⊗ Λ^2H/omega, which is trivial on I_2.
- Delta_1(phi) = -(d rho(phi)/dt)|_{t=-1} is an M_2-equivariant homomorphism with rank-14 image.
- tau_2 = Theta ∘ Delta_1. Kasahara also has Z_{phi(1)} = Z_{tau_2} = Z/10.

read-kasahara's notes indicate that Kasahara's t need not be the Jones-polynomial variable q, since rho(psi_0) is scalar at primitive fifth roots of t. Kasahara's t = -1 does correspond to q = -1. Section 4 is written in the bracket variable A, with q = A^{-4}. It must be transported to Kasahara's variable before machine use.

**(I6) Bracket of a plat [STD].**
- W = W(6,0) over Z[A^{±1}], with basis the 5 crossingless matchings.
- pi_A(sigma_i) = A + A^{-1} e_i.
- Loop pairing: <x, y> = delta^{#loops(xbar ∪ y)}, with delta = -A^2 - A^{-2}.
- Take w_0 = {12, 34, 56} and w_1 = {23, 45, 61}. Then <w_1, pi_A(beta) w_0> = delta·<D_beta> with <O> = 1, and <w_1, w_0> = delta.

Jones's rho is this module, corrected by a scalar unit character so that it descends to Mod(S_{0,6}), then pulled back to M_2 [LIT-2; brief]. Whether Jones's variable is A^{-4} or A^{4} must be fixed once, on the trefoil plat. That choice changes the sign of L inside F and nothing in Section 6.

---

## 3. The exact constant (Proposition 3)

**Proposition 3 [DER, CHK].** On I_2, in convention 1.4:

    lambda(M_phi) = -d^(phi)/10 + q(tau_2(phi)),      q(tau_2(T_c)) = 1/10 - a_2(K_c).

Equivalently, for any word phi = Π T_{c_j}^{e_j} in separating twists, lambda(M_phi) = -Σ_j e_j a_2(K_{c_j}).

*Proof sketch.*

**Step 1.** lambda restricted to I_2 is a homomorphism (I2), and I_2 is generated by separating twists (I1). So by (I3), lambda(M_phi) = -Σ e_j Λ^2theta(omega_{c_j}, omega_{c_j}).

**Step 2 (the standard Seifert form).** Take a symplectic basis a_i, b_i of H_1(Σ), where a_i bounds a disk in H, b_i bounds a disk in the outer handlebody H', and push-offs go into H'. Then:
- theta(a_i, ·) = 0 and theta(·, b_j) = 0;
- theta(b_i, a_j) = ±delta_ij, and the sign is irrelevant below.

Let B be the symmetrisation of Λ^2theta. It is a linear form on

    S^2(Λ^2 H_Q) = [22] ⊕ [11] ⊕ [0] ⊕ [0]      (dimensions 14 + 5 + 1 + 1 = 21).

- *The [11] part is zero.* That summand is {omega·xi}. B(omega, xi) = 0 for every xi, because every term contains a factor theta(a_i, ·) or theta(·, b_i).
- *The invariant part.*
  - The invariant tensors are Omega_1 = omega ⊗ omega and Omega_2 = (Λ^2J)^{-1}.
  - The invariant forms are B_1 = <omega, ·> ⊗ <omega, ·> and B_2 = Λ^2J.
  - The Gram matrix (B_k(Omega_l)) is [[4, 2], [2, 6]].
  - B(Omega_1) = 0 and B(Omega_2) = 1.
  - Solving gives B_inv = -(1/10) B_1 + (1/5) Λ^2J.
- *On a genus-one splitting* omega_c = x∧y, with x·y = 1: B_1 = 1 and Λ^2J(omega_c, omega_c) = 1. So B_inv(omega_c^{⊗2}) = 1/10 for every splitting.

Hence

    a_2(K_c) = B(omega_c^{⊗2}) = 1/10 + B_22(pi_22 omega_c^{⊗2}).

**Step 3.** Therefore

    lambda(M_{T_c}) = -1/10 - B_22(pi_22 omega_c^{⊗2}) = -(1/10) d^(T_c) + q(tau_2(T_c)),

where q := -B_22, transported through tau_2 ∝ pi_22 (I2). Both sides are homomorphisms on I_2, and they agree on generators. ∎

**The coefficient is forced.** tau_2(I_2) ⊗ Q has no invariant vector. So no nonzero multiple of d^ factors through tau_2, and the split lambda = c·d^ + (tau_2-term) is unique.

**Checks [CHK, `check/sanity.py` Part 2].** I ran the same computation in genus 3 and genus 4 with the analogous Seifert form. It gives an invariant part of h(g-h)/(2(2g+1)) on a genus-h splitting. Two things came out that were not put in:
- the combination of h^2 and h is exactly Morita's closed core h(g - h);
- the factor is 1/(2(2g+1)). read-casson derived the same factor from Faes-Massuyeau's formula d^ = -((2g+1)/12) d + ((g-1)/3) d'.

For g ≥ 3 this checks only the invariant part.

A splitting with a_2 = 1: x = a_1 + b_1, y = a_1 + 2b_1 + a_2 + b_2. Here x·y = 1 and the determinant of theta restricted to <x, y> is 1.

**Corollary 3' [DER].** On Ker tau_2 ⊂ I_2, lambda(M_phi) = -d^(phi)/10.
- Casson integrality then gives d^(Ker tau_2) ⊆ 10Z.
- Combined with Kasahara's computer value Z_{tau_2} = Z/10, this says some phi in Ker tau_2 has lambda(M_phi) = ±1.
- read-casson made the same observation.

Values on separating twists:
- q(tau_2 T_{c_0}) = 1/10 for a reducing curve, where K_{c_0} is the unknot.
- q(tau_2 T_c) = -9/10 for a trefoil curve.

---

## 4. The matrix coefficient and the writhe (Lemma 4)

For phi in I_2, choose beta over phibar and set

    r_phi(A) := <w_1, pi_A(beta) w_0> / <w_1, w_0>  =  <D_phi>  =  (-A^3)^{w(D_phi)} V_{K_phi}(A^{-4}).

Suppose rho(phi) = chi(phi)·C pi_A(beta) C^{-1}, with chi a scalar unit. Put w_0' = C w_0 and w_1' = C^{-T} w_1. Then, up to a unit ±A^k,

    r_phi = <w_1', rho(phi) w_0'> / <w_1', w_0'>,

which is a normalised matrix coefficient of rho(phi).

Dividing by <w_1', w_0'> is essential. That pairing equals delta up to a unit, and it vanishes at A = e^{iπ/4}, which is q = -1.

**Lemma 4 [DER].** Put D_r(A) := A r'(A)/r(A). For any unit multiple r = ±A^k V(A^{-4}) of the Jones polynomial of a knot:

    L = V'(-1)/V(-1) = (1/4) [ D_r(e^{iπ/4}) - D_r(1) ].

*Proof.* D_r(A) = k - 4 q V'(q)/V(q), with q = A^{-4}.
- At A = 1 we have q = 1, and V'(1) = 0 for knots, so D_r(1) = k.
- At A = e^{iπ/4} we have q = -1, so D_r = k + 4L. ∎

So every unit cancels. This covers:
- the writhe;
- Jones's scalar correction;
- the choice of lift beta, whose ambiguity acts on W(6,0) by scalars.

By-products:
- For any knot diagram D, w(D) = D_{<D>}(1)/3. Check on the standard right trefoil diagram: <D> = -A^5 - A^{-3} + A^{-7}, so D(1) = 9 and w = 3.
- In the variable q: if P = ±q^j V, then L = D_P(1) - D_P(-1), with D_P = q P'/P.
- V_{K_phi}(-1) = Delta(-1) ≡ 1 mod 4, and det = 1. So V_{K_phi}(-1) = 1 on I_2.

**The explicit function.** For X = rho(phi):

    Lambda(X) := (1/4) [ D_{r_X}(e^{iπ/4}) - D_{r_X}(1) ],   r_X := <w_1', X w_0'> / <w_1', w_0'>,
    G(X)      := (10/3) Lambda(X) + 40 Q(Delta_1),          Delta_1 = -(dX/dt)|_{t=-1},

where Q is the linear functional on Delta_1(I_2) ⊗ Q with Q(Delta_1(T_c)) = 1/10 - a_2(K_c). Q is well defined because q∘tau_2 = Q∘Delta_1, by (I5).

G uses three pieces of data:
- r_X to first order at q = 1;
- r_X to first order at q = -1, which is second order in the raw coefficient, because of delta;
- Delta_1.

So G is not a function of Kasahara's h-adic truncation phi(2) at t = -1 alone. It also needs the first-order data at q = 1.

---

## 5. The identity

**Theorem [DER, from Lemma 1, (I4), Proposition 3, Lemma 4, (I5)].** For every phi in I_2:

    4 d^(phi) + 5 sigma(K_phi)  =  (10/3) L(phi) + 40 q(tau_2(phi))  =  G(rho(phi)).      (*)

*Proof.*
- Lemma 1 and Mullins give lambda(M_phi) = sigma(K_phi)/8 - L(phi)/12.
- Proposition 3 gives lambda(M_phi) = -d^(phi)/10 + q(tau_2 phi).
- Multiply the difference by 40.
- Lemma 4 and (I5) make the right side a function of rho(phi). ∎

**Equivalent forms.**

    d^(phi) = -(5/4) sigma(K_phi) + (5/6) L(phi) + 10 q(tau_2 phi)
    d(phi)  = 3 sigma(K_phi) - 2 L(phi) - 24 q(tau_2 phi),
              where d = -(12/5) d^ = 24·(invariant part of lambda) = -d_1 (Kasahara)

**Meyer form [remark; sign unverified].** Meyer's hyperelliptic function phi_M restricts on I_2 to the invariant homomorphism phi_M(T_c)·d^, with |phi_M(T_c)| = 4/5 (Endo). read-casson quotes -4/5 from secondary sources, and the sign depends on conventions. If phi_M(T_c) = -4/5 in convention 1.4, then on I_2:

    sigma(K_phi) - phi_M(phi) = (2/3) L(phi) + 8 q(tau_2 phi),

and on N, sigma(K_kappa) = phi_M(kappa).

This is the genus-two plat analogue of Gambaudo-Ghys, where the signature defect of closed braids is the Meyer cocycle of Burau at -1. Here Meyer's function takes the place of the cocycle.

---

## 6. Consequences

**(a) Kernel elements [DER].** Let kappa be in N.
- r_kappa is a unit, so V_{K_kappa} = 1, because V(1) = 1 and V'(1) = 0 fix the unit.
- L(kappa) = 0, and tau_2(kappa) = 0 by (I5).

So (*) gives

    sigma(K_kappa) = -(4/5) d^(kappa),        lambda(Sigma_2 K_kappa) = sigma(K_kappa)/8 = -d^(kappa)/10.

In the brief's normalisation this is d(kappa) = 3 sigma(K_kappa).

Integrality:
- lambda in Z forces sigma(K_kappa) in 8Z. Equivalently, det = 1 and Arf = 0, since V(i) = 1.
- Hence d^(kappa) is in 10Z, so 10 divides |Z_rho| whenever it is finite.
- This reproves Kasahara's lower bound, in its divisibility form, from Casson integrality.
- sigma(K_·) restricted to N is a homomorphism N -> 8Z.

**(b) Finiteness [DER].** Write d^(N) = mZ with m ≥ 0. By Lemma 2, Z_rho ≅ Z/m. Then:

    Z_rho finite  <=>  m ≠ 0  <=>  some kappa in N has d^(kappa) ≠ 0  <=>  some kappa in N has sigma(K_kappa) ≠ 0,

and |Z_rho| = m = (5/4)·min{ |sigma(K_kappa)| : kappa in N, sigma(K_kappa) ≠ 0 }, which is a multiple of 10.

If m > 0, take kappa with d^(kappa) = m. Then K_kappa is a knot with:
- V = 1;
- sigma = -4m/5 ≤ -8;
- lambda(Sigma_2 K_kappa) = -m/10 ≠ 0;
- 4-genus and unknotting number at least 2m/5.

So K_kappa is a counterexample to T, certified by its signature (or by Sigma_2 K_kappa ≠ S^3). This needs no distance argument and no Ito construction.

If Kasahara's "order exactly 10" holds, there is a Jones-trivial 3-bridge knot with sigma = -8 and lambda(Sigma_2) = -1.

Kernel elements with d^ = 0, such as hypothetical commutators [T_c, T_c'], give knots with sigma = 0 and lambda(Sigma_2) = 0. (*) says nothing about those.

**(c) Infiniteness [DER].** The following are equivalent:
1. Z_rho ≅ Z;
2. d^ vanishes on N;
3. d^ = f∘rho on I_2 (Kasahara's Prop 6.1);
4. lambda(M_phi) is a function of rho(phi) on I_2;
5. sigma(K_phi) is a function of rho(phi) on I_2.

*Proof of the new equivalence 5.*
- If sigma = s∘rho, then d^ = (G - 5s)∘rho / 4, which kills N.
- If d^ = f∘rho, then sigma = (G - 4f)∘rho / 5. ∎

**(d) T implies Z_rho ≅ Z [DER].** Let kappa be in N. K_kappa has V = 1, so T makes it the unknot. Then sigma(K_kappa) = 0 and d^(kappa) = 0. This uses neither Ito's theorem nor the normal-intersection lemma. read-casson made the same remark.

**(e) Side remark: twist rays [DER, sketch].** Along a twist ray, L(T_c^n) = n·L(T_c), and so sigma(K_{T_c^n}) = n·sigma(K_{T_c}) by (*).

*Reason.*
- Delta_3^2 acts on W(6,0) restricted to B_3, which is 2·W(3,1) ⊕ W(3,3), by two scalars.
- The writhe changes by an even multiple of n.
- So V_n := V_{K_{T_c^n}} = alpha t^{un} + beta t^{vn} with u and v even, and alpha + beta = V_0 = 1 (K_{T_c^0} is the unknot).
- Hence V_n = t^{vn} + (V_1 - t^v)·(t^{un} - t^{vn})/(t^u - t^v). At t = -1 the last ratio tends to n and V_1(-1) = 1, so V_n(-1) = 1 and V_n'(-1) = n·V_1'(-1).

This is consistent with read-casson's unaudited claim that sigma(K_·) is a homomorphism on I_2. By (*) and Morita, that claim is equivalent to L being a homomorphism on I_2. The remark does not prove it.

---

## 7. Sanity check: T_c^n with a trefoil curve [CHK]

**Setup.**
- Let U be the closed 3-braid sigma_1 sigma_2, which is the unknot, and let A be its braid axis.
- Let D be a meridian disk of A meeting U in three points, and put gamma = ∂D on the bridge sphere around three branch points.
- In Sigma_2(U) = S^3, the open book (A, D) lifts to an open book whose page D~ is the double cover of D over 3 points: a once-punctured torus.
- Its monodromy is the lift of sigma_1 sigma_2, namely T_a T_b. This is the right-handed trefoil fibration.

So c := ∂D~, the lift of gamma, is a separating curve on the Heegaard surface with K_c = right-handed trefoil and a_2 = 1.

**The knots.** The twist T_c lifts Delta_3^4 = (sigma_1 sigma_2)^6, by the chain relation (T_a T_b)^6 = T_c. So K_{T_c^n} is the closure of (sigma_1 sigma_2)^{6n+1}, which is T(3, 6n+1). For n < 0 this is the mirror of T(3, 6|n| - 1).

**Consistency with convention 1.4.** M_{T_c^n} = S^3_{-1/n}(RHT) = Sigma(2,3,6n+1) = Sigma_2(T(3,6n+1)). The other twist direction would give -Sigma(2,3,6n-1), whose Casson invariant has the wrong sign. So the convention and the knot are consistent.

**Data, exact, for n = -3, ..., 3 (script Part 1).**
- V_{T(3,6n+1)} = t^{6n}(1 + t^2) - t^{12n+2} for n ≥ 0, and the mirror for n < 0.
  - V(1) = 1, V'(1) = 0, V(-1) = 1, V'(-1) = 0. So L = 0.
- sigma(T(3,6n+1)) = -8n, by the lattice-point formula. For reference, T(3,4), T(3,5), T(3,7), T(3,11), T(3,13) give -6, -8, -8, -16, -16.
- Mullins: sigma/8 - L/12 = -n = lambda(S^3_{-1/n}(RHT)) = -n·a_2. ✓
- d^(T_c^n) = n, and q(tau_2 T_c^n) = n(1/10 - 1) = -9n/10.
- (*): the left side is 5 sigma + 4 d^ = -40n + 4n = -36n. The right side is (10/3)·0 + 40·(-9n/10) = -36n. ✓ for all seven values of n.
- Reducing curve c_0, with K_{c_0} the unknot: K_{T_{c_0}^n} is the unknot, sigma = L = 0, d^ = n and q = n/10. Then 0 + 4n = 40·n/10. ✓

**What this tests.** Mullins's normalisation, the Birman-Hilden identification and the twist convention, on an infinite family.

**What it does not test: the coefficient -1/10.**
- On a single twist ray, any coefficient c fits, with q(tau_2 T_c) = -a_2(K_c) - c.
- The value q(tau_2 T_c) = 1/10 - a_2 comes from the same surgery formula, so that part of the check is tautological.
- The constant rests on the invariant-theory step of Proposition 3, which is checked in Section 3.
- A non-tautological test of -1/10 needs an explicit element of Ker tau_2 with d^ ≠ 0, and its knot. Kasahara's computation guarantees such an element of the form T_c^{10}·w with w in [M_2, I_2]. Finding one is a computer search, so it was not done.

---

## 8. What is already in the literature

- **Kasahara 2001.** read-kasahara read §§2, 3 and 6 in full.
  - Prop 6.1 is the first equivalence in (c): d_1 factors through rho iff Z_rho ≅ Z.
  - Rem 6.3(1) is a weak form of (b): Z_rho finite implies rho is unfaithful on I_2.
  - Problem 6.2 asks for |Z_rho|.
  - He never uses Mullins's formula or knot signatures.
- **Morita 1991.** The decomposition lambda = core + tau_2-term, and the homomorphism property.
  - The closed-surface core normalisation h(g - h) is Morita's Thm 5.7, as cited by Faes-Massuyeau (via read-casson).
  - The genus-two coefficient -1/10, i.e. -1/(2(2g+1)), was derived by read-casson from that formula and here from the Seifert form.
  - I did not find it stated verbatim. The likely place is Morita-Sakasai-Suzuki, Quantum Topol. 11 (2020), arXiv:1711.07855. Its abstract does not state it, and I did not read the full text.
- **Mullins 1993.** The Sigma_2 formula.
- **Meyer function on I_2.** Endo 2000 and Morifuji, via read-casson; sign unverified.
- **Not found in any source:**
  - the combination (*);
  - its consequences (a) and (b) in signature form;
  - the fifth equivalence in (c);
  - consequence (d).

  Searches behind this:
  - two web searches here: Casson/Mullins/Jones/Torelli in genus two, and Morita's closed formula with 2(2g+1);
  - read-casson's and read-kasahara's searches, including the OpenAlex list of the 10 works citing Kasahara 2001.

  The search is not exhaustive: read-kasahara could not reach Semantic Scholar or MathSciNet. All the ingredients are classical, so a specialist may regard (*) as folklore.

---

## 9. Obstructions and open points

- **(*) is a reformulation.** It makes no progress on existence. Deciding Problem 6.2 is now exactly deciding whether the signature homomorphism sigma(K_·) restricted to N vanishes. No step above produces kernel elements or constrains their signatures.
- **Where d^ can hide.** Every term on the rho-side of (*) depends on the Heegaard embedding: Lambda and Q are not M_2-invariant.
  - The only M_2-invariant homomorphism, d^, is invisible to traces of first-order expansions, because det rho = ±1 (Kasahara's addendum). For example, at q = 1 the trace of the first-order term vanishes on I_2.
  - So (*) routes d^ through a matrix coefficient and sigma. This is how an invariant d^ can be nonzero on N while every rho-side quantity vanishes there.
- **Conventions not pinned in a source here.** None of these affects (a)-(d) beyond the overall sign of sigma(K_kappa) relative to d^(kappa).
  - the twist direction of 1.4, relative to Morita's or Kasahara's "positive" twist;
  - Jones's variable versus A^{∓4}, and Kasahara's t versus q;
  - the Meyer sign.
- **Inputs taken from sibling reports rather than re-read:**
  - Morita's homomorphism theorem and his tau_2 formula;
  - Kasahara's Cor 1.2 and the rank-14 Gamma_{0,2} statement;
  - Mullins's normalisation.
- **Possible next step (theory, not a sweep).** Take psi in Ker phi(2), so that rho(psi) = I + O(h^3) at t = -1. Then r_psi = 1 + O(h^2) there, and Q(Delta_1(psi)) = 0. So (*) reduces to

      4 d^(psi) + 5 sigma(K_psi) = (10/3) · (q d/dq) log r_psi |_{q=1},

  a statement about the first-order expansion of rho at q = 1 alone. At q = 1, I_2 acts by scalars, because the Hecke algebra becomes Q[S_6] and I_2 dies in Sp(4, F_2) = S_6. So this is the derivative of one matrix coefficient of a homomorphism I_2 -> gl_5. Controlling it on Ker phi(2) is the most concrete place I can see to look for a constraint on sigma over N.
