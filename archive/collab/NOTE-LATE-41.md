# The LATE-41 theorem: uniqueness of rational solutions of framed tangle equations, and its unframed extension

Note for Caleb, written by Claude on 2026-11-03 from the project's authoritative files: `outputs/rational-tangle-uniqueness-audited-proof.txt` (Astra, 1 Nov 2026), `outputs/rational-tangle-uniqueness-audit.txt` and `work/final-audit/{surgery,floer,novelty}.txt` (Astra's audits, 1 Nov), `collab/audits/LATE-41-audit.md` (my six-referee audit, 2 Nov), and `work/big_reductions/surgery.md` (Astra's unframed extension, 3 Nov, checked by me the same morning). Status in one line: a complete deduction from published results, audited internally several times with no gap found, with a method antecedent (Gainullin 2018) that must be credited, and with priority unverified; Sikora's own talk of 15 October 2026 still states the framed statement as a conjecture.

## 1. What the theorem says and why it matters

A two-string tangle is a pair of arcs in a ball meeting the boundary in four marked points. Given a tangle X and a rational tangle P (one of Conway's fractions), the closure C_P(X) is the link obtained by gluing P to X along the four points; in Sikora's notation this is N(X + P). A tangle equation asks which X have a prescribed closure. Sikora's paper (Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed rationals, Canad. J. Math. 76 (2024), arXiv:2005.08162) sets up the framed version: the ambient balls are oriented, links are considered up to balanced framed isotopy, and the Kauffman bracket of a tangle lives in a rank-two module with basis the two trivial tangles, so that the bracket of every closure is a linear functional of the bracket vector [X].

Sikora proves two things we use. Theorem 21: two closure functionals with distinct underlying unframed slopes determine the bracket vector. Corollary 20: balanced framed rational tangles are distinguished by their bracket vectors. He conjectures (Conjecture 2 in arXiv v2, Conjecture 1.2 in the journal):

**Conjecture (framed rational-solution uniqueness).** Let P, Q be framed rational closing tangles with distinct unframed slopes, R a framed rational tangle, X an arbitrary framed two-string tangle with the same boundary marking. If C_P(X) = C_P(R) and C_Q(X) = C_Q(R) as balanced framed links, then X = R as balanced framed tangles.

Sikora also shows that Jones unknot detection implies this conjecture. The converse is not claimed and does not follow; see Section 6. The point of the conjecture is that a system of two framed tangle equations with a rational solution has no other solution among all tangles whatsoever (uniqueness among rational tangles alone is his Proposition 1, an easier statement).

LATE-41 is Astra's proof of the conjecture. The hypotheses are actual link isotopies, which is why the proof can use surgery theory and Floer theory on the double branched covers.

## 2. The objects in the cover

Let V be the double branched cover of the ball over R and M the double branched cover over X. Since R is rational, V is a solid torus. The common boundary marking identifies the slope lattices of the two boundary tori, and the double cover of a closure C_P is the Dehn filling along the lift of the slope of P: C_P(X) has cover M(p), C_P(R) has cover V(p). An orientation-preserving link isotopy lifts to an orientation-preserving homeomorphism of the covers (not necessarily preserving the filling cores). The determinant of a link equals the order of the first homology of its double branched cover, with determinant 0 meaning infinite homology.

Two slopes are fixed once and for all: lambda, the slope that bounds a disk in V, so that V(lambda) = S^1 x S^2 and C_lambda(R) is the two-component unlink; and mu, a slope meeting lambda once and distinct from both probes, so that V(mu) = S^3 and C_mu(R) is an unknot. Choosing mu before anything else matters, because the auxiliary manifold Y = M(mu) and its core knot K are defined in terms of it.

## 3. The proof in five steps

**Step 1 (bracket vector).** By Theorem 21 the two equations give [X] = [R]. Hence every rational closure of X has the same bracket as the corresponding closure of R, in particular the same determinant. Normalisation matters here: use the reduced bracket with unknot value 1, evaluate its absolute value at A = exp(i pi/4); this is the determinant, and the framing units have absolute value one there.

**Step 2 (integral peripheral data, no closed components, irreducibility).** The mu-closure of X has determinant 1 and the lambda-closure has determinant 0. A link with c components has determinant divisible by 2^(c-1) (Stoimenow), so the determinant-one closure is a knot, so X has no closed components (a closed component of X would survive into every closure). Therefore Y = M(mu) is an integral homology sphere and M, the exterior of its core K, has H_1(M) = Z and H_2(M) = 0. For a knot in an integral homology sphere the unique filling slope with infinite homology is the preferred longitude, so the determinant-zero slope lambda is the preferred longitude of K, and mu, lambda form a common meridian-longitude basis for M and V. Nothing says Y is S^3, and nothing says Y is an L-space; the proof never needs either. At most one of the two probes is lambda, so at least one probe gives an actual rational-link closure, whose cover is an actual lens space (possibly S^3): M has an actual lens-space filling. This makes M irreducible: a closed summand in a prime decomposition would have trivial first homology (since H_1(M) = Z and the boundary piece already carries b_1 at least 1), would survive every filling, and would then be a homology-sphere summand of a lens space, hence S^3; a nonseparating sphere is excluded by H_2(M) = 0.

**Step 3 (both probes nonlongitudinal).** Write the probe slopes as alpha_i = p_i mu + q_i lambda with p_i nonzero; distinctness gives q_1/p_1 different from q_2/p_2. The actual isotopies lift to orientation-preserving homeomorphisms

    Y_{p_i/q_i}(K) = S^3_{p_i/q_i}(U),   i = 1, 2,

with the same signed coefficients on both sides. This is the most delicate point and the one the audits spent most time on: the boundary identification preserves orientation, both covers carry the orientation of the same oriented ball, the two lifts of the marking differ by the deck involution, which acts as minus the identity on boundary homology and so changes (p, q) to (-p, -q) without changing p/q, and Step 2 has identified both the longitude and the chosen meridian. So there is no hidden shear or sign between the two exteriors.

Now apply the Casson-Walker surgery formula (Boyer-Lines; in the form of Ni-Wu, Proposition 3.1, which is stated for null-homologous knots in rational homology spheres, exactly the situation here) to both equalities. The lens-space terms cancel and what remains is

    0 = lambda_CW(Y) + (q_i / (2 p_i)) Delta_K''(1),   i = 1, 2,

with Delta_K symmetric and normalised by Delta_K(1) = 1. Subtracting the two equations eliminates the unknown lambda_CW(Y) and gives Delta_K''(1) = 0.

Both fillings are lens spaces, hence L-spaces, so by Rasmussen-Rasmussen (Floer simple manifolds and L-space intervals, Adv. Math. 2017, Proposition 1.3) M is Floer simple. Their Proposition 1.4 and Section 2.1 then give the normal form of the torsion: tau(M) = D(t)/(1 - t) = sum a_n t^n with a_0 = 1, each a_n in {0, 1}, and a_n = 1 for large n; since H_1(M) = Z, D is the polynomial normalisation of Delta_K and RR's projected polynomial is D itself. The coefficients of D are the differences a_n - a_(n-1), so the nonzero coefficients of Delta_K alternate +1, -1, ..., +1 and the central one is present:

    Delta_K(t) = (-1)^k + sum_{j=1}^{k} (-1)^{k-j} (t^{n_j} + t^{-n_j}),   0 < n_1 < ... < n_k.

Then Delta_K''(1) = 2 sum_j (-1)^{k-j} n_j^2, which is a sum of positive differences of squares (plus a lone positive square when k is odd), hence strictly positive unless k = 0. So Delta_K = 1. An independent cross-check in the audit writes D = 1 + (t - 1) sum_{n in E} t^n for the finite set E of zero coefficients and gets Delta_K''(1) at least 2|E|, with the same conclusion.

Finally, if the boundary of M were incompressible, RR's Corollary 2.3 would compute the Thurston norm of a generator of H_2(M, boundary) as degree(D) - 1 = -1, which is impossible. So the boundary compresses; an irreducible manifold with one torus boundary component and a compressing disk is a solid torus.

**Step 4 (one probe is lambda).** Then the shared closure at that probe is the two-component unlink, so M(lambda) = S^1 x S^2, and the other probe gives an L-space filling. RR Proposition 7.8 says the exterior of a knot in S^1 x S^2 with an L-space surgery is a generalised solid torus; in their Definition 7.2 the order g_M of the homological longitude in H_1(M) is 1 here (the longitude is null-homologous and H_1(M) = Z), and the definition bounds degree(projected Delta) below g_M = 1, so the polynomial has degree zero. Corollary 2.3 gives the same norm contradiction, the boundary compresses, and irreducibility from Step 2 makes M a solid torus. The earlier version of this step went through Ni-Vafaee and capping off a fibre; it was valid but longer. The proof does not claim that every generalised solid torus is a solid torus; torsion-free homology and irreducibility are what make it one here.

**Step 5 (back to the tangle).** A two-string tangle whose double branched cover is a solid torus is rational (Lickorish 1981; the criterion is recorded in Buck-Mauricio, Theorem 3.5(2)), applied to the given cover and its given deck involution. Then [X] = [R] and Sikora's Corollary 20 give X = R as balanced framed tangles with the required marking. End of proof.

## 4. Why each hypothesis is needed

The audit's stress tests explain the shape of the argument.

- A solid torus connected-summed with a nontrivial integral homology sphere that is an L-space has H_1 = Z, Delta = 1 and many L-space fillings, yet is not a solid torus. It is reducible, and its fillings keep the closed summand, so they are never the actual lens spaces the hypotheses supply. This is why Step 2 proves irreducibility from an actual lens filling; Floer simplicity alone would leave this case open.
- A trefoil exterior has H_1 = Z and is Floer simple, with Delta = t - 1 + t^(-1) and Delta''(1) = 2. Two lens fillings alone do not force a solid torus; the matched-surgery constraint Delta''(1) = 0 from two equations is what kills it.
- The familiar irreducible generalised solid tori that are not solid tori have homological torsion, excluded here by H_1(M) = Z.
- Homology orders alone, or unoriented lens-space identifications, would not justify the signed Casson-Walker comparison. Actual oriented isotopies are used.
- A hypothetical nontrivial knot with Jones polynomial 1, tied locally into R, would preserve every bracket while destroying the actual closures. This is why the theorem does not prove Jones unknot detection (Section 6).

## 5. The unframed extension of 3 November (RB-HOM3, RB-3PROBE, RB-ARITH)

Astra's pass of 3 November replaced the framed hypotheses by unframed ones plus a single number, through an elementary lemma that recovers the integral peripheral data from determinants alone. I checked the lemma from scratch the same morning.

**Lemma (homology interpolation).** Let M be a compact connected oriented 3-manifold with one torus boundary and V a marked solid torus with the same slope lattice. Put h(Y) = |H_1(Y)| when finite and h(Y) = 0 otherwise. If h(M(alpha)) = h(V(alpha)) for three distinct slopes, then H_1(M) = Z and the two integral boundary functionals agree up to sign; in particular M and V have the same longitude.

Proof. One finite filling gives b_1(M) = 1 (half lives, half dies). Write H_1(M) = Z + T with T finite and let ell be the composite H_1(boundary) -> H_1(M) -> Z, an integral functional, not necessarily primitive. Filling along alpha kills its class, and (Z + T)/<(n, t)> has order |n| |T| for n = ell(alpha) nonzero and is infinite for n = 0; so h(M(alpha)) = |T| |ell(alpha)|. Put m = |T| ell and let l be the primitive functional of V. The three equalities say that the quadratic form m^2 - l^2 = (m - l)(m + l) vanishes on three pairwise independent integer vectors; one of the two linear factors then vanishes on two independent vectors, hence identically; so m = plus or minus l, and primitivity of l forces |T| = 1 and ell primitive, with kernel the disk slope of V. QED.

**Theorem (unframed three-probe rigidity).** Let R be a rational two-string tangle and X any two-string tangle in the same marked ball. Suppose that at two distinct slopes alpha, beta, nonlongitudinal for R, the unframed closures of X are ambient isotopic to those of R, and that at a third distinct slope gamma the determinants agree. Then X = R as unframed marked tangles. In particular three actual unframed closure equalities suffice, since at most one slope is longitudinal.

Proof. The determinants at alpha, beta, gamma agree (two from the isotopies, one by hypothesis), so the lemma gives H_1(M) = Z and the longitude, with no framing input. The two actual isotopies are then exactly the input of Step 3 above, with the Seifert longitude already in hand, and Steps 3 and 5 finish; this route never uses RR Proposition 7.8. QED.

Two corollaries are worth recording. First, a sharp diagnostic: if a nonrational X satisfies two actual nonlongitudinal closure equalities with a rational R, its determinants differ from R's at every other slope, so one more determinant anywhere separates the entire alternative. Second, an arithmetic two-probe statement: with d the distance between the two probe slopes, if d does not divide twice the common determinant of either matched closure, two actual nonlongitudinal equalities already force X = R; the only alternative homology functional is m* = (u, -v - 2au/d) in suitable coordinates, integral only when d divides 2u. The calibration against the known two-probe rival is instructive: the Ernst-Sumners example X = <-1> + <1/2> + <1/3> against R = <1/4> has N(X) = N(R) = U and N(X + <1>) = N(R + <1>) = T(2,-5) with X nonrational; its determinants at add-on <p/q> are |6p - q| against |4p + q|, whose squares differ by 20 p (p - q), vanishing exactly at the two shared closures and nowhere else, as the diagnostic predicts. In this example the probes are at distance one, so the arithmetic criterion correctly stays silent; and the unknot-closure case at distance at least three may already follow from older rational-subtangle-replacement classifications (Baker-Buck), so that special case should not be advertised as new.

## 6. Relation to Jones unknot detection and to Lemma Q

The theorem converts actual topology at two slopes, plus scalar data, into rationality. Jones data supply the scalars: if the id-coefficient of a crossing complement vanishes and one closure is an actual unknot, every rational closure has the determinant of the corresponding closure of the trivial tangle, so the lemma recovers H_1 = Z and the Seifert longitude for free (this is the zero-surgery description of the double cover of the band-move link that the overnight work already had). What Jones data cannot supply is a second actual lens-space filling; polynomial equality is not link isotopy, and the local-knotting example of Section 4 shows no polynomial argument can bridge that gap. Sikora proves that Jones detection implies the framed conjecture; proving the consequent does not establish the antecedent. This is the precise sense in which LATE-41 is a theorem about tangle equations; it leaves the unknot conjecture where it was.

## 7. Prior art, novelty, status

- Method antecedent: Gainullin, Heegaard Floer homology and knots determined by their complements, Algebr. Geom. Topol. 18 (2018), Theorem 8.2, already runs the chain surgery comparison, Casson-Walker, vanishing second derivative, alternating L-space Alexander form, genus detection. His hypotheses include an ambient L-space; here the auxiliary Y is only an integral homology sphere, and two matched equations plus Floer simplicity of the exterior replace that assumption. Any write-up must credit this.
- The unknot-product special case (one shared closure an unknot) is close to the surgery characterisation of the unknot (Kronheimer-Mrowka-Ozsvath-Szabo) and should not be presented as new surgery rigidity.
- Two-closure rigidity for 4-plat closures is an old theme (Ernst-Sumners 1990 with the cyclic surgery theorem; Buck-Mauricio; Baker-Buck). The EARLY-25 example above shows two unframed closure equalities alone do not suffice in general; the third determinant is what the unframed theorem adds.
- The framed statement was still called the Uniqueness of Rational Solutions Conjecture in Sikora's IPAM talk of 15 October 2026 (abstract read; recording not reviewed). No prior exact proof was located in the bounded searches. This is evidence of open status; a priority certificate would need more.
- Audits: Astra's three-agent audit of 1 November (surgery, Floer, novelty) found no fatal gap; my six-referee audit of 2 November returned "valid with minor revisions", confidence medium-high, with one false shortcut removed (Sikora Proposition 10(1) must not be used; it is false) and the required fixes incorporated in the audited file. The 3 November unframed extension was checked by me step by step. None of this is external specialist review.

Recommended wording, from the audit: a candidate deduction of Sikora's framed rational-solution uniqueness conjecture from published surgery and Floer-theoretic results, with an unframed extension; no fatal gap found in repeated internal audits; external review and priority pending. Any outward step (contacting Sikora, posting) is Caleb's call.

## References

- A. S. Sikora, Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed rationals, Canad. J. Math. 76 (2024) 707-727; arXiv:2005.08162v2. Conjecture 2 (journal 1.2), Section 4, Corollary 20, Theorem 21.
- J. Rasmussen and S. D. Rasmussen, Floer simple manifolds and L-space intervals, Adv. Math. 322 (2017) 738-805; arXiv:1508.05900. Propositions 1.3, 1.4, 7.8; Corollary 2.3; Definition 7.2.
- Y. Ni and Z. Wu, Cosmetic surgeries on knots in S^3, J. reine angew. Math. 706 (2015), Proposition 3.1 (Casson-Walker surgery formula, after Boyer-Lines).
- F. Gainullin, Heegaard Floer homology and knots determined by their complements, Algebr. Geom. Topol. 18 (2018) 69-109, Theorem 8.2.
- D. Buck and M. Mauricio, Tangle solutions for composite knots, arXiv:1007.0948, Theorem 3.5(2) (Lickorish's solid-torus criterion).
- A. Stoimenow, Square numbers, spanning trees and invariants of achiral knots, Comm. Anal. Geom. 13 (2005), Proposition 6.5.
- O. Dasbach, D. Futer, E. Kalfagianni, X.-S. Lin, N. Stoltzfus, Alternating sum formulae for the determinant and other link invariants, Section 3.
- P. Kronheimer, T. Mrowka, P. Ozsvath, Z. Szabo, Monopoles and lens space surgeries, Ann. of Math. 165 (2007).
- C. Ernst and D. W. Sumners, A calculus for rational tangles, Math. Proc. Camb. Phil. Soc. 108 (1990); K. Baker and D. Buck, The classification of rational subtangle replacements between rational tangles, Algebr. Geom. Topol. 13 (2013).
- A. Sikora, IPAM talk, 15 October 2026, https://www.mathinstitutes.org/videos/25091.
