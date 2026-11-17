# Generic Jones attack: tangle unit cancellation

Bounded pass on 2026-10-31. These notes prove a useful algebraic restriction and identify, rather than solve, the generic topological obstruction. No claim of novelty.

## 1. Exact generic reduction and its limitation

Sikora, *Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed rationals*, CJM 76 (2024), Theorem 9.2, proves that Jones unknot detection is equivalent to:

> Every framed two-tangle with Kauffman bracket vector (1,0) is the trivially framed zero tangle.

It is also equivalent to the bracket distinguishing each rational tangle from all tangles. In his proof, a tangle with vector (1,0) yields two closures with monomial brackets. Assuming Jones detection converts those closures to actual unknots; only then can the Gordon–Luecke surgery theorem force the tangle to be rational. Using that topological theorem before establishing actual unknottedness would be circular.

The converse construction takes a Jones-trivial knot K and ties it into one strand of the zero tangle, giving K#0 with vector (1,0). It does not give a prime/no-local-knot tangle. Rotations and boundary twists preserve this local knot. Cutting K in another way supplies a single closure equation, not the full vector. I found no valid generic reduction removing the local knot requirement.

Source: https://doi.org/10.4153/S0008414X23000755 (Section 9).

## 2. Complete unit classification in the two-tangle skein algebra

Let R=Z[A,A^-1], delta=-A^2-A^-2, and

    S = R[e]/(e^2-delta e).

The horizontal zero tangle represents 1 and the infinity tangle represents e. Multiplication corresponds to horizontal concatenation. Thus

    (f+g e)(h+k e)=fh + (fk+gh+delta*gk)e.

The two ring characters are

    chi_0(f+g e)=f,
    chi_1(f+g e)=f+delta*g.

**Lemma.** The element f+g e is a unit if and only if both f and f+delta*g are units in R.

Necessity follows by applying the characters. Sufficiency follows from the explicit inverse

    (f+g e)^-1 = ((f+delta*g)-g e) / (f(f+delta*g)).

The only units in R are signed monomials. Write

    f=eta A^m,  f+delta*g=epsilon A^n,  eta,epsilon in {+1,-1}.

Since delta divides epsilon A^n-eta A^m, reduction modulo A^4+1 gives

    n-m=4k, epsilon=eta(-1)^k

for an integer k. This is exact: modulo A^4+1, A^4=-1 and 1,A,A^2,A^3 are a Z-basis, so no other exponent classes work.

In Sikora's convention, the positive integer crossing is

    b=A^-1+A e,
    b^-1=A+A^-1 e.

Its two characters are A^-1 and -A^3. Therefore every unit of S is uniquely of the form

    eta A^(m+k) b^k.

The characters identify an element uniquely because delta is not a zero divisor. This proves the classification for every positive or negative k.

**Consequence.** If a product of tangle brackets is 1, each factor already has the bracket of an integer tangle up to a signed Laurent monomial. Multiplying known nonunit pieces cannot produce an invisible tangle. This applies to arbitrarily complicated individual pieces, not a named knot family.

The statement concerns skein algebra units. Concluding that each actual tangle is geometrically an integer tangle would assume precisely the missing topology.

## 3. Scalar normalization for actual tangles

If an actual tangle T has unit bracket eta A^r b^k, concatenate the integer tangle -k. The resulting actual tangle Q has vector (eta A^r,0), so its denominator closure has monomial bracket eta A^r.

The standard identities V_L(1)=(-2)^(number_of_components-1) and V_K'(1)=0 show that any link with a monomial bracket has one component and normalized Jones polynomial 1. Hence eta A^r must in fact be the framing unit (-A^3)^w. Thus every actual tangle with a unit skein image has exactly the bracket of a framed integer tangle.

Jones detection would force T to equal that integer tangle (Sikora Theorem 9.2). Conversely, if all actual unit-bracket tangles were integer tangles, applying this to K#0 would prove Jones detection. Consequently, reflection of skein units back to actual geometric units is equivalent to the original conjecture, not a free algebraic fact.

## 4. Explicit failed shortcut: one trivial closure is insufficient

The positive two-crossing integer tangle has vector

    [2]=(A^-2,1-A^4).

Rotate it to obtain T, with vector

    [T]=(1-A^4,A^-2).

Its numerator closure is an actual unknot with framing 2, and algebraically

    [N(T)]=delta(1-A^4)+A^-2=A^6.

But its two horizontal characters are

    1-A^4 and -A^4-A^-4,

neither a unit. Its bracket pair is primitive (the second entry is a unit), but its skein-algebra element is not invertible. Thus even an actual unknot closure does not imply a unit tangle bracket, rational slope alone is insufficient, and coprime bracket entries do not solve the problem.

More generally the equation for one numerator closure is

    delta f+g=u,

where u is the framing monomial. It leaves f free and g=u-delta*f. Polynomial realizability and the geometry of the resulting tangle remain substantial constraints, but there is no algebraic inference to f=1,g=0.

## 5. Further elementary boundaries

Tying a local knot J into a strand multiplies both bracket entries by [J]. Therefore any ratio of the two entries, including Sikora's q-ratio, is unchanged. A ratio-only argument cannot distinguish even a trefoil tied into a trivial strand from the original trivial strand.

The same-width product obstruction extends to TL_n: this is a finite free R-algebra, so if a product is a scalar unit, the determinants of left multiplication by its factors are units, making each factor invertible. It does not apply to a closure, which pairs cups/caps with an operator rather than factoring the identity inside one fixed algebra.

Kauffman's MLinks.pdf pp.15–16 exhibits a nonsplittable tangle with one zero bracket coefficient, but its remaining coefficient is a nonunit proportional to delta. It has a closed component: its two closure brackets, up to framing, are delta and delta^2, forcing respectively 2 and 3 components. Therefore it does not disprove the analogous zero-coefficient conjecture restricted to two-string tangles, and it is not an invisible-tangle counterexample.

Source: https://homepages.math.uic.edu/~kauffman/MLinks.pdf .

## 6. Verification and status

The unit classification and scalar/framing details were independently audited by the braid subagent. The accompanying standard-library script `tangle_unit_check.py` performs 2,754 exact Laurent unit/inverse checks, including negative twists, and verifies the one-closure counterexample. These computations check conventions; the argument above establishes the unbounded statement.

No proof of generic Jones detection and no counterexample was obtained. The concrete output is a general pruning result for proposed cancellation constructions, and a clear separation between scalar closure information and a unit in the full tangle skein algebra.

## 7. The higher-arity unit classification fails

In TL_3, use e_1^2=delta e_1, e_2^2=delta e_2, and e_1e_2e_1=e_1. Define

    N=delta e_1e_2-e_1.

Then

    N^2=delta^2 e_1e_2-delta e_1-delta^2 e_1e_2+delta e_1=0.

Thus 1+N is a unit with inverse 1-N. It is not a Laurent-monomial multiple of a braid image. At A=i, delta=2, every braid generator is unitary for the standard involution e_j*=e_j, while

    (1+N)*(1+N)-1 = 8e_2-2(e_1e_2+e_2e_1) != 0.

The basis elements here are linearly independent even after specializing delta=2. This is a formal skein-algebra example; no single-tangle realization of 1+N is asserted. It shows exactly why the two-strand classification cannot simply be copied to higher arity.

## 8. Explicit failure of induction through rotations and caps

The preceding single-rational-tangle example can be strengthened to a nonrational algebraic tangle. Set

    T = <-1> + <1/2> + <1/3>.

Using R to denote rotation, this is b^-1 + R(b^-2) + R(b^-3). Direct exact multiplication gives

    f_T=A^2-2A^-2+2A^-6-A^-10,
    g_T=A^4+A^-8-A^-12,
    delta*f_T+g_T=1.

Its numerator is actually an unknot: an independently constructed six-crossing diagram simplifies to zero crossings with Regina. Its denominator polynomial is not monomial.

T is not rational. At A=exp(pi i/4), f_T=6i and g_T=1, so its tangle fraction A^-2*g_T/f_T is -1/6. The rational tangle with fraction -1/6 is R(<6>), whose infinity coefficient is the monomial A^-6, up to a framing unit. The displayed three-term g_T rules out equality even with a framing change. This uses the proved classification of rational tangles, not Jones detection.

Now let Q=R(T). Then Q is nonrational and its skein element is not a unit (its zero coefficient has three terms). Nevertheless

    [e Q] = (f_Q+delta*g_Q)e = e.

So a cap can absorb a nonrational tangle into the trivial infinity bracket. There is no paradox: Q has an actual unknot denominator closure, and the cap performs that closure. A recursion through rotations reaches the nonunit element e, where cancellation into a scalar closure is possible. This explicitly defeats the proposed induction from the unit classification to all algebraic tangles.

The standard-library check includes this exact identity. The independent diagram check used Spherogram RationalTangle(-1)+RationalTangle(1,2)+RationalTangle(1,3), numerator closure, and Regina's Reidemeister simplifier, which returned zero crossings.
