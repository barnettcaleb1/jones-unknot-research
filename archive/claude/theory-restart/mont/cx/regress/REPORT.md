# REGRESS REPORT (WIDTH2-UNIT-LINE regression; Codex challenge 20261117-020642)
Lane: ~/jones-lanes/theory-restart/mont/cx/regress/  (Claude, 17 Nov 2026, started ~02:20 CST)
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.  Certification standard: CERTIFIED_UNKNOT only by (a) diagram <= 24 crossings
with V_K = 1, (b) Tietze reduction of pi_1 to <a|>, (c) Reidemeister reduction to 0 crossings; CERTIFIED_NONTRIVIAL only by a
nonabelian representation checked on every relator; everything else UNRESOLVED.

## STATUS (03:15)
- Steps 3/4: every unit line classified; 99.42% have a PROVED isotopy (types S1, S2, J1, J2, E); 764 type-R lines unresolved.
  Corrected conjecture in 4.3.  (b)-certifier (tietze.py) being validated for the > 24-crossing bases.
## STATUS (02:50, superseded)
- Step 1 DONE: template reproduced exactly; bug located (engineB/template_screen.py line 79: `possible(nz, d) is True`
  drops the 'trivial' return of line 40; line 77 drops |NZ| = 1).
- Step 2 DONE: corrected census (5,5) and (6,6) complete (section 3): 33,414 and 131,578 unit lines; (1,-1) is the
  largest class.  Step 3/4 (mechanism classification + certification) running.

## 1. Reproduction of the fixed template (V = x2.x1, U = x1, direction (1,-1), offset 0)  [DONE 02:35]
Files: step1_exact.py (+ out/step1_exact.log, .json), step1_trace.py (+ out/step1_trace.log); engineB code copied verbatim to
orig/ (only sys.path and output paths changed; `diff` recorded in this folder's history, see section 2).
- CHECKED (exact, sympy, engineB's exact_sectors module unchanged): in engineB's normalisation (X_i = t^2 M[x_i], phi = PHIT t^2/(1+t)^4)
    c00 = t^5/(t^2+t+1),  c22 = -t^5,  c44 = t^6 (t^4+t^3+t^2+t+1)/(t^2+t+1),  c02 = c20 = c24 = c42 = 0,  sum = t^8,
  ratio to Codex's values = 1 in every sector (same normalisation; Codex used engineB's JSON matrices).
- CHECKED: X1 X2 f0 = t^4 f2;  X1 f2 = X3 f2 = t f0 + (t^2+t^3) f1 + t^3 f2;  phi X1 f2 = t^4;  f2 is NOT an X1- or
  X3-eigenvector and phi X1 is NOT an eigen-covector (rank tests).  So neither site is scalar on either boundary.
- CHECKED lp.J: s.l1.l1.x2.x1.x1^(2m).y3^(2m).x1.u2.u2 has J = 1 for m = 0,1,2,3; (1,0) and (0,1) points give the same
  non-unit (span 9).  NEW: the parallel line m + n = -1 is ALSO a unit line: F = c00 + c22 u^s + c44 u^(3s) at s = m+n = -1
  equals (t^5 + Phi_5 - t^3 Phi_3)/Phi_3 = 1 exactly (lp.J(s.l1.l1.x2.x1.y3.y3.x1.u2.u2) = 1); s = 0 gives t^8.
- Trace through template_screen (seed 1, (5,5) enumeration): the junction IS enumerated (top representative ('x2','x1'),
  bottom representative ('x1',)), knot_ok = True, mod-p sector pattern nz = {00, 22, 44} (|NZ| = 3), and
    possible(nz, (1,-1)) = 'trivial'   (one nonzero equal-slope group {00,22,44})
    possible(nz, d) = False for the other 15 directions (three singleton groups);
  hence dl = [] and the junction is dropped by `if not dl: continue`.  Admitting (1,-1): all 49 offsets pass the
  single-group test, and exactly 2 are unit-valued (fastJ exact): m+n = 0 (J = 1, word x2.x1.x1) and m+n = -1
  (J = 1, word x2.x1.y3.y3.x1).

## 2. Why the diagonal was lost (diagnosis, offending lines)  [DONE 02:40]
DIAGNOSIS (CHECKED by the trace above): the cause is the candidate-direction filter of the line census, nothing else.
engineB/template_screen.py:
    40     if len(gs) <= 1: return 'trivial'      # at most one nonzero group: every line is J(0,0)-like
    77                     if len(nz) <= 1: continue
    79                     if key not in poss_cache: poss_cache[key] = [d for d in DIRS if possible(nz, d) is True]
    81                     if not dl: continue
possible() has THREE outcomes: False (>= 2 singleton groups: no unit line), True (>= 2 nonzero groups, a unit line can only
occur at an offset where all but one group cancel), and 'trivial' (all nonzero sectors share ONE slope in direction d).
Line 79 keeps only `is True`, so every 'trivial' (junction, direction) pair is discarded, and line 77 discards every |NZ| = 1
junction.  But 'trivial' is exactly the case "all but one equal-slope group vanishes IDENTICALLY" (Codex's criterion): F is
constant along EVERY line of direction d, and the line is a unit line whenever that constant is a unit.  It is the strongest
form of a unit line, and it is the only form that the mechanisms quoted by engineB (a site scalar on a boundary vector or
covector) can produce, because those mechanisms do not depend on the offset.  The comment's premise is also false: the
constant depends on the transverse offset (Codex's template: value t^8 on m+n = 0, value 1 on m+n = -1, non-units elsewhere),
so a 'trivial' direction is not "J(0,0)-like" and needs its own unit test at each offset.
Consequences for engineB's REPORT section 4(c):
  * the 1,840 / 11,870 "single-group lines" and the 1,360 / 7,366 unit lines are ONLY the offset-specific ones
    (>= 2 nonzero groups); every identically-constant line, in every direction, was never examined;
  * "unit lines occur only in directions (1,0), (0,1)" is an artefact of the filter (direction (1,-1) is the LARGEST class,
    section 3); and (iv) "one site acts by a scalar on one side" describes lines that were filtered out, not the lines
    that were counted (the counted ones are offset-specific, i.e. NOT one-site-scalar, see section 4).
Ruled out (each CHECKED on the trace): direction set ((1,-1) is in DIRS); sign convention of n (n > 0 <-> x3.x3, so Codex's
y3^(2m) is n = -m and the slope grouping e_a p + e_b q puts 00, 22, 44 together for (1,-1)); grouping of equal-exponent
sectors (correct); the unit test (fastJ returns J = 1 when the line is admitted); the junction enumeration (the junction is a
class representative and passes knot_ok); Hilden representatives (the representatives are the words x2.x1 and x1 themselves).
FIX (census_fixed.py): keep engineB's loop verbatim for `True`, and for 'trivial' test every one of the 49 offsets of the
direction (value of the single group at the random t in {+-t^k}); record |NZ| = 1 junctions as planes.

## 3. Corrected line census ((5,5) and (6,6), same junctions, same 16 directions)
Files: census_fixed.py (engineB loop verbatim for `True`; the fix for 'trivial'; planes), merge.py; logs out/census_*.log,
out/census_*_merge.txt, worker pickles out/census_D1_D2_w*.pkl (every unit line with its junction words, offset, supports).
REPRODUCTION CHECK: the fixed code reproduces engineB's numbers exactly where they overlap: (3,3): 4,031 knots, 18 offset-type
unit lines (engineB 18); (5,5): 868,361 knots, |NZ| histogram identical, 1,840 offset-type candidates = 1,360 unit + 480
non-unit (engineB: 1,840 = 1,360 + 480).
(5,5) CORRECTED COUNT (CHECKED, seed 1; unit test of single-group lines mod p at a random t, exact re-check in section 4):
   direction   offset-type (engineB)   single-group (MISSED)   total unit lines
   (0,1)            1,138                  12,720                13,858
   (1,-1)               0                  17,222                17,222
   (1,0)              222                   2,112                 2,334
   other 13             0                       0                     0
   TOTAL            1,360                  32,054                33,414
 plus |NZ| = 1 junctions ("planes", F = c u^(...) on the whole (m,n) plane): 3,105, of which 789 are unit-valued
 (each is a unit line in all 16 directions at all 49 offsets; not included above).
 Single-group pairs (junction, direction) exist ONLY in directions (0,1) [114,080], (1,-1) [79,530], (1,0) [5,696].
 Unit single-group lines by transverse offset r (q m0 - p n0): symmetric in r -> -r (mirror pairs); e.g. (1,-1):
 r=0: 4,388, |r|=1: 3,614 each, |r|=2: 1,924, |r|=3: 716, |r|=4: 149, |r|=5: 14.
(6,6) CORRECTED COUNT (CHECKED, 10 workers, 538 s wall; reproduces engineB exactly where they overlap: 13,263,181 knots,
 identical |NZ| histogram, 11,870 offset-type candidates = 7,366 unit + 4,504 non-unit, as in engineB's template_6_6.json):
   direction   offset-type (engineB)   single-group (MISSED)   total unit lines
   (0,1)            5,650                  49,598                55,248
   (1,-1)               0                  66,596                66,596
   (1,0)            1,716                   8,018                 9,734
   other 13             0                       0                     0
   TOTAL            7,366                 124,212               131,578
 plus 14,297 |NZ| = 1 junctions (planes), 2,011 of them unit-valued (unit lines in every direction at every offset).
 Single-group pairs (junction, direction): (0,1) 1,106,344; (1,-1) 664,000; (1,0) 43,974; none in the other 13 directions.
 Unit single-group lines by transverse offset r: (1,-1): r=0: 15,416, |r|=1: 13,037 each, 2: 7,791, 3: 3,461, 4: 1,085,
 5: 199, 6: 17;  (0,1): r=0: 14,360, |r|=1: 10,292, 2: 5,154, 3: 1,783, 4: 349, 5: 40, 6: 1;  (1,0): r=0: 2,208,
 |r|=1: 1,652, 2: 854, 3: 326, 4: 68, 5: 5.  (Mirror-symmetric in r.)
 So engineB's census saw 7,366 of 131,578 unit lines (5.6%) at (6,6), and none of the largest class (1,-1).

## 4. Unit-line types and geometric reasons; corrected WIDTH2-UNIT-LINE conjecture
4.0 HALF MODELS (geo.py, validate_geo.py; exact free-group computations with engineB's fgroup Artin action).
 TOP half T_V (axis + caps (0,1),(2,3), then V): complement group F_3, psi_V = psi_0 o V_*^-1 (engineB's orbit_search).
 BOTTOM half B_U (U, then the u2.u2 closure): in the complementary ball the closure is a planar forest = an H-tree
 {axis puncture - v_bot - v_top - E; v_bot - leg 0; v_top - c - leg 3} plus the cup (1,2); complement = genus-4 handlebody,
 pi_1 = F_4 = F_5/<<g2 g3>>, phi_U = phi_0 o U_* (loops pushed DOWN through U).  Conventions CHECKED on hand examples
 (closure: c12 dies; U = x2.x1 and y2.y1: c01 dies; x2.y1, x1.x2, x3.x2: nothing dies; x2.x3, y2.y3: c23 dies; x2.y3: no).
 DISC CRITERIA (PROVED, Dehn's lemma): if a junction curve c (c01 = g1g2, c23 = g3g4) is null-homotopic in a half's complement it
 bounds an embedded disc there, and the full twist along c extends as a disc twist that fixes the half: X1^2 (resp. X3^2) acts
 trivially on that half (the twist slides off a cap or cup).  If c0123 = g1g2g3g4 dies in the TOP complement, the axis is split
 off by a disc and the two arcs form a rational tangle R in a sub-ball; then X1 R = X3 R (flype: a twist on one pair of
 adjacent endpoints of a rational tangle equals the twist on the complementary pair), so X1 X3^-1 fixes the top.
 KERNEL TEST IS SUFFICIENT FOR THE TOP (PROVED here; closes engineB's GAP in REPORT 2(ii)): if the two cap curves of T_V1 die
 in pi_1(B - T_V2), Dehn's lemma + innermost-circle surgery give two disjoint discs in B - T_V2 cutting B into three balls,
 each containing one arc of T_V2 whose complement is a solid torus (cut handlebody), hence a trivial 1-string tangle;
 T_V1 has the same decomposition, so T_V1 = T_V2 rel boundary (Alexander trick on each ball).  For the BOTTOM the analogous
 kernel test is NOT sufficient (an unknotted H-tree is not determined by the cup curve), so only the disc criteria are used there.
 VALIDATION over ALL (5,5) halves (820 tops, 1,589 bottoms), geometric disc vs rho_2 scalar action (support in one colour class):
   top X1: 3 both / 817 neither;  top X3: 99 / 721;  top X1X3^-1: 64 axis-split = rep-scalar, 742 neither, 14 rep-scalar
   without axis split, and for ALL 14 the exact kernel test gives X1X3^-1 in Stab(T_V) (words x0.x2.x1.x0, y0.y2.y1.y0,
   x0.x2.x2.x1.x0, ... : the axis clasps the nested-cap band as a whole);  bottom X1: 7 / 1,582;  bottom X3: 17 / 1,572;
   bottom X1X3^-1: never (rep or geometric; PROVED impossible geometrically: the H-tree joins legs to the axis).
 So on every (5,5) half: rho_2 scalar action of a site (or of X1X3^-1) <=> geometric stabiliser of that half.  CHECKED(2,409).

4.1 MECHANISM CLASSIFICATION OF EVERY UNIT LINE (classify2.py = half stabilisers with re-cuts; disc_test.py + classify3.py =
 global disc; whitehead.py = exact one-relator word problem).  A RE-CUT slides a twist site through letters it commutes with
 (X1: x1,y1,x3,y3; X3: x0,y0,x1,y1,x3,y3; the joint X1^2X3^-2: x1,y1,x3,y3), offset twists included, and re-tests at every cut.
 EXACT RE-CHECK: every unit line and plane found by the modular census was re-verified with fastJ (exact J = 1 at the
 representative point): CHECKED(34,203) at (5,5), CHECKED(133,589) at (6,6); no false positive.
 TYPE S1  SITE-STAB, top (cap): the moving site's curve (c01 for (1,0), c23 for (0,1)) dies in pi_1(top complement) at some cut
          -> bounds a disc there (Dehn) -> the full twist slides off a cap.            (5,5): 10,678   (6,6): 41,542
 TYPE S2  SITE-STAB, bottom (cup): the curve dies in pi_1(bottom complement) at some cut -> twist slides off the cup.
                                                                                         (5,5):  4,154   (6,6): 16,074
 TYPE J1  JOINT-STAB axis-split, direction (1,-1) only: c0123 dies in the top -> axis split off, the two arcs form a rational
          tangle, X1 R = X3 R (flype), so X1^2 X3^-2 fixes the top.  Codex's template is this type (top x2.x1 = nested caps,
          leg-only).                                                                    (5,5): 14,986   (6,6): 57,872
 TYPE J2  JOINT-STAB band-clasp, (1,-1): axis NOT split, but the exact kernel test gives T_V = T_{V.x1.x1.y3.y3} (tops such as
          x0.x2.x1.x0, y0.y2.y1.y0: the axis clasps the nested-cap band as a whole, the band twist slides past the clasp).
                                                                                         (5,5):  2,236   (6,6):  8,724
 TYPE E   END-SEGMENT / GLOBAL DISC: no half stabiliser at any cut; the site twists the two END segments of the quotient arc
          (the strands that run to v_bot and, via c, to v_top).  Push the site curve to the closure level, c'' = U_*(c); it
          avoids the cup disc (free-factor test), so it lies on the sphere S' around the closure's H-tree; it is null-homotopic
          in pi_1(B' - T') = F_3/<<psi_V(U_*^-1(g2 g3))>> (relator PRIMITIVE, decided exactly by Whitehead's algorithm), hence
          bounds a disc in the complement of everything except the H-tree (Dehn), and the twist slides off "through the axis".
          ALL of engineB's offset-type lines with end-segment legs are type E:          (5,5):  1,284   (6,6):  6,602
 TYPE R   RESIDUAL cup-leg twist: the site twists the two legs of the cup, but between the site and the cup the legs are
          threaded/twisted with other strands; no half stabiliser at any cut, c'' not cup-avoiding.  Site curve IS
          null-homotopic in pi_1(S^3 - theta) (CHECKED on all of them; = pi_1(B'-T'), the H-tree adds nothing), which an
          isotopy would require, but an interior null-homotopic curve need not bound a disc.  Mechanism NOT identified.
          (only engineB offset-type (0,1) lines)                                         (5,5):     76   (6,6):    764
 PLANES (|NZ| = 1, unit): both sites explained (S1/S2/E) -> the whole (m,n) plane is one knot: (5,5) 613 of 789,
          (6,6) 1,439 of 2,011; the rest have one or two type-R sites: (5,5) 176 (one R site), (6,6) 572 (104 with both).
 By direction: (1,0) and (0,1) lines are S1, S2, E or R; (1,-1) lines are J1 or J2 (all of them); no unit line, single-group or
 offset-specific, in the other 13 directions (CHECKED, both enumerations).
 Totals (6,6): 131,578 unit lines = 130,814 with a PROVED isotopy mechanism (99.42%) + 764 type R; planes 1,439 + 572.
4.2 WHAT IS AND IS NOT ONE-SITE-SCALAR.  rho_2 level: a 'single' line is top-scalar or bottom-scalar (support of V v or of
 phi U in one slope class) in every case at (5,5)/(6,6) [rep labels in out/classify2_*.log]; the offset-type lines (engineB's
 1,360 / 7,366) are NEVER one-site scalar on either boundary: they are types E and R.  So engineB's sentence (iv) is wrong twice:
 the lines it counted are not one-site-scalar, and the one-site-scalar lines (and the joint ones) were not counted.
 NOTE on planes: a unit plane (|NZ| = 1) is a unit line in EVERY direction; the direction statements below exclude them.
4.3 CORRECTED CONJECTURE (WIDTH2-UNIT-LINE, replaces "unit line => one site scalar on a boundary vector or covector"):
 CONJECTURE (WIDTH2-UNIT-LINE-GEO).  For a two-site template s.l1.l1.V.X1^(2m)X3^(2n).U.u2.u2, a line {(m0,n0)+k(p,q)} is a
 unit line only if the moving element g = X1^(2p) X3^(2q) is a geometric stabiliser of the theta-curve at (m0,n0); then all
 knots of the line are isotopic.  The stabilisers that occur are: (a) one site bounding a disc in one half (cap or cup), after
 sliding the site through letters it commutes with; (b) direction (1,-1): X1 X3^-1 fixing the top half (axis split off ->
 flype of a rational tangle; or a band clasped by the axis) -- on the axis-straight summand Hom(V0, V2^{x4}) only a = b occurs,
 which is the rho_2 shadow of (b); (c) a GLOBAL disc: the site curve, pushed to the sphere around the closure's H-tree, bounds
 a disc in the complement of the rest (end-segment twists).  In particular unit lines occur only in directions (1,0), (0,1),
 (1,-1).  STATUS: (a), (b), (c) are PROVED sufficient (Dehn's lemma + exact free-group computations); the conjecture is
 CHECKED(130,814 of 131,578 unit lines and 1,439 of 2,011 unit planes at (6,6)); the remaining 764 lines (type R) are
 consistent with it (null-homotopic site curve) but not decided: GAP.

## 5. Isotopies / certification status per type
ISOTOPIES (each makes every knot of the line isotopic to the knot at any one point of the line, in particular to the BASE point
= the point with the fewest crossings after free reduction, k in [-40,40]):
 S1/S2 PROVED: Dehn's lemma gives an embedded disc in the half's complement bounded by the site curve; the full twist along it
        is a homeomorphism of that half fixing the half's arcs (rotate the cap/cup ball).  Re-cuts are braid identities.
 J1    PROVED: the disc bounded by c0123 splits off the axis; the remaining 2-string tangle is rational (a sub-tangle of a
        trivial tangle cut by a disc); a rational tangle is invariant under the flype that moves a half twist from the pair
        (0,1) to the pair (2,3), so X1 X3^-1 fixes the top.
 J2    PROVED: exact kernel test + the disc-system argument of 4.0 (T_V and T_{V.x1.x1.y3.y3} are the same tangle rel boundary).
 E     PROVED: c'' bounds a disc in B' - T' (Dehn's lemma on the boundary sphere S'), the twist along it fixes T', and the
        H-tree side is untouched.
 R     UNRESOLVED: no isotopy found.  Cleanest member (from s.l1.l1.x0.y2.(x3.x3)^n.x2.y3.y0.x1.x1.u2.u2 by braid relations:
        x0 commutes to y0 and cancels, y2.X3^(2n).x2 = x3.X2^(2n).y3 and the leading x3 slides off cap B):
            R_n = s.l1.l1.(x2.x2)^n.y3.y3.x1.x1.u2.u2  = caps . X2^(2n) . X1^2 X3^-2 . closure,
        lp.J(R_n) = 1 for n = -3..5 (CHECKED), V_K(R_n) = 1 exactly for n = -3..4 (<= 24 crossings: CERTIFIED_UNKNOT each).
        Here the moving site is X2 on the CUP legs (1,2), and the closure has been pre-twisted by X1^2 X3^-2 (cup legs twisted
        with the two end segments in opposite senses); X1^2 X3^-2 does NOT fix the closure (no bottom (1,-1) stabiliser, 4.0),
        so the X2 twist cannot be slid onto the cup.  rho_2 shadow: w' = phi X1^2 X3^-2 pairs only with the X2-colour-0 part of
        caps.  A Seifert-disc mechanism (the site disc meets an equivariant spanning disc of the unknot in one arc, so every
        member stays an unknot without the twist being a stabiliser) would explain it; NOT verified.  Every knot of a type-R line has J = 1; its points with <= 24 crossings are individually
        certifiable by V_K = 1 (Tuzun-Sikora), the infinitely many others are presumed unknots and are RETAINED as
        unresolved (representatives: out/classify3_6_6.log, e.g. s.l1.l1.y0.y2.x3.x3.x3.x3.(x3.x3)^n.x2.y3.x0.x1.x1.u2.u2).
 PLANES with an R site: the R direction is UNRESOLVED in the same way.
BASE-KNOT CERTIFICATION (exact V_K by tools/kauffman.bracket, ident3 normalisation, at the base point):
 (5,5): every unit line/plane whose base has <= 24 crossings has V_K = 1 exactly (34,130 of 34,203); 73 bases exceed 24.
 (6,6): 130,275 of 133,589 with base <= 24 crossings, all V_K = 1 exactly; 3,314 bases exceed 24 crossings
        (S1/S2 (0,1): 524, (1,0): 842; J (1,-1): 1,552; E (0,1): 364, (1,0): 32) -- these bases lie at transverse offsets
        |r| >= 2, where the offset twist itself adds crossings.
 Per type (out/certify_summary.txt; "lines" = unit lines, planes counted once):
   (6,6)            lines    base<=24 & V_K=1   base>24
   S1 cap (0,1)    38,348        38,186            162
   S1 cap (1,0)     3,194         2,386            808
   S2 cup (0,1)    11,250        10,888            362
   S2 cup (1,0)     4,824         4,790             34
   J1 axis-split   57,872        56,489          1,383
   J2 band-clasp    8,724         8,555            169
   E end-seg (0,1)  4,886         4,618            268
   E end-seg (1,0)  1,716         1,684             32
   R residual (0,1)   764           668             96
   planes geo       1,439         1,439              0
   planes with R      572           572              0
   (5,5): 34,203 lines/planes, 34,130 with base <= 24 & V_K = 1, 73 bases > 24 (68 distinct words).
 => CERTIFIED_UNKNOT, every knot on the line (isotopy PROVED + base certified by (a)):
        (6,6): 129,035 unit lines and 1,439 unit planes;  (5,5): 33,878 lines/planes.
 => ONE knot per line, UNRESOLVED until certified (isotopy PROVED, base > 24 crossings): (6,6) 3,218 lines (2,604 distinct
    base words over all types incl. R), (5,5) 73.  (b)-CERTIFICATES (tietze.py): Wirtinger presentation of pi_1(S^3 - K) from
    the same full symmetric diagram kauffman/alex use, reduced by valid Tietze moves (ELIM a generator occurring once in a
    relator; AUT = Whitehead/Nielsen change of generators; KILL a relator conjugate to one generator) to <a | >, every
    certificate REPLAYED from scratch.  Adversarial check: 339 random width-two knots with V_K != 1 -> 0 certified;
    301 random V_K = 1 knots -> 301 certified and replayed.  Pass 1 (<= 3 generators for AUT): 1,997 of the 2,604
    distinct > 24-crossing base words CERTIFIED_UNKNOT (out/certify_big.json); pass 2 (more effort) running on the 607 left.
 => UNRESOLVED lines (no isotopy): type R, (6,6) 764 lines (668 bases <= 24 certified pointwise) and the R direction of 572
    planes; (5,5) 76 lines + 176 planes.  These are retained; none is CERTIFIED_NONTRIVIAL (no knot here has V_K != 1).
