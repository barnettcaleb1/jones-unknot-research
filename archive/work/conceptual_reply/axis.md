# Retain the band: conceptual assessment of the axis and annular frames

2026-11-03. Conceptual pass; no computation or scan. The hand deductions below are TRUSTED pending peer review. No claim of novelty.

## 1. A decisive calibration: the Whitehead link is not band-trivial

The Whitehead link is a useful winding-zero annular example, but it is **not** one band move from the unknot. Thus it is not a model satisfying the proposed geometric hypothesis.

The Whitehead link is the two-bridge link of fraction 8/3, so its double branched cover is L(8,3), up to orientation conventions. A source for the fraction is Kauffman–Lambropoulou, *From Tangle Fractions to DNA*, Figure 30 and surrounding text: https://www.math.uic.edu/~kauffman/Dresden.pdf .

Suppose a band took it to U. The Montesinos trick converts the band move into distance-one fillings of one torus-boundary manifold, one filling being S3. Consequently L(8,3) would be integral surgery on a knot in S3. Its surgery coefficient would be +8 or -8, because its first homology has order 8.

The linking pairing of an integral ±8 surgery has a generator with self-linking ±1/8. In L(8,3), every generator has self-linking ±3u²/8 with u odd. But every odd square is 1 modulo 8. Hence no generator has self-linking ±1/8. Contradiction.

Equivalently, the standard one-band necessary condition is: if det L=D>0 and L is one band from U, H1(Sigma2 L) must be cyclic of order D and its linking form must represent ±1/D on a generator. The Whitehead link fails. This is a special instance of the already archived linking-form gate, not a new obstruction.

It follows that winding zero, wrapping two, an unknotted axis, and an unknotted pattern are all insufficient to characterize our domain. The fusion band is doing real work even before using Jones data. The statement that the Whitehead link is 'band-trivial, width four or less' should be withdrawn or replaced by a different example.

## 2. Which object should be retained?

I would retain a **marked simple theta curve**, equivalently the link together with its specified fusion band, as the domain. The annular expansion is a useful coordinate system on that object, but the unmarked annular pattern forgets precisely the geometry which supplies the actual unknot filling.

The ambient assertion 'K2 is a two-bridge knot' concerns its isotopy class after filling in the complementary solid torus. It does not classify its embedding relative to the chosen axis. Even both components being unknotted permits nontrivial, complicated relative linking. A continued-fraction formula for the ambient knot does not automatically become a continued-fraction formula for that annular embedding. Such a lift would require a simultaneous position theorem for the knot, the axis, and the fusion band. No such theorem has been supplied.

This is the same general distinction behind the earlier failure of the plat-width argument: simplicity after forgetting a marked object is not simplicity relative to it. A bridge disk may wind around the marked punctures. The useful next theorem would therefore have to state explicitly what simultaneous relative position is forced by our hypotheses.

The hyperelliptic genus-three description is honest bookkeeping of the actual-U locus. But a curve on the standard genus-three surface is not itself a simplification mechanism. Its payoff would be a new compressing disk, a controlled band slide, or an additional actual filling. Otal's theorem by itself still does not guarantee a disk avoiding the marked band.

The recent three-probe result makes the desired output especially precise: construct one more actual nonlongitudinal rational closure while retaining the Jones-supplied determinant data. Framing alignment would then no longer be an extra problem. This is a geometric target, not a claim that the marked theta description automatically supplies it.

## 3. KL(6,2) and faithfulness: a missing implication

There is a useful hardness warning here, but the claimed implication to faithfulness is not yet a proof.

Let C be the set of cap-tangle types under consideration, and let

    S(C)={D : cap_D cup_C is a qualifying split two-arc tangle}.

Suppose the Key Lemma is true and beta is in the kernel of W(6,2). Then the matrix coefficients give

    S(beta C)=S(C)

for every C, subject to keeping the two-arc/no-closed-component domain explicit. That is what follows immediately.

To conclude that beta fixes every cap type requires the separate **separation statement**

    S(C)=S(C') ==> C=C'.

To conclude beta is central then requires identification of the kernel of the braid action on these cap-tangle types. Neither assertion is supplied by generic nondegeneracy of the cell form: that is a linear statement about the skein vectors, whereas C -> [C] may identify distinct tangle types, which is the issue under study.

There may be a route through an appropriate arc/disk complex, but one must first identify this actual split-incidence relation with a known geometric complex relation. It is not enough to invoke standard faithfulness of the mapping-class action on the ordinary arc complex. The cap classes are modulo slides, and splitness of the composed 3-dimensional tangle is not literally disjointness of two chosen planar arc systems.

Thus KL(6,2) is still a very strong target and should not be advertised as an easy rung. But 'KL implies faithful up to center' should currently be labelled conditional on geometric separation and the action-kernel statement, rather than treated as a proved equivalence.

## 4. A disciplined next page

My proposed common page is not a fresh universal noncancellation conjecture. It should specify one geometrically natural subclass of **marked banded annular patterns**, prove a relative-position statement in that class, and then write the actual skein module and closure maps. The output must be an actual disk or actual additional filling, not just a scalar annihilator.

A useful stop rule: if the proposed subclass is described only by the ambient knot types of K1 and K2, it has probably forgotten the band. If it uses only an uncolored Hopf evaluation, it has probably forgotten most of the annular skein class. The Whitehead linking-form calculation is a cheap exact control against the first omission; the explicit kernel of the Hopf functional is a control against the second.

No new theorem deriving such a relative-position statement from the Jones hypothesis emerged here. This is a choice of domain and required output, with the existing crux left visible, not a solution in a new vocabulary.
