# ROUND F / U2 REPORT: referee and independent re-run of regress's type-E global-disc argument
Lane folder: ~/jones-lanes/theory-restart/mont/cx/roundF/u2/  (Claude, 17 Nov 2026, started 07:00 CST).  Nothing outside u2/ was edited
(regress/ and critic/ data were only READ: pickles hold builtins only, no regress module was imported anywhere; HIT folder untouched).
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.  Family status: CERTIFIED = PROVED isotopy (every member isotopic to one knot) +
members CERTIFIED_UNKNOT by the audited tool; else UNRESOLVED (retained).  Standard exactly as in CLAIMS.md: (a) <= 24 crossings and
V = 1, (b) replayable Tietze reduction of pi_1 to <a|> (Dehn), (c) R-moves to 0 crossings; CERTIFIED_NONTRIVIAL only by an explicit
nonabelian representation checked on every relator.
Certifier: u2/code = COPY of the audited fixed cert/run/code (only the 9 sys.path strings re-pointed; `diff` = paths only);
certificates re-checked in a fresh process by BOTH checkers (replay.py and audit-2's a2lib) with verify_sample.py at fraction 1.0.

## STATUS
- 07:31 FINAL.  NO HIT (nothing CERTIFIED_NONTRIVIAL anywhere; no HIT file written).  ALL U2 families CERTIFIED (section 3):
  (6,6) 2,462 E (0,1) + 1,716 E (1,0) lines, 450 geo planes, 490 census-missed planes; (5,5) 1,062 + 222 E lines, 168 planes.
  UNRESOLVED: 0 (u2/out/unresolved.json = []).  Referee: regress's type-E LINE argument SOUND; its PLANE rule has a GAP as
  stated (section 1 viii), closed for every U2 plane by a stronger simultaneous criterion (2c).  New self-contained second proof
  (upstairs, section 2b) for every family; downstairs re-implementation reproduces regress exactly.
- 07:19 RESULT (indep/run.py, 56 s): ALL 9,382 families pass the NEW upstairs global-disc test (section 2b): every U2 family
  (2,462 + 1,716 E lines at (6,6), 1,284 at (5,5), 450 geo + 490 census-missed + 168 (5,5) planes) and the already-covered ones
  (2,424 axis-free (6,6) E (0,1) lines; 388 planes with a Lemma-K + swap-sum proof: 234 at (6,6), 154 at (5,5)).  The independent downstairs re-implementation agrees with regress on every family (0 disagreements).
- 07:00 skeleton.

## 1. Referee of regress's type-E argument (disc_test.py, whitehead.py, geo.py, classify3.py)   VERDICT: lines SOUND; planes GAP in
##    regress's stated rule, CLOSED here for every U2 plane (section 2c)
Setting (re-derived, CHECKED against geo.py/fgroup.py and the full picture of alex.symmetrize).  K = full symmetric diagram of
s.l1.l1.W.u2.u2; theta = A u k its quotient (A = axis circle, k = quotient arc).  The cut V|U of W = V.U is the boundary sphere S of
the ball T that holds the caps (L1 L0), (L3 L2), the braid V and the axis segment from g0 up to E (E just below v_top on the outer
cap); S meets theta in g0 (axis), g1..g4 (legs L0..L3) and E.  The complementary ball holds U and the closure: a PLANAR H-tree
(v_bot on the centre cup, v_top on the outer cap, A_seg = the axis between them through infinity; edges to g0, to leg 0, to E and,
via L4 and the cup (L4 L3), to leg 3) plus the cup (legs 1, 2).
 (i) Twist = Dehn twist about the site circle c (g1g2 for X1, g3g4 for X3) at the cut: theta_k = (S^3_{-1/k}(c), theta_0).  If c
     bounds an embedded disc in S^3 - theta_0, the surgery is trivial, theta_k ~ theta_0 with edge labels, and the double branched
     covers along A give K_k ~ K_0.  SOUND (standard).
 (ii) "c'' on S'": c'' = U_*(c) is the image of the simple closed curve c under the braid homeomorphism of the shell (its class is
     the Artin image, simple closed curves on a punctured sphere are determined by their free homotopy class).  The free-factor
     test (cyclic word in the basis {g0, g1, h = g2g3, g3, g4} has no g3) is EXACTLY "c'' is isotopic off the shadow arc beta of the
     cup": pi_1 of the level sphere minus N(beta) is the free factor <g0,g1,h,g4>; a curve homotopic into it has i(c'', h) = 0, can
     be isotoped off h, and cannot then sit inside N(beta) as a curve around g2 or g3 alone (those are not conjugate into the
     factor).  Off beta, c'' misses the cup disc and is pushed past the cup onto S' = dB_H (B_H = regular nbhd of the planar
     H-tree; the shell between the closure level and S' is a product with 4 straight strands because the tree is planar).  SOUND.
 (iii) pi_1(B' - T') = F_3 / << psi_V(U_*^-1(g2 g3)) >>: van Kampen over the top (F_3, psi_V = psi_0 o V_*^-1), the braid shell (F_5)
     and the closure shell minus the cup (F_5/<<g2g3>>).  It also equals pi_1(S^3 - theta) (B_H - H has the group of S' - 4 points),
     which is why regress's type-R remark "c is null-homotopic in pi_1(S^3 - theta)" is the same group test WITHOUT the boundary
     condition.  SOUND.
 (iv) Dehn's lemma: c'' is a simple closed curve on S' - N(4 points), a subsurface of d(B' - N(T')); null-homotopic in B' - N(T')
     => bounds a properly embedded disc there, i.e. a disc in S^3 - theta.  SOUND.  PRIMITIVITY (Whitehead) is used only to SOLVE
     the word problem: phi(r) = z^{+-1} cyclically gives F_3/<<r>> = F_3/<<z>> = free on the other two letters; greedy Whitehead
     reduction is complete for primitivity by peak reduction (non-primitive r returns 'undecided', never 'disc').  whitehead.py
     enumerates exactly the type-II automorphisms (a, A).  SOUND.
 (v) Re-cuts: the test is CUT-INDEPENDENT (every commuting letter fixes the site circle as a word, and
     r = psi_0((W^-1)_*(g2g3)) does not depend on the cut), so 'T-disc-recut' only records that classify3 tries the lowest cut first.
     CHECKED: both of my implementations give the same verdict at every reachable cut on all 9,382 families.  Harmless.
 (vi) 'H-vertex' (c'' ~ g0g1 on S') is geometrically valid but can never occur for a site circle (odd winding about the branch point
     a, whereas a site circle lifts to TWO circles); 0 occurrences.  'S-trivial' (c'' = the cup curve: the twist rotates the cup) is
     valid; it occurs for one site of every U2 plane.
 (vii) Lines: the test is run at the line's offset point (m0, n0) and the line is exactly the twist family about that point.  SOUND.
 (viii) GAP (planes, regress's rule 'both sites explained (each at some cut; top / bottom / global) => the whole (m,n) plane is one
     knot'): two single-site isotopies at the base point only prove the two coordinate lines through it.  For m n != 0 one needs one
     site's disc to survive the other site's twist: a global disc for X1 lies in B' - N(T'), which CONTAINS the X3 site circle, and a
     half-space disc for X3 may lie in a half that contains the X1 site.  Not justified as written.  It is CLOSED for every U2
     plane below (2c): BOTH sites pass the global test (one T-disc, the other S-trivial), so all site circles sit simultaneously on
     the boundary of the same handlebody-complement and the surgery induction applies.
 Downstairs verdict: the type-E LINE argument is a correct proof; regress's computation is reproduced exactly (section 2a).

## 2. Independent re-implementation and a second (upstairs) proof   [indep/; no import from regress or critic]
Files: indep/fg.py (free groups, Whitehead's algorithm for TUPLES of cyclic words, written from the definition), indep/down.py
(downstairs re-implementation of regress's test), indep/up.py (NEW upstairs test), indep/fam.py (family extraction from the
read-only pickles/JSON; typ() and the critic's axis-free reduction re-typed), indep/run.py (all families, every cut, Lemma K at
every cut for the plane sites, plane composition), indep/validate.py (falsification), indep/lemmak_lines.py, make_words.py.
2a. DOWNSTAIRS re-implementation (same theorem, own code: own Artin action, own psi_0, own cup-avoidance in the h-basis, own
 Whitehead).  Result on all 9,382 families: identical to regress on every family: every E line T-disc at every cut; every plane:
 one site T-disc, the other S-trivial.  CHECKED(9,382).
2b. UPSTAIRS proof (NEW; works with K itself, no quotient, no axis, no H-tree).  Full picture (alex.symmetrize): positions 0..9,
 caps (0,9),(1,2),(3,4),(5,6),(7,8), braid on 1..8 (x0 -> s4, x_i -> s_(4-i) s_(4+i)), cups (0,1),(2,3),(4,5),(6,7),(8,9).
 Strands 0, 9 never cross, so the outer arc cup(0,1)+strand 0+cap(0,9)+strand 9+cup(8,9) is swept across the outer face of the
 projection sphere to a big cup (1,8) below everything.  B_H~ := regular nbhd of (big cup u centre cup (4,5) u a planar arc
 joining them below the cups (2,3),(6,7)): a ball meeting K in two trivial arcs; B~' := its complement, a ball with
 T~' = K n B~' = 4 caps + braid + cups (2,3),(6,7).  Van Kampen: pi_1(B~' - T~') = F_4/<< psi_V(U^-1(a2a3)), psi_V(U^-1(a6a7)) >>.
 A site X3 (resp. X1) is a pair of twist circles C, C' around positions (1,2),(7,8) (resp. (3,4),(5,6)) at the cut.
 TEST: for C and for C': C'' = U_*(C) is cup-avoiding w.r.t. the shadows of (2,3) AND (6,7) (cyclic word in the basis
 {a1, a2a3, a3, a4, a5, a6a7, a7, a8} uses neither a3 nor a7) and psi_V(C) = 1 in F_4/<<r1, r2>> (decided by Whitehead reduction of
 the relator PAIR to single letters; anything else = 'undecided', never 'disc').
 THEOREM (PROVED).  If every site circle of a family passes, every member of the family is isotopic to the base knot.
 Proof.  The site circles of a family (2 for a line, 4 for a plane) are disjoint circles at one level; push the whole system down
 through U (an ambient isotopy of the braid shell, which keeps them disjoint) and, each being cup-avoiding (zero geometric
 intersection with the shadow arcs; a multicurve can be put in minimal position with the arcs simultaneously), off the two cup
 discs onto dB~'.  M := B~' - N(T~'); all circles now lie on dM - K.  Each is null-homotopic in M, so by DEHN'S LEMMA it bounds a
 properly embedded disc D_i in M (interior in int M, hence D_i misses K and every other circle).  Twisting along C_1 (-1/k surgery)
 is undone by the homeomorphism supported in a nbhd of D_1, which fixes K and the other circles; the images of the other discs
 are again discs bounded by their circles missing K and the remaining circles.  Induction over the circles: the multi-twisted
 knot is K itself.  [The discs may intersect each other; only "disc misses the other circles" is used.]  QED.
 For a line this is two circles (C, C'); for a plane four (both sites at the same cut; the test is cut-independent).  This is a
 self-contained proof that does not use regress's downstairs model; its conventions (Artin push-down / pull-up, adjacent caps and
 cups only) are those cert/run VALIDATED against proved moves, and they are re-validated here (2d).
 WORKED EXAMPLE (family 66-L59113, E (1,0), V = x0.x2, U = x2.y3.x1.x0.x1, offset (0,1), base 16 crossings): at the cut
 V | x3.x3.x2.y3.x1.x0.x1: r1 = c2^-1 c1 c2 c3^-1, r2 = c2 c3 c4^-1 c3^-1 (Whitehead -> (c1, c4^-1): quotient free on 2 letters);
 C = a3a4 -> C'' = a2^-1 a1 a2 a3 a4 a3^-1 (cup-avoiding), psi_V(C) = c2^-1 c1^-1 c2 c3 = 1 since c3 = c2^-1 c1 c2;
 C' = a5a6 -> C''' = a5 a8 (cup-avoiding), psi_V(C') = c3^-1 c2^-1 c3 c4 = 1 since c4 = c3^-1 c2 c3.  Both circles bound discs:
 every member is the base knot.  Downstairs: T-disc (regress: global:T-disc).
2c. PLANES.  Every U2 plane: BOTH sites pass the upstairs test (the S-trivial site is the cup-rotation: C'' = a2a3 around a cup;
 it is also a Lemma K bottom stabiliser, cert/run's PROVED criterion), so the 4-circle surgery induction proves the whole
 (m,n) plane is one knot.  This closes regress's plane GAP (1 viii) for all of them.
2d. VALIDATION of both implementations (not assumed):
 * Falsification (indep/validate.py, seed 2, 20,000 random templates |V|,|U| <= 6, one site, re-cuts; 2,608 knot families with the
   fingerprint (|Delta(-1)|, |Delta(2)|, |Delta(3)|) of K_k, k = -2..2, from tools/alex.py = the certifier's K): upstairs 'disc' on
   376 families, downstairs on 395, VIOLATIONS (disc verdict but non-constant fingerprint) 0 and 0; 1,080 families with a
   non-constant fingerprint, all rejected by both.  CHECKED(2,608).  The 19 (63 over all 20,000 words) 'downstairs yes / upstairs
   no' cases are all downstairs S-TRIVIAL (no word problem needed) where the upstairs relator pair does not Whitehead-reduce
   (the upstairs test always demands that reduction): conservative, no contradiction.
 * POWER of the falsification (seed 3, the same test with push-down and pull-up EXCHANGED): 456 upstairs and 534 downstairs
   violations among 3,529 knot families.  So a convention error would have been caught.  CHECKED.
 * Upstairs GROUP MODEL vs the certifier's knot (indep/model_check.py): the model's plat presentation
   F_4/<<psi_W(a2a3), psi_W(a4a5), psi_W(a6a7)>> gives #Hom(pi_1, S_3) = 3 + 3^(d+1) with #Hom > 6 exactly when 3 | det
   (det from alex.py) on 2,806/2,806 random knots (836 with 3 | det; counts 6/12/30/84).  On the 1,993 distinct U2 base words the
   relator triple Whitehead-reduces to 3 letters (group Z) on 1,925 (the other 68: a redundant relator is not Aut-reducible;
   Andrews-Curtis-type moves needed; irrelevant, all bases carry audited Tietze certificates).  CHECKED.
 * Cut-independence: both implementations give the same verdict at every reachable cut on all 9,382 families.  CHECKED.
 * Negative control: on regress's 764 type-R lines and the 676 R sites of the 572 PLANE-with-R planes the upstairs test says
   'not-cup-avoiding' for both circles every time (indep/rlines_up.py): it does not pass everything, and agrees with regress there.
 * Lemma K (cert/run, audited tangle_kernel) at EVERY reachable cut of all 7,886 E lines ((6,6) 6,602, (5,5) 1,284): 0 half
   stabilisers (out/lemmak_lines.json), as the definition of type E requires; so Lemma K gives no second proof for E lines.
   For planes, the S-trivial site is a Lemma K bottom stabiliser on every one of the 1,496 planes (run_results.json LK1/LK3).
 * Swap-sum lemma: not available for the U2 lines (none axis-free under the critic's reduction, re-typed in fam.py: (6,6)
   2,462 + 1,716, (5,5) 524 + 222 are not; the 2,424 + 538 axis-free E (0,1) lines are the critic's), nor for the U2 planes
   (no Lemma-K-site + axis-free-direction combination: critic_indep = 'regress only').

## 3. Results per family   [out/final_families.json; out/unresolved.json = []]
Rule: CERTIFIED iff the upstairs proof (2b/2c) passes for every site circle AND every member point (lines: k = -2..2 + base;
planes: (m,n) in {-1,0,1}^2 + base) is CERTIFIED_UNKNOT by the audited tool AND that certificate passes BOTH checkers.
| family set (U2) | families | upstairs proof (2b/2c) | downstairs re-impl. = regress | members certified | status |
|---|---|---|---|---|---|
| (6,6) E (0,1) lines, not axis-free | 2,462 | 2,462 | 2,462 T-disc | all | CERTIFIED 2,462 |
| (6,6) E (1,0) lines | 1,716 | 1,716 | 1,716 T-disc | all | CERTIFIED 1,716 |
| (5,5) E (0,1) lines (524 not axis-free + 538 axis-free) | 1,062 | 1,062 | 1,062 T-disc | all | CERTIFIED 1,062 |
| (5,5) E (1,0) lines | 222 | 222 | 222 T-disc | all | CERTIFIED 222 |
| (6,6) geo planes with a global site, 'regress only' | 450 | 450 (both sites) | T-disc + S-trivial | all | CERTIFIED 450 |
| (6,6) census-missed planes (PLANE-PARTIAL) | 490 | 490 (both sites) | T-disc + S-trivial | all | CERTIFIED 490 |
| (5,5) geo planes with a global site, 'regress only' | 168 | 168 (both sites) | T-disc + S-trivial | all | CERTIFIED 168 |
| (not U2, run for completeness) (6,6) axis-free E (0,1) lines; planes already covered by the critic ((6,6) 234, (5,5) 154) | 2,424 + 388 | all pass | all agree | (critic) | already CERTIFIED (critic) |
Members: 43,852 member points = 27,509 distinct halfwords (2-46 crossings; 11,524 with <= 24, 15,985 with > 24), certified by
u2/code/cert_words.py (3 processes): 27,509/27,509 CERTIFIED_UNKNOT, all by Tietze certificates (median 9 ms, max 0.33 s);
fresh-process re-check of EVERY certificate by BOTH checkers (verify_sample.py fraction 1.0, seed 31): 27,509/27,509 pass
(replay.py AND a2lib).  CHECKED(27,509).  Far points (extra evidence, not needed for the proof): k = +-6 on 300 random U2 lines
and (m,n) = (3,-2), (-2,3) on 100 random U2 planes: 800/800 CERTIFIED_UNKNOT (30-69 crossings), both checkers 800/800.
0 UNRESOLVED, 0 CERTIFIED_NONTRIVIAL, 0 COUNTEREXAMPLE / LEMMA_Q_HIT, no ALARMS; no HIT file.
CONSEQUENCE for CLAIMS.md: R3 and U2 are closed: every (6,6) type-E line (6,602) and every unit plane whose site needed the
global disc (450 geo + 490 census-missed) is CERTIFIED by a PROVED isotopy with certified members, now with TWO independent
proofs (regress's downstairs argument, refereed SOUND and re-implemented; the new upstairs argument), and regress's plane rule
is replaced by the simultaneous-circle criterion (2c).  Together with the critic's section 4 this leaves the (6,6) template census
(145,842 lines + 2,537 planes) with an independent proof for every family.  Remaining black boxes as in CLAIMS U7 (Dehn's lemma,
alex.py/a2lib as the definition of K, the audited certifier) plus the census COVERAGE questions R1/R5/U6, untouched here.

## 4. Files (all under roundF/u2/)
 code/   audited certifier copy (paths re-pointed only).  indep/  fg.py, up.py, down.py, fam.py, run.py, validate.py,
 model_check.py, lemmak_lines.py, rlines_up.py, make_words.py, final.py.  out/  families.json (9,382 families), run_results.json,
 final_families.json, unresolved.json ([]), member_words.json, member_points.json, far_words.json, validate_20000.json,
 validate_WRONG_20000.json, model_check.json, lemmak_lines.json, cert/members.jsonl.gz (+ verify_members.json), cert/far.jsonl.gz
 (+ verify_far.json), logs.  Load-aware: at most 3 worker processes (load average 30-50 from other lanes).
