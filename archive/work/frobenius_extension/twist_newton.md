# Twist families: a finite exceptional-parameter theorem

Theory-only conditional mechanism, 2026-11-03. No diagram computation and no application to an unconstructed Watson quotient. The proof is elementary; novelty is unassessed.

## 1. Precise hypotheses

Work over Q(A), with A transcendental. Suppose a specified scalar tangle coefficient x(n) is obtained from a FIXED finite tensor/contraction diagram, whose only n-dependent operators are

    T_j^(a_j n+b_j),       a_j,b_j integers,

and whose other maps are independent of n. Assume each T_j is diagonalizable over Q(A), with eigenvalues epsilon_(j,l) A^(k_(j,l)), where epsilon is +1 or -1 and k is integral. An additional nonzero scalar normalization u(n,A) may be arbitrary; it does not affect zeros.

These assumptions hold directly for ordinary two-strand twist regions, even when the full diagram has a much larger intermediate interface. They must be checked for the ACTUAL marked quotient diagram, not inferred from a rational presentation of the covering knot. They are not assertions about arbitrary braid operators.

Then, for each r in {0,1}, there are a fixed nonzero D_r(A) and a Laurent polynomial F_r(A,z) in Z[A^+-1,z^+-1] such that

    x(n)=u(n,A) F_r(A,A^n)/D_r(A),       n=r mod 2.     (1)

After rescaling u, integer coefficients are obtained by clearing all rational constants and Laurent denominators. If all eigenvalue signs in the varying powers are constant in n, one polynomial F suffices without the parity split.

## 2. Why the form exists

Write T_j=sum_l epsilon_(j,l) A^(k_(j,l)) P_(j,l), with fixed spectral projectors. Its integer power is

    T_j^(a_j n+b_j)
      =sum_l epsilon_(j,l)^(a_j n+b_j)
             A^(k_(j,l)(a_j n+b_j)) P_(j,l).

Expand the fixed finite contraction. This gives a finite sum

    x(n)/u(n,A)=sum_i c_i(A) sigma_i^n A^(v_i n),

where c_i is in Q(A), sigma_i is +1 or -1, and v_i is integral. On n=r modulo two, absorb sigma_i^r into c_i. Clearing the common denominator and setting z=A^n proves (1). Terms with identical exponent pairs must be combined before discussing Newton support.

For a two-strand Kauffman-bracket crossing, this requires no general semisimplicity theorem. With e^2=delta e, delta=-A^2-A^-2, and sigma=A I+A^-1 e,

    sigma^k=A^k(I-e/delta)+(-A^-3)^k e/delta,

for every integer k. Thus a full-twist region has eigenvalues A^2 and A^-6, both without signs. The fixed denominators introduced by these projectors are harmless over Q(A).

Diagonalizability matters. A Jordan block can introduce polynomial factors in n; its powers need not admit (1) with coefficients independent of n. Generic braid eigenvalues need not be monomials. Neither problem occurs for the displayed two-strand formula.

## 3. Newton-polygon obstruction to a zero

Fix one parity and assume F=F_r is nonzero. Write its fully combined Laurent expansion as

    F(A,z)=sum_(i,j) c_(i,j) A^i z^j,

with distinct exponent pairs and nonzero integer coefficients. Let P be the convex hull of its support. Specialization sends (i,j) to the A exponent i+n j.

**Theorem.** If F(A,A^n)=0 as a Laurent polynomial in A, then BOTH the maximizing and minimizing faces of P for the functional (i,j)->i+n j contain at least two support points.

Proof: a unique maximizing point would contribute a unique nonzero coefficient to the highest A exponent, which cannot cancel. The same argument applies to the lowest exponent. Since the specialized polynomial is zero, neither can occur.

Consequences:

- If P is two-dimensional, every possible exceptional n is the negative reciprocal slope determined by a pair of PARALLEL OPPOSITE supporting edges. An edge joining (i_1,j_1) to (i_2,j_2) gives the only candidate n=-(i_2-i_1)/(j_2-j_1), when j_2!=j_1. It must be integral and in the required parity/range.
- A two-dimensional polygon with no parallel opposite supporting edges gives nonvanishing for every n at once.
- If P is a segment, a zero can occur only when the functional is constant on that segment, so there is at most one candidate n. If P is a point, there is no zero.
- These are NECESSARY conditions. Even at a candidate edge slope, the edge coefficients may have nonzero sum, or a lower collapsed line may survive. No sufficiency claim is made.

Thus the family has only finitely many exceptional parameters on each nonzero parity branch, with a finite explicit candidate list read from the Newton polygon. This is a mechanism for turning an exact twist-family expression into a theorem, rather than a knot-table scan.

## 4. Algebraic root bound and an exact factor interpretation

Let d=max_j(j)-min_j(j), the z-exponent span of F. Multiply F by a z monomial to obtain a degree-d polynomial in z over Q(A). Distinct integers n give distinct elements A^n of Q(A). Hence there can be at most d integers for which F(A,A^n)=0.

Equivalently, each exceptional integer gives a linear factor z-A^n in Q(A)[z]. For the integral Laurent ring the kernel of evaluation z->A^n is generated by z-A^n; monic polynomial division proves the same factorization there after clearing a z monomial. Distinct exceptional parameters yield distinct factors. This explains the supporting-edge condition via the Newton segment of z-A^n, although the extremal-term proof above needs no Newton-product theorem.

A single exact nonzero anchor x(n_0) proves F_r is nonzero for the parity containing n_0. It does NOT prove the other parity branch nonzero. For example the formal expression 1-(-1)^n vanishes identically on even n and is nonzero on odd n. Without sign dependence, one anchor suffices for the single common F.

## 5. Scope for the proposed Sakuma family

This gives a usable conditional statement: once the actual preferred quotient for the fixed inversion of [2,-4n,2,2n] is expressed using a fixed finite collection of affine two-strand twist regions, and x(n) is extracted, one nonzero anchor per genuinely distinct parity branch prevents infinitely many exceptional n. Its Newton polygon may exclude every admissible n directly; otherwise it produces a finite exceptional list requiring separate mathematics.

This does not claim that the quotient has already been constructed, that F_r is nonzero, or that any resulting candidate is excluded. It does not turn a nonzero anchor into all-parameter nonvanishing without the Newton or factor step.

Preferred framing needs a precise distinction. A pure Reidemeister-I normalization factor (-A^3)^(w(n)), even with NONAFFINE w(n), is a nonzero scalar and cannot change the zero set, so it causes no problem in (1). A change of boundary marking that inserts actual extra twists into the relative tangle is different: if its exponents are nonaffine, or if it changes which coefficient is the flatness test, the stated one-variable form must be re-established. For example a genuine n^2 twist would naturally introduce an additional specialization variable A^(n^2). No such correction should be silently absorbed into a scalar unit.

All statements concern exact Laurent-polynomial vanishing at generic A, not values at a numerical root of unity. The finite-field fifth-root saturation theorem does not obstruct this mechanism, because the full A variable retains the degrees that distinguish the monomials.
