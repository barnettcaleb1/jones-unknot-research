# One fixed opposite-Omega orbit already determines universal preservation

2026-11-03. TRUSTED, exact algebra with an independent internal derivation.
No novelty claim. This is a finite design test, not a detection theorem.

Let F=Q(A), let Omega=L^2 R L^2 be the archived EKT boundary operation,
and take nonzero v,w in F^2 and C in M_2(F). Define

    s_n=v^T (Omega^T)^n C Omega^(-n) w.

Then s_n is constant for all integer n if and only if

    Omega^T C Omega^(-1)=C.

The same assertion holds on the even-iterate orbit, or with Omega replaced
by any nonzero integral power. Thus using only ONE fixed pair of rational
input vectors does not evade the universal tensor gate for an entire
constant opposite-Omega orbit. Isolated coincidences are not excluded.

## Proof

The determinant and trace are

    det Omega=-A^-6,
    tr Omega=-A^7+A^3-A^-1+A^-5-A^-9+A^-13.

No eigenvalue belongs to F. If one did, both eigenvalues would belong to
F and would be integral, together with their inverses, over the integrally
closed ring Q[A,A^-1]. They would be Laurent units c A^k. Their sum could
have at most two monomials, contradicting the displayed trace.

Over the quadratic splitting field choose an eigenbasis P, with eigenvalues
lambda1,lambda2. Every nonzero F-vector has both eigen-coordinates nonzero:
otherwise it would supply an eigenline defined over F and hence an
F-valued eigenvalue. Put v=P alpha, w=P beta, and C'=P^T C P.

At A=infinity choose the order of the eigenvalues so that

    lambda1=-A^7(1-A^-4+O(A^-8)),
    lambda2= A^-13(1+A^-4+O(A^-8)),
    r=lambda1/lambda2=-A^20(1-2A^-4+O(A^-8)).

No nonzero power of r is a monomial or a root of unity: its next coefficient
is -2m in r^m=(-1)^m A^(20m)(1-2m A^-4+O(A^-8)).

Now

    s_n=d+p r^n+q r^-n,
    p=alpha1 beta2 C'12,     q=alpha2 beta1 C'21.

All four eigen-coordinates are nonzero. Independence of the three distinct
exponential sequences forces p=q=0 when s_n is constant. This is exactly
C' diagonal, equivalently the stated universal identity. The constant-zero
case is included.

## Finite consequences

Three equal raw values at any THREE DISTINCT integer parameters force the
universal identity. Indeed, multiply s_n=s by r^n: the quadratic
p z^2+(d-s)z+q has three distinct roots z=r^n. Unless the orbit is constant,
any prescribed raw value can therefore occur at most twice.

Suppose instead s_n=u z^n with u nonzero and z=+/-A^k. Four CONSECUTIVE
values satisfying this formula already force z=1 and universal invariance.
If z differs from1,r,r^-1, a four-by-four Vandermonde matrix on those
distinct bases forces all coefficients, including u, to vanish. But r and
r^-1 are not monomials. The remaining possibility is z=1, which reduces
to the preceding argument. This also works for even Omega iterates.

## Framing and topology scope

These are raw-bracket statements. To use four equal normalized Jones
values, first establish a linear writhe increment w_n=w_0+n d for the
actual marked diagrams. For a fixed even-Omega insertion with preserved
endpoint orientations, copies of the same pure boundary word give this
increment directly; still record the convention and value. Then constant
Jones gives s_n=u(-A^3)^(n d), to which the monomial result applies. Do not
omit this framing step or claim three normalized Jones values always suffice.

Actual input bracket vectors are nonzero, because a closed link bracket
cannot vanish identically (evaluate at A=1). Neither universal preservation
nor equal values prove the produced knots are nontrivial.

Consequence for CX-EKT-FUSE1: a fixed external band whose basis11 corner
has determinant1 cannot evade the all-band exclusion by asking only for a
constant entire opposite-Omega orbit of chosen inputs, provided the framing
increment is established as above. A moving band/shell, action on additional
relative coordinates, or isolated equalities remain outside this result.

Checked independently by /root/omega_orbit_scope and re-derived by root.
No scan or invariant computation was needed.
