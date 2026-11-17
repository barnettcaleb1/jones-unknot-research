# Joint formal model: the all-order Alexander and loop gate

Bounded independent theory pass, 2026-11-03. No diagram-basis enumeration. Conclusion: the specified sequence satisfies the scalar Melvin–Morton–Rozansky and Rozansky rationality constraints to all orders, including their elementary integrality refinement. A completed primitive Jacobi-diagram lift and a graph-level rational Kontsevich lift must be distinguished.

## 1. The exact sequence

Write the parent's candidate without ambiguous subscripts:

    F_N(q) = 1 + (q+q^-1-2)
                   (q^N+q^-N-q-q^-1)
                   (q^N+q^-N-q^2-q^-2).                   (1)

For each integer N this is an integral Laurent polynomial. F_1=F_2=1, but it is not the constant sequence. It is invariant under N -> -N and q -> q^-1.

Set q=e^h. Its fixed-color expansion begins

    log F_N(e^h) = (N^2-1)(N^2-4) h^6 + O(h^8).           (2)

Every coefficient of h^d in log F is an even polynomial in N, vanishes at N=1 and N=2, and has degree at most d-2. To see the bound, each occurrence of F-1 has the color-independent factor 2cosh(h)-2, costing at least two h-degrees. In a term (F-1)^k, the degree in N is therefore at most d-2k. Odd h-coefficients vanish.

## 2. All scalar loop functions are Laurent polynomials

Treat z=q^N as an independent variable and put

    H=z+z^-1,       C(h)=2cosh(h).

Then the exact two-variable expression is

    F(z,h) = 1+(C(h)-2)(H-C(h))(H-C(2h)).                  (3)

It follows immediately that

    F(z,h) = sum_(r>=0) h^r P_r(z),
    P_r(z) in Q[z,z^-1],
    P_0=1,   P_1=0,
    P_2(z)=(z+z^-1-2)^2,                                 (4)

and every odd P_r is zero. In fact every P_r has Laurent degree at most two, because (3) is quadratic in H.

The MMR diagonal is consequently 1, consistent with Alexander polynomial Delta=1. The scalar rationality theorem writes loop coefficients as P_r(z)/Delta(z)^(2r+1), so every denominator requirement holds automatically here, to all orders. The formal and analytic versions of these statements, with normalization J_U,N=1, are stated in [Garoufalidis–Lê, Theorems 2–4](https://people.mpim-bonn.mpg.de/stavros/publications/analyticMMR.pdf).

This is not merely a low-order check. Formula (3) is an explicit all-order certificate. It also gives the expected small-angle analytic behavior: substitute h=alpha/N and z=e^alpha. Ordinary Taylor expansion of the entire functions C(h) and C(2h) gives the full 1/N expansion, uniformly for alpha in compact sets, and F_N(e^(alpha/N)) tends to 1.

An elementary integral refinement holds as well. Before replacing q by e^h, the expression

    1+(q+q^-1-2)(H-q-q^-1)(H-q^2-q^-2)

belongs to Z[q,q^-1,z,z^-1]. Its expansion at q=1 has coefficients in Z[z,z^-1], since negative integer powers of q have integral binomial expansions in q-1.

## 3. Taking the logarithm does not introduce scalar poles

Equation (3) has the form 1+h^2 Q(z,h), with Q in Q[z,z^-1][[h]]. Therefore

    log F = sum_(k>=1) (-1)^(k+1) h^(2k) Q(z,h)^k/k

still has a Laurent-polynomial coefficient in z at every h-degree. Only finitely many k contribute to any one coefficient. Rational denominators such as 1/k are harmless for a rational primitive diagram algebra.

Consequently neither the scalar loop expansion of F nor that of log F supplies an all-order obstruction to this candidate. This does not prove that arbitrary Laurent loop functions are realizable as graph-valued invariants.

## 4. Independent check of the parent's proposed primitive spanning argument

The following deduction is conditional on the Vogel-action input being checked by the other agent: a degree-one element t acts on the strut-free primitive Jacobi-diagram space and satisfies

    W_sl2(t D) = c W_sl2(D),   c != 0,                    (5)

where c is independent of the representation dimension N. The parent uses c=2; its precise nonzero normalization does not affect the argument.

Normalize the Kontsevich integral by the unknot under the connected-sum Hopf-algebra product before taking its logarithm. Let P_(2m) be the degree-2m primitive part of that logarithm for the zero-framed trefoil, and p_(2m)(N) its reduced sl2 weight. Its top N-degree coefficient is nonzero. Indeed

    Delta_trefoil(e^x)=cosh(3x/2)/cosh(x/2),

so MMR identifies that coefficient with

    [x^(2m)] (log cosh(x/2)-log cosh(3x/2)).               (6)

Every even positive-degree coefficient of log cosh(x) is nonzero; multiplying by 1-3^(2m) preserves nonvanishing.

At degree d>=2 the primitives

    t^(d-2m) P_(2m),    1<=m<=floor(d/2),                (7)

then have weight polynomials with distinct top N-degrees 2m. Each vanishes at N=1. They therefore form a weight-image basis of the space of even polynomials of N-degree at most d vanishing at N=1: that space has dimension floor(d/2).

Under input (5), every degree of log F can thus be lifted independently to a primitive diagram, and exponentiation gives a group-like element of the degree-completed diagram algebra with sl2 weight F. The order-one framing component is set to zero. There is no further compatibility condition between degrees for an abstract completed primitive series.

The normalization caveat matters: use a weight map multiplicative for connected sum and normalized to recover reduced J_N. Mixing an unnormalized quantum dimension with an ordinary trace would invalidate the direct logarithm statement.

## 5. The remaining, stronger rationality gate

Graph-level rationality is stronger than scalar rationality after applying sl2. Kricker's theorem represents each fixed-loop part by a finite linear combination of connected trivalent graphs with rational edge labels having Alexander-controlled denominators. For Delta=1 the allowed edge labels are Laurent polynomials. See [Kricker, Theorem 1.0.8](https://arxiv.org/pdf/math/0005284).

The degree-by-degree construction (7) does not by itself show that, after reorganizing by loop degree, infinitely many hair terms resum into such a finite beaded-graph expression. The scalar images resumming to Laurent polynomials does not force this: the weight map can erase graph-level information.

Thus the precise unresolved extension is:

> Does there exist a group-like, graph-rational Jacobi-diagram series with Delta=1 whose complete reduced sl2 weight is the exact sequence (1)?

No obstruction to that extension was identified in this pass, but no graph-rational lift was constructed. Even a positive answer would not show that the series is the Kontsevich integral of an actual knot. These are separate claims:

1. Integral colored sequence with scalar loop rationality: verified directly by (1)–(4).
2. Completed group-like primitive lift: follows from the independently verified Vogel-action hypothesis (5) and the triangular argument.
3. Graph-rational lift: not established here.
4. Actual knot realization: not established and not implied by the preceding formal conditions.

The candidate therefore survives all scalar Alexander/loop tests considered here. Claiming that those tests force J_2=1 to propagate to every color would contradict this explicit all-order model.
