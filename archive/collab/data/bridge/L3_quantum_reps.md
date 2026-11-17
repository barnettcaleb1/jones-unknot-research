# L3 bridge notes: quantum representations, operator algebras, TQFT (Claude helper, 17 Nov 2026)

Status: working notes. Nothing outward-facing. Proofs below are mine and have not been refereed.

## 0. Verdict in five lines
1. The precise "trace-faithfulness" statement equivalent to JC is CONSERVATIVITY (reflection of units) of the bracket
   functor on (1,1)- or (2,2)-tangles, not faithfulness of any braid representation. JC <=> Cons_1 <=> Cons_2 <=> U_2
   (unitarity version). Lemma Q is Cons_2 restricted to tangles with unknotted N-closure, and is equivalent to
   "V detects the 2-component unlink among the doubles D(T)". (Sections 1-2; mostly a reformulation of Sikora's equivalence.)
2. Faithfulness, including asymptotic faithfulness, sits DOWNSTREAM of JC (Bigelow 2002, Ito 2015) and is vacuous at n = 1.
   With the colour fixed at 1, "asymptotic faithfulness" of the Jones representations is the same thing as generic
   faithfulness (open for n >= 5). Asymptotic faithfulness in the FWW/Andersen sense needs colours that grow with the level. (Section 3.)
3. Positivity combined with the BHMV/Marche-Narimannejad machinery PROVES a detection theorem, but only in doubled
   (diagonal) geometry: Theorem E (the BHMV invariants detect the unknot among curves on the standard Heegaard surface of
   #^g(S^1xS^2); the equality case of Garoufalidis' Heegaard-genus bound characterises #^g(S^1xS^2)). (Section 4.)
4. Precise obstruction: in S^3 every Heegaard splitting is off-diagonal. The unknot sits at Cauchy-Schwarz ratio
   eta_r^g -> 0, deep in the interior, and the missing ingredient is reflection positivity for the S^3 gluing. (Section 4.4.)
5. At rank >= 3, TL_n(Z[A^+-1]) has exotic units that come from no braid: 1+x with x = e1 - delta e1 e2, x^2 = 0.
   So conservativity is special to the commutative range n <= 2. The right higher-rank statement is unitarity
   (U_n), which kills these units. (Section 5.)

## 1. Conventions and the eigen-dictionary (checked by the H-diagram computation)
- TL_2 = span{1,e}, e^2 = delta e, delta = -A^2-A^-2. Minimal idempotents p0 = e/delta, p2 = 1 - e/delta.
  Unnormalised Markov trace (empty = 1): tr(p0) = 1, tr(p2) = delta^2 - 1 = [3].
- A (2,2)-tangle T (2 top, 2 bottom endpoints): <T> = y 1 + x e = lambda0 p0 + lambda2 p2 with lambda2 = y, lambda0 = y + delta x.
  TL_2 is commutative and stacking multiplies eigenvalues: lambda_j(T o T') = lambda_j(T) lambda_j(T').
- N(T) = cap o T o cup: <N(T)> = delta lambda0. Trace closure: <D_tr(T)> = lambda0 + [3] lambda2.
- Rotation by 90 degrees swaps 1 <-> e. In eigen-coordinates it is the SU(2) S-matrix on the channels {0,2}:
  (lambda0, lambda2) -> ((lambda0 + [3] lambda2)/delta, (lambda0 - lambda2)/delta), and S^2 = I because 1 + [3] = delta^2.
  So the arborescent calculus (stacking plus Conway sum) is "pointwise product + S-conjugated product" on C^2.
  This should be the board's star product in R[s]/(s(s-d)) written in eigen-coordinates. (Normalisations not cross-checked.)
- THE DICTIONARY. Frame the quotient tangle so that the axis is N(T). Inside N(k) the axis is a cap+cup and the rung k
  joins them. The colour-2 rung with (1,1,2) vertices is the H-diagram, and it equals p2 in T's vertical frame. Hence
  <Theta;1,1,2> = tr(<T> p2) = [3] lambda2. So J = lambda2 and the axis condition is "lambda0 is a unit" (after framing).
  The same computation in the width-ladder frame (axis = trace closure D(X)) gives J = the e-coefficient, which is the same statement rotated by 90 degrees.
  Consistent with CONTEXT ("<Theta;1,1,2> = Delta_2 y").

## 2. Bridge A: JC as conservativity of the bracket functor
Definitions. Tang = category with objects n and morphisms (n,n)-tangles in D^2 x I up to isotopy rel boundary.
F = Kauffman bracket functor to TL(Z[A^+-1]), framed. Aut(n) = B_n: an invertible (n,n)-tangle is a braid, because its exterior
is cut from a product by an incompressible horizontal surface (Waldhausen).
- Faith_n: F restricted to B_n is injective modulo framing scalars.
- Cons_n: if <T> is a unit of TL_n(Z[A^+-1]), then T is a braid.
- U_n: if <T>^* <T> = 1, where * is the bar-involution A -> A^-1 composed with up-down reflection, then T is a braid.
  Equivalently <T> is unitary at every Jones root, where the TL quotient is a C*-algebra.
  Note <T>^* = <T^r>, with T^r the reflection of T in a horizontal plane; for braids beta^r = beta^-1.

PROPOSITION A1 (units of TL_2). TL_2(Z[A^+-1])^x = { +-A^k <sigma>^n : k,n in Z } = image of framed braids, up to sign.
Proof. A unit has lambda0 = e0 A^a and lambda2 = e2 A^b with x = (lambda0-lambda2)/delta integral. Since delta = -A^-2(A^4+1),
the condition is e0 zeta^(a-b) = e2 in Z[zeta_8]: either a-b = 0 mod 8 with equal signs, or a-b = 4 mod 8 with opposite signs.
The braid sigma^n gives (lambda0, lambda2) = ((-A^-3)^n, A^n), so a-b = -4n with sign ratio (-1)^n. Solve n = (b-a)/4, k = b-n. QED.
So at n = 2: unit = unitary = braid-like. By Parseval, a Laurent polynomial with |f| = 1 on the circle is a signed monomial.

THEOREM A2. JC <=> Cons_1 <=> Cons_2 <=> U_2. Lemma Q <=> Cons_2 restricted to T with N(T) = unknot.
Proof. Cons_1 is JC, because a (1,1)-tangle is a long knot and <K> is a unit iff V_K = 1 (use V(1) = 1 and V'(1) = 0).
Cons_2 => JC: tie K into one strand of 1_2.
JC => Cons_2: suppose <T> is a unit. Then lambda0 is a unit, so V(N(T)) = 1. If N(T) were a 2-component link then |V(1)| = 2, a contradiction.
So N(T) is a knot, and by JC it is the unknot. Then T is the quotient tangle of a strongly invertible knot: Sigma_2 of the closing
ball is a solid torus, so Sigma_2(B^3,T) = E(K) for a knot K in S^3, and the covering involution is a strong inversion. Now J = lambda2 is a unit.
JC => Lemma Q (Gordon-Luecke, as on the board), so T is rational. A rational tangle with N(T) = U is sigma^n, a braid.
U_2 <=> Cons_2 by A1 and Parseval. The Lemma Q clause is the dictionary of section 1. QED.
Novelty: this is a categorical repackaging of Sikora (Canad. J. Math. 76 (2024) 707-727, arXiv:2005.08162: JC <=> the bracket
detects rational tangles). The phrasing "conservative functor / unit group / Faith_1 is vacuous" was not found anywhere.

PROPOSITION A3 (doubling identity, reflection positivity). For every (n,n)-tangle T, the double D(T) = (B^3,T) glued to its mirror
along the boundary sphere equals the trace closure of T^r o T. Reason: the involution z -> -z of D^2 x S^1, extended to S^3, is a
reflection whose fixed set is a 2-sphere bounding the ball containing T. Hence
   <D(T)> = tr(<T>^* <T>)  (an L^2(tr) norm, i.e. the GNS norm in the Jones tower),
and for n = 2:  <D(T)> = |lambda0|^2 + [3] |lambda2|^2  as Laurent polynomials, with |f|^2 := f fbar. Writhe(D(T)) = 0, so no framing correction is needed.
COROLLARY A4. If N(T) = U then <D(T)> = 1 + [3] J Jbar. Hence
   Lemma Q <=> V detects the 2-component unlink among the doubles D(T) of tangles with unknotted N-closure.
Also T is rational <=> D(T) is the unlink, since Sigma_2(D(T)) is the double of the knot exterior and contains an incompressible torus unless E(K) is a solid torus.
Categorified shadow: Khovanov homology detects unlinks (Hedden-Ni, Geom. Topol. 17 (2013) 3027; Batson-Seed, Duke 164 (2015) 801).
So Kh(D(T)) = Kh(U_2) forces T to be rational. Through Kh(D(T)) = H(End([T])) for the tangle invariant, Lemma Q becomes the
decategorification gap "chi(End[T]) = chi(End[1]) versus End[T] = End[1]". This is the categorification lane's question in my coordinates
(KWZ: rational <=> single embedded rational curve).
VARIANCE CRITERION. At a Jones root the trace is faithful and positive on the semisimple quotient, so for x = <T>:
   x unitary <=> tau(x^*x) = 1 = tau((x^*x)^2).
The second condition is a statement about the trace closure of (T^r T)^2. So U_n is equivalent to the Jones polynomials of two explicit "doubled" links.

## 3. Where faithfulness and asymptotic faithfulness actually sit
- Bigelow, JKTR 11 (2002) 493-505 (arXiv:math/0012086), and Ito, Math. Z. 280 (2015) (arXiv:1402.2028): if a quantum (for example TL)
  representation of some B_n is unfaithful modulo the centre, then a nontrivial knot (hyperbolic, of arbitrary genus) has trivial invariant.
  So JC => Faith_n for all n. Faithfulness is a CONSEQUENCE of JC, not a route to it.
- At n = 1, Faith_1 is vacuous (B_1 = 1) while Cons_1 is all of JC. This one line shows that no faithfulness theorem can imply JC by itself:
  the content lies in the non-invertible morphisms (caps and cups), i.e. in the Markov closure.
- FIXED-COLOUR DEGENERATION. At A = -e^{i pi/2r}, rho_r(sigma_i) -> -P_{i,i+1} as r -> infinity (delta -> -2 and e -> P-1).
  So the colour-1 Jones representations converge to a representation that factors through S_n. Also
  intersection over r of ker rho_r = ker rho_generic, because the matrix entries are Laurent polynomials vanishing at infinitely many points.
  Hence "asymptotic faithfulness at fixed colour" = generic TL faithfulness, which is open for n >= 5 and implied by JC.
  The FWW (Geom. Topol. 6 (2002) 523), Andersen (Ann. Math. 163 (2006) 347) and Marche-Narimannejad (Duke 141 (2008) 573) theorems live where
  colours (or the closed-surface Hilbert space) grow with the level. That regime sees coloured Jones and character varieties, not V.
- MUTATION KERNEL. The Klein four-group of pi-rotations of S_{0,4} acts by signs on every fusion channel of V_r(S^2; c,c,c,c),
  for all r and all equal colours c. So the quantum representations of Mod(S_{0,4}) relevant to 4-ended tangles are never faithful,
  and SU(2) coloured invariants do not see Conway mutation. The board's WIDTH2-COVECTOR non-injectivity (420 geometric bottom classes)
  is exactly what this predicts. To CONFIRM "mutation", test whether the coinciding bottoms differ by a pi-rotation of a 4-ended sub-tangle.
  Representation theory predicts the coincidences but does not certify the geometry.
- FLW (Comm. Math. Phys. 228 (2002) 177): for r >= 5, r != 6 (with small exceptions), the image of rho_r is dense. Each single level is
  therefore wildly non-detecting: values V(e^{2 pi i/r}) are dense. Detection can only come from the intersection over all r,
  i.e. from the polynomial identity, which is why JC is "arithmetic".

## 4. Bridge B (developed): positivity + BHMV gives detection exactly in doubled geometry
Setting: the BHMV SU(2) TQFT V_{2r} at A = -e^{i pi/2r}, with positive-definite Hermitian forms on closed surfaces (BHMV, Topology 34 (1995) 883;
see Marche-Narimannejad Remark 2.2). Here delta_r = -2cos(pi/r) and eta_r = Z_r(S^3).
H = genus-g handlebody with Sigma = boundary of H, and Z(H) = Z_r(H) in V_r(Sigma). For a simple closed curve w on Sigma, T(w) = curve operator (colour 1).

FACTS USED. (F1) Choose a handlebody H_w in which w is a meridian. In its BHMV orthogonal basis T(w) is diagonal with eigenvalues
-2cos(pi(j+1)/r), j = 0..r-2, where j is the colour on the edge dual to w. So T(w) is self-adjoint, its spectrum lies in [delta_r, -delta_r],
and its MINIMUM eigenvalue is delta_r, attained exactly on the w-colour-0 subspace. (Lemma 3.4 in Marche-Narimannejad uses this eigenvalue rule.)
(F2) BHMV Thm 2.1: the vectors u_sigma = Z_r(H, G_sigma) (admissibly coloured spine graphs) form an orthogonal basis with nonzero
(positive) norms.
(F3) Przytycki: the skein module K(H) is free over Z[A^+-1]. Over Q(A) the JW-coloured spine graphs G_sigma form a basis.
The denominators [n]! are nonzero at A = -1 and at A_r for n < r.
(F4) Bullock; Przytycki-Sikora (Topology 39 (2000) 115): K(H) at A = -1 is the coordinate ring of the SL2(C)-character variety
of pi_1(H) = F_g, with a knot gamma mapping to -tr rho(gamma).
(F5) Egorov identity, exact in TQFT: Z(f) T(w) Z(f)^-1 = T(f(w)).

THEOREM E (extremal rigidity in the double). Let w be a simple closed curve on the standard Heegaard surface Sigma of
#^g(S^1xS^2) = H u_id (-H). Suppose that for infinitely many r
     Z_r(#^g(S^1xS^2), w) = delta_r * Z_r(#^g(S^1xS^2)),   (unknot value)
Then w bounds a disk in H, so w is the unknot. The converse is obvious.
PROOF. (i) Z_r(#^g S^1xS^2, w) = <Z(H), T(w) Z(H)> and Z_r(#^g S^1xS^2) = ||Z(H)||^2. By F1, T(w) - delta >= 0, so the hypothesis says
<Z(H), (T(w)-delta) Z(H)> = 0. Hence (T(w)-delta)^{1/2} Z(H) = 0, i.e. T(w) Z(H) = delta Z(H) EXACTLY (positivity).
(ii) Gluing gives Z_r(H, s) = 0 for the skein s = w - delta*empty in K(H). Expand s = sum c_sigma(A) G_sigma (finitely many sigma, F3).
For r large every sigma that appears is admissible, and Z_r(H,s) = sum c_sigma(A_r) u_sigma. By F2, c_sigma(A_r) = 0.
This holds at infinitely many A_r, so c_sigma = 0 identically and s = 0 in K(H) (freeness).
(iii) Specialise A = -1 (F4): -tr rho(w) + 2 = 0 for every rho: F_g -> SL2(C). Take rho faithful into SU(2) (free groups embed in SU(2)).
Then tr = 2 forces rho(w) = I, so w = 1 in pi_1(H). (iv) By Dehn's lemma a simple closed curve on the boundary that is null-homotopic in H bounds a disk. QED.

COROLLARY E1 (equality case of Garoufalidis' bound; Topology 37 (1998) 219). If M = H u_f (-H) has Heegaard genus <= g and
|Z_r(M)| = Z_r(#^g S^1xS^2) for infinitely many r, then M = #^g(S^1xS^2).
Proof. By Cauchy-Schwarz, |<Z(H), Z(f) Z(H)>| <= ||Z(H)||^2, with equality iff Z(f)Z(H) = c Z(H). Then for every meridian gamma of H, F5 gives
T(f(gamma)) Z(H) = delta Z(H). Steps (ii)-(iv) show that f(gamma) bounds a disk in H. f sends a meridian system to disk-bounding curves,
which can be made disjoint, so f extends over H and M = H u_id (-H). QED.
In particular, the projective stabiliser of the handlebody vector, intersected over infinitely many levels, is exactly the handlebody group.
This is a finite-level, exact version of the Marche-Narimannejad mechanism. It uses positivity plus infinitely many levels and needs NO asymptotic integration.

NOVELTY (Theorem E, E1). Not found: searched for "quantum invariants detect connected sum of S^1xS^2" / Heegaard genus equality / handlebody stabiliser.
Closest: Garoufalidis 1998 (the inequality); Calegari-Freedman-Walker, JAMS 23 (2010) 107, arXiv:0802.3208, Appendix B (Cauchy-Schwarz genus bounds,
Dijkgraaf-Witten); Gilmer (WRT of links in #^g S^1xS^2 are rational functions for r large; lens-space skein detection, arXiv:math/9801132).
Treat as NEW-but-folklore-level: every ingredient is classical.

### 4.4 The precise obstruction: JC is OFF-diagonal
Every knot K in S^3 is isotopic onto some Heegaard surface Sigma of S^3 = H u_{f0} H'. Then
   <K>_r = <Z(H'), T(K) Z(H)>,  with  Z(H') = Z(f0) Z(H) != Z(H).
- Cauchy-Schwarz: |<K>_r| <= |delta_r| ||Z(H)|| ||Z(H')|| = |delta_r| eta_r^{1-g}, while the unknot gives |delta_r| eta_r.
  The unknot sits at ratio eta_r^g, and eta_r -> 0 (eta_r ~ r^{-3/2}). So it is never extremal: no Cauchy-Schwarz rigidity is available.
  The same happens in every presentation I checked. Markov trace: unknot tr = delta versus max delta^n. m-bridge plat: delta versus delta^m.
  Lemma Q / doubles: <D(T)> = 1 + [3]|J|^2 has no a priori upper bound, because <T> is not a bounded operator.
- POSITIVE-OPERATOR FORM OF JC (for K on Sigma): P_K := T(K) - delta_r >= 0 (F1), and
     V_K(zeta_r) = V_U(zeta_r)  <=>  <Z(H'), P_K Z(H)> = 0,     K bounds a disk in H  <=>  P_K Z(H) = 0  <=>  <Z(H), P_K Z(H)> = 0 (Theorem E).
  So JC says: orthogonality of P_K^{1/2} Z(H') and P_K^{1/2} Z(H), at all levels, forces the second to vanish, for SOME Heegaard surface containing K.
  The missing input is a positivity (reflection-positivity) relation between Z(H') and Z(H). It exists for doubles and fails for S^3.
  Expanding P_K = sum_{j>=1} (mu_j - delta) Pi_j over K-colours, the coefficients mu_j - delta are > 0, but the partial overlaps
  <Pi_j Z(H'), Pi_j Z(H)> are Fourier transforms (S-matrix) of the coloured Jones of K and have no sign.
- TRANSFER REFORMULATION (a restatement, recorded for completeness): JC <=> every K with V_K = 1 lies on a Heegaard surface Sigma whose
  Heegaard double D_Sigma(K), in #^g(S^1xS^2), has the unknot's BHMV invariants. (<= is Theorem E; => is trivial.)
  This is the precise sense in which the TQFT toolkit "almost" reaches JC: it decides the diagonal coefficient, and JC is the off-diagonal one.

## 5. Precise obstruction at rank 3: exotic units
In TL_3(Z[A^+-1]) let x = e1 - delta e1 e2. Then x^2 = delta e1 - delta^2 e1e2 - delta e1 + delta^2 (e1e2e1)e2 = 0. So u_f = 1 + f x is a unit for every f.
CLAIM: for f != 0, u_f is not +-A^k rho(beta) for any braid beta, and is not unitary at Jones roots.
Proof. At all but finitely many Jones roots, x acts nontrivially on the cell module W(3,1), which survives in the C*-quotient.
Braid images are unitary there, while u_f is unipotent and not the identity, and a unipotent unitary is the identity. QED.
So Cons_3 is NOT a formal consequence of anything at rank 2, and TL_n, n >= 3, has an "exotic unit" problem that TL_2 (commutative, units = braids by A1) does not.
- Realisation question (OPEN): is there a non-braid (3,3)-tangle T with <T> = 1 + f x? Constraints: f must vanish at A = +-1, +-i
  (at A = -1 every tangle with identity connectivity evaluates to +-1), plus ROOTS-type congruences.
  If such T exists, its trace closure has <.> = tr(1) (tr x = 0): a Jones-trivial 3-component link of EKT type. Cons_3 would fail while JC could still hold.
  The board's CX-ANTISYM note ("non-braid tangles ... not excluded; none constructed") is this question.
- Exotic units are NOT unitary, so the right higher-rank generalisation of JC is U_n (unitarity), not Cons_n.
  Open arithmetic question: is the integral unitary group U(TL_n(Z[A^+-1]), *) equal to +-A^k rho(B_n)? True for n = 2 (A1).
  For n = 3 this asks whether the Burau image of B_3 is the full integral unitary group of the Squier form over Z[t^+-1].
  (Compare McMullen, Math. Ann. 2013, and Venkataramana, Ann. Math. 2014, at roots of unity.) If yes, U_3 <=> "no non-braid tangle has a braid's bracket".
- Lesson for the width-two lane: End(V1 x V2 x V2) = Mat2 + Mat2 + K is non-commutative, so its blocks carry exotic units and nilpotents.
  A width-two "J = 1 without rationality" mechanism would most naturally be a nilpotent defect inside a Mat2 channel that dies under the fixed-cut trace.
  This suggests a targeted counterexample design (search for boxes whose channel matrices differ from a braid's by a nilpotent) and,
  dually, a proof target ("no box has a nilpotent channel defect").

## 6. Bridge C (sketch): all-colour Lemma Q through the theta-curve exterior vector
- The coloured theta evaluations {<Theta; a,b,c>} at level r are exactly the coordinates of Z_r(E(Theta)) in V_r(Sigma_2)
  in the BHMV orthogonal basis of the genus-2 handlebody N(Theta) with spine Theta. The trivial theta gives the handlebody vector Z_r(H'_2).
  So J is ONE coordinate, (1,1,2), of a vector in a space of dimension ~ r^3.
- If ALL coordinates matched the trivial theta's up to units at infinitely many r, steps (i)-(iv) of Theorem E would reduce
  "Theta trivial" to one skein statement: gamma - delta*empty = 0 in K(E(Theta)) for the meridians gamma of H'_2. That needs injectivity of the
  skein module of E(Theta) into the TQFT family on that element. This is known for handlebodies and fails in general:
  Gilmer, lens space L(9,q), arXiv:math/9801132.
- Similarly, with puncture colours c_r ~ alpha r, the Theorem-E argument reduces Sikora's statement to two coloured inputs:
  (a) asymptotic faithfulness for coloured punctured spheres, giving a disk in the tangle complement (T = rational + local knots);
  (b) coloured unknot detection for the local knots.
- VERDICT: the toolkit acts on the whole vector, while JC/Lemma Q give one fixed-colour coordinate. "One coordinate determines triviality of the vector"
  is the irreducible content. No transfer from colours to colour 1 is known: q-holonomicity does not supply initial conditions from J_1 alone,
  and cabling expresses J_N(K) through V of cables, i.e. through LINK Jones polynomials, where EKT shows detection fails.

## 7. Bridge D (negative): Jones' unitary representations of Thompson's group F
Jones (J. Comb. Algebra 1 (2017) 1-44, arXiv:1412.7740) realises every link as L(g), g in F, with the Kauffman bracket equal to the vacuum coefficient
<pi_delta(g) Omega, Omega> of a unitary representation, up to a power of delta set by the number of leaves. This holds for delta in the Jones spectrum.
So V is a positive-definite function on F, and JC is a statement about the fibre of g -> L(g) over the unknot.
Same obstruction: the unknot's coefficient is delta^{1-(#leaves-1)}-ish, interior. Cauchy-Schwarz rigidity applies only to the unlink with the maximal number of components,
which by the argument of section 4 is again a stabiliser statement. No leverage found; recorded so nobody repeats it.

## 8. What I would do next (cheap, concrete)
1. (Width two, 1-2 h, exact) For the 420 covector-coincident geometric bottom pairs, test the mutation prediction directly: is one bottom
   obtained from the other by a pi-rotation of a 4-ended sub-tangle? Representation theory (section 3) predicts all SU(2) coincidences of this type.
2. (Rank 3, < 10 min search) Enumerate (3,3)-tangles cap_i beta cup_j, beta in B_5 of length <= 8. Flag those whose bracket is a unit of TL_3 but lies outside
   +-A^k rho(B_3); test: unit with non-unitary Mat2 block at a Jones root. Any hit refutes Cons_3 and yields Jones-trivial 3-component links.
3. (Theory) Is U(TL_3(Z[A^+-1]),*) = +-A^k Burau(B_3)? An arithmetic question with a definite answer. If yes, U_3 reduces to the braid-fibre question.
4. (Theorem E referee) Check F1-F4 conventions against BHMV and decide whether Theorem E / E1 are worth a short note (they are true, clean and probably new,
   but off the JC path).

## Citations (checked by search unless marked)
- Sikora, Canad. J. Math. 76 (2024) 707-727, arXiv:2005.08162 (JC <=> bracket detects rational tangles; tangle equations).
- Bigelow, Does the Jones polynomial detect the unknot?, JKTR 11 (2002) 493-505, arXiv:math/0012086.
- Ito, A kernel of a braid group representation yields a knot with trivial knot polynomials, Math. Z. 280 (2015), arXiv:1402.2028.
- Marche-Narimannejad, Some asymptotics of TQFT via skein theory, Duke Math. J. 141 (2008) 573-587, arXiv:math/0604533
  (read: Thm 3.2 and the trace formula concern Tr_p(gamma) on Sigma x S^1; asymptotic faithfulness corollary).
- Blanchet-Habegger-Masbaum-Vogel, TQFTs derived from the Kauffman bracket, Topology 34 (1995) 883-927 (Thm 2.1 orthogonal basis, as quoted by M-N).
- Garoufalidis, Applications of quantum invariants in low dimensional topology, Topology 37 (1998) 219-224.
- Calegari-Freedman-Walker, Positivity of the universal pairing in 3 dimensions, JAMS 23 (2010) 107-188, arXiv:0802.3208.
- Freedman-Walker-Wang, Geom. Topol. 6 (2002) 523-539; Andersen, Ann. of Math. 163 (2006) 347-368;
  Freedman-Larsen-Wang, Comm. Math. Phys. 228 (2002) 177-199 [standard, not re-searched].
- Przytycki-Sikora, Topology 39 (2000) 115-148; Bullock, Comment. Math. Helv. 72 (1997) 521-542 [standard, not re-searched].
- Hedden-Ni, Geom. Topol. 17 (2013) 3027-3076; Batson-Seed, Duke Math. J. 164 (2015) 801-841 [standard, not re-searched].
- Gilmer, Skein theory and WRT invariants of links in lens spaces, Comm. Math. Phys. 202 (1999), arXiv:math/9801132.
- Jones, Some unitary representations of Thompson's groups F and T, J. Comb. Algebra 1 (2017) 1-44, arXiv:1412.7740 [not re-searched].

## 9. Sanity computations (run 17 Nov, < 1 min; script scratchpad l3/check.py, plain complex arithmetic, no sympy on this Mac)
- At three random generic A: <sigma> has eigenvalues (lambda0, lambda2) = (-A^-3, A); S^2 = I; S(<sigma>) = <sigma^-1>; TL_3 relations on W(3,1) hold;
  x = e1 - delta e1e2 satisfies x^2 = 0 with x != 0. All PASS.
- At Jones roots r = 5, 7, 11 (A = -e^{i pi/2r}): the cap Gram form on W(3,1) is definite (eigenvalues delta +- 1, both negative).
  sigma1 and sigma2 are unitary for it (defect ~ 1e-15). The exotic unit 1+x has unitarity defect 7.5, 13.6, 19.2. So 1+x lies outside the braid image, as claimed in section 5.
- NOT done: the rank-3 tangle realisation search (section 8, item 2) and a link-level check of the doubling identity. The identity is a formal consequence
  of the reflection argument and was checked by hand on sigma (D = unlink) and on knotted-strand examples (D = K # K* split with U).
