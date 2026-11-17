# References and credit map

This is the curated bibliography for the public exposition. The archive contains additional source-specific citations and exact theorem locators. It is not a claim that every historical reference has been reverified, or that any project result has established priority. See [Human work and corrections](HUMAN_WORK_AND_CORRECTIONS.md) before using a version-specific criticism.

**Verification labels.** `primary-source-inspected` means the relevant primary text was reopened for this publication audit. `metadata-checked` means the primary bibliographic record was checked; the substantive theorem audit remains in the linked research notes. `archived-primary-audit` means the project records an earlier primary-source read, not a fresh full proof review here. `archived-reference` is bibliographic attribution only. Handoff additions distinguish newly checked metadata or statements from locators inherited from earlier source audits; `original-not-reopened` and `archived-attribution` mark explicit limits. All publication-audit dates here are 17 November 2026; pinned versions are intentional.

Machine-readable counterpart: [references.json](../data/references.json). The list credits inputs, not only papers the project criticized.


## Foundations


### JONES85

Vaughan F. R. Jones. [A polynomial invariant for knots via von Neumann algebras](https://doi.org/10.1090/S0273-0979-1985-15304-2). Bulletin of the AMS 12 (1985), 103–111.

Foundational invariant and V_L(1)=(-2)^(number of components-1), the classical input to the project’s boundary-matching lemma. Also recorded in Champanerkar–Kofman 2006, Proposition 2.2, equation (3); no unchecked original theorem number is asserted. Verification: **archived-reference**.


### KAUFFMAN87

Louis H. Kauffman. [State models and the Jones polynomial](https://doi.org/10.1016/0040-9383(87)90009-7). Topology 26 (1987), 395–407.

Bracket state sum and skein calculus underlying the exact certificates. Verification: **archived-reference**.


### LM86

W. B. R. Lickorish and Kenneth C. Millett. [Some evaluations of link polynomials](https://web.math.ucsb.edu/~millett/Papers/1986Millett6LickorishCommMathHelv.pdf). Comment. Math. Helv. 61 (1986), 349–359.

Theorems 1 and 3 supply the Arf and sixth-root evaluations; Theorem 1 credits H. Murakami. Verification: **primary-source-inspected**.


### EKT03

Shalom Eliahou, Louis H. Kauffman and Morwen Thistlethwaite. [Infinite families of links with trivial Jones polynomial](https://homepages.math.uic.edu/~kauffman/ekt.pdf). Topology 42 (2003), 155–169.

Infinite Jones-trivial link families and the Hopf-shell/Omega construction, following Thistlethwaite’s 2001 examples. Preserve component and framing conventions; fusion does not automatically give knot counterexamples. Verification: **primary-source-inspected**.


### EF17

Shalom Eliahou and Jean Fromentin. [A remarkable 20-crossing tangle](https://arxiv.org/pdf/1610.05560v2). J. Knot Theory Ramifications 26 (2017), 1750091; arXiv:1610.05560v2; DOI 10.1142/S0218216517500912.

Definitions 3.1–3.2, Lemma 4.2, Proposition 5.2: source of the coefficientwise modulo-2^r family and the seed for the project’s depth-four deduction. Distinct nontrivial knots are supplied, not a primality or increasing Taylor-depth theorem. Verification: **primary-source-inspected**.


### CK06

Abhijit Champanerkar and Ilya Kofman. [On links with cyclotomic Jones polynomials](https://arxiv.org/abs/math/0605631v3). Algebr. Geom. Topol. 6 (2006), 1655–1668; arXiv:math/0605631v3.

Definition 1/Proposition 2.1: twist bracket; Examples 4–5: Kanenobu invisible directions; Proposition 2.2, equation (3): component specialization; Lemmas 3.1–3.4/Example 6: resonant hyperplanes; Proposition 3.5 and Proposition 4.1. Prior framework for the project’s explicitly fixed-template algorithm. Verification: **primary-source-inspected; further locators from archived primary audit**.


### CK05

Abhijit Champanerkar and Ilya Kofman. [On the Mahler measure of Jones polynomials under twisting](https://arxiv.org/abs/math/0404236v3). Algebr. Geom. Topol. 5 (2005), 1–22; arXiv:math/0404236v3; DOI 10.2140/agt.2005.5.1.

Mahler-measure convergence under twisting; Proposition 3.3 is the one-site predecessor of the 2006 twist-bracket formulation. Keep this paper distinct from CK06. Verification: **metadata-checked; substantive-locators-from-archived-audit**.


### THISTLETHWAITE01

Morwen Thistlethwaite. [Links with trivial Jones polynomial](https://homepages.math.uic.edu/~kauffman/tj.pdf). J. Knot Theory Ramifications 10 (2001).

First nontrivial two- and three-component examples with the corresponding unlink polynomial, preceding EKT’s infinite families. Verification: **primary-source-inspected; journal attribution from archived audit**.


### KANENOBU86A

Taizo Kanenobu. [Examples on polynomial invariants of knots and links](https://arxiv.org/pdf/math/0605631v3). Math. Ann. 275 (1986), 555–572.

Original polynomial-preserving families used in CK06 Example 5. Linked CK06 supplies the checked bibliographic citation [4] and its application; the original paper was not reopened here. Verification: **bibliography-checked-in-CK06; original-not-reopened**.


### KANENOBU86B

Taizo Kanenobu. [Infinitely many knots with the same polynomial invariant](https://arxiv.org/pdf/math/0605631v3). Proc. Amer. Math. Soc. 97 (1986), 158–162.

Original constant-sum family underlying CK06 Example 4. Linked CK06 supplies the checked bibliographic citation [5] and its application; the original paper was not reopened here. Verification: **bibliography-checked-in-CK06; original-not-reopened**.


## Tangle equations and surgery


### SIKORA24

Adam S. Sikora. [Tangle equations, the Jones conjecture, slopes of surfaces in tangle complements, and q-deformed rationals](https://arxiv.org/pdf/2005.08162v2). Canad. J. Math. 76 (2024), 707–727; DOI 10.4153/S0008414X23000755; arXiv:2005.08162v2.

V2 Proposition 1, Conjecture 2, Theorems 3/7/21/24 and Corollary 20. Theorem 24 = journal Theorem 9.2 is the existing equivalence of Jones unknot detection with bracket detection of rational tangles; Proposition 25 gives bounded-crossing scope. V2 Proposition 10(1) = journal Proposition 2.1(1) is the separate statement challenged by the project. See the guide for the numbering concordance and limits of Lemma Q. Verification: **primary-source-inspected**.


### RR17

Jacob Rasmussen and Sarah Dean Rasmussen. [Floer simple manifolds and L-space intervals](https://arxiv.org/abs/1508.05900v2). Adv. Math. 322 (2017), 738–805; arXiv:1508.05900v2.

Propositions 1.3–1.4, torsion normal form, Corollary 2.3, Definition 7.2 and Proposition 7.8 in the pinned version. Verification: **metadata-checked; proof-locators-in-manuscript-audits**.


### GAINULLIN18

Fyodor Gainullin. [Heegaard Floer homology and knots determined by their complements](https://arxiv.org/abs/1504.06180). Algebr. Geom. Topol. 18 (2018), 69–109; arXiv:1504.06180.

Theorem 8.2: methodological antecedent for surgery comparison, Alexander derivative and L-space structure. Verification: **metadata-checked; proof-locator-in-manuscript-audits**.


### NIWU15

Yi Ni and Zhongtao Wu. [Cosmetic surgeries on knots in S3](https://arxiv.org/abs/1009.4720v2). J. Reine Angew. Math. 706 (2015), 1–17; arXiv:1009.4720v2.

Proposition 3.1: Casson–Walker surgery formula for a null-homologous knot in a rational homology sphere, with symmetric normalized Alexander polynomial. Specializing to 1/n surgery in S3 gives the Casson/a2 input to the odd-closure audit, after matching orientations. Credits the original Boyer–Lines formula. Verification: **primary-source-inspected**.


### BOYERLINES90

Steven Boyer and Daniel Lines. [Surgery formulae for Casson’s invariant and extensions to homology lens spaces](https://doi.org/10.1515/crll.1990.405.181). J. Reine Angew. Math. 405 (1990), 181–220.

Antecedent for the formula cited in the explicit Ni–Wu restatement; no unchecked original theorem number is asserted. Verification: **archived-reference**.


### BUCKMAURICIO11

Dorothy Buck and Mauro Maximo Mauricio. [Connect sum of lens spaces surgeries: application to Hin recombination](https://arxiv.org/abs/1007.0948). Math. Proc. Cambridge Philos. Soc. 150 (2011), 505–525; arXiv:1007.0948.

Preprint title differs: Tangle solutions for composite knots: applications to Hin recombination. Theorem 3.5(2) supplies the cited form of Lickorish’s criterion. Verification: **archived-primary-audit**.


### LICKORISH81

W. B. R. Lickorish. [Prime knots and tangles](https://doi.org/10.1090/S0002-9947-1981-0621991-2). Trans. Amer. Math. Soc. 267 (1981), 321–332.

Rational-tangle/solid-torus criterion; project uses the explicit Buck–Mauricio formulation. Verification: **archived-reference**.


### ES90

Claus Ernst and De Witt Sumners. [A calculus for rational tangles: applications to DNA recombination](https://doi.org/10.1017/S0305004100069383). Math. Proc. Cambridge Philos. Soc. 108 (1990), 489–515.

Classical rational-tangle calculus. The project’s specific two-probe example is credited instead to the 1999 paper. Verification: **archived-reference**.


### ES99

Claus Ernst and De Witt Sumners. [Solving tangle equations arising in a DNA recombination model](https://doi.org/10.1017/S0305004198002989). Math. Proc. Cambridge Philos. Soc. 126 (1999), 23–36.

Example 3: source of the unframed two-probe calibration, after the stated mirror and reparametrization. Verification: **archived-primary-audit**.


### BAKERBUCK13

Kenneth L. Baker and Dorothy Buck. [The classification of rational subtangle replacements between rational tangles](https://arxiv.org/abs/1304.7669). Algebr. Geom. Topol. 13 (2013), 1413–1463; arXiv:1304.7669.

Prior classification and tangle-rigidity context; not superseded by a scalar bracket argument. Verification: **archived-reference**.


### KMOS07

Peter Kronheimer, Tomasz Mrowka, Peter Ozsváth and Zoltán Szabó. [Monopoles and lens space surgeries](https://arxiv.org/abs/math/0310164). Ann. of Math. 165 (2007), 457–546; arXiv:math/0310164.

Classical unknot-surgery special case; must not be presented as a new project theorem. Verification: **archived-reference**.


### LICKORISH97

W. B. R. Lickorish. [An Introduction to Knot Theory](https://doi.org/10.1007/978-1-4612-0691-0_9). Graduate Texts in Mathematics 175, Springer (1997).

Chapter 9, Theorems 9.3–9.4 and Corollary 9.5: Goeritz presentation, including determinant-zero situations. Verification: **archived-primary-audit**.


### STOIMENOW05

Alexander Stoimenow. [Square numbers, spanning trees and invariants of achiral knots](https://doi.org/10.4310/CAG.2005.v13.n3.a5). Comm. Anal. Geom. 13 (2005), 591–631.

Proposition 6.5 is used only for the checked odd-determinant/knot consequence. Verification: **archived-primary-audit**.


### MULLINS93

David Mullins. [The generalized Casson invariant for 2-fold branched covers of S3 and the Jones polynomial](https://people.mpim-bonn.mpg.de/stavros/publications/printed/signatures_of_links_and_finite_type_invariants_of_cyclic_branched_covers.pdf). Topology 32 (1993), 419–438.

Theorem 5.1 is the Casson/signature/Jones-derivative input to the odd-closure audit. The linked Garoufalidis paper supplies an extension, normalization discussion and original citation [Mu]; no fresh inspection of the original full proof is claimed. Verification: **bibliographic citation and normalization discussion checked in Garoufalidis; locator from archived audit**.


### GAROUFALIDIS99

Stavros Garoufalidis. [Signatures of links and finite type invariants of cyclic branched covers](https://people.mpim-bonn.mpg.de/stavros/publications/printed/signatures_of_links_and_finite_type_invariants_of_cyclic_branched_covers.pdf). Contemp. Math. 231 (1999); arXiv:math/9811021.

Theorem 1.1 and Remarks 1.2/2.2: extension and conventions for Mullins’s relation. Compare orientation, signature, Jones-variable and Casson normalization before using the formula. Verification: **primary-source-inspected**.


## Strong inversions and categorification


### SNAPE18

Michael Snape. [Homological invariants of strongly invertible knots](https://theses.gla.ac.uk/39015/). PhD thesis, University of Glasgow (2018).

Chapter 3, unnumbered question after Example 3.2.6, p. 67: existing strongly-invertible-unknot Jones question. Theorems 0.1.1–0.1.3 prove Khovanov versions; Propositions 2.1.7–2.1.8 concern framed Sakuma links. The Example 3.2.6 framing discrepancy is conditional and convention-sensitive. Verification: **metadata-checked; exact-locators-in-archived-audits**.


### WATSON17

Liam Watson. [Khovanov homology and the symmetry group of a knot](https://arxiv.org/abs/1311.1085v4). Adv. Math. 313 (2017), 915–946; arXiv:1311.1085v4.

Theorem 1, Definition 10 and Proposition 11: persistent homological invariant; homological detection does not imply Euler detection. Verification: **metadata-checked; proof-locators-in-archived-audits**.


### KWZ19

Artem Kotelskiy, Liam Watson and Claudius Zibrowius. [Immersed curves in Khovanov homology](https://arxiv.org/abs/1910.14584v2). arXiv:1910.14584v2.

Curve invariant, gluing and graded algebra; Definition 4.19 and Theorem 4.21 in the pinned source. Verification: **metadata-checked; proof-locators-in-archived-audits**.


### KWZ21

Artem Kotelskiy, Liam Watson and Claudius Zibrowius. [Khovanov homology and strong inversions](https://arxiv.org/abs/2104.13592v1). Open Book Series 5 (2022), 223–244; arXiv:2104.13592v1.

Published inversion table and long-special pairing; longer components were already noted after Conjecture 3.7. Verification: **metadata-checked; proof-locators-in-archived-audits**.


### KWZ22

Artem Kotelskiy, Liam Watson and Claudius Zibrowius. [Khovanov multicurves are linear](https://arxiv.org/abs/2202.01460v1). arXiv:2202.01460v1.

Theorems 1.2, 5.1 and 5.4: Khovanov multicurve geography over F2. Theorem 4.4: whole-object extension; it does not automatically split into independent summand extensions. Do not transfer the Khovanov linearity classification to all Bar–Natan curves. Verification: **metadata-checked; proof-locator-in-archived-audit**.


### KWZ26

Artem Kotelskiy, Liam Watson and Claudius Zibrowius. [On mutation invariance in Khovanov homology](https://arxiv.org/abs/2602.23442v1). arXiv:2602.23442v1.

Definition 3.12 and Theorems 3.17, 3.19: normal forms and geography over fields; the project’s convention dictionary is separate. Verification: **metadata-checked; proof-locators-in-archived-audits**.


### KLMWZ

Artem Kotelskiy, Tye Lidman, Allison H. Moore, Liam Watson and Claudius Zibrowius. [Cosmetic operations and Khovanov multicurves](https://arxiv.org/abs/2109.14049v1). Math. Ann. 389 (2024), 2903–2930; DOI 10.1007/s00208-023-02697-5; arXiv:2109.14049v1.

Theorems 2.6–2.7 and proof of Theorem 1.2: actual unknot-cap structure and split-tangle detection. Verification: **metadata-checked; proof-locators-in-archived-audits**.


### LMZ24

Lukas Lewark, Laura Marino and Claudius Zibrowius. [Khovanov homology and refined bounds for Gordian distances](https://arxiv.org/abs/2409.05743v2). arXiv:2409.05743v2.

Replacement-map invariants and rational Gordian distance; the project separately studies what those maps cannot detect in formal examples. Verification: **metadata-checked; proof-locators-in-archived-audits**.


### LS22

Robert Lipshitz and Sucharit Sarkar. [Khovanov homology of strongly invertible knots and their quotients](https://arxiv.org/abs/2203.13895v1). arXiv:2203.13895v1.

Theorem 1.1/Section 3: unreduced F2 spectral sequence for an intravergent diagram, targeting an axis-moving cone for annular quotient knots; Proposition 4.4: geometric fixed-point data. Not a proved relation with N(T) or the tangle multicurve, nor established non-additivity relative to KWZ summands. Verification: **metadata-checked; proof-locator-in-archived-audit**.


### GW10

J. Elisenda Grigsby and Stephan Wehrli. [On the Colored Jones Polynomial, Sutured Floer Homology, and Knot Floer Homology](https://arxiv.org/pdf/0807.1432v3). Adv. Math. 223 (2010), 2114–2165; arXiv:0807.1432v3.

Proposition 5.20 and Theorem 1.2 are inputs; Proposition 6.9 and Conjecture 7.1 enter the separate conditional grading objection. Verification: **primary-source-inspected**.


### GWANN10

J. Elisenda Grigsby and Stephan Wehrli. [Khovanov homology, sutured Floer homology, and annular links](https://arxiv.org/abs/0907.4375v2). Algebr. Geom. Topol. 10 (2010), 2009–2039; arXiv:0907.4375v2.

Theorem 1.1 fixes mirror conventions. Do not import the removed converse of the cutting theorem from v1. Verification: **archived-primary-audit**.


### JUHASZ06

András Juhász. [Holomorphic discs and sutured manifolds](https://arxiv.org/abs/math/0601443v3). Algebr. Geom. Topol. 6 (2006), 1429–1457; arXiv:math/0601443v3.

Example 2.4 and Proposition 9.2: meridional sutures and knot Floer target. Verification: **archived-primary-audit**.


### DAEMI15

Aliakbar Daemi. [Abelian Gauge Theory, Knots and Odd Khovanov Homology](https://arxiv.org/abs/1508.07650v1). arXiv:1508.07650v1.

Theorems 2, 3, 4.9 and Section 1.4: plane-Floer filtered complex underlying MATCH. Verification: **metadata-checked; proof-locators-in-archived-audits**.


### KM11

Peter B. Kronheimer and Tomasz S. Mrowka. [Khovanov homology is an unknot-detector](https://arxiv.org/abs/1005.4346v1). Publ. Math. IHES 113 (2011), 97–208; arXiv:1005.4346v1.

Reduced Khovanov rank-one detection; Euler characteristic alone is weaker. Section 1.1 and Propositions 1.2/1.4 give I^natural(U)=Z, correcting the project’s withdrawn gauge-lens formula. Verification: **metadata-checked; source-locators-in-archived-primary-audit**.


### HEDDENWATSON10

Matthew Hedden and Liam Watson. [Does Khovanov homology detect the unknot?](https://arxiv.org/abs/0805.4423). Amer. J. Math. 132 (2010); arXiv:0805.4423.

Theorem 1: Khovanov detection for tangle-unknotting-number-one knots, including unknotting-number-one and Whitehead-double applications. It does not establish the analogous Jones statement. Verification: **metadata-checked; substantive-locators-from-archived-audit**.


### HEDDENWATSON18

Matthew Hedden and Liam Watson. [On the geography and botany of knot Floer homology](https://arxiv.org/abs/1404.6913v3). Selecta Math. (N.S.) 24 (2018), 997–1037; arXiv:1404.6913v3.

Corollary 8: rank-three knot-Floer detection of the trefoil over F2, the correct input to the low-rank discussion. Verification: **metadata-checked; substantive-locators-from-archived-audit**.


### BALDWINVELAVICK18

John A. Baldwin and David Shea Vela-Vick. [A note on the knot Floer homology of fibered knots](https://msp.org/agt/2018/18-6/agt-v18-n6-p14-p.pdf). Algebr. Geom. Topol. 18 (2018), 3669–3690; arXiv:1801.06563; DOI 10.2140/agt.2018.18.3669.

Corollary 1.5 gives a second rank-three trefoil detection input over F2; not a rank-five classification. Verification: **metadata-checked; substantive-locators-from-archived-audit**.


### FRW24

Ethan Farber, Braeden Reinoso and Luya Wang. [Fixed-point-free pseudo-Anosov homeomorphisms, knot Floer homology and the cinquefoil](https://arxiv.org/pdf/2203.01402v2). Geom. Topol. 28 (2024), 4337–4381; arXiv:2203.01402v2; DOI 10.2140/gt.2024.28.4337.

Theorem A detects the cinquefoil from bigraded HFK over Q, not total rank five. The incorrect total-rank attribution in an archived letter was ours. Verification: **primary-source-inspected**.


## Braids, representations and class theorems


### HHS24

Mikami Hirasawa, Ryota Hiura and Makoto Sakuma. [The equivariant genera of marked strongly invertible knots associated with 2-bridge knots](https://arxiv.org/abs/2312.06156v2). arXiv:2312.06156v2.

Proposition 2.2 supplies the scope distinction between side-preserving and side-exchanging inversions. Verification: **metadata-checked; proof-locator-in-archived-audit**.


### BIGELOW03

Stephen Bigelow. [Representations of braid groups](https://arxiv.org/abs/math/0304212). Proceedings of the ICM, Beijing 2002, vol. 2, 37–46; arXiv:math/0304212.

Homological representations and pairings: background, not justification for an unproved specialization-faithfulness inference. Verification: **metadata-checked**.


### FUNARKOHNO14

Louis Funar and Toshitake Kohno. [On Burau representations at roots of unity](https://arxiv.org/abs/0907.0568v4). Geom. Dedicata 169 (2014), 145–163; arXiv:0907.0568v4.

Section 3, particularly Proposition 3.5 and Lemma 3.4 on the odd sequence, in finite-index pattern arguments. Verification: **archived-primary-audit**.


### JONESREZNIKOFF06

Vaughan F. R. Jones and Sarah A. Reznikoff. [Hilbert space representations of the annular Temperley–Lieb algebra](https://msp.org/pjm/2006/228-2/pjm-v228-n2-p02-p.pdf). Pacific J. Math. 228 (2006).

Section 2, Theorem 2.1 and preceding discussion: positive unitary specialization used in the TRUSTED constant-braid restriction. Verification: **archived-primary-audit**.


### FLW02

Michael H. Freedman, Michael J. Larsen and Zhenghan Wang. [A modular functor which is universal for quantum computation](https://www.microsoft.com/en-us/research/wp-content/uploads/2017/09/universality-02.pdf). Commun. Math. Phys. 227 (2002), 605–622.

Equations (14)–(15) for a unitary path model; no generic exact-gate universality is inferred. Verification: **archived-primary-audit**.


### LT88

W. B. R. Lickorish and Morwen B. Thistlethwaite. [Some links with non-trivial polynomials and their crossing-numbers](https://www.e-periodica.ch/cntmng?pid=com-001%3A1988%3A63%3A%3A32). Comment. Math. Helv. 63 (1988), 527–539.

Adequacy and adequate-link nontriviality; semiadequate extreme-coefficient constraints and partial Montesinos results. Do not attribute Stoimenow’s broader semiadequate theorem to this paper. Verification: **archived-primary-audit; bibliographic record checked**.


### STOIMENOW11

Alexander Stoimenow. [Coefficients and non-triviality of the Jones polynomial](https://arxiv.org/pdf/math/0606255v1). J. Reine Angew. Math. 657 (2011), 1–55; DOI 10.1515/crelle.2011.047; arXiv:math/0606255v1.

Pinned v1 Theorem 4.1, Corollary 4.1, Proposition 4.3 and Corollary 6.3: semiadequate, Montesinos, Whitehead-double and 3-braid nontriviality. V2 is retitled Non-triviality of the Jones polynomial and the crossing numbers of amphicheiral knots; do not transfer v1 locators without checking. Verification: **primary preprint metadata checked; theorem locators and journal metadata from archived audit**.


### TUZUNSIKORA22

Robert E. Tuzun and Adam S. Sikora. [Verification of the Jones unknot conjecture up to 22 crossings](https://arxiv.org/abs/1606.06671). J. Knot Theory Ramifications 27 (2018), 1840009; DOI 10.1142/S0218216518400096; arXiv:1606.06671.

Earlier computer verification, superseded in crossing range by the 24-crossing paper. Verification: **archived-primary-audit**.


### TUZUNSIKORA23

Robert E. Tuzun and Adam S. Sikora. [Verification of the Jones unknot conjecture up to 23 crossings](https://arxiv.org/abs/1809.02285). arXiv:1809.02285.

Intermediate verification; included to distinguish historical crossing bounds. Verification: **archived-reference**.


### TUZUNSIKORA24

Robert E. Tuzun and Adam S. Sikora. [Verification of the Jones unknot conjecture up to 24 crossings](https://arxiv.org/abs/2003.06724v2). arXiv:2003.06724v2, 23 March 2021; J. Knot Theory Ramifications, DOI 10.1142/S0218216521500206.

Established computational crossing bound used in the ledger; no inference beyond 24 crossings. Together with Sikora v2 Proposition 25, controls rational-tangle comparisons of total crossing number below 24. Verification: **metadata-checked; substantive-locators-from-archived-audit**.


### FLWDENSITY02

Michael H. Freedman, Michael J. Larsen and Zhenghan Wang. [The two-eigenvalue problem and density of Jones representation of braid groups](https://arxiv.org/abs/math/0103200). Commun. Math. Phys. 228 (2002), 177–199; arXiv:math/0103200; DOI 10.1007/s002200200636.

Density input in quantum-representation discussions; distinct from the universal-modular-functor paper FLW02. Density or approximation does not supply generic exact-gate realizability. Verification: **metadata-checked; original proof not re-audited**.


### DASBACHLOWRANCE18

Oliver T. Dasbach and Adam M. Lowrance. [Invariants for Turaev genus one links](https://arxiv.org/abs/1604.03501v2). Comm. Anal. Geom. 26 (2018), no. 5, 1103–1126; arXiv:1604.03501v2.

At least one extreme Jones coefficient has modulus one for Turaev-genus-one or almost-alternating links. Used to position E6, whose asserted extremes both have modulus two; it does not independently verify E6. Verification: **metadata-checked; substantive-locators-from-archived-audit**.


## Version-specific proof discussions


### BBB26

Vasudha Bharathram, Joan S. Birman and Tara E. Brendle. [The Burau representation is faithful for n = 4](https://arxiv.org/pdf/2607.05283v2). arXiv:2607.05283v2, posted 14 September 2026; paper dated 15 September.

V2 Section 3 equation (1), Lemma 3.1, Observation 2.1; Proposition 6.7, Corollary 6.8, Theorems 2.3/6.9 and Corollary 1.1. The project reports an apparent gap in the combined preparation/parity/count argument, with AI-only checks; the main theorem is not refuted. Modified-loop parity concerns were also raised in an earlier AI review of v1. Verification: **primary-source-inspected**.


### CC26

Avishy Carmi and Eliahu Cohen. [On trivial Jones–Vassiliev polynomials](https://arxiv.org/pdf/2606.22410v1). arXiv:2606.22410v1.

Proposition 5.12 (pp. 39–40), Theorem 5.6 (pp. 30–31) and Lemma 5.8 (pp. 31–33): joint universal residual package challenged by the explicit family. Theorem 6.8 (pp. 50–53) uses Theorem 5.11 and Lemma 5.8; Theorem 6.9 (p. 53) claims Jones detection. The project’s conclusion concerns a proof gap, not false main theorems. Verification: **primary-source-inspected**.


### PITH26

pith.science (AI-generated review). [Review of arXiv:2607.05283v1](https://pith.science/paper/2607.05283). Recorded in the project’s November audit as posted 7 July 2026.

Prior modified-loop parity concern credited by the BBB note. This is an AI review, not specialist endorsement; the project does not claim that concern as new. Verification: **archived-attribution; page could not be reopened in handoff edit**.


## Complexity


### HLP99

Joel Hass, Jeffrey C. Lagarias and Nicholas Pippenger. [The Computational Complexity of Knot and Link Problems](https://arxiv.org/abs/math/9807016). J. ACM 46 (1999), 185–211; arXiv:math/9807016v1.

Theorems 1.1–1.2 put unknot recognition and splitting in NP. Section 1, p. 6 of v1 credits Welsh’s 1993 conditional P^#P observation; input to the project’s routine conditional complexity refinements. Verification: **metadata-checked; proof-locator-in-archived-audit**.


### LACKENBY21

Marc Lackenby. [The efficient certification of knottedness and Thurston norm](https://arxiv.org/abs/1604.00290v3). Adv. Math. 387 (2021); arXiv:1604.00290v3.

Theorem 1.1: knottedness in NP; no GRH assumption is needed for this input. Verification: **metadata-checked; proof-locator-in-archived-audit**.


### KUPERBERG15

Greg Kuperberg. [How Hard Is It to Approximate the Jones Polynomial?](https://theoryofcomputing.org/articles/v011a006/). Theory of Computing 11 (6) (2015), 183–219; arXiv:0908.0512.

Theorem 1.2 concerns promised root-value distinctions and Cook–Turing hardness, not exact full-polynomial many-one JT2 hardness. Verification: **primary-source-inspected**.


### WOCJANYARD

Pawel Wocjan and Jon Yard. [The Jones polynomial: quantum algorithms and applications in quantum complexity theory](https://arxiv.org/abs/quant-ph/0603069v3). arXiv:quant-ph/0603069v3.

Theorems 8.3–8.4 concern bits of normalized root evaluations, not the full unit fibre. Verification: **archived-primary-audit**.


### BARNATAN95

Dror Bar-Natan. [Polynomial invariants are polynomial](https://www.math.utoronto.ca/drorbn/papers/poly/poly.pdf). Math. Res. Lett. 2 (1995), 239–246; arXiv:q-alg/9606025; author PDF edition 30 June 1996.

Theorems 1–2 concern a fixed finite-type invariant: O(n^m) evaluation and C n^m magnitude. They do not control C as m grows. Remark 1.1 announces links/tangles without proof. The project’s uniform Jones-jet and link estimates therefore use separate direct skein arguments. Verification: **primary-source-inspected**.


### JVW90

François Jaeger, Dirk L. Vertigan and Dominic J. A. Welsh. [On the computational complexity of the Jones and Tutte polynomials](https://doi.org/10.1017/S0305004100068936). Math. Proc. Cambridge Philos. Soc. 108 (1990), 35–53; DOI 10.1017/S0305004100068936.

Classical exact evaluation hardness, including Jones polynomials of alternating links. This does not establish many-one hardness of exact equality to a fixed whole unlink polynomial. Verification: **primary publisher metadata and abstract checked**.


### WELSH93

Dominic J. A. Welsh. [Complexity: Knots, Colourings and Counting](https://arxiv.org/pdf/math/9807016v1). London Math. Soc. Lecture Note Ser. 186, Cambridge University Press (1993).

Credited via HLP Section 1, p. 6: an affirmative Jones conjecture yields a P^#P unknot-recognition algorithm. The project’s conditional complexity sandwich and coefficient-counting membership observations carry no novelty claim. The linked source is the checked attribution, not the original monograph. Verification: **archived-primary-audit of HLP; original monograph not reopened**.
