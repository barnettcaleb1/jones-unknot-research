# Closure-invisible objects: a categorical obstruction and a precise positivity gate

**Archive audit correction:** the generic obstruction and positivity discussion below are not new progress. The root agent identified stronger previously banked versions in EARLY-39/LATE-30/LATE-50, including explicit four-special objects satisfying the curved extension conditions. Do not reopen this generic route or count this note as a new result. The targeted continuation is in `two_special_bn.md`: a restricted s=0 obstruction and an explicit nonzero-slope countermodel to a broader support-only argument.

Scope: bounded structural pass for U5/Lemma Q, with no enumeration. No proof of Lemma Q or Jones unknot detection is obtained. The concrete result below is an elementary categorical obstruction, not a claim of a realizable tangle counterexample.

## 1. Current literature that matters

The 2026 preprint [Kotelskiy–Watson–Zibrowius, *On mutation invariance in Khovanov homology*](https://arxiv.org/pdf/2602.23442), Theorem 3.19, classifies every reduced Khovanov tangle component over a field as a rational or special curve, with specified standard local systems and arbitrary overall bigrading shift. Theorem 10.4 supplies a curved A-infinity extension of the actual tangle complexes; this is a real geometric restriction, used to rule out wrapping around the distinguished puncture. It does **not** claim that all collections of allowed components are realizable by tangles, nor does it constrain their total Euler characteristic enough to prove Lemma Q. Its Lemma 6.4 records that a rational filling curve pairs with a same-slope special component with rank zero.

[Kotelskiy–Lidman–Moore–Watson–Zibrowius, *Cosmetic operations and Khovanov multicurves*](https://pmc.ncbi.nlm.nih.gov/articles/PMC11139753/), Theorems 1.2 and 3.1, use full homology: respectively, they constrain actual equal fillings of an unknot-closure tangle and detect split tangles. An Euler equality cannot be substituted for either homological hypothesis. Their gluing model makes the obstruction in Section 2 transparent.

[Haiden–Katzarkov–Kontsevich, *Flat surfaces and stability structures*](https://pmihes.centre-mersenne.org/articles/10.1007/s10240-017-0095-y/), supplies genuine stability structures on appropriate surface Fukaya categories, with curves and flat geometry as the underlying objects. This provides a possible language for the positivity gate in Section 4. It does not establish the required compatibility with tangle realization or with the Jones central charge.

## 2. Definition: a closure-invisible object

Let C be a graded triangulated category modeling the tangle invariant, and let F_mu:C -> D^b(k-grVect) be the exact rational-closure pairing functor. Call E **mu-invisible** if F_mu(E)=0. In the curve model, special components of slope mu give nonzero examples. Let R be a rational tangle object with F_mu(R)=k in the chosen normalization.

This definition is intrinsic to the full closure functor, rather than to Euler characteristic. It is useful because the actual unknot closure constrains F_mu(M), but leaves its kernel unobserved.

### Formal invisible-pair lemma

Suppose E is a nonzero mu-invisible object. Put

    M = R direct-sum E direct-sum E[1],

where [1] is homological shift, with quantum grading held fixed. Then:

1. F_mu(M) = F_mu(R) = k.
2. [M] = [R] in the quantum-graded Grothendieck group.
3. Every exact closure functor F_nu has the same graded Euler characteristic on M and R.
4. If some F_nu(E) is nonzero and finite dimensional, then F_nu(M) has strictly larger total rank than F_nu(R). Hence M is not isomorphic to R.

Proof: additivity and exactness give F_mu(E[1])=F_mu(E)[1]=0. In K_0, [E[1]]=-[E], including coefficientwise quantum grading, proving (2). Euler characteristic of F_nu(E)+F_nu(E)[1] cancels, proving (3). Total ranks add rather than cancel, proving (4).

For a special curve of slope mu, a transverse rational test slope nu gives the nonzero test needed in (4). The constructed object consists entirely of curve types allowed by the geography theorem, and adding E and E[1] does not alter the count or slope of the rational component.

**Scope:** this is a formal object, not an actual tangle. Realizability is precisely what is missing. It therefore does not refute Lemma Q. It proves that the package "allowed curve types + rational Euler class + full rank-one meridional closure" cannot establish Lemma Q at the level of arbitrary category objects.

## 3. What this rules out, and what it does not

Any proposed extra condition stable under finite direct sums and homological shifts also survives invisible-pair attachment, provided E and R satisfy that condition. Examples at the abstract level include existence of specified null-homotopies, and existence of lifts along a restriction functor when lifts of R and E have been supplied. Direct sums of such lifts and their shifts lift M.

One must **not** infer from KWZ Theorem 10.4 alone that an individual special summand lifts: an extension of a direct sum need not split into extensions of its summands. I have not established that splitting, and therefore do not claim the specific M above satisfies every curved extension condition. The safe conclusion is narrower: merely saying "unobstructed/extendable" cannot be used as a positivity principle without showing why the actual realizability or extension requirement excludes these invisible shifted pairs. The extension problem could itself contain useful non-additive information.

The new 2026 component classification does not close the Euler gap by itself. In particular, no argument using only the individual permitted shapes and local systems can exclude M. It must impose a global constraint on their shifts, extensions, or simultaneous realization.

There is also a mutation barrier: the same 2026 paper proves reduced Khovanov homology over any field is invariant under component-preserving mutation. A universal reconstruction of all knot topology from this category would be too strong. Unknot detection remains compatible with mutation invariance, but topology reconstructed by a proposed argument must be scoped accordingly.

## 4. A precise positivity gate, with its missing hypotheses exposed

Here is a valid conditional theorem that explains what a stability argument would have to supply.

Let f:R -> M be a comparison morphism whose closure F_mu(f) is a quasi-isomorphism. Let D=Cone(f). Suppose:

(i) [M]=[R] in the graded Grothendieck group;

(ii) D lies in the heart A of a bounded t-structure;

(iii) a group homomorphism ell:K_0(C) -> R is strictly positive on every nonzero object of A.

Then D=0 and f is a quasi-isomorphism. Indeed, [D]=[M]-[R]=0, whereas a nonzero D in A would have ell([D])>0.

A concrete sufficient setting for (iii) is a finite-length heart with finitely many simples whose classes remain independent in K_0(C), with ell equal to the sum of their composition multiplicities. A stability condition can give the analogous assertion when all relevant charges lie in a strict common half-plane; one must check the boundary cases rather than simply invoke "stability".

This criterion avoids asking for equality of total Khovanov ranks. Its ingredients can be tested separately: compute whether f exists, its cone, and its membership in a fixed heart. But **both the comparison map and the heart-membership statement are missing in Lemma Q**. Rank-one meridional closure only produces a map from the meridional tester, not automatically a map from the rational bracket twin R. Choosing a heart after seeing a desired conclusion would be circular. A universal actual-unknot-closure implies heart condition has no evidence and must first survive the standard trefoil and figure-eight quotient tangles and the Whitehead-tower examples.

The invisible-pair lemma predicts the necessary geometric content: a viable heart must separate E and E[1], and some property of actual tangle realization must force the relevant defect into one side. This is a potential research gate, not an established new route to the theorem. Without that realization mechanism it is no stronger than the parked C1 proposal.

## 5. Judgment for the current scaffold

The most useful result of this pass is the explicit invisible-pair obstruction. It isolates what "beyond Euler characteristic" must mean: not more additive numerical data or the existence of a categorification, but a non-additive restriction on which categorical objects can arise from an actual tangle with an unknot closure.

The most specific possible next theoretical target is whether the **particular curved A-infinity extension attached to an actual tangle** imposes a global compatibility on opposite homological shifts of meridionally invisible components. This cannot be inferred from existence of separate abstract lifts; an obstruction would have to use how the tangle supplies the extension. No such obstruction is proved here. This is preferable to another rank sweep, but it is still an OPEN mechanism and should not be promoted to TRUSTED.
