# Arithmetic bridges: exact translations and their missing input

17 November 2026. Bounded theory/source audit for the cross-field pivot. No knot enumeration. The elementary deductions below are written proofs, awaiting the collaboration's referee; no novelty claim is made.

## 1. An exact arithmetic translation: nonunits have a finite-field zero

**Lemma (elementary).** For P in Lambda=Z[t,t^-1], the following are equivalent:

1. P is a unit of Lambda, hence P=+/-t^k;
2. P(zeta_n) is a unit in Z[zeta_n] for every positive n;
3. P has no zero at a nonzero element of any finite field.

Proof. Units satisfy both conditions. Conversely multiply P by a monomial to obtain Q in Z[t] with nonzero constant term. A constant nonunit has a prime divisor and vanishes modulo that prime. If Q is nonconstant, choose a prime p not dividing its leading and constant coefficients. An irreducible factor of Q modulo p gives a nonzero root alpha in some F_(p^r), r<=deg Q. Let n be the multiplicative order of alpha, so p does not divide n. Alpha is a root of Phi_n modulo p, giving a homomorphism Z[zeta_n] -> F_(p^r) sending zeta_n to alpha. The image of P(zeta_n) is zero, so it cannot be a unit. Zero P is immediate.

For an ordinary normalized knot Jones polynomial, V(1)=1 and V'(1)=0 make a Laurent unit necessarily 1. Thus JC is exactly:

> Every nontrivial knot has a finite field F and alpha in F^* with V_K(alpha)=0.

Equivalently, the arithmetic scheme Spec Lambda/(V_K) is nonempty for every nontrivial knot. This differs from a witness that V_K(alpha) differs from 1: it asks for a zero of V itself.

**Assessment.** This is a genuine exact translation, but not yet a reduction: the lemma applies to every Laurent polynomial and supplies no geometric reason that V_K is nonunit. Its potential leverage would be a construction of a finite-field zero from geometric input (e.g. a representation of a knot group), independent of knowing the polynomial. No such construction is supplied here. A proposal that merely evaluates more roots has not crossed this gap.

The proof is effective after the polynomial is known. If its shifted degree is D>0 and coefficient height is H, any prime p>H supplies some root in an extension of degree at most D, hence a cyclotomic witness of order at most p^D-1. This is an elementary bound, not an efficient algorithm from a knot diagram.

## 2. Finite probes and Mahler measure: clear limits

If P-1 has Laurent span D and P(zeta_n)=1 for one primitive root of each order n in a finite set S, then product_(n in S) Phi_n divides P-1 after a monomial shift. Hence sum_(n in S) phi(n)>D forces P=1. Height is unnecessary for exact characteristic-zero evaluations. If evaluations are only modular, coefficient bounds or additional primes are needed to reconstruct a characteristic-zero conclusion.

This interpolation is useful for certificates but does not give a uniform finite set of probes for unknown degrees. Formally, 1+Q(t) product Phi_n(t)^e_n passes any prescribed finite collection of root values/jets. These are formal Laurent polynomials, not asserted Jones polynomials. Our FT-DEEP result independently rules out a uniform finite initial jet for actual J in its stated domain; it does not automatically rule out every finite collection of distinct roots for actual knots.

Mahler measure alone is already defeated by the figure-eight: V_4_1=t^-2 Phi_10 has measure 1 and is nonconstant. Kronecker-type conclusions allow cyclotomic factors, exactly what this example uses. Replacing equality by algebraic-unit evaluations at all roots removes that example but returns to the elementary lemma above; a finite list still leaves a realization problem.

## 3. Habiro integrality does not propagate one color into all colors

Habiro's cyclotomic completion has injective Taylor expansion at every root of unity (Theorem 5.4), and suitable infinite root-value families determine an element (Theorem 6.1). These are uniqueness results for the whole completed invariant, not recovery from one finite coefficient or one color. [Habiro, *Cyclotomic completions of polynomial rings*, §§5–6](https://arxiv.org/pdf/math/0209324).

In the normalization J_n(U)=1, the integral Habiro coefficients H_k satisfy

    J_n(q) = sum_(k>=0) c_(n,k)(q) H_k(q),
    c_(n,k) = q^(-kn) (q^(n+1);q)_k (q^(n-1);q^-1)_k,

where c_(n,k)=0 for k>=n. Thus H_0=1 and

    J_2=1  iff  H_1=0.

The whole coefficient sequence is equivalent to the colored Jones sequence, by triangular inversion. These formulas and integrality are recorded in equations (2)–(4); Proposition 2.2 gives the equivalence with descendant/root-value families. [Garoufalidis–Kashaev, *The descendant colored Jones polynomials*, §2](https://people.mpim-bonn.mpg.de/stavros/publications/descendants.colored.jones.pdf).

**Formal obstruction, proved here.** Fix r>=2. Set H_0=H_r=1 and all other H_k=0. The resulting finite colored Habiro element is integral, all of its root specializations and Taylor expansions are compatible, and its color sequence is q-holonomic (it is a finite Laurent polynomial in q and q^n). It has

    J_2=...=J_r=1, but J_(r+1)=1+c_(r+1,r) != 1.

Therefore integrality, cyclotomic compatibility and q-holonomicity alone cannot prove even J_2=1 => J_3=1. The proposed first bridge theorem must use a geometric admissibility constraint on actual H_k, not these formal structures alone. The smallest precise target is “H_1(K)=0 implies H_2(K)=0”; even that is an open new implication, not a consequence of the completion. A stronger proposed divisibility H_1 | H_k must be tested before use and is not asserted.

This gives a concrete cheap falsifier for an arithmetic proof proposal: apply it to the finite H_0=H_2=1 model. If it still concludes H_2=0, it has silently assumed realization or used a false algebraic implication.

## 4. The colored ladder is not a solved endpoint

Do not invoke an old announcement that the complete colored Jones sequence detects the unknot. The current K3 problem list explicitly asks whether a nontrivial knot can have all colored Jones polynomials trivial (Problem 1.24(b)); its nearby discussion treats volume conjectures as a possible route, not an available theorem. [Baykur–Kirby–Ruberman et al., *K3: A New Problem List in Low-Dimensional Topology*, pp.31–33](https://math.berkeley.edu/sites/default/files/surv-295-ruberman-watermarked-author-pdf.pdf).

Thus a route through H_1=0 => H_k=0 for all k would still have a second open endpoint: detection by all colors. Categorified colored detection does not supply this decategorified endpoint. The distinction matters before investing in a color-propagation program.

## Recommendation

Arithmetic supplies two useful deliverables now: the finite-field-zero formulation and the explicit formal obstruction to color propagation. Neither yet reduces JC to a known arithmetic theorem. Prioritize a geometric source for the arithmetic zero, or a concrete realizability identity among the first Habiro coefficients. Treat an unrestricted “Habiro rigidity” claim as empty until it excludes the finite H_0=H_2 model. The newer Garoufalidis–Wheeler lift to an Alexander-localized Habiro ring is relevant literature to inspect next, but no detection consequence is imported from its abstract. [*A lift of the colored Jones polynomial of a knot* (2026)](https://arxiv.org/abs/2603.01619).
