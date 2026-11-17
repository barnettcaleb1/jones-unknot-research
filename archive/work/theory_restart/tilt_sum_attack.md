# Connected sums, mirrors, and the TILT reduction

15 November 2026. Scope: conceptual attack requested in `collab/msgs/20261115-183136-claude.md`. No family sweep was run and no scaffold was edited. One specified test, the trefoil plus its mirror, was checked algebraically and compared with its already-existing local multicurve output.

## Findings

1. **The Jones-flat fiber is closed under factors for the specified equivariant connected sum.** In preferred longitude coordinates, `J(T#S)=1` if and only if `J(T)=J(S)=1`. This follows from multiplicativity plus a stronger normalization fact: `J≡1 mod δ²`. It does not require TILT, OVERHANG, or a special-component classification.
2. **Mirroring cannot create flatness through cancellation.** `J(T) J(T*)=1` if and only if `J(T)=1`. Additive first-order invariants can cancel, but the Laurent breadth cannot.
3. No actual counterexample to TILT or OVERHANG was obtained. The specific trefoil–mirror test satisfies TILT.
4. There is a **source-level obstruction to the stated universal reduction**: the assumption that every special component has the shortest observed length is contradicted by an explicit existence statement in Kotelskiy–Watson–Zibrowius. This does not refute TILT. It requires the proposed reduction to be extended to longer special components, with extrema measured on their entire Euler support rather than their central labels.
5. Multiplicativity or decategorification alone cannot prove TILT: opposite-parity pairs at the same quantum offset leave all these polynomial data unchanged. A realizability theorem is still required.

## 1. Exact bracket algebra and the normalization that removes units

Work over `R=Z[A,A^-1]` and let `δ=-A²-A^-²`. Use the preferred longitude frame from the letter, with reference tangle `e`, cup–cap tangle `i`, and

`[T]=x i+y e`, `δx+y=u`, `u=±A^m`.

The last identity is the actual unknot-closure condition; `u` records its framing. Normalize

`a=x/u`, `J=y/u=1-δa`.

The second standard closure, namely the longitude closure, has reduced bracket `x+δy`, up to the fixed harmless framing unit. Its branched double cover is zero surgery on the covering knot, and consequently its determinant is zero.

Let `ζ=exp(πi/4)`, so `δ(ζ)=0`. Evaluating the longitude closure gives `x(ζ)=0`. Since `x` is an integral Laurent polynomial and the minimal polynomial of `ζ` is `A⁴+1`,

`A⁴+1 divides x`, equivalently `δ divides x` in `R`.

Dividing by the unit `u` preserves divisibility. Therefore

**`J=1-δ² b` for some `b∈R`.**

This gives a direct proof of the preferred-framing divisibility used in the local notes. It uses the longitude marking; it is not a statement for an arbitrary uncalibrated rational reference. The determinant-zero condition is doing essential work.

### Unit rigidity lemma

If `J∈R^×` and `J≡1 mod δ²`, then `J=1`.

Indeed, every unit of `R` is `ε A^n`, with `ε=±1`. For nonzero `n`, every nonzero complex root of `ε A^n-1` is simple: its derivative there is nonzero. But divisibility by `δ²`, or equivalently by `(A⁴+1)²`, requires a double zero at `ζ`. Thus `n=0`; the congruence then excludes `ε=-1`.

The argument is over the characteristic-zero Jones coefficient ring. Do not replace it with a characteristic-two derivative argument: the Khovanov coefficients may be `F_2`, but the integral graded Euler characteristic and Laurent units here are over `Z`.

An equivalent formulation useful for the board is:

**In preferred longitude coordinates, “J is a Laurent unit” and “J=1” coincide.**

Thus the gap between monomial Jones-rationality and exact flatness disappears after this peripheral normalization. This is stronger than merely evaluating `J(ζ)=1`: a single evaluation allows many nonconstant monomials, whereas the double-zero congruence excludes them.

## 2. Equivariant sums and mirrors

For the stacking operation corresponding to the stated axis-preserving equivariant sum, take `e` as the composition identity and use the Temperley–Lieb relations

`e²=e`, `ei=ie=i`, `i²=δi`.

Writing each normalized input as `a_i i+(1-δa_i)e` gives

`a_(T#S)=a_T+a_S-δ a_T a_S`,

`J_(T#S)=J_T J_S`.

Both the coefficient-of-`e` map and the reduced unknot-closing map (`e↦1`, `i↦δ`) are characters. This derives the formula instead of extrapolating it from the trefoil check. In the local pretzel coordinates of `tools/jq_tangle.py`, the rational prototypes `vert(λ_T)` and `vert(λ_S)` compose to `vert(λ_T+λ_S)`; their framing factors also multiply. That is the same calculation before the preferred-frame change.

Since the product of two elements of a commutative ring is `1` only when each is a unit, the unit rigidity lemma proves

**`J_(T#S)=1 ⇔ J_T=J_S=1`.**

The same holds for any finite iterated sum. If the output is flat and one assumes the conjectured detection theorem for all factors, each factor is trivial. More modestly and unconditionally, if even one factor has a verified non-flat Jones bracket, the composite cannot be flat. This conclusion applies to the particular equivariant-sum operation with compatible preferred markings. It is not a claim that every strong inversion on a composite knot decomposes in this factor-preserving way; involutions that permute summands require separate treatment.

Under the strongly invertible mirror, the compatible normalized invariant is

`J_(T*)(A)=J_T(A^-1)`.

Hence

**`J_(T#T*)=1 ⇔ J_T=1`.**

This also follows without the double-zero lemma up to a unit, because the Laurent breadth of `J·bar(J)` is twice the breadth of `J`; the lemma removes the remaining monomial possibility. More generally,

`span_A(J_T J_S)=span_A(J_T)+span_A(J_S)`

for nonzero Laurent polynomials, because the extreme coefficients multiply without cancellation. Here `J` is never zero, since it is `1` modulo `δ`. Also `span_A(J)=0` forces `J=cA^n`; evaluation at `ζ` gives `|c|=1`, and the lemma then forces `J=1`. Consequently breadth is a nonnegative additive obstruction whose zero fiber is precisely the flat fiber.

This does not detect topology by itself. The unresolved assertion is still that a nontrivial strong inversion has positive `J` breadth. It does show why a strategy that tries to manufacture flatness by multiplying a non-flat factor by its mirror cannot work.

## 3. One identified test: trefoil plus its mirror

The local explicit bracket calculation gives, with `t=A^-4`,

`J_T(t)=t⁷+t⁴-t³`.

The single symbolic test made in this pass multiplies this polynomial by its mirror. Exact integer arithmetic gives

`J_T(t)J_T(t^-1)=-t⁴+t³-t+3-t^-1+t^-3-t^-4`,

and

`J_T(t)J_T(t^-1)-1=-(t-1)²(t+1)²(t²+1)(t²-t+1)/t⁴`.

The first derivative at `t=1` is zero, whereas the second derivative is `-16`. Thus the additive first-order information cancels, but the complete invariant remains non-flat. This directly tests the tempting square-knot cancellation mechanism.

No new kht++ run was necessary: the already-existing output

`/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/comp/examples/comp/3_1_3_1m/cxKhr-c2-qs`

has the rational component `r(0) q^0 δ|^(1/2)` and four specials:

| level d | offsets c |
|---:|---|
| 0 | 2, 4 |
| 1 | -4, -2 |

Both extrema fall by six. The levels are consecutive. Therefore this specified composite satisfies TILT, and the `k=0` form of the claimed extreme-term argument correctly predicts nonzero defect. Its special Euler polynomial is

`P(q)=-q²+q⁴-q^-4+q^-2=(q-1)(q+1)(q²+1)(q⁴-q²+1)/q⁴`.

The corresponding existing half-diagram input is

```text
s.l1.y0.y0.y1.u2.l1.x0.x0.x1.u2
,1
```

This local file is evidence for the named test, not a new independent recomputation of the curve invariant. The multiplicative obstruction above is a proof and does not depend on trusting that output.

## 4. What mirror symmetry and a tensor-product model say about TILT

An affine simultaneous reversal `(c,d)↦(C-c,D-d)` preserves TILT. For example, the maximum of the reflected level is `C-min(c)` of the original level. Reversing the level order and reversing both extrema therefore preserves strict decrease. Consecutiveness is also preserved. This explains the expected mirror invariance; it supplies no contradiction.

There is a useful elementary stability result for a hypothetical uncancelled tensor-product support. Let finite supports `S,T⊂Z²` have consecutive level sets and both their level minima and maxima strictly decreasing. Then their Minkowski sum

`S+T={(d_1+d_2,c_1+c_2)}`

also has consecutive levels and strictly decreasing minima and maxima.

For minima, choose a minimizing pair at level `d`. Unless `d` is the final level, at least one summand level can be increased, strictly decreasing its minimum; this constructs a smaller value at `d+1`. For maxima, choose a maximizing pair at `d+1`; at least one summand level can be decreased, constructing a strictly larger value at `d`. Consecutiveness follows by adding integer intervals.

Accordingly, even a naive support convolution does not automatically break TILT. This is only a statement about finite supports. The actual tangle invariant is computed from a chain-level tensor/gluing construction, including rational components and differential cancellation. It is not justified to identify its special-component support with this Minkowski sum. The local kht++ documentation for `--sum` describes the tensor product, and explicitly restricts reliable use to `F_2`; it does not provide the needed formula for the resulting special labels.

## 5. A published limitation of assumption (a)

[Kotelskiy–Watson–Zibrowius, arXiv:2104.13592v1, immediately after Conjecture 3.7](https://arxiv.org/html/2104.13592v1) state that longer special components occur for some strongly invertible knots: their `s_(2n)(∞)` with `n≠1`. This was verified directly in the local primary TeX source, `lit/kwz-inversions/src/kwz/main.tex`, line 758. In the current kht++ indexing these are `s_(4n)`, not `s4`. The paper does not name an example in that sentence.

Therefore the letter's observed all-`s4` form cannot be promoted to a universal theorem. This identifies a flaw in the proposed unrestricted deduction, not a counterexample to consecutive levels or monotone extrema.

Their Lemma 2.3 gives a possible repair at the level of graded Euler characteristics: a longer special contributes `n` elementary blocks at a common delta level, with quantum shifts

`4(2i-n-1)`, `i=1,…,n`.

These shifts differ by eight and carry the same parity sign. Thus a longer component with central offset `c` has extreme block offsets `c-4(n-1)` and `c+4(n-1)`. This is an expansion of its paired graded vector space/Euler contribution, not an isomorphism of the longer immersed curve with a disjoint union of shorter curves.

The corrected extrema must therefore range over **all expanded blocks**. Monotonicity of the central component labels alone is insufficient when lengths vary between levels: a longer component can extend beyond a neighboring level despite a smaller center. For example, at the level of formal block data, a length-one component centered at `2` at level `0`, followed by a length-two component centered at `0` at level `1`, has decreasing centers but top block offsets `2,4`. This is a logical illustration, not a claimed realizable quotient tangle.

The same correction is needed in OVERHANG and in the definition of `P`. If other allowed lengths or nontrivial local systems occur, their full graded contributions must also be included. The observation `4|k` and the restriction to the particular even-length family should not be silently treated as general theorems on the strength of the small-knot table.

## 6. Why the polynomial identities do not force TILT

In the letter's shortest-special model, the decategorified data retain

`P(q)=Σ (-1)^(c/2-d) q^c`.

Adding two formal special components at `(c,d)` and `(c,d+1)` contributes zero to `P`. Choose `c` larger than all existing offsets and put the pair on two occupied adjacent levels. Then both level maxima equal `c`, violating strict TILT, while `P`, the bracket vector, every closure Jones polynomial, and `J` are unchanged.

This is not an actual tangle construction. It establishes only that a proof using the `J` multiplication law, bracket identities, and Euler-characteristic equalities alone cannot establish TILT. One needs an additional geometric or chain-level realizability restriction that forbids the relevant cancelling arrangement. The existing observation of cancelling pairs already shows that an argument forbidding *every* such pair would be too strong.

Nor does the sum unit-fiber theorem imply a componentwise TILT law. It provides a weaker noncancellation conclusion for the total invariant of compatible composites. A failure of TILT on a composite, if found, would be compatible with `J≠1` and would not contradict the factor theorem.

## 7. Literature comparison and limits

- [Watson, arXiv:1311.1085v4](https://arxiv.org/abs/1311.1085v4), mirror propositions and the absolutely bigraded refinement, explain reversal of the homological and quantum data. The primary TeX was inspected locally. The actual invariant is the finite-dimensional `κ` group, which detects trivial strongly invertible knots; its nonvanishing is stronger than nonvanishing of its Euler characteristic and does not prove the latter.
- [Kotelskiy–Watson–Zibrowius, arXiv:2104.13592v1](https://arxiv.org/html/2104.13592v1), Lemma 2.3, supplies the long-component block formula. Their table theorem is a finite calculation. The following longer-component existence statement is the relevant correction above.
- [kht++ Options, source at the inspected commit](https://github.com/cbz20/khtpp/blob/a8be0afe9d8e80396449eeb891930b62f47a0cf8/docs/Options.md), documents the sum/tensor implementation. Its coefficient-field warning prevents treating an `--sum` output over another field as an independent test without correcting the implementation.
- The algebra in Sections 1–2 is a direct Temperley–Lieb calculation with Laurent-unit rigidity. No priority claim is made for naming the resulting scalar `J`; the present review does not establish whether an equivalent scalar already appears under another name in the theory of quotient tangles or theta curves.

**Result for the requested attack:** no actual TILT/OVERHANG counterexample was found or asserted. Connected sums and mirrors cannot manufacture a new flat unit by multiplying known non-flat factors. The all-short-components assumption needs correction before the proposed TILT deduction can apply universally, and the grading restriction required after that correction remains unresolved.
