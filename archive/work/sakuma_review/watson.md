# Watson's invariant and the information in rational-closure Jones polynomials

Theory-only response to Claude 20261103-092928(ii). No computations or census searches.

## Source facts

[Watson, *Khovanov homology and the symmetry group of a knot*, arXiv:1311.1085v4](https://arxiv.org/pdf/1311.1085), Definition 10 and Proposition 11, constructs kappa from the inverse system A_n=Kh~(T(n)), with resolution maps f_n:A_(n+1)->A_n. He takes the inverse limit modulo sequences vanishing sufficiently far in the negative direction. Corollary 15 supplies eventual surjectivity on the positive end and injectivity on the negative end. Theorem 1 says kappa=0 exactly for the strongly invertible unknot. Its proof uses both positive and negative L-space surgeries once kappa vanishes.

An important coordinate correction: the integer closures of the trivial Watson tangle are the (2,n-1) torus links in the representative used in his proof, not all unknots. On our locus, closure polynomials agree with those of the rational twin; only particular closure subfamilies have Jones polynomial one.

[Snape's thesis](https://theses.gla.ac.uk/39015/1/2018SnapePhD.pdf), §4.3.2, Definitions 4.3.11 and Propositions 4.3.10–12, reviews this construction. Its §5.1 distinguishes the polynomial invariants from these detecting homological invariants; it does not give a detecting polynomial shadow of kappa.

## An exact information statement

Let R=Z[A^+-1]. For consistently marked and framed two-string tangles, the complete family of rational-closure brackets contains exactly the information of the rank-two relative bracket.

Indeed every rational closure is an R-linear functional on the skein module R id + R e. Conversely the two standard closures have pairing matrix, up to an interchange of conventions,

    [[1, delta], [delta, 1]].

Its determinant 1-delta^2 is nonzero in R. Hence equality of those two closures forces equality of bracket vectors; equality of bracket vectors forces equality of every rational closure. Division is unnecessary for this implication because R is a domain.

Consequently any invariant computed ONLY from the full marked closure-Jones family (with the consistent framing/orientation corrections) takes the same value on a flat tangle and its rational twin. Processing infinitely many such polynomials cannot manufacture an additional observable on that fiber. This does not prove that the fiber has a nonrational member, nor forbid a geometric proof that it does not. It identifies exactly where that proof would have to enter.

In particular, if a proposed Euler-characteristic shadow of kappa is computed from these polynomials alone, it cannot supply an independent test on our locus. Do not assume without proof that the Euler characteristic of the finite inverse-limit quotient is computable from the Euler characteristics of its terms: images, persistent subspaces, and infinite quotients require map data.

## A precise obstruction to an Euler-plus-exact-triangle argument

There is a simple formal model showing why merely appending the skein exact triangles to the polynomial family does not repair the loss of information.

Work after normalizing the gradings so the maps in the integer-indexed system have degree zero. Let (C_n^0,f_n^0) be the rational-tangle system in the derived category of graded vector spaces. Choose a finite nonzero complex H with zero differential and zero graded Euler characteristic; for example one generator in homological degree zero and one in degree one, at the same quantum degree. Form

    C_n'=C_n^0 direct-sum H,
    f_n'=f_n^0 direct-sum id_H.

Every term has the same graded Euler characteristic as before. Moreover

    Cone(f_n') = Cone(f_n^0) direct-sum Cone(id_H)
                is quasi-isomorphic to Cone(f_n^0).

Thus the meridional resolution object and the exact triangles remain unchanged, as do eventual injectivity/surjectivity. But the inverse-limit quotient acquires H: the constant identity system on H has inverse limit H, and none of its nonzero constant sequences vanishes on the negative end. Since the rational system has kappa=0, the modified formal system has kappa=H != 0.

This is NOT asserted to be the Khovanov system of a classical tangle. It is a countermodel to the inference from the stated algebraic data alone. Any successful argument needs a realizability restriction excluding such persistent Euler-invisible summands, or some additional geometric/categorical structure not included in that argument. The model is the persistence-module form of the already identified Euler-characteristic barrier, not a new knot counterexample.

## A genuine categorical target

The natural map-level replacement is a finite-composite vanishing statement:

> For the flat Watson tangle, some sufficiently long composite f_i f_(i+1) ... f_(j-1): A_j -> A_i is zero.

This is sufficient: every compatible sequence is then zero at i and hence at all indices below i, so kappa=0 and Watson's theorem detects the unknot. Conversely, eventual injectivity on the negative end and surjectivity on the positive end identify kappa with the image of such a composite once i,j lie beyond the two transition regions; so kappa=0 implies one of these composites is zero.

One can see that image description directly. Surjectivity on the positive end lets each class in A_j extend to a compatible positive tail. Its image in A_i gives the negative tail. Injectivity on the negative end makes a compatible sequence eventually zero there precisely when its A_i coordinate is zero. Quotienting by the eventually-zero sequences therefore leaves exactly the image of the middle composite.

This gives a complete conditional route:

    flat bracket + actual unknot closure
       -> [OPEN: a middle resolution-map composite vanishes]
       -> kappa=0
       -> underlying knot is U
       -> quotient tangle rational.

It is not a new proof mechanism by itself. Its advantage is precision: the missing object is a composition of actual saddle maps, rather than a further scalar combination of closure Jones polynomials. A decategorified quantity retaining traces or images of these maps would be additional input, not something reconstructed from their object Euler characteristics.

No assertion is made that ordinary closure polynomials determine the saddle maps, or that all formal systems satisfying these triangles are classically realizable.
