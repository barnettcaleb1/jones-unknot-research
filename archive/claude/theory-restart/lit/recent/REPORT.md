# REPORT: status scan June-November 2026 (brief "recent")

Status: COMPLETE (scan date 2026-11-15). Author of this digest: research-assistant agent.
Raw material: `src/` (arXiv TeX sources by id, PDFs in `src/pdf`, arXiv API result files `src/api*.xml`,
IPAM schedule fragments in `src/ipam`, McMullen preprint in `src/mcmullen`, K3 problem list in `src/k3`).
Small sanity scripts written by me: `check/t2n.py`, `check/squier_sig.py`, `check/coshcheck.py` (pure Python, outputs quoted below).

Conventions used below. V_K(t): Jones polynomial with V(unknot)=1 and skein t^{-1}V_+ - tV_- = (t^{1/2}-t^{-1/2})V_0.
Reduced Burau of B_3: s_1 -> [[-t,1],[0,1]], s_2 -> [[1,0],[t,-t]] (any equivalent convention; t -> 1/t and transposes do not affect the statements).
q-deformed modular group (Morier-Genoud-Ovsienko): R_q = [[q,1],[0,1]], S_q = [[0,-1/q],[1,0]]; projectively this is reduced Burau of B_3 at t = -q
(Morier-Genoud-Ovsienko-Veselov, IMRN 2024). "Items I did not read in full text" are flagged [NOT READ].

---------------------------------------------------------------------------------------------------

## 0. Summary of findings

1. BBB (arXiv:2607.05283): two versions (v1 6 Jul 2026, v2 14 Sep 2026). No withdrawal, no erratum, no published comment or response found.
   The v2 comment says "Minor corrections and improved exposition", but the TeX diff shows a mathematically substantive repair in Section 6.3
   (three new lemmas replacing a "without loss of generality" paragraph) and a new case in Section 5. Publicly the result is being reported as settled
   (Columbia Math news 3 Aug 2026; cited as an announcement in arXiv:2611.10850). No independent verification located.
2. Carmi-Cohen (arXiv:2606.22410): v1 only (21 Jun 2026), math.GM, no withdrawal, no response found. It claims the Jones unknot conjecture and the
   Vassiliev unknot-detection conjecture. From a partial read: the proof uses nontriviality of K only to pick a diagram with a non-nugatory crossing;
   everything else would apply verbatim to a non-minimal diagram of the unknot, where the conclusion is false. So it should be treated as unverified
   and very probably incorrect (my assessment; no public referee statement exists).
3. Jost-Lewark (arXiv:2601.16588): v1 only. Theorem 1.1: V_K(e^{2 pi i/6}) is determined by H_1 of the double branched cover with its linking pairing.
   Not a detection result. For the K_n of the brief (double cover an integral homology sphere) it gives V_{K_n}(e^{2 pi i/6}) = 1, no information.
4. Sikora, IPAM, Thursday 15 Oct 2026, 16:00-16:45: "Tangle Equations, the Jones Unknot Conjecture, and Lens Space Surgeries." Abstract recorded in 1.4.
   No new Sikora arXiv paper on this in 2026 was found.
5. S1 (colored Jones and the unknot): claimed by Andersen, arXiv:1206.2785 (2012, v1 only, never located in a journal; the last section is a sketch
   with an explicit unverified nondegeneracy assumption). The K3 problem list (Baykur-Kirby-Ruberman, AMS, 2020s) lists it as OPEN (Problem 1.24(b)).
   Conditional: follows from the AJ conjecture (Dunfield-Garoufalidis Cor. 1.3) and from the Volume Conjecture (Murakami-Murakami, Section 5).
6. S2 (Vassiliev invariants and the unknot): open (Vassiliev's conjecture); S1 implies S2. Only the Carmi-Cohen preprint claims it.
7. S3: the statement "projective image of B_3 under reduced Burau at -t = e^{+-2 pi i/n}, n >= 7, is the Fuchsian (2,3,n) triangle group" IS in the
   literature: McMullen, Braid groups and Hodge theory, Section 5 (Examples: n = 3); Funar-Kohno Props 3.3-3.5; Miyamoto arXiv:2609.33703 Thm 3.2 and
   Prop 3.7 (Sep 2026). I found no published cosh-distance formula for Jones values of two-bridge links, and no published claim that one root of
   unity detects the unknot among two-bridge knots. Such a claim would be false: V_{T(2,2m-1)}(t) = 1 for every t with t^m = 1, t != +-1, m >= 3
   (classical t_k-move phenomenon, Przytycki 1988; exact identity, verified numerically).

---------------------------------------------------------------------------------------------------

## 1. Recent papers and announcements

### 1.1 Bharathram, Birman, Brendle, arXiv:2607.05283 (read: TeX of v1 and v2; PDF of v2 for numbering)

Versions. v1 Mon 6 Jul 2026 (title in TeX "The Burau representation is faithful for n = 4"); v2 Mon 14 Sep 2026 (arXiv title "The Burau representation
of the braid group is faithful for n = 4"; comment: "28 pages, 32 figures. Minor corrections and improved exposition"). math.GT, math.GR. No journal
reference. No withdrawal, no erratum.

Statements (v2 numbering). Main theorem (Introduction): the reduced Burau representation rho_4 of B_4 is faithful. Corollary 1.1 (p. 2): the Jones
representation of B_4 is faithful (with a pointer to Kasahara, Remark 5.6). Proposition 1.2 (p. 2): faithfulness on the Brunnian subgroup Brun_4
implies faithfulness on B_4. Theorems 2.2, 2.3 (Moody; p. 5): if the Moody polynomial M_{Phi.Gamma} differs from M_Gamma for some Gamma in B_n then
Phi is not in ker rho_n. Proposition 5.1 (p. 12): for Phi in K_n and a proper product Phi.Gamma, the arcs (beta)Gamma and alpha are in minimal position.
Proposition 6.7 (p. 20): for Phi in B_4 a proper product Phi'.Gamma_1 there is a push-map Gamma in K_5 with f(Phi).Gamma a proper product in B_5 and both
f(Phi).Gamma and Gamma satisfying the parity condition, with unequal intersection numbers. Corollary 6.8 (p. 24), Theorem 6.9 (p. 24): rho_4 is faithful
on Brun_4. The argument passes through B_5 (f: B_4 -> B_5 adds a puncture), where Burau is known to be unfaithful, and uses Theorem 2.3 there.

v1 -> v2 diff (my diff of the two TeX files; 1031 -> 1182 lines, 213 diff lines):
- Section 5: a new class of bigon-forming configurations is added, "generalized bigons/trigons/rectangles with basepoint" (with a new figure), and the
  list in the sentence before the minimal-position lemma is amended to "... rectangles, possibly with basepoint". In the proof of Prop. 5.1 a single
  sentence is added: the proof is written only for the old cases and "goes through when adding in each case with basepoint".
- Section 6.3 (Embedding in B_5): three lemmas are new in v2: Lemma 6.4 ("4-disks become 5-disks" for a loop disjoint from beta modulo 4-disks),
  Lemma 6.5 (alternation of signs of Gamma with beta_*^3 modulo 4-disks for loops "properly simple modulo 4-disks"), Lemma 6.6 (such a loop satisfies
  the parity condition), with new definitions ("disjoint from beta modulo 4-disks", "simple modulo 4-disks", "properly simple modulo 4-disks").
  In the proof of Prop. 6.7 the v1 paragraph that derived the parity condition for Gamma from "we may further assume without loss of generality that
  each alpha-gamma_1 disk is equivalent to one of the five disks ...; otherwise we could have made a different choice of gamma_1" is commented out in
  the v2 source and replaced by an appeal to Lemma 6.6 ("condition (1) is immediately satisfied by the constriction [sic] ...").
- Acknowledgements: Khalid Bou-Rabee added. Both versions state "AI was used to proofread a draft of the manuscript."
Judgement: v2 repairs a step of v1 that was not justified; the repair is itself stated tersely (conditions (1)-(3) of "properly simple" are asserted
for the constructed Gamma in two lines). Whether v2 is complete cannot be decided from a status scan. Relation to T: by Bigelow (2002) and Ito (2015)
[NOT READ in this scan, from memory] a nontrivial kernel of Burau_4 would give a nontrivial knot with V = 1; the converse direction is not known, so
faithfulness of Burau_4, even if established, does not imply T.

Responses found: none critical. Columbia Mathematics news item dated 3 Aug 2026 ("resolved the last remaining open case"), social-media posts,
nLab reference list entry, arXiv:2611.10850 (Pourkia, 7 Nov 2026) which calls it a 2026 announcement. No MathOverflow thread, no comment paper, no
erratum. Related 2026 arXiv items: 2608.29147 (Shimizu-Yaguchi, crossing matrix and Burau matrix of pure braids), 2608.08079 (E-Haridas, multivariate
Burau), 2611.10850 (Pourkia: a "non-homogeneous" local representation that detects Bigelow's B_5 kernel element).

### 1.2 Carmi, Cohen, arXiv:2606.22410 "On trivial Jones--Vassiliev polynomials" (read: TeX v1, partially; PDF v1 for numbering)

Versions. v1 only, Sun 21 Jun 2026; primary class math.GM (General Mathematics); 62 pages; no withdrawal; no journal reference; no response located.
The source file is `main_machines_21_06_26_final.tex`, 9826 lines of which a large part is commented-out earlier drafts; there are two "Unknot detection"
subsections (the second under a disabled \if).

Definitions and statements (PDF numbering).
- Lemma 3.1 (p. 13), "JVP": with p := x - x^{-1} (x = t^{1/2}), the class of V_K(x) in Z[p][x]/(x^2 - p x - 1) has a unique expansion
  V_K(x,p) = sum_{q>=0} (a_q(K) + b_q(K) x) p^q with integers a_q, b_q, and a_q, b_q are Vassiliev invariants of order <= q.
  K is "J_m-trivial" if a_q = b_q = 0 for 1 <= q <= m-1; "p-constant" if a_q = b_q = 0 for all q >= 1 (for knots: V_K = 1).
- Corollary 3.7 (p. 13): for an n-crossing diagram of an l-component link, a_q = b_q = 0 for q > 3n + l - 1.
- Theorem 5.11 (p. 36), "facewise two-clasping descent": D a crossing-minimal diagram of K, B_0 = 3c(K), \hat B = B_0 + kappa_mach (= 3c(K)+11);
  plant two "clasping twist machines" of odd residual lengths > \hat B + 2 at crossings u != v; assume (C1)-(C4), (H1) and f_r(K) = 0 for
  1 <= r <= \hat B + 2; then the JVP layers of order >= 2 vanish on the two-crossing sign face F_u x F_v (in particular a_2 = b_2 = 0 at all four
  sign choices of u, v).
- Lemma 6.4 (p. 49): every non-nugatory crossing u of a knot diagram has an "admissible witness" v (a crossing between the two components of the
  oriented smoothing at u).
- Theorem 6.8 (p. 50), "triviality barrier": a nontrivial J_N-trivial knot has N <= 3c(K).
- Theorem 6.9 (p. 53): V_K = 1 implies K is the unknot. Corollary 6.10 (p. 54): a knot that is m-trivial (Goussarov) for all m is the unknot.

Structure of the proof of Theorem 6.8. Assume N > 3c(K); with Cor. 3.7 this gives f_r(K) = 0 for all r >= 1 (so the "quantitative" theorem is proved
only by reduction to the case V_K = 1). Take a crossing-minimal diagram D; "Since K is nontrivial, D has at least one non-nugatory crossing u";
take a witness v; Theorem 5.11 gives c_2 = 0 on the face; the order-one and order-two skein recursions for c_0, c_1, c_2 then force
c_0(u=0, v=0) = 4, i.e. three components after smoothing u and v, contradicting that smoothing v merges the two components.

Judgement (mine, from a partial read; not a referee report).
- The only places where "K nontrivial" or "D crossing-minimal" enter are (i) existence of a non-nugatory crossing, and (ii) the numerical identity
  #cross(D) = c(K) used to name the degree cap B_0 = 3 #cross(D) (grep of all uncommented occurrences of "minimal"/"nontrivial"; Cor. 3.7 holds for
  every diagram). The vanishing hypothesis f_r = 0 for all r >= 1 also holds for the unknot.
- Hence the argument, if every step is valid, applies verbatim to any diagram D of the unknot that has a non-nugatory crossing (for instance the
  standard trefoil shadow with one crossing changed, n = 3, B_0 = 9). There Theorem 5.11 would assert a_2 = 0 at all four sign choices of (u, v),
  one of which is the trefoil, whose order-2 invariant is nonzero; and Step 2 would produce the same "three components" contradiction for the unknot.
  So either some step uses minimality in an unstated way, or (more likely) the descent machinery (Thm 5.6, 5.10, 5.11 or the smoothing-proxy lemma)
  is wrong. This "proves too much" test is the natural first question to put to the authors.
- Independent prior: nontrivial links with trivial Jones polynomial exist (Thistlethwaite 2001; Eliahou-Kauffman-Thistlethwaite 2003), so any proof
  by skein/finite-type manipulation must use knot-ness in an essential way; here knot-ness enters only through c_0 = 1, c_1 = 0 on knots.
- Status: unverified claim in math.GM with no community uptake found in five months.

### 1.3 Jost, Lewark, arXiv:2601.16588 "Signs of knot polynomial evaluations from a topological perspective" (read: TeX v1; PDF for numbering)

Versions. v1 only, Fri 23 Jan 2026, 20 pages, math.GT. No journal reference yet.
Convention: skein t^{-1}V_{L_+} - tV_{L_-} = (t^{1/2} - t^{-1/2})V_{L_0}, V(unknot) = 1. D_K = double branched cover.
Known evaluations recalled (Introduction): V_K(1) = V_K(e^{2 pi i/3}) = 1; V_K(-1) = (-1)^{(det K - 1)/2} det K; V_K(i) = (-1)^{Arf K};
V_K(e^{2 pi i/6}) = eps_K (i sqrt 3)^{dim H_1(D_K; F_3)} with eps_K = +-1 (Lickorish-Millett, Lipson).
- Theorem 1.1 (p. 2; proved p. 14 via Prop. 3.6): write det K = 3^alpha q with 3 not dividing q. Then
  V_K(e^{2 pi i/6}) = nu(q) (-1)^{alpha + dim H_1(D_K;F_3) + sum_k r_{3,k}(K)} (i sqrt 3)^{dim H_1(D_K;F_3)},
  where nu(eta) = 1 for eta = +-1 mod 12 and -1 for eta = +-5 mod 12, and r_{p,k} in Z/2 are Wall's isometry invariants of the linking pairing on
  H_1(D_K; Z). So V_K(e^{2 pi i/6}) is determined by the oriented homeomorphism type of D_K.
- Theorem 1.2 (p. 3): if u(L) = dim H_1(D_L; F_p) - c(L) + 1 (p odd prime) and L is unknotted by u_+ positive and u_- negative crossing changes, then
  Lipson's singular determinant delta_p(L) is 1, (-1)^{u_-}, (-1)^{u(L)}, (-1)^{u_+} for p = 1, 3, 5, 7 mod 8. For u = 1 knots this is Lickorish's
  obstruction; for p = 3 it is Traczyk's.
- Theorem 4.1 (p. 15): analogous statement for the Q-polynomial at the reciprocal of the golden ratio; a counterexample to a conjecture of Stoimenow.
What it does not do: nothing about detection. Consequence for the brief's K_n (D_{K_n} = S^3_{1/n}(kappa), an integral homology sphere): det = 1,
H_1 = 0, so V_{K_n}(-1) = 1, V_{K_n}(i) = 1 and by Thm 1.1 V_{K_n}(e^{2 pi i/6}) = 1; the evaluations at 1st, 2nd, 3rd, 4th, 6th roots of unity carry
no information on Lemma Q.

### 1.4 Sikora: IPAM talk and q-rationals

Talk (source: IPAM schedule API, `src/ipam/sched_QTWS1.json`, `src/ipam/abs_sikora.json`): Adam Sikora (SUNY Buffalo), "Tangle Equations, the Jones
Unknot Conjecture, and Lens Space Surgeries.", IPAM Workshop I "Hyperbolic Structures and Quantum Invariants" (12-15 Oct 2026) of the long program
"Quantum Topology, Character Varieties and Low-Dimensional Geometry" (23 Sep - 18 Dec 2026); Thursday 15 Oct 2026, 16:00-16:45. A recording is posted
(Kaltura entry 1_zqd2sckl; "View on Youtube" link on the abstract page). [Recording NOT watched.]
Abstract, paraphrased: systems of tangle equations N(X+T_1) = L_1, N(X+T_2) = L_2 are related to the Nugatory Crossing and Cosmetic Surgery
conjectures. The "Uniqueness of Rational Solutions Conjecture" says a rational solution of a system of (framed) tangle equations is unique.
A failure of this topological statement would disprove the Jones unknot conjecture. Double branched covers turn the unframed version into a statement
about lens space surgeries, "leading to new results and conjectures about them, and potentially guiding towards counterexamples to the Jones Unknot
Conjecture" (the one quoted phrase).
Background paper: Sikora, "Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed rationals",
Canad. J. Math. 76 (2024) 707-727, arXiv:2005.08162 [abstract only read here]: every system of framed tangle equations has at most one framed
rational solution; T implies uniqueness of a rational solution among all 2-tangles; Kauffman bracket ratio of a 2-tangle, equal to the MGO q-rational
for rational tangles.
No 2026 arXiv paper by Sikora on this was found (arXiv API author query, 1 Jan - 15 Nov 2026). Other IPAM talks in the same program touching the
subject: C. Lee (colored Jones and volume through categorification, 15 Oct), J. Higgins (minimal sl(N) complexes of rational tangles via the Fukaya
category, WS III, Nov; arXiv:2610.20558).

### 1.5 Other items, June-November 2026 (arXiv API scans; abstracts read, papers not read unless stated)

q-rationals, q-modular group, roots of unity (relevant to S3):
- K. Miyamoto, arXiv:2609.33703 (27 Sep 2026), "Cyclotomic factors and irreducibility of the denominators of q-deformed rational numbers" [TeX read].
  Thm 3.2 (p. 5): for a primitive d-th root of unity zeta, d >= 2, ker(rho_zeta: PSL(2,Z) -> PGL(2,C)) = N_d := normal closure of R^d, and the
  stabiliser of infinity in the image is generated by the image of R; so the image is the (2,3,d) triangle group, Fuchsian for d >= 7 (Prop. 3.7,
  p. 6, proof by trace comparison (0, 2cos(pi/d), 1) for zeta = e^{2 pi i/d}; Lemma 3.5 transfers the kernel to the other primitive roots).
  Thm A = Thm 3.8 (p. 7): for gamma(infinity) = r/s, Phi_d | S_{r/s}(q) iff gamma in <R> N_d; Phi_d | R_{r/s}(q) iff gamma in S<R>N_d.
  Cor B = Cor 3.9: then s = 0, r = +-1 mod d (resp. r = 0, s = +-1 mod d); Remark 3.11: for d >= 6 divisibility is not a congruence condition.
  The introduction attributes ker = N_d "essentially" to Funar-Kohno as corrected by Dlugie when 3 | d.
- T. Byakuno, X. Ren, K. Yanagawa, arXiv:2603.08439v2 (v2 Aug 2026) [TeX skimmed]: G_q(zeta) finite iff zeta = zeta_n, n = 2,3,4,5; the set
  {J_{r/s}(zeta)} of values of normalised Jones polynomials of rational links is finite iff zeta = zeta_n, n = 2,...,6. Normalisation
  J_{r/s}(q) = +- t^h V_{L(r/s)}(t) at t = -q^{-1}, constant term 1; J_{r/s}(q) = q R_{r/s}(q) + (1-q) S_{r/s}(q) for r/s > 1 (MGO Prop. A.1; BBL Thm A.3).
- A. Elzenaar, arXiv:2609.29831v2 (24/29 Sep 2026) [TeX skimmed]: q-reals as limit sets of the quasi-Fuchsian groups PSL(2,Z)_q; Thm 1.1 describes
  the discreteness locus Q (two punctured discs meeting at q = -1); Remark 3.5: for fixed q the values |V_{r/s}|(-q) (Jones polynomial of the
  two-bridge link with all coefficients made positive) are dense in half of the limit set; Remark 3.8: on the unit circle the discrete groups are the
  Fuchsian triangle groups (reference to Elzenaar-Gong-Martin-Schillewaert arXiv:2405.15970, Remark in Section 6, which uses Knapp and Brenner).
  arXiv:2405.15970 Introduction states that relating the Farey polynomial of a two-bridge link to its Jones polynomial "remains open".
- Jouteur, Paris-Romaskevich, Thomas, arXiv:2607.22308v2 (Jul/Sep 2026): uniqueness of q-rationals up to conjugacy via character varieties; a second
  deformation whose numerators are (up to sign and power of q) the Jones polynomials of rational knots at a = -1/q.
- Ovsienko arXiv:2609.10999 (q-deformed cross-ratio); Germoni arXiv:2610.09953; Yanagida arXiv:2611.10104.

Khovanov / tangles / strongly invertible:
- T. Mejia-Gomez, arXiv:2610.10262 (7 Oct 2026): proves the KWZ conjecture that the A_infinity-extended Bar-Natan twisted complex of a four-ended tangle
  is a tangle invariant (via matrix multifactorizations generalising Ballinger). Directly relevant to the KWZ calculus.
- Kegel, Teragaito, arXiv:2608.00864 (1 Aug 2026): first infinite family of strongly invertible L-space knots with no Khovanov-thin surgery.
- T. Sano, arXiv:2608.07114: involutive Khovanov homology for involutive tangles (divide and conquer), equivariant Rasmussen invariant.
- Collari, Lisca, arXiv:2606.21471: polynomial invariant P^e of strongly involutive links (equivariant HOMFLY-PT analogue; Euler characteristic of the
  third page of the Lobb-Watson spectral sequence).
- Boyle, Spyropoulos, arXiv:2609.40122: Khovanov homology of nullhomologous alternating links in RP^3 determined by Jones polynomial and signatures.
- Hsueh, Kegel, Suchodoll, Thiele, arXiv:2608.24353: a Legendrian simple knot not detected by Khovanov homology (disproves Chernov-Maguire).
- Eftekhary, Souri, arXiv:2610.21153 (Heegaard Floer pillowcase); Ballinger, Conners arXiv:2611.09367 (HOMFLY homology for tangles).
Jones polynomial constraints:
- Ichihara, arXiv:2609.32507, and Ichihara-Kishimoto, arXiv:2610.10019: a knot with nontrivial Jones polynomial of span <= 14 has no purely
  cosmetic surgery (these results exclude V = 1 by hypothesis).
- Garoufalidis-Li arXiv:2610.07198, Harper-Kohli arXiv:2610.12352: the colored Jones function does not determine the Links-Gould polynomials.
No other 2026 arXiv paper with "Jones polynomial" and "unknot" in the abstract was found besides Carmi-Cohen (API query, 15 May - 15 Nov 2026).
The verified range for T remains 24 crossings (Tuzun-Sikora 2021, as cited in K3 Problem 1.24, Remark 2).

---------------------------------------------------------------------------------------------------

## 2. Status questions

### S1. Do the colored Jones polynomials (all colors) detect the unknot?

State: claimed, not established in the refereed literature; treated as open by the current standard problem list.
- Announcement: Grigsby-Wehrli (arXiv:0807.1432v3, Introduction) report that Andersen "has announced a proof" that the full collection of colored
  Jones polynomials is an unknot detector, via growth rates of the invariants and nontrivial SU(2) representations of surgeries; their bibliography
  entry is Andersen's "Toeplitz operators and Hitchin's connection" (Hitchin Festschrift). Hedden (arXiv:0805.4418) mentions the same announcement.
- Preprint with the claim: J. E. Andersen, "A geometric formula for the Witten-Reshetikhin-Turaev quantum invariants and some applications",
  arXiv:1206.2785v1 (11 Jun 2012; single version; arXiv admin note of substantial text overlap with arXiv:1206.2635; no journal reference on arXiv,
  and none found by search). Theorem 10 (p. 6): if X is 1-surgery on a nontrivial knot K then |Z^{(k)}(X)| != |Z^{(k)}(S^3)| for some level k.
  Corollary 1 (p. 6): if the colored Jones polynomials of K equal those of the unknot then K is the unknot. Inputs: the geometric formula (Thm 9),
  Kronheimer-Mrowka (1-surgery on a nontrivial knot has an irreducible SU(2) representation), and degenerate stationary phase (Varchenko;
  Denef-Nicaise-Sargos). The proof of Theorem 10 (last section, TeX lines 2666-2843) is a sketch: it contains the sentence "We will from now assume that
  the phase functions have non-singular principal part with respect to their Newton diagram", and the conclusion is drawn in one paragraph without
  addressing possible cancellation between contributions. I regard S1 as not proved by this text as written.
- K3 problem list (Baykur, Kirby, Ruberman, eds., AMS; author's preliminary version, Section 1.4, pp. 31-32), Problem 1.24 "(Jones Unknot Detection)":
  (a) nontrivial knot with trivial Jones polynomial? (b) nontrivial knot whose colored Jones polynomials are all trivial? (c) trivial HOMFLYPT?
  All three are posed as open; Remark (3): a positive answer to (b) [sic: non-existence] would follow from the Volume Conjecture [MM01]; Andersen's
  preprint is not cited there although Andersen is among the contributors.
- Conditional results: Dunfield-Garoufalidis, "Non-triviality of the A-polynomial for knots in S^3", AGT 4 (2004) 1145-1153 (arXiv:math/0405353):
  Theorem 1.1 (A-polynomial of a nontrivial knot is not a power of L-1; from Kronheimer-Mrowka, Thm 1.2 there; independently Boyer-Zhang);
  Corollary 1.3: if the AJ conjecture holds then the colored Jones function distinguishes the unknot. The AJ conjecture is proved for some two-bridge
  and pretzel knots (Le; Le-Tran; Le-Zhang, as cited in K3 Problem 1.25). Murakami-Murakami, Acta Math. 186 (2001) (arXiv:math/9905075), Section 5:
  the Volume Conjecture implies Vassiliev's conjecture below and (final Remark, via Melvin-Morton-Rozansky proved by Bar-Natan-Garoufalidis) that a
  knot is trivial iff all its colored Jones polynomials are trivial.
- Categorified versions are theorems: Khovanov homology detects the unknot (Kronheimer-Mrowka 2011); Khovanov's categorification of the reduced
  n-colored Jones polynomial detects the unknot for every n > 1 (Grigsby-Wehrli 2010); 2-cable Khovanov homology (Hedden 2009).
- 2026: Garoufalidis-Li and Harper-Kohli (above) show the colored Jones function is not a universal invariant in another direction. No 2020s paper
  proving S1 was found.

### S2. Do Vassiliev invariants detect the unknot?

State: open. Vassiliev's conjecture (finite type invariants separate knots) and its weakest case (a knot all of whose Vassiliev invariants agree with
the unknot is trivial; stated as Conjecture 5.x in Murakami-Murakami Section 5 with reference to Vassiliev 1990, 6.1) are unproved.
- S1 implies S2: the coefficients of the colored Jones polynomials in h = log t are Vassiliev invariants (Birman-Lin), so a knot with all Vassiliev
  invariants trivial has trivial colored Jones polynomials (argument in Murakami-Murakami Section 5).
- Hence S2 follows from the AJ conjecture or from the Volume Conjecture (Melikhov, arXiv:2406.09331v2, Introduction, states exactly this and treats
  Vassiliev's Conjecture (K) as open in 2024; it also recalls that finite type invariants fail to separate knots in the Whitehead manifold).
- Still unknown (same source, citing Chmutov-Duzhin-Mostovoy): whether finite type invariants detect knot orientation.
- Classical obstruction to cheap proofs [from memory, NOT re-read]: for every n there are nontrivial knots with all invariants of order <= n trivial
  (Ohyama; Stanford; Goussarov-Habiro n-equivalence).
- The only 2026 claim is Carmi-Cohen Corollary 6.10 (Section 1.2 above); unverified.

### S3. Jones polynomial at a single root of unity, two-bridge links, triangle groups

(a) The triangle group statement (claim C1). It is in the literature, in three places.
- C. T. McMullen, "Braid groups and Hodge theory", Math. Ann. 355 (2013) 893-946 (read: author's preprint, 64 pages, `src/mcmullen/hodge.pdf`;
  page numbers below are the preprint's). Setting: X: y^d = prod (x - b_i), rho_q the action of B_n on H^1(X)_q = Ker(T^* - q), q^d = 1.
  Theorem 5.5 (p. 24): for q^n != 1, rho_q is dual to the reduced Burau representation specialised to t = q.
  Section 5, "Examples: n = 3" (p. 25), in the one sentence I quote: "For n = 3 and p > 6, the image of A_{n-1}(-zeta_p) in PU(1,1) is simply the
  (2,3,p)-triangle group acting on the hyperbolic plane." Presentation {a, b : a^2 = b^3 = (a^{-1}b)^p = e}, a = image of s_1 s_2 s_1, b = image of
  s_1 s_2; "This group arises as rho_q(B_3) when q = zeta_d^{-k} and k/d = 1/2 +- 1/p"; for p = 3,4,5 the images are A_4, S_4, A_5 in PU(2); for p = 6
  the reduction lies in PU(1). Corollary 11.5 (p. 50) uses "the discrete (2,3,p) triangle group" as rho_q(B_3) in U(1,1) for q the primitive d-th
  root closest to -1.
- L. Funar, T. Kohno, "On Burau's representations at roots of unity", Geom. Dedicata 169 (2014) 145-163 (read: arXiv:0907.0568v4, 18 pages).
  Definition 3.1 and Proposition 3.3 (pp. 11-12): for q = exp(i alpha), alpha in (-pi/3, pi/3), the subgroup Gamma_{-q} of PU(1,1) generated by the
  classes of beta_{-q}(g_1^2), beta_{-q}(g_2^2) is discrete iff q = exp(+-2 pi i/n), n >= 7 (three rotations of angle 2 alpha about the vertices of
  an equilateral triangle, Lemma 3.1; Knapp, Mostow, Deraux). Proposition 3.4 (p. 13): for q of order 2k the group Gamma_{-q} is the (k,k,k) triangle
  group; Proposition 3.5 (p. 14): for q of order 2k+1, k >= 3, Gamma_{-q} is isomorphic to Delta(2,3,2k+1). Theorem 1.2 = Theorem 3.3 (pp. 1, 16):
  presentation of beta_{-q}(B_3) for q a primitive n-th root (braid relation plus g_i^{2k} = (g_1^2 g_2^2)^k = 1 for n = 2k, k odd; etc.).
  Caveat: E. Dlugie, "The Burau representation and shapes of polyhedra", AGT 24 (2024) 2787-2805 (arXiv:2210.06561v2), Theorem 5.4 (p. 14):
  for q a primitive d-th root, d >= 7, ker beta_3(-q) = ncl(sigma^d) . <tau_3^l> with l = 2d/gcd(12, d+6) the order of (-q)^3; "This theorem corrects
  the result stated in [Funar-Kohno, Theorem 1.2], which is incorrect in the cases when d is a multiple of 3."
- K. Miyamoto, arXiv:2609.33703 (Sep 2026), Thm 3.2 and Prop. 3.7, in q-modular-group language (see 1.5), and Elzenaar-Gong-Martin-Schillewaert
  arXiv:2405.15970 (Remark in Section 6: the discrete groups on the unit circle are exactly triangle groups, by Knapp and Brenner).
Precision needed when quoting C1: (i) it is the image in PU(1,1) (projectivised); the linear image in GL_2(C) is a central extension whose kernel is
given by Dlugie Thm 5.4; (ii) Fuchsian means -t = e^{+-2 pi i/n} exactly. For the other primitive n-th roots the image is abstractly the same quotient
of B_3 (Galois conjugation; FK Props 3.4-3.5, Miyamoto Lemma 3.5) but is either non-discrete in PU(1,1) or lies in PU(2); (iii) n = 6 is the Euclidean
case, n <= 5 finite (A_4, S_4, A_5 for 3, 4, 5).

(b) Signature of the invariant Hermitian form (claim C2). Squier, "The Burau representation is unitary", Proc. AMS 90 (1984) 199-202 [NOT READ: the AMS
server refused automated download], gives the form. The signature statement is explicit in:
- Funar-Kohno Proposition 2.1 (p. 4): for q = exp(i alpha) not of order 2 or 3, the two-dimensional representation of B_3 factoring through the
  Temperley-Lieb quotient is conjugate into U(2) or U(1,1) according to eps_q = sign(q + \bar q + 1): eps_q = +1 for alpha in (-2pi/3, 2pi/3),
  eps_q = -1 for alpha in (2pi/3, pi) u (pi, 4pi/3); Prop. 2.3 identifies Burau of B_3 with this representation up to a character.
- McMullen Corollary 3.2 (p. 15): for q = zeta_d^{-k} the intersection form on H^1(X)_q has signature (r,s) = (ceil(n k/d - 1), ceil(n(1 - k/d) - 1));
  for n = 3: (0,2) for k/d < 1/3, (1,1) for 1/3 < k/d < 2/3, (2,0) for k/d > 2/3 (Introduction, p. 2: r, s count the n-th roots of unity strictly
  below and above the line through 1 and q).
- My numerical check (`check/squier_sig.py`): for the reduced Burau matrices above and t = e^{i theta}, the invariant Hermitian form is definite for
  theta = 10, 60, 100, 119, -100 degrees and of signature (1,1) for theta = 121, 140, 170, 180, -150 degrees; the sign is that of 1 + 2 cos(theta).
So: definite exactly on the open arc |arg t| < 2 pi/3, signature (1,1) on the open complementary arc, degenerate (and the representation reducible)
at the two primitive cube roots of unity. At t = -1 the form has signature (1,1) and the image is PSL(2,Z)-like (cusped).

(c) Two-bridge links: what is published, and what is not.
- Published ingredients. (1) J_{r/s}(q) = q R_{r/s}(q) + (1-q) S_{r/s}(q) for r/s > 1, where [r/s]_q = R/S is the MGO q-rational and J is the Jones
  polynomial of the two-bridge link normalised to constant term 1 at t = -1/q (Morier-Genoud-Ovsienko, Forum Math. Sigma 8 (2020), Prop. A.1; Lee-Schiffler
  2019; restated in BRY Section 2 and in arXiv:2405.15970 Introduction). (R, S) is, up to a unit +-q^m, the first column of the word matrix in R_q, S_q
  (Miyamoto Lemma 2.1). So J is a matrix coefficient of the projective Burau representation of B_3 at t = -q: this is the "plat closure" side.
  (2) The triangle group statements in (a). (3) BRY: the set of values J_{r/s}(zeta) is finite iff zeta = zeta_n, n <= 6. (4) Miyamoto Thm A: exact
  description of the slopes with S_{r/s}(zeta_d) = 0 or R_{r/s}(zeta_d) = 0 as N_d-orbits. (5) Jones, Ann. of Math. 126 (1987) 335-388 [NOT READ: no
  accessible copy; cited through Przytycki]: Corollary 14.7, the set {|V_L(e^{pi i/5})|} over all links is dense in [0, infinity); the 1987 paper also
  contains the closed 3-braid formula via Burau and the unitarity range, but I could not check its two-bridge/plat section.
- Not found: any published formula expressing |V| of a two-bridge link at a root of unity as a hyperbolic cosine of a distance in the (2,3,n)
  tessellation; any published statement that V at a single root of unity detects the unknot among two-bridge knots. Searches: web (extended) with
  several phrasings, arXiv API, the sources above and their introductions. Elzenaar et al. explicitly call the relation between Farey polynomials
  and Jones polynomials of two-bridge links open, and Elzenaar's Remark 3.5 is the only geometric statement about Jones values found (limit sets,
  generic q, coefficients made positive).
- What is published and cuts the other way: J. H. Przytycki, "t_k moves on links", Contemp. Math. 78 (1988) 615-656 (read: arXiv:math/0606633).
  Corollary in the Introduction, part (a): if t^k = (-1)^k, t != -1 (t^{1/2} = -i e^{pi i m/k}), then V_{t_k(L)}(t) = (-1)^m i^k V_L(t), where t_k adds
  k positive half twists to two parallel strands; part (b) = Corollary 1.10: if t^{2k} = 1, t != -1, then V_{\bar t_{2k}(L)}(t) = V_L(t) for the
  antiparallel 2k-move; Theorem 1.13 for \bar t_k, k odd. Hence at a root of unity the Jones value (up to an explicit root of unity) is constant on
  t_k-equivalence classes, which contain infinitely many two-bridge knots.
- Explicit consequence (my computation, `check/t2n.py`, exact identity plus numerics): from V_{T(2,n)}(t) = t^{(n-1)/2}(1 - t^3 - t^{n+1} + t^{n+2})/(1 - t^2),
  for t^{2m} = 1, t != +-1: V_{T(2,2m-1)}(t) = t^{m-1} (t - t^3)/(1 - t^2) = t^m = +-1, and = 1 when t^m = 1. Checked numerically: T(2,9) at primitive
  5th roots, T(2,13) at 7th roots, T(2,17) at 9th roots, T(2,21) at 11th roots, T(2,15) at 8th roots, T(2,23) at 12th roots give exactly 1; T(2,7) at
  primitive 8th roots and T(2,5) at 6th roots give -1. So for every root of unity t of order m >= 3 the nontrivial two-bridge knot T(2,2m-1) has
  V(t) = 1: no single root of unity detects the unknot among two-bridge knots, including the Fuchsian values t = -e^{+-2 pi i/n} (order m = n/2 for
  n = 2 mod 4, e.g. n = 14, T(2,13); order n for n = 0 mod 4, e.g. n = 8, T(2,15); order 2n for n odd, e.g. n = 7, T(2,27)).
- Cross-check of the shape of a distance formula (my derivation; verified numerically in `check/coshcheck.py` for d = 7, 9, 14 on 200 random words each,
  deviation < 1e-14): for zeta = e^{2 pi i/d}, d >= 7, Q the point of the disc fixed by rho(R) (vector e_1), and gamma(infinity) = r/s > 1,
      |J_{r/s}(zeta)| = 2 sin(pi/d) cosh( dist(S.Q, gamma.Q) / 2 ),
  with dist the hyperbolic distance of curvature -1. Reason: the functional (q, 1-q) annihilates the second fixed vector of S R S^{-1}, hence is the
  Hermitian dual of S e_1. The slope 0 (unlink) gives the minimum 2 sin(pi/d); the unknot value |J| = 1 is attained at the d orbit points
  nearest to S.Q (the neighbours of S.Q in the {3,d} tiling by the order-d vertices), i.e. for gamma in S R^j S <R> N_d (slopes N_d-equivalent to
  -1/j); T(2,d-1) (slope d-1 = R^d(-1)) is one of them. So what one root
  of unity detects among two-bridge links is the N_d-orbit (Miyamoto's N_d, generated by conjugates of R^d, the t_d-type twist moves), not the unknot.
  This is consistent with, and no stronger than, Przytycki's theorem. I did not find this identity in print.

---------------------------------------------------------------------------------------------------

## 3. Claim checks

- C1 (image of B_3 under reduced Burau at -t = e^{2 pi i/n}, n >= 7, is the Fuchsian (2,3,n) triangle group): CONFIRMED, with the precision that
  it is the image in PU(1,1). References: McMullen, Math. Ann. 355 (2013), Section 5 "Examples: n = 3" (preprint p. 25) with Thm 5.5 (t = q, dual);
  Funar-Kohno, Geom. Dedicata 169 (2014), Props 3.3-3.5 and Thm 1.2 (kernel corrected by Dlugie, AGT 24 (2024), Thm 5.4, when 3 | n);
  Miyamoto arXiv:2609.33703 Thm 3.2, Prop. 3.7.
- C2 (form definite exactly on the arc between the primitive cube roots containing 1, signature (1,1) on the complementary arc): CONFIRMED
  (open arcs; degenerate at the cube roots). Funar-Kohno Prop. 2.1 (p. 4); McMullen Cor. 3.2 (preprint p. 15) with n = 3; numerical check.
- C3 (no published source states the cosh-distance formula for two-bridge links): CONFIRMED within the limits of this search (Jones 1987 and Squier 1984
  full texts not accessible). All ingredients are published (MGO Prop. A.1; McMullen; Funar-Kohno; Miyamoto Thm 3.2 and Thm A), and the formula is a
  short corollary of them; the closest printed statements are Miyamoto Thm A (vanishing loci), BRY (finiteness of value sets) and Elzenaar Rem. 3.5.

## 4. Open questions for the mathematician

1. Carmi-Cohen: does any step of Thm 5.11 or of the smoothing-proxy lemma use crossing-minimality beyond #cross(D) = c(K)? If not, the trefoil-shadow
   unknot diagram is a counterexample to the method.
2. BBB v2: are conditions (1)-(3) of "properly simple modulo 4-disks" really satisfied by the Gamma constructed in the proof of Prop. 6.7, and does
   the added "with basepoint" case in Section 5 need its own argument in Prop. 5.1?
3. Is there a refereed proof of S1? Andersen's 2012 preprint was not found in any journal; a direct query to the author or to the K3 editors
   (Problem 1.24(b)) would settle whether it is considered proved.
4. Sikora's talk announces "new results and conjectures" on lens space surgeries; no preprint yet. The recording should be watched for the precise
   statements, since they concern exactly the two-closure (tau(infinity), tau(0)) structure used in Lemma Q.

## 5. Sources (URLs)

arXiv: 2607.05283 (v1, v2), 2606.22410, 2601.16588, 2609.33703, 2609.29831, 2607.22308, 2603.08439, 2405.15970, 0907.0568, 2210.06561, 1206.2785,
math/0405353, math/9905075, 0807.1432, 0805.4418, 2406.09331, math/0606633, 2610.10262, 2608.00864, 2608.07114, 2606.21471, 2609.40122, 2608.24353,
2609.32507, 2610.10019, 2610.07198, 2610.12352, 2611.10850 (all at https://arxiv.org/abs/<id>).
McMullen preprint: https://people.math.harvard.edu/~ctm/papers/home/text/papers/bn/bn.pdf
K3 problem list (author's preliminary version): https://math.berkeley.edu/sites/default/files/surv-295-ruberman-watermarked-author-pdf.pdf
IPAM Workshop I schedule: https://www.ipam.ucla.edu/programs/workshops/workshop-i-hyperbolic-structures-and-quantum-invariants/?tab=schedule
Sikora abstract: https://www.ipam.ucla.edu/abstract/?tid=21771&pcode=QTWS1
Columbia news item on BBB: https://www.math.columbia.edu/2026/08/03/professor-joan-birman-and-collaborators-resolved-the-last-remaining-open-case-for-the-burau-representation-of-the-classical-braid-group/
Sikora, Canad. J. Math.: https://arxiv.org/abs/2005.08162
