# CLAIMS LEDGER (cx counterexample lane): completeness critic
Critic: Claude, 17 Nov 2026, 06:03-06:58 CST.  Working folder: mont/cx/critic/ (scripts, logs, certificates).  Nothing outside
critic/ and this file was edited, with ONE incident (section 6).  Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.
CERTIFICATION STANDARD (used exactly): CERTIFIED_UNKNOT only by (a) a diagram of K with <= 24 crossings and V_K = 1 (Tuzun-Sikora),
(b) a replayable Tietze reduction of pi_1(S^3 - K) to <a | > (Dehn), (c) validated Reidemeister reduction to 0 crossings.
CERTIFIED_NONTRIVIAL only by an explicit nonabelian representation checked on every relator.  Everything else UNRESOLVED.
Status words for CLAIMS:
  CERTIFIED     every J = 1 knot of the region is certified by (a)/(b)/(c) (or, for an infinite family, a PROVED isotopy or
                PROVED identification plus certified members) AND coverage of the region is proved.
  NCH           "no certified nontrivial hit": what was examined holds no certified nontrivial J = 1 knot, but coverage or
                per-knot certification is incomplete.
  UNJUSTIFIED   the claim is stated more strongly than its basis (e.g. det/Delta or V = Delta = 1 used as an unknot test).
  EMPTY-EXACT   exact computation (or a theorem) finds NO unit J at all; no knot needs certifying; the status is that of the
                computation/theorem, not of any unknot identification.
Certifier used by the critic: a COPY of the audited, fixed cert/run/code (critic/code; only sys.path strings re-pointed,
`diff` = paths only), run as cert_words.py; every certificate re-checked in a fresh process by BOTH independent checkers
(replay.py and audit-2's a2lib) via verify_sample.py at fraction 1.0.

## STATUS
- 06:55 FINAL.  NO HIT, no COUNTEREXAMPLE, no LEMMA_Q_HIT, no HIT file.  Open items: section 3.
- New this pass: (i) engineA's 169 stored units CERTIFIED (27 of them contain general bodies and had only det/Delta);
  (ii) 14,264 unit lines + 526 unit planes of the (6,6) template census were never enumerated (non-geometric bottom dedup):
  now classified with regress's own classifier (all PROVED types, 0 type R) and their 5,343 base knots CERTIFIED;
  (iii) all 2,604 > 24-crossing base knots of regress's lines (incl. the 412 'one knot UNRESOLVED' bases) CERTIFIED with the
  audited tool; (iv) SWAP-SUM LEMMA (PROVED): every type-R family is axis-free, hence K_k = K'_k # rK'_k with K'_k a 4-plat,
  and det = 1 at 7 points (3x3 grids for planes) forces K_k = unknot for ALL k: the 764 lines + 572 planes of type R are
  CERTIFIED by proof; (v) INDEPENDENT SECOND PROOFS for the whole (6,6) census incl. the missed families: swap-sum route
  56,012 lines, cert/run's Lemma K route 85,652 lines (0/400 on E/R negative controls), planes 1,597 of 2,537; only 4,178
  type-E lines and 940 planes rest on regress's global-disc argument alone; (vi) engineC2's 11,481 + 65 J = 1 theta-curves
  are still UNJUSTIFIED (presumed trivial), the largest open item.

## 1. Claims table (emptiness claims and "J = 1 configuration is an unknot" identifications)
| # | claim (source) | status now | basis / what is missing |
|---|---|---|---|
| B1 | engineB 2(iii): all width-two theta-curves s.l1.l1.W.u2.u2, \|W\| <= 14 (207M knots): every J = 1 is an unknot (\|W\| <= 12) or 'presumed unknot' | CERTIFIED EMPTY (as repaired by cert/run); engineB's own argument UNJUSTIFIED | cert/run: all 685,033 J = 1 survivor pairs (633,260 words) certified by the audited tool; tops geometric (Lemma K, 9,758/9,758); bottoms NOT geometric (420 missed classes) -> 69,928 missed J = 1 junctions + 420 missed-pair closures certified; zeta_7/zeta_10 tests exact necessary conditions; spot checks 431/431. Trusted: rho_2 == lp.J (CHECKED 1,276 + 20,000 junction spot check), alex.py's K, Tuzun-Sikora, Dehn |
| B2 | engineB: \|W\| <= 12 'rigorous via the 24-crossing verification' | CERTIFIED (sub-region of B1); original argument UNJUSTIFIED | engineB used modular V_K on representatives only, with a non-geometric bottom dedup; extract re-did exact V_K on all 276,085 words; cert/run repaired coverage |
| B3 | engineB 4(c): window (4,4), \|m\|,\|n\| <= 6 (9.8M theta-curves), 154,869 J = 1 'presumed unknots', HITS 0 | CERTIFIED EMPTY | cert/run: 131,473 J = 1 words + 5,878 theta-curves of the 2 missed depth-4 bottom classes certified; extract independently (word moves + Tietze); 306/306 random J = 1 window points in the list |
| B4 | engineB 2(iii): 76,584 covector-coincidence closures are (presumed) unknots; 'no non-geometric covector stabiliser, bottom dedup validated to depth 8' | closures CERTIFIED (76,584/76,584, two lanes); the dedup claim REFUTED | 698 coincidences are different bottom tangles (kernel test + S_3 boundary reps), 2 already at depth 4; suspected mutation (CONJECTURE) |
| B5 | engineB 2(ii)/cert: 36,764 top re-hit closures (depth <= 8) are unknots; cap-side state map injective | CERTIFIED (closures); injectivity CONFIRMED geometric to depth 7 (Lemma K) | builder certify.py (pre-fix tool, sound for UNKNOT per both audits) |
| B6 | engineB 4(c): (6,6) seven-sector screen, '7,366 unit lines, all unknot families; unit lines only along (0,1),(1,0); (iv) one site scalar' | UNJUSTIFIED as stated (filter artefact); the corrected census is rows R1-R5 | template_screen.py dropped every 'trivial' (identically constant) direction and \|NZ\| = 1 junctions: 124,212 lines + 2,011 planes missed at (6,6); (iv) describes lines that were not counted |
| B7 | engineB 3: guided searches E3/E3b/E3c/E3d 'HITS 0' | NCH | J = 1 configurations with kcert V = Delta = 1 were discarded unstored and uncertified; only width-two n <= 14 is covered by B1; n = 16..40, width three (E3c) and E3d are not; the annealing is not reproducible |
| R1 | regress: corrected (6,6) census = 131,578 unit lines + 2,011 unit planes (and (5,5) 33,414 + 789), 'every unit line classified' | UNJUSTIFIED as a complete census -> repaired here | census_fixed.py reuses mitm.bfs, i.e. engineB's non-geometric bottom dedup. Critic: behind 73 bottom representatives hide 82 missed tangle classes (depth <= 6), giving 14,264 unit lines + 526 unit planes never seen ((5,5): 2,090 + 154, a subset). All 14,790 classified with regress's own classify2/classify3 (read-only): SITE-STAB 12,700, JOINT-STAB 1,564, PLANE-GEO 36, PLANE-PARTIAL with global T-disc + half 490, NONE/R 0; their 5,343 distinct base knots CERTIFIED_UNKNOT (Tietze, 3-30 crossings, both checkers 5,343/5,343). Same status as R2 |
| R2 | regress: types S1, S2, J1, J2, E have PROVED isotopies; 130,300 lines + 1,439 planes CERTIFIED; 514 (+9 at (5,5)) lines 'one knot, base > 24, UNRESOLVED' | CERTIFIED; isotopy now independently re-proved for all but 4,178 E lines + 940 planes (section 4: swap-sum 56,012 lines, Lemma K 85,652 lines incl. missed) | critic re-certified ALL 2,604 distinct > 24-crossing base words (25-36 crossings) with the audited tool: 2,604/2,604 CERTIFIED_UNKNOT, both checkers; this covers the 412 distinct 'unresolved one-knot' bases and supersedes regress's own (unaudited) tietze.py certificates. <= 24-crossing bases: exact V_K = 1 (project bracket) = route (a) |
| R3 | regress type E (6,602 lines at (6,6)): 'PROVED (global disc, Dehn on the sphere around the H-tree, Whitehead)'; cert/run (05:50) on the same 7,366 offset lines: 'CONJECTURE' | PROVED per regress, disputed; independent proof for the axis-free subset (section 4) | cert/run only tested one-sided half stabilisers (0/7,366) and never evaluated regress's global-disc argument; the two reports conflict. Critic: the 2,424 axis-free E (0,1) lines are independently PROVED by the SWAP-SUM route (exact det = 1 at k = -2..2 on 2,424/2,424, rlines/edet.py); the other 2,462 E (0,1) + 1,716 E (1,0), and 450 geo planes + 490 missed planes whose site needs the global T-disc, rest on disc_test.py alone (U2); Lemma K finds no stabiliser on E lines (0/200 control), as expected |
| R4 | regress type R: 764 lines + 572 planes (R directions) at (6,6), 76 + 176 at (5,5): 'UNRESOLVED (no isotopy)' | CERTIFIED (PROVED identification, section 4) | all 1,440 R families (764 lines + 676 plane directions; the (5,5) ones are a subset) reduce to AXIS-FREE families; SWAP-SUM LEMMA => K_k = K'_k # rK'_k, K'_k a 4-plat; det K'_k = \|p(k)\|, deg p <= 1; exact det(K_k) = 1 at k = -3..3 on all 1,440 families and on the 3x3 grid of all 104 double-R planes => K_k = unknot for every k. The 2,182 + 200 R points regress left 'V = Delta = 1 UNRESOLVED' are covered |
| R5 | regress: WIDTH2-UNIT-LINE-GEO (unit line => geometric stabiliser; only (1,0),(0,1),(1,-1)) | CONJECTURE (CHECKED on (5,5)/(6,6) incl. the 14,790 missed) | R lines are not stabiliser lines in the (a)-(c) sense; they are unit lines because every member is K' # rK' with K' trivial. Beyond depth 6 junctions: unexamined (GAP, nobody claims it) |
| R6 | Codex fixed template s.l1.l1.x2.x1.x1^(2m).y3^(2m).x1.u2.u2 (and the second unit line m+n = -1) | CERTIFIED for all m | cert/run Lemma K (x1x1.y3y3 stabilises T(x2.x1)) + 6-crossing base; regress J1; extract k in [-6,6]; builder \|m\| <= 10. The m+n = -1 line is a census line (R2) |
| C1 | cert/run: '\|W\| <= 14 and window CERTIFIED EMPTY; unresolved.json = []; S1/S2/S3a/S3b all certified' | CERTIFIED (agree) | audited tool, 5% + 100% re-checks by two checkers; soundness gate passed before use |
| C2 | cert/run: '7,366 offset lines: NCH, unknot family CONJECTURE; constant-J lines unexamined outside the window (GAP)' | SUPERSEDED | the 7,366 = 6,602 E (R3) + 764 R (R4); constant-J lines of (5,5)/(6,6) junctions examined by regress + critic (R1, R2) |
| A1 | engineA E1: R(8) single-child roots, 142 units 'all det = Delta(2) = Delta(3) = 1 (2-bridge unknots: sanity)' | was UNJUSTIFIED -> now CERTIFIED (142/142) | critic: halfwords rebuilt from e1_L0.pkl with engineA's vc (read-only), Tietze certificates, 127 with <= 24 crossings, 15 with 25-43; both checkers 142/142; exact lp.J = 1 re-checked on 82 (others timed out, not needed for the unknot claim) |
| A2 | engineA e2_test.pkl (test run of E2, not in the REPORT): 27 two-child units with GENERAL bodies g0/g8/g13/g24 and nested general boxes, checked by units2.py (det, Delta(2), Delta(3)) only | was UNJUSTIFIED (no 2-bridge argument exists for general bodies) -> now CERTIFIED (27/27) | Tietze certificates, 10 with <= 24 and 17 with > 24 crossings (max 43), both checkers 27/27; J = 1 re-confirmed 27/27 by engineA's exact vector calculus (vc.Jtree) on the same trees, halfwords identical to vc.hw |
| A3 | engineA sec. 2: Lemma W brute-force validation, 167 horizontal + 308 vertical units in random rational products | UNJUSTIFIED under the standard (not stored) | mathematically two-bridge with det 1 (units only at n <= 1 by Q-MONT / V3), so harmless; no region claim depends on them. Regenerate with a fixed seed and certify, or drop the sentence |
| A4 | engineA sec. 4-5, 7: every '0 units' region (E1 Montesinos 2.76M + G-lib 1.0M candidates, E2 lib B / 100 posb / d2pos pairs, E4/E9, E6, E7, E11 R(8)/R(7)/R(5)/R(4), e11_mix, d2pos singles) | EMPTY-EXACT (CHECKED); nothing to certify | exact vector calculus (CHECKED 38 + 38 vs lp.J) + Lemma W windows (PROVED) + stated completeness arguments; much of it later PROVED by C1 (V3), lpgen (M300, D36), arb (4a, 4c), all modulo Theorem V's skein dictionary (refV3 G1). Not claimed and correctly so: library A deep stages, E11 R(6) n <= 6 |
| E1 | engineC2 sec. 5-6, 10: class S2 two-pole symmetric plats \|W\| <= 7: 11,481 J = 1 words, E4: 65 unit (box, N) pairs, periodic families (aB)^n etc. 'presumed trivial / certified-trivial' | UNJUSTIFIED; region S2 \|W\| <= 7 is NCH | identification = constituent A_1 u k 'unknotted' (V test only) + sister invariant a unit: necessary conditions, not certificates (integrator 03:45 agreed: 'join the certification queue'); no lane has certified them (grep, 06:40) |
| E2 | engineC1, roundD lpgen/refV3, roundE arb/refM300, engineC2 S-necklace 'REGION CLOSED': no unit J in their regions | EMPTY-EXACT / PROVED (modulo Theorem V's skein dictionary) | units they report are only 2-bridge unknot sanity cases (refV3: n = 1, a = +-1; arb pretzel n0: (a,N) = (+-1,0),(1,1),(-1,-1)), identified structurally; the 4 arb words (s.l1.x2.u1, s.l1.y0.x2.u1, s.l1.y2.u1, s.l1.x0.y2.u1: exact J = 1) CERTIFIED 4/4 by the critic (sanity/), refV3's n = 1 units not done (trivially certifiable); the theorems themselves not re-examined here |

## 2. engineA unit identifications (task item)
 engineA's REPORT says 'every unit is verified by halfword, det and Delta(2), Delta(3)' (units.py, units2.py).  Under the
 standard this is NOT a certification: det = Delta(2) = Delta(3) = 1 holds for Alexander-trivial knots (KT, Conway, the E3d
 knots), and for the 27 general-body units there is no two-bridge argument.  The stored units are exactly: e1_L0.pkl 142
 (R(8) single-child roots: 114 horizontal, 28 vertical) and e2_test.pkl 27 (two-child test run); every other engineA pickle
 has units = 0 (critic scan of all 30 pickles).  CRITIC RESULT (critic/engA/): 169/169 CERTIFIED_UNKNOT (Tietze; 32 of them
 have 25-43 crossings, so route (a) would not have applied), re-checked by both independent checkers 169/169
 (verify_units.json); J = 1 re-checked exactly with lp.J on 82/82 completed (87 exceeded the time limit).  So engineA's
 identifications were correct, but they were unjustified until now.  The Lemma W validation units (A3) were never stored.

## 3. What remains uncertified, and the cheapest route
 U1 engineC2: 11,481 S2 J = 1 theta-curves (\|W\| <= 7), 65 E4 unit pairs, the identically-J = 1 periodic families
    ((aB)^n, (AAbd)^n, (Ab)^n, (BB)^n).  Cheapest route: they are 'presumed trivial THETA-CURVES', so certify triviality of
    the theta-curve from engineC2's own event lists (no translator to halfwords needed): Wirtinger presentation of
    pi_1(S^3 - Theta) (arcs, crossing relations, vertex relations) reduced by the existing Tietze code to F_2 with 0 relators,
    plus the three constituent knots certified unknotted (Tietze); then Theta is planar (Scharlemann-Thompson: a graph is
    planar iff every proper subgraph is planar and the exterior is a handlebody; free pi_1 of an irreducible exterior gives
    the handlebody), and K = lift of k is the unknot (unique inversion).  Alternative: build K's Morse word from the circle
    model and run certify.py.  The periodic families need a family argument (or the swap-sum test of section 4 if axis-free).
 U2 regress type E lines not axis-free: 2,462 E (0,1) + 1,716 E (1,0) at (6,6) (and their (5,5) subsets), plus 450 geo
    planes and 490 census-missed planes whose site is explained only by the global T-disc: rest only on regress's
    disc_test.py (base knots and sample points certified, the infinite families not).  Cheapest: a referee read of disc_test.py / whitehead.py (one page of topology:
    is c'' really on S' and is Dehn applied to a curve on the boundary of B' - N(T')?), then a re-run with an independent
    implementation; or extend the swap-sum idea (R4) to these families.
 U3 DONE (was: regress's S1/S2/J1/J2 classifier unaudited): every S1/S2/J1/J2 line now has an independent proof
    (swap-sum or Lemma K, section 4); nothing left here.
 U4 engineB E3/E3b/E3c/E3d (width two n = 16..40, width three, Delta = 1 class): J = 1 configurations lost.  Not a region
    claim; cheapest: patch e3_search.py to store every J = 1 word and pipe it through certify.py inline; until then 'NCH'.
 U5 engineA Lemma W validation units (167 + 308): not stored; regenerate with a fixed seed and certify (minutes) or drop.
 U6 Junctions beyond the census depth (\|V\| or \|U\| >= 7 with an inserted double twist): unexamined; nobody claims them.
 U7 Structural black boxes behind every CERTIFIED region: rho_2 == lp.J (CHECKED, not PROVED), Theorem V's skein
    dictionary (for engineA/C1/roundD/E vertical results), alex.py as the definition of K, Tuzun-Sikora's 24-crossing
    verification, Dehn's lemma.

## 4. SWAP-SUM LEMMA and the type-R lines (critic, PROVED)
 LEMMA.  If the halfword s.l1.l1.W.u2.u2 has no axis letter (x0, y0), then K = K_L # rK_L, where K_L is the 4-plat with caps
 (L3 L2)(L1 L0), braid W (x_i -> sigma on legs i-1, i) and nested cups (L2 L1), (L3 L0).
 PROOF.  In the full symmetric picture (positions L4..L0 R0..R4, x0 -> sigma_4, x_i -> sigma_{4-i} sigma_{4+i}) the only
 crossings on the axis line are the sigma_4's, i.e. the axis letters; K meets the axis line only at the outer cap (L4,R4)
 and at the centre cup (L0,R0).  With no axis letter the plane through the axis perpendicular to the projection plane meets
 K in exactly these 2 points, so it is a summing sphere: K = K_L # K_R, K_R = h(K_L) with orientation reversed.  K_L: strand
 L4 runs crossing-free from the top axis point down to its cup with L3, and the axis segment closes L0's centre cup back up
 to the top point; both lie in the outer face, so together they form one cup (L3, L0) around the cup (L2, L1).  Two maxima:
 K_L is a 4-plat (2-bridge or trivial).  []
 FALSIFICATION TEST (rlines/swapsum_test.py): 150/150 random axis-free knots with V != 1 have V_K a perfect square; control
 with axis letters: 118/150 are not squares.  CHECKED.
 COROLLARY (PROVED).  For an axis-free family (one varying full-twist site), K_k unknot <=> det K'_k = 1, and det K'_k =
 \|p(k)\| with p of degree <= 1 (Conway skein at a twist site: affine recursion for antiparallel strands; double root i of
 x^2 - 2ix - 1 for parallel strands), so det K_k = det(K'_k)^2 = 1 at 3 points gives det = 1 and K_k = unknot for ALL k;
 joint (1,-1) sites: degree <= 2, 5 points; planes: bilinear, a 3x3 grid.
 APPLICATION.  Reduction moves that are isotopies for every member (right-angled cancellation with {x0,x2},{x0,x3},{x1,x3}
 and the varying block as a token; deletion of an axis letter that commutes to the bottom end = R1 at the bottom vertex):
 rlines/axisfree2.py.  ALL 764 + 676 type-R families at (6,6) are axis-free (the (5,5) ones are a subset), e.g. regress's
 'clean member' R_n = s.l1.l1.(x2.x2)^n.y3.y3.x1.x1.u2.u2 is axis-free outright.  Exact det(K_k) = 1 at k = -3..3 for all
 1,440 families (rdet.py) and on the 3x3 grid {-1,0,1}^2 for all 104 double-R planes (rgrid.py).  So every knot on every
 type-R line or plane is the unknot: R4 CERTIFIED (by proof + certified members; the standard's per-knot routes cover the
 sampled points only).
 SECOND, INDEPENDENT PROOF FOR EVERY AXIS-FREE LINE (rlines/alldet.py, exact det at k = -2..2, 5 points, enough for one site
 (3 needed) and for the joint (1,-1) site (5 needed)): 58,364/58,364 axis-free families have det = 1 at all 5 points:
 J1 40,562/57,872 lines, S1 (0,1) 8,846/38,348, S2 (0,1) 2,304/11,250, E (0,1) 2,424/4,886, R 764/764, planes: PLANE-geo
 597 + 597 directions, PLANE-with-R 572 + 572, census-missed (0,1) 1,112/12,512 and 14 missed plane directions.  So
 54,900 of regress's 131,578 (6,6) lines (41.7%) are PROVED unknot families without using regress's isotopy classifier.
 All (1,0) lines and all J2 lines carry axis letters (the varying x1-block does not commute with x0).
 LEMMA K ROUTE FOR THE REST (rlines/lemmak_lines.py = cert/run's lines_family.line_ok, exact kernel test in the full picture,
 PROVED criterion, no re-cuts): every NON-axis-free S1/S2/J1/J2 line: 85,652/85,652 have the varying block as a stabiliser of
 an adjacent top or bottom tangle (S1 (0,1) 29,502, S1 (1,0) 3,194, S2 (0,1) 8,946, S2 (1,0) 4,824, J1 17,310, J2 8,724,
 missed 13,152).  Negative control: 0/200 E lines and 0/200 R lines.  PLANES (rlines/planes_indep.py, rgrid_all.py): 755
 geo planes with both sites Lemma K, 234 with one Lemma-K site and an axis-free other direction, 36 missed planes both
 Lemma K, all 572 R planes 2-parameter axis-free with det = 1 on the 3x3 grid: 1,597 of 2,537 planes.
 BOTTOM LINE for the (6,6) template census incl. the missed families: 145,842 lines + 2,537 planes; independent proof
 for 141,664 lines + 1,597 planes; regress's global-disc argument alone for 4,178 E lines + 940 planes (all bases
 certified, all of them with certified sample points only).

## 5. Checks run by the critic (all under critic/)
 engA/: make_unit_words.py, cert_units.jsonl.gz (169 records, full certificates), verify_units.json, j_check.json.
 missed/: missed_lines.py (join of regress census with cert/run geo_bfs missed classes), classify_missed.py (+ .log),
   missed66_classified.json, cert_missed66_bases.jsonl.gz (5,343), verify_missed66.json.
 regbig/: big_bases_words.json (2,604), cert_big.jsonl.gz, verify_big.json.
 rlines/: swapsum_test.py, axisfree2.py, rfamilies.json, rdet.py (+ rdet66.json), rgrid.py, edet.py, alldet.py
   (+ alldet66.log/json), lemmak_lines.py (+ lemmak66.log/json), planes_indep.py, rgrid_all.py.  sanity/: 4 arb words.
 code/: copy of cert/run/code (paths re-pointed).  Load-aware: 3 processes throughout (load average 20-100).

## 6. Incident
 06:30 rlines/axisfree.py (first version) imported regress/certify_summary.py for its typ() function; that module runs at
 import and rewrote regress/out/certify_summary.txt and regress/out/big_bases.pkl.  Both were regenerated deterministically
 from unchanged pickles: same sizes (1,947 and 196,062 bytes), same printed table, same 2,604 + 68 base words (checked
 against the critic's earlier copy).  Only the modification times changed (06:30:51).  typ() is now copied, not imported.
