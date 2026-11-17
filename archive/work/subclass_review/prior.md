# Targeted prior-art and subclass review

Task: Claude 20261103-094424, proposed branch-set annular extreme-term theorem for strongly inverted two-bridge knots. This was a bounded primary-source read, with no numerical computation or diagram scan.

## 1. What descriptions are actually available

[Snape, §1.2, Proposition 1.2.11 and Figures 1.10–1.11](https://theses.gla.ac.uk/39015/1/2018SnapePhD.pdf), reproduces Sakuma's strong-inversion templates from Sakuma Figure 2.5. They use an even continued-fraction expansion of the two-bridge knot. Snape expressly distinguishes this from Conway's usual normal form. Thus there is an explicit starting diagram for each inversion type, rather than merely an abstract existence theorem.

This does **not** by itself establish a product of ordinary rational-tangle 2x2 twist matrices for the Watson quotient. A quotient whose cover is a nontrivial knot exterior cannot be a rational tangle: the latter has solid-torus cover. In particular, a sequence consisting only of ordinary rational twists and rotations starting from e cannot produce that quotient. A continued-fraction recursion must retain some additional nonrational clasp, connectivity, or quotient operation. Its skein action and markings need to be derived, not inferred from the rational diagram of the original knot.

I searched the complete local primary text of [Watson, arXiv:1311.1085v4](https://arxiv.org/pdf/1311.1085). It gives quotient-tangle constructions and explicit examples, but I did not find the remembered general continued-fraction formula for the Watson tangles of two-bridge or (1,1) knots. The appearances of two-bridge links in its main computations concern branch sets of torus-knot fillings. In particular, Theorem 18 proves thinness of the invariant for torus knots using their lens-space surgery, whose branch set is two-bridge. That is not a formula for quotient tangles of two-bridge input knots.

For inversion scope, Watson Theorems 6–7 state that torus knots have a unique inversion, whereas a hyperbolic knot has up to two, with two precisely when it also admits a free or cyclic involution. Snape's templates treat the two-bridge inversion cases; do not confuse the knot's rational-tangle presentation with its exterior quotient.

## 2. Nearby newer literature, without a Jones deduction

[Di Prisa–Framba, *A new invariant of equivariant concordance and results on 2-bridge knots*, AGT 25 (2025), 1117–1132, arXiv:2303.08794](https://arxiv.org/abs/2303.08794), gives diagrammatic butterfly-link calculations for strongly inverted two-bridge knots and proves a nontrivial equivariant-concordance result. It supplies relevant explicit diagrams and distinguishes Sakuma's eta information from the butterfly information.

This is not a Jones-detection theorem. No implication from flat quotient bracket to vanishing of those eta/Alexander-type obstructions has been established here. It should be used as a source of explicit inversion diagrams, not cited as already proving or disproving the proposed subclass theorem.

In this bounded read I found no primary theorem asserting Jones detection of the strongly invertible unknot for every two-bridge input knot. This is a negative search result, not a claim of novelty or exhaustive literature coverage.

## 3. The torus pilot is already excluded by a banked necessary condition

The project's flat-quotient condition implies a_2(kappa)=0. But

    a_2(T(p,q)) = (p²-1)(q²-1)/24,

which is strictly positive for every nontrivial torus knot; for T(2,m) it is (m²-1)/8. Thus the proposed T(2,m) detection pilot is already a consequence of the established low-order obstruction, independently of inversion diagrams or an extreme-term proof. The project also already records the torus subclass in U5-SF.

The same triage covers all genus-one two-bridge knots: their length-two nonzero even continued fraction has Conway polynomial 1 plus or minus ab z², with a,b nonzero. Its a_2 is nonzero. The first genuinely unaddressed two-bridge cases therefore lie at genus at least two with a_2=0; b(31,13), whose Conway polynomial is 1-2z^4, is an existing project control in precisely that locus.

An extreme-term derivation for torus knots could still be useful as a calibration of an actual quotient recursion. It should not be described as the first positive strongly-invertible result or as new detection scope.

## 4. What Snape's extreme calculation does and does not supply

The primary indexed text of Snape Proposition 3.4.4 confirms that the lowest q term in the longitude-annular P_{-4} coefficient for T(-m,2) is -q^{-4m-1}. His proof sums a selected family of states to coefficient -1; it is not merely “the all-zero state is unique.” In fact the all-zero state does not itself meet the required annular-circle condition.

Consequently this is a real noncancellation mechanism, but its transfer to branch-set P_2 needs a new argument. The source does not establish that the full Sakuma link is adequate or that the branch-set coefficient has a unique extremal state. Those claims must not be attributed to it.

Recommendation: if the subclass is pursued, first derive a correctly marked quotient recursion for the even continued-fraction templates and state the surviving-state claim on the a_2=0 locus. That is the actual new geometry. The ordinary rational-tangle matrix product alone cannot be the whole quotient construction.
