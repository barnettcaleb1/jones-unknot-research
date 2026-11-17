# Single-example referee: an actual failure of endpoint survival

16 November 2026. Assignment: audit only the stored example `ce1` from section 7 of the Floer lens report. No search or new family computation was performed. One fresh computation over F₂ was run from the original half-diagram, as authorized.

## Verdict

**The example survives the independent checks in this report.** It is a valid symmetric diagram of a knot, and kht++'s quotient construction supplies an actual four-ended quotient tangle with an unknot closure. A fresh F₂ run reproduces the claimed minimal Bar–Natan chain exactly, despite using a different simplified quotient diagram. Independent extraction of the bullet generators gives precisely two generators at the maximal quantum grading:

\[
(h,q)=(4,8),(5,8).
\]

Their signed sum is zero. Thus universal **END**, **NP**, and the stated **PARALLELOGRAM LAW** fail. The F₂ special-curve output also refutes universal **TILT**. The example does not refute Lemma Q: its J polynomial is nonunit.

Moreover, the equivariant sum with its mirror has cancellation at **both** quantum endpoints, by the already audited tensor-product theorem. Therefore weakening the proposed reduction to “at least one endpoint survives” does not repair it.

## 1. Actual diagram and the unknot-closure condition

The original half-diagram word is

```
s.r1.x2.y1.y0.r2.y0.y1.y0.y1.x2.u3.u1
```

with top orientation `,1`. The original saved input is

`/Users/calebbarnett/jones-lanes/theory-restart/mech2/floer/work/examples/check/ce1.kht`.

The program's documented symmetric-diagram input requires: equal numbers of caps and cups; none at axis index zero; valid local strand indices; and one component after completing the symmetry. These are genuine restrictions: an arbitrary string beginning `s.` is not automatically a strong inversion of a knot.

I checked those restrictions for this word. Using the explicit symmetry expansion in `Tangle::complete_symmetry()` and adding the top cap, the closed Morse diagram is

```
l0.r1.l1.x4.x0.y3.y1.y2.r4.l2.y4.y5.y3.y4.y5.y3.x6.x2.u7.u1.u3.u1.u0
```

All indices are valid, the end width is zero, and there are exactly 13 crossings. An independent connectivity trace that creates paired endpoints at each cap, swaps them at each crossing, and joins them at each cup has **one connected component**. This verifies a 13-crossing diagram of a knot; it makes no claim that its crossing number is minimal.

The half-diagram construction completes by a half-turn about the displayed axis. The knot meets that fixed axis at the two cap endpoints. Hence it gives a strong inversion. The quotient construction removes the invariant neighborhood of the knot and uses the axis as its branch locus. Restoring the meridional rational filling restores the original unknotted rotation axis. Thus the designated infinity closure is topologically the unknot, independently of Jones evaluation.

This is exactly the construction specified in the kht++ primary documentation, `docs/Input.md`, subsection “Strongly invertible knots”, and `docs/Options.md`, subsection “Quotients of strongly invertible knots”. The source `sources/modules/Tangles.cpp`, `Tangle::quotient()`, implements the doubled-band diagram and the writhe correction; this audit checked that the current halfword satisfies its topological input conditions. A monomial bracket alone would not certify the unknot closure, and is not used for that certification here.

## 2. Fresh F₂ reproduction

Fresh input and output are retained in

`work/theory_restart/ce1_referee_run/`.

The run was

```
/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++ \
  -c2 -q -s examples/check/ce1.kht
```

from that directory, with full output in `ce1_c2.log`. It exited successfully. The simplified quotient word differs from both saved F₃/Q simplifications and the old F₂ simplification, but the resulting `examples/check/ce1/cxBNr-c2-qs` agrees component by component with the previous F₂ file.

The output has one isolated bullet at `(0,0)` and eight square components with initial bullet bidegrees

\[
(-1,-2),\ (-5,-8),\ (-3,-4),\ (-2,-2),\
(-7,-10),\ (-6,-8),\ (-9,-12),\ (-13,-18).
\]

Each square has bullet offsets

\[
(0,0),\ (5,8),\ (6,10),\ (1,2).
\]

Consequently `dim N = 1 + 8·4 = 33`. The greatest q is 8, attained only by the `(6,10)` corners of the squares beginning at `(-1,-2)` and `(-2,-2)`. Their h values are 5 and 4. The least q is −18, attained once at `(-13,-18)`.

This is a fresh computation in the same invariant implementation, not a second independent implementation. Its useful independence is that it starts from the halfword, takes and simplifies the quotient anew, and does not load the stored homology answer.

## 3. Independent chain parsing and field scope

I independently parsed the arrow words, rather than extracting N from the formula involving special-curve offsets. For each displayed arrow, the homological increment is its direction ±1; the quantum increment is the direction times the algebraic degree, 1 for S, 2 for D, and the appropriate multiple for powers. Suppressed S between equal idempotents means S². Every cyclic component closes with consistent gradings.

The saved files checked are:

* F₂: `floer/work/examples/words/wef4c96470e/cxBNr-c2-qs`;
* F₃: `floer/work/examples/check/ce1/cxBNr-c3-qs`;
* rationals: `floer/work/examples/check/ce1/cxBNr-c0-qs`;

under `/Users/calebbarnett/jones-lanes/theory-restart/mech2/`.

All three saved outputs have the same complete multiset of 33 bullet bidegrees, although their component decompositions differ. The extracted data, including each component's bullets, are in `ce1_referee_run/parsed_certificate.json`.

Over F₃ and Q the components are three P₁-by-D squares, three P₂-by-D squares, and a nine-bullet arc. The P₂ square beginning at `(-2,-2)` supplies the top bullet `(4,8)`. The arc has bullet sequence

\[
(0,0),(-5,-8),(-4,-6),(3,6),(2,4),(5,8),
(4,6),(-1,-2),(0,0),
\]

and supplies `(5,8)`. Thus the top cancellation is not an artifact of the F₂ component-decomposition formula.

**Two necessary limitations:**

1. The Q log explicitly warns that rational arithmetic in this build is experimental and integer overflow is not checked. Its agreement is useful corroboration, not an independently audited exact characteristic-zero certificate.
2. Agreement over F₂, F₃ and Q does not establish that the integral groups are Z, nor rule out torsion at other primes. The Floer report's sentence making that inference is too strong. The exact F₂ counterexample already suffices for the stated universal F₂ laws.

## 4. What is refuted, and what is not

At q = 8,

\[
\sum_h(-1)^h\dim N^{h,8}=1-1=0.
\]

END fails at the upper endpoint. The corresponding delta values are `8/2−4=0` and `8/2−5=−1`, so NP fails. The proposed parallelogram condition implies NP, so it fails as well.

The F₂ Khovanov curve output has actual specials at offset 4 on both levels 0 and 1, with no larger offset. Thus the maximal offset fails to strictly decrease between these adjacent occupied levels. This is a direct failure of TILT, without invoking a longer-special expansion.

The Euler polynomial is

\[
J(t)=-t^{-9}+t^{-8}-t^{-6}+t^{-5}+t^{-1}+t^2-t^3.
\]

In particular it is nonunit. The top homology degree q = 8 cancels, and the next surviving upper polynomial degree is q = 6. Hence the tangle remains nonflat, as Lemma Q predicts. The example refutes the proposed endpoint-survival sufficient mechanism, not the desired knot-detection conclusion.

Nothing in this verification identifies the actual differentials in the sutured sequence. A diagram of two candidate higher maps between four squares is a formal explanation consistent with ranks, not a computation of the geometric spectral sequence. The proposed “quadruple law” and “corrected outline” remain new conjectures and are not certified by this example.

## 5. Both endpoints can fail in an actual quotient tangle

Use the audited equivariant-sum rule

\[
N(T\mathbin{+}T')\cong N(T)\otimes N(T')
\]

and take `T'` to be the mirror tangle. Mirroring negates h and q up to a uniform shift. In centered conventions, the source above has its top at q = 8 with bullets `(4,8),(5,8)` and its bottom at `(-13,-18)`.

For the sum with its mirror, the greatest q is 26. Its only generators are

\[
(17,26),(18,26),
\]

and the least q is −26, with only

\[
(-17,-26),(-18,-26).
\]

Each pair has opposite parity, so **both** endpoint Euler characteristics vanish. Uniform framing or grading normalization does not change these cancellations. The sum is geometrically the equivariant connected sum of the two actual strong inversions, so it remains within the unknot-closure class.

Its J polynomial is `J(t)J(t^{-1})`, up to any convention unit. This is nonunit: if a product in the Laurent polynomial domain were a unit, both factors would be units. Thus this is another actual failure of an outline mechanism, not a counterexample to Lemma Q.

No additional invariant run is needed for this corollary. It rules out the immediate weakened proposal that every nontrivial quotient tangle has *at least one* noncancelling endpoint.
