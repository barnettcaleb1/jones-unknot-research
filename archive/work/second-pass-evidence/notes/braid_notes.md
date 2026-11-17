# Exact exclusion of an infinite Bigelow-kernel family

This bounded investigation does not settle whether the Jones polynomial detects the unknot. It rules out a specified two-parameter family for every integer value of its parameters, using exact polynomial arithmetic and a finite algebraic certificate. No novelty claim is made.

## Family and result

Write braid words from left to right and use `[x,y]=xyx^{-1}y^{-1}`. In `B_5`, put

```
psi1 = sigma3^-1 sigma2 sigma1^2 sigma2 sigma4^3 sigma3 sigma2
psi2 = sigma4^-1 sigma3 sigma2 sigma1^-2 sigma2 sigma1^2 sigma2^2 sigma1 sigma4^5
H = psi1^-1 sigma4 psi1
F = psi2^-1 (sigma4 sigma3 sigma2 sigma1^2 sigma2 sigma3 sigma4) psi2.
```

Let `alpha = sigma1^e1 sigma2^e2 sigma3^e3 sigma4^e4`, where each `ei` is `+1` or `-1`. Let `c` be the identity or any of the eight single letters `sigma_i^{+/-1}`, `1 <= i <= 4`. For integers `m,n`, consider

```
K(m,n;alpha,c) = closure( [H^m,F^n] c alpha c^-1 ).
```

There are 16 choices of alpha and nine choices of c. The exact certificate establishes, for all 144 choices,

```
V_K = 1  if and only if  m=0 or n=0.
```

When either exponent is zero the commutator is the identity, and the closure is an unknot. Each signed Coxeter anchor alpha destabilizes successively to the one-strand unknot. For all exponents the displayed closures are knots: F is pure, the commutator is pure, and each anchor has a five-cycle permutation.

Bigelow gives the two conjugated factors on page 403 of his 1999 paper. His page-399 convention is `[x,y]=x^{-1}y^{-1}xy`, so his displayed commutator is the member `m=n=-1` of our convention. The certificate checks Burau triviality directly; it does not depend on a word-length claim. Source: [Bigelow, *The Burau representation is not faithful for n=5*, Geometry & Topology 3 (1999), 397–404](https://doi.org/10.2140/gt.1999.3.397), [author's PDF](https://web.math.ucsb.edu/~bigelow/publications/02.pdf). [Sage's braid documentation](https://doc.sagemath.org/html/en/reference/groups/sage/groups/braid.html) independently gives the same factors with our commutator convention.

## Why four polynomial evaluations control every pair of powers

Use the Kauffman-bracket conventions

```
delta = -A^2-A^-2,  rho(sigma_i)=A I + A^-1 e_i,
t=A^-4,  V(closure(beta))=(-A)^(-3w(beta)) bracket(closure(beta)).
```

The generic Temperley–Lieb algebra on five strands has components of dimensions 1, 4, and 5. Here the four-dimensional component is the reduced Burau representation after multiplying each generator by A and putting `t=A^-4`. We avoid relying only on that identification: `tl5_block.py` checks the following trace formula on all 42 diagram basis elements, so it holds on the entire algebra by linearity:

```
bracket(closure(beta)) =
 (delta^4-4 delta^2+3) A^w
 +(delta^2-2) A^w tr(Burau_reduced(beta; A^-4))
 +tr(rho_5(beta)).
```

The five-dimensional module is built explicitly from the five noncrossing link states with one through strand. The certificate checks its Temperley–Lieb relations and the full 42-element trace identity with integer Laurent-polynomial entries.

Direct exact Burau multiplication verifies that H and F commute in the Burau representation. Therefore every commutator `[H^m,F^n]` acts trivially in the one- and four-dimensional components, and its difference from the identity can affect the closure polynomial only through the five-dimensional component. The two exact matrix identities in that component are

```
(rho_5(H)-A I)(rho_5(H)+A^-3 I)=0,
(rho_5(F)-I)(rho_5(F)-A^-8 I)=0.
```

Over `Q(A)` the eigenvalues in each identity are distinct. Consequently there are fixed idempotents P,Q such that, up to a scalar that cancels inside the commutator,

```
rho_5(H^m) = scalar * (I+(x-1)P),  x=(-t)^m,
rho_5(F^n) = I+(y-1)Q,             y=t^(2n).
```

This holds for negative exponents as well, since `(I+(x-1)P)^-1=I+(x^-1-1)P`. Multiply the commutator minus I by xy. Its entries are polynomials of degree at most two separately in x and y. They vanish identically at x=1 and at y=1, so each is divisible by `(x-1)(y-1)`. Taking the normalized closure trace with a fixed suffix gives

```
V_K-1 = ((x-1)(y-1)/(xy)) * (a xy+b x+c y+d),
```

where a,b,c,d are fixed rational functions, independent of m,n. Four exact Jones evaluations at `(m,n)=(1,1),(1,-1),(-1,1),(-1,-1)` recover these four coefficients. The implementation clears denominators explicitly, using a fixed nonzero Laurent polynomial. No numerical interpolation or root-of-unity specialization occurs.

For nonzero m,n neither prefactor factor vanishes in `Q(t)`. Jones-one is therefore equivalent to the Laurent-polynomial identity

```
a(t)(-t)^m t^(2n) + b(t)(-t)^m + c(t)t^(2n) + d(t) = 0,
```

where now a,b,c,d denote the denominator-cleared Laurent polynomials saved in the certificate.

## A leading-degree proof for every nonzero exponent pair

The exact coefficient calculation has a particularly simple consequence: in each of the 144 rows, all four nonzero Laurent polynomials a,b,c,d have the same highest degree, say d0. Their leading coefficients are respectively a nonzero multiple of `(1,-1,-1,1)`; the observed multiplier is -1, 1, or 2. Only the equal degrees and nonzero coefficients are needed below.

The four summands in the cleared identity therefore have highest exponents

```
d0+m+2n,  d0+m,  d0+2n,  d0.
```

When m and n are both nonzero, exactly one is largest. Indeed, the largest shift is `max(m,0)+max(2n,0)`, attained by the unique choice of including each positive contribution and excluding each negative contribution. The corresponding leading coefficient is nonzero, including the possible factor `(-1)^m`. No other summand can cancel it. Thus the cleared polynomial cannot vanish for any nonzero pair, with no bound on the exponents.

The verifier recomputes all four coefficients for every row and explicitly checks that their highest degrees agree. This elementary argument is the core all-integer exclusion proof; no root-solving algorithm is required for it.

## Optional independent integer-root audit

The exponent shifts of these four summands have respective weights `(1,2),(1,0),(0,2),(0,0)`. If a nonzero Laurent sum vanishes, its highest exponent must occur in at least two summands. Thus every root lies on one of at most six affine integer lines

```
(weight_i-weight_j) dot (m,n) = degree(p_j)-degree(p_i).
```

Discard lines without integer points and parameterize each remaining line by one integer. Split into two parity classes when necessary to make `(-1)^m` constant. Along each resulting line, combine all terms with the same exponent slope. If all groups cancel, the whole line is a root family. If only one group remains, it has no roots. Otherwise a second highest-exponent tie between groups with distinct slopes gives finitely many parameter values, which are evaluated exactly. This is exhaustive, including negative and arbitrarily large exponents. The code also handles identically zero coefficients and whole-plane solution sets.

As an additional audit, this procedure finds that all 144 cleared polynomials have no integer roots and no affine-line solution families, including on the axes. It performs 576 exact one-variable candidate checks. The axis cases `m=0` or `n=0` of Jones-one arise from the prefactor. This stronger observation about the cleared polynomials is unnecessary for the leading-degree proof.

## Verification and limitations

The portable directory contains only Python standard-library code and JSON data. Run:

```
python3 braid_certificate/verify.py
```

The verifier checks familiar knot polynomials and braid identities; checks the Burau kernel; checks all 42 TL basis traces and the two matrix quadratic identities; independently recomputes the 576 sample Jones polynomials and recovered coefficients; compares them with the saved certificate; and checks equal highest degrees for the leading-degree proof. Extra exponents test the four-sample recovery formula against the full Jones calculation. Add `--audit-solver` to repeat the independent exhaustive integer-root audit as well.

The seed `[H,F] sigma1 sigma2 sigma3 sigma4` is already far from Jones-one: its polynomial has t-degrees -33 through 38 and a largest coefficient of absolute value 90,424,762. Burau-kernel membership is therefore not Jones-kernel membership.

The result covers only these specific factors, 16 anchors, and nine conjugating contexts. It says nothing universal about all Burau-kernel insertions, all braids, or all knots. It excludes this infinite family as a source of a counterexample; it does not prove the Jones unknot-detection conjecture.

## Separate audit: Lobb's ribbon-twist theorem

[Lobb, *The Kanenobu knots and Khovanov–Rozansky homology*, arXiv:1105.3985, Theorem 1.4](https://arxiv.org/abs/1105.3985) applies to a knot with a one-ribbon presentation: surgery on the chosen band gives the actual two-component unlink. Twisting that ribbon by p half-twists gives

```
H_n(K_p)=H_n(U) direct_sum M_n(K_p),
M_n(K_(p+2))=M_n(K_p)[2]{-2n}.
```

An actual unknot seed makes the complementary summand zero, so the same-parity twisting orbit has the unknot's reduced sl2 homology and consists of unknots by Khovanov unknot detection. For two independent one-ribbon sites, the shifts cancel under opposite full twists. To apply this to a Watson-type construction, one must verify geometrically that each relevant band smoothing is an actual unlink; its Jones polynomial alone does not verify that hypothesis. A second seed or a further theorem is needed to cover the other parity class.
