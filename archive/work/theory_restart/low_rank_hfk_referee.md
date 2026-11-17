# Low-rank Floer audit of Claude 233719, item 3

15 November 2026. Coefficients are F₂ unless otherwise stated. This report does not change the board.

## Verdict

The rank-three statement is correct. The claimed rank-five classification is false: T(3,4)=8₁₉ already has total knot Floer rank five and is neither the figure-eight nor T(2,5). Farber–Reinoso–Wang prove detection of the **bigraded** knot Floer homology of T(2,5), not detection by its total rank. Their published theorem cannot supply the asserted list.

Consequently the proposed conclusion `flat nonrational => dim N >= 7` is **not established by that argument**. A valid, narrower conclusion is

\[
T\text{ flat and nonrational}\Longrightarrow\dim N(T)\ge5.
\]

The equality case can be sharply restricted without a rank-five knot classification: it would have covering knot κ satisfying

\[
\operatorname{rk}\widehat{HFK}(\kappa)=5,\quad \Delta_\kappa=1,
\quad \kappa\text{ nonfibered},\quad |\tau(\kappa)|=g(\kappa),
\]

and its Alexander-graded ranks would be two at ±g, one at zero, and zero elsewhere. This is a necessary profile, not a realization theorem or a claim that such a knot exists. In this equality case Theorem S's sequence collapses from its E² page by equality of total ranks.

## 1. Exact source statements

**Rank three.** Hedden–Watson, *On the geography and botany of knot Floer homology*, Selecta Math. (N.S.) **24** (2018), 997–1037, [arXiv:1404.6913v3](https://arxiv.org/html/1404.6913v3), Corollary 8: a knot in S³ with total hat knot Floer dimension three is a trefoil. The paper uses F=Z/2Z. An independent proof is Baldwin–Vela-Vick, *A note on the knot Floer homology of fibered knots*, Algebr. Geom. Topol. **18** (2018), 3669–3690, [journal PDF](https://msp.org/agt/2018/18-6/agt-v18-n6-p14-p.pdf), Corollary 1.5; the proof uses their next-to-top nonvanishing theorem and genus/fiberedness detection. Either chirality is allowed.

**What FRW actually prove.** Farber–Reinoso–Wang, *Fixed-point-free pseudo-Anosov homeomorphisms, knot Floer homology and the cinquefoil*, [arXiv:2203.01402v2](https://arxiv.org/html/2203.01402v2), Theorem A: a knot whose hat knot Floer homology over Q is isomorphic **as a bigraded vector space** to that of T(2,5) is T(2,5). The theorem also states that T(2,5) is the only genus-two L-space knot. Neither statement classifies total-rank-five knot Floer groups, and the second statement has a genus hypothesis.

**Counterexample to the rank-five list.** T(3,4) has genus three and normalized Alexander polynomial

\[
\Delta(t)=t^3-t^2+1-t^{-2}+t^{-3}.
\]

It is an L-space knot. Ozsváth–Szabó, *On knot Floer homology and lens space surgeries*, Topology **44** (2005), 1281–1300, [arXiv:math/0303017v2](https://arxiv.org/html/math/0303017v2), Theorem 1.2, gives rank one at each of the five indicated Alexander gradings and zero elsewhere. This is the same counterexample already used against the earlier genus-rank bound; it lies in Claude's own table with dim N=5.

The source audit did not find a theorem giving the requested total-rank-five list. This report does not assert a complete classification of rank-five knots in its place. Binns–Dey's low-rank link classification is not a substitute: its ranks 4, 6, and 8 concern links with at least two components, not a rank-five classification of knots.

## 2. Strong inversions of the proposed small knots

The inversion list itself is complete, under the usual equivalence by orientation-preserving diffeomorphisms of (S³,K): the trefoil and T(2,5) each have one strong inversion, and the figure-eight has two. Marking one of the two arcs of the fixed set introduces additional marked versions and must not be conflated with the count of unmarked inversions.

A directly accessible primary source is Hirasawa–Hiura–Sakuma, *The equivariant genera of marked strongly invertible knots associated with 2-bridge knots*, [arXiv:2312.06156v1](https://arxiv.org/html/2312.06156v1), Proposition 2.2. For nontrivial two-bridge torus knots it gives one strong inversion and two marked versions. For the figure-eight K(2/5), the hyperbolic case with 2² not congruent to 1 modulo 5 gives two strong inversions and four marked versions. The paper records the classical source as Sakuma, *On strongly invertible knots*, in *Algebraic and topological theories* (Kinosaki, 1984), Kinokuniya, Tokyo, 1986, pp. 176–196; the torus uniqueness is Sakuma's Proposition 3.1.

No inversion enumeration is needed to exclude these knots from flatness. The already audited U4 implication is independent of inversion:

\[
T\text{ flat}\Longrightarrow a_2(\kappa)=0.
\]

The values for 3₁, 4₁, T(2,5), T(3,4) are respectively 1, −1, 3, 5; mirrors have the same a₂. Thus all their inversions are excluded at once. The present audit uses U4 as banked, rather than claiming to re-audit its Casson–Walker/Mullins argument.

## 3. The safe lower bound and the exact equality profile

For an actual nonrational quotient tangle T, κ is nontrivial. Theorem S and rank-one detection give an odd rank r(κ)>1 with

\[
r(\kappa)\le \dim N(T)=1+2m(T).
\]

If dim N≤3, then r=3 and κ is a trefoil. Its a₂ is nonzero, contradicting flatness. Hence dim N≥5, or m≥2.

Suppose now dim N=5 and T is flat. The preceding argument excludes ranks one and three, so r=5 and the sequence collapses by total dimension. Write the symmetrized Alexander polynomial

\[
\Delta(t)=a_0+\sum_{i>0}a_i(t^i+t^{-i}).
\]

Since Δ(1)=1, a₀ is odd, hence |a₀|≥1. The Euler-characteristic inequality gives

\[
|a_0|+2\sum_{i>0}|a_i|=\|\Delta\|_1\le5,
\qquad \sum_{i>0}|a_i|\le2.
\]

Also a₂(κ)=Δ″(1)/2=∑aᵢi²=0. With total positive-index coefficient mass at most two, this is possible only if all aᵢ vanish: one nonzero coefficient cannot cancel; two coefficients with opposite signs must both be units, and would force their distinct positive indices to have equal squares. Thus Δ=1.

At every nonzero Alexander grading, Euler characteristic zero forces the dimension to be even. Genus detection supplies a nonzero group at g>0 and conjugation symmetry supplies its partner at −g. The total dimension five therefore forces exactly ranks (2,1,2) in Alexander gradings (−g,0,g), with opposite Maslov parities in each outer pair. The top rank is two, so κ is nonfibered.

One can also pin down |τ|. Transfer the knot Floer filtered differential to the hat HFK group: there is a square-zero differential of Maslov degree −1 strictly decreasing Alexander grading, with one-dimensional homology. This is the canceling differential recalled by Hedden–Watson, §1 (equations (3)–(4) and the paragraph headed “Canceling differential”). A filtered homogeneous cancellation basis gives two cancelling pairs and one survivor.

If the survivor were the central generator, the two top generators would have to map isomorphically, with Maslov degree −1, to the two bottom generators. If the top Maslov degrees are p,q, conjugation makes the bottom degrees p−2g,q−2g. Comparing the sums of degrees for such an isomorphism gives

\[
(p+q)-2=(p+q)-4g,
\]

or 4g=2, impossible for an integer genus. The survivor lies at one of ±g, so τ=±g. This argument locates the filtered survivor; it does not manufacture an actual rank-five knot or settle whether the profile is realizable.

## 4. What is and is not gained

This is a legitimate restricted reduction: a hypothetical smallest flat object with two special components must map, with no rank loss, to a nonfibered Alexander-one knot Floer profile supported in only three Alexander gradings and with maximal absolute τ. The table's rank-five fibered knots are irrelevant to that remaining profile.

It is not a proof of m≥3. Replacing a failed knot classification by the exact residual profile is the sound status change. A subsequent theorem ruling out that actual knot Floer profile, or showing it is incompatible with the quotient tangle's absolute gradings, would establish the stronger bound. No knot scan, numerical test, or inversion sweep was performed here.
