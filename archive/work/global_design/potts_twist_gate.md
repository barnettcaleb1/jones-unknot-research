# Three-terminal Potts identities with actual integer twist edges

2026-11-03. Bounded design check; no enumeration or new diagram computation.

**Outcome:** no candidate survives the elementary star–triangle move with series/parallel integer twist boxes as its three edges. The exact equation forces two of the effective edges to be opposite single crossings. The remaining operation is the twist-box version of the usual graph Reidemeister III move, implemented by a flype / successive Reidemeister moves. A sequence of such moves starting from an actual unknot remains an actual unknot.

Scope: this excludes the specified elementary network construction. It does not classify arbitrary three-terminal tangle replacements or arbitrary integer rational-tangle networks.

## Prior result, not redone

`outputs/jones-graph-cancellation-audit.txt`, §2, and handoff LATE-18 already give the full boundary-channel condition. A star with arm weights a,b,c has coefficients

    (λ, ab, bc, ac, abc),    λ=Q+a+b+c.

Matching a triangle in all five boundary partitions requires

    abc=Q(Q+a+b+c).                         (1)

When this holds and λ≠0, its triangle edges are Q/a, Q/b, Q/c, assigned opposite the corresponding arms, with common multiplier λ. Matching only the first four partitions does not suffice.

At the Jones specialization let y=−A⁴. Then

    Q=2−y−y⁻¹,
    a_n=yⁿ−1.

The two elementary crossing weights are a_1 and a_−1, with

    a_1 a_−1=Q,     a_1+a_−1=−Q.

A parallel bundle of signed net multiplicity n has effective weight a_n. A series bundle has effective weight Q/a_n, after retaining its scalar prefactor. Opposite crossings inside a bundle cancel first. We exclude n=0 and singular effective reductions in the following statement; the zero cases are smoothing/disconnection or Reidemeister-II degenerations, not a new nondegenerate star–triangle identity.

## Extension to integer twist bundles

**Lemma.** If each of a,b,c is either a_n or Q/a_n for a nonzero integer n, then (1) holds if and only if the three effective weights contain the pair a_1,a_−1. The third effective weight may be any allowed bundle weight.

Sufficiency is immediate: the sum of the opposite pair is −Q and their product Q.

Here is a hand proof of necessity, separated by the number of series arms.

**No series arms.** All three exponents of the same sign are excluded by comparing highest powers of y (or applying y↦y⁻¹ first): the product has higher degree than the right side of (1). Otherwise write the exponents p,q,−r with 1≤p≤q and r>0, using inversion and permutation. If p>1, the product's highest exponent p+q exceeds the right side's maximum q+1, a contradiction. Thus p=1. The obstruction factors exactly as

    abc−Q(Q+a+b+c)
      = (y−1)(b+(y−1)/y)(c+(y−1)/y),    a=a_1.

Consequently another arm is a_−1.

**One series arm.** Write a=Q/a_p, b=a_q, c=a_r. Clearing denominators turns (1) into

    (y^q−y^p)(y^r−y^p)
       = (y^p−y)(y^p−y⁻¹).                (2)

For p=±1, a is already a single crossing, and the factorization above (or its y-inverse) forces its opposite. For |p|>1, uniqueness of the cyclotomic factor multiplicities in the two binomial products in (2), followed by matching their lowest powers and signs, gives {q,r}={1,−1}. More explicitly, the absolute differences {|q−p|,|r−p|} equal {|p−1|,|p+1|}; for p>1 the signs must both be negative to offset the y^(2p) factor, and p<−1 follows by inversion.

**Two series arms.** Write a=Q/a_p, b=Q/a_q, c=a_r. Equation (1) is

    a_r (Q−a_p a_q)=Q(y^(p+q)−1).         (3)

If p,q>0, highest degrees force r=1. The preceding single-crossing factorization then forces p=1 or q=1, giving the opposite effective crossing Q/a_1=a_−1. The all-negative case follows by inversion. If p>1 and q<−1, the left factor Q−a_p a_q has highest exponent p and lowest exponent q. For p+q>0 the right side has highest exponent p+q+1<p; for p+q<0 it has lowest exponent p+q−1>q. Neither is possible after multiplication by a_r, which can only increase the highest exponent or decrease the lowest. If p+q=0 the right side is zero while both factors on the left are nonzero. Thus in the mixed case one series arm must itself be a single crossing, and again its opposite is forced.

**Three series arms.** Clearing denominators gives

    y^(p+q+r)+y+y⁻¹=y^p+y^q+y^r.

Both sides have positive coefficients, so their exponent multisets agree. In particular {p,q,r} contains 1 and −1. Their effective series weights are the opposite elementary pair.

## What the classification means geometrically

With a,b the opposite crossing pair and c the remaining box, λ=c. The triangle replacement swaps the two crossing weights and replaces c by its series/parallel dual Q/c. For the actual integral twist box this is its quarter-turned presentation in the usual twist-box flype. In braid coordinates the underlying identity is explicitly

    σ₁ σ₂^n σ₁⁻¹ = σ₂⁻¹ σ₁^n σ₂.

Indeed the case n=1 is the braid relation rearranged, and all integer n follow by taking powers of that conjugation identity. Rotating the local patch gives its series-box version. Thus this is an equality of actual tangles, before applying their bracket. Equivalently, expand the box into its individual crossings and slide the adjacent crossing detour through it by Reidemeister III, cancelling the inverse crossings by Reidemeister II as needed. The internal scalar prefactors of compressed series edges must be restored; they are not extra physical crossing weights.

The underlying signed-graph star–triangle correspondence with Reidemeister III is explicitly recorded by [Kauffman, *A Tutte polynomial for signed graphs*, pp.125–126](https://homepages.math.uic.edu/~kauffman/TuttePolySignGraphs.pdf). The extension above is our algebraic check of which integer bundle substitutions can satisfy the full five-channel identity; no novelty claim is made.

This leaves a sharp gate for any genuinely new network candidate: at least one arm must be a more general marked tangle whose effective weight is outside the integer series/parallel families, or the proposed replacement must involve more than this elementary star–triangle relation. Assigning an arbitrary rational weight Q/a formally does not construct that tangle. I have no explicit physical non-isotopic realization with an actual unknot anchor, so I do not recommend a candidate or a word search from this pass.
