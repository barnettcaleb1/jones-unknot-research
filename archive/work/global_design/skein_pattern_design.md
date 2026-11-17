# Scalar-core patterns: the target already contains Jones detection

Date: 2026-11-03. Bounded theory pass; no scans or new matrix computations.

## Main conclusion

A noncore knot pattern `P` with annular bracket `[P] = u e_1`, where `u` is a Laurent monomial unit, would already imply a counterexample to Jones unknot detection. Requiring `P(U)=U` does not make this a harmless universal Jones-preserving gadget: a meridional twist of that same unknot pattern must then be a nontrivial knot with Jones polynomial one.

Thus constructing this pattern is a counterexample route in its own right, not a weaker auxiliary construction for transferring an unknown counterexample to an easier class. The Ren example supplies no such pattern, and its even-to-odd conversion leaves an uncontrolled surviving fusion channel.

## 1. Exact reduction to annular core detection

Let `R=Z[A,A^-1]`, `delta=-A^2-A^-2`, and identify the solid-torus bracket skein module with `R[z]`, where `e_1=z` is the framed core. Say that a pattern is a core if it is isotopic to the core as an unframed knot in the solid torus; framing units are allowed in the algebraic statement.

**Proposition.** The following assertions are equivalent:

1. The Jones polynomial detects the unknot among knots in `S^3`.
2. If an annular knot has bracket `u z`, with `u` a unit of `R`, it is a core.

**Proof of 1 => 2.** First, `[P]=u z` forces absolute winding number one. At `A=-1`, the skein class of a knot representing the `w`th power of the solid-torus generator is minus its `SL_2` trace. Writing the core variable as minus the trace, this polynomial has degree `|w|`: it starts `-2, z, 2-z^2, z^3-3z` for `w=0,1,2,3`. Hence equality with `u(-1)z` forces `|w|=1`. This is also obtained directly from crossing-change invariance at `A=-1` and the trace/Chebyshev recurrence.

Let `P_n` be obtained by `n` meridional twists of the ambient solid torus, and fill the axis in the standard way to obtain knots `K_n` in `S^3`. The induced skein map sends a framed core to a framed core, so `[P_n]` is again a unit times `z`. After filling, the normalized Jones polynomial of `K_n` is a monomial. For every knot, `V(1)=1` and `V'(1)=0`; a monomial with these two properties is exactly `1`. By assertion 1, every `K_n` is an actual unknot.

Now apply Baker--Motegi's twist-family theorem: if `g(K_n)-g_4(K_n)` is bounded for infinitely many integers `n`, then winding is zero or winding equals wrapping. Winding here is one, so wrapping is one. A wrapping-one annular knot is a core with a local knot tied into it: cutting at a once-intersecting meridian produces a one-string tangle in a ball. Its ordinary closure is that local knot. Since `K_0=U`, the local knot is trivial, so `P` is the core.

**Proof of 2 => 1.** If `J` is a knot with `V_J=1`, tie `J` locally into an annular core. The resulting pattern has bracket a unit times `z`. Assertion 2 makes it a core; filling the axis gives `J=U`.

This is a derived equivalence, not a claim of novelty. The topology input is [Baker--Motegi, Seifert vs. slice genera of knots in twist families](https://arxiv.org/pdf/1705.10373), Theorem 1.2 in arXiv v1, page 2. The same page explicitly records that a twist family with wrapping greater than one contains at most two unknots, citing earlier work. The proof above needs only their stated Theorem 1.2. The `A=-1` interpretation is the standard skein/character dictionary; see [Przytycki--Sikora, Skein algebra of a group](https://impan.pl/en/publishing-house/banach-center-publications/all/42/0/110286/skein-algebra-of-a-group).

**Anchored corollary.** If `P(U)=U`, `P` is noncore, and `[P]=u z`, then some `K_n` is a nontrivial Jones-trivial knot. In fact only finitely many `K_n` can be unknots, by the same twist-family theorem. The anchored hypothesis makes this a direct source of a counterexample family if such a pattern is constructed; it does not downgrade the difficulty.

**Slightly weaker algebraic input suffices.** If `P(U)=U` and `deg_z[P]=1`, parity implies `[P]=p(A)z`. Filling gives `p(A)delta=u delta`, so `p=u` in the domain `R`. Thus a noncore unknot pattern of annular degree one is already enough for the counterexample conclusion.

## 2. What Ren's construction actually supplies

[Ren, A counterexample to the wrapping number conjecture](https://arxiv.org/html/2609.11084v2) gives an annular knot of wrapping four and annular degree at most two. Its mechanism kills the four-through term using the six-strand Burau summand `W(6,4)`. It does not kill all lower channels.

Our existing archived theorem strengthens the limitation for that particular core: every attached four-strand braid has degree exactly two. In the Chebyshev basis its class is therefore

    [R_beta] = c_0 e_0 + c_2 e_2,       c_2 != 0.

References to existing certificates, not recomputed here:

- `work/ren-braid-obstruction-note/main.tex`: all attached `B_4` braids.
- `work/research47/ren_composition.txt`: powers of one fixed block still have degree two; satellite composition of standard Ren-family patterns has degree eight.

The core target is odd, whereas Ren's example is even in the solid torus's `Z/2` homology grading. Adding a disjoint core changes parity but gives, exactly,

    (c_0 e_0+c_2 e_2)e_1 = (c_0+c_2)e_1 + c_2 e_3.

The nonzero `e_3` term survives. Connecting the two components by a band is not an operation determined by their closed annular skein class. A specified band can define a linear map on an appropriate **relative** skein module, but one must keep the marked attachment intervals before closure. Applying a band to a closed polynomial as if it were multiplication or a projection silently discards precisely the information one needs.

Likewise, satellite substitution is linear, not multiplicative: `z^j` is sent to an actual `j`-parallel cable. The recorded two-cable degree-eight term explains why composing Ren patterns restores high annular degree.

## 3. The narrow constructive problem that remains

The honest next construction target would be an odd-through **relative** tangle with two geometrically different interacting capped blocks, a specified closure producing a single winding-one component, and an actual unknot anchor. In a generic TL character decomposition one needs all odd annular trace channels `e_j`, `j>=3`, to vanish and the `e_1` coefficient to be a unit. Known Burau-kernel cancellation controls one highest cell quotient; it gives no relation forcing the remaining lower odd traces to vanish.

This target is smaller than the kernel of the full TL representation: a single annular closure requires character/trace cancellation, not an identity operator. That distinction is a genuine allowance for a construction. But neither Ren's single-block theorem nor its known powers provides the required cancellation. A full braid closure is itself unsuitable because its highest through sector contributes a nonzero scalar; genuine caps are necessary. A Jones--Wenzl projector may formally isolate `e_1`, but it is a rational linear combination of diagrams, not an actual knot pattern.

The first potentially productive change would therefore be a **new geometric banded two-block identity in a relative skein module**, accompanied by a disk or surgery description proving its unknot anchor. This is a precise counterexample design problem. I have no candidate identity and would not propose a word search as a substitute.

Finally, if a pattern has a hyperbolic two-component axis exterior, this does not make `P(K)` hyperbolic for nontrivial companions: a genuine satellite retains its companion torus. A hyperbolic-pattern construction cannot by itself reduce arbitrary knots to hyperbolic knots.

## Recommendation

Do not treat scalar-core unknot patterns as an inexpensive escape from the colored-Jones barrier. Their existence would already refute the original conjecture. Bank the annular core-detection equivalence as a clear scope statement, keep the existing Ren obstruction, and only reopen this construction route if someone has a concrete relative skein identity with an actual unknot anchor.
