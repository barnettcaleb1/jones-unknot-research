# Literature digest: strong inversions, quotient tangles and kappa

Brief key: `kwz-inversions`. Status: complete.

Sources read
- [KWZ] Kotelskiy, Watson, Zibrowius, "Khovanov homology and strong inversions", arXiv:2104.13592 **v1** (28 Apr 2021; the only version). TeX source `src/kwz/main.tex`; page numbers from the 15-page arXiv PDF. Coefficients F = F_2 throughout.
- [W] Watson, "Khovanov homology and the symmetry group of a knot", arXiv:1311.1085 **v4** (5 Apr 2017). TeX source `src/watson/involutions.tex`; page numbers from the 31-page arXiv PDF. Statements are numbered consecutively 1-33 ("[Watson2017, Conjecture 28]" in [KWZ] is this numbering).
- [site] kht++ example pages, https://cbz20.raspberryip.com/code/khtpp/examples/strong_inversions.html (one page per inversion; copies in `src/khtpp/examples`), and the kht++ documentation pages Output and Options (`src/khtpp/docs`).
- Cross-reference only: Kotelskiy, Watson, Zibrowius, "Thin links and Conway spheres", arXiv:2105.06308v3, section "The geography problem for Khr" (`src/thin`).

Everything marked **[digest]** is a computation or inference of mine from the data, not a statement of the sources.

Notation in this report: Khr, BNr = reduced Khovanov / Bar-Natan multicurves; a(s) = BNr(Q_s); gradings h (homological), q (quantum), delta, with **delta + h = q/2** in [KWZ]; a shift is written h^a delta^b; t = q^2 is the Jones variable.

---

## 1. Strong inversions and the quotient tangle

[KWZ] Section 1, pp. 2-3; [W] Sections 2.1-2.2, pp. 7-11.

- A strong inversion on K in S^3 is an orientation-preserving involution of S^3 reversing the orientation of K. (K,h) ~ (K',h') if an orientation-preserving homeomorphism f of S^3 has f(K) = K' and h = f^{-1} h' f; equivalently a conjugacy class of order-two elements in Sym(S^3,K) = MCG of the exterior ([KWZ] p. 2; [W] Definitions 5, 8, p. 9). Torus knots have a unique strong inversion ([W] Theorem 6); hyperbolic knots have 0, 1 or 2, and 2 exactly when there is a free or cyclic involution ([W] Theorem 7).
- Quotient: h restricted to the exterior has fixed set two arcs meeting the boundary in 4 points; (S^3 minus nu(K))/h is a ball B^3 and tau = image of Fix(h) is a pair of arcs. T_{K,h} = (B^3, tau), and the exterior is the double branched cover Sigma(B^3, tau) ([KWZ] p. 2).
- Equivalence of tangles in [KWZ]: homeomorphism of pairs fixing the boundary only setwise; a "framed tangle" fixes it pointwise. [W] uses sutured tangles (D^2 x I, tau) with two endpoints on each of D^2 x {0}, D^2 x {1}, up to homeomorphism fixing the suture (Definition 3, p. 7).
- **Correspondence.** [KWZ] p. 3: there is a bijection between equivalence classes of non-trivial strongly invertible knots (K,h) and tangles (B^3,tau) for which tau(infinity) is unknotted; attributed to Gordon-Luecke [GL1989, Theorem 2], "compare" [W, Proposition 9]. [W] Proposition 9 (p. 10): one-to-one correspondence between strongly invertible knots and sutured tangles T with T(1/0) the trivial knot. Inverse construction ([W] p. 10): the double cover of S^3 branched over the unknot T(1/0) is S^3, and K is the lift of an unknotted arc joining the two lobes of the closure.
- The trivial tangle = quotient of the solid torus = the rational tangle ([KWZ] p. 3).

## 2. Conventions: closures, fillings, gradings

**Rational closures** ([KWZ] p. 3, Figure 3). Q_{p/q} are fixed framed rational tangle diagrams (Q_infinity, Q_0, Q_1, Q_{1/3} drawn). tau(p/q) is by definition the link obtained by gluing **Q_{-p/q}** to tau (Figure 3(e)), and

    S^3_{p/q}(K) = Sigma(S^3, tau(p/q))        (Montesinos trick).

**Preferred representative** ([KWZ] p. 3): the framed tangle T with tau(infinity) <-> S^3_infinity(K) = S^3 (so tau(infinity) is the unknot) and tau(0) <-> surgery along the Seifert longitude. Hence, in the notation of the brief, K_n = tau(1/n) = T glued to Q_{-1/n} has double cover S^3_{1/n}(K); the closures tau(n), n integer, have double cover S^3_n(K) and are the ones at distance 1 from the unknot slope. Exception: Figure 4 (p. 3) draws the two tangles of 9_46 with framings n_1 = 2 and n_2 = -6 instead.

**[W] closures** (p. 7-8, Figure 3 there): T(1/0) joins the endpoints inside D^2 x {0} and inside D^2 x {1}; T(0) joins across; T(n) = T^n(0) where T^n has n half-twists added on D^2 x {1}, a positive crossing counting +1. For the preferred representative T° ([W] p. 10, p. 17), S^3_n(K) = Sigma(T°(n)). Example: right-hand trefoil, T°(1) = 10_124 = T(3,5), T°(6) = connected sum (reducible surgery).

**Pairing** ([KWZ] eq. (1), p. 4, quoting [KWZ, Theorem 1.9] of the multicurve paper): for K = T_1 union T_2,

    Khr(K) = HF( m(BNr(T_1)), Khr(T_2) ),      m = mirror identifying the two four-punctured spheres.

In practice ([KWZ] p. 7, Counterexample 3.5): Khr(tau(s)) = HF(a(s), Khr(T)) for the slopes used (s = infinity, 0, n).

**Curve terminology** ([KWZ] pp. 4-5). Curves are drawn in the cover R^2 minus Z^2 -> T^2 minus 4 points -> S^2_{4,*}. A curve is *linear* of slope p/q if it can be homotoped to have all lifted tangent slopes in any neighbourhood of p/q; a linear curve is *rational* if it can avoid a fixed neighbourhood of the special puncture, otherwise *special*. s_n(0), r_n(0), n >= 1 are the curves of Figure 6 (s~_n(0) runs past 2n punctures, r~_n(0) past n); s_n(p/q), r_n(p/q) are their images under the matrix [[q, r],[p, s]] in PSL(2,Z). BNr(Q_{p/q}) = {a(p/q)}, Khr(Q_{p/q}) = {r_1(p/q)} (Example 2.1, p. 5).

**Indexing warning.** [KWZ]'s s_n is the curve called s_{2n} in arXiv:2105.06308 and in current kht++ output. The curve s_2(infinity) of [KWZ] (12 generators, meets a(0) in 4 points) is "s4" in the later notation; the curve s_1 of [KWZ] is the later "s2". The old kht v0.1 pages on [site] still print "s2(0)", the regenerated ones "s4(0)" for the same curve.

**Slope warning for [site].** kht++ labels curves by the negative reciprocal of the [KWZ] slope: site "s2(0)"/"s4(0)" = [KWZ] s_2(infinity); site "r(-1/k)" = [KWZ] r_1(k); site "r(∞)" = r_1(0). The tangle itself is framed as in [KWZ] (kht++ Options page, option -q: closure of slope infinity is the unknot, slope 0 is the longitude).

**Gradings.**
- [W] (Section 1, pp. 4-6): u homological, q quantum with V_L(t) = sum over q of chi_u(Khr_q) t^q (so [W]'s q is the exponent of t and is half-integral for even links), delta_W = u - q; det(K) = |chi_delta Khr(K)|.
- [KWZ]: h, q, delta with delta + h = q/2. [KWZ] p. 10: compared with [W], "our delta-grading has the opposite sign, and our quantum grading is twice as large". So q_KWZ = 2 q_W, delta_KWZ = -delta_W up to normalisation, h = u.
- **[digest]** The absolute normalisations differ by more than a sign. In the five examples printed in both papers (3_1, 4_1 both inversions, 5_1, 8_19, mirrored where needed) one finds h = u and delta_KWZ = -delta_W + 4j, where j = lk(tau(0))/4 is the integer of Section 8. [W]'s absolute delta is a convention (the stable non-kappa generators are put in delta_W = +1/2, Section 7 of [W], p. 27); [KWZ]'s is the kht++ bigrading of the oriented tangle (Section 8 below). [KWZ] claims agreement with [W] only as *relatively* bigraded invariants (p. 8).

## 3. Watson's kappa and its description by curves

**Inverse system** ([W] Section 2.1, pp. 7-8). For a representative T of a sutured tangle put A_i = Khr(T(i)). The long exact sequence of a crossing resolution gives f_i : A_{i+1} -> A_i (third term a shift of Khr(T(1/0))). Kh<-(T) := inverse limit of {A_i, f_i}. Proposition 4 (p. 8): this is an invariant of the sutured tangle; if T is braid-like (arcs can be oriented from D^2 x {0} to D^2 x {1}) it is Z-graded by u, because for that orientation the maps f_i^+ preserve u. T(1/0) unknotted implies braid-like (p. 10).

**Definition 10** ([W] p. 11). A = Kh<-(T_{K,h}), elements = sequences (x_j) with f_j(x_{j+1}) = x_j. K = subspace of sequences with x_j = 0 for j << 0. **kappa(K,h) := A/K.**

**Proposition 11** (p. 11): kappa(K,h) is a finite-dimensional Z-graded invariant of (K,h); any graded section gives injections iota_j : kappa -> A_j = Khr(T(j)) for every j.

**Stability** (Lemma 13, p. 13): with X = F in bigrading (c_T, (1-c_T)/2) a shifted copy of Khr(T(1/0)), up to an overall -n/2 in delta, Khr(T(n)) = H_*( Khr(T(0)) -> sum_{i=0}^{n} X[i,0] ) (as printed) with a differential of bidegree (1,1). Corollary 14: Khr(T(n+1)) = Khr(T(n)) + F for n >> 0. Corollary 15: f_i is surjective for i >> 0 and injective for i << 0. Consequence used repeatedly: Khr(T(n)) = kappa + F^m with the F^m in a single relative delta-grading (proof of Theorem 1, p. 15).

**Theorem 1** ([W] p. 3, proof pp. 14-15): kappa(K,h) = 0 if and only if K is the trivial knot. The "if" direction is the computation f_0 f_1 = 0 for the trivial tangle (T(n) = T(2,n-1)). The "only if" direction is not internal to Khovanov homology: kappa = 0 forces Khr(T(n)) thin of dimension n = det, the Ozsvath-Szabo spectral sequence then makes S^3_n(K) an L-space for all |n| >> 0 of both signs, hence g(K) = tau(K) = -tau(K) = 0.

**Mirror** (Proposition 12, p. 12): kappa^u((K,h)*) = kappa^{-u}(K,h); bigraded version Proposition 32 (p. 28): kappa^{u,2delta}((K,h)*) = kappa^{-u,-2delta}(K,h).

**Absolute bigrading** ([W] Section 7, p. 27): fix delta on kappa by requiring the potential generators of sum X[i,0] to lie in delta_W = +1/2 (2 delta = +1). Trefoil (right-handed): kappa of dimension 4 in u = -5, -3, -2, 0, 2delta = 1. Figure eight: u = 0, 2, 3, 5 at 2delta = -3 and u = 4, 6, 7, 9 at 2delta = -1.

**Curve description** ([KWZ] Definition 3.4, p. 8): s(K,h) := set of special components of Khr(T_{K,h});

    kappa(K,h) := HF( a(0), s(K,h) ).

[KWZ] p. 8 then asserts, with no proof and no reference ("One can show"), that this agrees as a relatively bigraded invariant with [W]'s kappa. The mechanism is visible in Counterexample 3.5 (p. 8): dim Khr(tau(n)) = dim kappa + dim HF(a(n), r_1(k)), the second term being dim Khr of the (2, n-k) torus link.

**Building block** ([KWZ] Definition 2.2, Lemma 2.3, Figures 7-8, pp. 5-6). V_kappa := the 4-dimensional bigraded space supported in delta = 0 and q = -5, -1, +1, +5. Lemma 2.3:

    HF(a(0), s_2(infinity))  = q^0 delta^{-1/2} h^{1/2} V_kappa,
    HF(a(0), s_{2n}(infinity)) = sum_{i=1}^{n} q^{4(2i-n-1)} delta^{-1/2} h^{1/2 + 2(2i-n-1)} V_kappa,

as absolutely bigraded spaces when the special curve is "symmetrically bigraded" (Figure 7: for s_{2n}, extreme h = ±(2n+1), extreme q = ±(4n+1), 8n generators in the idempotent of a(infinity)). Proof: dimension 4n = minimal intersection number, gradings by the path rule of [KWZ, Section 7]. V_kappa is [W]'s V = F^{(0)} + F^{(2)} + F^{(3)} + F^{(5)} in one delta-grading ([W] p. 25).

## 4. Structure of Khr(T_{K,h}) and BNr(T_{K,h})

What [KWZ] proves or states.

1. (p. 4) BNr(T) has exactly one non-compact component (no closed tangle components); Khr(T) has only compact components. Local systems are suppressed (trivial over F_2 in all known examples).
2. (p. 5) "Geography", stated as computational evidence, to be established elsewhere: every component of Khr(T) is linear; special components are s_n(p/q); rational components are r_n(p/q). Components of BNr(T) are "known to be much more complicated even when restricting to only compact components". arXiv:2105.06308v3 (theorem "Each component of Khr(T) is either rational or special", cited there from "Khovanov multicurves are linear", Theorem 1.2) records this as a theorem, with special curves s_{2n} in the doubled indexing.
3. (p. 7) Since tau(infinity) is the unknot, HF(a(infinity), Khr(T)) = F, so Khr(T) is homotopic to a multicurve meeting a(infinity) exactly once. Given the geography, Khr(T) "should be" special components of slope infinity plus a single rational component of integer slope.
4. **Theorem 3.1** (p. 7; computer verification with kht++, no proof beyond computation). For every strong inversion h on a knot K with at most 9 crossings,

       Khr(T_{K,h}) = r_1(k) union n copies of s_2(infinity),    k in 4Z, n in Z_{>0}.

   Table 1 (pp. 7-8) lists (k, n) for 82 rows; Section 4 (pp. 9-14) lists the absolutely bigraded kappa. 81 knots, 57 of them with two inversions, 138 inversions in total.
5. (p. 8, after Remark 3.2) The slope of the rational component need not be 0: it need not agree with the slope of the rational longitude.
6. Symmetry: nothing beyond [W] Propositions 12/32. **[digest]** In the data the six amphicheiral strongly invertible knots (4_1, 6_3, 8_3, 8_9, 8_12, 8_18) have their two inversions exchanged by (k; a_i, b_i) -> (-k; -a_i, -b_i).
7. Slope and shape of the non-compact component of BNr(T_{K,h}): **not addressed** in either paper. See Section 8 for what the kht++ data show.

What is not proved: any statement for all strongly invertible knots about which special components occur, about k, or about BNr. Theorem 3.1 is a finite verification.

## 5. Conjectures, questions, counterexample

- **Counterexample 3.5** ([KWZ] p. 8) to [W, Conjecture 29] (p. 26: dim kappa(K,h_1) = dim kappa(K,h_2) for two inversions on one knot): for 9_46, dim kappa(K,h_1) = 16 < 28 = dim kappa(K,h_2); (k,n) = (0,4) and (-4,7). Remark 3.2: 9_46 is the only knot up to 9 crossings whose two inversions are separated by the ungraded Khr(T); consequently dim Khr(tau_1(n)) != dim Khr(tau_2(n)) although the double covers agree (hyperbolic counterexamples to Ozsvath's question). For all knots with fewer than 9 crossings dim Khr(tau_1(p/q)) = dim Khr(tau_2(p/q)) (p. 3).
- **Conjecture 3.6** = [W, Conjecture 28] (p. 25): kappa(K,h) is a direct sum of shifted copies of V_kappa; in particular 4 | dim kappa. Verified up to 9 crossings by Theorem 3.1.
- Consequence drawn on p. 9: Conjecture 3.6 implies 4 | k. Argument: det(tau(0)) = |H_1(S^3_0(K))| = infinity so 0 = det(tau(0)) = |V(-1)| = |chi_delta HF(a(0), Khr(T))|; the special part comes in groups of 4 in single delta-gradings, the rational part lies in a single delta-grading.
- **Conjecture 3.7** (p. 9): every special component of Khr(T_{K,h}) is s_{2n}(infinity), n > 0 (even length). All tabulated examples have n = 1, but there exist (K,h) with s_{2n}(infinity), n != 1 (stated without example). Remark 3.9: expected for all four-ended tangles.
- **Questions 3.3** (p. 8): is there a geometric meaning of the slope k of the rational component? Is k always divisible by 4?
- **Question 3.8** = corrected [W, Question 19]: is there a hyperbolic knot with two strong inversions not distinguished by absolutely bigraded kappa? Up to 9 crossings absolutely bigraded kappa separates all pairs (p. 9). Hyperbolicity is needed: satellite examples related by mutation of a subtangle cannot be separated.
- **Remark 3.10** (p. 9): over other fields the conjectures fail. Khr(T_{7_4^2}; Z/3) = r_1(6) + 2 s_2(infinity) + 5 s_1(infinity).
- **Remark 4.1** (p. 10): Sakuma's diagram of 9_43 actually shows 9_22; the table uses the corrected knot.
- [W, Conjecture 30] (p. 26): a non-trivial strongly invertible K is an L-space knot iff kappa(K,h) is supported in a single delta-grading. Not discussed in [KWZ].
- Status after 2021: I did not check whether Conjectures 3.6/3.7 or Questions 3.3 have been settled.

## 6. Sakuma's eta polynomial

- [KWZ] does not mention eta. Sakuma is cited only for terminology, the numbering of inversions, and the erroneous 9_43 diagram.
- [W]: eta(K,h) is "an Alexander-like polynomial invariant" vanishing for the trivial knot (p. 4, p. 14) and for every amphicheiral K with unique inversion (Proposition 21 = Sakuma Prop. 3.4(1)); [W] offers kappa as the non-vanishing counterpart (Theorem 1). Values quoted: eta(9_9,h_1) = eta(9_9,h_2) = -2t^{-2} + 4 - 2t^2 (kappa separates them); eta(10_155,h_1) = 0, eta(10_155,h_2) = 2t^{-2} - 4 + 2t^2; eta(8_20,h) = 0 (kappa detects non-amphicheirality); eta(10_104,h) = -t^{-3} + t^{-2} - t^{-1} + 2 - t + t^2 - t^3 (Remark 27).
- No formula relating kappa or its Euler characteristic to eta appears in either paper.

## 7. Data: `data.json` (and `summary.tsv`)

All 138 inversions are extracted completely.

**From the paper** (TeX source of arXiv:2104.13592v1, auto-generated files):
- `computations/summary` (Table 1): k and n. A row with superscript star serves both inversions.
- `computations/gradings` (Section 4): each `\mynode{x}{y}{m}` stands for m summands h^{x+1/2} delta^{y+1/2} V_kappa. The half-unit offset comes from how the boxes are drawn; it is confirmed by the worked example kappa(4_1^1) = h^{2.5} delta^{5.5} V_kappa + h^{6.5} delta^{4.5} V_kappa (p. 10).
- Naming: K^i = i-th inversion in Sakuma's numbering; chirality follows Sakuma's table (3_1 is the left-hand trefoil, k = -4).
- Fields: `rational_component.slope_k`, `n_special`, `special_components[*].kappa_shift_h / kappa_shift_delta / multiplicity` and the four generators of each summand (h = a + {-5/2,-1/2,1/2,5/2}, q = 2(a+b) + {-5,-1,1,5}), `kappa_delta_support`.

**From [site]** (not in the paper): for each inversion the F_2 output of kht (v0.1, 7 March 2021) or kht++ (v0.1-56, February 2024), option -q (quotient tangle):
- `khtpp.input`: the kht++ string of the symmetric knot diagram.
- `khtpp.BNr_components`: every component of BNr(T) as a chain, with the bigrading of every generator.
- `khtpp.Khr_components`: every component of Khr(T) with recognised type (rational/special), slope (site and paper convention), chain, generator bigradings, and the site descriptor ("r(1/4) q^96/5 δ|^4": average q-grading and vertical delta-grading). This supplies the bigrading of r_1(k), which the paper omits.
- Chain conventions (kht++ Output page): generators ⬮ / ⬯ (recorded B / W); `—>` is D, `~>` is S between different idempotents and S^2 between equal ones, labels give other powers; a chain ending in an arrow is cyclic (compact). The printed bigrading is that of the first generator; for an arrow x -> y with label D^n: h(y) = h(x)+1, q(y) = q(x)+2n; with label S^m: h(y) = h(x)+1, q(y) = q(x)+m. W is the idempotent of a(0), B that of a(infinity) (matches [KWZ] Figure 7).

**Checks performed [digest]** (all pass for all 138):
- n from the gradings file = n in Table 1.
- [site] slopes and special-component bigradings reproduce Table 1 and the Section 4 table exactly (descriptor "q^X δ|^Y" of a special component gives b = Y - 1/2, a = X/2 - b).
- every special component has 12 generators and slope infinity; every rational component has length 1.
- |sum_i (-1)^{b_i - 1/2}| = |k|/4 (the determinant relation of [KWZ] p. 9).
- class of Khr = (q - q^{-1}) x class of BNr in the Grothendieck group; cyclic chains close up consistently in bigrading.

**Caveats.** (i) Five old pages (7_6^2, 8_6^1, 8_13^1, 8_21^1, 9_17^1) print the non-compact part of BNr as two chains (a 2-generator piece plus the rest); the gradings fit a single arc with one D-arrow missing from the printout. Flagged `BNr_arc_printed_as_two_chains`. (ii) The site also has Z/3, Z/5, Z/7, Z/11 and Q data, the 9_43-Sakuma tangle, and extra families (TorusKnotQuotient, BKM, ...); not extracted, raw pages are in `src/khtpp/examples`. (iii) No planar diagrams of the tangles are given anywhere except Figure 4 of [KWZ] and the kht++ strings.

Knots with at most six crossings (a_i, b_i = h- and delta-shift of each V_kappa summand; j, P_kappa, eta are defined in Section 8):

| (K,h) | k | n | j | (a_i, b_i) | P_kappa(q) | eta/(1-q^8) | BNr: arc gens / compact comps |
|---|---|---|---|---|---|---|---|
| 3_1 | -4 | 1 | 1 | (2.5, 4.5) | q^14 | - q^11 + q^13 - q^15 | 11 / 0 |
| 4_1^1 | 0 | 2 | 1 | (6.5, 4.5), (2.5, 5.5) | q^16 + q^22 | - q^13 + q^15 - q^17 | 13 / 0 |
| 4_1^2 | 0 | 2 | -1 | (-2.5, -5.5), (-6.5, -4.5) | -q^-22 - q^-16 | q^-25 - q^-23 + q^-21 | 13 / 0 |
| 5_1 | -8 | 2 | 1 | (-1.5, 4.5), (-0.5, 4.5) | q^6 - q^8 | - q^3 + 2q^5 - 2q^7 + q^9 - q^11 + q^13 - q^15 | 9 / 1 |
| 5_2^1 | -4 | 3 | 2 | (10.5, 8.5), (6.5, 9.5), (2.5, 10.5) | q^26 + q^32 + q^38 | - q^23 + q^25 - q^27 - q^35 + q^37 - q^39 | 23 / 0 |
| 5_2^2 | -4 | 3 | 0 | (-2.5, -0.5), (-6.5, 0.5), (-5.5, 0.5) | -q^-12 + q^-10 - q^-6 | q^-15 - 2q^-13 + 2q^-11 - q^-9 | 11 / 1 |
| 6_1^1 | 0 | 4 | 2 | (14.5, 8.5), (10.5, 9.5), (6.5, 10.5), (2.5, 11.5) | q^28 + q^34 + q^40 + q^46 | - q^25 + q^27 - q^29 - q^37 + q^39 - q^41 | 25 / 0 |
| 6_1^2 | 0 | 4 | 0 | (4.5, -1.5), (5.5, -1.5), (0.5, -0.5), (1.5, -0.5) | 1 - q^2 + q^6 - q^8 | - q^-3 + 2q^-1 - 2q + q^3 | 1 / 2 |
| 6_2^1 | -4 | 5 | 1 | (2.5, 4.5)x2, (3.5, 4.5), (-1.5, 5.5), (-0.5, 5.5) | q^8 - q^10 + 2q^14 - q^16 | - q^5 + 2q^7 - 2q^9 + q^13 - q^15 | 11 / 2 |
| 6_2^2 | -4 | 5 | 1 | (9.5, 2.5), (10.5, 2.5), (5.5, 3.5), (6.5, 3.5), (2.5, 4.5) | q^14 - q^18 + q^20 - q^24 + q^26 | - q^11 + q^13 - 2q^17 + 2q^19 - q^21 | 11 / 2 |
| 6_3^1 | 0 | 6 | -1 | (-2.5, -5.5), (-6.5, -4.5)x2, (-5.5, -4.5), (-10.5, -3.5), (-9.5, -3.5) | -q^-28 + q^-26 - 2q^-22 + q^-20 - q^-16 | q^-31 - 2q^-29 + 2q^-27 - q^-23 + q^-21 | 13 / 2 |
| 6_3^2 | 0 | 6 | 1 | (9.5, 3.5), (10.5, 3.5), (5.5, 4.5), (6.5, 4.5)x2, (2.5, 5.5) | q^16 - q^20 + 2q^22 - q^26 + q^28 | - q^13 + q^15 - 2q^19 + 2q^21 - q^23 | 13 / 2 |

Global statistics: k takes the values -16 (1 inversion), -12 (5), -8 (18), -4 (38), 0 (38), 4 (20), 8 (14), 12 (4); n ranges from 1 (3_1) to 37 (9_40); (k, absolutely bigraded kappa) takes 138 distinct values.

## 8. Decategorification of the data [digest]

None of this is in the papers; it is what the data say about the Jones polynomial. Scripts in `tools/`.

**Dictionary.** For a multicurve gamma let chi_B(gamma), chi_W(gamma) = sum over its generators in idempotent B, W of (-1)^h q^{q-grading}. Then, with the generator of each arc in bigrading (0,0),

    chi HF(a(0), gamma)        = [ chi_W (1 + q^-2) + chi_B q^-1 ] / (1 - q^-2),
    chi HF(a(infinity), gamma) = [ chi_B (1 + q^-2) + chi_W q^-1 ] / (1 - q^-2),

and the class of Khr(T) is (q - q^-1) times the class of BNr(T). Checked: the first formula applied to the symmetric s_2(infinity) of Figure 7 returns exactly q^-5 + q^-1 - q - q^5 with the signs of Lemma 2.3, and the second returns 0. Therefore, writing (chi_W, chi_B) for BNr(T),

    chi Khr(tau(infinity)) = chi_W + (q + q^-1) chi_B,     chi Khr(tau(0)) = (q + q^-1) chi_W + chi_B,

i.e. (chi_W, chi_B) is the Kauffman bracket vector of T in the basis (Q_0, Q_infinity), up to one overall unit and with q + q^-1 in the role of the loop value (the sign of -A^2 - A^-2 is absorbed by (-1)^h). Q_0 is the trivial quotient tangle: BNr(Q_0) = a(0) is one W generator, tau(infinity) is the unknot and tau(0) the two-component unlink. Independent check: a direct Temperley-Lieb computation of the bracket vector of the pretzel tangle P(-2,3) with six twists (the preferred quotient tangle of the trefoil, tau(0) = P(-2,3,6)) reproduces the site's (chi_W, chi_B) for 3_1 with q = A^{-2}, up to one overall unit (`tools/check_trefoil.py`).

**Results for all 138 inversions.**
1. chi Khr(tau(infinity)) = q^{24j} for an integer j in {-3,...,4}, not 1. So the absolute bigrading of kht++ and of the table in [KWZ] is the one in which the unknot closure sits in q^{24j} h^{8j}. My reading: the tangle is oriented with its two strands parallel (compatible with tau(0), not with tau(infinity)); then 4j = lk of the two components of tau(0) in that orientation. Consistent with (d/dq) chi Khr(tau(0)) at q=1 equal to 24j in all cases, and for the trefoil with the direct computation (lk = -4 in the other orientation).
2. Put **eta := chi_B(BNr(T))**. Then chi_W = q^{24j} - (q + q^-1) eta, so the bracket vector is

       [T_{K,h}] = q^{24j} [Q_0] + eta ( [Q_infinity] - (q + q^-1) [Q_0] ).

   eta = 0 exactly when [T_{K,h}] is a unit multiple of the class of the trivial tangle, i.e. when every rational closure has the Jones polynomial of the corresponding closure of the trivial tangle. **eta != 0 for all 138 inversions.**
3. eta is divisible by 1 - q^8 = 1 - t^4 in all 138 cases, and (eta/(1-q^8))(1) = -j.
4. With P_kappa(q) := sum_i (-1)^{a_i - 1/2} q^{2(a_i + b_i)}, so that chi(kappa) = P_kappa(q) (q^-5 + q^-1 - q - q^5):

       eta = - chi(kappa) / (q^2 + 1 + q^-2)  +  q^{24j+1} (1 - q^{2k}) / (1 + q^2)
           = - q^-3 (1 - q^2)(1 + q^4) P_kappa(q)  +  q^{24j+1} (1 - q^{2k}) / (1 + q^2).

   Verified for all 138. The first term is the contribution of the special components, the second that of r_1(k); the second vanishes exactly when k = 0.
5. Consequences: 2j = P_kappa(1) - k/4 (P_kappa(1) is the signed count of special components, sign = parity of the h-shift); chi(kappa) at q^2 = -1 has absolute value |k| (the determinant relation); eta = 0 would force j = 0. P_kappa != 0 for all 138; P_kappa(1) = 0 for 25 of them.
6. **Arc of BNr.** BNr(T_{K,h}) = one non-compact component plus between 0 and 18 compact components. It is a single arc and nothing else for 3_1, 4_1^1, 4_1^2, 5_2^1, 6_1^1, 7_2^1, 8_1^1, 9_2^1. The arc has exactly 1 + |k| + 6|P_kappa(1)| generators. It has the shape of the linear arc a(k) (one W generator, |k| B generators) exactly for the 25 inversions with P_kappa(1) = 0; for the 12 inversions with k = 0 = j (6_1^2, 8_3^1, 8_3^2, 8_8^1, 8_9^1, 8_9^2, 8_20, 9_19^1, 9_27^2, 9_42, 9_44, 9_46^1) it is a(0) with its generator in bigrading (0,0), the arc of the trivial tangle. Otherwise it is not linear (trefoil: 11 generators, 3 W and 8 B). With its absolute bigrading the arc depends only on (k, j) for 137 inversions; the exception is 9_46^2, whose arc contains a D^2 arrow. Table in `data.json`, `meta.arc_classes`.

## 9. Claim checks

**C1** (one component of Khr(T_{K,h}) meets the unknot-slope arc once; all others are compact curves of the unknot slope along the lattice line through the special puncture). **Confirmed, with scope.** "Meets a(infinity) once" is [KWZ] p. 7, a consequence of HF(a(infinity), Khr(T)) = F. That the other components are special of slope infinity and the remaining one is r_1(k), k integer, is Theorem 3.1 for at most 9 crossings (computer); in general [KWZ] derives it from geography statements that were conjectural there and are cited as a theorem in arXiv:2105.06308v3. All components of Khr are compact, including the one meeting the arc.

**C2** (Watson's kappa corresponds to the compact special part; nonzero exactly for nontrivial inversions). **Confirmed, with a gap in the written record.** kappa = HF(a(0), special components) is Definition 3.4; agreement with [W]'s inverse-limit quotient is asserted without proof on p. 8, and only as relatively bigraded invariants. Non-vanishing is [W, Theorem 1], whose proof uses the Ozsvath-Szabo spectral sequence and L-space surgeries.

**C3** (chi(kappa) = unit x universal factor x coefficient x; "Jones detects the trivial inversion" iff chi(kappa) != 0). **Modified.** Neither paper discusses the graded Euler characteristic of kappa, the Kauffman bracket, or Jones polynomials of closures; the only decategorified statements are det = |chi_delta| ([W] p. 5) and 0 = det(tau(0)) = |V(-1)| = |chi_delta HF(a(0), Khr(T))| ([KWZ] p. 9). From the data (Section 8, item 4): the coefficient that vanishes iff [T] is a unit times the trivial class is eta = -chi(kappa)/(q^2+1+q^-2) + q^{24j+1}(1-q^{2k})/(1+q^2). So x is proportional to chi(kappa), with universal factor -(q^2+1+q^-2), **only when k = 0** (38 of 138 inversions). For k != 0, chi(kappa) != 0 is automatic (its value at q^2 = -1 is ±k) and does not imply x != 0; the correct criterion is chi(kappa) != q^{24j+1}(q^2+1+q^-2)(1-q^{2k})/(1+q^2). The implication "x != 0 for all nontrivial inversions implies chi(kappa) != 0 for all" does hold. Verified directly on the trefoil (k = -4): eta/((1-q^2)(1+q^4)) = -q^11 - q^17, one monomial from kappa and one from r_1(-4). In the notation [T] = x id + y e of the brief, x is eta provided e denotes the class of the trivial quotient tangle Q_0 (the generator whose unknot-slope closure is one circle); I could not check the mathematician's own normalisation.

**C4** (delta-gradings supporting kappa). **Unrestricted in number, contiguous in all data.** [W, Theorem 18] (p. 19): for torus knots kappa lies in a single delta-grading and dim kappa <= |pq| - 1. [W, Conjecture 30]: single delta-grading iff L-space knot. Under Conjecture 3.6 each V_kappa summand is delta-homogeneous but different summands may differ. Data up to 9 crossings: number of delta-gradings = 1 for 5 inversions (3_1, 5_1, 7_1, 9_1, 8_19: the torus knots), 2 for 17 (smallest: 4_1, delta = 4.5, 5.5; in [W] 2delta = -3, -1), 3 for 31 (smallest 5_2^1), 4 for 42 (6_1^1), 5 for 30 (7_2^1), 6 for 12 (8_1^1), 7 for 1 (9_2^1). The support is always a set of consecutive delta-gradings. The complementary summand of Khr(tau(n)) lies in a single delta-grading ([W, Lemma 13]).

## 10. Surprises and open points

- The kht++ site holds the full bigraded BNr and Khr of all 138 quotient tangles; the paper prints only (k, n) and kappa.
- The absolute bigrading of the paper's kappa table is shifted by q^{24j} h^{8j} relative to the normalisation in which the unknot closure is in bigrading 0, and by delta = 4j relative to [W]; the paper mentions only a sign and a factor 2.
- eta is divisible by 1 - t^4 and the arc of BNr is governed by (k, j) alone, except for 9_46^2.
- The examples index of the site lists a folder "Jones/Thistlethwaite"; the page returns 404.
- Open: a proof of the kappa identification of [KWZ] p. 8; a topological meaning of k (Questions 3.3) and of j beyond lk(tau(0))/4; whether item 4 of Section 8 follows formally from Theorem 3.1-type structure (it should, by additivity of Euler characteristics, but I only verified it numerically); whether Conjectures 3.6, 3.7 have been proved since 2021.

## Files

- `/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/REPORT.md`
- `/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/data.json` (138 records; `meta` documents every field and convention)
- `/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/summary.tsv` (one line per inversion)
- `/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/tools/` (parsers and checks; run with `python3 -I`)
- `/Users/calebbarnett/jones-lanes/theory-restart/lit/kwz-inversions/src/` (arXiv sources and PDFs, kht++ pages)
