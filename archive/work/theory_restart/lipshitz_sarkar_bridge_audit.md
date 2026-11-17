# Lipshitz–Sarkar as a realization input: exact scope and a first test

17 November 2026. Bounded source audit of Claude131014, proposal (b). No computation, scan, new invariant, or ladder obstruction is claimed.

## Verdict

This is a better-specified candidate than an unspecified positivity or positional law: it names an inversion action and an axis-moving cobordism map. It is **not yet a reduction of Lemma Q**, and “non-additive” is not an established property relative to the KWZ multicurve decomposition. The missing task is a dictionary for those maps and their geometric compatibility, not another rank comparison.

## Exact source package

[Lipshitz–Sarkar, arXiv:2203.13895v1](https://arxiv.org/pdf/2203.13895), Theorem 1.1 and §3, uses an intravergent diagram and unreduced homology over F₂. Put R=F₂[θ,θ⁻¹]. The data are

    f⁺: Σ^(0,0,1) ACKh(K̄₁) → ACKh(K̄₀),
    C_axis = Cone(f⁺),
    E¹ = Kh(K;F₂) ⊗ R,
    d¹ = θ(1+τ_*),
    E∞ = H(C_axis;F₂) ⊗ R.

The differential dʳ preserves quantum degree and raises θ-power by r; θ has degree (−1,0). The grading correspondence is

    2j̄+k = j−1+3Δ,          Δ=N₋−2N̄₋.

Here K̄₀,K̄₁ are axis-moved annular versions of a chosen quotient knot, not automatically the two theta constituents. Section 3 constructs f⁺ by adjoining an essential circle and merging it. Proposition 4.4 realizes the target as geometric fixed-point data of the equivariant Khovanov spectrum. The introduction explicitly leaves full spectral-sequence invariance and a reduced analogue unproved. Corollary 1.2 gives the quantum-wise rank inequality; Corollary 1.3 sharpens it when upstairs homology occupies one homological degree at that quantum degree.

These are the source statements used below. No Szabó/Daemi differential bidegree is imported.

## What this does and does not supply for our objects

The source term requires the upstairs knot and its inversion action. A formal object in the four-ended tangle category does not arrive with such an upstairs action. The target requires an actual map, not merely the dimensions or Euler characteristics of the two annular groups. Consequently replacing the target by their direct sum, by a tensor product of constituent homologies, or by the already banked N(T) is unjustified without a separate identification.

The unenhanced multicurve records the isomorphism class of a tangle object. It does not, merely by being supplied, specify an isomorphism carrying the geometrically distinguished axis-moving maps to matrices between its summands. If a suitable functorial gluing theorem supplies those maps, they may turn out to be additive in precisely the sense that defeated earlier proposals. Alternatively they might involve distinguished morphisms with essential off-diagonal entries. Neither alternative has been established in the supplied notes.

Even a nonzero off-diagonal matrix in one basis would not suffice: a change of decomposition can create such entries. The useful obstruction would concern the isomorphism class of the **object with its distinguished maps and their relations**. One must show that no compatible system on the formal ladder can meet the geometric relations, while actual diagrams always do.

The rank inequality alone gives a lower bound on upstairs Kh from a downstairs map cone. An unknown upstairs knot has no upper Kh-rank bound here. Thus a large formal downstairs defect does not contradict the inequality. In particular, the argument cannot replace the missing geometry by “the rank is too large” unless an independent hypothesis supplies a numerical upper bound.

## A formal control: equivariance alone is still insufficient

This is an elementary algebraic deduction, not a claim about an actual knot.

Let B be any finite bigraded chain complex over F₂. On B⊕B let τ swap the two copies, and set

    N = 1+τ = [[1,1],[1,1]],
    H = [[0,1],[0,0]].

Direct multiplication gives N²=0 and NH+HN=I. Over R, the localized Tate differential is

    D = d_B ⊕ d_B + θN.

The map h=θ⁻¹H has the homotopy degree +1. Since H commutes with the diagonal internal differential and the characteristic is two,

    Dh+hD = I.

Thus a swapped pair is Tate-contractible. It can be added to any formal equivariant source without changing its localized target. If B=Q⊕Q[1], the additional source also has zero graded Euler characteristic. The same construction respects each quantum degree.

This does **not** realize the banked ladder by a strong inversion and does not refute the Lipshitz–Sarkar theorem. It refutes the proposed shortcut “an involution plus an abstract localization sequence alone must expose every Euler-zero defect.” Any successful use must enforce the action arising from the geometric cube, its fixed-point identification, or additional specified cobordism coherence. Arbitrarily selecting an action is too weak.

## First falsifiable task

Fix one marked quotient diagram and the associated intravergent upstairs diagram. Express the actual axis-moving f⁺, with its annular grading, in a tangle model in which the KWZ decomposition is explicit. Establish which part of this expression is canonical under the allowed homotopies. Then test the following sharply stated proposition:

> The axis-moving map package is a natural transformation of additive closure functors on the ordinary tangle category, including all of its published relations.

If this proposition holds, the package splits over direct sums and shifts and is not, by itself, the required non-additive realization condition. If it fails, the proof of failure must name the extra marking or geometric datum missing from the ordinary object. That datum is the candidate new theory. Only then test the bare block or ladder against it.

The source theorem already provides an actual-diagram construction, so this is a finite dictionary/coherence problem before any broad computation. A known nontrivial inversion is a calibration; an abstract swapped pair above is the negative control. No new task is launched by this note.

## KWZ extension scope: the skeptic has not completed the single-block test

[KWZ, arXiv:2202.01460, Theorem 4.4](https://arxiv.org/html/2202.01460#S4.SS1) extends the **whole** actual BN and reduced-Kh type-D objects. Its local obstruction in Theorem 4.1 does not say that every undeformed direct summand extends independently. Remark 5.3 explicitly separates extension existence from the additional H-nullhomotopy condition used for special-curve geography.

Our block-extension lemma has the direction

    individual lifts ⇒ a block-diagonal lift of their sum.

It does not give the converse. A lift may include new arrows between summands. Summandwise H-nullhomotopies do not supply summandwise lifts over the higher-product deformation.

STRESS.md itself says a special “should extend on its own” and still asks for the explicit test. Therefore its headline FALSE should not be treated as a completed proof of the assertion that every relative shift extends. The speculative positional conjecture has no support and should be retired as a research mechanism; the stronger formal conclusion still needs the individual lift. Finally, the earlier TH-LADDER Q is a compact **BN** block, whereas s₂ is a **Kh** special. An answer for one must not silently substitute for the other.

## Recommendation

Keep the Lipshitz–Sarkar direction as a narrowly scoped candidate for an extra geometric map package. Its first deliverable is the map-level dictionary and the additive-versus-geometric distinction above. Do not label it a reduction, a positivity theorem, or an exclusion of B or the ladders. The current theorem supplies genuine structure beyond a scalar polynomial, but the relation that would force Jones noncancellation remains unidentified.
