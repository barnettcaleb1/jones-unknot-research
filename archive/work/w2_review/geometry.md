# Geometry review of Claude 20261103-090406

## Verdict

The claimed implication from a joint `(1,2)`-bridge presentation and linking number zero to wrapping number at most two is **false**. This is stronger than the observation that the supplied proof has a gap: the two-bridge link `L(24,5)` is a counterexample to that geometric implication. It does not satisfy any asserted Jones-triviality or unknot-band hypothesis; no conclusion about Lemma Q itself follows.

## A concrete counterexample, without a search

Take the two-component two-bridge link

\[
L=L(24,5)=L(rq-1,q),\qquad r=q=5.
\]

Each component is an unknot. The linking number of the family is `(r-q)/2`, hence zero here. Chen–Zemke–Zhou give these facts and an explicit Alexander-polynomial support walk in §8.3, pp. 71–73 of [Applications of the L-space satellite formula](https://arxiv.org/pdf/2509.20288). Substituting `r=q=5` into their published walk gives support

\[
\begin{split}
&(0,0),(1,1),(2,1),(1,0),(0,-1),(1,-1),\
&(2,0),(3,0),(2,-1),(1,-2),(2,-2),(3,-1),
\end{split}
\]

with coefficient `(-1)^(i+j)` at `(i,j)`. In particular its span is **three in each variable**. This is a hand specialization of the stated formula, not a numerical knot search.

Let `E` be any spanning disk for either component, transverse to the other component in `w` points. In the link exterior, the punctured disk `F` represents the coordinate cohomology class which evaluates as one on the first component's meridian and zero on the other meridian. Its complexity is `max(w-1,0)`. The Alexander norm of that coordinate class is the corresponding variable span, namely three. [McMullen, Theorem 1.1](https://people.math.harvard.edu/~ctm/papers/home/text/papers/alex/alex.pdf), gives

\[
3=\|\phi\|_A\leq\|\phi\|_T\leq\max(w-1,0).
\]

Thus every such disk has `w >= 4`: the wrapping number is at least four in either direction.

A two-component two-bridge link has one bridge per component. A local bridge perturbation of the second component changes this to a joint `(1,2)`-bridge presentation, preserving the link and its wrapping number. This supplies exactly the bridge-count premise used in the proposed argument, while contradicting its conclusion.

The obstruction is unbounded: the same published support formula for `r=q=2k+1` has coordinate span `2k-1`, hence wrapping at least `2k`, while every member still admits a joint `(1,2)`-bridge presentation after one perturbation. It is enough to use `L(24,5)` if a single counterexample is preferred.

## Where the proposed disk construction fails

Simultaneous triviality gives pairwise disjoint bridge disks **within each half-ball**. It does not give upper and lower bridge-disk shadows for the axis that are mutually disjoint in the sphere punctured by the other component.

Consequently `s_+ union s_-` need not be a simple closed curve. Its intersections can be essential relative to the four other punctures, so the region `R` and disk `E=Delta_+ union R union Delta_-` used in the letter are not available. An isotopy that removes intersections in the unpunctured sphere may pass through the other component. The counterexample shows that no general simultaneous-disjointness repair is possible under just the stated bridge and linking assumptions.

## What can be salvaged conditionally

**Conditional disk lemma.** Suppose the upper and lower axis bridge shadows can be chosen mutually disjoint, as well as disjoint from their respective systems. Then, with linking number zero, the other component has wrapping zero or two.

Indeed the two shadows form a Jordan curve. Of the two complementary disks, choose one containing at most two of the other component's four sphere punctures. Combining it with the bridge disks gives an axis spanning disk with at most two intersections. Algebraic intersection zero excludes exactly one intersection. Zero intersections imply splitness; if the link is nonsplit, wrapping is therefore exactly two.

The further assertion about the two punctures has a correct combinatorial version. Orient the two-bridge component and label its sphere punctures by their crossing signs. There are two plus and two minus signs. Its four bridges form a four-cycle, alternating upper and lower edges, and each edge connects opposite signs. Those four edges exhaust all four possible plus/minus pairs. Thus any pair of oppositely signed punctures is joined by a bridge in **one** hemisphere. One may need to swap the upper and lower hemispheres.

The letter's parenthetical argument—endpoints of different bridges on the same side necessarily have the same sign—is false as phrased; the four-cycle argument supplies the conclusion actually needed.

Finally, a selected bridge shadow leaving `R` is not by itself an invariant certificate of nonsplitness. A shadow inside `R` can provide the claimed simplification; conversely one needs an existence statement over suitable bridge disks or representatives, rather than an obstruction read from an arbitrary shadow.

## Scope for the research route

The wrapping-two algebra may still be useful on a separately specified wrapping-two subclass. It cannot presently stand for all width-six tangles using bridge count alone. A repair would need a new theorem deriving the simultaneous-disjointness/disk condition from additional hypotheses such as the actual unknot band closure or the Jones equality. The example above neither assumes nor disproves such a theorem.

## Addendum: the wrapping-two outside cover and an odd-square obstruction

This concerns the genuine wrapping-two subclass, independently of the failed bridge-count reduction above.

**Status: TRUSTED, pending Claude's independent check. No novelty or priority claim.**

### Direct identification of the outside cover

Let `E` be the encircling disk, pierced by the two strands, and take its regular neighborhood as the outside ball. Its branch set is `boundary(E)` together with the two transverse strand segments. The double cover `Q` of this ball is the orientable twisted interval bundle over the Klein bottle. Here is a construction rather than an inference from two fillings.

First take the twofold cover of `E` branched at its two interior punctures. This is an annulus. Since the boundary circle of `E` is itself in the three-dimensional branch locus, the two boundary circles of that annulus are identified under the deck involution in the full preimage of `E`. The deck involution preserves the induced boundary orientations, so this boundary identification produces a nonorientable closed surface of Euler characteristic zero: a Klein bottle. Local branched-cover coordinates show that its regular neighborhood is the full outside cover `Q`. Since `Q` is oriented, this is the orientable twisted interval bundle.

This is also the standard cover of the `(-2,2)` pretzel tangle: see [Ishiwata–Przytycki–Yasuhara, Example 2(a), Figure 6](https://arxiv.org/pdf/math/0109046). The argument above identifies the encircling outside piece directly, rather than relying on an unspecified isotopy to their diagram.

Write

\[
\pi_1(Q)=\langle a,b\mid aba^{-1}=b^{-1}\rangle,
\qquad \pi_1(\partial Q)=\langle a^2,b\rangle.
\]

The annulus-core direction is `b`. The ordinary `D`-closure slope is the lift of an arc joining the two punctures on a face of `E`, hence is `b`. The ordinary annular `K`-closure slope is at distance one from it, hence has the form `a^2 b^k`, up to orientation. The homology calculation below is independent of `k`.

One can fix the shear using the standard identity filling: its branch link is the three-component chain obtained as the connected sum of two Hopf links. Thus the filled cover is `RP^3 # RP^3`, with infinite fundamental group. Filling `Q` at `a^2 b^k` gives the group obtained by imposing `a^2=b^{-k}`; for `k != 0` this group is finite, because `b^(2k)=1` and every word reduces to `b^j` or `ab^j`. Consequently `k=0`. This uses the filling only to fix the marking after the direct identification of `Q`.

### Homology lemma

Let `M` be an oriented rational homology solid torus, with primitive rational longitude `lambda` and complementary slope `mu`. Write

\[
H_1(M)=\mathbb Z c\oplus T,\quad |T|=t,\quad
i(\lambda)=\ell\in T,\quad \operatorname{ord}(\ell)=g.
\]

Integral boundary duality gives that the image of `H_1(boundary M)` in the free quotient has index `g`. Here is the integral check. Poincare–Lefschetz duality and the universal coefficient theorem give `H_1(M,boundary M) = H^2(M)`, of order `t`. The exact sequence of the pair makes this the cokernel of the boundary map. If the free-boundary index is `d_0`, that cokernel has order `d_0 t/g`: the torsion image of the boundary is precisely the cyclic subgroup generated by `ell`. Comparing orders gives `d_0=g`.

Thus, after orientations are chosen, `i(mu)=gc+v`, with `v in T`. Glue `M` to the outside cover with `lambda` identified to `b` and `mu` to `a^2 b^k`. Since `H_1(Q)=Z a + Z/2 b`, Mayer–Vietoris gives

\[
H_1(M\cup Q)=
\frac{\mathbb Zc\oplus\mathbb Za\oplus T}
{\langle gc+v-2a-k\ell,\;2\ell\rangle}.
\]

Set `d=gcd(g,2)`. Quotienting `T` by the subgroup generated by `2ell` leaves a finite group of order `td/g`. The remaining relation has free coordinates `(g,-2)`, whose common divisor is `d`. Therefore

\[
\boxed{\;|\operatorname{Tor}H_1(M\cup Q)|
=\frac{t}{g}\gcd(g,2)^2.\;}
\]

The torsion component `v-k ell` of the relation does not change this order: after a primitive change of free coordinates, the finite part has a presentation obtained by adjoining one generator with relation `d z + v'`, and therefore order `d|T/<2ell>|`.

### Stronger clean statement: no Jones hypothesis is needed

**Proposition.** Let `N=U union K_2`, where `U` is an unknot with a spanning disk meeting the knot `K_2` exactly twice. If `H_1(Sigma_2(N))=Z`, then for the cut-tangle cover `M` there is an odd positive integer `g` such that

\[
H_1(M)=\mathbb Z\oplus\mathbb Z/g,
\qquad \det(K_2)=g^2.
\]

**Proof of the hypothesis reduction.** The ordinary annular closure is the knot `K_2`, so `M(mu)` is a rational homology sphere and `b_1(M)=1`. Before knowing the rational longitude, write the free components of `i(mu),i(lambda)` as `p c,n c`. The free gluing relations have matrix with rows `(p,-2)` and `(2n,0)` after eliminating the order-two generator of `Q`. If `n != 0`, the glued manifold has first Betti number zero, contrary to `H_1(Sigma_2(N))=Z`. Thus `n=0`, making the primitive ordinary `D` slope `lambda` the rational longitude. The boxed torsion formula now applies.

The boxed formula then forces `t/g=1` and `gcd(g,2)=1`. Consequently `t=g` is odd, and

\[
\boxed{\det(K_2)=|H_1(M(\mu))|=tg=g^2,
\qquad g\text{ odd}.}
\]

Moreover, `ell` has order `g=t=|T|`, so it generates all of `T`; therefore `T` is cyclic as claimed.

**Band corollary.** If `N` is one band move from the unknot and has determinant zero, the Montesinos trick identifies its branched cover with zero-surgery on a knot in `S^3`. Hence its first homology is `Z`, supplying the proposition's hypothesis. This applies to a wrapping-two band-Jones candidate, but the proposition itself is purely homological.

This is a necessary condition. It supplies no new sufficient condition and does not restore the false assertion that all width-six configurations have wrapping two.
