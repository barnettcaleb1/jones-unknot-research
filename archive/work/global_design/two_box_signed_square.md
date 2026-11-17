# A signed square for two marked smoothing boxes

2026-11-03. CX-BOX-SQUARE. TRUSTED after two independent internal reads
and a separate derivation by root. No novelty claim.

This is a local diagram theorem. All four corners must be obtained from
ONE planar diagram by the two crossingless fillings in TWO disjoint
marked boxes. The outside crossings and framing stay fixed. Use the
common reduced bracket, with bracket(U)=1: equivalently divide every
absolute bracket by the same delta polynomial before evaluation. Never
divide a corner by a component-dependent power of delta.

Put zeta=exp(pi i/4), so delta=-A^2-A^-2 vanishes at zeta. Let C_ij be the
four reduced raw brackets, and suppose abs(C_11(zeta))=1. Write
u=C_11(zeta). Then

    C_01(zeta)/u = i a,   C_10(zeta)/u = i b,
    C_00(zeta)/u = d,
    det(C(zeta))/u^2 = d+ab = m^2,

for integers a,b,d,m. In particular the square has a POSITIVE sign.
The hypothesis is only determinant one at corner11; the whole polynomial
C_11 need not be a unit, and corner11 need not already be known to be U.

## Proof: keep the phases in the spanning-tree calculation

Insert an auxiliary crossing in each box. We may assume the completed
projection is connected: otherwise every state of every resolved corner
has at least two circles, so all four reduced brackets vanish at delta=0
and the nonzero-anchor hypothesis fails. Checkerboard-color this
connected projection and let G be its black Tait graph, with v vertices.

At an outside crossing e, write s_e=+1 or -1 according as the black-IN
smoothing has weight A or A^-1. Its OUT weight is A^-s_e. At zeta the
IN/OUT ratio is i s_e. At a marked edge, use a formal variable x or y
instead; the auxiliary crossing weights are not part of the corner.

At delta=0 exactly the one-circle states contribute. For a connected
plane diagram, these are precisely the spanning trees of G. If the
marked edges have inclusion bits b=(b_1,b_2), the outside part of the
tree has v-1-b_1-b_2 edges. Thus, in black-IN coordinates,

    C_b(zeta) = q i^(-b_1-b_2) tau_b,
    q = zeta^(-sum_outside s_e) i^(v-1),

where the integers tau_b are the coefficients of the signed tree
polynomial

    T(x,y)=tau_00+tau_10 x+tau_01 y+tau_11 xy.

Here every outside edge has weight s_e, and the two marked edges have
weights x,y. A marked loop, bridge, or zero coefficient causes no
exception: tree states that cannot occur contribute zero.

By the matrix-tree theorem, for an integral symmetric reduced Laplacian
M and reduced incidence vectors p,q_0,

    T(x,y)=det(M+x p p^T+y q_0 q_0^T).

The rank-two determinant identity gives

    tau_10 tau_01 - tau_00 tau_11
      = (p^T adj(M) q_0)^2 = m^2.

For invertible M this is the determinant lemma followed by
(p^T M^-1 p)(q_0^T M^-1 q_0)-(p^T M^-1 q_0)^2 for the xy coefficient.
Clearing denominators makes it a polynomial identity, valid also for
singular M. The one-vertex case has no nonzero incidence vectors and
gives the zero square directly.

The corner matrix in black-IN coordinates is

    q [[tau_00,-i tau_01],[-i tau_10,-tau_11]],

so its determinant is q^2 m^2. If identifying the supplied 0/1 labels
with black-IN bits reverses k of the two axes, the determinant becomes
(-1)^k q^2 m^2. At the supplied corner11 the black-IN bit sum is 2-k.
The determinant-one premise makes its tree coefficient +1 or -1.
Consequently u^2=(-1)^k q^2, proving the positive-square statement.
The same phase formula gives the displayed integral a,b,d.

More generally, for ANY nonzero corner C_ij(zeta), the same calculation gives

    (-1)^(i+j) det C(zeta)/C_ij(zeta)^2 = (m/t)^2 >= 0,

where m and t are integers and t is the corresponding nonzero signed
tree count. A determinant-one anchor has t=+/-1. Corner labels are 0/1;
reversing either axis changes the determinant and anchor parity together.
This formulation is independent of which filling is named 0. The general
form was independently re-derived in Claude's 15 November signed-square
referee report; it is not needed to reject CX-CLASP.

## Consequence for the opposite-Omega invariant tensor

The previously derived invariant equations are

    C_01=C_10=r,
    C_00=delta(delta^2-3)^2 r - (delta^2-2)(delta^2-4) C_11.

At zeta they give d=-8 and a=b. Therefore EVERY actual local two-box
realization with determinant-one corner11 satisfies

    a^2-m^2=8.

Factoring (a-m)(a+m)=8, with the two factors of the same parity, gives
only abs(a)=3 and abs(m)=1. Both single corners have determinant THREE.
In particular two-component single corners are impossible, since their
determinants are even. The Hopf case would give m^2=4-8=-4.

This rejects CX-CLASP even with opposite clasp signs and arbitrarily
entangled fingers. The former unsigned surgery possibilities
a_surgery=-b_surgery=+/-2 and abs(ell)=2 did not keep track of the raw
bracket phases. They were necessary magnitude conditions, not a
realizability certificate. The signed square eliminates them.

More precisely, the only remaining component/determinant pattern in
this unit11 invariant setting is

    components (00,01,10,11) = (2,1,1,1),
    determinants             = (8,3,3,1).

The odd single determinants force knots. At A=1 the invariant equation
is C_00=-2r. A knot has abs(r(1))=1, whereas a mu-component link has
absolute reduced bracket value 2^(mu-1); hence corner00 has two
components. The determinant-one corner11 is also necessarily a knot.

## A calibration that must NOT be promoted to a candidate

The residual pattern already occurs in ordinary rational gluing.
Let G=[[delta,1],[1,delta]] and Omega=L^2 R L^2, with

    L=[[A,0],[A^-1,-A^-3]],  R=[[-A^3,A],[0,A^-1]].

The realizable tensor C=G Omega is invariant and has

    C_11=-A^-15,
    C_01=C_10=-A^-1-A^-9+A^-13,
    C_00=A^9-A^5+2A-A^-3+2A^-7-A^-11.

Direct Laurent arithmetic checks Omega^T C=C Omega and the invariant
equation exactly. Its input tangles and gluing are rational. Therefore
any Jones-unit knot closure in this calibration is an actual unknot
by rational/2-bridge detection. Passing (8,3,3,1) is not evidence of a
counterexample or of escaping known detection classes.

## Scope and review

The local two-box setup is exactly what CX-CLASP and its requested four
actual marked corner diagrams require. This proof is independent of a
general assertion about determinants of spherical-tangle invariants.
Chung--Lin asked a general square-determinant question in Section5 of
*On n-punctured ball tangles* (math/0502176); their Lemma4.11 keeps
opposite off-diagonal phases in the canonical normalization. We do not
claim a general identification of their full object class with this
diagram model, a solution of that historical question, or novelty here.
Primary reference: https://arxiv.org/abs/math/0502176 .

Independent internal readers: /root/unit_corner_goeritz and
/root/unit_corner_phase_referee each checked the tree-state model,
marked-edge phases, singular-matrix case, label reversals, common
reduced-bracket convention and the Hopf contradiction. Root re-derived
the calculation and checked the rational calibration separately.
