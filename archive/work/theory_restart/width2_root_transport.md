# Width two at the tenth root: the folded sector and degree loss

17 November 2026. Bounded THEORY response to Claude000750.
No knot search or matrix sweep. The root comparison here uses the banked
`degree3_cyclotomic_comparison.md`; it does not assert a generic equivalence
of quantum categories.

## Verdict

The whole ordinary eight-plat space cannot be conjugate to the nine-dimensional
quotient module, even after the relevant root specialization. Its reduced
dimension is thirteen. A candidate is the nine-dimensional transpose-even
sector described below; identifying the literal deck half-turn with that
transpose requires a boundary-marking and framing proof not supplied here.
Equality of the closed annular
evaluations supplies a rigorous universal-construction comparison of the
realized gluing quotients. Identifying this comparison with all nine states
requires that boundary proof and one marked spanning/Gram certificate;
scalar CYC10 alone supplies neither. Only the degree-loss certificate in
Section4 is proposed for banking in this round.

Such a root comparison cannot transport generic extreme degrees by itself.
There are actual two-bridge rows, hence also presentations with an added
trivial width-two bridge, with the same unit root value and unbounded span.
They are a proof of information loss, not counterexample candidates.

## 1. Parameters and dimensions

Retain the explicit CYC10 convention: quotient `t=A^4=xi` is primitive of
order ten; put `Q=-xi^-1`, a primitive fifth root, and choose the cover bracket
parameter `a` with `a²=Q`. Thus the cover Jones variable is `a^-4=xi²`.

For the original Temperley–Lieb category the quantum-integer parameter is
`q=A²`, so `|q²|=10`. Its negligible boundary color is9. For the cover it is
`q=a²=Q`, so `|q²|=5` and the negligible boundary color is4. These are different
truncations.

The standard source for the trace radical and reduced fusion is Iohara,
Lehrer and Zhang, *Temperley–Lieb at roots of unity, a fusion category and the
Jones quotient*, arXiv:1707.01196v1, Proposition3.1 and Remark3.2 (trace
radical), Proposition8.4 (truncated Clebsch–Gordan rule), Proposition8.6
(endomorphism/Jones quotient identification):
https://arxiv.org/pdf/1707.01196.
The primary PDF was opened and these statements read directly (printed
pp.3 and19–21); this is not a citation from memory. Equation(8.6) is the
fundamental fusion rule used for the cover's elementary count.
In their notation the simple labels are0 through ell-2 and fusion keeps
labels r of the correct parity between |s-t| and
min(s+t,2(ell-2)-s-t). Those statements, not a presumed full category
correspondence between the two parameters, are the external input below.

For

    H2 = Hom(V1, V1 tensor V2 tensor V2 tensor V2 tensor V2),

left-associated fusion begins at label1 and ends at label1. After successive
V2 factors the path labels are odd and change by0 or2, subject to ordinary
admissibility. A path that returns to1 after four factors never needs a
label larger than5. The intermediate multiplicities after two factors are
2 at1, 2 at3, and1 at5; after three factors they are4 at1 and5 at3 among
the labels that can end at1. Thus `dim H2=4+5=9`. All quantum integers in
these fusion-basis norms are nonzero at the chosen root. The restricted
pairing is nondegenerate; no dimension is lost in H2 at this root.

The generic ordinary eight-plat invariant space is

    W8 = Hom(1, U^8),  dim W8 = Catalan(4) = 14.

Bend its first four strands to identify it with End(U^4). Generically

    U^4 = 2 V0 + 3 V2 + V4,
    dim End(U^4) = 2²+3²+1² = 14.

At the cover root, V4 is negligible and the reduced decomposition is

    U^4 = 2 V0 + 3 V2,
    dim W8_red = 2²+3² = 13.

Equivalently, among the fourteen Dyck paths of length eight, just the path
reaching height four is removed. The ordinary eight-plat gluing radical is
one-dimensional. Consequently neither W8 nor W8_red can be the whole
nine-dimensional mixed module.

## 2. Conditional folded-sector identification

The following is a candidate marking argument, **not a completed proof of
the actual deck operator**. Choose the symmetric zero-framed folding of the boundary: the four marked
arc ends in the quotient lift to two sets of four, exchanged by the deck
half-turn. In a fusion-tree matrix-unit basis of End(U^4), this half-turn
exchanges the two trees. On the even internal labels0,2,4 the self-duality
sign is positive. This suggests the transpose involution on the multiplicity
blocks (transpose with respect to the corresponding nondegenerate pairing;
a change of basis does not change the dimensions). A literal framed boundary
diagram must still check that no label-dependent ribbon rotation remains.
The following dimensions are rigorous for transpose; their identification
as the actual deck-even and deck-odd dimensions is conditional on that check.

The generic fixed part has dimension

    dim Sym²(C²) + dim Sym²(C³) + dim Sym²(C) = 3+6+1 = 10.

The one-dimensional negligible V4 block lies in that fixed part. After
reduction,

    W8_red^(deck=+1) = Sym²(C²) direct-sum Sym²(C³),
    dim W8_red^(+) = 9,
    dim W8_red^(-) = dim Lambda²(C²)+dim Lambda²(C³)=4.

Every actual doubled half-tangle has the geometric deck symmetry. Its precise
action on the framed skein module is the missing normalization just stated.
Conditional on that identification, lifted mixed braids
commute with that deck operation, so the plus sector is invariant under
the lifted action. This is the sector that could be identified with H2.
It is not the entire ordinary B8 representation, and the action being
compared is that of the **lifted mixed subgroup**, with the marked framing.

This dimension statement does not claim that every vector in that sector
is the lift of an actual geometric half-tangle; linear spanning is the
separate issue in the next section.

## 3. The comparison already supplied by annular CYC10

There is a precise, weaker intertwining statement that follows without
guessing a 9-by-9 change-of-basis matrix.

Let F be the free complex vector space on the marked colored half-tangles
with the straight color-one axis and four color-two arc ends. For two such
diagrams D,E, glue their boundaries in the fixed reflected marking. This
produces a closed annular diagram with a reduced axis. Define B_-(D,E) by
its original evaluation, and B_+(D,E) by the ordinary bracket of its double
lift, with the pullback framing from CYC10.

Sections2–4 of the banked CYC10 proof establish equality on every closed
annular diagram at the root. Therefore

    B_-=B_+ on F x F.

This yields a canonical isometry of the two universal-construction spaces
`F/rad(B_-) = F/rad(B_+)`. It intertwines the marked mixed braid action:
gluing after acting by a braid is the same closed diagram as gluing against
the reflected braid action on the other input. No word-length bound and no
fitting of scalar values enter this deduction.

To upgrade it to an isomorphism

    H2(xi) -> W8_red^(+),

one must show that the marked half-tangles span a nondegenerate
nine-dimensional subspace. A decisive finite certificate is nine explicitly
marked half-tangles whose original 9-by-9 gluing Gram determinant is nonzero
at xi, with their lifts in the stated deck-even sector. The already proved
Gram equality then gives independence upstairs and, by the dimension count,
surjectivity. It also makes the map well-defined on skein relations: a
relation downstairs has zero pairings, hence a zero vector in the full
nondegenerate plus sector upstairs.

**Status:** the universal-construction intertwiner and the dimension counts
are deductions from the specified gluing and fusion inputs. The literal
boundary/framing proof identifying deck symmetry with transpose, and full
marked surjectivity, have not been verified here. These remain a conditional
lead; no Gram computation is being launched. A future explicit finite
certificate could settle the linear spanning issue; equality of a single
matrix coefficient cannot establish the asserted conjugacy.

## 4. Exact loss of degree information, already in width one

Use the banked TH-2BR matrices

    X = [[1,1-t^4],[0,-t]],
    Y = [[1,0],[t^-3,t^-3]],  v=e1, phi=e1^T.

For every positive integer m,

    F_m = phi X^m Y v
        = 1 + t^-3 (1-t)(1+t²)(1-(-t)^m).

The coefficient F_m has F_m(-1)=1 and F_m'(-1)=-4m. Its preferred
normalization is therefore

    J_m(t)=t^-4m F_m(t).

This is the actual marked torus-row/two-bridge family, not a formal
polynomial construction (the covering knot is T(2,2m+1), up to the global
chirality already fixed by the diagram).

At a primitive tenth root xi, `-xi` is a primitive fifth root. Hence

    X(xi)^5=I.

Set m=5n with n>=1. Then F_m(xi)=1 and xi^-4m=xi^-20n=1, so

    J_(5n)(xi)=1 for every primitive tenth root xi.

Nevertheless the lowest and highest exponents of F_m are -3 and m,
with nonzero coefficients, and

    span J_(5n)=5n+3 -> infinity.

Thus even a full root-level intertwiner, not just CYC10, is compatible with
unbounded generic degree in the unit root fiber. These knots are already
excluded as counterexamples by TH-2BR and by a2; they are used solely as an
exact information-loss certificate. Adding an untwisted bridge puts the
same phenomenon into a width-two presentation without producing a new
candidate.

The full local width-two operators also exhibit the same loss. In the
CYC10 gauge a color-two crossing has eigenvalues

    Q, -Q^-1, Q²,

and a mixed full twist has eigenvalues Q²,-Q^-1. These are distinct at the
primitive fifth root and their tenth powers are all1. The specialized
operators therefore satisfy B22^10=T^10=I. Inserting tenth powers changes
generic Laurent degrees while leaving the root representation unchanged.
Framing-renormalized generators retain the same statement projectively.

## 5. Consequence for the overnight theory lane

The root comparison is a way to implement and verify the finite fifth-root
gate in a smaller, geometrically marked sector. It can also constrain the
candidate's specialized matrix coefficient or stabilizer. It cannot turn
the ordinary cover polynomial's generic endpoints into quotient endpoints
without extra information controlling the multiples of Phi10.

The missing global input must concern the Laurent deformation away from
the root: for example, a bound or a sign rule for the correction term in
`J(t)-V_K(t²)=Phi10(t)R(t)`, or an independently proved valuation statement
for the marked nine-state module. No such rule is supplied by the root
conjugation. The root-fiber test should remain a necessary-condition filter,
while the exact extreme-path analysis stays the principal theory target.
