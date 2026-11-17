# Exterior comparison: fixed-color probes miss the traceless classical fiber

Design pass, 2026-11-03. No computation. Conclusion: no qualified new Jones-to-exterior mechanism emerged, but there is a precise support obstruction to a tempting local-to-global bridge. It is sharper than the statement that drilling is not skein-linear. The proposed bridge would have to cross from the curves below to a different classical meridian fiber; ordinary Jones equality does not supply that continuation.

## 1. Filling probes live on explicit curves in the meridian base

Let M=E(K), R=C[A,A^-1], B=R[m], and S=S_R(M), with m acting by adding a boundary-parallel meridian. For each nonnegative integer j, fill M by the original solid torus and decorate its core by the j-th second-kind Chebyshev skein S_j. This defines an R-linear filling functional

    phi_j : S -> R.

Its value on the empty skein is the unreduced color-(j+1) Jones invariant, with the chosen zero framing. The standard encircling identity is

    phi_j(m*s)=lambda_j(A)*phi_j(s),
    lambda_j(A)=-(A^(2j+2)+A^(-2j-2)).                                    (1)

The meridian can be pushed into the filling torus and encircles only its colored core, so (1) applies to every exterior skein s, not merely the empty skein. The eigenvalue appears explicitly in [Bonahon-Wong, proof of Lemma 8](https://arxiv.org/pdf/1309.0921), PDF p.6. One may use the integral closed Chebyshev decoration rather than introduce Jones-Wenzl denominators.

Thus phi_j is B-linear if its target R is given the B-module structure

    R_j = B/(m-lambda_j(A)).

Each integral color probes the curve Gamma_j: m=lambda_j(A) in the two-dimensional meridian base Spec(B).

## 2. Exact support-separation lemma

The classical traceless fiber used by the Kronheimer-Mrowka endpoint is at

    p=(A+1,m).

For every fixed j, lambda_j(-1)=-2. Therefore m-lambda_j(A) takes the value 2 at p, is a unit in B_p, and

    (R_j)_p=0.                                                          (2)

Consequently every finite direct sum of integral-color filling targets localizes to zero at p. These probes cannot furnish an injective LOCAL comparison of a nonzero exterior module at the traceless point. This is independent of the knot and does not depend on whether its ordinary Jones polynomial is trivial.

The point is not that these invariants have no knot information. It is that their algebraic supports are the wrong ones for a direct localization argument at this particular detection fiber. At A=-1 the fixed-color curves all arrive at m=-2, the meridional trace-2 value, rather than m=0.

An elementary module countermodel makes the distinction explicit: B and B direct-sum B/p, with distinguished elements 1 and (1,0), have identical restrictions to every Gamma_j. The extra traceless-fiber summand disappears on each probe curve. This is not asserted to be a knot skein module; it refutes an inference based only on those restrictions. The extra summand is A-torsion, so an independently proved flatness condition could exclude this particular model, but not the next integrality obstruction.

## 3. Even integral values in every color need not imply regularity at p

Consider the rational function

    f(A,m)=(m+2)/(A+1).

It has a pole at p, since its numerator takes the nonzero value 2 there. But for every j>=0,

    f(A,lambda_j(A))
      = -(A^(j+1)-A^(-j-1))^2/(A+1)  belongs to R.                       (3)

Indeed A^(j+1)-A^(-j-1) vanishes at A=-1, so the numerator in (3) is divisible by (A+1)^2. Thus all integral-color restrictions are integral despite a pole at the precise classical point needed by the exterior argument.

This rules out the formal claim “integrality along all colored-Jones curves forces regularity across the meridian base.” Additional geometric control of allowed poles is essential. It does not refute stronger theorems for actual knot modules, whose realization conditions are extra data.

## 4. Root-of-unity shadows reinforce, but do not enlarge, the conclusion

For A a primitive 2N-th root with N odd, let T_N be the first-kind Chebyshev polynomial normalized by T_N(z+z^-1)=z^N+z^-N. Setting z=A^(2j+2) gives

    T_N(lambda_j(A))=-2.                                                 (4)

Here z^N=1 and T_N is odd. This is consistent with the published fact that the closed-surface WRT skein representation has the trivial classical shadow: [Bonahon-Wong, Theorem 2 / Theorem 14](https://arxiv.org/pdf/1309.0921).

Two qualifications are crucial. First, WRT classical shadow is a Chebyshev-central character at a fixed root; it is not the same object as a large-level WKB boundary holonomy. Second, colors growing with N can have lambda_j(A) approaching zero even while (4) remains true. Thus this is NOT a proof that all colored Jones data, or all levels together, cannot contain traceless geometry. It specifically blocks a direct finite-root shadow transfer and explains why fixed color and scaled color must not be conflated.

## 5. Quadratic rescaling separates the colors at the abelian point

The root agent proposed the following exact coordinate refinement. Write h=A+1, y=m+2, and introduce the chart

    y=h^2 z.

This is the quadratic rescaling chart, equivalently the h^2-chart of the blowup of the ideal (h^2,y). Put N=j+1. Along the color-N curve,

    z_N(h)=-(A^N-A^-N)^2/h^2

extends regularly across h=0 and satisfies

    z_N(0)=-4N^2.

Indeed A=-1+h gives A^N-A^-N=(-1)^N(-2Nh+O(h^2)). Thus the trivial color N=1 reaches z=-4 and the ordinary fundamental color N=2 reaches z=-16. The shifted coordinate -(z+4)/4 takes the limiting values N^2-1, matching the familiar quadratic Casimir dependence up to normalization.

All fixed colors approach the same point and tangent in the original meridian base; the quadratic rescaling separates them. In contrast, the traceless condition m=0 is z=2/h^2 and escapes every bounded-z part of this chart as h tends to zero. Consequently a regular fixed-color expansion does not by itself justify continuation into that regime. Colors growing as 1/h are a different scaling problem.

This is a coordinate lemma, not a theorem that the relevant quantum knot state extends across this blowup, and not a claim of novelty. In particular an equality only on the N=2 section does not determine a two-variable function on the chart: multiplication by z-z_2(h) already produces an invisible function. It makes the necessary nonuniform-color or off-section comparison explicit.

## 6. What a genuine revival would require

The earlier exterior theorem detects a nontrivial knot through a nonnilpotent commutator defect in S/((A+1),m). Equations (1)-(3) show why merely adjoining ordinary meridian encirclings, finitely many colors, or an integrality slogan does not deliver that certificate.

A proposed bridge must supply at least one genuinely new ingredient:

1. A geometric comparison family with an independently varying meridian parameter, regular near (A,m)=(-1,0), together with a derivation of its relevant relation from ordinary J_2=1; or
2. A geometric theorem forbidding the invisible support/pole defect on the Jones-unit locus, without assuming the desired exterior rank or commutator conclusion.

Neither ingredient was found. Equality along the fundamental-color curve alone cannot be analytically continued to the whole base: the nonzero factor m-lambda_1(A) already vanishes on that entire curve. Generic skein finiteness or q-holonomicity does not repair this without a specified additional equation and sufficient initial data.

Recommendation: bank the support-separation and hidden-pole calculations as scoped obstruction lemmas, with no novelty claim. Do not reopen the generic exterior/AJ route until a comparison map crosses the identified support gap. These calculations identify the missing structure more sharply; they do not create it.
