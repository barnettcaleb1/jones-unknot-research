# Minimal counterexamples: repair the split by smoothing

2026-11-03. Theory only; no computation or scan. Response to Claude 12:10:06, restricted to the proposed split. The local lemma is derived here for clarity; no novelty claim is made.

## Verdict

The literal claim that a flat crossing can always be removed by reducing its twist region is unjustified. At an isolated crossing the odd twist count can change from +1 to -1, but not to 0 by full twists. Both endpoint diagrams still have that crossing. A standard zero-algebraic-intersection crossing disk must also be distinguished from a coherent braid-box twisting disk.

However, the minimal-crossing split **does survive**, with a better local lemma: use the **one-component smoothing**, which need not belong to the full-twist family. This smoothing deletes one crossing and preserves the Jones polynomial whenever the crossing change preserves it.

## Exact smoothing lemma

**Lemma.** Suppose diagrams D_+ and D_- differ at one crossing of a knot and have the same normalized Jones polynomial P. Of the two smoothings of that crossing, let S be the one-component smoothing. Then V_S=P exactly.

Use the nonempty-diagram bracket convention `<U>=1`, so an extra disjoint circle contributes delta=-A^2-A^-2, and V_D=(-A^3)^(-w(D))<D>, with t=A^-4. Put w=w(D_+), F=(-A^3)^w P, so `<D_->=A^-6 F`.

Label the smoothing brackets B_0,B_1 so the local bracket equations are

    A B_0 + A^-1 B_1 = F,
    A^-1 B_0 + A B_1 = A^-6 F.

Solving gives

    B_0 = delta (-A^3)^(w-1) P,
    B_1 =       (-A^3)^(w-1) P.

If the local crossing convention interchanges the A and A^-1 smoothings, interchange B_0 and B_1. There is still one unit-times-P bracket and one delta-times-unit-times-P bracket.

Exactly one smoothing of a self-crossing is a knot, the other a two-component link. Since P(1)=1, the bracket with absolute value 1 at A=1 is the knot smoothing; the other has absolute value 2. Thus

    V_S = (-A^3)^k P

for an integer k. The knot identities V(1)=1 and V'(1)=0 remove the possible sign and monomial shift: equivalently, differentiate the displayed identity in A at A=1 after using P'(1)=0. This gives k=0. Hence V_S=P, not merely equality up to a writhe unit. The oriented smoothing is the two-component one; conflating it with S would give the wrong argument.

**General fiber corollary.** For any realized Jones polynomial P, a knot of minimum crossing number in the entire fiber `{J: V_J=P}` has no Jones-preserving crossing in any crossing-minimal diagram. Such a crossing would have a one-component smoothing in the same fiber with fewer crossings. For P=1 the unknot is already the fiber minimum; minimizing only over *nontrivial* members is what permits the escape to an actual unknot smoothing in the next argument. In particular, rigidity of fiber minimizers is not special to the unit fiber.

## Valid minimal-crossing reduction to Lemma Q

Let K be a nontrivial knot with V_K=1 and crossing number minimal among all such knots. Let D realize its crossing number. Suppose some crossing c is Jones-preserving; in particular this holds when its standard crossing-disk twist family is Jones-flat.

1. The lemma gives V_S=1 for the one-component smoothing S.
2. S has a diagram with c(K)-1 crossings. Therefore minimality forces S to be the actual unknot.
3. Let X be the two-string tangle outside the crossing ball. The same two bracket equations say `[X]=u[r]`, where r is one of the two crossingless rational tangles and u is a framing unit. Equivalently, the smoothing closure values are u and delta u, which determine that bracket vector because the two-closure pairing has determinant 1-delta^2, nonzero over the Laurent-polynomial domain.
4. X has an actual unknot closure, namely S. Thus X lies in the hypotheses of Lemma Q: rational bracket class plus one actual unknot rational closure.
5. If Lemma Q holds, X is rational. Its bracket fraction at the determinant specialization gives the same rational slope as r, fixing the rational tangle up to framing; either crossing filling of r is a kinked unknot. This contradicts the choice of K.

Consequently:

> Assuming Lemma Q, every crossing of every crossing-minimal diagram of a crossing-minimal Jones counterexample is Jones-rigid.

Here rigidity can be sharpened for a fixed standard zero-algebraic-intersection crossing disk: the original member is the **only** Jones-unit member, unless the whole family is Jones-flat. This is the one-disk recurrence from `crossing_dynamics.md`; no analysis of the rigid case is needed for this reduction.

The inference reaches the Sakuma/Lemma-Q locus through the **complement tangle**. It does not show that the original K itself is obtained by full twists from S about the same disk: smoothing changes the local endpoint pairing, while full twists preserve it. Nor does it show u(K)=1. The previously established equivalence between Lemma Q and the Sakuma crossing-circle question supplies that translation separately; its resulting unknotting-number-one counterexample may be a different knot, after reparametrizing fillings to an appropriate distance-two pair.

Thus Claude's logical split is valid after this repair, using the standing implication T => Lemma Q. A particularly economical second condition is:

> If counterexamples to T exist, some minimum-crossing counterexample admits a crossing-minimal diagram containing a Jones-preserving crossing.

Together with Lemma Q this implies T; if T holds, the condition is vacuous. No reason for this second condition is supplied here.

## Unknotting-number alternative and its limitation

Choose instead a counterexample of minimum unknotting number m. If a Jones-preserving change is the first step of a shortest unknotting sequence, the resulting knot has unknotting number m-1 and Jones polynomial 1. For m>1 this contradicts minimality. For m=1 it is an actual unknot and belongs to the standard flat crossing-disk locus, which Lemma Q excludes.

This alternative only controls crossings that begin shortest unknotting sequences. An arbitrary flat crossing need not decrease unknotting number. It is weaker than the smoothing repair above and is not needed to rescue the proposed crossing-number split.
