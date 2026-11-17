# Independent audit: a mod-two cyclotomic obstruction from a flat Sakuma link

Status: the stated conditional proposition checks, including the zero-framing normalization. This is a written hand proof, not a computational search. Independent of the first derivation in periodic.md; novelty and literature priority are unassessed.

## Proposition

Let (kappa,tau) be a strongly invertible knot whose preferred Sakuma link S=U union c has the Jones polynomial of the two-component unlink. Let J_N(kappa;q) denote the reduced, zero-framed N-dimensional colored Jones polynomial, normalized to one on the unknot; J_2 is the ordinary Jones polynomial, up to the harmless choice q versus q^-1. Then

    J_3(kappa;q)-1 is divisible by
    (q+1)^4 Phi_3(q) Phi_5(q)

in F_2[q^+-1]. In particular,

    V_kappa(q) = 1 in F_2[q^+-1]/(Phi_5(q)).

The latter quotient is F_16 because Phi_5 is irreducible over F_2. The congruence is unchanged by q inversion.

## 1. Two measurements of the other annular class

Use the annular class P(A,z) of c in the complement of U, NOT the branch-set annular class in the opposite solid torus. Put

    delta=-A^2-A^-2,    lambda=-A^4-A^-4.

Choose zero framing on c. Since c is an unknot, P(A,delta)=delta. Since the preferred Sakuma link has unlink Jones and lk(c,U)=0, the compatible zero-framed encircling equality is P(A,lambda)=delta. There is no unknown monomial here: adding the zero-framed axis has no self-writhe contribution and its mixed signs sum to 2lk=0.

The winding number of c is zero, so P has only even powers of z. Write y=z^2. The two evaluations of P-delta vanish at y=delta^2 and y=lambda^2. Division by the two monic linear factors, in the integral domain Z[A^+-1], gives

    P(A,z)-delta=(z^2-delta^2)(z^2-lambda^2)R(A,z^2).

The two factors need not generate comaximal ideals: after dividing by the first, substitution into the second gives (lambda^2-delta^2)R_1(lambda^2)=0, and the nonzero first factor can be cancelled in the domain.

## 2. The twofold annular lift, with framing fixed

For an annular framed link P and its twofold cyclic lift, the state-orbit argument gives

    <lift P>(A) = P(A^2,delta(A)) modulo 2.

Noninvariant state pairs cancel. Invariant states are lifted states downstairs; every contractible state circle lifts twice, whereas an essential annular state circle lifts once. The identity delta(A)^2=delta(A^2) modulo two supplies the coefficient substitution. This is the bracket version of [Melissa Zhang, AGT 18 (2018), Corollary 5](https://msp.org/agt/2018/18-2/agt-v18-n2-p18-p.pdf). The author is Zhang, not Cornish; the latter is cited in her paper for an earlier rank result.

For the preferred Sakuma construction, lifting c in the double cover branched over U gives two parallel pushoffs of kappa, with linking number zero. We also need their individual framings to be zero. Let c_push be the downstairs zero-framing push-off, and c_1,c_2 the two lifts. Linking transfer in the cyclic branched cover gives

    lk(c,c_push)=lk(c_1,(c_push)_1)+lk(c_1,(c_push)_2).

The left side is zero; the second term is the mutual linking of the preferred parallel pair, also zero. Thus the first term is zero, and the other component follows by the deck involution. Therefore the lifted framed link is the ZERO-framed two-parallel cable of kappa.

At the diagram-normalization level, one downstairs curl lifts to one curl on each component. If u=(-A^3)^w is the removed framing unit, then u(A)^2=u(A^2) modulo two. Thus the lift identity remains exact after the stated zero-framing choices; no unspecified unit is carried into the final value one.

## 3. Divide out the color-three dimension

Let s=delta(A)^2. Over F_2,

    delta(A^2)=delta(A)^2,
    lambda(A^2)=delta(A)^4.

Substituting (A^2,delta(A)) in the factorization therefore gives

    <two-parallel kappa>-delta(A)^2
       = (s-s^2)(s-s^4) R(A^2,s)
       = s^2(1-s)(1-s^3) R(A^2,s).

The skein identity z^2=e_2+1 for the Chebyshev/Jones-Wenzl basis gives

    <two-parallel kappa>=1+(delta^2-1)J_3(kappa).

Cancelling the nonzero polynomial s-1 in the Laurent domain gives

    J_3(kappa)-1 divisible by delta^4(1-delta^6).

Set q=A^4. In characteristic two,

    delta^4=q^-2(q+1)^4,
    1-delta^6=q^-3 Phi_3(q)Phi_5(q).

This proves the proposed colored congruence. Divisibility descends from F_2[A^+-1] to F_2[q^+-1] because the former is free over the latter with basis 1,A,A^2,A^3; comparing these components removes any possible extra A dependence in the quotient.

## 4. Color reflection at a fifth root, without a framing ambiguity

Use the cyclotomic expansion

    J_N(K;q)=sum_(k=0)^(N-1) H_k(K;q) C_(N,k)(q),
    C_(N,k)=product_(j=1)^k(q^N+q^-N-q^j-q^-j),
    H_0=1.

The H_k are integral Laurent polynomials independent of N. A primary research reference for this precise convention is [Garoufalidis-Le, Geometry & Topology 15 (2011), §3.2, equations (11)-(12)](https://people.mpim-bonn.mpg.de/stavros/publications/printed/asymptotics_of_the_colored_jones_function_of_a_knot.pdf), citing Habiro's cyclotomic theorem.

Modulo Phi_5 one has q^3+q^-3=q^2+q^-2. Consequently

    C_(3,1)=C_(2,1),   C_(3,2)=0,

and therefore J_3=J_2 modulo Phi_5, already over Z[q^+-1]. Combining with the colored congruence proves the ordinary Jones congruence modulo (2,Phi_5).

## 5. What this does and does not add

This is not a universal congruence for knots. In one conventional variable choice the trefoil has V=q+q^3-q^4, whose difference from one reduces to q^2 modulo (2,Phi_5), so it fails. Mirroring merely applies q inversion.

It is also not implied by a_2=0 alone. The figure-eight Jones polynomial is q^2-q+1-q^-1+q^-2, which reduces to Phi_5 times a unit and hence to zero in F_16. Thus the strongly invertible connected sum of a trefoil and a figure-eight has a_2=1-1=0 but Jones value zero in F_16, not one. This example may already be excluded by other project results; its role here is only logical independence from the a_2 test.

Part of the larger factor is universal and should not be advertised as new information: Habiro's first kernel for N=3 is

    q^-3(q^2-1)(q^4-1),

which in characteristic two is q^-3(q+1)^6. Thus the displayed (q+1)^4 factor is weaker than a universal factor. No claim is made here about independence of the Phi_3 factor. The Phi_5 conclusion is a nontrivial necessary condition, but it is only finite congruence data and is not a detection theorem.

No axis-swap equivalence was assumed. Only two scalar evaluations of the other annular class were used; its full polynomial remains undetermined.
