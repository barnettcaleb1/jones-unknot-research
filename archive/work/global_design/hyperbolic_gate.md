# Hyperbolic gate: exact Jones preservation versus imitation

2026-11-03. Bounded primary-literature/theory pass; no knot enumeration. One conditional exact construction is recorded below, and it is already a known representation-kernel route. No unconditional reduction of Jones unknot detection to hyperbolic knots was established.

## 1. What is actually reduced for free

Prime knots suffice. If K=K1#...#Kr and V_K=1, multiplicativity in Z[t,t^-1] makes every V_Ki a Laurent unit. The identities V_Ki(1)=1 and V'_Ki(1)=0 make each unit exactly 1. Thus any counterexample has a nontrivial prime counterexample among its summands.

There is also an immediate exact reduction to ribbon knots, but not to hyperbolic ribbon knots: K#mirror(K) is ribbon and has Jones polynomial V_K(t)V_K(t^-1). If V_K=1 and K is nontrivial, this is a nontrivial ribbon counterexample. It is composite, so this construction does not solve the hyperbolic step.

Prime torus knots cannot be counterexamples, for example because a2(T(p,q))=(p^2-1)(q^2-1)/24 is nonzero for nontrivial torus knots and V''(1)=-6a2. The residual alternatives are a hyperbolic prime counterexample or a prime satellite counterexample. Eliminating the second alternative requires a new argument; prime decomposition does not do it.

## 2. The hyperbolic imitation theorem does not preserve Jones

[Silver--Whitten, *Hyperbolic covering knots*, Theorem 2.2](https://arxiv.org/html/math/0503152v2) produces, for any knot K, hyperbolic knots with arbitrarily large volume, a meridian/longitude-preserving group epimorphism onto the group of K, the same Alexander invariant, and ribbon concordance to K. Their operation adds crossing-local unknotted staples and performs sufficiently long Dehn fillings. Its Alexander argument places the staples in the second commutator subgroup. This is an exact abelian-invariant statement, not an exact Jones identity.

Ribbon concordance alone cannot supply that missing identity: every ribbon knot is ribbon concordant to U, and ribbon knots with nontrivial Jones polynomial are elementary examples. The theorem itself supplies no control of the bracket effect of a staple. Nor can its arbitrary-volume conclusion be combined with a finite-order agreement theorem by simply taking a limit: the output knot changes with the prescribed order.

This also specifies what is missing from an appeal to Kawauchi imitation. The primary imitation-based statements inspected preserve Alexander information or selected HOMFLY coefficients, not the full Jones polynomial. No claim is made that imitation is fundamentally incapable of exact preservation, only that the cited theorems do not provide it.

## 3. Even very strong polynomial approximation leaves the required tail

[Ito, *Knots whose braided satellite have the same HOMFLY polynomial up to given z-degrees*, Theorem 2 and Proposition 1](https://arxiv.org/html/2410.12344v1) gives infinitely many hyperbolic outputs matching any prescribed finite list of HOMFLY coefficient polynomials, simultaneously for bounded-winding braided satellites. The construction multiplies a fixed braid by deep pure-braid commutators; pseudo-Anosov dynamics and large fractional Dehn twist coefficient give hyperbolicity. The construction deliberately produces unbounded genera.

Write P(v,z)=sum_j P^(2j)(v) z^(2j). Agreement through j=N gives only

    P_out(v,z)-P_in(v,z) = z^(2N+2) R(v,z).

After the Jones substitution v=t and z=t^(1/2)-t^(-1/2), the factor on the right is not zero. A nonzero tail may therefore remain. To infer exact equality one needs an independent upper bound killing all higher z-degrees, or a separate identity forcing R to vanish under the Jones substitution. Neither follows from bounded braid index, nor is either asserted by Ito's theorem.

The quantifier issue is essential:

    for each N there is a hyperbolic H_N with order-N agreement

does not imply a single hyperbolic H has agreement at all orders. This is the precise failure of the approximation-to-exactness proposal.

## 4. Standard exact mutation cannot perform hyperbolization

This route is actually excluded, rather than merely missing an estimate. [Dunfield--Garoufalidis--Shumakovitch--Thistlethwaite, *Behavior of knot invariants under genus 2 mutation*, Section 2.3 and Theorem 2.4](https://nyjm.albany.edu/j/2010/16-7p.pdf) explain Ruberman's theorem including compressible symmetric surfaces: mutation of a hyperbolic manifold along the relevant symmetric surfaces remains hyperbolic. Mutation is reversible. Consequently neither Conway mutation nor genus-two mutation can turn a nonhyperbolic knot into a hyperbolic knot. Sequences of these mutations have the same limitation.

This is stronger than saying that Gromov norm is preserved: a satellite can have positive Gromov norm, so that numerical equality alone would not exclude hyperbolization. The preservation of hyperbolicity in both directions is the relevant theorem.

## 5. Watson's paired extensions: an exact identity with the wrong anchor

[Watson, *Any tangle extends to non-mutant knots with the same Jones polynomial*, Sections 4--7](https://personal.math.ubc.ca/~liam/files/preprint.pdf) uses a bilinear bracket evaluation

    br(T) M br(U)^t,
    M = [[v_figure-eight(A)^2, delta], [delta, delta^2]],

preserved by opposite boundary twists of T and U. Suitable prime tangles yield prime, non-mutant extensions sharing this value. The theorem neither equates that value with a chosen closure of T nor guarantees hyperbolicity.

An algebraic check isolates the missing anchor: det M=delta^2(v_figure-eight^2-1) is nonzero, while a product of two selected closure measurements is represented by a rank-one matrix. Thus the full bilinear functional is not determined by that product. Jones-triviality of selected input closures does not itself make the extension value one. A geometric subclass could add further identities, but those are additional hypotheses requiring proof.

The Kanenobu examples show exact Jones-preserving changes can alter prime/composite and hyperbolic status in particular families. They do not give a universal operation on an arbitrary input knot. Root is investigating the corresponding band-twist formula separately; no broad extension is inferred here.

## 6. The one precise exact hyperbolization route

The known conditional construction is [Ito, *A kernel of a braid group representation yields a knot with trivial knot polynomials*, Theorem 1 and Corollary 1](https://arxiv.org/html/1402.2028v1).

If the relevant quantum braid representation has a nontrivial kernel, its normal-subgroup structure supplies pseudo-Anosov kernel elements with large Dehornoy order. Multiplying a braid alpha by suitable such elements beta gives hyperbolic closures, while

    rho(alpha beta)=rho(alpha)

preserves the quantum trace. Ito states the resulting conclusion directly for any prescribed input knot: infinitely many hyperbolic knots with the same quantum invariant. Applied to the ordinary Jones representation and the unknot, this gives hyperbolic Jones-trivial knots.

The full Jones/Temperley--Lieb representation is required. A kernel in one Burau or cell-module summand does not make its whole quantum trace unchanged. Thus this is a real end-to-end construction, conditional on a specific algebraic input, but it is the existing faithfulness obstruction already on the board. It is not a new reduction obtainable from an arbitrary hypothetical Jones-trivial knot: scalar trace equality does not produce a representation kernel element.

## Verdict

Bank the exact prime reduction and the mutation no-go. Do not promote hyperbolic imitation, finite-type approximation, ribbon concordance, or Watson's paired extension theorem to an exact Jones-preserving hyperbolization theorem. The inspected primary literature leaves the arbitrary prime-satellite counterexample case untransferred. The only complete conditional hyperbolization mechanism found is Ito's existing full-representation-kernel route.
