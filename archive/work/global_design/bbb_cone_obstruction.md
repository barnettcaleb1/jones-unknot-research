# Irrational rotations obstruct the proposed finite cone certificate

2026-11-03. Node BBB-CONE, supporting the Burau rung of BBB-MULTISET.
Status: TRUSTED, with independent internal construction and algebraic/topological read. No external priority claim. This is a theorem about the explicit proposed domains, not a kernel element or a nonfaithfulness theorem.

## Statement

Fix a rational real number t>2 and let

    R = [t² t-1 t-1; 0 1 0; 0 0 1],
    C = [0 0 t^-1; 1 0 0; 0 1 0].

These are the matrices in Section 3 of bbb_perron_extensions.md. They act on real projective space RP².

**Theorem.** There is no nonempty open semialgebraic set U in RP² satisfying

    R^-1 U ⊂ U,       R^-1 C U ⊂ U,       U ∩ C U = empty.

More generally, the same conclusion holds whenever the boundary of U is contained in the zero set of a nonzero homogeneous real polynomial.

Consequently, the proposed X_+,X_- ping-pong certificate in Section 4 of bbb_perron_extensions.md cannot have nonempty open semialgebraic X_-. In particular it cannot use finite unions of full-dimensional open polyhedral cones. The same obstruction applies to semialgebraic domains with nonempty interior, by passing to that interior. No assignment of individual image cones to destination cones is assumed: arbitrary finite unions and overlaps are covered.

## 1. An infinite family of attracting projective lines

Put a=1/(t+1), q_n=t^(-2n). Exact matrix multiplication gives

    A_n = R^-n C = [a(q_n-1) a(q_n-1) q_n/t; 1 0 0; 0 1 0],

with characteristic polynomial

    f_n(s)=s³+a(1-q_n)s²+a(1-q_n)s-q_n/t.

As n tends to infinity this converges to

    f_infinity(s)=s(s²+a s+a).

The two nonzero roots of the limit are nonreal conjugates of modulus sqrt(a); its remaining root is zero. All three roots are simple. Therefore, for all sufficiently large n, A_n has a real eigenvalue r_n and conjugate eigenvalues alpha_n,beta_n, with

    |r_n| < |alpha_n| = |beta_n|.

Let L_n be the projectivization of the real two-dimensional invariant plane associated to alpha_n,beta_n. Every point except the real eigenpoint has a forward orbit whose distance to L_n tends to zero.

## 2. The rotations are irrational for every sufficiently large n

Choose alpha_n continuously in the upper half-plane and beta_n as its conjugate, and write zeta_n=alpha_n/beta_n. Since t is rational, f_n is a rational cubic. Its splitting field has degree at most six. If zeta_n were a root of unity of order m, then phi(m)<=6. There are only finitely many such roots of unity.

On the other hand zeta_n tends to zeta_infinity, where

    zeta_infinity + zeta_infinity^-1 = a-2.

The right side is a rational noninteger. If zeta_infinity were a root of unity, its sum with its inverse would be a rational algebraic integer, hence an integer. This is impossible. The limit is consequently outside the finite set of possible root-of-unity ratios, and zeta_n is not a root of unity for every sufficiently large n.

The action of A_n on L_n is therefore conjugate to an irrational rotation of RP¹. Every forward and backward orbit on L_n is dense. For a point outside the real eigenpoint, its forward orbit accumulates on every point of L_n: after rescaling by the modulus of the complex eigenvalues, the real-eigenline component tends to zero and the plane component rotates irrationally.

## 3. The attracting lines are pairwise distinct

Write A(q)=A(0)+q e_1 v^T, where v^T=(a,a,1/t). The normal to the dominant plane is a left eigenvector associated to the remaining real eigenvalue. Every left eigenvector of this companion matrix has nonzero first coordinate: a left eigenvector (0,y,z) would satisfy (y,z,0)=r(0,y,z), forcing y=z=0. Normalize the first coordinate to one.

If two distinct q-values had the same invariant plane, their common normalized normal ell and real eigenvalues r_1,r_2 would satisfy

    (q_1-q_2)(a,a,1/t)=(r_1-r_2) ell.

Thus r_1!=r_2 and ell=(1,1,(t+1)/t). But, with b=a(q-1),

    ell A(q)=(b+1, b+(t+1)/t, q/t).

Its first two coordinates differ by 1/t, whereas the first two coordinates of r ell coincide. The forced common normal is impossible. Hence the L_n are pairwise distinct.

## 4. Invariance forces entire lines into the boundary

The first two hypothesized inclusions imply

    A_n U = R^-(n-1)(R^-1 C U) ⊂ U

for every n>=1. For each sufficiently large n choose a point of the nonempty open U other than the real eigenpoint of A_n. Its forward orbit lies in U and accumulates densely on L_n. Thus

    L_n ⊂ closure(U).

If L_n meets U, then L_n is entirely contained in U. Indeed, U∩L_n is a nonempty open subset of L_n and is forward invariant. For any p in L_n, its dense backward orbit meets U∩L_n; forward invariance then gives p in U.

But L_n⊂U implies C L_n⊂C U, and any two real projective lines intersect. This contradicts U∩C U=empty. Therefore every sufficiently large L_n must lie wholly in the boundary of U.

This is the useful general obstruction: **any open domains satisfying the three inclusions must have infinitely many distinct complete projective lines in their boundary.**

## 5. Finite algebraic boundaries cannot contain those lines

Suppose the boundary lies in Z(F), for a nonzero homogeneous real polynomial F. A polynomial vanishing on a full real projective line is divisible by the linear form defining that line: change coordinates to put the line at Z=0 and restrict the polynomial. The infinitely many distinct L_n would give infinitely many distinct linear factors of F, which is impossible.

Every open semialgebraic subset of RP² has a boundary contained in such an algebraic set. On each of the three affine charts choose a finite polynomial sign description and discard identically zero defining polynomials. A boundary point must lie on the zero set of at least one remaining polynomial, since all signs are locally constant away from those zeros. Homogenizing and multiplying the finitely many polynomials over the charts, with coordinate factors if needed for chart boundaries, gives a nonzero homogeneous F containing the global boundary.

This proves the theorem. If a semialgebraic domain has nonempty interior but is not itself open, invertibility implies that each inclusion passes to its interior, and disjointness also passes to the interior. The open theorem then applies.

## Consequence for the proposed proof

For the earlier certificate, take U=X_-. Its conditions imply R^-1 U⊂U and R^-1 C U⊂U because C X_-⊂Y and R^-1Y⊂X_-. They also imply U∩C U=empty because U⊂X and C U⊂Y. The theorem therefore directly obstructs that certificate at every proposed rational parameter t>2.

The obstruction is exact and structural; no braid-word enumeration or numerical eigenvalue test is used. The positive-word Perron argument of BBB-PERRON is unaffected. Mixed inverse/rotation words A_n have qualitatively different dynamics from those positive words.

Scope limits:

- This does not refute Burau_4 faithfulness, BBB-MULTISET, or the Jones unknot conjecture.
- It does not rule out arbitrary open domains with more complicated boundaries, lower-dimensional domains, a different action, or a certificate outside the stated inclusions.
- The parameter is rational t>2. No claim here covers all irrational specializations.
- The explicit unmodified Gamma comparison remains Claude's task; this work neither constructs nor tests that loop.

The finite cone alternative is closed at its stated scope. The held geometric Moody-profile comparison remains OPEN.
