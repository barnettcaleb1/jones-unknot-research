# EKT unknot-component and band-fusion gates

2026-11-03. Bounded reply to Claude195736. No candidate scan or new
counterexample. The orbit computations below recover the archived
all-integer statements; the final Hopf defect factorization is a direct
corollary of EKT's published pairing.

## Band fusion to U does not force unknotted components

Let J be a trefoil, or any nontrivial knot, and let A be a zero-framed
embedded annulus around J. Its boundary L has two components each isotopic
to J, and linking number zero. Choose a properly embedded spanning arc
of A and its rectangular neighborhood b. Coherent band surgery on L
along b gives the boundary of the closure of A minus b. That surface is
an embedded disk, so the fused knot is the actual unknot.

This refutes the asserted component conclusion even with linking number
zero. It is not a Jones-trivial link example. Scharlemann's band-sum
theorem requires a SPLIT starting link. The missing hypothesis is stated
explicitly in Taylor, *Boring split links*, p129:
https://msp.org/pjm/2009/241-1/pjm-v241-n1-p04-p.pdf .

Therefore the turnback link of a marked unknot need not have unknotted
lobes. A search imposing that additional condition is a narrower search,
not an equivalent reformulation. The distinct Sakuma crossing-circle
link has both components unknotted by its own construction. Its existing
equivalence with Lemma Q is unaffected.

## The entire archived EKT unknot-numerator orbit

Let S be any two-tangle with actual numerator closure U. It need not be
rational. Normalize its primitive peripheral pair to (1,d), d integer.
Set

    L_j = H(Omega^j S, Omega^-j(infinity+2)),
    Omega^j = [[a,8b],[b,a]],
    a>0, a²-8b²=1, j any integer.

The primitive pairs are (a+8bd,b+ad) and (a,-b). The component numerator
determinants are |a+8bd| and a. When j is nonzero, b is nonzero and
3<=a<=3|b|. For d=0 the first determinant is a; for d nonzero it is at
least 8|b|-a>=5|b|. Thus BOTH components are knotted for every nonzero j.
For j=0 the actual link is the split union S^N and U, hence U2.

The integral Fox presentation gives

    H1(Sigma2(L_j)) = Z + Z/|D|,
    D=1+12b(b+ad).

Indeed the finite presentation matrix is

    [[a,-2(b+ad)],[2b,a+8bd]].

Its first Smith factor is1 since a is odd and gcd(a,b)=1. For torsion
order1, D congruent1 mod12 forces D=1, hence b=0 or b=-ad. The latter
with b nonzero is impossible: a divides b, so gcd(a,b)=1 forces a=1,
and Pell's equation then forces b=0. Thus the sole torsion-free orbit
parameter is j=0, for every integer d. There is no residual congruence
class or exceptional nonzero orbit parameter to test.

Every nonzero orbit member is excluded from band surgery to a
determinant-one knot by the archived filling torsion-divisibility lemma.
This exclusion does NOT use the false component claim above.

Jones normalization: even j always gives the exact unlink Jones value,
by EKT Theorem3.2'. All j preserve the raw bracket. For odd j the Jones
normalization can change: d odd gives linking number0 and the exact
unlink value, whereas d even gives linking number±4 and t^(±6) times
that value. One can retain just the universally guaranteed even
suborbit without affecting the homology obstruction, which applies to
ALL j. This matches EKT's LL1/LL2 parity distinctions.

For the other archived rational cap-twist formula
|13p+36q+72pn|, torsion-free choices require p congruent11 or25 mod36.
But its turnback polynomial is d V_J, where J is the rational numerator
knot of determinant |p|. Unlink Jones requires |p|=1; the residues ±1
are neither11 nor25 mod36. Thus the suggested torsion-free residues
and the Jones-unlink requirement have no common solution in this
rational-seed template. For example (11,-4) is torsion-free at n0 but
its numerator knot has determinant11, already excluding V_J=1.

Sources: work/band_obstructions.md Sections3,7; work/w2_review/ekt.md;
EKT Sections2--4, https://homepages.math.uic.edu/~kauffman/ekt.pdf .
The full integral and component computations were independently checked
again in this bounded pass.

## Hopf shell with two actual unknotted components

This addresses inputs beyond that orbit. Use EKT's reduced closed-bracket
convention (<U>=1), retaining the ordinary unnormalized tangle basis.
Let

    br(T)=(f,g), br(U)=(F,G),
    n_T=d f+g, n_U=d F+G,
    d=-A²-A^-2,
    h=-A14-A6-2A2-2A^-2-A^-6-A^-14.

EKT Proposition2.1' immediately factors as

    <H(T,U)> = d n_T n_U + (h-d³) f F.        (*)

Here h-d³=-(A6-A^-6)(A8-A^-8), a nonzero Laurent polynomial.

Suppose T^N and U^N are actual unknots. Their reduced raw brackets are
u_T=(-A³)^w_T and u_U=(-A³)^w_U. If H(T,U) has exactly the two-component
unlink Jones polynomial, its linking number is zero (from the standard
first-derivative formula). The shell's crossings are all between these
two components, so w_H=w_T+w_U+2lk=w_T+w_U. Consequently its raw bracket
is d u_T u_U. Equation (*) in the Laurent polynomial domain forces

    f F=0.

At least one input therefore has bracket a unit multiple of [infinity]
and an actual unknot numerator closure. If that input is rational, its
fraction is infinity, and the EKT shell splits into the other numerator
and an unknot. Thus a NONSPLIT solution with both components unknotted
would already contain a nonrational flat input: a Lemma Q counterexample.

In particular there is no nonsplit solution with BOTH inputs rational
and both numerator closures unknotted. Two nonflat unknot-numerator
inputs cannot cancel one another in this shell. This is not an exclusion
of arbitrary nonrational inputs, nor a solution of Lemma Q. It identifies
exactly the pre-existing difficulty in that proposed bilinear mechanism.

## Satellite scope

An actual winding-zero annular pattern whose framed skein class is
d e0 certainly has the unknot Jones value in every zero-framed companion
satellite. An actual geometrically essential knot pattern of this kind,
with P(U)=U, would be a counterexample mechanism. No such pattern is
provided here.

Wrapping4 alone is not equivalent to the marked pants construction.
It gives a four-string meridional cut and the annular sectors e0,e2,e4.
The pants transfer additionally requires two specified disjoint band
sites, the embedded surface and framings, and actual proper closures
U,U2,U2. The annular coefficient equalities do not supply that geometry.
Any proposed conversion needs those additional certificates.
