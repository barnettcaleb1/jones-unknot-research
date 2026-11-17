# Surgery-collapse sources and grading audit

Codex subagent, 15 November 2026, referee of Claude233719 item 2. No knot search or numerical survey was performed. Verdict: the plane-Floer statement is stronger than recalled, but it also makes the proposed unlabelled matching bound against surgery Floer rank automatic for actual closures. The bound can reject formal objects; it is not by itself a new constraint on actual tangles.

## 1. Daemi supplies the full quantum-monotone degree rule

Primary source: Aliakbar Daemi, *Abelian Gauge Theory, Knots and Odd Khovanov Homology*, arXiv:1508.07650; author-hosted version dated 2 January 2017, https://www.math.wustl.edu/~adaemi/PFH.pdf . The author's publication page still lists this as a preprint. The exact places are §1.3, §3.2 (especially Lemma 3.10 and the following paragraph), Corollary 3.15, and Theorem 4.9. The introduction's Theorems 2–4 summarize the result; §4.2 explicitly specifies **reduced** odd Khovanov homology.

Over the characteristic-two Novikov field Lambda, the spectral sequence starts at reduced Khovanov homology of the mirror link and abuts to plane Floer homology of its branched double cover. Daemi's homological filtration increases, and his delta grading increases by exactly one under the total differential. Theorem 4.9 relates the ordinary Khovanov gradings by

    h_Kh = h_Daemi,
    q_Kh = 2(h_Daemi - delta_Daemi) + 1.

Consequently, on page r,

    Delta h_Kh = r,
    Delta q_Kh = 2r - 2,
    Delta(q_Kh/2 - h_Kh) = -1.

The constant +1 is only the normalization of the reduced quantum grading. Thus, after E2, r>=2 and the quantum degree increases strictly. This is **not an extra conjectural quantum refinement of the Daemi sequence**. It is already part of its grading statement. Base extension from F2 to Lambda does not change the dimension of any Khovanov bigraded summand.

This says nothing by itself about the degree rule for the Ozsvath–Szabo sequence with Heegaard Floer target. Those are different sequences. The previous Saltz caution about ordinary holomorphic-polygon maps remains relevant to that identification, but does not alter Daemi's distinct construction.

Section 1.3 computes

    rank_Lambda PFH(Y) = 2^{b1(Y)} |Tor H1(Y;Z)|.

Hence the plane-Floer target has rank det(L) when det(L) is nonzero. For a closure whose cover is S3_0(kappa), the target has rank **2**, since H1=Z; it never has rank zero. The mirror changes neither this target dimension nor the matching obstruction, provided the grading conventions are transformed consistently.

## 2. The exact matching consequence, and why R adds nothing to it

For a finite bigraded vector space V, form the graph whose vertices are its generators with multiplicity and whose edges join pairs differing by (r,2r-2) for some integer r>=2. Let

    mu(V) = dim(V) - 2 maximum_matching_size.

This is a relaxation of a specified geometric spectral sequence: actual pages may use linear combinations, but graded Gaussian elimination transports the pairs to graded bases at E2. Their source/target bidegrees and multiplicities still give such a matching. Conversely, a disjoint matching can be made into a formal filtered differential by mapping each source to its paired target and setting every other map to zero. This converse constructs only an abstract filtered complex, not a geometric spectral sequence or functorial maps.

Daemi therefore implies

    mu(Kh~(L;F2)) <= det(L),                 det(L) != 0.

Every permitted edge lowers delta=q/2-h by one, so its endpoints cancel in the delta Euler characteristic. In the usual reduced normalization, its absolute value is det(L): evaluate the Jones Euler polynomial at q=i, accounting for the common phase when the quantum degrees are odd. Thus every matching leaves at least det(L) generators. Combining the two directions gives the exact necessary property of every actual link:

    mu(Kh~(L;F2)) = det(L),                 det(L) != 0.

For the actual integer closures of a quotient tangle,

    mu(Kh~(T(n))) = |n|,                    n != 0,
    mu(Kh~(T(0))) <= 2.

At n=0 the delta Euler characteristic is zero, so this argument does not decide between minimum 0 and minimum 2.

Now compare with the proposed inequality

    mu(Kh~(T(n))) <= rank HFhat(S3_n(kappa)).

For n!=0 this is automatically the familiar rank bound rank HFhat >= |H1|=|n|. For n=0 the right side is a positive even number and therefore at least 2: nonvanishing plus the zero Euler characteristic of hat Floer homology for b1=1. The plane-Floer matching already leaves at most 2. Therefore the inequality is automatic at every integer slope for actual tangles and cannot extract a new lower bound on the surgery defect R.

This does not make the finite matching check useless. It can falsify the realizability of a **formal** tangle object if even one of its formal closures fails the Daemi condition. Such a rejection is an actual gain over the separate augmentation-level model in the preceding letter. What it cannot do is supply new restrictions on an actual knot's R merely by comparing minimum possible matching rank with its Heegaard Floer rank.

The quantum distribution, Spin-c labels, target gradings, cobordism maps, or compatibility between closure slopes could still contain information. They are not captured by mu.

## 3. Ozsvath–Szabo's surgery rank formula: exact scope

Use the **journal** version: Peter Ozsvath and Zoltan Szabo, *Knot Floer homology and rational surgeries*, Algebraic & Geometric Topology **11** (2011), 1–68, Proposition **9.6**, pp. 51–52, https://msp.org/agt/2011/11-1/agt-v11-n1-p01-s.pdf . The arXiv v1 HTML has a differently numbered and less carefully stated predecessor; it should not govern this audit.

Write mK for the mirror. The proposition assumes

    p != 0, q > 0, gcd(p,q)=1,
    nu(K) >= nu(mK).

Set R(K)=sum_s(rank H(Ahat_s(K))-1). If nu(K)>0 or p>0, it states

    rank HFhat(S3_{p/q}(K))
      = p + 2 max(0,(2nu(K)-1)q-p) + q R(K).

If nu(K)=0 and p<0, it states instead

    rank HFhat(S3_{p/q}(K)) = |p| + q R(K).

Thus Claude's displayed positive-integer formula is the p=n>0,q=1 specialization **with the orientation hypothesis included**. One can mirror to arrange that hypothesis, but the surgery sign changes and R must be recomputed for the selected knot. In particular, use neither an absolute value in place of the first p in the first formula nor the same R on both mirrored sides without a separate proof. The case p=0 is not part of Proposition 9.6.

For a positive L-space knot, nu=g and every H(Ahat_s) has rank1, so R=0 and positive surgeries n>=2g-1 have rank n. A direct sum decomposition of CFK into a positive L-space staircase and **unit** acyclic boxes has each box contributing two to R (its L-shaped truncation contributes rank2 at one index). This is a statement about that specified filtered CFK model. The picture of squares in N(T), or the condition Delta=1, does not identify those squares with CFK boxes. Rectangles with nonunit lengths require their own truncation count. On the opposite orientation even a staircase without boxes can have nonzero R.

## 4. The labelled-special inference does not follow from R=0

Even on the L-space surgery side, the target rank n does not imply that every generator supplied by a special component dies. Under the quoted closure formula the rational component supplies |n-k| generators, which is generally not n. Later differentials can also mix the rational and special components; the direct sum at E2 need not remain a direct sum on later pages.

For example, if n>k>0 and the rational part has n-k generators, an n-dimensional target necessarily has at least k survivors involving the special part, unless the asserted component/rank decomposition itself changes. For k<=0 there is no such immediate contradiction, but the conclusion still requires a geometric argument selecting the surviving n-dimensional rational contribution. Total rank alone does not provide one.

Accordingly the claims about every top-level special being a source, every bottom-level special being a target, and anti-tilt being impossible cannot be deduced from R=0 alone. They become valid elementary endpoint statements only after the appropriate subset is proved fully matched, and after all other possible partners (including the rational summand) are accounted for.

## 5. Scope of the present audit

The exact closure pairing model and the proposed shifted ladder are being checked separately by the root agent. This source audit does not certify their numerical matching counts or their grading normalization. In particular the exceptional rational self-pairing at slope n=k must be handled separately; a generic |n-k| intersection formula can miss the parallel-curve contribution there.

The useful next mathematical object is the family of **geometrically compatible** Daemi/closure maps or a precise finite obstruction to realizing its closure profiles. The existence of a rank-bounded matching at each slope, taken separately, is an established necessary condition, not a new mechanism for NP.

## 6. Novikov coefficients and the target grading

The Novikov energy variable does not invalidate the preceding bidegree calculation. Section 1.3 assigns plane degree to Morse generators by deg_p(alpha)=2 ind(alpha)-b1(Y), extended linearly over the coefficient field. The energy weights occur in matrix coefficients. Lemma 3.10 proves the degree of the whole cobordism map, not just an individual unweighted term. Thus the characteristic-two field extension does not supply hidden quantum shifts.

The stronger assertion that every E-infinity generator for b1=0 lies in one Khovanov delta degree, identified with a signature shift, has **not been certified by this audit**. Theorem 3.2 is stated as a chain-homotopy identification in the unfiltered category, while the later filtered graded invariance is proved for diagram changes. Equation (61) carries the signature term needed for a graded comparison, and such a refinement may be derivable, but it must be written rather than inferred merely from the fact that Jac(Y) consists of points. None of the matching/rank conclusions above requires this extra target-grading identification.

## 7. Follow-up on Claude234649/235059: coefficients and the bare-object count

The geometric Daemi spectral sequence is over the characteristic-two Novikov field Lambda, with E2=Kh~(L;F2) tensor Lambda. The matching statement is nevertheless about the unchanged F2 bigraded dimensions. An abstract F2 filtered complex with that matching can be constructed using coefficients 0 and 1, but this is not descent of Daemi's geometric maps, naturality, or cobordism structure.

A finite check of the stated closure grid in `tools/daemi_match.py` confirms that at n=1 each of the two adjacent rows for bare B has half-quantum multiset {0,1,2,3,3,4,5,6}. At most six of its eight generators can be strictly-increasing matched to the other row. Four remain, and the free rational generator can remove at most one of these, so minimum rank is three. This establishes the needed n=1 obstruction within that closure model.

The stronger all-n claim “minimum rank is 2n+1” is not correct for that model: its row polynomial is

    (1+x)(1+x^2)(1+x^3)(1+x+...+x^{n-1}).

The maximum coefficient is at most eight, and the matching defect of two identical rows under strict increase is twice that maximum; allowing the extra free generator reduces this by one. In particular n=8 gives maximum multiplicity eight, 56 row-to-row pairs, and minimum rank 15, rather than 17. This changes no nonrealizability conclusion: the n=1 obstruction already suffices. The checks made here are the specified n=1,2,3 certificates and the single n=8 countercheck to the asserted general formula, not a knot scan.
