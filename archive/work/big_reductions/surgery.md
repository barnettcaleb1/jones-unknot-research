# Three-probe unframed rigidity and the two-probe arithmetic alternative

Date: 2026-11-03. Author of the main three-probe idea: root agent in this pass. Independent derivation/audit and arithmetic corollaries: surgery_reduction agent.
Status: TRUSTED, new in this project; complete deduction from the surgery lemma already underlying audited LATE-41; no new external specialist review; priority unverified. This is not a proof of Jones unknot detection.

## 1. General homology interpolation lemma

Let M be a compact connected oriented 3-manifold with one torus boundary, with at least one rational-homology-sphere filling. Let V be a marked solid torus with the same boundary slope lattice. Put h(Y)=|H_1(Y;Z)| when this group is finite, and h(Y)=0 when it is infinite.

**Lemma.** If h(M(alpha_i))=h(V(alpha_i)) for three distinct slopes alpha_1,alpha_2,alpha_3, then H_1(M)=Z, the boundary-to-free-homology map is surjective, and M and V have the same homological longitude.

**Proof.** A finite filling gives b_1(M)=1. Write H_1(M)=Z+T, and let ell_M:H_1(boundary M) -> Z be the free projection of the inclusion map. This linear integral functional need not initially be primitive. Filling kills the class of alpha, and hence

    h(M(alpha)) = |T| |ell_M(alpha)|.

This also holds when ell_M(alpha)=0, using h=0. Let m=|T| ell_M and let l be the primitive functional of V. The homogeneous degree-two polynomial

    m(x,y)^2-l(x,y)^2=(m-l)(m+l)

vanishes in three distinct projective directions, so it is identically zero. Thus m=+l or m=-l. Since l is primitive integral, |T|=1 and ell_M is primitive. Its kernel is the disk slope of V. QED.

No Jones information, framing, or geometric equality of the third filled manifold is involved here.

## 2. Two matched finite fillings once homology is calibrated

**Surgery lemma (the nonlongitudinal case of LATE-41).** Suppose M is as above, H_1(M)=Z, its boundary map is primitive, and its homological longitude agrees with the meridian of the marked solid torus V. If, at two distinct nonlongitudinal slopes alpha,beta, there are orientation-preserving homeomorphisms

    M(alpha) ~= V(alpha),   M(beta) ~= V(beta),

then M is a solid torus with the same disk slope as V.

**Proof details.** Choose a slope mu dual to the common longitude lambda. Then Y=M(mu) is an integral homology sphere and M is the exterior of the filling core K in Y. Writing alpha_i=p_i mu+q_i lambda gives

    Y_{p_i/q_i}(K) ~= L(p_i,q_i),  p_i != 0,

with the same signed coefficient on the two sides, because the boundary marking preserves orientation. Casson-Walker surgery gives

    0=lambda_CW(Y)+(q_i/(2p_i)) Delta_K''(1).

The ratios q_i/p_i are different, so Delta_K''(1)=0 and lambda_CW(Y)=0.

The two lens fillings are L-spaces. Rasmussen-Rasmussen Proposition 1.3 gives Floer simplicity. Their torsion normal form (Proposition 1.4 and Section 2.1) gives alternating nonzero coefficients of the symmetric normalized Alexander polynomial. If

    Delta(t)=(-1)^k + sum_{j=1}^k (-1)^{k-j}(t^{n_j}+t^{-n_j}),
    0<n_1<...<n_k,

then Delta''(1)=2 sum_j (-1)^{k-j} n_j^2 is strictly positive whenever k>0 (pair adjacent terms, leaving the positive smallest term if k is odd). Hence Delta=1. RR Corollary 2.3 would give Thurston norm degree(Delta)-1=-1 if the boundary were incompressible. Therefore the boundary compresses.

M is irreducible: in a separating connected-sum decomposition M=M_0#Z, the torus-boundary piece has positive b_1, so H_1(M)=Z forces H_1(Z)=0. A lens filling is prime, so Z must be S^3. A nonseparating sphere is excluded by H_2(M)=0. Boundary compression now implies M is a solid torus. Its disk slope is its homological longitude, as required. QED.

This explicitly avoids RR Proposition 7.8 and the false shortcut through Sikora Proposition 10(1).

## 3. Positive theorem: two actual closures plus one determinant

**Theorem.** Let R be a rational two-string tangle and X an arbitrary two-string tangle in the same marked ball. Let alpha,beta be distinct rational closure slopes for which the closures of R have nonzero determinant. Suppose the unframed links C_alpha(X), C_beta(X) are ambient isotopic to C_alpha(R), C_beta(R), respectively. If for any third distinct slope gamma,

    det C_gamma(X)=det C_gamma(R),

then X is isotopic to R as an unframed marked tangle.

**Proof.** Double branched covers give two actual orientation-preservingly matched lens fillings. The third determinant gives the third homology order. Apply Sections 1 and 2. A tangle with solid-torus double branched cover is rational; rational tangle classification then identifies X and R because their disk slopes agree. QED.

**Three actual closures corollary.** If three distinct rational closures of X are ambient isotopic to the corresponding closures of a rational R, then X=R unframed. At most one closure slope is longitudinal for R; choose the other two as alpha,beta, and use the third only for its determinant.

**Sharp diagnostic corollary.** If a nonidentical X and rational R satisfy two such actual nonlongitudinal closure equalities, then their determinants differ at *every* other closure slope. Thus even one arbitrarily chosen additional determinant measurement rules out the entire nonunique alternative.

## 4. Additional positive theorem: an arithmetic condition eliminates the third probe

Let d=Delta(alpha,beta)>0 be the geometric intersection number of the two filling slopes, and let u be a signed value of the solid-torus homology functional on alpha, so |u|=det C_alpha(R).

**Theorem.** Under the two actual nonlongitudinal closure hypotheses of Section 3, if

    d does not divide 2 det C_alpha(R),

then X=R without a third closure or determinant assumption. The divisibility condition is equivalent with beta in place of alpha.

**Proof.** Use an integral oriented basis with alpha=(1,0), beta=(a,d), gcd(a,d)=1. Write the primitive functional of V as l=(u,v). The two absolute homology equalities imply, after a global sign choice m(alpha)=u, either

    m=l,

or the only alternative is

    m*=(u, -v-2au/d).

Since m=|Tor H_1(M)| ell_M is integral, the second case is possible only if d divides 2au, equivalently d divides 2u. Under the stated hypothesis it is impossible, so m=l. Primitivity gives H_1(M)=Z and common longitude, and Section 2 finishes. Finally l(beta)=au+dv, so d|2l(beta) iff d|2u. QED.

**Example of scope.** If one matched closure is the unknot, its determinant is 1. Any matched second nonlongitudinal rational closure at slope distance at least 3 therefore forces rationality. In contrast, the crossing-change distance-2 case always passes the divisibility test: this result does not settle Lemma Q.

**Explicit residual alternative.** For arbitrary two-probe data, all nonidentical solutions must have homology-order functional m* above, up to global sign. Consequently every remaining determinant is prescribed by |m*(gamma)|, not merely bounded. The primitive longitude and the product |Tor H_1(M)| times the boundary-image index are computable from m*. This is a concrete arithmetic restriction on candidate unframed counterexamples.

## 5. Sharpness calibration against an actual known two-probe rival

Archive EARLY-25 records the Ernst-Sumners example

    X=<-1>+<1/2>+<1/3>,   R=<1/4>,
    N(X)=N(R)=U,
    N(X+<1>)=N(R+<1>)=T(2,-5),

with X nonrational. For a rational add-on <p/q>, the usual Montesinos homology determinant gives

    det N(X+<p/q>) = |(2)(3)q(-1+1/2+1/3+p/q)| = |6p-q|,
    det N(R+<p/q>) = |(4)q(1/4+p/q)| = |4p+q|.

The q=0 values follow by denominator closure, or directly by the linear homology functionals. Their squared difference is

    (6p-q)^2-(4p+q)^2 = 20p(p-q).

Thus the determinants agree exactly at add-ons 0 and 1, which are the two actual common closures. They differ at every third slope, exactly as the new theorem predicts. In particular, the denominator closures have determinants 6 and 4. This also shows that two unframed actual closure equalities alone cannot replace three in the general theorem. The two probes here have distance 1, so the arithmetic obstruction correctly leaves the example alive.

## 6. Relation to Jones and the precise missing input

Theorem 3 converts actual topology at only two slopes plus one scalar datum into rationality. In the unit-Jones / Lemma-Q setting, the bracket supplies all scalar determinant data, and an actual unknot supplies one actual filling. What is still missing is a second genuine lens filling (or a different geometric condition strong enough to replace it). The theorem does not promote Jones equality to link isotopy. Its value is that framing is no longer the obstruction once a third determinant is available, and the full residual ambiguity of two unframed equations is an explicit reflected homology functional.

## 7. Sources and bounded novelty check

- Rasmussen and Rasmussen, *Floer Simple Manifolds and L-Space Intervals*, arXiv:1508.05900, Proposition 1.3, Proposition 1.4, Section 2.1, Corollary 2.3: https://arxiv.org/abs/1508.05900 . The detailed hypothesis audit is already in collab/audits/LATE-41-audit.md. In this pass I independently reopened the primary HTML and checked Proposition 1.3, the coefficient normal form preceding Proposition 1.4, and Corollary 2.3 exactly as used above.
- Casson-Walker formula: Boyer-Lines, restated in Ni-Wu, *Cosmetic surgeries on knots in S3*, arXiv:1009.4720, Proposition 3.1: https://arxiv.org/abs/1009.4720 . The primary Ni-Wu HTML was reopened in this pass; Proposition 3.1 has exactly the null-homologous/rational-homology-sphere hypotheses and signed q/(2p) formula used here. Orientation preservation and identical signed boundary coefficients are essential.
- Gainullin, *Heegaard Floer homology and knots determined by their complements*, Algebraic & Geometric Topology 18 (2018), 69-109, Theorem 8.2: https://msp.org/agt/2018/18-1/agt-v18-n1-p03-p.pdf . Prior method overlap must be credited; our auxiliary homology sphere Y is not assumed to be an L-space.
- Sikora, *Tangle Equations, the Jones Conjecture, Slopes of Surfaces in Tangle Complements, and q-Deformed Rationals*: https://arxiv.org/html/2005.08162v2 . The paper's main setup is systems of two closure equations.
- Buck and Mauricio, *Tangle solutions for composite knots: application to Hin recombination*, Theorem 3.5(2), records the solid-torus branched-cover criterion attributed to Lickorish: https://arxiv.org/pdf/1007.0948 . Equality of the marked disk slopes then uses the usual classification of rational tangles.
- Baker-Buck, *The classification of rational subtangle replacements between rational tangles*, for nearby rational-tangle replacement classification: https://msp.org/agt/2013/13-3/agt-v13-n3-p05-p.pdf . The bounded search found this nearby literature, not the stated marked three-probe theorem.

Searches for three matched solid-torus fillings, three rational closure uniqueness, and two matched unknot surgeries did not identify a prior statement of Sections 3-4. This is not a novelty certification. The unknot-closure distance-at-least-3 special case may be recoverable from older rational-subtangle-replacement classifications; do not advertise it as new before that comparison.
