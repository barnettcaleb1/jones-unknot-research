# Crossing dynamics: exact one-disk rigidity, no intermediate-value principle

Date: 2026-11-03. Bounded theory pass. No scans.

## 1. The disk is part of the dynamical state

A standard crossing disk meets the knot twice with algebraic intersection zero. This convention is explicit in [Moore, Symmetric unions without cosmetic crossing changes](https://arxiv.org/pdf/1507.07996), Section 1. Twisting along that disk is different from inserting full twists into an arbitrary coherent braid box. A coherent braid-axis disk has algebraic intersection +/-2. The two markings can realize the same single crossing change while producing different longer twist families.

In particular, the standard theorem that all twists at a nugatory crossing preserve knot type is not contradicted by the coherent family T(2,2n+1), whose members at n=-1 and n=0 are unknots and whose member at n=1 is a trefoil. The latter twists about a different disk. Any proposed dynamical rule must specify its disk, rather than just the crossing's diagrammatic location.

## 2. Exact recurrence, including writhe

Use sigma=A*1+A^-1*e, e^2=delta*e, delta=-A^2-A^-2, and t=A^-4. The two eigenvalues of sigma are A and -A^-3, so those of a positive geometric full twist sigma^2 are A^2 and A^-6.

Let F_n(t) be the normalized Jones polynomial of a fixed outside tangle closed after n additional full twists. Full twists preserve the endpoint permutation, so if one closure is a knot, all are knots.

- For coherent strand orientations the writhe increases by 2. The normalized full-twist eigenvalues are t and t^3. Thus

      F_(n+2)=(t+t^3)F_(n+1)-t^4 F_n.

- For oppositely oriented strands the writhe decreases by 2 with this geometric-crossing convention. The normalized eigenvalues are 1 and t^-2. Thus

      (S-1)(S-t^-2)F=0,
      F_n=C+D t^(-2n).

Reversing the twist convention replaces t by t^-1 in the relevant formulas. These are exact Laurent identities, derived from TL_2, not numerical recurrences.

**One-disk rigidity lemma.** For a standard algebraic-intersection-zero crossing disk, if F_r=F_s for two distinct integers r,s, then F_n is constant for every integer n.

Proof: D(t^(-2r)-t^(-2s))=0 in Q(t), so D=0. Equivalently the consecutive defects satisfy F_(n+1)-F_n=t^-2(F_n-F_(n-1)). Therefore either every step is Jones-flat or none is. In particular equal adjacent values do give an infinite constant Jones family in this convention.

This is a useful positive lemma: if an actual unknot and another member of the same standard two-point twist family have Jones polynomial one, all intermediate and extrapolated members also have polynomial one. It applies equally to twists of order greater than one. Turning that conclusion into actual unknottedness is still the missing Jones/cosmetic-crossing input.

For a coherent braid box, equal adjacent values have a different consequence. If F_0=F_1=P, then

    F_n=P * V_{T(2,2n-1)}(t),
    F_2=P(t+t^3-t^4).

The torus family satisfies the same recurrence and initial values, proving the identity. A nonzero such sequence has at most one flat adjacent step: two such steps would give two independent linear equations killing both eigenmode coefficients. Thus an arbitrary-box version of the infinite-flat-family assertion is false, while its standard crossing-disk version is correct.

## 3. Telescoping defects are an exact cocycle, not a positivity theorem

For a crossing-change path K_0,...,K_m put

    d_i=V_{K_i}-V_{K_(i-1)}.

Then sum_i d_i=V_{K_m}-V_{K_0}. This is the coboundary of the Jones function on the marked Gordian graph. Equal endpoint values merely say that the path's vector increments sum to zero.

One can remove the universal knot factor. Since every knot has V(1)=1, V'(1)=0, and V(omega)=1 for a primitive cube root omega,

    H_K(t)=(V_K(t)-1)/((t-1)^2(t^2+t+1))

is an integral Laurent polynomial. The normalized edge defects are H_{K_i}-H_{K_(i-1)}. This is still an exact cocycle; dividing by the universal factor creates no order or sign constraint.

There is an actual classical counterexample to the proposed intermediate-value principle, even if every crossing change is negative-to-positive. Write a=sigma_1 and b=sigma_2 in B_3 and take braid closures:

    beta_0=a^-1 b^-1 a b^-1,
    beta_1=a b^-1 a b^-1,
    beta_2=a b a b^-1.

The first change flips the first crossing; the second flips the second crossing. Both are negative-to-positive, and they are different marked crossings. The middle closure is the standard figure-eight knot. Cyclically rotating beta_0 gives b^-1 a^-1 b^-1 a=a^-1 b^-1, so its closure is U. The braid relation gives beta_2=b a, also closing to U. Hence

    U -> 4_1 -> U

has equal endpoint Jones polynomials and neither edge is Jones-flat. Since

    V_(4_1)=t^2-t+1-t^-1+t^-2,
    H_(4_1)=t^-2,

the normalized defects are exactly +t^-2 and -t^-2. This rules out any positive cone for all negative-to-positive crossing changes, even after the standard universal factor is removed. It also shows that evaluating at a fixed positive real t does not create monotonicity.

This path is not a shortest unknotting path—the endpoints are both U. Therefore it does not refute a new theorem restricted to a specially selected shortest path from a hypothetical Jones-trivial nontrivial knot. It refutes the claim that telescoping, crossing signs, or endpoint equality by themselves supply that theorem.

## 4. Why several twist sites restore the cancellation problem

For two independent algebraic-intersection-zero twist sites, the exact spectral form is

    F(m,n)=c_00+c_10 lambda^m+c_01 mu^n+c_11 lambda^m mu^n,

with lambda and mu appropriate t^+/-2 powers and coefficients in Q(t). One endpoint equality is one equation among the four channels. No one-variable rigidity survives automatically along a path changing both coordinates.

A formal countermodel, not asserted to be a knot family, is

    F(m,n)=1+(t-1)^2(t^2+t+1)(t^(2m)-t^(2n)).

It obeys the one-site recurrences and the listed universal evaluations; its diagonal is identically one, but every coordinate step is non-flat. Thus even those recurrences plus the standard knot evaluations cannot yield a multidimensional intermediate-value theorem. A proof must constrain the realizable joint coefficient array geometrically.

## 5. Candidate mechanism, obstacle, and first meaningful lemma

The plausible mechanism would be a geometrically selected unknotting process whose edge defects belong to one pointed positive cone in a fixed Laurent-polynomial vector space. Endpoint equality would then force every defect to vanish, and an independently justified geometric treatment of flat standard crossing disks could finish.

The first lemma must specify the selection rule and prove cone membership from topology; “choose a good representative” is not a rule. Crossing sign alone fails by the explicit figure-eight path. Choosing independent framing units separately on the edges also invalidates the original telescoping identity, unless a genuine transport law proves the reweighted sum still computes the endpoint difference.

A still stronger energy descent proposal is already impossible: every nontrivial knot cannot admit a crossing change strictly lowering E=sum(coefficients squared), since E(T(3,q))=3 while u(T(3,q))=q-1 is unbounded. Repeating such strictly decreasing steps would give u<=1 on that family. A viable process must allow long plateaus or larger geometric moves, and those require their own termination and zero-defect arguments.

I have no topology-derived selection rule or positive cone. The result of this pass is the exact one-disk rigidity lemma and the precise location where a global dynamics argument loses it: changing disks introduces independent smoothing/relative-tangle data and permits defect cancellation.
