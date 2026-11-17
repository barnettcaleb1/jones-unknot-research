# A regularity lemma for uniformly bounded color expansions

2026-11-03. Written proof and independent internal algebra check. No novelty claim. This gives a positive formal statement, but neither a Jones-to-exterior comparison nor unknot detection.

## Statement

Let h,y be independent formal variables and let f belong to C[[h,y]][h^-1]. For each positive integer N substitute

    y_N(h)=-4*sinh(Nh)^2.

Suppose every resulting f(h,y_N(h)) is in C[[h]], and for every k>=0 its h^k coefficient, as a function of N, is a polynomial of degree at most k. Then f belongs to C[[h,y]]: it has no vertical h-pole.

Conversely every f in C[[h,y]] has these two properties. Thus, within the stated finite-pole class, uniform color triangularity is precisely regularity in these local coordinates.

## Proof

Write f=h^-r F, with r>=0, F in C[[h,y]], and if r>0 choose the representation with F(0,y) nonzero. Let b be the smallest exponent with c=[h^0 y^b]F nonzero. The term c y^b contributes

    c*(-4)^b*N^(2b)

to the coefficient of h^(2b-r) after substitution.

A term h^a y^j with a>0 contributing to this same h-power has N-degree at most 2b-a, strictly less than 2b: each coefficient of h^ell in y_N(h)^j is a scalar times N^ell. Terms with a=0 and j<b are absent by definition; terms with a=0,j>b cannot reach this h-power. Therefore this coefficient is a nonzero polynomial in N of degree exactly 2b.

If 2b-r<0, it contradicts regularity of all samples: a nonzero polynomial cannot vanish at every positive integer N. If 2b-r>=0 and r>0, it contradicts the assumed degree bound because 2b>2b-r. Hence r=0.

Conversely, in a term h^a y^b with a>=0, a contribution at h^k has N-degree k-a<=k. There are only finitely many contributing pairs a,b at each h-order because y_N has order two. This proves the converse and the validity of the formal substitution. QED.

## Why these are the meridian coordinates

Put A=-exp(h) and let m denote the boundary-meridian skein action. The color-N encircling eigenvalue is

    lambda_N(A)=-(A^(2N)+A^(-2N))=-2*cosh(2Nh).

Thus y=m+2 samples exactly y_N=-4*sinh(Nh)^2. All fixed colors approach the abelian meridian point m=-2. In the quadratic chart y=h^2 z they separate at z=-4N^2. The traceless meridian m=0 instead requires z=2/h^2, outside the bounded-z chart.

The usual MMR triangular bound is stated in a logarithmic Jones parameter; rescaling that parameter by a fixed nonzero constant does not affect the degree bound. The lemma makes the regularity content of a UNIFORM-in-color bound explicit. One fixed color cannot supply it.

## Scope and relation to the preceding countermodels

The function (m+2)/(A+1) in skein_bridge_design.md is integral on every fixed-color curve but has a vertical pole. It fails the uniform triangular bound: in logarithmic coordinates its first nonzero coefficient has N-degree two at h-order one. Thus MMR supplies genuinely stronger information than integrality alone. Do not use that rational function as a countermodel to the combined hypotheses of this lemma.

The repaired sequence in colored_propagation.md DOES obey the uniform triangular bound and loop-rationality shape while having F_1=F_2=1 and F_3!=1. Therefore the positive regularity lemma still does not imply color propagation.

Nor does it imply regularity along all meridional divisors, convergence near m=0, a comparison with the entire knot-exterior skein module, absence of invisible module summands, or reflexivity of that module. Those are separate geometric conditions. In particular the module B direct-sum B/(A+1,m) used in the support countermodel has a different kind of defect from a vertical pole in a scalar function.

Finally, regularity does not make two section values determine a function. If f(h,y_1(h))=f(h,y_2(h))=1, formal division in C[[h]][[y]] gives

    f-1=(y-y_1(h))*(y-y_2(h))*g(h,y)

for some g. Divide by the first monic factor, evaluate at y_2, and cancel the nonzero series y_2-y_1 in the domain C[[h]] to obtain the second factor. The undetermined g is the local algebraic freedom that a geometric argument must control. This factorization is not an additional constraint on actual knot realizations beyond the corresponding colored-data identities.
