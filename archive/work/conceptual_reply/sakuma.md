# Strong-inversion link dictionary

Bounded conceptual literature pass, 2026-11-03. No computation, no scaffold change.

## Answer to A

**Do not identify the zero-surgery branch link N with Sakuma's eta link.** Write p:S3 -> S3/tau, B=p(Fix(tau)), and choose disjoint equivariant preferred longitudes l,tau(l) of kappa. Sakuma's link is

    S(kappa,tau) = B union p(l union tau(l)).

Both components are unknots. Its preferred-framing definition needs the inversion, but no selected half-axis. Its eta function distinguishes the axis component. Snape, *Homological invariants of strongly invertible knots* (2018), §2.1 pp.23–26 and §3.1 p.54, gives this construction and normalization explicitly. His §3.2 p.67 already defines the Jones invariant of these links and asks whether it detects the strongly invertible unknot. Thus this proposed invariant direction has direct prior art. [Thesis](https://theses.gla.ac.uk/39015/1/2018SnapePhD.pdf).

The thesis's §2.3 p.47 also identifies the annular closure of Watson's quotient tangle with the axis B inside the complement of the other Sakuma component. This is a potential exact connection to the previously parked annular reformulation, subject to matching our longitude/framing conventions. No scalar formula is asserted here.

**Axis-swap warning.** This Watson annular pattern is B in E(L), whereas Sakuma's eta calculation uses lifts of L in E(B). These are opposite choices of annular axis. Equality or triviality of one annular skein class cannot simply be fed into the other's eta function.

Narrow followup: the indexed thesis introduction, Proposition 0.1.5–0.1.6 (p.xxii), compares strengths: certain adjacent (2,m) torus-knot strong inversions have equal eta invariants, while their annular Jones invariants differ. No derivative or specialization formula recovering eta from Jones/annular Jones was located in the narrow check. Whether the thesis contains one elsewhere is **unknown**, not a negative theorem; no such relation should be used in our scaffold.

## Three constructions must be kept apart

Our N is the fixed set in the *filled quotient*: Sigma_2(N)=S3_0(kappa). In the downstairs theta-curve picture it results from band surgery on B along the quotient arc p(kappa). By contrast, the lift of Sakuma's non-axis component in the double cover branched over B is l union tau(l), a parallel pair of kappa. These are different operations. In particular the general N need not have two unknotted components, whereas the Sakuma link does. Even in an example where both do, their coincidence needs proof.

The butterfly link is a third object: it lives upstairs and is obtained by banding kappa along a chosen half-axis, with twists adjusted to the prescribed linking number. The involution exchanges its two components. A direction consists of that half-axis plus an orientation of the axis. See Di Prisa, *Equivariant algebraic concordance of strongly invertible knots*, Definitions 2.1 and 2.8. [Primary paper](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/topo.70006).

The moth link is kappa together with a meridian of the inverse-fusion band core, again upstairs. See Di Prisa–Framba, *A new invariant of equivariant concordance and results on 2-bridge knots*, Definition 5.2 and Figure 9. [Primary paper](https://msp.org/agt/2025/25-2/agt-v25-n2-p12-p.pdf). It is not N either.

## Consequence for the proposed route

Eta(N) is definable whenever N has linking number zero, but one cannot import formulas for eta(S(kappa,tau)), the butterfly function, or the moth function by calling them the same link. A comparison theorem or a specific local skein construction is needed.

There is a sensible narrower comparison to pursue only if useful: the annular closure identification may show that a flat relative bracket gives the trivial annular Sakuma class. That would place Lemma Q beside Snape's explicit detection question. It would still be a reduction to another detection problem, not evidence of noncancellation. The annular embedding and peripheral markings, rather than the S3 knot type of a component, carry the missing information.

Access note: the thesis PDF exceeds the web tool's size limit; the specified pages were read through its indexed primary-source extracts. The original Sakuma PDF was not successfully fetched in this pass. Do not treat this as a diagram-level verification of the annular normalization.
