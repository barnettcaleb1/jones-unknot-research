# Fifth-root transfer: universal Sakuma identity and nearest prior art

Bounded theory/primary-source pass, 2026-11-03. No enumeration. The identity below was derived independently here and by the parent thread during this pass. Priority remains unassessed.

## A stronger statement than the flat-case obstruction

Let (kappa,tau) be any strongly invertible knot, S=U union c its PREFERRED Sakuma link, and let V be the ordinary Jones polynomial normalized to one on the unknot. Let q be a primitive fifth root in F_16 and interpret q^(1/2) as its unique square root q^3. Put

    d = q^(1/2)+q^(-1/2).

Then d^2+d+1=0, so d^3=1 and d^2-1=d in characteristic two. The proposed universal identity is

    V_S(q)^2 = 1 + d V_kappa(q).                       (1)

Equivalently,

    V_S(q)^2 - d^2 = d (V_kappa(q)-1).                (2)

Consequently

    V_S(q)=V_(U_2)(q) iff V_kappa(q)=1.

This equivalence is ONLY at this finite-field specialization. It does not claim that full Sakuma Jones is determined by ordinary Jones of kappa. Since squaring is an automorphism of F_16, (1) also says that this specialized Sakuma value is independent of the strong inversion. Explicitly V_S(q)=1+d^2 V_kappa(q)^8.

## Proof

Use the zero-framed annular bracket P(A,z) of c in S^3 minus U. Choose A with A^(-4)=q; it too has order five. Write delta(A)=-A^2-A^-2 and lambda(A)=-A^4-A^-4. Then delta(A)=d and, in characteristic two,

    lambda(A^2)=delta(A)^4=d.

By the twofold annular state-orbit transfer,

    B(C_2^0(kappa))(A)=P(A^2,delta(A)) modulo 2.

The preferred-framing and linking-transfer argument in periodic_audit.md identifies this lift as the zero-framed two-parallel, including each component's framing. The preceding eigenvalue identity turns the right side into P(A^2,lambda(A^2)). By the encircling formula,

    P(A^2,lambda(A^2))=B_S(A^2)/delta(A^2)=V_S(q^2).

Here lk(U,c)=0 and zero self framings make the normalized Jones equality exact. Frobenius gives V_S(q^2)=V_S(q)^2, including the half-integer exponents under the chosen square-root convention.

Finally z^2=e_2+1 gives B(C_2^0(kappa))=1+(d^2-1)J_3(kappa;q). Habiro's expansion gives J_3=J_2 modulo Phi_5: q^3+q^-3=q^2+q^-2 makes the first cyclotomic kernels equal and the second N=3 kernel zero. Thus J_3=V_kappa at q, proving (1).

The shorter proof uses only ONE evaluation of P: the encircled one. The extra evaluation P(A,delta)=delta was needed for the stronger integral factorization in the original audit but is unnecessary at the fifth root, because the two relevant evaluation points already coincide there.

## What is standard, and what was actually found

1. [Melissa Zhang, A rank inequality for the annular Khovanov homology of 2-periodic links, AGT 18 (2018), Corollary 5](https://msp.org/agt/2018/18-2/agt-v18-n2-p18-p.pdf) is the direct annular-periodic congruence ingredient. The proof above is its elementary bracket state-orbit form.

2. [Snape's thesis, Theorem 3.3.14 and equation (3.18)](https://theses.gla.ac.uk/39015/1/2018SnapePhD.pdf) supplies the encircling relation and compares the two annular viewpoints. A bounded text read of its polynomial sections did not locate (1), but this is not an exhaustive priority claim.

3. [Garoufalidis-Le, Asymptotics of the colored Jones function of a knot, Geometry & Topology 15 (2011), section 3.2](https://people.mpim-bonn.mpg.de/stavros/publications/printed/asymptotics_of_the_colored_jones_function_of_a_knot.pdf) states Habiro's cyclotomic expansion in precisely the normalization needed for the color reflection. This last step is standard, not a new colored-Jones theorem.

4. [Murasugi, Jones polynomials of periodic links, Pacific J. Math. 131 (1988), Theorem 1](https://msp.org/pjm/1988/131-2/pjm-v131-n2-p09-s.pdf) is the nearest classical ordinary-Jones comparison. For period two its ideal contains 1-t-t^(1/2); modulo two that is Phi_3(t^(1/2)), rather than Phi_5(t). Formula (1) uses the retained axis component and the preferred parallel geometry, not merely the ordinary Jones polynomial of the quotient knot c. Thus it is not simply Murasugi's basic period-two congruence with variables renamed.

5. [Sakuma, An evaluation of the Jones polynomial of a parallel link, Math. Proc. Cambridge Phil. Soc. 104 (1988), 105-113](https://doi.org/10.1017/S0305004100065270) is plausible nearby prior art by title and subject. Only the publisher's extract was accessible during this bounded pass; no assertion about its full contents or absence of (1) is justified.

## Adjacent 2026 paper: distinguish the invariant

[Collari-Lisca, A Polynomial Invariant of Strongly Involutive Links, arXiv:2606.21471](https://arxiv.org/html/2606.21471v1), Theorem 1.3 and Remark 1.4, proves a modulo-two reduction from its equivariant HOMFLY-PT invariant to ordinary HOMFLY-PT. Its equivariant Jones specialization is an Euler characteristic from the Lobb-Watson theory and recovers Couture's invariant. It is NOT defined as the Jones polynomial of the Sakuma link. That theorem therefore supplies useful context for loss of inversion information modulo two, but cannot be substituted for (1) or used to infer flatness without an additional comparison theorem.

## Research judgment

The exact new-to-this-project statement worth recording is (1), not a proliferation of root tests. It explains why the fifth-root flatness test is inversion-independent, gives a normalization check for any two proposed Sakuma diagrams of the same knot, and shows the mechanism as an equality of annular evaluation points after Frobenius. It remains finite information. Neither an infinite tower nor a theorem recovering the full Jones polynomial follows from it.
