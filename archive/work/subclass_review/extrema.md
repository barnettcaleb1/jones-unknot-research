# The proposed two-bridge extreme-term mechanism

Theory-only read for Claude 20261103-094424. No enumeration or diagram computation. This note addresses the proposed mechanism, not priority of the subclass theorem.

## Verdict

I do not have a counterexample to every possible sector-specific extreme-term theorem for two-bridge strong inversions. But the proposed geometric reason for expecting a product of the usual 2x2 rational-tangle twist matrices is incorrect. It must be replaced by an actual quotient construction before it can support an extremal argument.

## 1. The matrix construction needs an additional geometric operation

Watson's quotient tangle T has double cover E(kappa), the **exterior** of the strongly inverted knot. It is not the rational tangle whose numerator closure is the two-bridge knot kappa.

If one starts with e and repeatedly applies the ordinary boundary-twist and quarter-rotation operators used in continued fractions, every resulting tangle is rational. Its double branched cover is a solid torus. Therefore this construction cannot give the Watson tangle of any nontrivial kappa.

Even a more generous version using arbitrary horizontal and vertical compositions of rational tangles only gives arborescent tangles. Their branched covers are graph manifolds. For a hyperbolic two-bridge kappa, E(kappa) is hyperbolic, so its quotient cannot arise from that arborescent construction either.

Primary sources for this second statement: [Baader–Blair–Kjuchukova–Misev, AGT 23 (2023), introduction](https://msp.org/agt/2023/23-1/agt-v23-n1-s.pdf), defines the arborescent tangle class as the closure of rational tangles under horizontal and vertical composition; [Bonahon–Siebenmann, introduction p.vii](https://dornsife.usc.edu/francis-bonahon/wp-content/uploads/sites/205/2023/06/BonSieb-compressed.pdf), explains the graph-manifold branched-cover correspondence. [Champanerkar–Kofman–Purcell, AGT 22 (2022), introduction](https://www.math.csi.cuny.edu/~ikofman/RAK_AGT.pdf), states the corresponding decomposition for tangle pieces.

This does NOT rule out a genuine 2x2 transfer-matrix recurrence computed by another method. Every final four-ended bracket is two-dimensional. It does mean that such a recurrence needs a verified nonarborescent operation, an appropriate nonrational seed, or a larger intermediate interface; its topological meaning cannot be inferred merely from the continued fraction of kappa. In particular, a rank-two final skein module is not a proof that the geometry can be propagated through a rank-two interface.

## 2. What Snape's extreme-term argument actually proves

[Snape, Proposition 3.4.4, printed p.92 onward](https://theses.gla.ac.uk/39015/1/2018SnapePhD.pdf), identifies the lowest term of P_{-4} for the LONGITUDE annular knot of T(-m,2). It is obtained from a family of extremal states whose signed sum leaves coefficient -1. The all-zero smoothing has no essential annular circles and is not itself in the required annular sector. Thus this is already a constrained-state cancellation argument, not an ordinary adequacy or unique-state theorem.

No implication from that longitude-sector result to a unit extremal coefficient of the BRANCH-SET P_2 follows from the argument. The axis change and the different sector must be implemented and controlled.

## 3. Adequacy distinctions

The underlying branch-set annular knot B is the ordinary unknot in S3. Consequently a nontrivial crossing diagram of B cannot be an adequate ordinary knot diagram: an adequate nonzero-crossing diagram would have nonzero Jones breadth. A sector-specific annular extremum could still survive, but it is not inherited ordinary adequacy of B.

Likewise kappa being alternating says nothing immediate about adequacy of its quotient's encircled link. A preferred Sakuma link has determinant zero, from the established gluing E(kappa) union Q. A nonsplit alternating link has positive determinant (the spanning-tree count), so a nontrivial preferred Sakuma link cannot itself be nonsplit alternating. This does not rule out nonalternating adequacy.

I have neither proved nor refuted full adequacy of all two-bridge Sakuma links. Nor have I certified uniqueness of an x-extremal state in their standard diagrams. Those should remain OPEN, rather than being advertised as properties inherited from the continued fraction.

## 4. A reasonable bounded theory target

Before an all-two-bridge argument, specify one strong inversion and an actual marked quotient diagram for a one-parameter family. Derive the annular sector recurrence from that diagram, including the nonrational operation. Then a statement about a surviving *family* of states is plausible in the same sense as Snape's proof. A claim of a unique state is unnecessary and currently unsupported.

The T(2,m) family is useful as a calibration of this mechanism, but a_2(T(2,m))=(m²-1)/8 is already nonzero for nontrivial odd m, so the project's existing a_2 obstruction already excludes flat quotient tangles there. A new extremal proof for that family would demonstrate a technique, not enlarge the detected class. The genuinely new two-bridge target must eventually include a_2=0 examples such as the previously identified b(31,13).
