# Generic braid and trace audit (2026-10-31)

This bounded pass did not find a knot counterexample or prove Jones unknot detection.
It checked the logical reach of the representation route and independently audited
the two-tangle algebra lemma. No novelty is claimed for the observations below.

## Current primary sources

1. Stephen Bigelow, *Does the Jones polynomial detect the unknot?*,
   https://arxiv.org/html/math/0012086 . Proposition 1.5 connects faithfulness of
   Burau, Temperley--Lieb, and the Hecke/Jones representation for B4. The proposed
   construction from a nonzero representation kernel was conditional in this paper.
2. Tetsuya Ito, *A kernel of a braid group representation yields a knot with trivial
   knot polynomials*, https://arxiv.org/html/1402.2028 . Theorem 1 establishes the
   normal-subgroup construction: if H is nontrivial, noncentral, and normal in B_n,
   and alpha closes to the unknot, then alpha H contains braids closing to hyperbolic
   knots of arbitrarily large genus and braid index n. In particular, a nonfaithful
   generic Jones/TL representation really would give Jones-trivial nontrivial knots.
3. Vasudha Bharathram, Joan S. Birman, Tara E. Brendle, *The Burau representation is
   faithful for n=4*, https://arxiv.org/html/2607.05283v2 , September 14, 2026.
   This recent preprint claims a proof of B4 Burau faithfulness and hence B4 Jones
   faithfulness. I verified the source and statement, not its entire 28-page proof.
   Accordingly, the classic B4-kernel search should not be treated as a currently
   unobstructed route. Even a valid faithfulness theorem would not establish Jones
   detection of the unknot among closed four-braids: equality of scalar traces is
   weaker than equality of matrices.

## Exact two-braid demonstration of the trace gap

Use R=Z[A,A^-1], delta=-A^2-A^-2, e^2=delta e, and

    rho(sigma)=A*1+A^-1*e.

For a braid beta of writhe w, set

    R(beta)=(-A)^(-3w)rho(beta).

The Jones polynomial of the closure is the closure functional applied to R(beta),
with a single circle normalized to 1. Thus

    R(sigma)   = -A^-2*1 - A^-4*e,
    R(sigma^-1)= -A^2*1  - A^4*e.

Both sigma and sigma^-1 close to an unknot; both scalar evaluations are 1, but the
two algebra elements differ. Moreover, appending the same context sigma^2 produces
sigma^3 (a trefoil) and sigma (an unknot). Their Jones polynomials are respectively

    A^-4 + A^-12 - A^-16,   1.

Consequently, equality of closed Jones polynomials cannot be used as a local
operator replacement rule. This is already false for the faithful B2 representation.

## Positivity pinpoints the missing equality case

For fixed n, normalize the Markov trace by tau(1)=1. Then

    V_cl(beta)(A) = delta^(n-1) tau(R(beta)).

At unit-circle A sufficiently near i, delta is real, positive, and close to 2.
The standard TL_n *-structure has e_i*=e_i; its Markov trace is positive and
faithful in this interval, and rho(sigma_i) is unitary. One way to justify the
interval is positivity and nondegeneracy of the trace form at delta=2, followed
by continuity for the fixed finite-dimensional algebra. Equivalently, the
quantum-dimension weights stay positive when delta=2cos(theta) and theta is
small compared with 1/n.

If an n-braid satisfies

    V_cl(beta)=delta^(n-1),

the Jones polynomial of the n-component unlink, then tau(R(beta))=1. Since

    tau((R(beta)-1)^*(R(beta)-1)) = 2-2 Re tau(R(beta)) = 0,

faithfulness gives R(beta)=1 at every parameter in the interval. Its Laurent
coefficients therefore vanish identically. Applying the one-dimensional character
e_i -> 0 gives (-1)^w A^(-2w)=1, hence w=0 and rho(beta)=1 generically. The converse
is immediate (the same character forces w=0). Thus

    V_cl(beta)=delta^(n-1)  iff  rho(beta)=1.

This statement concerns the n-component unlink value of an n-braid, not a knot.
For a knot with V=1 represented on n>1 strands, the trace condition instead is

    tau(R(beta))=delta^(1-n),

strictly inside the unit disk when delta>1. The positive-trace norm calculation
then gives a positive number, not zero. Hence the most direct positivity proof
has no equality case to exploit for arbitrary knots. Faithfulness alone does
not supply the missing implication from this interior trace value to a Markov
simplification of the braid.

## Independent audit of the two-tangle unit classification

Let S=R[e]/(e^2-delta e). Write x=f+ge and lambda=f+delta*g. The determinant of
left multiplication by x, in basis (1,e), is f*lambda. Therefore x is a unit iff
both f and lambda are Laurent units. The explicit inverse is

    x^-1 = ((f+delta*g)-g*e)/(f*(f+delta*g)).

Write f=eta*A^m and lambda=epsilon*A^n, eta,epsilon in {+1,-1}. Their difference
is divisible by delta exactly when

    n-m=4k,   epsilon=eta*(-1)^k

for an integer k. Indeed, R/(delta)=Z[A,A^-1]/(A^4+1), where A^4=-1 and the basis
(1,A,A^2,A^3) shows that no other signed monomial equals 1.

Using the other team's horizontal-tangle convention

    b=A^-1+A*e,

whose two eigenvalues are A^-1 and -A^3, we obtain exactly

    x=eta*A^(m+k)*b^k.

This includes negative k, since b^-1=A+A^-1*e. Thus all algebra units are monomial
scalars times integer-tangle brackets. A unit bracket does not by itself prove
that a geometrical tangle is integer/rational.

For an actual tangle, composing with b^-k leaves a scalar times the horizontal
identity. Its denominator closure has monomial bracket. The absolute value of
V_L(1) is 2^(components-1), so this closure is a knot. The identity V_K'(1)=0 then
forces a monomial Jones polynomial to equal 1. Accordingly, the scalar is a
framing unit (-A^3)^r, rather than an arbitrary signed power of A. The remaining
step from trivial bracket to a geometrically trivial tangle remains precisely
the nontrivial Jones-detection issue; it cannot be inserted into the algebra proof.

## Extension of the nonunit-factor obstruction to all strand counts

Every TL_n over R is free of finite rank. If x_1 ... x_m is a scalar unit times 1,
then each x_i is a unit. Apply left multiplication and take determinants over R:
the product of determinants is a unit, so each determinant is a unit. Thus each
left multiplication map is invertible. Its inverse applied to 1 supplies a right
inverse; injectivity then supplies the left inverse as well.

This rules out composing algebraically noninvertible tangle pieces to obtain the
identity operator at any fixed strand number. It does not rule out their closure
having Jones polynomial 1, because the closure is only a scalar functional.
