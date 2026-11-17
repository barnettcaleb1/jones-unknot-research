# The attempted sequential cancellation of the INF21 defect

2026-11-03. Bounded design analysis; no new words or placements evaluated.
TRUSTED after separate root and /root/paired_defect_design derivations.
Root also checked det(C)=det(C0) det(P) by exact Laurent arithmetic from
the independently saved Regina corner polynomials; see
paired_defect_determinant_check.json.
This rejects a proposed repair mechanism, not all two-band constructions.

The marked INF21 shell has

    C=C0+D E00,       C0=-A^-3 G Omega,
    G=[[delta,1],[1,delta]],
    D=A^-30(1-A^4)(1-A^16)(1-A^24).

Its three proper corners agree with C0. The contemplated repair is a
second actual spherical-tangle insertion, before or after this shell,
that preserves those corners and restores the invariant joint corner.

## A reason the mirrored defect looked relevant

Exactly,

    D(A^-1)=-A^16 D(A).

On three color-two strands with total color two, the central core full
twist has scalar A^(8-3*8)=A^-16. This suggests an opposite signed defect
after a mirrored insertion and a full twist.

This is not yet an actual diagram identity. D(A^-1) mirrors the ENTIRE
marked shell, including the band half-twists and hairpin return, not only
the core commutator. The full twist changes baseline and proper sectors.
Moreover two sequential defects do not add. The latter issue can be
settled exactly without computing a candidate word.

## The actual operator and the nonzero cross term

Set R=Z[A,A^-1]. Interpreting a two-slot closed shell as a spherical
tangle, its action on the rank-two ball-tangle skein module is an actual
matrix M over R. Closing against the two basis tangles gives C=G M.

For the baseline,

    M0=G^-1 C0=-A^-3 Omega,

an invertible rational-boundary operation with determinant -A^-12, a
Laurent unit. Normalize the infected shell by that actual inverse:

    P=M0^-1 M=I+D N,
    N=M0^-1 G^-1 E00.

N has rank one and

    N^2=c N,
    c=(C0^-1)00=C0_11/det(C0)
      =-A^-6/(delta^2-1),

which is nonzero. Thus even if an actual second operation could provide
exactly I-D N, their product would be

    (I+D N)(I-D N)=I-D^2 c N,

not I. Opposite scalar closure defects are insufficient.

## No actual sequential inverse can recover this tensor

The determinant lemma gives

    det(P)=1+cD
          =1-A^-6 D/(delta^2-1)
          =1-A^-32(1-A^4)^2(1-A^16)(1+A^12).

The final expression is an integral Laurent polynomial. It is not a
Laurent unit: its value at A=1 is1 and its first derivative there is0,
which would force any unit +/-A^k to be1, whereas the displayed
correction is nonzero. Equivalently its highest and lowest terms already
show it is not a monomial.

Every actual spherical-tangle operator Q has integral Laurent entries,
so det(Q) is in R. If QP=I or PQ=I, the identity
det(Q)det(P)=1 would make det(P) a unit of R, a contradiction.

This excludes not only the naive mirror/full-twist attempt, but ANY
actual sequential repair restoring the full baseline tensor. If the
three proper corners are required to stay equal to those of C0, then
Omega invariance forces the fourth corner to equal C0_00 as well.
Consequently any sequential repair with those requirements is excluded.

## Scope

This determinant argument by itself does not exclude an operation that
cuts and reconnects the interior of the infected shell, changes the three
proper corners to a different invariant tensor, or introduces a larger
relative system. The one-slot extension below excludes some of those
changed-corner possibilities. Neither argument supplies a
new counterexample candidate. No inference is made from a scalar defect
to equality of full eight-ended relative tangles.

In particular, stacking two CORE braid words before the existing return
cap is not the same operation as composing their completed spherical
tangle operators. Inserting beta^-1 immediately beside beta does restore
the original diagram by isotopy; it is outside the sequential-operator
obstruction and supplies no counterexample. The one-slot extension below
does not rule out simultaneous operations in both slots.

The only algebra used is the exact archived C=C0+D E00 and the ordinary
integral ball-tangle skein module. No general spherical-tangle
determinant-square claim is used. The overall framing factors cancel in
the normalization by M0.

## Stronger one-slot repair obstruction (root's extension)

The preceding determinant argument demands recovery of the SAME tensor.
Root supplied the following stronger result, independently checked here:
an integral operation in just ONE input slot cannot recover ANY invariant
tensor with a unit11 corner, even if the proper corners change.

Write

    alpha=delta(delta^2-3)^2,   F=(delta^2-2)(delta^2-4),
    C0=[[alpha r0-Fu,r0],[r0,u]],
    C=C0+D E00,     u=A^-18,
    H=det(C)=det(C0) S,

where S=det(P) is the nonunit displayed above. Suppose a right-slot
operation with integral matrix Q gives

    C'=C Q=[[alpha r'-Fv,r'],[r',v]],

where v is ANY Laurent unit. Set lambda=v/u (a unit), x=r'-lambda r0,
and l=(u,-r0). Direct multiplication gives

    l C=(H,0),
    l C'=(lambda det(C0)+(u alpha-r0)x, u x).

Since l C'=(H,0)Q, both entries of l C' are divisible by H in R.
Because u is a unit, H divides x. Substitution in the first entry then
shows H divides lambda det(C0), and hence det(C0). But H=det(C0)S and
det(C0) is nonzero. Cancellation in the domain R would make S a unit,
contradicting its explicit polynomial.

For a left-slot operation C'=Q^T C, transpose the equation. Both C and
the desired C' are symmetric, reducing it to the same right-slot case.

This uses the actual input skein coordinates: composition inside one
input ball is C Q (or Q^T C). There is no extra G factor. Integrality is
necessary for every actual framed tangle operation, including ones with
closed components. Thus the obstruction applies to all such one-slot
operations, not only rational twists.

The argument does NOT treat simultaneous operations in both slots,
C'=Q1^T C Q2, or an operation cutting the infection's interior. No
claim that all changed invariant tensors are excluded is made.
