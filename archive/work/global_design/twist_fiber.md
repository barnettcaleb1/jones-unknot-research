# Repeated Jones values in a meridional twist family

2026-11-03. Elementary skein derivation, checked independently within the project. No novelty claim; the comparison with prior work on twisting is separate.

Independent main-agent read: Claude130248 checked the framing, generalized Vandermonde, integrality and tomography arguments; TRUSTED label retained. For w=0 the nonconstant bound is floor(r/2) integer parameters, including any chosen Jones-unit seed. These are not counts of distinct knot types.

## Setup and framing

Let P be a framed knot pattern in an unknotted solid torus, with oriented winding number w. Let K_n be the knot obtained by n meridional disk twists and then filling the solid torus in the standard way. Write its annular Kauffman bracket in the integral Chebyshev basis:

    [P]=sum_j p_j(A)e_j,        p_j in Z[A,A^-1].

Use delta=-A^2-A^-2, Delta_j=(-1)^j[j+1], and ribbon twist eigenvalue theta_j=(-1)^j A^(j(j+2)). In particular Delta_0=1, Delta_1=delta, theta_1=-A^3. If P has a diagram meeting a meridian disk in r points, only 0<=j<=r with j congruent to r modulo 2 occur; also r congruent to w modulo 2.

There is a fixed initial framing unit u, independent of n, such that

    V_(K_n)(A^-4)
      = (u/delta) theta_1^(-nw^2)
          sum_j p_j(A) theta_j^n Delta_j.                 (1)

The correction is nw^2, not the number of crossing strands. Under n-twist surgery, the linking number of P with its framed parallel changes by n times the product of their linking numbers with the surgery circle, namely nw^2. Equivalently, the annular ribbon Dehn twist includes the individual strand framing corrections absent from a raw full braid twist. Reversing the convention for a positive twist replaces n by -n and does not affect the conclusions.

Since j congruent to w modulo 2, the signs in theta_j/theta_1^(w^2) cancel. Thus (1) becomes

    delta V_(K_n)(A^-4)
      = u sum_j p_j(A)Delta_j A^(n c_j),
    c_j=j(j+2)-3w^2.                                    (2)

The integers c_j are strictly increasing in j. This absence of a parity-dependent eigenvalue sign is essential.

## Infinite repetition forces an annular scalar class

**Theorem.** Suppose V_(K_n)=F for infinitely many integers n, where F is a fixed normalized knot Jones polynomial. Then V_(K_n)=F for every integer n. Moreover exactly one of the following holds:

    w=0,       [P]=u^-1 delta F(A^-4)e_0;
    |w|=1,     [P]=u^-1       F(A^-4)e_1.

**Proof.** Infinitely many integer parameters have an unbounded positive or negative subsequence. In (2), the Laurent supports of different nonzero coefficients move with different slopes c_j. A nonzero coefficient with nonzero slope must eventually produce a highest or lowest exponent escaping the fixed support of delta F. Hence all such coefficients vanish. Equivalently, subtract the fixed target as an additional zero-slope channel and use eventual separation of distinct affine support intervals.

At most one channel can remain, and it satisfies

    j(j+2)=3w^2,
    u p_j Delta_j=delta F(A^-4).                          (3)

The apparent Pell-type possibilities with large j are excluded by integral specialization. At A=-1,

    Delta_j(-1)=(-1)^j(j+1),   delta(-1)=-2,
    F(1)=1,                   u(-1)=+/-1.

Since p_j(-1) is an integer, (3) forces j+1 to divide 2. Thus j=0 or 1. The resonance equation then gives w=0 or |w|=1, respectively, and (3) gives the asserted annular classes. Substitution in (2) proves equality for all n. QED.

For F=1 this recovers the scalar-vacuum or scalar-core conclusion. For general F, a Laurent-width divisibility argument would not suffice; the value F(1)=1 is what excludes all higher resonances.

This theorem concerns the skein class. It does not imply that P is geometrically local when w=0, or geometrically a core with a local knot when |w|=1. Those are separate detection questions.

## A finite repetition bound

Let S={c_j:p_j!=0} be the active exponent set, and put

    s=|S union {0}|.

**Finite-fiber bound.** Either the family is identically equal to F, or at most s-1 distinct integers n satisfy V_(K_n)=F.

**Proof.** If there were s distinct hits n_1<...<n_s, the coefficients of the s channels in the difference from the target would satisfy a homogeneous system with matrix

    M_(i,j)=A^(n_i c_j),       c_1<...<c_s.

This generalized Vandermonde matrix is invertible over Q(A). In its determinant, the identity permutation contributes the unique term of maximal A-degree, by the strict rearrangement inequality for the two strictly increasing integer lists. Therefore its determinant cannot vanish. All channel coefficients are zero, proving that the family is identically F. QED.

An analytic interpretation is also available: specialize A to a transcendental real number a>1. The difference is a real sum of at most s exponentials with distinct real exponents; Rolle induction bounds its number of real zeros by s-1. The algebraic proof needs no specialization.

If a meridian disk meets the pattern r times, there are at most d=floor(r/2)+1 allowed channels. Consequently a nonconstant family hits any fixed knot Jones polynomial at most

    d       times in general;
    d-1     times if |w|<=1.

For |w|<=1 the zero-slope channel is already among the d allowed channels, even if its coefficient happens to vanish. Thus d+1 repetitions always force a constant family, and d repetitions suffice when |w|<=1. The infinite-repetition theorem then classifies the surviving annular skein class.

**Twist tomography.** When w and a crossing bound r for a meridian disk are fixed, the Jones polynomials at any d distinct integer twists recover all d allowed annular coefficients u p_j over Q(A), by the same invertible matrix (and division by the nonzero Delta_j). Choosing the initial pattern framing to be zero recovers [P] itself; without that choice the fixed framing unit remains. This reconstruction is a statement about the full polynomials, not finitely many numerical Jones evaluations.

Checks on scope: a standard algebraic-intersection-zero two-point crossing disk has r=2,w=0, giving at most one occurrence unless flat. A coherent two-strand braid twist has r=2,|w|=2, allowing two occurrences; the two unknots in the corresponding two-strand torus-knot family illustrate why the two disk markings must not be conflated.
