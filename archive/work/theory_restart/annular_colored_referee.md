# Annular, curve and coloured audit of Claude's 23:12 letter

15 November 2026. Scope: assertions 1(a), 1(c), 1(e) of
`20261115-231228-claude` and the corresponding parts of
`~/jones-lanes/theory-restart/notes/2026-11-15b-sutured-side.md`.
The spectral sequence's sutures and its proposed genus bound are audited separately.
No sample search is used here.

## Verdict

The identification of the bullet augmentation with the top annular-weight complex
survives, after specifying the seam and the overall grading shifts. The asserted
semisimple `sl_2` decomposition does **not** hold over the stated field `F_2`,
already for the trivial two-strand braid. The curve interpretation is valid as a
finite test-arc/intersection model; the unqualified wrapped-Floer formula needs a
boundary/stopping convention that the cited closure pairing theorem does not
supply. The doubled-tangle identity `J(T_K)=J_3(K)` is correct with zero framing
and the normalization `J_3(U)=1`.

These identifications explain the object `N(T)` and connect it with known
invariants. None of them supplies END or the new Newton-polygon assertion. In
particular, an inequality about total rank cannot control cancellation of its
graded Euler characteristic.

## 1. Top annular weight: a chain-level identification

Use the horizontal tangle direction in which the matching `b=Q_0` is the
identity. Form the annular closure by joining its two incoming ends to its two
outgoing ends, and mark the annular seam at that joining. The seam meets the
diagram twice. For every complete resolution:

* a `b` resolution closes to two essential circles;
* a `c` resolution closes to an inessential circle;
* circles that were already closed inside the cut disk are inessential.

Consequently the annular `k=2` complex has exactly the `b` resolutions, with both
essential circles labelled `v_+`. The labels on inessential circles are the
ordinary Khovanov labels. Delooping those inessential circles is the same
delooping used in the Bar--Natan tangle complex.

On these resolutions, dots on an essential strand lower annular weight, and
saddles into or out of the other matching leave the top-weight sector. They
therefore induce zero in the annular associated graded at weight 2. After
delooping, precisely the scalar identity coefficients on `b` remain. This is
the bullet augmentation: kill `c`, kill all nonidentity paths/dots, and retain
the identity of `b`.

Thus, with consistent diagram conventions,

`C_AKh(annular closure(T), k=2) = q^2 F_b C_BN(T)`

in the unnormalized convention in which the two open strands of the identity
have degree zero and `deg(v_+)=1`. If `N` is defined after an additional tangle
normalization, the same normalization must be included on the right. For the
trivial identity tangle this statement says that its one generator of degree
zero becomes the all-plus state of the two essential circles, quantum degree
2. This calibration is essential: an equality in absolute gradings without it
is false even for the identity. One can instead use the adjusted annular degree
`j'=j-k`, in which the two identity generators have matching degree zero.

This argument works over `F_2` and does not use an `sl_2` splitting. It also
explains the familiar balanced-tangle summand in Grigsby--Wehrli. Their
*Khovanov homology, sutured Floer homology, and annular links*, arXiv:0907.4375v2,
Theorem 3.1, identifies the cut balanced-tangle sequence as a direct summand
of the annular sequence. The top-weight description here uses the additional
fact that our chosen cut has exactly two strands and uses the non-backtracking
resolution matching.

Appending a two-strand braid does not preserve the raw absolute bigrading.
The bullet augmentation of a crossing complex is a one-generator complex,
because its other resolution is killed. Hence appending `sigma^n` tensors
with that one-generator factor. It preserves `N` **up to its known homological
and quantum shift**. The shift depends on crossing signs and on whether one
uses a framed bracket normalization or an oriented Jones normalization.
Therefore the safe statement is that the annular weight-2 homology of
`T sigma^n` is a grading shift of `N(T)`; record the shift before comparing
absolute polygons or Rasmussen data. No claim about the unchanged integer
coordinates of a polygon should use the unshifted assertion.

## 2. The characteristic-two representation-theoretic correction

Grigsby--Licata--Wehrli, *Annular Khovanov homology and knotted Schur--Weyl
representations*, arXiv:1505.04386v1, Section 2.1, explicitly works over
`C`. Its semisimple representation statements cannot be transported verbatim
to `F_2`.

An explicit obstruction is the annular closure of the identity two-braid. Its
annular homology is `V tensor V`. In characteristic two put

`a=v_+ tensor v_+`, `w=v_+ tensor v_- + v_- tensor v_+`,
`d=v_- tensor v_-`.

For the usual raising/lowering operators,

`F(a)=w`, `E(d)=w`, `E(w)=F(w)=0`.

The span of `a,w,d` is the three-dimensional Weyl submodule. The common kernel
of `E` and `F` in `V tensor V` is exactly the line spanned by `w`. Thus every
trivial submodule lies inside that three-dimensional submodule, and there is
no complementary trivial line. In particular

`V tensor V != V_2 direct-sum V_0`

as an `sl_2` module in characteristic two. The ordinary Cartan eigenvalue
also does not recover the integer annular weight in characteristic two.

Over characteristic zero, a module whose annular weights are contained in
`{-2,0,2}` does split into copies of the three-dimensional irreducible and the
trivial representation, and its top-weight multiplicity space is `N` with the
shift just described. Over `F_2`, retain the annular weight decomposition and
the top-weight chain identification, but delete the claimed semisimple
decomposition. This correction does not affect the top-weight spectral
sequence or the generic Temperley--Lieb argument below.

## 3. What the curve picture does and does not establish

Kotelskiy--Watson--Zibrowius, *Immersed curves in Khovanov homology*,
arXiv:1910.14584v2, Section 5.1, distinguishes the parametrizing arc system
`{b,c}` from its dual arc system. The parametrizing arcs have ends on the
outer boundary corresponding to the distinguished puncture. Invariant
Bar--Natan curves instead have their ends on the inner boundary components.

In the curve reconstruction of a reduced type-D structure, generators with
idempotent `b` are precisely intersections with the parametrizing arc `b`.
After cancellation of identity arrows, their finite test-arc complex has no
remaining differential: a removable puncture-free bigon is the corresponding
identity cancellation. Nonidentity paths around punctures are killed by the
augmentation. Local-system fibres contribute their dimensions and grading
labels. This gives the useful, precise statement:

`N(T)` is the graded intersection vector space of the reduced Bar--Natan
curve with the bullet parametrizing arc, equivalently its augmentation
pairing.

Writing this as `HF(BN(T),A_b)` is acceptable **if** `HF` is defined to be
that finite/stopped test-arc pairing. It is not a direct invocation of the
ordinary link closure Pairing Theorem in KWZ Section 7. That theorem pairs
the mirrored invariant of a pointed tangle with another tangle invariant;
the classification's wrapped morphism model wraps the allowed invariant
curves at inner boundaries. The parametrizing arc has ends at the other
boundary, and its role must be specified. A general stopped-category
identification is plausible, but should not be promoted to a cited theorem
without the test object and its stops.

Likewise, saying that this is the *shape* of a meridional Floer pairing is a
useful analogy. It is not yet a grading-preserving functor from these
Bar--Natan curves to bordered knot Floer curves. The spectral sequence needs
its own sutured-manifold proof; no polygon restriction follows merely from
the similar surface pictures.

## 4. Doubled tangles and the 3-dimensional coloured Jones polynomial

Lewark--Zibrowius, *Rasmussen invariants of Whitehead doubles and other
satellites*, arXiv:2208.13612v2, **Definition 3.9** defines `T_K` by removing
a trivial band from the zero-framed two-parallel of `K`, with
`T_K(infty)=U`, `T_K(0)` the zero parallel, and linking number zero.
**Remark 3.10** identifies its branched double cover with `E(K#K)` and its
inversion with the summand-swapping inversion. (The definition is not 3.5.)

The scalar calculation is independent of the characteristic-two categorical
issue. Work over the generic bracket field, write

`T_K = y I + x e`, `e^2=delta e`,

and split by the usual Temperley--Lieb projectors

`p_0=e/delta`, `p_2=I-e/delta`.

The eigenvalues are

`lambda_0=y+delta x=u`, `lambda_2=y=uJ`.

The `p_2`-cabled, zero-framed `(1,1)`-tangle of `K` is precisely the
highest-weight-two (three-dimensional colour) knot tangle. Its scalar is
the reduced coloured Jones polynomial normalized by `J_3(U)=1`. The
colour-zero summand is trivial and has scalar 1. Therefore the actual
zero-framing normalization gives

`u=1`, `J(T_K)=J_3(K)`.

For a blackboard-framed input one must first insert the usual framing
correction; using the ratio `y/u` with a stated preferred framing avoids
silently comparing differently framed polynomials. The Laurent-variable
substitution must also be the same on both sides.

Consequently Lemma Q, if true for all quotient tangles, would imply that
the three-dimensional coloured Jones polynomial detects the unknot:
`J_3(K)=1` makes `T_K` flat; Lemma Q makes its covering knot `K#K` trivial;
genus additivity then makes `K` trivial. This is a valid difficulty
calibration, not a proof of coloured detection and not its converse.

## Sources actually checked

* Grigsby--Wehrli, arXiv:0907.4375v2,
  <https://arxiv.org/html/0907.4375v2>, especially Theorem 3.1 and the
  introduction's weight-space interpretation.
* Grigsby--Licata--Wehrli, arXiv:1505.04386v1,
  <https://arxiv.org/html/1505.04386v1>, Sections 2.1 and 4; published in
  *Compositio Mathematica* 154 (2018), 459--502.
* Kotelskiy--Watson--Zibrowius, arXiv:1910.14584v2,
  <https://arxiv.org/abs/1910.14584>, local primary TeX Sections 5 and 7
  in `lit/kwz-immersed/src/tex/sections/05Classification.tex` and
  `07Pairing.tex`.
* Lewark--Zibrowius, arXiv:2208.13612v2,
  <https://arxiv.org/abs/2208.13612>, Definition 3.9 and Remark 3.10;
  *J. reine angew. Math.* 816 (2024), 241--296. Local primary TeX
  `lit/bn-torsion/src/2208.13612/sections/basic-definitions.tex` and the
  paper's numbered text were checked against each other.
