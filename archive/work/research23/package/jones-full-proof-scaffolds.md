# Jones unknot detection: complete conditional proof scaffolds

31 October 2026 · Research notes, not a proof of the conjecture. No novelty claim.

The strategic aim is to identify assumptions under which the **entire** theorem follows, before investing in a difficult local lemma. The hypotheses below are proposed research targets. Naming them does not provide evidence that they are true or tractable.

**Current assessment.** There are complete conditional arguments, but no established route through their central unproved premises. Keep the global homology-boundedness scaffold as the principal target, with ribbon concordances as a geometric test of cancellation. New geometric checks leave **seven table pairs up to simultaneous mirroring**, with no ribbon concordance certified; all require multiple interacting bands. Actual torus knots rule out replacing the whole Jones polynomial by its coefficient magnitudes or an amplitude bound. A quantum moment calculation also disproves automatic positivity for ribbon doubles. A recent quantum braid Floer construction supplies another setting for the missing geometric theorem, but no proof of it. These are restrictions on possible approaches, not evidence that a full proof is close.

## 1. A global route through bounded hidden homology

Normalize the Jones polynomial by \(V_U=1\), and use reduced Khovanov homology over \(\mathbb Q\), with the unknot in bidegree \((0,0)\). Write

\[
r(K)=\dim_{\mathbb Q}\widetilde{Kh}(K;\mathbb Q).
\]

**Proposed hypothesis H-rank.** For every fixed Jones polynomial \(P\) realized by a classical knot, there is a finite number \(B(P)\) such that

\[
V_K=P\quad\Longrightarrow\quad r(K)\le B(P).
\]

The bound may depend on the entire polynomial. It need not be explicit, small, or computable. This assertion allows knots with the same Jones polynomial to have different Khovanov homology.

**Conditional theorem.** H-rank implies that the Jones polynomial detects the unknot.

**Proof.** Suppose \(V_K=1\). Let \(K^{\#m}\) denote the connected sum of \(m\) copies of \(K\). Jones multiplicativity and the reduced Khovanov connected-sum formula over a field give

\[
V_{K^{\#m}}=1,
\qquad
r(K^{\#m})=r(K)^m.
\]

H-rank therefore gives \(r(K)^m\le B(1)\) for every positive integer \(m\). Since \(r(K)\) is a positive integer, it must equal one. Kronheimer–Mrowka's unknot-detection theorem then gives \(K=U\). This proves the conditional theorem. □

This is the useful amplification mechanism: connected sums multiply any hidden homology while leaving a Jones-one polynomial unchanged. No reduction to unknotting number one, a special braid family, or colored Jones information is needed.

### An alternative using the spread of homology

Let

\[
h(K)=\max\{j:\widetilde{Kh}^{i,j}(K;\mathbb Q)\ne0\}
-\min\{j:\widetilde{Kh}^{i,j}(K;\mathbb Q)\ne0\}.
\]

**Proposed hypothesis H-spread.** For every fixed Jones polynomial \(P\), the numbers \(h(K)\) with \(V_K=P\) have a finite upper bound \(D(P)\).

The same argument gives

\[
h(K^{\#m})=m h(K)\le D(1),
\]

so a Jones-one knot has \(h(K)=0\). Its reduced homology lies in a single quantum grading, necessarily zero because its Euler polynomial is one. The reduced/unreduced exact sequence then puts unreduced homology only in quantum gradings \(-1,1\), with twice the reduced total rank. Every nonzero differential in the rational Lee spectral sequence would raise quantum degree by a positive multiple of four. None is possible between these two gradings. The spectral sequence collapses, and Lee homology of a knot has total rank two. Reduced Khovanov rank is therefore one, and Kronheimer–Mrowka again gives the unknot.

Thus H-spread also closes a full proof. A universal bound in terms of Jones span, such as \(h(K)\le C\operatorname{span}_q V_K(q^2)+D\), would suffice, but is stronger than the fixed-polynomial hypothesis and is not required.

### What this changes—and what it does not

- H-rank and H-spread are **unproved proposals**. We have not established either assertion or its novelty. Neither follows from taking a graded Euler characteristic.
- Restricting either boundedness claim just to the polynomial \(1\) gives an assertion equivalent to the original conjecture, by the proofs above. That restricted restatement is not an easier theorem merely because it uses a bound.
- The broader claims are useful research proposals because they concern known nonunit Jones polynomials as well. An explicit family with exactly constant Jones polynomial and unbounded rational Khovanov rank or quantum spread would disprove the corresponding proposal without resolving unknot detection.
- Bounds for prime knots alone do not justify the argument: connected sums leave that class. An additional bridge would be needed.
- Abstract complexes can carry arbitrarily many Euler-invisible pairs. Any successful proof must use geometric restrictions on complexes arising from actual classical knots.

The first research decision is whether either broad boundedness claim survives known fixed-Jones families. A failed test should terminate that version of the scaffold, rather than trigger efforts to prove it anyway.

The first Watson test has now been narrowed. For fixed tangles and braid, we derive a **uniform finite bigrading support window**, including nonsimple inputs: the capped resolutions come from a finite fixed list, and the two normalized skein sequences identify consecutive knot groups outside its shifted support. The argument was independently checked against Watson's diagrams and grading corrections. It does not bound multiplicities inside the window. Thus this orbit cannot refute H-spread; H-rank remains undecided there. No bound uniform over all templates follows. [Watson, Sections 3 and 7.3](https://personal.math.ubc.ca/~liam/files/identical.pdf).

A sharper test for H-spread comes from Wang's band-twist theorem, discussed in Section 4. A Jones-invisible nontrivial band would refute H-spread while leaving H-rank untouched.

### A weaker quantitative target, and a failed shortcut

For a fixed Jones-one knot, it would suffice to bound \(r(K^{\#m})\) subexponentially, or \(h(K^{\#m})\) sublinearly, along any cofinal sequence of integers \(m\). Uniform bounds over an entire fiber are stronger than necessary. On the unit fiber these asymptotic assertions still imply the original conjecture, so the reformulation alone is not progress.

The paired-skein argument supplies one possible mechanism: connect \(K^{\#m}\) to reference knots along actual moves for which the union of all shifted cap supports and reference supports fits in a quantum interval of length \(o(m)\). Exactness would give the needed sublinear bound, irrespective of the number of moves. This geometric construction is unproved.

There is an exact obstruction to doing it factor by factor. Smoothing a move confined to one summand leaves a cap link of the form \(L\#K^{\#(m-1)}\), whose reduced quantum diameter is \(h(L)+(m-1)h(K)\). If \(h(K)>0\), that single cap already has linear spread. Any successful construction must coordinate different summands; repeating local simplifications cannot supply the required bound.

### What a geometric compression theorem would need to retain

There is an actual-knot obstruction to several proposed numerical bounds. For \(K_k=T(3,3k+1)\), \(k\ge1\), the reduced specialization of Schütz's block decomposition gives

\[
V_{K_k}(t)=t^{3k}+t^{3k+2}-t^{6k+2},\qquad r(K_k)=4k+1.
\]

Thus the coefficient magnitudes are always \(1,1,1\), and \(|V_{K_k}(t)|\le3\) everywhere on the unit circle, while homology rank grows without bound. For even \(k\), the determinant is also one. No bound depending only on these coefficient magnitudes, or monotonically on that amplitude bound, can work. The whole polynomials differ: their exponent gaps grow. This does **not** refute H-rank. It shows why a successful theorem must retain more information. [Schütz, Theorem 5.3(2)](https://arxiv.org/html/2501.11547v1).

One concrete sufficient target is the following **unproved geometric matching hypothesis M**: for each whole polynomial \(P\), every knot with Jones polynomial \(P\) has a diagram whose reduced enhanced-state complex admits an acyclic algebraic Morse matching with at most \(F(P)<\infty\) unmatched generators. The matching must use invertible differential entries in the actual state basis. Algebraic Morse reduction would then bound homology by \(F(P)\), giving H-rank and the full conditional proof above. Allowing arbitrary Gaussian reduction after computing homology would merely restate H-rank. No diagram-selection or matching construction establishing M has been found. [Algebraic Morse framework, Kelomäki–Schütz, Theorem 2.2](https://arxiv.org/html/2601.02119v1).

Polynomial factorization alone cannot repair this gap. In fact, H-rank for all knots is equivalent to the conjunction of unknot detection and H-rank restricted to prime knots. The forward direction is above. Conversely, Laurent unique factorization gives finitely many possible nonunit factor polynomials of a fixed \(P\), and knot normalizations \(Q(1)=1\), \(Q'(1)=0\) fix their Laurent units. Detection excludes arbitrarily many Jones-one prime factors; prime-fiber bounds then multiply to an all-knot bound. Thus counting polynomial factors misses precisely the difficult unit-polynomial factors.

### A recent Floer construction: a variant of the same global bottleneck

Anghel–Juhász construct quantum braid Floer homology \(qHFB(\beta)\) over \(\mathbb F_2\), with a spectral sequence to \(\widehat{HFK}(K)\). Its two-variable Euler polynomial specializes to Alexander and Jones polynomials. It depends on the braid presentation and generally changes under both Markov moves. These inputs are read from their preprint; we have not independently reproved its construction. [Anghel–Juhász, Sections 1.8 and 8–9](https://arxiv.org/html/2601.08805v4).

Define \(m(K)\) as the minimum dimension of \(qHFB(\beta)\) over the braid presentations of \(K\) covered by the construction. A bound \(m(K)\le B(V_K)\) would also prove detection: with \(f(K)=\dim_{\mathbb F_2}\widehat{HFK}(K)\), the spectral sequence and HFK connected-sum formula give

\[
V_K=1\quad\Longrightarrow\quad f(K)^n\le m(K^{\#n})\le B(1),
\]

forcing \(f(K)=1\), hence the unknot by Floer genus detection. No connected-sum formula for \(qHFB\) is assumed. This bound remains unproved; on the unit fiber it is again equivalent to the desired conclusion. [HFK connected sums](https://arxiv.org/abs/math/0209056), [genus detection](https://arxiv.org/abs/math/0311496).

Two exact checks prevent mistaking the new construction for the missing theorem. First, the unknot presentations \(\sigma_1\), \(\sigma_1\sigma_2\), and \(\sigma_1^2\sigma_2\sigma_1^{-1}\) have Euler coefficient norms \(3,5,9\), respectively, so their quantum braid Floer ranks are at least those numbers. Jones-one cannot force rank one in every presentation. Second, in the paper's quantum convention the Markov-invariant quotient is

\[
\mathbb Z[x^{\pm1},d^{\pm1}]/((d-1)(xd+1)).
\]

Our direct algebra calculation identifies it exactly with pairs \((A,J)\) of Laurent polynomials satisfying \(A(-1)=J(-1)\), via evaluation at \(d=1,-x^{-1}\). For sufficiency, lift the pair by \(A+x(d-1)(A-J)/(x+1)\); the kernel is precisely the displayed ideal. Thus this quotient carries the Alexander/Jones pair, with no additional mixed polynomial datum. The unquotiented homology may carry more information, but controlling that information geometrically is still the unresolved step. This is a possible workspace for M-like cancellation, not a separate established route around it.

## 2. A topological route through an unknotting crossing

The previous investigation developed a conditional chain connecting nontrivial Jones-one knots of unknotting number one, flat skein data of strongly inverted knot exteriors, and certain essential zero-response satellite patterns. These are derived results in our working notes, not a substitute for independent review.

A full proof through that route still needs **two** geometric inputs:

**G: generic reduction.** From any nontrivial knot with \(V_K=1\), construct a nontrivial knot \(L\) with \(V_L=1\) and \(u(L)=1\).

**R: rigidity in the reduced class.** Rule out the flat, nontrivial strongly inverted exteriors—or equivalently the associated nontrivial Jones-one \(u=1\) examples—by a geometric argument.

Assuming G and R, a hypothetical generic counterexample produces an example forbidden by R, so the full theorem follows. Both assumptions remain unproved.

Our adjacency construction supplies an intermediate step: a hypothetical nontrivial Jones-one \(u=1\) example produces nontrivial Jones-one knots that are \(n\)-adjacent to the unknot, for each prescribed \(n\). This does not supply G. It also does not place the resulting knots in the specific braided construction of the next section.

### A concrete candidate operation for G

Use the convention

\[
t^{-1}V_{L_+}-tV_{L_-}
=(t^{1/2}-t^{-1/2})V_{L_0}.
\]

For two marked crossings, with coherent induced orientations, two applications of this relation give

\[
V_{K_{+,-}}-V_{K_{-,+}}
=t(t^{1/2}-t^{-1/2})
\bigl(V_{L_{0,-}}-V_{L_{-,0}}\bigr).
\]

Consequently, equality of the Jones polynomials of the two displayed smoothing links certifies an exact Jones-preserving simultaneous crossing change. This supplies a precise move to investigate; preserving the polynomial is already justified.

The proposed missing geometric theorem is that suitable certified moves can reach a nontrivial \(u=1\) knot from any hypothetical counterexample. The moves must preserve nontriviality at the required endpoint. A polynomial identity alone does not establish reachability or that endpoint condition.

For an induction version, seek an output with lower Seifert genus unless the knot already has unknotting number one. A minimal-genus Jones counterexample is prime: Jones multiplication forces each prime factor to have Jones polynomial one, and genus is additive. This avoids assuming the unresolved additivity of crossing number. The genus-decreasing operation itself has not been constructed.

A second, more explicit construction target is an actual four-ended tangle \(S_D\) built from a diagram \(D\) of any knot \(K\), satisfying

\[
[S_D]=u_DQ_0+c_D(A)(V_K(A^{-4})-1)(Q_\infty-\delta Q_0),
\qquad \delta=-A^2-A^{-2},
\]

where \(u_D\) is a framing unit and \(c_D\ne0\). Two additional **geometric** properties are essential: a specified meridian closure is an actual unknot, and a nontrivial input gives a double cover that is not a solid torus. Assuming all three properties, Jones-one immediately gives a nontrivial flat exterior and hence the required \(u=1\) example. A formal skein expression is not yet an actual tangle satisfying those topological conditions. This construction remains conjectural.

### A candidate now excluded: the mirrored-three-braid Watson template

For this particular template, let \(J\) be its underlying two-bridge knot and \(D(T),D(U)\) its input denominator closures. Its bracket matrix gives

\[
\det L=\det(J)^2\det D(T)\det D(U).
\]

Consequently Jones-one forces \(\det J=1\), hence \(J=U\). A separate geometric argument, using the three-braid normal form and cancellation of complementary spherical twists, then gives

\[
L\cong D(T)\#D(U).
\]

This conclusion is not inferred from polynomial factorization. The marked topology and algebra were independently audited in our notes. Each denominator summand has Jones polynomial one. If both are nontrivial, genus decreases on passing to either; if one is trivial, the other is the entire output, so there is no descent. A nontrivial \(u=1\) output is prime and therefore already occurs as a denominator summand.

Every coupled-twist orbit in this template containing an actual unknot consequently consists entirely of unknots, even without simple tangles. This closes this proposed converter. It gives no classification of arbitrary Jones-one knots. [Watson's construction, Proposition 5.1 and Figure 7](https://personal.math.ubc.ca/~liam/files/preprint.pdf).

## 3. The quantum norm route and its coverage gap

For the specific doubled-Brunnian-pure-braid/clasp construction analyzed in this investigation, the local projector calculation gives

\[
V_{K_\beta}-1=C(A)\langle w,(U_\beta-I)w\rangle.
\]

On an arc where the finite representation has a positive Hermitian form and is unitary, with \(C\ne0\),

\[
\operatorname{Re}\frac{V_{K_\beta}-1}{C}
=-\tfrac12\|(U_\beta-I)w\|^2.
\]

The calculation has a general local skein argument and an exact check against our explicit knot diagram. Its scope is this particular construction. The coefficient \(C\) can be complex; dropping it before taking real parts would be incorrect.

The complete conditional route is:

1. **Unproved coverage:** convert an arbitrary hypothetical counterexample to a nontrivial Jones-one knot in this particular family.
2. **Derived identity:** Jones-one forces \(U_\beta w=w\).
3. **Unproved geometric stabilizer theorem:** fixing this vector forces the corresponding closure knot to be the unknot.
4. This contradicts the nontriviality preserved in step 1.

Faithfulness of the representation does not replace step 3: faithful representations can have nontrivial vector stabilizers. Also, the norm identity makes step 3 equivalent to Jones detection within the chosen family. It changes the tools available, but does not itself solve that restricted problem.

This route should receive major investment only alongside a credible construction for step 1. Proving its stabilizer theorem alone would not settle the generic conjecture.

## 4. A global route through ribbon concordances

There is an unconditional reduction that avoids the coverage gaps above. For any knot \(K\), its connected sum with its mirror, with reversed orientation when needed,

\[
R=K\#\overline K,
\]

is ribbon. It is nontrivial when \(K\) is nontrivial, and \(V_R(t)=V_K(t)V_K(t^{-1})\). Thus any Jones counterexample produces a ribbon counterexample. This does not claim that every ribbon knot belongs to our special Brunnian braid family. [Symmetric-union construction](https://arxiv.org/abs/0802.2283).

Puncturing a ribbon disk gives a ribbon concordance \(C:U\to R\). Such a concordance induces a bigraded split injection on Khovanov homology. With the based reduced rational theory, write

\[
\widetilde{Kh}(R)=\widetilde{Kh}(U)\oplus E_C.
\]

The graded Euler polynomial of \(E_C\) is \(V_R(q^2)-1\). [Levine–Zemke](https://doi.org/10.1112/blms.12303).

**Proposed hypothesis E.** For actual ribbon concordances between knots, a nonzero homological complement \(E_C\) has nonzero graded Euler polynomial.

**Complete conditional proof.** If \(V_K=1\), then \(V_R=1\), so the Euler polynomial of \(E_C\) vanishes. Hypothesis E gives \(E_C=0\). Therefore

\[
1=r(R)=r(K)^2,
\]

and Kronheimer–Mrowka gives \(K=U\).

Every step except E is supplied by established results. Restricting E to concordances from the unknot is equivalent to the original detection problem through this reduction. Its all-source version is a stronger, independently testable proposal. Neither the split injection nor the ribbon property proves E: a nonzero graded vector space can have identically zero Euler polynomial.

Over \(\mathbb Q\), the bigraded dimensions of the complement are the endpoint dimensions subtracted grade by grade. They therefore do not depend on which ribbon concordance supplies the split injection. A well-chosen movie might reveal a useful geometric constraint, but changing the movie alone cannot remove these cancelling dimensions.

### An exact geometric test supplied by Wang

Let \(K_b\) be a band sum of a split two-component link, and \(K_\#\) the ordinary connected sum of its components. For a nontrivial band, Wang proves a nonzero reduced rational homological complement \(H_b\). Adding \(n\) full twists gives

\[
\widetilde{Kh}(K_{b+n})
\cong\widetilde{Kh}(K_\#)\oplus H_b[2n]\{4n\}.
\]

The Euler difference is therefore \(q^{4n}P_b(q)\), where \(P_b=\chi_q(H_b)\). Wang explicitly leaves open whether \(P_b\) must be nonzero. His Remark 1.9 supplies the reduced rational coefficient version used here. [Wang, introduction and Theorems 1.7–1.8](https://arxiv.org/abs/2006.01070).

An actual nontrivial band with \(P_b=0\) would refute E and H-spread: all its twists would have the same Jones polynomial, while the fixed summand and shifting nonzero complement separate by \(4|n|+O(1)\) in quantum degree. Total rank stays constant, so this would **not** refute H-rank. Our bounded source search found no such example; it does not establish the current literature status exhaustively.

Even proving \(P_b\ne0\) for every such band would leave work: an arbitrary ribbon movie need not decompose into split-link band sums, and nonzero Euler contributions at different stages could cancel. Those would be additional geometric and algebraic requirements, not consequences of the single-band theorem.

### A stronger consequence that calibrates the difficulty

**Conditional theorem.** H-rank and H-spread together imply that every crossing change preserving the Jones polynomial is nugatory. This is stronger than the cosmetic crossing conjecture, which assumes the two knots are isotopic.

To see this, resolve the crossing to an oriented two-component link \(L\). The original knots are consecutive members of the associated oriented-band twist family \(K_n\). In Wang's unnormalized convention, with \(J_U=q+q^{-1}\), the skein relation gives

\[
J_{n+1}=q^4J_n+(q-q^3)J_L.
\]

Thus consecutive differences satisfy \(J_{n+2}-J_{n+1}=q^4(J_{n+1}-J_n)\). One equal pair makes the entire integer orbit Jones constant. H-rank bounds its reduced rational homology ranks. Wang's Proposition 1.7, valid over every field, then forces \(L\) to split. [Wang, *Split link detection*, Proposition 1.7](https://arxiv.org/pdf/2112.09110).

Now the split-band theorem above applies. If the band were nontrivial, its nonzero shifting complement would give unbounded quantum diameter, contradicting H-spread. The band is trivial, which makes the original crossing nugatory. The same argument handles equal Jones polynomials at any two distinct integers in this band-twist family, since the sum \(1+q^4+\cdots+q^{4(m-1)}\) cannot annihilate a nonzero Laurent polynomial.

This gives a sharper falsification test: an actual Jones-preserving non-nugatory crossing would disprove at least one global boundedness hypothesis. A nonsplit smoothing would force unbounded rank; a split smoothing with nontrivial band would force unbounded quantum spread. No such example was certified in this bounded search. The implication also warns against treating the two hypotheses as routine estimates.

There is also an **unconditional restricted consequence**. Call a knot Euler-efficient when its reduced rational Khovanov rank equals the sum of the absolute values of its Jones coefficients; equivalently, its homology has no cancellation within each quantum grade. Every knot whose reduced rational homology lies on one diagonal has this property. In a Jones-constant, non-nugatory band-twist family, only finitely many members can be Euler-efficient. For nonsplit smoothing this follows from Wang's rank divergence. For split smoothing and a nontrivial band, there are no efficient members: the rank is constant, so one efficient member would make every member efficient with the same quantum support, contradicting the shifting nonzero complement. This supplies a rigorous endpoint for a possible geometric reduction. No construction sending arbitrary Jones-one knots into such families with efficient members has been established.

### Why reflection positivity does not finish this route

For a \(2b\)-plat presentation at a unitary specialization, with normalized cup state \(\psi\) and loop value \(\delta>1\),

\[
V_{K\#\overline K}
=\delta^{2b-2}|\langle\psi,U_\beta\psi\rangle|^2.
\]

Jones-one fixes the overlap magnitude at \(\delta^{1-b}\), strictly below one for \(b>1\). It is therefore not an extremal equality forcing the full state to be the vacuum. Reflection measures one scalar channel; other channels remain undetermined. This rules out the proposed automatic positivity argument, without ruling out a new geometric constraint on actual ribbon states.

There are two additional concrete checks. For the symmetric doubles of the trefoil and figure-eight, respectively, the Jones defects at \(t=e^{i\theta}\) begin \(+6\theta^2\) and \(-6\theta^2\). Thus a universal positive norm with a common fixed-sign prefactor cannot equal the ordinary ribbon Jones defect.

At the categorical level, the Khovanov Frobenius algebra is \(\mathbb Q[X]/(X^2)\), with birth \(\eta(1)=1\) and death \(\epsilon(1)=0,\epsilon(X)=1\). A nonzero birth followed by its reversed death is therefore zero. Reversal cannot be a positive Hilbert adjoint, since that would give the nonzero birth vector norm zero. The ribbon split-injection theorem uses the actual sphere and dot relations; it does not turn the Euler characteristic into a positive trace. A successful proof of E must use additional geometry beyond these formal relations.

Nor can one assume that the extreme quantum grades of a ribbon complement have a single homological parity. The retained rational homology data for \(12n25\), combined with mirror duality and the connected-sum formula, give cancelling opposite-parity pairs at both quantum extremes \(j=\pm14\) of its symmetric double. The ribbon image of the unknot is at \((0,0)\), so those pairs remain in the complement. This refutes that proposed stronger mechanism on actual knots; the full Jones polynomial of the example is nontrivial, so it does not refute E.

Using every Markov presentation does not supply the missing measurements. Transporting the ordinary closure functional through conjugation or stabilization gives the same functional, by the Markov identities. At a faithful positive finite-level specialization, stabilization has conditional-expectation variance exactly \((1-\delta^{-2})I\), including for the unknot. Even the unknot presentations \(\sigma_1\) and \(\sigma_1^{-1}\) have distinct writhe-normalized operators with the same trace. Thus the kernel of one trace cannot be treated as the two-sided trace radical. A geometric destabilization theorem remains possible; the scalar identities do not establish it. The calculations and precise positivity domains are in the accompanying audit, using the [Aharonov–Jones–Landau trace conventions](https://arxiv.org/pdf/quant-ph/0511096).

### A precise failure of the positive-moment proposal

Let \(H_N\) denote zero-framed colored Jones polynomials normalized to one on the unknot. In the \(SU(2)\) fusion algebra at level \(r-2\), define \(\phi_R(\chi_N)=d_NH_N(R;e^{2\pi i/r})\), where \(d_N=\sin(N\pi/r)/\sin(\pi/r)\). For a ribbon double \(R=K\#\overline K\), these basis values are nonnegative, but the functional need not be positive on squares.

For the trefoil double at \(r=6\), exact evaluation gives \(H_2(R)=3\), \(H_3(R)=1\). Since \(x=\chi_2\) satisfies \(x^2=1+\chi_3\),

\[
\phi_R(x)=3\sqrt3,\qquad \phi_R(x^2)=3,
\qquad \phi_R((x-3\sqrt3)^2)=-24.
\]

This actual ribbon knot disproves automatic positivity of this annular functional. It does not contradict positivity of the different Hilbert-space pairings in unitary TQFT. The framing and colored-trefoil evaluations are recorded with an exact arithmetic verifier, using [Morton's torus-knot formula](https://www.liverpool.ac.uk/~su14/papers/colouredjones.pdf).

If positivity could instead be proved specifically when \(V_K=1\), the fundamental moment would equal the largest eigenvalue of \(x\). Positivity would force a point mass at that eigenvalue and all colored polynomials of the double would be trivial. But on this locus the positivity premise is **equivalent to that colored promotion**, so naming it does not solve the gap. Completing this particular chain would also require an unproved AJ-type implication; the established A-polynomial detector does not by itself establish colored-Jones detection. [Dunfield–Garoufalidis, Section 1.3](https://arxiv.org/pdf/math/0405353).

### A finite falsification screen for E

We screened 12,965 retained KnotInfo records, including their mirror variants, for equal Jones polynomials and a strict grade-by-grade increase of reduced rational Khovanov dimensions. There were 460 directed pairs. Knot Floer injection and Alexander divisibility reduced these to 134; Rasmussen's concordance invariant reduced them to 54. The other checks—reduced integral and mod-2 Khovanov splitting constraints, smooth four-genus, tau, and signature—removed none further. These give **27 pairs up to simultaneous mirroring**, involving 47 endpoint knots. Jones polynomials of all 47 endpoints were independently checked from their planar diagrams. Homology values remain sourced from the table.

These are possible counterexamples to the broader premise E **only if an actual ribbon concordance is constructed**. Passing necessary conditions does not supply one. An earlier one-band screen examined 5,732 short bands and found no recognizable removal. That computation was unnecessary: all the candidate endpoints have equal Seifert genus, and the geometric obstruction below excludes every one-band realization, on every diagram. Retain the computation as historical evidence, but do not extend that search.

### A derived relative Lee-bar obstruction

There is a stronger necessary condition than grade-by-grade Khovanov injection. Write \(P_L(u,q)\) for the reduced rational Khovanov Poincaré polynomial of a knot \(L\). If a ribbon concordance \(J\to K\) has \(d\) births and \(d\) saddles, then

\[
P_K(u,q)-P_J(u,q)
=\sum_{a=1}^{d}(1+u q^{2a})S_a(u,q),
\qquad S_a\in\mathbb Z_{\ge0}[u^{\pm1},q^{\pm1}].
\]

Here is the reason. Let \(i\) and \(p\) be the maps of the concordance and its reverse on lifted Lee homology over \(\mathbb Q[X]\). Ribbon splitting gives \(pi=\mathrm{Id}\). The two evaluations of the same cobordism in Sarkar's proof give \(X^d\ker p=0\). Thus the relative graded module adds only torsion bars \(X^a\) of length at most \(d\). Graded decomposition over the polynomial PID, followed by specialization \(X=0\), gives exactly the displayed nonnegative sum. This is a deduction from [Sarkar, Section 6](https://arxiv.org/pdf/1903.11095) and the graded decomposition used by [Dunfield et al., Section 6.2](https://arxiv.org/html/2303.04233v1), not a claim that those sources state this precise relative corollary.

For \(d=1\), differentiating the Euler specialization at \(q=1\), using \(V'_L(1)=0\), gives \(S_1(-1,1)=0\). Consequently \(r(K)-r(J)\) is divisible by four. For larger \(d\), differentiation gives only \(\sum_a aS_a(-1,1)=0\); no general rank congruence follows.

We tested the full nonnegative pairing condition by exact integer flow on the graded dimensions. Of the initial 54 directed pairs, six fail even when every positive bar length is allowed. They are

- \(12n338\to12n244\);
- \(13n4838\to13n627\);
- \(13n4838\to13n716\);

and their simultaneous mirrors, with the endpoint chirality choices recorded in the data. Subject to the tabulated homology values, these pairs admit **no ribbon concordance** in the indicated direction. This leaves **48 directed pairs, or 24 mirror classes**, involving 42 underlying table knots. Of these, 42 directed pairs pass the one-band polynomial test; the other six require at least two births and saddles. Passing a bar test still does not construct a concordance. The full proof, explicit pairing certificates, and failed-flow certificates are retained in the accompanying evidence archive. A separate verifier reconstructed all 54 homology differences from the included table subset and checked every certificate; it needs only Python's standard library.

### Geometric rigidity reduces the list to seven classes

If \(J\to K\) is ribbon, \(K\) is fibered, and \(g(J)=g(K)\), then \(J\) and \(K\) are isotopic. The target-fibered version is stated explicitly in [Zemke, Section 1.5, p. 935](https://annals.math.princeton.edu/wp-content/uploads/annals-v190-n3-p05-s.pdf). All 48 remaining directed pairs have equal genus. In 34, the target is fibered, so those are excluded. The top knot Floer rank test agrees with the independent table's fibered field in every case.

The remaining **14 directed pairs form seven simultaneous-mirror classes**:

| Source | Target | Common genus |
|---|---|---:|
| mirror \(13n2215\) | \(13n3605\) | 3 |
| \(13n3301\) | \(13n3041\) | 3 |
| mirror \(13n5018\) | \(13n1003\) | 3 |
| \(13n3820\) | mirror \(13n3898\) | 3 |
| \(13n3820\) | mirror \(13n3899\) | 3 |
| \(13n3821\) | mirror \(13n3939\) | 4 |
| \(13n3821\) | mirror \(13n3941\) | 4 |

No ribbon concordance between these endpoints has been certified. These are tests of the stronger hypothesis E, not candidate Jones-one knots.

There is a further global movie restriction. A one-birth/one-saddle ribbon concordance presents its target as a band sum of the split link \(J\sqcup U\). If its genus equals \(g(J)\), the equality case of the band-sum genus theorem supplies a band-compatible minimal Seifert surface for \(J\) and a spanning disk for \(U\). A neighborhood of that disk gives a splitting sphere crossing the band in one cocore. The band is trivial, so the endpoints are isotopic. Both ingredients appear in [Miyazaki, proof of Lemma 5 and Theorem 1, Case 1](https://arxiv.org/pdf/1903.11266).

Consequently any ribbon movie between distinct equal-genus knots must have at least two births and a level with at least three link components. Otherwise it factors through one-birth/one-saddle knot stages; genus monotonicity forces every stage to preserve genus, making every stage endpoint-trivial. Six of the seven surviving classes pass the length-one algebraic bar test, but none can have a one-band movie. The \(13n5018/13n1003\) class already requires length two algebraically.

Equal genus alone does not exclude general ribbon concordance: Whitehead satellites give distinct genus-one ribbon-related knots. [Baker, Remark 6](https://arxiv.org/pdf/1409.7646). Thus a constructive test of E here must use interacting bands. Familiar equal-Jones families do not automatically provide them: the Moore–Starkston genus-two mutant pairs have equal total rational Khovanov rank but different bigradings, excluding either directional ribbon injection; distinct Kanenobu knots are fibered of equal genus, so the rigidity theorem excludes those relations too. [Moore–Starkston, Corollary 4.2](https://msp.org/agt/2015/15-1/agt-v15-n1-p02-s.pdf), [Hedden–Watson, Section 6.5](https://d-nb.info/114370181X/34).

Nor can an arbitrary ribbon disk with cyclic complement group replace the missing cancellation theorem: nontrivial boundaries with such disks are explicitly constructed by [Nakanishi–Nakagawa, proof of Theorem 3(b)](https://da.lib.kobe-u.ac.jp/da/kernel/E0001171/E0001171.pdf). Any argument using the canonical double's disk must retain that particular disk and its boundary data.

## 5. How to choose the next investigation

| Route | Does the argument reach arbitrary knots under its assumptions? | Main unresolved work | First useful falsification test |
|---|---|---|---|
| Homology boundedness | Yes, directly by connected sums | Establish a bound for actual knots with one fixed Jones polynomial | Find a fixed-Jones family with unbounded rational rank or quantum spread |
| Ribbon-concordance complement | Yes, by the unconditional \(K\#\overline K\) construction | Prove E for actual ribbon maps | Find equal-Jones endpoints of a ribbon concordance with nonzero homological complement |
| Topological reduction | Yes, assuming both G and R | Construct the reduction and prove rigidity in its target class | Test the proposed crossing moves for polynomial preservation, nontriviality, and descent |
| Quantum norm | Yes, assuming coverage and the stabilizer theorem | Establish both geometric statements | Test whether the construction covers the outputs of our reductions before tackling stabilizers |

The homology route has the shortest conditional argument; the ribbon route adds concrete geometry without a separate coverage assumption. Neither central premise has been proved. The topological route still needs a new converter after the Watson exclusion. The quantum identity remains restricted to a special family.

The next substantial investment should address a genuinely global bottleneck: a constraint on ribbon-concordance complements, or a geometric reason hidden rank cannot grow indefinitely at fixed Jones polynomial. Hypothesis M makes the latter into a concrete diagram-selection and matching problem, but no construction has yet passed a general test. The new Floer setting faces the same obstruction; it should not launch a separate research branch without a proposed geometric cancellation mechanism. Further Watson calculations and one-band searches on the surviving table pairs currently have no path to either bottleneck.

The proposed working rule is: pursue a difficult lemma only after writing the full conditional argument, checking that its conclusions match the next step's hypotheses, and identifying a concrete way the lemma could fail.

## Sources and provenance

- Kronheimer and Mrowka, *Khovanov homology is an unknot-detector*: https://arxiv.org/abs/1005.4346. This supplies the rank-one endpoint, not H-rank or H-spread.
- Khovanov, *Patterns in knot cohomology I*: https://arxiv.org/abs/math/0201306. Background for reduced homology and connected sums.
- Lee, *An endomorphism of the Khovanov invariant*: https://arxiv.org/abs/math/0210213. Background for the rational deformation and spectral-sequence endpoint.
- Lidman and Moore, *Adjacency of three-manifolds and Brunnian links*: https://arxiv.org/abs/2308.06211. Geometric input for the adjacency construction; it does not supply generic reduction G or braid-family coverage.
- Stoimenow, *Some applications of Tristram–Levine signatures and relation to Vassiliev invariants*: https://doi.org/10.1016/j.aim.2004.07.003. Source of the particular braid/clasp family.
- Our previous conditional reduction and its exact example are recorded in `jones-brunnian-reduction-and-exact-test.txt` in this output directory. The norm calculation and the present scaffold still require the usual independent mathematical review before any publication claim.

No full proof or counterexample has been obtained.

The latest exact checks, candidate subset, independent audits, and portable verifiers are saved in [the global geometry and quantum tests archive](jones-global-geometry-and-quantum-tests.zip). The scripts verify the stated algebra and table deductions; they do not verify the original published theorems or certify any remaining ribbon concordance.
