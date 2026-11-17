# Wrapping-two cut: hand audit of the algebra

2026-11-03. No computation or enumeration. This note audits Claude's 090406 letter under the explicitly stated annular cut conventions; it does not establish the width-six-to-wrapping-two geometry.

## 1. The encircling identity is correct

Use unreduced framed brackets, empty value 1 and unknot value

    d=delta=-A²-A^-2.

Let e_k be the Chebyshev basis of the annular skein. For the ordinary and encircled closures,

    F0(e_k)=Delta_k,
    F1(e_k)=Delta_k lambda_k,
    lambda_k=-(A^(2k+2)+A^(-2k-2)).

The identity Delta_k lambda_k=d S_k(lambda_1) gives

    F1(P)=d P(A,lambda_1),   F0(P)=P(A,d),
    lambda_1=2-d².

This special evaluation formula is valid; it does not make F1 injective.

## 2. Connectivity and the two closures

Assume an actual meridional disk meets the oriented pattern knot in exactly two points and its algebraic winding is zero. The crossings have opposite signs. After cutting, each of the two resulting arcs has both endpoints on one of the two disk copies: this is e-type connectivity. No extra closed components occur because the pattern was a single knot.

In the stated basis, id closes annularly to two core circles, while e closes to one contractible circle. Thus for [T]=x id+y e,

    P=x z²+y d,
    K=<K2>=d(xd+y),
    D=<D(T)>=d(x+yd),
    N=<axis union K2>=d[x(d²-2)²+yd].

Here the D closure caps each disk copy internally. Since the actual connectivity is e, it is a two-component link. These formulas are mutually consistent.

## 3. The bracket line and determinant consequence

With u the actual framing/writhe unit associated to the Jones normalization, the equation N=u d² is equivalent to

    x(d²-2)²+yd=ud.

It implies d divides x in Z[A,A^-1]. Indeed modulo d the factor (d²-2)² becomes 4, and Z[A,A^-1]/(d) is the domain Z[zeta_8]; multiplication by 4 has no kernel. Equivalently d is a unit times the irreducible cyclotomic polynomial A⁴+1.

Also

    det D(T)=|[D(T)/d]_(A=zeta_8)|
            =|x(zeta_8)|.

The bracket must be divided by d BEFORE evaluation. Because x has integer Laurent coefficients, x(zeta_8)=0 iff A⁴+1 divides x, iff d divides x. Hence the claimed equivalence with determinant zero is correct.

Writing x=d x' gives y=u-x'(d²-2)². This is the correct affine line of framed skein vectors. It is not a classification of actual tangles realizing the line.

## 4. Elimination is correct in brackets; the displayed t-sign is wrong

Direct substitution gives the exact identity

    (d²-3) K/d - (d²-4) D/d² = u.

For example, before imposing the line, its left side is

    x(d³-4d+4/d)+y = [x(d²-2)²+yd]/d.

For Jones polynomials choose compatible orientations on T's arcs, induced orientations on the two D components, and matching closure framings. The added axis has zero self framing and algebraic linking zero, so the closures can use a common writhe factor u. Then K=u d V_K and D=u d V_D, and

    (d²-3)V_K - (d²-4)V_D/d = 1.

Now put t=A^-4 and s=t^(1/2)+t^(-1/2), so d=-s. The correct t-form is therefore

    (t-1+t^-1)V_K
      + (t-2+t^-1)V_D/(t^(1/2)+t^(-1/2)) = 1.

The sign before the second term is PLUS. The minus sign in the letter fails already for T=e: K=U, D=U2, V_K=1, V_D=-s. With the plus sign the identity is 1; with the minus sign it is 2s²-7.

If arbitrary independent framings/orientations are used, their factors must be retained separately. The existence of some arbitrary Laurent unit is not itself the exact normalized Jones assertion: u must be the appropriate writhe/framing unit. In zero component framings and linking number zero, the encircled unlink equality is exactly N=d².

## 5. Rational cuts and the Whitehead calibration

If the cut T is rational, its D closure is two-bridge. Determinant zero identifies the unique rational slope whose D closure is the two-component unlink; in these marked conventions that is T=e, up to framing. Thus the rational-cut exclusion is valid.

The words 'twisted Whitehead doubles included' need scope. Rational clasp/twist patterns have rational cuts. A Whitehead double of a nontrivial companion can leave knotted companion strands in the cut ball, and its cut is not automatically rational.

For the proposed Whitehead vector

    x=1-A^-4,  y=A²,

the ordinary reduced closure is

    xd+y=A^-6,

an unknot bracket with writhe -2. The D reduced closure is

    x+yd=-(A⁴+A^-4),

the Hopf bracket. At A=zeta_8, x=2 and lambda_1=2, so the encircled link has determinant 8. This is consistent with the Whitehead link; it does not supply a band from Whitehead to U.

## 6. What Q2 and Q3 obtain from this algebra

If K2 is actually U, the normalized elimination identity forces V_D=d. More strongly K/u=d combined with the bracket line forces x=0 and y=u, because

    (K/d)-u = -(x/d)(d²-1)(d²-4).

The domain is integral and the displayed factors are nonzero. Thus we return to a flat tangle with one actual U closure. No strictly decreasing geometric complexity has been demonstrated: this is a self-reduction to the existing Lemma-Q situation.

For a general two-bridge K2, D inherits the displayed affine relation with V_K2, not the unlink polynomial. There is no automatically inherited flatness statement.

Finally x modulo d is a determinant/Fox-coloring, hence abelianized double-cover, datum. A diagram of the four arcs can compute it, but the conclusion det D=0 supplies homological dependence rather than an embedded separating disk. Promoting that condition to a planar disk statement requires additional geometry, not the algebra above.
