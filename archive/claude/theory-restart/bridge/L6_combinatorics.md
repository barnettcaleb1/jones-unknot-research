# L6 — Combinatorics / stat-mech / matroids / virtual knots lens
(agent notes, written continuously; started 2026-11-17)

Lens: bracket = Potts/Tutte-type partition function of a signed planar graph; virtual knots with V=1 exist, so planarity (genus 0) is essential to JC. Goal: bridges importing tools (ribbon graphs, delta-matroids, partial duality, zero-free regions, transfer matrices).

## Log
- [start] read CONTEXT.md.

## 1. The virtual mechanism, made precise (and corrected)

**Fact (Zulli 1995 / Traldi-Zulli arXiv:0808.3392 / Traldi JKTR 19 (2010)): the bracket factors through the SIGNED CHORD DIAGRAM.**
Gauss diagram of a (virtual) knot = circle, chords c_1..c_n, each with an arrow (over->under) and a sign eps_c.
Let M in Mat_n(GF2) be the interlace matrix (M_cd = 1 iff chords c,d cross), zero diagonal.
For R subset of chords, smooth crossings in R by the non-Seifert (orientation-reversing) smoothing, the rest Seifert.
Cohn-Lempel / Traldi (Europ. J. Combin. 32 (2011), arXiv:0903.4405): #loops(R) = 1 + nullity_GF2(M + I_R).
Positive crossing: A-smoothing = Seifert (checked on right trefoil). Hence with x = A^{-2}, d = -(x + 1/x):

  <D> = A^w * S(M,eps),   S(M,eps) = sum_{R} x^{eps(R)} d^{nullity(M + I_R)},   eps(R) = sum_{c in R} eps_c,
  V(t) = (-1)^w x^w S(M,eps),  t = x^2.        [checked by hand: right trefoil gives -A^5 - A^-3 + A^-7.]

So V sees only (M, eps): NOT the arrows. Virtualization of a crossing (flank by two virtual crossings + switch)
reverses the arrow and keeps the sign. That is the whole virtual mechanism: it moves along fibres of
  {virtual diagrams} --> {signed chord diagrams},  and the bracket is constant on fibres.
For a CLASSICAL diagram the arrows are recoverable from (Gauss code, signs) because the planar embedding fixes the
local orientation at each crossing (Gauss code realizable => curve unique up to reflection, and reflection+switch-all
is a rotation of R^3). So on the planar locus the forgetful map loses nothing.

=> Lesson: "virtual knots with V=1 exist" is NOT evidence that genus 0 is what JC uses. Virtualization examples have
EXACTLY the same signed chord diagram as a classical unknot diagram. The correct non-planar analogue of JC lives on
signed chord diagrams modulo Reidemeister moves = virtual knots modulo the Z-move (= graph-links of Ilyutko-Manturov,
arXiv:0810.5522, for realizable graphs).

**Literature check (done):**
- Fenn-Kauffman-Manturov conjectured: V=1 => Z-equivalent to a classical knot. REFUTED by Kauffman's knot KS
  (Gauss code 1232454315, five crossings, only crossing 3 even), via Manturov's parity bracket:
  L. Kauffman, Introduction to virtual knot theory, JKTR 21(13) (2012) 1240007, arXiv:1101.0665, Sec. 7, Fig. 12.
  Kauffman: no method other than the parity bracket was known to detect such examples.
- Open (Cheng, J. Math. Soc. Japan 69 (2017), arXiv:1511.08459, Sec. 2): is every nontrivial virtual knot with V=1
  obtained by virtualization? Is v(K) non-classical? (yes to both => JC). Silver-Williams JKTR 2004 "On a class of
  virtual knots with unit Jones polynomial" (knot group analysis).
- So: the non-planar analogue of JC IS FALSE, but the known failure is PARITY-DRIVEN (odd crossings).
  Gauss parity of a chord = its degree in the interlace graph mod 2. Classical => all chords even (Gauss 1800s).
  Even (all chords even) <=> checkerboard colourable virtual diagram <=> Z/2-null-homologous on the Carter surface.

## 2. Computation log (code in L6_code/: scd.py bracket via GF(2) nullity; enum.py enumeration)
- Formula verified: right trefoil t+t^3-t^4; figure-eight t^-2-t^-1+1-t+t^2 (correct sign pattern); KS word
  1232454315 has V=1 for 8 sign patterns (all with odd writhe 0). Consistent with Kauffman 2012.
- Enumerated ALL chord diagrams n<=6 (up to rotation/reflection), all signs (mod mirror). V=1 signed diagrams that are
  R1/R2-irreducible ("cores", R2 allowed for any adjacent opposite-sign pair since arrows are free mod Z):
    n=4: 1 core (odd)            n=5: 27 cores (22 odd, 5 EVEN)          n=6: 153 cores (127 odd, 26 EVEN)
- THE n=5 EVEN CORE: Gauss word 0120324314, interlace graph = 5-cycle C5 (all degrees 2 => checkerboard colourable),
  V=1 for 5 sign patterns. C5 violates Rosenstiehl condition (ii) (non-adjacent chords share 1 common neighbour), so it
  is NON-REALIZABLE in the plane (min Carter genus 1).  [CORRECTION: my hand check for R3 was wrong (I only looked
  at triples forming triangles in the interlace graph). Chords {1,2,4} DO form an R3 configuration.]
  Z/2-Khovanov homology (Manturov) depends only on (Gauss word, signs) => Z-move invariant. Implemented (kh2.py,
  checked on 3_1 and 4_1 incl. Z/2 torsion classes). Result: EVERY one of the 181 cores (n<=6) has Kh(Z/2) = unknot's.
- R3 rule for signed chord diagrams with free arrows (derived from three directed lines forming a triangle; zbfs.py):
  a=P12,b=P13,c=P23, s1=+1 iff a before b on strand 1, s2: a before c on strand 2, s3: b before c on strand 3;
  o=(s1s2, s1s3, s2s3); move valid unless eps_a o_a = eps_c o_c = -eps_b o_b (cyclic heights). Consistency check:
  Kauffman's KS (provably Z-nontrivial) is never trivialised by the search.
- Z-triviality search (zsearch2.py: closure under R1-,R2-,R3, iterative deepening on # of R2+ moves):
    EVEN cores: all 31 (5 at n=5, 26 at n=6) are Z-TRIVIAL, using NO increasing move.
    ODD cores: 92 trivialised, 58 not (<=1 increasing move), KS among the 58.
  Since R1/R2 reductions preserve evenness and V, this gives:
  **Fact (computer, exhaustive): every checkerboard-colourable (all chords even) signed chord diagram with <= 6 chords
  and V = 1 is Z-equivalent to the unknot.**  The non-planar failures at <= 6 crossings are all odd.
- Odd writhe: all 1300 V=1 signed diagrams with n<=5 have odd writhe J=0. Empirical congruence (1440 random signed
  diagrams, n=2..7, no exception): Im V(A=e^{i pi/4}) == J (mod 4). At A=e^{i pi/4}, d=0, so V(-1) is a sum over
  R with M+I_R nonsingular over GF(2) (a delta-matroid feasible-set sum). Unproved.

## 3. Propositions (with proofs)

**Prop 1 (parity lemma).** Let B be symmetric over GF(2), d = diag(B). Then d lies in col(B), and for any u with
Bu = d, rank(B) == u^T B u (mod 2).
Proof. q(x) = x^T B x = d.x is linear and vanishes on ker B, so d is orthogonal to ker B = col(B)^perp, so d in col(B).
B induces a nondegenerate symmetric form on GF(2)^n / ker B of dimension r = rank B. If d = 0 the form is
alternating and r is even, and u^T B u = d.u = 0. If d != 0 the form is non-alternating, hence (classical, over F_2)
has an orthonormal basis, i.e. is congruent to I_r; the "diagonal vector" of I_r is (1,..,1) = I_r(1,..,1), and
1^T I_r 1 = r. The class u + ker B and the value d.u are basis-independent. QED.
**Cor.** If the chord diagram is EVEN (M.1 = 0, Gauss's condition, <=> checkerboard colourable), take u = 1 for
B = M + I_R: (M+I_R)1 = 1_R = diag, so rank(M + I_R) == |R| (mod 2) for every R. Consequences:
 (a) every term of V has exponent parity n + |R| + null(M+I_R) == 0, so V in Z[t^{+-1}] (recovers Kamada, Osaka J.
     Math 39 (2002), arXiv:math/0008074, for knots);
 (b) changing one smoothing changes rank by exactly 1: the loop count always changes by +-1, i.e. NO 1-1
     bifurcations, so the Khovanov cube is made of merges/splits only, exactly as classically. Odd chords are the
     only source of half-integer exponents and of 1-1 bifurcations.

**Prop 2 (Z-faithfulness at the unknot).** If a classical knot K is Z-equivalent (virtual R-moves + Z-moves /
virtualizations) to the unknot, then K is the unknot.
Proof. Manturov's Khovanov homology with Z/2 coefficients (1-1 maps = 0; Izvestiya Math. 2007, arXiv:math/0601152)
is built from the cube of smoothings, whose circles and merges/splits depend only on (Gauss word, signs); Z-moves
change only arrows, so it is a Z-invariant, and on classical diagrams it is Bar-Natan's Kh(.;Z/2). So
Kh(K;Z/2) = Kh(U;Z/2) = (Z/2)^2. By Shumakovitch Kh(K;Z/2) = Khr(K;Z/2) (x) (Z/2)^2, so Khr(K;Z/2) has rank 1; by
universal coefficients rank Khr(K;Q) <= 1, so = 1, so K is the unknot by Kronheimer-Mrowka (Publ. IHES 113 (2011)).
QED. [Answers the K' = unknot case of Fenn-Ilyutko-Kauffman-Manturov problems 11(c), 24, arXiv:1409.2823.]
**Cor.** JC <=> every classical knot with V = 1 is Z-trivial. So JC is the planar case of a statement about SIGNED
CHORD DIAGRAMS modulo Reidemeister moves, where virtualization is invisible.

## 4. The Even Jones Conjecture (EJC) -- the genus-free, parity-respecting analogue
EJC. A checkerboard-colourable virtual knot (equivalently: one with an all-even Gauss diagram; equivalently a
"graphical" virtual knot coming from a signed ribbon graph = Tait graph on its Carter surface, Deng-Jin-Kauffman
arXiv:1712.06711) with V = 1 is Z-equivalent to the unknot.
- EJC => JC (Prop 2). EJC is strictly stronger. Not found in the literature (checked: FIKM problem list 1409.2823
  #11, #24; Kauffman JKTR 2012 Sec 7; Cheng 1511.08459 Sec 2; Deng-Jin-Kauffman 1712.06711).
- The all-virtual version (FKM, = FIKM #11(b)) is FALSE (KS, odd). Data: up to 6 crossings every failure is odd.
- What this says about planarity. Planarity of a Gauss diagram = (P1) Gauss evenness M.1 = 0 [linear over GF(2);
  = Z/2-null-homology on the Carter surface = Tait graph exists] + (P2) Rosenstiehl's quadratic conditions
  (non-adjacent chords share an even number of neighbours; adjacent pairs with an even number form a cocycle; de
  Fraysseix-Ossona de Mendez, DCG 22 (1999)) + arrow recoverability. Arrow recoverability only matters for the
  knot type, never for V (virtualization). (P1) is exactly what blocks the only known mechanism (parity bracket /
  odd crossings surviving smoothing). (P2) is NOT needed in our data: the C5 cores violate (P2) and are Z-trivial.
- In ribbon-graph language: EJC = "a signed ribbon graph (any genus) whose Jones specialisation of the signed
  Bollobas-Riordan polynomial (Chmutov-Pak, Moscow Math J 7 (2007), arXiv:math/0609012; Chmutov JCTB 99 (2009))
  is trivial is Z-trivial". Genus is allowed; what is forbidden is the non-checkerboard (non-graphical) world.
- In matrix language: EJC is a statement about pairs (M, eps), M a GF(2) symmetric zero-diagonal CIRCLE-graph
  matrix with M.1 = 0, under the graph Reidemeister moves (isolated vertex; opposite-sign twin pair; R3 = complement
  a triple {a,b,c} with N(a)+N(b)+N(c) = 0 outside, under the sign rule above). V is the loop-complementation sum
  of GF(2) nullities: a specialisation of the Brijder-Hoogeboom/Traldi interlace (transition) polynomial.

## 5. Why this could give leverage (honest)
- It relocates JC: the obstruction to Jones detection that the virtual world exhibits is parity (odd chords), not
  genus. If EJC is true, a proof may use only GF(2)-linear structure (M.1 = 0) and can use virtual R3 moves freely
  (no planarity bookkeeping). If EJC is false, the first even counterexample tells us exactly which part of
  Rosenstiehl's planarity JC needs. Either outcome is informative; up to 6 crossings EJC holds.
- Parity for OUR objects: the quotient 2-string tangle T / theta-curve carries a natural Manturov parity
  (mixed crossings between the two strands vs pure ones; R2 pairs share parity, R3 triples contain 0 or 2 mixed).
  A parity-bracket refinement of [T] = y b + x c keeps mixed crossings as graph vertices; a unit J would force
  cancellation of all graph-valued terms, a constraint invisible to J. Speculative; not developed.
- Cheap next steps: (1) extend the exhaustive even check to n = 7, 8 (only even words; enum.py has even_quick);
  (2) prove/disprove V=1 => odd writhe == 0 mod 4 via the d = 0 Gauss-sum at A = e^{i pi/4};
  (3) implement the parity bracket to certify the 58 odd survivors.

## 6. Shorter bridges (not developed)
- Split decomposition <-> Conway circles. A split V1|V2 of the interlace graph (complete bipartite between A1, A2)
  <=> the Gauss word is W1 X1 W2 X2 with no W-X crossings; for planar curves with A1, A2 nonempty, X lies in one
  complementary disc of the connected set W, giving a circle meeting K in 4 points (proof sketched in head; check).
  Cunningham's canonical split tree = canonical tree of Conway circles; Chmutov-Lando (AGT 7 (2007),
  arXiv:0704.1313) already use splits = mutations. Conjecture: arborescent diagram <=> interlace graph
  distance-hereditary (rank-width 1). Then rank-width (Oum) is a canonical width hierarchy beyond arborescent.
- Lemma Q as a two-terminal Potts problem: Tait graph of the quotient tangle = planar 2-terminal network; (x,y) =
  (cluster-separated, cluster-joined) partition functions at Q = t+2+1/t, v = -(1+t^{+-1}); rational = one-edge-at-
  a-time series-parallel, arborescent = series-parallel (Brylawski 2-sum formula = TL_2 coefficients); SPQR
  decomposition: R-nodes = basic polyhedra, so the first class beyond arborescent is one R-node (K4 -> 6*).
  t = -1 is Q = 0 (Kirchhoff / Goeritz). Mostly restatement; the new tool would be SPQR canonicity.
