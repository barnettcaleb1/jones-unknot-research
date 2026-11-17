# Fifth-root satellite saturation

Theory-only deduction, 2026-11-03. No computation or enumeration. Written proof; priority unassessed. This is an elementary consequence of cyclotomic color reduction, not a new faithfulness or detection theorem.

## Proposition

Let F=F_2[q]/(Phi_5(q))=F_16, with q the distinguished fifth root. Use the usual Jones convention q=A^-4 and set A=q, which satisfies that equation at order five. Put d=A^2+A^-2=q^2+q^3. For every framed annular pattern P, embedded using the zero framing of a companion knot K, its bracket value in F has the form

    B(P(K)) = a_P + b_P V_K(q),

where a_P,b_P depend only on the framed pattern, not on K. Consequently,

    V_K(q)=1
       iff B(P(K))=B(P(U)) for EVERY framed annular pattern P.

The implication to all patterns holds for arbitrary links or skein elements in the solid torus, without a winding restriction or a strong inversion. The converse uses only the core pattern, since d is nonzero.

Therefore applying U5-FROB5 to any or all compatible (p,+/-1) cable descendants of a flat strongly invertible knot supplies NO additional fifth-root condition beyond U5-FROB5 itself. The same is true for every other unknotted pattern P(U)=U: once the companion passes this test, its satellite passes automatically. This claim concerns the fixed quotient F only, not the full Jones polynomial or higher cyclotomic jets.

## 1. Color reduction with no semisimplicity assumption

Use reduced zero-framed colored Jones J_N, with J_1=1 and J_2=V. Habiro's integral cyclotomic expansion is

    J_N(K;q) = sum_(k=0)^(N-1) H_k(K;q)
                product_(j=1)^k(q^N+q^-N-q^j-q^-j),
    H_0=1.

The H_k are integral Laurent polynomials independent of N. Primary reference for these exact conventions: [Garoufalidis-Le, Geometry & Topology 15 (2011), section 3.2, equations (11)-(12)](https://people.mpim-bonn.mpg.de/stavros/publications/printed/asymptotics_of_the_colored_jones_function_of_a_knot.pdf), referring to Habiro's theorem.

At q^5=1, this immediately implies

    J_N(K;q)=1       if N = +/-1 modulo 5;
    J_N(K;q)=V_K(q)  if N = +/-2 modulo 5.

For the first statement the j=1 factor is zero, so every k>=1 term vanishes. For the second the first factor is the same as for N=2, and the j=2 factor is zero, so all k>=2 terms vanish. These identities hold for arbitrarily large N; the first vanishing factor remains present in every later product.

No assertion is made that J_(5r) is determined by V. Those reduced colors can retain additional information, but their unreduced quantum dimension is zero at this specialization, which makes them invisible to an ordinary satellite bracket.

## 2. The integral annular basis and zero dimensions

The solid-torus bracket skein is Z[A^+-1][z]. Use its integral Chebyshev basis

    e_0=1,   e_1=z,   e_(n+1)=z e_n-e_(n-1).

Write the actual framed pattern as a finite skein expansion

    [P]=sum_(n>=0) p_n(A)e_n.

This step is an identity in the solid torus BEFORE any root specialization. It does not require Jones-Wenzl projectors to exist after specialization and does not infer a satellite operator from equality in the skein of S^3.

Evaluation on the zero-framed companion is the usual colored identity

    B(e_(N-1)(K))=Delta_(N-1) J_N(K;q),
    Delta_(N-1)=(-1)^(N-1)
                (A^(2N)-A^(-2N))/(A^2-A^-2).

The denominator is nonzero in F, since q has order five. In characteristic two the signs disappear. Because A also has order five, the dimensions satisfy

    Delta_(N-1) = 0  for N = 0 modulo 5,
                  1  for N = +/-1 modulo 5,
                  d  for N = +/-2 modulo 5.

Here d^2+d+1=0 and d is a unit. These values follow from the displayed geometric sum; in particular the dimensions are periodic with period five.

Combining dimensions and color reduction gives the complete evaluation table:

    B(e_(N-1)(K)) = 0, 1, or d V_K(q),

according to these three residue classes. Thus

    a_P = sum_(n+1=+/-1 mod5) p_n(A),
    b_P = d sum_(n+1=+/-2 mod5) p_n(A).

This proves the affine satellite formula. It also proves

    B(P(K))-B(P(U))=b_P(V_K-1).

All patterns are covered at once, so iterated satellite constructions cannot add information at this specialization either.

## 3. Normalization and the cable consequence

The theorem is stated for framed brackets, eliminating possible writhe ambiguity. For an oriented pattern with its framing fixed in the solid torus, the same framing normalization factor relates B(P(K)) to its Jones polynomial for every ZERO-framed companion K. The number of components and that factor depend on the pattern, not on which knot is inserted with its preferred longitude. Since the unknot bracket d is nonzero in F, equality of the framed bracket values gives equality of the corresponding normalized Jones values.

In particular P=C_(p,+/-1) has P(U)=U as a knot. If V_K=1 in F, then V_(C_(p,+/-1)(K))=1 in F, for every p. This statement is unconditional and independent of whether the cable carries the compatible strong inversion required in U5d. Therefore the conditional propagation of flatness in U5d followed by FROB5 can never yield a stronger test than FROB5 alone.

The authoritative scope of U5d was checked in work/defect-calculus/cable_screen.txt: its propagation is for compatible marked shells with the inherited inversion. No all-axis classification is assumed here, and none is needed for the saturation conclusion.

## 4. Interpretation and limits

This is a precise finite-information ceiling for the proposed cable amplification. At the fifth root in characteristic two, the entire family of ordinary satellite measurements contains exactly the same companion information as the single ordinary Jones value. Colors divisible by five are lost to zero quantum dimension; colors in the other residue classes reduce to colors one and two.

The proof uses integral identities before reduction, so characteristic-two nonsemisimplicity does not invalidate it. No modular-category semisimplicity, positivity, or faithfulness is used. The same basic color-reflection argument works at a complex fifth root, with the appropriate dimension signs, so it should be regarded as familiar root-of-unity truncation made explicit for this proposed amplification.

To get beyond this ceiling, one needs genuinely different data: other roots, derivatives before specialization, reduced colors with vanishing dimension, or a geometric consequence not determined by the specialized satellite brackets. Flatness has not been shown to supply any of those additional data here.
