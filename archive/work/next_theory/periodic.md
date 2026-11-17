# Periodic transfer between the two Sakuma axes

Theory-only pass; no numerical search. The new colored congruence below is a written deduction proposed for independent checking, not a priority claim or a detection theorem.

## 1. The elementary Frobenius transfer

Let P_L(A,z) be the unreduced annular Kauffman bracket, with empty diagram 1 and a contractible circle delta(A)=-A²-A^-2. Let L^(p) be the p-fold cyclic lift of an annular link, p=2^r. Then

    P_(L^(p))(A,z) = P_L(A^p,z) mod 2.

Proof: choose a lifted periodic diagram and act on its Kauffman states. Non-fixed orbits have even cardinality and cancel mod2. Fixed states descend to states downstairs. Crossing weights acquire exponent p. Every contractible state circle lifts to p circles, whose value delta(A)^p equals delta(A^p) in characteristic two; every essential state circle lifts to one essential circle and retains a factor z. This proves the annular identity. Evaluating z=delta(A) gives the ordinary lifted bracket.

This is the bracket form of the decategorified relation in [Melissa Zhang, AGT18 (2018), Corollary 5](https://msp.org/agt/2018/18-2/agt-v18-n2-p18-p.pdf). It is not Cornish's theorem; the latter is cited in Zhang's discussion of earlier next-to-top-sector rank inequalities.

If the branch-set annular knot B=U in the complement of c has flat class u(A)delta(A), every 2^r-fold annular lift has, modulo 2, the framed bracket of the 2^r-component unlink. With compatible Jones normalization this is the corresponding unlink Jones congruence. The winding-zero hypothesis makes the lift have 2^r components.

**Axis warning:** this lifts U in the branched cover of c. The zero-framed two-parallel of kappa is instead the lift of c in the cover branched over U. The latter requires the OTHER annular polynomial.

## 2. Two evaluations of the other annular polynomial still give a useful factor

Let S=U union c be a preferred Sakuma link with the unlink Jones polynomial, and let

    P(A,z) = annular bracket of c in S3 minus U.

Both components are unknotted and lk(U,c)=0. With compatible diagrams the same writhe unit u normalizes c and S. Therefore, putting lambda(A)=-(A^4+A^-4)=2-delta²,

    P(A,delta)=u delta,
    P(A,lambda)=u delta.

The first equation is c=U; the second is the encircling identity and unlink Jones for S. Because the winding number is zero, P contains only even z powers. Set Pbar=P/u. Polynomial division in w=z² over R=Z[A^+-1] gives

    Pbar(A,z)-delta
      = (z²-delta²)(z²-lambda²) H(A,z²)                 (1)

for H in R[z²]. This does not assert that Pbar is trivial. To justify the second factor without any comaximality assumption, first divide by w-delta², then evaluate at lambda²; the nonzero difference lambda²-delta² is not a zero divisor in R.

## 3. A colored-Jones consequence, modulo two

Let C_2^0(kappa) denote the zero-framed two-parallel of kappa. It is the lift of c in Sigma2(U)=S3. Let j_3(kappa;q) be the reduced, zero-framed color-three Jones polynomial, normalized to 1 on the unknot, using q=A^4 (inverting q changes none of the cyclotomic divisibility claims).

The Jones-Wenzl relation e_2=z²-1 gives the unreduced relation

    B(C_2^0(kappa)) - delta²
       = (delta²-1)(j_3(kappa)-1),                     (2)

where B is the zero-framed unreduced bracket. Preferred Sakuma framing is essential here: otherwise the lifted parallel has nonzero framing.

Apply Frobenius transfer to (1), with A replaced by A² and z=delta(A). The Jones/framing normalization is compatible modulo2: u(A²) and the cover's squared writhe unit agree modulo2. In characteristic two,

    delta(A²)=delta(A)²,
    lambda(A²)=delta(A)^4.

Thus (1) gives

    B(C_2^0(kappa))-delta²
      = delta^4(1+delta²)(1+delta^6) H(A²,delta²) mod2.

Cancel the nonzero factor delta²-1=delta²+1 using (2), in the Laurent domain F2[A^+-1]. We obtain

    j_3(kappa)-1
      is divisible by delta^4(1+delta^6) modulo2.       (3)

Now delta²=q+q^-1 modulo2, so

    delta^4 = (q+1)^4/q²,
    1+delta^6 = (q²+q+1)(q^4+q³+q²+q+1)/q³.

Consequently the proposed necessary condition is

    j_3(kappa;q) = 1
      mod (2, (q+1)^4 Phi_3(q) Phi_5(q)).             (4)

The passage from divisibility in F2[A^+-1] to F2[q^+-1] is valid by decomposing the former free module into the four A-exponent residue classes modulo4; both the numerator and the factor in (4) lie in the zero residue class.

In particular j_3 is 1 at primitive third and fifth roots over characteristic two. This is a finite congruence, not full colored-Jones triviality. I have not checked its novelty or whether portions are already universal consequences of the Arf invariant/cyclotomic expansions. The (q+1) factor may overlap known universal divisibility. The proof uses two known scalar evaluations of the OTHER-axis annular class, not an invalid assertion that this entire class is flat.

## 4. Component geometry of the opposite-axis lift

Let cutting U along the crossing disk of c give the e-type arcs A and B in the cut ball T. Let D(T)=J_A union J_B be the two ordinary component closures. In the double cyclic lift of U in the complement of c, the two lifted components use A from sheet1 with B from sheet2, and A from sheet2 with B from sheet1. Each component has knot type

    J_A # J_B,

up to orientation; the covering charts are orientation-preserving, so no mirror is introduced merely by the cover.

Proof: for a single lifted component, each cut-copy ball meets that component in one proper arc and its boundary is a connected-sum sphere. Closing those proper arcs gives exactly J_A and J_B. After replacing both one-string tangles by trivial arcs, the remaining standard lift component is an unknot. This is a component-knot statement, not a description of the whole lifted link. The two lifted components may be entangled, so their full Jones polynomial cannot be replaced by the product of component polynomials.

This observation and the modulo-two unlink polynomial of the opposite lift do not yet yield a new constraint on V(J_A)V(J_B). A splitting or partial-trace argument would be additional mathematics, not a consequence of the link polynomial alone.

## 5. What Smith theory does and does not provide

Zhang's spectral sequence gives a rank inequality from the annular homology of a periodic lift to that of its quotient. Later localization results, for example [Borodzik–Politarczyk–Silvero, Khovanov homotopy type, periodic links and localizations, Theorems1.3–1.5](https://doi.org/10.1007/s00208-021-02157-y), also compare ordinary homology of the lift with annular homology downstairs.

These inequalities point from the lift's rank down to the quotient's rank. Polynomial congruence to an unlink provides no upper rank bound for either lift; hence it does not collapse the detecting homology. In particular, using Hedden's two-cable unknot detection would require the actual homology of C_2^0(kappa), not its finite characteristic-two Jones congruence.

The constructive output of this pass is (1)–(4): a way to exploit both axes without identifying their annular polynomials. Its limitations are explicit and it leaves Lemma Q open.
