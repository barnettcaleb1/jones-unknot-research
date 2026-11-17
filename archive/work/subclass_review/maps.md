# Subclasses already covered by the a_2 obstruction, and the map-level alternative

Theory-only response to Claude 20261103-094424(3). No computation or census was run. This note takes the project's banked U4 implication as input:

> A flat Watson quotient bracket with an actual unknot meridian forces a_2(kappa)=Delta''_kappa(1)/2=0.

The conclusions below are consequences of that implication and published structure theorems, not new claims of priority.

## 1. Torus knots and genus-one alternating knots need no new extreme-state argument

For a nontrivial torus knot T(p,q),

    a_2(T(p,q)) = ((p²-1)(q²-1))/24 > 0.

For example this follows by putting t=exp(x) into the symmetrically normalized torus Alexander polynomial and expanding the ratio of hyperbolic sines to order x². Therefore every strong inversion of every nontrivial torus knot is already excluded from the flat locus by U4. Beginning with T(2,m) may calibrate a proposed extreme-term mechanism, but it does not establish a previously unavailable detection subclass for this project.

There is another immediate finished subclass:

> No nontrivial genus-one alternating knot, with any strong inversion, has a flat quotient bracket.

Proof. Its Conway polynomial has the form 1+a_2 z². The Crowell–Murasugi theorem says the breadth of the Alexander polynomial is twice the genus, so a_2 cannot be zero. This contradicts U4. The same argument works for any genus-one knot with nontrivial Alexander polynomial; it does not apply to Alexander-trivial genus-one knots such as untwisted Whitehead doubles.

A primary modern proof of the needed genus theorem is [Kindred, *A simple proof of the Crowell–Murasugi theorem*, Theorem 1](https://arxiv.org/pdf/2209.09850). It applies in particular to all genus-one two-bridge knots, including the double-twist families. Their standard two-band calculation gives Conway polynomial 1 plus a nonzero product of the two twist parameters times z², with the sign determined by conventions.

Thus the new content of an all-two-bridge theorem begins at **genus at least two with a_2=0**, not at the torus or double-twist seed. The project's b(31,13), Conway 1-2z⁴, is already an explicit member of that residual class. No assertion is made that this residual class has flat bracket.

## 2. An L-space subclass and a precise thin-closure endpoint

More generally, every nontrivial knot admitting an integer L-space surgery has a_2>0. Here is the short argument.

[Ozsváth–Szabó, *On knot Floer homology and lens space surgeries*, Theorem 1.2 and Corollary 1.3](https://arxiv.org/pdf/math/0303017) give

    Delta(t)=(-1)^k + sum_(j=1)^k (-1)^(k-j)(t^(n_j)+t^(-n_j)),
    0<n_1<...<n_k.

For a nontrivial knot here k>=1: if k=0 the stated knot Floer description is supported only in Alexander degree zero, and [knot Floer genus detection](https://arxiv.org/abs/math/0311496) forces genus zero. Differentiating gives

    a_2 = sum_(j=1)^k (-1)^(k-j) n_j² > 0.

If k is even, pair successive terms as n_(2r)²-n_(2r-1)²; if k is odd, retain n_1² and pair the remaining terms. Every displayed summand is positive. Mirroring preserves Delta and a_2, so either surgery sign is covered.

Consequently U4 already excludes every nontrivial strongly invertible knot with such a surgery. A useful conditional endpoint, stated with an integral slope to avoid unnecessary rational-surgery input, is:

> If a flat Watson tangle has a reduced-Khovanov-thin closure at some nonzero integer surgery slope, then its cover knot is U.

Indeed thinness gives rank Kh~=det=|n|; the Khovanov-to-Floer spectral sequence forces the filling to be an L-space; the preceding positivity contradicts a_2=0 unless the knot is U. This is a complete conditional result. It does not prove that a flat tangle has such a closure. It names the same missing rank/filling step already tracked by U5, rather than supplying a new mechanism for that step.

## 3. Why alternating/two-bridge/tunnel-one kappa does not automatically simplify Watson's maps

There is a strong warning against assuming the closure family is thin merely because kappa is alternating or two-bridge. The same [Ozsváth–Szabó paper, Theorem 1.5](https://arxiv.org/pdf/math/0303017) says an alternating knot with an integral L-space surgery must be a T(2,2n+1) torus knot.

Therefore a hyperbolic two-bridge kappa has **no** nonzero-integer-surgery branch closure of minimal reduced Khovanov rank, for any strong inversion: such a closure would force an L-space surgery. In particular these closures cannot be delta-thin. The simplicity of the knot's alternating diagram does not transfer to the Khovanov homology of the surgery branch sets.

Tunnel number one alone supplies a Heegaard/quotient description, not the missing differential or saddle-map information. I found no primary theorem in this bounded check making the full Watson inverse system uniformly computable or thin for all tunnel-one knots. This is not a proof that no such description exists; it is a reason not to assume one.

Recommendation: if the goal is a fresh subclass proof, first state the residual class a_2=0, genus>=2 explicitly. An extreme-term theorem for that class would have new mathematical content beyond U4. A torus/double-twist calculation is a calibration, and the one-thin-closure criterion is a precise conditional endpoint, but neither should be presented as a newly discovered route through the general gap.
