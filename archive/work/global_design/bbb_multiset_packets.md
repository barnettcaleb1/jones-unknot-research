# BBB-MULTISET: anchored packets and a bundled-puncture repair

Date: 2026-11-03. Holder: Codex. Explicit-braid attacker: Claude.

Status: the universal multiset assertion remains OPEN. The covering-space and bundle propositions below have written proofs, an independent internal read, and Claude's independent read in message161336; the board label remains TRUSTED. No assertion of Burau faithfulness or of novelty.

## 1. The actual target and its normalization

Use BBB's unreduced Burau representation and right action. Let Phi be a nontrivial proper product in Brun_4 with rho_4(Phi)(-1)=I. Let Gamma be the unmodified auxiliary-puncture push of Proposition 6.7, before its Furthermore modification. Fix the same lift of alpha and the common based lifts of the compared arcs

  b_1 = (beta_3^*) f(Phi) Gamma,   b_0 = (beta_3^*) Gamma.

The held statement asks that their coherent height multisets differ even up to translation. For excluding a kernel element, the weaker ANCHORED inequality M(alpha,b_1) != M(alpha,b_0) suffices: a kernel element requires exact equality with these lifts. Independently renormalizing the two polynomials would discard useful information.

All statements invoking the particular disk sequence or coherence are conditional on the geometrical assertions in BBB Lemmas 6.3–6.6 holding for this actual push. Those assertions are being tested, not silently upgraded.

If W_i=k_(i+1)-k_i is an old disk increment, the proposed disk correspondence gives

  s_1=0,
  s_(i+1)-s_i = sgn(W_i) if |W_i|=4, and 0 otherwise,
  k'_i = k_i+s_i.

A separately chosen initial lift adds a common offset. This is SIGNED winding, not unsigned nesting depth. In BBB section 7 the displayed final exponents decrease by one across a negative four-disk, despite the prose saying “increase.” No alternation of four-disk signs, or two-value bound on s_i, has been established.

## 2. A colored probe of the same Burau operator

Give meridians of the four old punctures weight t and the auxiliary puncture weight u. The resulting Z^2 cover has relative first homology, relative to all lifts of the boundary basepoint, free of rank five over

  R = Z[t^{+/-1},u^{+/-1}].

In a compatible meridian basis the action of f(Phi), which is supported in the old four-punctured disk, is

  rho_4(Phi)(t) direct-sum 1.

The pure push Gamma preserves the coloring. The lifted intersection pairing of alpha with each compared arc is a finite Laurent polynomial M_i(t,u). Write

  D(t,u)=M_1(t,u)-M_0(t,u).

**Kernel implication.** If rho_4(Phi)(t)=I, then D(t,u)=0.

Proof: f(Phi) acts identically on the relative module just described; composing with Gamma and applying the lifted intersection functional preserves equality. Equivalently, D is a matrix coefficient of rho_4(Phi)-I, after extending scalars and composing with the colored matrix of Gamma. No faithfulness assertion for a colored representation is used.

On the repaired arc, the colored exponent at an intersection is (k_i,s_i), up to the fixed initial deck offset. The usual BBB polynomial is M_i(t,t). If BBB parity holds, M_i(-x,-y) has coefficients of one common sign. Ordinary parity records k_i+s_i modulo two, so this follows term by term.

**Packet constraint.** If rho_4(Phi)-I is divisible by (t+1)^r, then D(t,u) is divisible by (t+1)^r in R. In particular, on the BI_4 slice,

  D(-1,u)=0.

Consequently, writing D=sum_b d_b(t)u^b, every d_b(-1)=0. Under two-sided coherence and the common lift convention, each fixed-u packet has the same total mass on both sides. At depth r its first r old-variable jets agree as well.

This identifies what the lift can and cannot do. The maximum auxiliary height and its multiplicity cannot separate the arcs on BI_4. A useful face comparison must distinguish the FULL old-t profile within a packet. It cannot be a count comparison in new notation.

## 3. Realizing the extra variable by an ordinary braid

**Bundle proposition.** Replace the auxiliary puncture by q nearby punctures in a small disk, for a positive integer q. Push that disk along the same Gamma, with fixed planar framing. Denote the resulting pure braid by Gamma_q and the stabilization of Phi by f_q(Phi). Then the ordinary Moody polynomials of the two compared old arcs satisfy

  M_i^(q)(t)=M_i(t,t^q),    D_q(t)=D(t,t^q).

Proof: outside the moving little disk, the pushed homeomorphism can be chosen to agree with the original one. The old arcs never enter its interior; they have exactly the same intersections with alpha. A loop formerly winding once around the auxiliary puncture now winds around all q punctures, while its old-puncture winding is unchanged. Thus each signed term t^a u^b becomes t^(a+qb). Use common based lifts throughout. An internal twist of the little disk does not affect these old arcs.

For odd q, every parity check is preserved: a+b and a+qb have the same parity. This includes the replacement of a five-disk by a disk containing 4+q punctures. The proposition itself does not require parity.

**Finite specialization bound.** Suppose D is nonzero. Let B be the range of its old-t exponents:

  B = max{a : [t^a u^b]D != 0} - min{a : [t^a u^b]D != 0}.

For every integer q>B, D(t,t^q) is nonzero.

Proof: if distinct support terms collide, then a-a'=q(b'-b). When b differs from b', the right side has absolute value at least q and the left side at most B, impossible. When b=b', collision requires a=a', and those terms were already aggregated. No support terms cancel after specialization.

Choose any odd q>B. This gives an ordinary stabilized Burau witness for the ORIGINAL Phi; stabilization acts as rho_4(Phi) direct-sum I_q. In particular, a collapse at the original q=1 can be repaired by a specified push in a larger disk if D is nonzero. A support bound before aggregation is also sufficient.

If D is identically zero, this entire bundled family is blind. The proposition does not assert otherwise. Its purpose is to make one exact colored calculation decisive and to supply a geometric repair, not to claim universal nonvanishing.

## 4. The geometric lemma I will hold

An occupation-measure equality pairs intersections of b_0 and b_1 with equal deck heights. Closing their based prefixes using the appropriate alpha segment gives loops of total puncture winding zero. Such a loop need not be embedded: zero winding alone says nothing about whether it encloses punctures in cancelling regions.

**Matched-ribbon extraction, OPEN.** For the actual proper-product configuration and its unmodified nested-band push, equality of the anchored height multisets permits a comparison matching with an outermost matched loop that, after undoing the push ribbons, is an embedded bigon-forming polygon forbidden by the proper-product conditions.

The intended mechanism is geometric: an embedded loop of total winding zero encloses no puncture, and the permitted polygon would contradict properness. The two missing steps are explicitly (i) extraction of an embedded loop from the equal-height matching, and (ii) identification after undoing ribbons with one of BBB's permitted polygon types. Neither follows merely from equal Laurent polynomials, from a formal height walk, or from nestedness without a planar proof.

The colored repair allows the stronger matching requirement of equal old and auxiliary heights. It may make ribbon extraction possible when equal total height does not. This is a repair candidate, not a proof of extraction. In particular, a proposed three-punctured-face argument must explain the forced (t+1)^r factors before it can invoke a coherent Burau_3 pairing.

## 5. The next decisive object

Claude retains the construction and ordinary comparison for the explicit Phi in BBB-GAP.md. No duplicate search is needed. Once Gamma is specified, the same relative/Fox matrices with weights (t,t,t,t,u) produce the colored difference. Retaining signed old/auxiliary heights, if the geometric construction already produces them, avoids losing the distinction at u=t.

- Failure of parity attacks the relevant geometric lemma.
- An ordinary anchored inequality certifies this Phi is not in the kernel.
- Ordinary equality but colored inequality supplies a bundled repair with the explicit bound above.
- Colored equality makes this push and all its bundles blind and supplies the actual object against which to test matched-ribbon extraction.

None of these outcomes alone proves the universal statement. Burau_4, G2-TWIST and T remain OPEN.

Sources read: the local primary text bbb-gap/bbb.txt, especially sections 2, 3, 6 and 7; read-bbb/bbb.md; ref-transfer/ref-transfer.md, all in /Users/calebbarnett/jones-lanes/g2-proof/. The two-variable and bundle arguments above are this pass's deductions. The disk assertions are kept conditional.


## 6. Brunnian localization refinement (reply162630)

The geometric endpoint need not be an empty polygon. BBB-LOCAL proves that a simultaneous comparison confined to pairwise disjoint disks, each visited once and each missing one of p1,p2,p4, already forces a Brunnian Phi to be trivial. A terminal disk containing p3 is allowed. The proof uses actual deletion isotopies and one-syllable-per-factor free-product normal form. Deriving this decomposition from equal occupation polynomials remains OPEN. See bbb_localization.md; this is a weaker sufficient endpoint for the same held target, not a universal nonvanishing result.


## 7. Actual mixed-splice gap (reply163948)

Primary Lemma 6.6 permits a side following a four-disk to splice through an original beta* segment to a three-disk containing p1,p2,p3 or a one-disk containing p4. Thus selecting an auxiliary-height packet does not itself eliminate old-puncture excursions. Nesting supplies order along gamma2, not automatically along the compared arcs. The global Brunnian/proper-product localization implication remains unproved. A separate exact theorem now detects the nested mixed-commutator family in bbb_mixed_returns.md, including arbitrary specialization depth; it does not certify the chosen scalar probe or all permitted splices.
