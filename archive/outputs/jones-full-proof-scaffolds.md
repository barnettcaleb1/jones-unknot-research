# Jones unknot detection: complete conditional proof scaffolds

Updated 1 November 2026 UTC · Research notes, not a proof of the conjecture. No novelty claim.

The strategic aim is to identify assumptions under which the **entire** theorem follows, before investing in a difficult local lemma. The hypotheses below are proposed research targets. Naming them does not provide evidence that they are true or tractable.

**Pass 50 update.** An internally checked argument now proves the framed rational-solution uniqueness statement formulated as Sikora's Conjecture 2, including the unlink-product case. It retires the entire proposed rational/nonrational two-probe construction. It does not prove Jones unknot detection: the known implication runs from detection to this uniqueness statement, and no converse or generic reduction has been established. See [the complete proof and its precise scope](/Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/outputs/jones-rational-tangle-uniqueness-proof.txt). The assessments below retain their historical scope; they should not be read as overriding this later exclusion.

**Current assessment, through pass 32.** A further complete conditional endpoint uses the total hyperbolic volume of knot exteriors: a bound throughout one nonempty Jones fiber would prove detection. The zero-volume exception is excluded by positivity of the second Conway coefficient for every nontrivial graph knot. The required whole-fiber bound remains unproved. A separate construction shows that arbitrarily large hyperbolic volume is compatible with any prescribed finite Jones Taylor jet and finite set of root-of-unity evaluations agreeing with the unknot, even with Alexander polynomial one. Thus those finite probes cannot replace the full polynomial. New spectral and dyadic-representation frameworks were also tested; neither supplies the missing bound or kernel automatically. Section 15 gives the proofs and limits. No full proof or counterexample to unknot detection has been obtained.

Pass 31 eliminated the proposed projective-span route. We derived \(\beta_{\Re}(K)=c(K)\) for classical local knots, with a proof using the double cover and an integer winding index. Consequently the proposed inequality \(\beta_{\Re}(K)\le\operatorname{span}V_K\) fails for \(T(3,4)\): its Jones span is five, while its Alexander span already forces at least six crossings. This targets the auxiliary inequality in Boyle–Spyropoulos. The proof and grading conventions received independent internal audits, and both polynomials were recomputed from the actual braid. No external-review or novelty claim is made for these research deductions.

The recent passes also supply an actual finite-resolution mechanism for the Watson rank bound, a finite satellite scalarity test, and a product formula excluding compensating cancellation in a two-input Bing family. Finite ordinary-Jones Taylor expansions and fixed ordinary-polynomial bounds on color-three span have been excluded as substitutes for the missing premises. These results close specific research branches or sharpen exact certificates. They do not establish that a full proof is close. Section 5 makes the research decisions explicit; Sections 6–15 record deductions and their limits. Section 14 supersedes Section 13's recommendation to pursue a general Jones-to-projective-complexity bound.

## The common global scaffold: one nonempty fiber is enough

The several boundedness proposals below share ONE amplification mechanism. They should not be counted as independent evidence for the conjecture.

**Conditional theorem.** Suppose there exists a Jones polynomial \(P\), realized by at least one knot, such that the bridge numbers of ALL knots with Jones polynomial \(P\) have a finite upper bound. Then the Jones polynomial detects the unknot. The polynomial \(P\) need not be \(1\), and the bound need not be effective.

**Complete proof.** Choose an anchor knot \(J\) with \(V_J=P\). If \(V_K=1\), put \(L_m=J\#K^{\#m}\). Multiplicativity gives \(V_{L_m}=P\). Schubert's connected-sum formula gives

\[
b(L_m)=b(J)+m\bigl(b(K)-1\bigr).
\]

The assumed finite bound forces \(b(K)=1\), so \(K\) is the unknot. This proves the entire conditional statement. No prime-knot restriction or special diagram class is allowed in its premise. [Schultens, *Additivity of Bridge Numbers of Knots*](https://arxiv.org/abs/math/0111032). □

Exactly the same anchored argument works with reduced rational Khovanov rank, or with its quantum spread, defined in Section 1:

\[
r(L_m)=r(J)r(K)^m,\qquad h(L_m)=h(J)+m h(K).
\]

The established endpoints used in Section 1 then give the unknot. Thus a hypothetical nontrivial Jones-one knot would force **every nonempty Jones fiber** to have unbounded bridge number, reduced rational Khovanov rank, and quantum spread. A bound on any ONE of these quantities in any ONE such fiber would suffice.

This narrows the research requirement relative to the all-polynomial hypotheses below. It permits choosing a nonunit polynomial whose coefficients might support an additional geometric argument. We have not found such an argument or proved the bound for a single unrestricted fiber. Choosing a simple anchor does not eliminate the difficult hypothetical knots \(J\#K^{\#m}\). A theorem only for prime knots, a fixed twist template, or knots already known to admit bounded bridge presentations would miss them.

The corresponding minimal next target is therefore: **identify one realizable polynomial and a geometric or categorical mechanism bounding one of these quantities throughout its entire fiber.** A conditional proof assuming that bound is complete; proving the bound remains a major mathematical step. The unit-fiber version is equivalent to unknot detection, and no claim is made that a selected nonunit-fiber version is easier.

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

The Watson test is now resolved in the boundedness sense. The earlier paired-skein argument supplied a uniform finite bigrading support window but did not bound multiplicities. Pass 26 supplies a different argument: resolve all fixed input-tangle crossings first. Each elementary closure is either a simple Watson knot or an explicit unlink. This bounds total rank even for nonsimple inputs. More precisely, Section 9 proves \(r(K)\le4^N\max\{\det K,4\}\), uniformly over the twist parameter and braid, where \(N\) counts fixed input-tangle crossings. Thus no one fixed Watson orbit can refute H-rank or H-spread. No bound on \(N\) throughout an unrestricted Jones fiber follows. [Watson, Lemma 3.1 and Section 7.3](https://personal.math.ubc.ca/~liam/files/identical.pdf).

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
| Bridge-number boundedness | Yes, directly by Schubert's connected-sum formula | Bound minimum plat bridge number on a whole fixed-Jones fiber | Find such a fiber with certified unbounded bridge number |
| Exterior-volume boundedness | Yes, by additivity and the graph-knot exclusion in Section 15 | Bound total hyperbolic JSJ volume throughout one whole Jones fiber, including composites | Produce an exact fixed-Jones family with unbounded total exterior volume; finite probes cannot substitute |
| Projective diagram compression | Conditional endpoint valid, but the proposed span and all-fiber bounds are refuted in Section 14 | For classical knots this is exactly crossing-number boundedness, equivalently finiteness of a selected fiber | Known infinite fixed-Jones families already refute the all-fiber version |
| Ribbon-concordance complement | Yes, by the unconditional \(K\#\overline K\) construction | Prove E for actual ribbon maps | Find equal-Jones endpoints of a ribbon concordance with nonzero homological complement |
| Topological reduction | Yes, assuming both G and R | Construct the reduction and prove rigidity in its target class | Test the proposed crossing moves for polynomial preservation, nontriviality, and descent |
| Quantum norm | Yes, assuming coverage and the stabilizer theorem | Establish both geometric statements | Test whether the construction covers the outputs of our reductions before tackling stabilizers |
| Generic representation kernel, for a counterexample | Yes: Ito supplies a nontrivial knot once a nontrivial generic kernel is established | Construct an actual braid in the full generic Jones kernel | Verify every representation block exactly and independently verify braid nontriviality |
| Four-moment braid family, for a counterexample | Yes, if both moment identities and a knot-nontriviality certificate hold | Realize the moment equations in an actual braid image and satisfy the topology certificate | Test the four exact identities before any family search; matrix-only solutions do not suffice |

The homology route has the shortest conditional argument; the ribbon route adds concrete geometry without a separate coverage assumption. Neither central premise has been proved. The topological route still needs a new converter after the Watson exclusion. The quantum identity remains restricted to a special family.

The next substantial investment should address a genuinely global bottleneck: a constraint on ribbon-concordance complements, a geometric reason hidden rank or bridge number cannot grow indefinitely in one whole Jones fiber, or an actual generic representation kernel. The anchored theorem above shows that controlling every polynomial is unnecessary. Section 14 now rules out the proposed projective bound as a general mechanism. Hypothesis M makes the homological option into a concrete diagram-selection and matching problem, but no construction has yet passed a general test. The Floer setting faces the same obstruction; it should not launch a separate research branch without a proposed geometric cancellation mechanism. Further Watson calculations and one-band searches on the surviving table pairs currently have no path to these bottlenecks.

The proposed working rule is: pursue a difficult lemma only after writing the full conditional argument, checking that its conclusions match the next step's hypotheses, and identifying a concrete way the lemma could fail.

This does not mean assuming the central premise and calling the remaining chain a solution. The chains above are already complete under their assumptions. Further investment is justified only by a mechanism for a missing premise: an explicit family of geometric moves, a controllable differential, or an actual braid construction. A named boundedness or positivity assumption, a new analogy, and additional negative examples do not by themselves provide such a mechanism.

## 6. Global obstructions to geometric compression

### Raw spanning-tree compression is false on a whole fixed-Jones fiber

Let \(\tau(D)\) be the number of spanning trees of the unsigned Tait graph of a knot diagram, and minimize this number over all diagrams of \(K\). The published spanning-tree complex gives \(r(K)\le\tau(D)\). However, we derive

\[
\tau_{\min}(K)\ge c(K),
\]

where \(c(K)\) is crossing number. Here is a graph proof. A loopless bridgeless connected graph has at least as many spanning trees as edges. For a nonseparable block, start an open ear decomposition at a cycle. Adding an ear of length \(\ell\) with endpoints \(u,v\) changes the tree count to \(\ell\tau+F_{uv}\), where \(F_{uv}\ge1\) counts spanning two-component forests separating the endpoints. Since the old count is at least two, the increase is at least \(\ell\). For several blocks, tree counts multiply and edge counts add; the product of their edge counts, each at least two, bounds their sum. In a knot diagram, removing nugatory crossings deletes loops or contracts bridges without changing tree count or knot type. The resulting reduced diagram therefore proves the inequality. The crossing-free unknot causes no exception.

Kanenobu supplies infinitely many distinct knots with the same entire Jones polynomial. Their crossing numbers are unbounded, so their minimum tree counts are unbounded. Thus a proposed bound \(\tau_{\min}(K)\le F(V_K)\) is false. The same obstruction applies to raw spanning quasi-tree counts via the established tree/quasi-tree correspondence. This does **not** refute H-rank: the differential can cancel arbitrarily many generators. It shows that a successful matching mechanism must perform essential cancellations on every possible diagram of some fixed-Jones families. [Spanning-tree complex](https://arxiv.org/html/math/0607510v3), [Kanenobu's infinite family](https://www.ams.org/journals/proc/1986-097-01/S0002-9939-1986-0831406-7/S0002-9939-1986-0831406-7.pdf), [quasi-tree correspondence](https://arxiv.org/html/0705.3453).

Two actual-homology tests further restrict possible cancellation rules. For \(T(3,4)\),

\[
P(u,q)=q^6+u^2q^{10}+u^3q^{12}+u^4q^{12}+u^5q^{16}.
\]

The zero Jones coefficient at \(q^{12}\) conceals two actual homology classes, so it is not an acyclic quantum column. For the table convention of \(10_{132}\), the largest reduced rational homology grading is \(-2\), whereas the largest Jones grading is \(-4\). Taking \(m\) connected summands produces an exterior difference of \(2m\). Thus neither zero-coefficient cancellation nor containment in the Jones exponent interval with a universal constant margin can be used as a general lemma. The latter family has varying whole Jones polynomials and does not refute H-spread. The torus formula is from [Schütz, Theorem 5.3](https://arxiv.org/html/2501.11547v1); the second calculation uses the retained KnotInfo vector, whose arithmetic is included in the evidence.

There is a separate published obstruction to controlling the size of a braid presentation. Takioka's Kanenobu family \(k(n)\) has a single HOMFLYPT polynomial, hence a single Jones polynomial, but braid index at least \(n+3\) for \(n\ge3\). Therefore the **minimum number of braid strands** is also unbounded on a fixed Jones fiber. A proposed physics interpretation that bounds particle number from the whole Jones polynomial cannot provide the global compression theorem. This concerns braid index, not bridge number or homology rank. [Takioka, Theorem 1.1](https://pdfs.semanticscholar.org/1cfd/410a7f28da8ead9f610c18d6bcce6b0886cf.pdf).

### A distinct complete scaffold using bridge number

Let \(b(K)\) be classical bridge number, or half the minimum strand count of a plat presentation. Consider the **unproved** whole-polynomial hypothesis that \(V_K=P\) implies \(b(K)\le B(P)<\infty\). For a Jones-one knot, Schubert's formula would give

\[
b(K^{\#m})=m(b(K)-1)+1\le B(1)\quad\text{for all }m.
\]

It follows that \(b(K)=1\), hence \(K=U\). This is a full conditional proof independent of categorification. [Schultens' proof of Schubert's theorem](https://www.math.ucdavis.edu/~jcs/pubs/addbri15.pdf).

The unit-fiber restriction is again equivalent to detection, and we have not established the broader hypothesis or its literature status. The physical analogy is a bound on the number of pairs needed to prepare a plat state while allowing arbitrarily long braid evolution; a scalar quantum amplitude supplies no such bound automatically. The mathematical gap is an actual presentation theorem. A falsification could instead come from a known nonunit fixed-Jones family with unbounded meridional generating requirements: surjections of its knot groups onto symmetric groups \(S_m\), with meridians mapped to transpositions and unbounded \(m\), would force \(b\ge m-1\). No such family is asserted here. Keep this as a side hypothesis with a complete endpoint, not another open-ended calculation branch.

### Polynomial cancellation does not establish geometric cancellation

Bigelow constructs embedded arcs in a punctured disk with zero Laurent weighted intersection that cannot be homotoped apart. In minimal position they still intersect without removable empty bigons. This is a counterexample in the Burau model, not a Jones-one knot; it invalidates the general inference from cancellation of abelian winding contributions to a geometric cancellation move. [Bigelow, Theorem 1.4 and Section 3](https://web.math.ucsb.edu/~bigelow/publications/02.pdf).

There is also a precise specialization problem. In the Lawrence–Krammer faithfulness proof, conversion of a fork surface to a closed cycle introduces \((1-q)^2(1+qt)\). The Jones substitution \(t=-q^{-1}\) makes this factor zero, and projects exponent pairs \((a,b)\) to \(a-b\). The original lexicographic sign argument cannot simply be specialized. This is a failure of that attempted argument, not a proof that the specialized representation is unfaithful. [Faithfulness proof, Sections 2.3 and 3](https://www.maths.ed.ac.uk/~v1ranick/papers/bigelow2.pdf), [Jones formula, Theorem 2.8](https://web.math.ucsb.edu/~bigelow/publications/06.pdf).

A valid sufficient certificate survives. In a Bigelow plat presentation, let intersection signs be \(\epsilon_p\) and winding labels \((a_p,b_p)\). If the signs \(\epsilon_p(-1)^{b_p}\) agree separately on both extreme faces of \(a_p-b_p\), then

\[
\operatorname{span}V_K=\max_p(a_p-b_p)-\min_p(a_p-b_p)-1.
\]

The subtraction is the span of the Jones normalization denominator. Projected width at least two therefore proves \(V_K\ne1\). A complete geometric route would require a theorem that actual plat-preserving moves always expose such faces or produce an explicit one-bridge unknot. We have no such normal-form or descent theorem. This is a clearly stated coverage gate, not a new proven approach.

The quantum braid Floer setting has an additional parity obstruction: after \(d=-x^{-1}\), a generator contributes \((-1)^{M+Q}x^{A-Q}\). Jones cancellation is therefore different from ordinary Maslov-parity cancellation. The unknot polynomial \(xd^2-xd+d\) already exhibits the distinction. Nor does differentiation normal to the Jones locus give a free extra invariant: the actual stabilization from \(\sigma_1\) to \(\sigma_1\sigma_2\) changes that derivative by \(-x^{-2}-x^{-1}\). Any derived or nearby-cycle repair needs a separate presentation-invariance theorem and a bridge back to Jones. [Anghel–Juhász, Section 9](https://arxiv.org/html/2601.08805v4).

## 7. Two complete counterexample scaffolds and a realizability restriction

### A genuine representation kernel has a known topological endpoint

An actual nontrivial braid in the full generic ordinary Jones representation kernel would suffice. Its normal closure stays in that kernel; Ito's theorem provides a kernel insertion into an unknot anchor whose closure is a nontrivial hyperbolic knot. Thus this route requires an exact generic matrix identity and an independent braid-nontriviality certificate. An identity at one root of unity, or a kernel of only one representation block, does not supply the premise. The familiar five-strand Burau kernel leaves an additional five-dimensional Jones block uncontrolled. [Ito, Theorem 1 and Corollary 1](https://arxiv.org/pdf/1402.2028).

A concrete sufficient construction would find a Burau-kernel braid \(B\) and an actual braid \(h\) with commuting residual matrices but noncommuting braid elements. Their commutator would be a nontrivial full Jones-kernel element, and the preceding paragraph would finish the counterexample argument. Matrix commutation and braid noncommutation are finite exact certificates. However, an arbitrary matrix in the residual centralizer need not lift to a braid. Earlier short-word tests found no successful pair. This branch should receive another search only after a geometric or algebraic mechanism predicts such a mismatch; the reformulation alone supplies no existence evidence.

### A weaker trace target has four equations and a separate topology gate

Let \(B\in B_5\) be pure, of writhe zero, with generic Burau matrix equal to the identity. Put \(C=\sigma_1\sigma_2\sigma_3\sigma_4\), and let \(M=\rho_5(B)\), \(Z=\rho_5(C)\) in the remaining five-dimensional Temperley–Lieb block. With the conventions in the supplied exact model,

\[
V_{\widehat{B^mC}}(A^{-4})-1=A^{-12}\operatorname{tr}(ZM^m).
\]

Here \(\operatorname{tr}Z=0\). The characteristic recurrence of the invertible five-dimensional matrix shows that **every integer power closure has Jones polynomial one if and only if**

\[
\operatorname{tr}(ZM^j)=0\quad (j=1,2,3,4).
\]

Five consecutive zero moments, including \(j=0\), propagate in both directions by Cayley–Hamilton. Purity makes every closure a knot. A separate verified inequality \(CB^m>_D\Delta^2\) in Dehornoy's braid order would give positive genus and complete a counterexample certificate. Other rigorous knot-nontriviality certificates could replace this one. The moment locus need not be a normal subgroup, so Ito's normal-subgroup existence theorem cannot supply this additional certificate automatically.

The cached Bigelow Burau-kernel seed fails the four equations. More strongly, for each \(i=1,2,3,4\), no integer \(h\) in the entire anchor family \(\sigma_i^{-h}C\sigma_i^h\) makes this seed satisfy all four moments. The generator has two eigenvalues, making each moment a Laurent quadratic in \((-A^{-4})^h\). Their cleared polynomials have greatest common divisor one at an exact finite-field specialization. This excludes every integer \(h\) in these four families, not just a bounded sample. It does not exclude isolated Jones-one power closures, other conjugators, or other seed braids.

### A derived spectral theorem excludes the simple formal matrix construction

Let \(\rho\) be an actual integral Laurent Temperley–Lieb module of a fixed braid group, and \(\beta\in[P_n,P_n]\). Every eigenvalue of \(M=\rho(\beta)\) that lies in \(\mathbb Q(A)\) equals one. If its characteristic polynomial splits completely over this field, then \(M=I\).

To prove this, specialize at \(A=1\), where generators square to the identity. Pure braids evaluate to \(I\), and their first derivatives add under multiplication. Thus a pure commutator has \(M=I+O((A-1)^2)\). A rational eigenvalue and its inverse are integral over the integrally closed ring \(\mathbb Z[A^{\pm1}]\), so the eigenvalue is a unit \(\pm A^k\). Its value at one fixes the sign, and the zero first derivative forces \(k=0\): otherwise \(\det(A^kI-M)\) has nonzero leading term \(k^d(A-1)^d\). Complete splitting therefore makes \(M\) unipotent. Fixed-strand Temperley–Lieb modules admit positive unitary specializations on an open unit-circle arc near one; a unitary unipotent matrix is the identity. Infinitely many such specializations give the Laurent identity \(M=I\).

The generic Burau kernel lies in \([P_n,P_n]\). Its elements are pure by specialization at one; the derivatives of the standard pure generators are the independent graph Laplacians \((e_i-e_j)(e_i-e_j)^T\), so the kernel has zero pure-braid abelianization. Hence the spectral theorem applies to the residual block above. The full proof, sign convention for the positive path model, and two independent audits are in the archive. The fixed-level unitarity framework is that of [Aharonov–Jones–Landau](https://arxiv.org/pdf/quant-ph/0511096).

In particular, formal diagonal models such as \(\operatorname{diag}(A^4,A^{-4},A^8,A^{-8},1)\), which can satisfy all four moments with a weighted cycle anchor, cannot be actual residual matrices of Burau-kernel braids. A surviving construction must either produce a genuine matrix kernel or have at least one eigenvalue outside \(\mathbb Q(A)\); this does not require an irreducible characteristic polynomial. Conversely, \(M=I\) does not prove the braid is trivial—it is precisely the generic-kernel possibility sought in the first scaffold. No such nontrivial braid or moment-family knot has been constructed here.

## 8. Pass 25: testing mechanisms before deeper calculations

### Fixed movie complexity does not bound hidden rank

Set \(K_k=T(3,3k+1)\) and \(R_k=K_k\#\overline{K_k}\), for \(k\ge1\). The bridge-doubling construction gives fusion number at most two: these actual ribbon knots admit movies from the unknot with at most two births and two saddles. Nevertheless,

\[
r(R_k)=(4k+1)^2,
\]

and

\[
V_{R_k}(t)=3+t^2+t^{-2}-t^{3k}-t^{-3k}-t^{3k+2}-t^{-3k-2}.
\]

Thus the number of bands, determinant one (take even \(k\)), Rasmussen invariant zero, and bounded Jones coefficient norm do not bound the actual ribbon complement's rank. The whole Jones polynomials vary, so this does not refute H-rank or E. It excludes a specific proposed mechanism for them. The fusion estimate is [Kanenobu, equation (4.4)](https://ocu-omu.repo.nii.ac.jp/record/2016720/files/111F0000020-09-8.pdf); the torus-knot rank input is [Schütz, Theorem 5.3](https://arxiv.org/html/2501.11547v1).

### Standard twist stability does not control compensating twists

Lobb's Theorem 1.10 supplies an isomorphism range \(h\le 2i-c_- -2\), where \(c_-\) counts negative crossings outside the varying positive twist block. For simultaneous opposite twists with \(i=n\) and \(c_-=2n+c_0\), this range becomes \(h\le-c_0-2\): it does not expand. Consequently this theorem alone does not control multiplicities in the middle degrees. This limitation of the stabilization argument remains correct, but the proposed Watson rank-growth test is superseded by Section 9's finite-resolution bound. No calculation of its middle maps is now needed to establish boundedness. [Lobb, *2-strand twisting and knots with identical quantum knot homologies*](https://msp.org/gt/2014/18-2/gt-v18-n2-p07-p.pdf).

### A bridge-growth test, with a limited role

Luecke–Osoinach give knots \(k_n^m\) with the same oriented \(n\)-surgery and, for fixed \(n\ne0\), bridge numbers tending to infinity with \(m\). Their entire Jones polynomials have not been computed here. If infinitely many in one row shared one Jones polynomial, they would refute the all-fiber bridge-boundedness proposal. They would not by themselves refute unknot detection or the possibility of a bound in a different fiber. [Luecke–Osoinach, Theorem 0.2](https://arxiv.org/abs/1407.1529).

The second Jones derivative cannot distinguish that row: the Casson–Walker surgery formula forces \(\Delta_K''(1)\) to be constant, and \(V_K''(1)=-3\Delta_K''(1)\). A third-order calculation is the first potentially informative Jones-derivative test. It is a bounded falsification experiment, not a direct proof mechanism, and does not currently justify substantial diagram reconstruction. [Ni–Zhang, equation (6.2)](https://www.math.buffalo.edu/~xinzhang/half-integral-surgery%209.pdf), [Ichihara–Wu, Lemmas 2.1–2.2](https://arxiv.org/pdf/1606.03372).

### The structural braid constructions still leave a real missing theorem

A derived restriction excludes nontrivial virtually multitwist braids from the generic Burau kernel. Kernel elements are pure and have zero pairwise linking numbers. Disjoint essential twist curves form a laminar family of puncture sets; their linking vectors are independent, by choosing punctures in distinct child clusters and inducting inward. Therefore a multitwist in this kernel has every exponent zero. Torsion-freeness gives the same conclusion for a braid with a positive multitwist power. This does not exclude reducible braids with pseudo-Anosov components or a multitwist used as an auxiliary braid.

An exact six-strand construction kills three generic Jones blocks but leaves the nine-dimensional block uncontrolled. Put \(P=\Delta_6^2\Delta_5^{-2}\). On the rectangular five-dimensional block it is the scalar \(A^{-6}\). If \(B\) is an embedded five-strand Burau-kernel braid, \([B,gPg^{-1}]\) therefore kills that block, the Burau block, and the scalar block. On the remaining block, however, \(P\) has eigenvalues \(A^2\) and \(A^{-10}\), with multiplicities five and four. Its conjugated splitting must still be preserved by \(B\). Taking \(g\) in the original five-strand subgroup makes the actual braid commutator trivial. Moving the curve leaves an unresolved representation-centralizer problem, with no established simplification of the original difficulty. [Kasahara, branching and rectangular representations](https://arxiv.org/abs/0803.0304).

**Decision.** Retain the one-fiber amplification scaffold and the exact braid-kernel endpoint. Do not treat another isolated fixed-template estimate, a larger braid-word scan, or a low-order annulus calculation as generic progress unless it addresses their missing geometric mechanism. The audits sharpen requirements and rule out shortcuts; they establish neither the required bounded fiber nor a nontrivial generic kernel.

## 9. Pass 26: a family theorem and finite construction certificates

### The Watson rank bound has a complete proof

Use the marked mirrored-three-braid template in Watson's Figure 1. The two input tangles have two arcs, no closed components, and the allowed nonvertical endpoint connectivities; the output is a knot. Let their fixed diagrams contain at most \(N\) crossings in total. Add \(n\) horizontal half-twists to one and \(-n\) to the other. Write \(d=\det K\). Then our derived estimate is

\[
\boxed{\dim_{\mathbb Q}\widetilde{Kh}(K;\mathbb Q)
\le 4^N\max\{d,4\}.}
\]

The estimate is uniform in both the twist integer and the intervening three-braid. It requires no bound on that braid's word length. This is a deduction for this precisely marked construction, with no claim of novelty.

**Proof.** Resolve only the \(N\) fixed input crossings. Each state leaves two planar matchings and \(\ell\le N\) split trivial circles, so there are at most \(2^N\) states and their circle weights sum to at most \(4^N\). If either matching is the infinity matching, the mirrored braid cancels through its rainbow cap by actual crossing slides and Reidemeister-II moves. The remaining closure is the two- or three-component unlink. If both matchings are zero, the remaining opposite-twist family consists of knots: an exact endpoint trace excludes the two braid permutations that could give links. Watson's integral homology-invariance theorem applies to this simple-tangle branch. [Watson, Lemma 3.1](https://personal.math.ubc.ca/~liam/files/identical.pdf).

Its zero-twist base is \(J_\beta\#\overline{J_\beta}\), where \(J_\beta\) is a two-bridge knot. The template's bracket matrix, established in the earlier geometric audit, gives

\[
d=(\det J_\beta)^2\det D(T)\det D(U).
\]

The denominator closures \(D(T),D(U)\) are knots and have positive odd determinants. Thus \((\det J_\beta)^2\le d\). Alternating thinness and the reduced connected-sum formula give reduced rank \((\det J_\beta)^2\) over \(\mathbb F_2\) for the base. Unreduced rank is twice reduced rank over this field. The three elementary branches consequently have unreduced ranks at most \(\max\{2d,8\}\). Iterating the crossing exact-triangle rank inequality gives \(\dim_{\mathbb F_2}Kh(K)\le4^N\max\{2d,8\}\). Divide by two using the characteristic-two splitting, then apply universal coefficients to bound reduced rational rank. This proves the displayed estimate. [Manolescu–Ozsváth, Theorem 1](https://web.stanford.edu/~cm5/quasi.pdf), [Shumakovitch, Corollary 3.2.C](https://arxiv.org/pdf/math/0405474v2). □

Two independently written endpoint verifiers agree in all 54 cap/permutation cases. Those checks certify connectivity; the cap isotopy and rank argument are separate mathematical proofs. We do not assume a link extension of Watson's knot theorem or a characteristic-zero reduced/unreduced splitting. The result gives boundedness, not homology constancy for nonsimple tangles.

**Complete conditional continuation.** If every knot in one nonempty Jones fiber admitted such a presentation with \(N\le N_0\), its determinant would be fixed and the displayed estimate would bound rank on that entire fiber. The connected-sum amplification at the beginning of this report would then prove unknot detection.

**The remaining premise is substantial.** Bounded input complexity would already bound bridge number: only finitely many endcap diagram types occur, while the arbitrarily long middle braid adds no local maxima. Thus this presentation premise also gives the bridge-number proof directly. The rank estimate supplies a genuine family theorem, but does not make the missing global premise easier. Existence of some Watson presentation is insufficient; the required uniform complexity bound is unproved. Stop testing fixed Watson orbits for unbounded rank.

### Partial braid kernels cannot reach the endpoint by the inspected iteration

Index generic Temperley–Lieb blocks by \([n-j,j]\), and let \(K(n,r)\) be the common kernel for \(0\le j\le r\). The one-overlapping-strand construction has parameter rule

\[
(n,r)\oplus(m,s)=(n+m-1,r+s).
\]

Consequently \(r/(n-1)\) becomes a weighted average of the input ratios. The certified seeds \((5,1),(9,2),(11,2)\) have ratios at most \(1/4\), whereas full block coverage requires at least \(1/2\). Iteration and padding therefore cannot **certify** a full kernel from these seeds. This does not rule out extra accidental cancellations in a particular braid. [Piwocki–Traczyk, Theorems 1–2 and Section 4](https://doi.org/10.1016/j.topol.2008.07.016).

The complete conditional route remains valid: at one fixed strand count, nontrivial zero-writhe kernels for **every** block have nontrivial common intersection by the normal-subgroup intersection theorem. Ito then gives hyperbolic Jones-one knots. The known constructions leave intermediate blocks uncontrolled. Generic algebra ideals are idempotent, so repeated commutators have no automatic nilpotent-filtration improvement. Larger examples using the same iteration do not close this gap. [Ito, Theorem 1 and normal-subgroup discussion](https://arxiv.org/pdf/1402.2028).

### A finite satellite certificate replaces an infinite companion test

Let \(P\) be a winding-zero knot pattern with a certified meridional disk meeting it at most \(2d\) times, and use zero-framed companions. Let \(T\) be a trefoil. Then the full annular bracket of \(P\) is scalar **if and only if** these \(d+1\) ordinary Jones polynomials are equal:

\[
V_{P(U)}=V_{P(T)}=V_{P(T\#T)}=\cdots=V_{P(T^{\#d})}.
\]

Here scalar means independent of the companion after satellite evaluation. The implication back to scalarity uses the wrapping bound, not merely equality of a few unspecified closures. In particular, wrapping at most four requires three full-polynomial comparisons.

For the proof, expand the annular class in the even Jones–Wenzl basis. After normalization its evaluations are \(\sum_{i=0}^d c_iH_{2i+1}(T)^r\), with \(H_N(U)=1\). For the chirality \(V_T=q^{-1}+q^{-3}-q^{-4}\), the torus-knot formula gives \(\operatorname{val}_q H_{2i+1}(T)=-6i^2-5i\). These eigenvalues are distinct, with the zeroth equal to one. Subtract the \(r=0\) equation and use the Vandermonde determinant to force every \(c_i\), \(i>0\), to vanish. The same distinct valuations show that otherwise the minimum Jones degree along these companion powers is eventually strictly decreasing. No infinite constant subsequence is missed. [Morton's torus-knot formula](https://www.liverpool.ac.uk/~su14/papers/colouredjones.pdf).

An actual essential scalar pattern would falsify the broad all-fiber bridge-bound proposal by Schubert's satellite inequality. If it additionally had \(V_{P(U)}=1\), its satellites on nontrivial companions would give counterexamples to unknot detection. No such essential pattern has been constructed here. The certificate is exact; its geometric realization remains the missing premise. Signed serial lasso chains and the inspected mutation constructions from local seeds do not provide that realization; the detailed exclusions are in the accompanying notes.

**Research decision.** Retain three complete endpoints: one bounded nonempty fiber proves detection; one nontrivial full generic braid kernel disproves it; one essential scalar pattern with unit closure also disproves it. Work on their missing geometric premises only when there is a mechanism to test. The present family bound and finite tests do not establish any of those premises, and should not be counted as independent evidence that the conjecture is near resolution.

## 10. Pass 27: an actual annular realization and the shared remaining requirement

### The Bing construction has one exact obstruction

Let \(B(C)\) be the untwisted Bing double of a zero-framed knot \(C\), and regard one component as a pattern \(P_C\) in the complement of the other. Both components are unknots and have linking number zero. In particular \(P_C(U)=U\) as an actual knot. If \(C\ne U\), the pattern is essential: its link exterior is the Borromean-rings exterior glued to the exterior of \(C\) along an incompressible torus. The resulting exterior is irreducible, so the link is nonsplit. This supplies the topology independently of any Jones-detection claim. [Cimasoni, Section 1](https://www.unige.ch/~cimasoni/Bing.pdf).

Write \(\delta=-A^2-A^{-2}\), \(q=A^{-4}\), and let \(z\) be the annular core, with the empty skein equal to one. From Suzuki's Bing-doubling coefficients we derive the full annular identity

\[
\boxed{[P_C]=\delta H_3(C)+\frac{1-H_3(C)}{\delta}z^2.}
\]

Here \(H_3\) is the reduced, zero-framed, dimension-three colored Jones polynomial, normalized to one on the unknot. The equality is over \(\mathbb Q(A)\); there is no assertion about division at roots of unity. A zero-framed local unknot has bracket \(\delta\).

For completeness, Suzuki's reduced-color coefficients vanish off the diagonal. With the pattern component fundamental-colored, all nonconstant probes vanish except the first. Its value simplifies to \(-\{1\}[3](H_3(C)-1)\). Habiro's dual basis for the Hopf pairing then reconstructs the full annular polynomial, giving the displayed formula. The extra \(\{1\}\) from expanding the fundamental color is necessary. Thus this is not an inference from agreement of one or two unbounded-degree closures. Two independent audits checked the normalization and reconstruction. [Suzuki, Theorem 3.2 and Lemma 6.1](https://arxiv.org/pdf/1305.0602).

It follows that \(P_C\) is scalar **exactly when \(H_3(C)=1\)**, and its scalar value is then \(\delta\). The geometric pattern is supplied for every \(C\); the missing input is an actual nontrivial knot with that whole colored polynomial. No numerical wrapping number is asserted or inferred from the annular degree.

### Two companions cannot cancel each other's nonzero responses

For any zero-framed companion \(J\), evaluate \(z^2\) as \(1+(\delta^2-1)H_3(J)\) and divide the result by \(\delta\) to normalize the output knot. The exact consequence is

\[
\boxed{V_{P_C(J)}-1
=-\frac{\delta^2-1}{\delta^2}
\bigl(H_3(C)-1\bigr)\bigl(H_3(J)-1\bigr).}
\]

The rational function prefactor is nonzero. Therefore this entire actual two-input family has Jones polynomial one if and only if at least one input has \(H_3=1\). When both input knots are nontrivial, the output is nontrivial: the satellite gluing retains an incompressible companion torus. This closes the conditional construction with no additional realization or knot-nontriviality premise.

The strategic consequence is restrictive. Choosing increasingly elaborate inputs with nonzero color-three defects cannot make those defects cancel. A nontrivial \(H_3\)-unit knot would suffice, but that is the same unresolved condition already exposed by the Whitehead formula in the earlier cabling report. The Bing calculation establishes a full annular realization and excludes a cancellation mechanism; it is not a second independent reason to expect a solution. It also cannot supply a nonunit scalar pattern to falsify the broad fiber-bound proposal more cheaply.

### Point-pushing and periodic symmetry do not remove the other gaps

There are two distinct braid forgetful constructions. The free subgroup obtained by deleting a strand from the pure disk braid group has full projective Zariski image in every nontrivial generic Temperley–Lieb block. It is normal in the pure braid group and contains a squared generator with distinct eigenvalues \(A^2,A^{-6}\); Kuperberg's density theorem and simplicity of \(\mathrm{PGL}\) give the conclusion. Its commutator subgroup remains dense. [Kuperberg, Theorem 1.1](https://msp.org/gt/2011/15-1/gt-v15-n1-p02-s.pdf).

Forgetting the capped-boundary puncture on the sphere is different. On a nontrivial block with through-label \(0<h<n\), the point-push \(\Delta_n^2\Delta_{n-1}^{-2}\) has eigenvalues \(A^{2h-2}\) and \(A^{-2h-6}\), so the same normality argument gives full projective image. Among nontrivial blocks, only the rectangular \(h=0\) blocks lose this image, as in the earlier partial construction; the one-dimensional \(h=n\) block is excluded. Dense image does not imply faithfulness; this result excludes the proposed automatic collapse to a smaller matrix action, not a particular exact kernel relation. [Kasahara, Propositions 2.4 and 2.6](https://arxiv.org/pdf/0803.0304).

The natural periodic connected-sum construction also supplies no new rank restriction. For \(p=2^r\), the knot \(K^{\#p}\) has a periodic presentation whose annular quotient is a local copy of \(K\) tied into the core. If \(P(q)\) records reduced mod-two homology ranks by quantum grading, all the resulting graded Smith inequalities reduce to

\[
(q+q^{-1})P(q)^p\ \ge\ (q+q^{-1})P(q^p)
\]

coefficientwise. These inequalities hold automatically for every polynomial with nonnegative integer coefficients. Thus retaining all quantum gradings in this particular symmetry does not turn Euler characteristic one into rank one. This does not rule out additional constraints from different symmetries. [Stoffregen–Zhang, Theorem 1.1 and equation (1.6)](https://arxiv.org/pdf/1810.04769).

**Decision.** Do not extend the two-input Bing search without a way to obtain a nontrivial \(H_3\)-unit input; do not treat point-pushing as an automatic source of a missing generic kernel; and do not add periodic connected-sum inequalities to the rank scaffold as independent evidence. The full endpoints remain intact, but none of their central unproved premises has been established.

## 11. Pass 28: finite-order geometry, exact polynomiality, and a cover endpoint

### An actual finite-order obstruction to color promotion

For every integer \(N\ge5\), there exists an actual knot \(R_N\) satisfying

\[
V_{R_N}(e^h)=1+O(h^{N+1}),\qquad
H_3(R_N;e^h)=1+320h^5+O(h^6).
\]

Every \(V_{R_N}\) is nevertheless nonconstant. The construction uses explicit chirality choices \(K=5_1\), \(L=10_{132}\) with equal whole ordinary Jones polynomials and different colored polynomials. Habiro's group of knots modulo \(C_{N+1}\) supplies an actual inverse representative \(L_N\), with \(L\#L_N\) indistinguishable from the unknot by finite-type invariants through degree \(N\). Set \(R_N=K\#L_N\). Multiplicativity gives the displayed expansions, while the nonunit factor \(V_K\mid V_{R_N}\) proves \(V_{R_N}\ne1\). This is an existence construction using a geometric theorem; explicit diagrams of the inverse representatives have not been generated. [Habiro, Theorems 5.4 and 6.18](https://arxiv.org/pdf/math/0001185).

The initial polynomial data were recomputed from explicit braid words. The all-color leading difference follows from the exact cyclotomic coefficient
\(\Delta a_2=q^{-15}(q^2-1)(q^3+1)(q^5+1)\):

\[
H_m(R_N;e^h)=1+8(m^2-1)(m^2-4)h^5+O(h^6)
\]

for each fixed \(m\). Terms with cyclotomic index at least three start in degree six. The coefficient \(320\) is therefore a normalization-dependent exact value in \(q=e^h\), not an interpolation across a few colors. [Habiro's integral expansion](https://arxiv.org/abs/math/0211044).

There are two useful quantitative consequences. If a nonzero Laurent polynomial with \(s\) terms vanishes at \(1\) to order \(N+1\), its first \(s\) exponential moments and the Vandermonde determinant give \(s\ge N+2\). Thus \(V_{R_N}\) has at least \(N+1\) nonzero terms, and reduced rational Khovanov rank is at least \(N+1\). For fixed \(N\), connected-sum powers of \(R_N\) preserve the same ordinary Taylor expansion while their bridge numbers and homology ranks grow without bound. Adding any anchor \(J\) proves the same statement for every realizable finite Taylor expansion. **No fixed finite ordinary-Jones Taylor jet can replace the whole-polynomial premise in our boundedness scaffold.**

### Why the completed limit is still not a counterexample

The normalized Kontsevich ratio \(G=Z(K)Z(L)^{-1}\) is group-like, fundamental-invisible, and realized by actual knots to every finite order. But this particular \(G\) cannot be the invariant of one finite knot: its color-three value is a quotient of unreduced Laurent polynomials with exponent spans \(34\) and \(48\). A Laurent quotient would have span \(-14\), impossible. Full polynomiality detects an obstruction missed by every finite truncation.

The diagram coproduct used for group-likeness must also be distinguished from the enveloping-algebra coproduct used for cabling. A primitive chord maps to a quadratic Casimir whose coproduct has additional cross terms. Centrality provides a natural action on representations; it does not make that action monoidal. Assuming tensor compatibility on the fundamental representation's first tensor square would already assume the missing implication \(H_2=1\Rightarrow H_3=1\).

The earlier formal cyclotomic example with \(a_2=q-1\) passes all-color Laurent polynomiality, but has no established group-like lift or finite-order actual realizations. These are separate examples; their favorable properties cannot be combined. A full quantum/classical proof still needs universal color promotion and a bridge such as AJ. Under AJ, Dunfield–Garoufalidis supply the all-colored unknot-detection endpoint. Neither missing assumption is proved here. [Theorem 1.1 and Corollary 1.4](https://msp.org/agt/2004/4-2/agt-v4-n2-p21-s.pdf).

### An unmarked geometric endpoint

Suppose the double branched covers \(\Sigma_2(L)\) of all knots in one nonempty whole Jones fiber are Dehn fillings of finitely many compact three-manifolds with torus boundary. Filling quotients fundamental groups, so their minimum generator numbers have a uniform bound \(B\). For a hypothetical \(V_K=1\), the covers of \(J\#K^{\#r}\) have group ranks

\[
d\pi_1\Sigma_2(J)+r\,d\pi_1\Sigma_2(K)
\]

by connected-sum decomposition and Grushko's theorem. Boundedness forces \(\pi_1\Sigma_2(K)=1\); Poincaré and Smith then give \(K=U\). This closes the full conditional proof without controlling deck involutions or equivariant tangle presentations. The finite-parent requirement is weaker than finite marked tangle templates; no equivalence with bridge boundedness is claimed.

No theorem deriving those finite parents from the Jones polynomial was found. Standard cover data cannot substitute for it: the actual ribbon knots \((T(3,5)\#\overline{T(3,5)})^{\#r}\) have cover-group rank \(4r\), despite determinant one, signature zero, and covers with zero Casson–Walker invariant, correction term and simplicial volume, and \(\widehat{HF}\) rank one. Their whole Jones polynomials vary. This excludes those quantitative intermediaries, not the whole-fiber hypothesis. [Milnor's branched-cover description](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnbries.pdf), [Ozsváth–Szabó, Proposition 2.3](https://arxiv.org/pdf/math/0303017).

### A structural restriction on the braid certificate

In the residual five-dimensional \(B_5\) block, the full twist about any three-puncture curve \(a\) has
\(\rho(D_a)=A^{-6}I+(A^6-A^{-6})P_a\), with \(P_a\) a rank-one idempotent. At \(A=1\), the trace overlap of two such projectors is \(1\) for the same enclosed puncture subset and \(1/9\) otherwise. Consequently commuting images of nonzero twist powers require identical generic projectors and the same enclosed subset. This excludes all different-subset pairs, regardless of winding. A distinct same-subset pair with equal generic projectors would give an actual residual kernel via \(D_aD_b^{-1}\), after which Long/Ito finish the counterexample construction. No such equality was obtained. The fixed matrix identities were checked exactly; the all-curve conclusion has a separate proof. [Kasahara's branching and specialization](https://arxiv.org/pdf/0803.0304).

**Decision.** A useful next mechanism must control whole-polynomial realizability, extract genuine finite-parent geometry, or produce an exact same-subset projector equality. Increasing finite Taylor order, replacing cover groups by their standard numerical invariants, or testing different-subset twist pairs cannot close these gaps.

## 12. Pass 29: testing whole-polynomial mechanisms against the full scaffold

### One fixed ordinary polynomial permits unbounded color-three span

An actual Watson family gives a counterexample to the proposed intermediate bound
\(\operatorname{span}H_3(K)\le B(V_K)\). This is a deduction and reproducible calculation, with no novelty claim. It is not a Jones-one counterexample.

Use the mirrored six-strand presentation specified in the accompanying certificate, with three-braid word \(\alpha=(1,1,1,-2,1)\) and opposite end tangles \((2m,-2m)\). Call its closure \(K_m\). The twists are even, so endpoint connectivity is independent of \(m\); tracing the zero-twist closure gives one component. The marked construction is Watson's, and the all-integer Jones equality follows from his opposite-twist theorem, not from extrapolating a finite list. In the ordinary variable \(t\), the common polynomial is

\[
P=-t^5+2t^4-4t^3+6t^2-7t+9-7t^{-1}+6t^{-2}-4t^{-3}+2t^{-4}-t^{-5}.
\]

The exact braid and the ordinary-polynomial invariance appear in [Watson, Section 8 and Lemma 5.2](https://personal.math.ubc.ca/~liam/files/preprint.pdf). The simple-tangle hypothesis also holds, so Watson's homology theorem keeps ordinary Khovanov homology constant along this family. This family therefore does **not** refute our ordinary homology-rank or quantum-spread hypotheses. [Watson, Lemma 3.1](https://personal.math.ubc.ca/~liam/files/identical.pdf).

Here is the all-parameter argument for the different colored behavior. Color three has skein label two. Its tensor square has channels with labels \(0,2,4\), and the full-twist eigenvalues are \(A^{-16},A^{-8},A^8\). Opposite twist boxes, with \(t=A^{-4}\), consequently give

\[
H_3(K_m;t)=\sum_{k\in\{0,\pm2,\pm4,\pm6\}}c_k(t)t^{km},
\qquad c_k(t)\in\mathbb Q(t).
\]

The local fusion and twist identities are independent of any global alternating-diagram assumption. [Elhamdadi–Hajij–Saito, equations (2.7) and (2.9)](https://arxiv.org/pdf/1605.04972). The diagram writhe is zero for every \(m\), so there is no missing parameter-dependent framing factor. Exact zero-framed two-parallel calculations recover
\(H_3=(\delta V_{K^{(2)}}-1)/(\delta^2-1)\), with \(\delta=-t^{1/2}-t^{-1/2}\). They show \(H_3(K_0)\ne H_3(K_1)\). A single surviving frequency would have the form \(c(t)t^{km}\); the identities \(H_3(1)=1\), \(H_3'(1)=0\) for zero-framed knots force \(k=0\), contradicting that inequality. Thus at least two distinct frequencies survive. Clearing one fixed denominator makes their extreme exponents separate linearly as \(m\to\infty\). Dividing by that fixed denominator subtracts a constant span. Therefore

\[
\boxed{V_{K_m}=P\text{ for all }m,\qquad
\operatorname{span}_t H_3(K_m)\longrightarrow\infty.}
\]

As an independent arithmetic check, seven exact evaluations at \(t=4\) determine the seven possible fusion coefficients; the coefficients at frequencies \(-4,0,4\) are nonzero. An eighth sample satisfies the resulting recurrence. The first eight colored spans are \(30,28,37,45,53,61,69,77\). These samples verify normalization and the recurrence; the fusion decomposition supplies the infinite-family proof. The evidence distinguishes diagram regeneration from the portable arithmetic checks.

### Positivity needs a theorem about closing the surface

The quantum-trace positivity theorem applies to essential simple curves on punctured surfaces. It does not make the map obtained by embedding that surface in \(S^3\) positive or injective. On a punctured Heegaard torus, a meridian \(\mu\) is essential on the surface but becomes a zero-framed unknot after closure. The nonzero surface skein
\(X=\mu+(A^2+A^{-2})1\) has positive quantum trace and closes to zero. Even actual zero-framed unknots of slopes \((1,2m)\) have unbounded positive trace mass in one fixed triangulation. Thus a presentation-wise positive-state bound from the closed Jones polynomial is false. A theorem choosing and simplifying presentations is still conceivable, but positivity alone supplies no such theorem. [Cho–Kim–Kim–Oh, Theorem 1.3](https://arxiv.org/pdf/1710.06217), [Hikami, equation (3.4)](https://sigma-journal.com/2019/003/sigma19-003.pdf).

The braid route has a related limitation: universal surface skeins distinguish curves, but the residual five-dimensional representation imposes an exact quadratic relation on each curve operator. Its kernel even contains nonzero reflected squares. Universal positivity therefore does not prove injectivity of the represented curve projectors. A separate all-integer argument excludes equal projectors obtained by even powers of one or two disjoint cross-partition half twists. It leaves overlapping operations unresolved and supplies no kernel element.

**Research decision.** Keep breadth at the level of global mechanisms: geometric presentation control, cancellation in actual knot complexes, or an actual generic braid kernel. The conditional endpoints are already complete. Do not invest in further local twist estimates, higher-colored degree bounds, or surface positivity without an explicit mechanism that reaches a missing global premise. The latest exclusions improve our choice of research targets; they are not evidence that any surviving premise is close to proof.

## 13. Pass 30: projective diagrams, an Ising identity, and a complete geometric scaffold

**Pass-31 update.** The geometric implications in this section remain valid, but the proposed Jones-to-complexity premise fails in its span and all-fiber forms. Section 14 proves that this complexity is ordinary crossing number on classical local knots. The following records the earlier conditional scaffold and its scope; its final research recommendation is superseded.

### The full target, before the local arguments

Boyle and Spyropoulos's September 2026 preprint defines a local crossing number \(\beta_\varepsilon\) for links in \(\mathbb{RP}^3\). For a classical knot placed in a ball, their Conjecture 1.1(2) would give

\[
\beta_{\Re}(K)\le \operatorname{span}V_K.
\]

They explain why this implies unknot detection; they do not prove the general inequality. Their graph definition is \(\beta(G)=e(G)-\alpha(G)\), where \(\alpha\) is the minimum number of edges deleted to leave a graph contained in a disk in \(\mathbb{RP}^2\). The knot invariant minimizes the appropriate checkerboard-graph value over projective diagrams. [Boyle–Spyropoulos, Definition 1.6 and Conjecture 1.1](https://arxiv.org/html/2609.40122v1).

Our additional deduction is a geometric endpoint valid for every finite bound, not just complexity zero:

\[
\boxed{\beta_{\Re}(K)\le b\quad\Longrightarrow\quad
b_{\mathrm{bridge}}(K)\le B(b)<\infty.}
\]

This deduction uses actual isotopies of diagrams, as detailed below. It gives the following complete conditional solution.

**Projective compression hypothesis.** There exist a realizable ordinary Jones polynomial \(P\) and a finite constant \(C\) such that every classical knot with \(V_K=P\) admits a projective diagram with the relevant checkerboard graph satisfying \(\beta\le C\).

**Conditional proof of detection.** Choose an anchor \(J\) with \(V_J=P\). If \(V_K=1\), every \(J\#K^{\#m}\) has polynomial \(P\), hence bridge number at most \(B(C)\). But Schubert's formula gives

\[
b_{\mathrm{bridge}}(J\#K^{\#m})=
b_{\mathrm{bridge}}(J)+m\bigl(b_{\mathrm{bridge}}(K)-1\bigr).
\]

Letting \(m\) increase forces \(b_{\mathrm{bridge}}(K)=1\), hence \(K=U\). All knots in the fiber, including composite knots, are essential to this argument. [Schultens's proof of the bridge formula](https://arxiv.org/abs/math/0111032). □

The source's span conjecture is sufficient to provide this hypothesis for every polynomial. The proof above needs only one. We have proved neither version of the Jones-to-complexity premise. Indeed, the existence of some such fiber bound is equivalent to detection: the converse follows by choosing \(P=1\) once detection is assumed. The new value of the formulation is its explicit geometric optimization and the theorem completing its endpoint, not evidence that the remaining premise is easier.

### The exact statistical-mechanics connection

Here and below these are our deductions from the graph definition. Give each vertex of an embedded graph \(G\subset\mathbb{RP}^2\) a chosen lift to the orientation cover \(S^2\). An edge \(uv\) then has a holonomy sign \(\eta_{uv}\in\{+1,-1\}\), according to whether its lift connects the chosen sheets. These topological signs are independent of crossing over/under signs.

A subgraph lies in a disk precisely when every cycle has trivial holonomy. For a connected subgraph, its regular neighborhood is then planar, and the complementary side containing the crosscap identifies an encompassing disk. Disjoint local components can be included in one disk by joining outer disk neighborhoods along a tree. Equivalently, the subgraph is balanced: vertex signs can make all its edges positive. Extending these signs to all vertices gives

\[
\boxed{\beta(G)=\max_{s_v=\pm1}
\#\{uv:\eta_{uv}s_us_v=+1\}
=\frac{e(G)+\max_s\sum_{uv}\eta_{uv}s_us_v}{2}.}
\]

Thus \(\alpha\) counts unsatisfied bonds in a particular geometric Ising model. This is an exact identity, not a physical analogy or an assumption about arbitrary spin systems.

There is an additional algorithmic simplification when \(G\) is connected and cellular. Its negative edges, under any vertex switching, are dual to a representative of the unique nonzero class in \(H_1(\mathbb{RP}^2;\mathbb F_2)\). A minimum representative is a single noncontractible simple dual cycle: decompose any even-degree representative into cycles and retain one with nonzero class. Hence

\[
\alpha(G)=\min_v d_{\widetilde{G^*}}(v^+,v^-),
\]

where \(\widetilde{G^*}\) is the orientation double cover of the geometric dual graph. One inequality lifts a noncontractible cycle to a path between opposite lifts. For the reverse inequality, project any such path, cancel repeated edges modulo two, and extract a noncontractible cycle. Loops, bridges, and repeated facial incidences cause no exception. If \(G\) itself is local, simply use \(\alpha=0\); no cellular-dual assertion is needed in that case.

This computes complexity for one given diagram. Minimizing across all diagrams of a knot is a separate problem. Neither shortest paths nor the Ising identity relates the resulting minimum to Jones-polynomial cancellations.

### Why bounded complexity really bounds bridge number

Let \(G\) be a connected realized checkerboard graph with \(\beta(G)\le b\). If it is local, it has at most \(b\) edges, and already belongs to a finite list of bounded diagrams. Otherwise proceed as follows.

1. A spanning tree is balanced, so \(v(G)\le b+1\). Every nonloop edge is satisfied with probability \(1/2\) under independent random spins. A local loop is always satisfied; a projective loop is never satisfied. The displayed maximum therefore bounds the total number of edges other than projective loops by \(2b\).

2. Projective loops all have the same base vertex. Otherwise two such loops would be disjoint essential curves in \(\mathbb{RP}^2\), contradicting their mod-two intersection number one. At that vertex every pair of projective loops has interleaving endpoints. Their cyclic subword is consequently \(1,\ldots,n,1,\ldots,n\). The at most \(4b\) other edge ends split these loops into at most \(4b+1\) blocks consecutive in both halves.

3. Remove a small disk around the vertex. The projective loops become parallel essential proper arcs in a Möbius band. Successive arcs in a block cobound a rectangle whose vertex-boundary intervals contain no other edge ends. Its interior contains no graph: an interior component could not attach without crossing the boundary, contradicting connectedness. In the medial link diagram these rectangles are empty bigons. Each block is therefore an actual two-strand braid in a disk, with arbitrary crossing signs reducing to one integer twist by Reidemeister II moves. With no other edge ends, open the cyclic bigon chain at one adjacency and use a fixed exterior closure.

4. Replace each block by a marked twist placeholder. The resulting graph has at most \(2b+(4b+1)=6b+1\) edges. There are finitely many such embedded marked graphs in \(\mathbb{RP}^2\): their ribbon cyclic orders, edge twists, and complementary-surface data are finite. A connected nonlocal graph is cellular; the local case was handled separately. Thus there are finitely many actual projective twist templates, not merely graphs related by smoothing.

5. Lift these templates through the unbranched cover \(S^3\to\mathbb{RP}^3\). Every disk twist box thickens to a ball and has two disjoint ball lifts. A fixed finite set of two-strand braid boxes admits a height presentation with a bounded number of maxima, independent of the twist exponents: arrange each braid box monotonically and retain the fixed exterior arcs. Take the maximum over the finite template list. A local classical knot lifts to two split copies of itself. Restrict the bounded-maxima presentation to one component to obtain the required \(B(b)\).

This proves the stated implication. It supplies no crossing-number bound: integer twist exponents remain arbitrary. Its use of isotopies is essential; arbitrary graph deletion or contraction would change the represented knot. Separate internal audits checked the signed-graph formula, the dual-systole formula, and the disk-twist geometry. These are research proofs awaiting external review, not a publication or novelty claim.

### A source-proof issue that does not obstruct this scaffold

The induction in the source's proof of Theorem 5.3 asserts that some edge deletion reduces \(\beta\) by one. An essential projective triangle disproves this assertion: it has \(e=3,\alpha=1,\beta=2\), while deleting any edge leaves a two-edge local path with \(\beta=2\). This is a gap in that induction step, not a disproof of the stated classifications or the conjectural inequality. [Source proof](https://arxiv.org/html/2609.40122v1#S5.SS2).

A valid graph reduction uses contraction. In an optimal spin assignment the satisfied spanning subgraph is connected; otherwise flipping a component satisfies every edge crossing its cut and increases the objective. Contract a satisfied nonloop edge after making it positive by switching. Assignments on the contraction correspond exactly to assignments satisfying that edge, including a global optimum, so \(\beta(G/e)=\beta(G)-1\). Once only one vertex remains, delete local loops. This reaches a projective-loop bouquet after exactly \(\beta\) reductions. These reductions are checkerboard smoothings and do not preserve the knot. They repair the graph descent statement, not the entire published induction, and are not used in our isotopy-based bridge proof.

### What the parallel branches changed strategically

The residual five-dimensional braid route has a useful equivalence: a nontrivial generic kernel exists if and only if two distinct three-puncture curves have identical rank-one projectors. The first curve can be fixed in advance, and the second can be required to enclose the same puncture subset. A kernel braid is pure, cannot be central, and therefore moves some such curve; equivariance gives the collision. Conversely equal projectors give a nontrivial twist-difference kernel. The supporting argument is in the evidence archive. Thus the collision target is exactly the existing faithfulness problem, not a weaker intermediate conjecture. No kernel was constructed.

The bounded homology and ribbon searches produced no certified counterexample to the remaining whole-fiber or ribbon hypotheses. In particular, a published Jones-invisible link tangle retains a closed component, and applying a wrapping-two satellite with a nonzero color-three coefficient cannot erase the color-three difference in the pass-29 family. These are reasons to stop those immediate constructions, not nonexistence theorems.

**Research decision.** Prioritize a global diagram-simplification or noncancellation mechanism connecting the whole Jones polynomial to minimized projective complexity. The downstream proof is now explicit. Do not spend further time on fixed-diagram Ising optimization as if it supplied that missing implication; do not assume graph smoothings preserve knots; and do not start another local braid scan without a mechanism producing an exact generic kernel. The geometric scaffold warrants investigation, but no evidence currently justifies predicting a near-term solution.

## 14. Pass 31: an exact crossing identity refutes the proposed projective-span bound

**Result derived here.** For every classical knot \(K\), embedded in a ball in \(\mathbb{RP}^3\),

\[
\boxed{\beta_{\Re}(K)=c_{S^3}(K).}
\]

More generally, for a nullhomologous projective knot with lifted component \(\widetilde K\subset S^3\),
\(\beta_{\Re}(K)\ge c_{S^3}(\widetilde K)\). This statement concerns the integral-exponent sector specifically. It makes no corresponding assertion about \(\beta_{\Im}\) or their minimum, and no assertion for arbitrary multicomponent links.

The definitions and sector conventions are from [Boyle–Spyropoulos, Definition 1.6, Table 2, and Proposition 4.4](https://arxiv.org/html/2609.40122v1). The argument below is our research deduction, independently audited within this investigation. It has not been externally reviewed, and no novelty claim is made.

### Proof: the double cover identifies a large local subgraph

Take any projective diagram \(D\) of the nullhomologous knot. First assume its shadow is nonlocal. Its lift is a spherical diagram of two knot components \(K_0,K_1\), exchanged by the antipodal deck map \(\tau\). This is an ordinary link diagram in \(S^3\): the pulled-back interval bundle is \(S^2\times I\), with two balls capping its ends.

Call a crossing of \(D\) *self* when its two lifts are self-crossings of \(K_0\) and \(K_1\), respectively. Otherwise both lifts are crossings between the components; call it *mixed*. If \(s_D\) counts self-crossings, deleting \(K_1\) from the lifted diagram leaves a diagram of \(K_0\) with exactly \(s_D\) crossings. Thus \(s_D\ge c(K_0)\).

Orient the knot and its lifts. Let \(I\) be an integer winding-index function of the projected curve \(K_0\) on the oriented sphere. The deck map reverses the orientation of the sphere, so \(-I\circ\tau\) is an index function of the compatibly oriented curve \(K_1\). Consequently

\[
J=I-I\circ\tau
\]

is an index function of the full lifted diagram, with \(J\circ\tau=-J\). Its parity descends to a checkerboard coloring downstairs. Shade the regions where \(J\) is odd, and call their Tait graph \(G\).

Put \(f=I\bmod2\). On a shaded region, \(f+f\circ\tau=1\). Therefore \(f\) selects exactly one lift of each vertex of \(G\). Across opposite shaded sectors at a self-crossing, \(f\) has the same value: a small path crosses two arcs of \(K_0\), or none. At a mixed crossing it changes value, because the path crosses exactly one such arc.

With these choices of vertex lifts, all self-edges of \(G\) have positive holonomy, while mixed edges have negative holonomy. The self-edge subgraph is therefore balanced and lies in a disk in \(\mathbb{RP}^2\), by the signed-graph lemma in Section 13. Deleting the mixed edges makes \(G\) local. Hence

\[
\beta(G)=c(D)-\alpha(G)\ge s_D\ge c(K_0).
\]

The crucial remaining point is to identify this particular shading with the \(\Re\) sector. A lower bound for an unspecified shading would not suffice.

### Proof: integer winding fixes the sector label

Perform oriented Seifert smoothing at all crossings, equivariantly in the sphere. In a crossing disk, the opposite sectors joined by this smoothing have equal integer indices; the sectors whose indices differ by two are not joined. Thus \(J\) extends over the smoothing, agrees outside those disks, and remains antisymmetric under \(\tau\).

All Seifert circles downstairs are contractible. Indeed, two essential simple circles cannot be disjoint in \(\mathbb{RP}^2\), while exactly one essential circle would contradict the zero mod-two homology class of the original knot. The complement of the Seifert circles therefore has exactly one nonlocal region. Its lift is connected and \(\tau\)-invariant. The continued index is constant there, and antisymmetry forces that constant to be zero.

It follows that the odd-colored side \(N\) of this state is local: it contains no crosscap. This is the regular neighborhood of the state subgraph of \(G\), not an assertion that arbitrary checkerboard smoothings preserve the knot.

Here is the grading calculation that converts that geometric fact into the required sector label. Write \(v=|V(G)|\), \(c=c(D)\), let \(\epsilon_e\in\{\pm1\}\) be the Tait signs, and let \(w\) be the oriented writhe. Every spanning-tree monomial has normalized \(A\)-exponent residue

\[
r_G\equiv 2(v-1)-\sum_e\epsilon_e-3w\pmod4.
\]

To see this directly, internal edges contribute exponent \(\epsilon_e\) modulo four, external edges contribute \(-\epsilon_e\), and a spanning tree has \(v-1\) edges. The writhe normalization contributes \(-3w\). Thus \(r_G=0\) identifies integral powers of \(t=A^{-4}\), while \(r_G=2\) identifies half-integral powers.

Let \(m\) be the number of crossings whose Tait sign differs from their oriented crossing sign. Then

\[
\frac{r_G}{2}\equiv v-1+m\pmod2.
\]

The black Seifert-state neighborhood \(N\) includes exactly the \(c-m\) equal-sign edges, so \(\chi(N)=v-c+m\). If \(q\) is its number of boundary circles, smoothing toggles component parity at each crossing, giving \(q\equiv c+1\pmod2\). Consequently

\[
\frac{r_G}{2}\equiv\chi(N)+q\pmod2.
\]

For a subsurface of \(\mathbb{RP}^2\), this last parity is zero if the subsurface is local and one if it contains the crosscap. Our \(N\) is local, so \(r_G=0\): the canonical odd shading is precisely \(G_{\Re}\). The sector identification does not depend on over/under choices; a crossing switch changes the displayed residue by a multiple of four.

We have therefore proved \(\beta_{\Re}(D)\ge c(K_0)\) for every nonlocal diagram. For a diagram contained in a disk, its canonical odd graph is local and has \(\alpha=0\), agreeing with the paper's ordinary planar Tait-graph convention for local diagrams. This gives the same lower bound directly; it requires no assertion that the exterior Möbius face is a disk. For a classical local knot, \(K_0\) is a copy of \(K\). Finally, a crossing-minimal classical diagram in a disk attains \(\beta_{\Re}=c(K)\). Minimizing over all projective diagrams proves the equality. □

### A concrete counterexample to the auxiliary conjecture

The source's Conjecture 1.1(2) explicitly includes classical local knots and proposes \(\beta_{\Re}(K)\le\operatorname{span}V_K\). [Exact statement](https://arxiv.org/html/2609.40122v1#S1.SS1).

For the positive torus knot \(T(3,4)\), direct calculations give

\[
V_K(t)=t^3+t^5-t^8,
\qquad
\Delta_K(t)=t^3-t^2+1-t^{-2}+t^{-3}.
\]

Their spans are five and six. A Seifert matrix of size \(2g(K)\) gives \(\operatorname{span}\Delta_K\le2g(K)\), and Seifert's algorithm on any \(c\)-crossing diagram gives \(2g(K)\le c\). Thus no crossing-number table is needed:

\[
\boxed{\beta_{\Re}(K)=c(K)\ge6>5=\operatorname{span}V_K.}
\]

The accompanying portable verifier computes the Jones polynomial from all 256 bracket resolutions of the actual braid \((\sigma_1\sigma_2)^4\), with writhe normalization. It independently computes Alexander from the reduced Burau matrix of that braid. Unknot and trefoil calibrations check the Jones convention. The Jones value also agrees with [Stoimenow's primary knot tables](https://stoimenov.net/stoimeno/homepage/ptab/). Mirroring reverses exponents and changes neither span. The verifier checks the polynomial certificate; the topological identity has the separate proof above.

This disproves the stated auxiliary span inequality. It is not a Jones-one knot and does not refute or prove Jones unknot detection. The result also does not invalidate the source's alternating-link theorems or classify every other statement in that preprint.

### Consequences for the full research strategy

The obstruction is broader than one proposed numerical inequality. Known infinite families of pairwise-distinct knots have one exact Jones polynomial. Since only finitely many classical knots have bounded crossing number, the identity above forces \(\beta_{\Re}\) to be unbounded on those fibers. Therefore **no bound \(\beta_{\Re}(K)\le F(V_K)\) can hold for all knots**, regardless of the function \(F\). [Watson's infinite-family theorem](https://personal.math.ubc.ca/~liam/files/identical.pdf).

The weaker assertion that one specified nonempty Jones fiber has bounded \(\beta_{\Re}\) is exactly the assertion that this fiber contains finitely many knot types. It still implies detection by connected-sum amplification, but the projective invariant supplies no relaxation of that crossing-number problem. The successful pass-30 bridge bound remains true; the proposed premise feeding it has now been tested and rejected in its general forms.

The parallel investigations also obtained fixed-color Mahler bounds and finite root-of-unity value sets for finite twist templates. Those deductions and the failed monotone-cancellation proposals are preserved in the archive, but they are unnecessary for the stronger crossing-number obstruction. They should not become new research branches merely because they remain interesting.

**Decision.** Close the general Jones-to-projective-complexity branch. Retain the independently viable targets of bounded bridge number or reduced homology in one whole Jones fiber, a geometric constraint on ribbon-concordance complements, or an actual generic representation kernel. A further pass must propose a mechanism for one of those missing statements; the projective-span conjecture can no longer serve as that mechanism.

## 15. Pass 32: exterior volume, finite probes, and two new framework tests

### A complete endpoint through exterior geometry

Let \(v(K)\) be the sum of the volumes of the hyperbolic pieces in the JSJ decomposition of the knot exterior. Equivalently, it is \(v_3\) times relative simplicial volume, where \(v_3\) is the volume of a regular ideal hyperbolic tetrahedron. This definition includes satellite and composite knots.

**Conditional theorem.** If \(v(K)\) is bounded throughout any one nonempty exact Jones fiber, then the ordinary Jones polynomial detects the unknot.

The issue that must be resolved first is that many nontrivial knots have zero exterior volume. Those knots are precisely graph knots, obtained from the unknot by cabling and connected sums. [Motegi–Takata, introduction](https://arxiv.org/pdf/1501.01105).

Write \(a_2(K)\) for the second Conway coefficient. The Alexander satellite formula and the symmetric torus-knot formula give

\[
a_2(K\#L)=a_2(K)+a_2(L),\qquad
a_2(C_{p,q}(K))=p^2a_2(K)+\frac{(p^2-1)(q^2-1)}{24},
\]

where \(p\) is longitudinal winding. Starting from the unknot, these formulas show that **every nontrivial graph knot has \(a_2>0\)**. Mirrors introduce no negative term. Winding-one cabling preserves the companion, and a torus knot with \(|q|=1\) is the unknot; thus the degenerate operations create no exception.

The normalized Jones skein relation gives \(V'_K(1)=0\) and \(V''_K(1)=-6a_2(K)\). Consequently a nontrivial knot with \(V_K=1\) cannot be a graph knot: it must have \(v(K)>0\).

Now choose an anchor \(J\) in the proposed bounded fiber. For a hypothetical nontrivial Jones-one knot \(K\), multiplicativity and simplicial-volume additivity give

\[
V_{J\#K^{\#m}}=V_J,\qquad
v(J\#K^{\#m})=v(J)+m\,v(K)\longrightarrow\infty.
\]

This contradicts the bound and completes the conditional proof. The additivity is Soma's theorem, recalled in [Detcherry–Kalfagianni–Yang, Section 5](https://users.math.msu.edu/users/kalfagia/paper1-23.pdf). No colored-Jones or volume conjecture is used in this implication. Independent internal audits checked the graph-knot induction and derivative normalization.

**Scope of the missing premise.** The bound must cover the entire fiber, including composites. A bound only for hyperbolic or prime knots would miss the displayed connected sums. The assertion that *some* fiber is bounded is itself equivalent to detection, because detection makes the unit fiber a singleton. Its usefulness would therefore require an independent mechanism for a specified nonunit fiber or a stronger general theorem. No such bound was proved here.

This is exterior volume, not branched-cover volume. Nor does bounded exterior volume imply finitely many knot types: Dehn fillings can vary infinitely while their volumes remain bounded. The known fixed-twist Jones families therefore do not refute the premise. The primary literature explicitly asks about fixed-Jones knots with unbounded volume; our bounded search found no established example, which is not an exhaustive status claim. [Stoimenow, Question 8.2(4)](https://stoimenov.net/stoimeno/homepage/progs/ntrivodd.pdf).

### An actual obstruction to replacing the full polynomial by finite probes

**Derived theorem.** Given any integer \(d\ge0\), finite set \(\Omega\) of roots of unity, and \(B>0\), there is a hyperbolic knot \(K\) with

\[
\Delta_K=1,\qquad
V_K(e^h)=1+O(h^{d+1}),\qquad
V_K(\zeta)=1\quad(\zeta\in\Omega),\qquad
v(K)>B.
\]

This establishes simultaneous agreement at prescribed finite probes. It does not establish that the whole polynomial is one.

Here is the construction. Use Kalfagianni's hyperbolic Brunnian link consisting of an unknot and \(n\) crossing circles. Twisting a proper subset of the circles leaves the unknot. After filling all circles, reversing any nonempty subset of twists therefore unknots the result. It is \(n\)-adjacent to the unknot. For \(n>2\), this forces Alexander polynomial one and agreement of finite-type invariants through every order less than \(2n-1\). [Brunnian construction, Lemma 2.4](https://arxiv.org/pdf/0710.0076), [adjacency consequences, Theorem 2.3](https://arxiv.org/pdf/math/0411384).

Choose \(n\) large enough for both the requested Taylor order and volume. To enforce the finite evaluations, at each \(\zeta\ne\pm1\) choose a root of unity \(A\) with \(A^{-4}=\zeta\). In the two-strand Temperley–Lieb algebra,

\[
g=A I+A^{-1}e,\quad e^2=(-A^2-A^{-2})e,\qquad
g^2=A^2I+(1-A^{-4})e.
\]

Its full-twist eigenvalues are \(A^2\) and \(A^{-6}\), distinct at these specializations. If \(R\) is a common multiple of the orders of all the selected \(A\)'s, then \((g^2)^R=I\), and the writhe normalization is also one. Choose every filling order to be a positive multiple of \(R\). Each twist then preserves all the chosen evaluations before any closure is taken.

At \(\zeta=1\), knot normalization gives one. At \(\zeta=-1\), Alexander polynomial one gives \(|V_K(-1)|=1\). The identities \(V_K(1)=1\) and \(V'_K(1)=0\) imply \(V_K(-1)\equiv1\pmod4\), fixing the sign to \(+1\). This separate step avoids dividing by a vanishing quantum dimension.

For each fixed \(n\), the multiples of \(R\) can be arbitrarily large. Hyperbolic Dehn filling makes their volumes approach the parent volume, which is at least \((n+1)v_3\). Increasing \(n\) and then choosing sufficiently long fillings gives \(v(K)>B\). Keeping only one parent would not yield unbounded volume.

The proof received an independent internal audit. A portable exact calculation checks the local twist identity at primitive \(A\)-orders 1 through 48, including its failure at order eight, where \(t=-1\) requires the determinant argument. These finite arithmetic checks support the conventions; the algebraic and geometric proof supplies the general statement. A separate unreduced all-color version is recorded in the archive, with its zero-quantum-dimension limitation kept explicit.

Thus no fixed finite collection of ordinary Jones evaluations and Taylor coefficients can bound exterior volume, even with the full Alexander polynomial supplied. A viable proof must exploit the entire Jones polynomial or additional geometry.

### What the new spectral and representation frameworks actually provide

The [Grlj–Lauda Laplacian preprint](https://arxiv.org/abs/2608.24298) gives geometric models for parts of the Khovanov complex. However, cooling the signed partition function cannot reveal its hidden rank. If \(Q=d+d^*\), then on each positive eigenspace of \(Q^2\), the operator \(Q\) pairs even and odd homological parity. Hence, in every quantum grade \(j\),

\[
\operatorname{Str}f(\Delta_j)=f(0)\chi_j
\]

for every function on the finite spectrum. All signed heat traces, signed resolvents, and ordinary superdeterminants contain exactly the Jones Euler data. The actual same-Jones pair \(5_1,10_{132}\) has reduced rational ranks five and eleven. A spectral gap controls positive eigenvalues, not the number of zero modes. The new source does not supply the missing whole-fiber bound.

The [Luo–Wan dyadic braid preprint](https://arxiv.org/abs/2610.09333) has genuine global link coverage. Its algebraic kernel, however, reduces to the direct limit of the finite-strand Jones kernels: the Thompson-group label survives the algebra relations, and the finite-stage inclusions are injective. Coverage up to extra split unknots also leaves a non-extremal normalization for every nontrivial knot. The enlarged framework therefore supplies neither a new kernel nor an automatic equality case for positivity. The precise deductions and scope are in the archive.

**Decision.** Retain exterior volume as a complete geometric endpoint, with its premise clearly open. A bounded total collection of hyperbolic Dehn-filling parents is an equivalent structural formulation, not a new proof of the bound. An essential scalar satellite pattern would concretely falsify the stronger all-fiber version by inserting companions of increasing exterior volume; none has been constructed. Stop the signed-heat-trace and automatic dyadic-kernel shortcuts. Further work must produce a whole-polynomial geometric mechanism or an actual braid/pattern certificate, rather than more finite probes or a renamed boundedness assumption.

## Sources and provenance

- Kronheimer and Mrowka, *Khovanov homology is an unknot-detector*: https://arxiv.org/abs/1005.4346. This supplies the rank-one endpoint, not H-rank or H-spread.
- Khovanov, *Patterns in knot cohomology I*: https://arxiv.org/abs/math/0201306. Background for reduced homology and connected sums.
- Lee, *An endomorphism of the Khovanov invariant*: https://arxiv.org/abs/math/0210213. Background for the rational deformation and spectral-sequence endpoint.
- Lidman and Moore, *Adjacency of three-manifolds and Brunnian links*: https://arxiv.org/abs/2308.06211. Geometric input for the adjacency construction; it does not supply generic reduction G or braid-family coverage.
- Stoimenow, *Some applications of Tristram–Levine signatures and relation to Vassiliev invariants*: https://doi.org/10.1016/j.aim.2004.07.003. Source of the particular braid/clasp family.
- Our previous conditional reduction and its exact example are recorded in `jones-brunnian-reduction-and-exact-test.txt` in this output directory. The norm calculation and the present scaffold still require the usual independent mathematical review before any publication claim.

No full proof or counterexample has been obtained.

Pass-32 exterior-volume proof, independent audits, finite-probe construction, exact root-specialization verifier, and framework tests are in [the exterior-volume and finite-probe evidence archive](jones-exterior-volume-and-finite-probes-evidence.zip).

Pass-31 crossing-identity proof, independent audits, exact torus-knot verifier, and parallel tests are in [the projective crossing-identity evidence archive](jones-projective-crossing-identity-evidence.zip).

Pass-30 geometric proofs, the Ising and dual-systole audit, source-proof counterexample, and parallel route assessments are in [the projective compression scaffold archive](jones-projective-compression-scaffold.zip).

Pass-29 family proofs, internal audits, actual diagram data, and portable arithmetic checks are in [the colored-fiber and positivity evidence archive](jones-colored-fiber-and-positivity-evidence.zip).

The pass-23 candidate subset and checks remain in [the global geometry and quantum tests archive](jones-global-geometry-and-quantum-tests.zip). The pass-24 global obstructions, braid criteria, spectral proof and independent audits, and portable exact verifiers are in [the geometric cancellation and braid evidence archive](jones-geometric-cancellation-and-braid-evidence.zip). Pass-25 notes, the anchored-fiber audit, and exact algebra checks are in [the scaffold mechanism audit archive](jones-scaffold-mechanism-audit.zip). Pass-26 proofs, independent audits, source locators and portable verifiers are in [the Watson bound and structural tests archive](jones-watson-bound-and-structural-tests.zip). Pass-27 notes and the audited Bing formula are in [the Bing realization and global mechanism archive](jones-bing-realization-and-global-mechanisms.zip). Pass-28 proofs, source locators, internal audits, and portable exact checks are in [the finite-order realizability and geometry archive](jones-finite-order-realizability-and-geometry.zip). The scripts verify the stated algebra and table deductions; they do not verify the original published theorems or certify any remaining ribbon concordance or Jones-one counterexample.
