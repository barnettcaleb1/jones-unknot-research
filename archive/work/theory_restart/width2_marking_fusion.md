# Width-two marking, fusion ranks and endpoint projectors

17 November 2026. Bounded THEORY subtask. Generic Temperley–Lieb calculations,
using the banked recoupling conventions in `twobridge_geometry_referee.md`
and `necklace_skein_referee.md`. No construction sweep or nine-by-nine module
implementation. One four-input connectivity sanity check is stated below.

## Conclusions usable immediately

1. The nine-dimensional module has adjacent-arc channels of ranks **2,4,3**
   and axis channels of ranks **4,5**. Its new color-four leading channel is
   rank three. The width-one scalar ratio automaton therefore does not extend
   merely by adding one scalar channel.
2. There is a completely marked nine-dimensional plat presentation, with
   halfword `s.l1.l3.W.u2.u2` and W using indices 0 through 3. Its empty
   closure is the trivial theta graph. Arbitrary two-cup halfwords also use
   index 4; a reduction of those words to this marked class has **not** been
   proved here. Calling the nine-dimensional representation all width-two
   halfwords would currently hide a geometric step.
3. Both endpoint conditions are rank-one projectors, although all three
   internal arc channels have rank greater than one. Their overlap is
   `Delta_2^-3`, rather than one. A unit matrix coefficient fixes an overlap;
   it does not force preservation of a line.

The following are generic skein deductions, offered for independent checking
before promotion beyond TRUSTED. They are identities available to validate
Engine B, not hypotheses to be fitted to its output.

## 1. Conventions and fusion paths

Work over Q(A), with delta=-A²-A^-2, `t=A^-4`, and color j denoted V_j.
The twist is `theta_j=(-1)^j A^(j(j+2))`. Use the half-twist handedness whose
raw color-(2,2) eigenvalues on channels c=0,2,4 are

    A^-8, -A^-4, A^4.

Let B_i be this raw crossing of adjacent arc legs. Normalize the inverse
crossing as `X_i=A^-8 B_i^-1`, agreeing with the width-one X eigenvalues
1,-t on its surviving channels. Let T be the raw axis–first-arc full twist,
whose channels 1,3 have eigenvalues A^-8,A^4, and put `Y=A^8 T`.
If the implementation uses opposite handedness, invert the stated generators
or replace t by t^-1 consistently. These scalar normalizations are ribbon
units; the final preferred normalization remains necessary.

The space is

    H2=Hom(V1,V1 tensor V2 tensor V2 tensor V2 tensor V2).

A left-associated basis is indexed by paths `(j1,j2,j3)` with j0=j4=1,
where successive labels fuse with V2. The nine paths are

    (1,1,1), (1,1,3), (1,3,1), (1,3,3),
    (3,1,1), (3,1,3), (3,3,1), (3,3,3), (3,5,3).

This is a basis count, not a specific normalization of the trivalent vertices.
The fusion rule used throughout is
`Va tensor Vb = sum_(c=|a-b|,|a-b|+2,...,a+b) Vc`.

## 2. Characteristic polynomials and central scalar

Y acts by 1 on j1=1 and t^-3 on j1=3. Hence

    char_Y(z)=(z-1)^4 (z-t^-3)^5,
    trace(Y)=4+5t^-3,  det(Y)=t^-15.

For any adjacent arc exchange X_i, the selected pair fuses to 0,2 or4.
The multiplicities are the dimensions of
`Hom(V1,V1 tensor Vc tensor (V0+V2+V4))`, namely2,4,3. Therefore

    char_Xi(z)=(z-1)^2 (z+t)^4 (z-t³)^3,
    trace(X_i)=2-4t+3t³,  det(X_i)=t^13.

The minimal polynomials have each of these distinct generic factors once.
All three channels genuinely occur in H2. The axis generator and adjacent
exchange obey the type-B mixed braid relation; the other generators obey the
ordinary braid and distant-commutation relations with the above inverse
handedness handled consistently.

For the normalized annular generators `(Y,X_1^-1,X_2^-1,X_3^-1)`,

    (Y X_1^-1 X_2^-1 X_3^-1)^4 = t^-24 I.

Proof: the corresponding raw word is the full twist on colors(1,2,2,2,2),
which acts on total color1 by
`theta_1/(theta_1 theta_2^4)=A^-32`. Each normalized factor contributes A^8;
there are16 factors. Thus the scalar is A^(128-32)=A^96=t^-24.
At width one the same calculation gives `(Y X^-1)^2=t^-4 I`, matching the
already banked two-dimensional matrices.

## 3. Simultaneous-channel ranks

Let `P_c^(i)` project to pair channel c for X_i; let Q1,Q3 be the Y-channel
projectors. For example,

    P_c^(i) = product_(d != c) (X_i-lambda_d I)/(lambda_c-lambda_d),
    (lambda_0,lambda_2,lambda_4)=(1,-t,t³),
    Q1=(Y-t^-3 I)/(1-t^-3),  Q3=I-Q1.

These are generic formulas; clear denominators before specializing at roots.
The distant pair projectors for X1 and X3 commute. Their joint ranks, with
rows/columns indexed0,2,4, are

    [[1,1,0],
     [1,2,1],
     [0,1,2]].

Indeed `Va tensor Vb` must contain total arc color0 or2, since only those
couple with the axis V1 to total1. This proves, in particular,

    P_0^(1) P_4^(3)=P_4^(1) P_0^(3)=0,
    rank(P_0^(1) P_0^(3))=1.

Q and the middle-pair projectors P^(2) also commute. Their joint rank table
has rows1,3 and columns0,2,4:

    [[1,2,1],
     [1,2,2]].

Count `Hom(V1,Va tensor Vc tensor V2)` for each a,c. Consequently
`rank(Q1 P_0^(2))=1`. These are selection rules available before any
leading-coefficient calculation: the corresponding path sectors are zero,
not merely small or liable to cancellation.

## 4. A marked connected-arc plat, and the missing normal form

Take four moving arc legs1,2,3,4 next to the axis. At the input use

    v = id_V1 tensor coev_(12) tensor coev_(34).

At the output cap legs2,3, and apply the width-one two-vertex functional to
the remaining axis,leg1,leg4. Denote this functional phi and normalize
`phi(v)=1`. With the empty braid, the cups and cap snake into the single
trivial arc joining the two theta vertices. Using the same two pairings at
both ends instead would introduce an extra closed arc component.

In the halfword convention of `tools/alex.py`, the corresponding presentation
is

    s.l1.l3.W.u2.u2,  W in {x0,y0,x1,y1,x2,y2,x3,y3}*.

Starting from one half-strand, l1 creates cup(1,2), l3 creates cup(3,4), and
the original fifth half-strand lies outside W. The two terminal u2 operations
cap(2,3) and(4,5). Bending spectator5 to the outside theta vertex gives the
colored marking just described. Crossing indices1,2,3 exchange moving legs;
index0 is the axis operation. Signs/units must still be calibrated to the
implementation, as in width one.

The connectivity check has a finite combinatorial form. Let pi be the arc
permutation of W and transport the input matching(12)(34) by pi. The arc is
connected exactly when this matching is not(14)(23): adjoining output edge23
then makes a path from1 to4, rather than a closed component23 plus edge14.
The symmetric lift of the connected quotient arc is a knot. This criterion
does not certify its nontriviality.

A fixed sanity check with `alex.symmetrize` and `alex.diagram` gives:

    empty W: knot;  W=x1: knot;  W=x2: knot;  W=x2.x1: not a knot.

These are four connectivity checks, not Jones evaluations or a candidate scan.

**Scope gap:** a general two-cup halfword has five half-strands and can use
x4,y4, crossing the spectator. The two-dimensional TH-2BR class similarly
restricts a one-cup halfword to indices0,1, rather than the full0,1,2 set.
No theorem here moves every general two-cup word into this spectator form
without increasing width. A full larger-width claim needs that geometric
normal form or an explicitly larger representation.

## 5. Rank-one endpoint projectors and what a unit coefficient means

Put

    E=P_0^(1) P_0^(3),   F=Q1 P_0^(2).

Both are rank-one self-adjoint idempotents in the generic Hermitian skein
pairing (bar A=A^-1). The input line is im E, and the output covector is the
dual of im F. In particular

    X1 v=X3 v=v,  phi X2=phi,  phi Y=phi.

These show only some geometric cap stabilizers. A classification of all
trivial closures, or all Hilden-type double cosets, has not been obtained.

Write `d=Delta_2=A^4+1+A^-4`. The endpoint overlap is

    EFE=d^-3 E,  FEF=d^-3 F,  trace(EF)=d^-3.

Proof by two snake contractions and one partial trace: projecting the two
input singlets12,34 onto a singlet23 gives `d^-1` times the pair of singlets
14,23. This costs `d^-2` in the normalized squared pairing. In the latter
state the axis–leg1 projector Q1 has normalized expectation `d^-1`, since
its partial quantum trace over V2 is the identity on V1
(`dim_q V1/dim_q V1=1`), while the singlet normalization divides by d.
Multiplying gives d^-3. This proof uses generic quantum traces; no positivity
at an exceptional root is assumed.

For the normalized marked coefficient `C_beta=phi rho(beta)v`, with all
generator framing units of norm one, the exact identity is

    C_beta bar(C_beta) = d³ trace(F rho(beta) E rho(beta)^*).

It follows by writing E and F as rank-one orthogonal projectors and dividing
the transition pairing by its empty-word value. The eventual preferred J
differs by a ribbon unit, so its norm obeys the same identity.

Thus `J=1` asks for the transition overlap `d^-3`, its empty-word value.
It does **not** ask for overlap1 or equality of the two lines. A line-stabilizer
or kernel element can force a unit coefficient, but searching only those
elements is a strict sufficient-condition strategy absent a separate rigidity
theorem. The rank-one endpoints do not restore the width-one automaton: the
interior propagators still have the multiplicities in Sections2–3.

## 6. Immediate use, without a new search

Engine B can check the characteristic polynomials, determinants, central
scalar, joint projector ranks, endpoint eigenvectors, and endpoint overlap
against its actual matrices and boundary vectors. A disagreement must first
be sorted into handedness, scalar normalization, or marking; it is not
automatically a failure of the representation.

For global cancellation theory, use the exact local expansion
`X_i^m=P0+(-t)^m P2+t^(3m) P4`. It has three distinct monomial channels,
but the last projector has rank3. Iterated maximal-degree paths can vanish
by the displayed selection rules, or cancel inside these multiplicity spaces.
No positivity, finite scalar automaton, or faithful-action implication has
been asserted. The missing claim is control of the **sum of surviving marked
path coefficients**, outside the actual trivial-closure locus.

## 7. Independent read of the two-site cancellation theorem

Read `width2_tropical_crux.md` Sections2–4 after the calculations above.
**ACCEPTED** as a fixed-template theorem. The opposite-sign operator envelopes,
their two scalar offset walls and endpoint signs are correct. The seven-point
normal-direction list is complete: it is the list perpendicular to pairwise
differences of `{00,01,10,11,13,31,33}`. The resulting active-sector thresholds
and both diagonal aggregate identities follow exactly from those partitions.

For clarity about normalization: insert full twists in fixed disjoint local
sites of an already marked knot template. Full twists preserve the endpoint
permutation, so knot versus extra-component connectivity is unchanged. The
orientations of the participating strands are also unchanged; writhe and
the relevant framing/linking corrections vary affinely in the integer
parameters. Hence preferred normalization differs from the fixed raw
coefficient by a monomial character `epsilon(m,n)t^(a+bm+cn)`. This preserves
the Laurent-unit locus. Once a raw value is a unit, the preferred root/value
and derivative normalization makes J exactly1.

The infinite-line argument therefore applies to actual preferred J on such
templates, not merely to a formal unnormalized sum. It gives necessary
sector zeros and aggregate cancellations. It neither proves nontriviality
of a unit closure nor excludes isolated unit parameters, and does not
extend the marked spectator class to arbitrary two-cup halfwords.

## 8. The unrestricted slice is twenty-one-dimensional

The marking gap has a precise replacement, requiring no new matrix fit.
For a horizontal slice with m actual half-strands of the quotient arc, put

    H_full(m)=Hom(V1,V1 tensor V2^m).

The halfword starts with one arc strand at a theta vertex. Its state is
the trivalent inclusion `i:V1 -> V1 tensor V2`, not an empty cup state.
Each off-axis cup inserts `coev_V2` in the specified adjacent positions,
each cap inserts `ev_V2`, and the final theta vertex is the projection
`p:V1 tensor V2 -> V1`. Choose compatible vertex normalization, for example
p i=id. All crossings act on these actual ordered factors: index0 is the
axis–first-arc full twist, and index j>=1 exchanges arc legs j,j+1.

Consequently arbitrary Morse halfwords with at most five half-strands are
represented by three spaces and rectangular cup/cap maps:

    H_full(1) <-> H_full(3) <-> H_full(5),
    dimensions    1              4              21.

Here

    V2^3 = V0 + 3V2 + 2V4 + V6,
    V2^4 = 3V0 + 6V2 + 6V4 + 3V6 + V8,

so V2^5 has multiplicities6 and15 in colors0 and2. Only those two total arc
colors can couple to the axis and return V1, giving dim H_full(5)=21.
The same count gives1 and4 for m=1 and3. No claim that an arbitrary Morse
word has already been converted to one fixed plat braid is necessary for
this finite-state-space description; cups and caps remain explicit maps.

For the fixed two-cup template `s.l1.l3.W.u2.u2`, unrestricted W may use
indices0 through4 and acts on H_full(5). Restricting to indices0 through3
leaves the fifth arc leg untouched. Recouple the first four legs with the
axis before adjoining that spectator. Only prefix colors1 and3 can fuse
with the spectator V2 to final color1. Thus the restricted action splits

    H_full(5) = Hom(V1,V1 tensor V2^4)
               direct-sum Hom(V3,V1 tensor V2^4),
    dimensions                 9 + 12.

The precise injection of the nine-dimensional module is

    h |-> (h tensor id_V2) i.

It is injective and intertwines all braids on the axis and first four
legs: it identifies H2 with the prefix-color-one summand. The initial cups
give h=id_V1 tensor coev12 tensor coev34, so the marked initial state lies
in that summand. Bending the untouched spectator recovers Sections4–5.

The omitted X4 is not block diagonal in general. One can see this already
at the classical spin limit: leave the first pair in its singlet and swap
leg4 with spectator5. The remaining three-leg configuration exchanges a
leg of a singlet with the leg attached to the initial spin-half vertex.
After the swap, coupling that spin-half prefix to the other singlet leg
has both spin-half and spin-three-halves channels. Partial trace over the
spin-one singlet leg gives weights1/3 and2/3, respectively. The latter is
nonzero, so the generic off-block map cannot vanish identically. Thus the
twenty-one-dimensional space is an actual requirement for unrestricted
index4 motion, not just a larger containing space chosen for convenience.

Likewise, unrestricted one-cup halfwords act on H_full(3), dimension4.
For words using only indices0,1, the third leg is a spectator and this
restricted representation splits2+2 by prefix color1 or3. The TH-2BR
marked initial state lies in the first two-dimensional summand. This
explains exactly why its theorem was scoped to the spectator class rather
than every one-cup word.

For additional engine checks, on H_full(5) the normalized arc eigenvalues
1,-t,t³ have multiplicities4,9,8, and the axis eigenvalues1,t^-3 have
multiplicities9,12. On H_full(3), those multiplicities are1,2,1 and2,2.
These follow from the same fusion counts. They are not additional search
regions: the topology and known-empty-class filters still apply.
