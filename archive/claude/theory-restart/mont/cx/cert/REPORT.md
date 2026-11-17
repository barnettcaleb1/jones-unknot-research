# CERT LANE REPORT: a sound certifier for the covering knot K of a halfword
Lane: ~/jones-lanes/theory-restart/mont/cx/cert/  (Claude, started 17 Nov 2026 02:25 CST)
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.
Certification standard (from the task, used exactly):
 CERTIFIED_UNKNOT only by (a) an actual diagram of K with <= 24 crossings and V_K = 1 (Tuzun-Sikora), (b) pi_1 presentation
 reduced by valid Tietze moves to <a | > with a replayable certificate (Dehn's lemma), (c) diagram reduced to 0 crossings by
 validated Reidemeister moves.  CERTIFIED_NONTRIVIAL only by an explicit homomorphism pi_1 -> G with nonabelian image checked
 on every relator.  Everything else UNRESOLVED.

## STATUS (newest first)
- 03:54 HEADLINE.  certify.py is READY (sound by construction: every certificate is accepted by the independent checker
  replay.py; zero false certifications in every nontrivial suite).  Beyond the task suites, the certifier was run on
  engineB's complete (7,7) screen: all 685,033 V_K = 1 survivors (engineB's 'presumed unknots') are now CERTIFIED unknots
  (568,895 jones24 + 116,138 Tietze), and all 113,348 depth-8 re-hit closures are CERTIFIED unknots.  14 survivors were
  UNRESOLVED on the first pass (Tietze blow-up) and were resolved by an adaptive relator-length cap.  Final-code reruns
  (03:53, out/v3/): (a) 2721/2721 CERTIFIED_UNKNOT, (b) 1944/1944 CERTIFIED_NONTRIVIAL with 0 false certifications in
  blind mode, stress 35,381 attempts 0 false, (c) unchanged or faster.  NO counterexample; no HIT file.
- 03:18 FINAL-CODE suites complete: (a) 2721/2721 unknots CERTIFIED_UNKNOT (Tietze, 100%); (b) 1944/1944 nontrivial
  CERTIFIED_NONTRIVIAL in blind mode, ZERO false certifications (+ 26,201 stress attempts, 6,528 transplant rejections);
  (c) 26-32 crossings: 4 ms (unknots) / 28 ms (nontrivial) median; ~64 crossings: 19 ms / 0.97 s median.
  READY.  Running now: mitm_cert.py 7 7 (re-certification of every survivor of engineB's (7,7) screen), then bulk_cert.py
  on all 113,348 depth-8 re-hit knots (section 9).
- 03:03 suites (a), (b) complete on first-version code: 2721/2721 unknots CERTIFIED_UNKNOT (Tietze), 1944/1944 nontrivial
  CERTIFIED_NONTRIVIAL, ZERO false certifications.  Engineering after that: substring search via str.find + memoised
  canonical words (Tietze ~3.5x faster), Delta computed lazily, reps-first when V_K != 1 (blind mode keeps the Tietze
  attempt for the soundness suite).  Final-code reruns of (a), (b), (c) queued (out/final_suite*), then the complete
  re-certification of engineB's (7,7) screen survivors (mitm_cert.py) and of all depth-8 re-hit families (bulk_cert.py).
- 02:48 steps 3-4 done; certify.py packaged; suite (a) first runs: 1300 + 700 + 700 + 21 unknots ALL CERTIFIED_UNKNOT
  via Tietze (incl. engineB's bottom re-hit 'presumed unknots' up to 32 crossings and Codex's family up to 86 crossings).
- 02:36 steps 1-2 done and validated (650 halfwords).
- 02:25 skeleton written; reading conventions (alex.symmetrize, kauffman.bracket, ident3.VK, alex.diagram).

## 1. Diagram (halfword -> oriented PD code)        [DONE 02:36; diagram.py]
 K := the knot of the Morse word alex.symmetrize(alex.parse(halfword)) (the project's definition; kauffman.py sweeps the
 same word).  PD code: edges 0..2n-1 along the orientation, crossing k = k-th crossing of the Morse word, tuple (a,b,c,d)
 counterclockwise from the incoming under edge, sign stored explicitly.  Planar picture: word drawn UPWARDS, positions left
 to right (this is the picture in which kauffman.py's smoothing weights are the standard ones; the downward picture is the
 mirror; alex.writhe is the writhe of the downward picture, hence kcert's sign remark).
 Bracket from the PD code by a frontier (planar matching) sweep; V_K = (-A^3)^-w <D>, t = A^-4 (V(right trefoil) =
 t + t^3 - t^4, V(4_1) = t^-2 - t^-1 + 1 - t + t^2: CHECKED).
 VALIDATION CHECKED(650) (validate_pd.py, seed 11; flat_search.gen words + width-two words with all prefixes/suffixes,
 |W| <= 16; crossings 1..31, mean 14.8; out/validate_pd_650.json):
   * check_pd: labels, orientation, planar Euler characteristic (faces = n + 2) 650/650;
   * V_K(PD) == ident3-normalised V_K(kauffman.bracket) EXACTLY (not up to mirror) 650/650 (242 have V_K = 1);
   * Alexander(PD, Fox calculus on the Wirtinger presentation) == alex.py's Alexander polynomial 650/650.  alex.py's
     polynomial is computed from alex.alex_matrix + alex.bareiss at integer points with exact interpolation (sympy's
     symbolic det is too slow past ~15 crossings); this interpolation itself == alex.alex_poly (sympy) on all 272 knots
     with n <= 12.
   Re-run after aligning the PD traversal orientation with alex.diagram (validate_pd_650_v2.json): again 650/650 on
   every check.
## 2. pi_1 presentations (Wirtinger, plat)           [DONE 02:36; wirtinger.py]
 WIRTINGER: generator k+1 = the arc that begins (as outgoing under edge) at crossing k; relator of crossing k:
   x_{k+1}^-1 x_o^s x_i x_o^-s (s = sign).  The opposite global rule is the Wirtinger presentation of the reflected diagram
   (mirror image), which has an isomorphic group; the rule is uniform in s (PROVED, elementary; README).
 PLAT: Morse sweep with the exact Artin action on free groups (cap -> new generator g, strands g, g^-1; 'x':
   (w_i, w_i+1) -> (w_i w_i+1 w_i^-1, w_i); 'y': (w_i, w_i+1) -> (w_i+1, w_i+1^-1 w_i w_i+1); cup -> relator w_i w_i+1).
 VALIDATION CHECKED(650): Fox calculus on BOTH presentations (plat: abelianisation solved from the exponent-sum matrix,
   last cup relator dropped as a consequence) gives alex.py's Alexander polynomial exactly, 650/650.
 GROUP-LEVEL CROSS-CHECK CHECKED(320) (validate_group.py, seed 21, up to 26 crossings): |Hom(pi, G)| computed from the
   CHECKER's Wirtinger presentation (replay.py, built from alex.diagram) and from the plat presentation (Artin action;
   no arcs, no signs) agree for G = S3, S4, A5 on 320/320 knots (960/960 counts); 104 (S3), 128 (S4), 173 (A5) of them
   have nonabelian homomorphisms (count > |G|), values up to 84 / 2016 / 3060.  (Both reduced by group-preserving
   eliminations; Hom = union over conjugacy classes of meridian images.)  So the two independent constructions present
   isomorphic groups at the level these invariants see; the Alexander check alone could not detect a mirror-type error.
## 3. Tietze simplifier + certificates + replay      [DONE 02:45; tietze.py, replay.py]
 tietze.py: canonical form after every move (free+cyclic reduction, least rotation of r and r^-1, drop empty/duplicate,
 sort by (len, word)); moves ('elim', g, j) [g occurs once in relator j], ('mult', i, j, e, kj, ki) [r_i := rot(r_j^e) rot(r_i),
 i != j: substring-replacement relator multiplication], ('nielsen', x, a, d, side) [x -> x a^d or a^d x; Whitehead length
 reductions are recorded as their elementary Nielsen factors]; driver: greedy minimal-growth elimination, then shortening
 relator multiplication, then Whitehead length reduction, then randomised neutral moves and restarts; each attempt
 is abandoned when the total relator length exceeds an adaptive cap (max(4000, 10 x initial length) x 1.6^attempt),
 added after 14 (7,7) survivors made the first greedy attempt crawl at 36k-72k letters (section 9).
 replay.py (INDEPENDENT: imports nothing from the certifier): rebuilds the Wirtinger presentation from alex.diagram (its own
 arc labelling and its own crossing signs), its own canonical form (Duval least rotation, not Booth), re-checks every
 move's precondition and accepts only on <g | >.  CHECKED: checker Wirtinger == certifier Wirtinger LITERALLY on 300/300
 random halfwords (after aligning the traversal orientation with alex.diagram); canonical cyclic words agree 3000/3000.
 Every certificate returned by certify.py has been accepted by replay.check (a rejected one is dropped and noted).
 CHECKER ADVERSARIAL TESTS: malformed certificates (missing images, out-of-range indices, mult with i = j, empty move
 list, jones24 on a V != 1 knot) are rejected, and any exception inside the checker counts as rejection;  TRANSPLANT
 test: 6,528 valid Tietze certificates of unknots (suite A1) re-labelled with the halfwords of nontrivial knots of the SAME
 crossing number (suite B2/B3): 0 accepted (CHECKED(6528)); typical rejection: the eliminated generator does not occur
 exactly once.
## 4. Nonabelian representations                     [DONE 02:47; reps.py]
 All targets are permutation groups (so certificates are permutation images and the checker multiplies permutations):
 Aff(F_p) on F_p (roots lam != 1 of Delta mod p, p <= 400, by linear algebra over F_p), S4, A5, S5, PSL(2,7), A6, S6,
 PSL(2,11), SL(2,5) and SL(2,7) (faithful on F_p^2 - 0), A7, S7, PSL(2,13).  Search on a meridian-preserving reduction
 (eliminations + relator multiplications only, so survivors are meridians): first image fixed, second up to the centraliser,
 all reduced relators checked; eliminated arcs recovered from their elimination words; the full certificate (images of
 ALL Wirtinger generators) is checked on every Wirtinger relator by replay.check, and two non-commuting images are named.
 First test: 12/12 Alexander-trivial E3d knots (31-36 crossings, Delta = 1 exactly) get A5 (11) or A6 (1) representations.
## 5. Reidemeister reduction                         [NOT IMPLEMENTED, by design]
 Optional item (5) was to be added only if it raised the success rate.  It would not: with the adaptive length cap the
 Tietze route certifies 100% of every unknot set tried (sections 6, 9: 2721 suite knots, 685,033 screen survivors, 113,348
 re-hit closures), from 6 to 86 crossings.  Route (a) (<= 24 crossings, V = 1) is checked directly
 on the Morse diagram (replay.check 'jones24': 1300/1300 on suite A1, project bracket).  Route (c) is used only for
 crossing-free diagrams.  If an unknot ever resists Tietze, the recommended addition is R1/R2 + an R3 walk on the PD code
 (diagram.faces already provides the face structure) with a move-level replay in replay.py.
## 6. Validation suites  [DONE 03:50 on the FINAL code (adaptive length cap); out/v3/*.summary.json + full .jsonl]
 (Earlier runs on two earlier code versions, out/suite*, out/final_suite*, gave the same counts.)
 (a) KNOWN UNKNOTS (default budgets).  CHECKED(2721), all by the TIETZE route, every certificate accepted by replay.py:
   A1 J = 1 configurations, |W| <= 12 (1300 distinct random words s.P.W.S, all 6 prefix/suffix pairs, 7..24 crossings;
      V_K = 1 and <= 24 crossings, so route (a) applies too: replay 'jones24' 1300/1300): 1300/1300, median 1 ms, max 4 ms.
   A2 explicit families (engineB section 2, regenerated by gen_families.py, rho_2 mod p, depth 8):
      top re-hits W = g2.g1^-1 (700 longest of 36,764; 20..32 crossings): 700/700, median 4 ms, max 0.32 s;
      bottom re-hits W = U1^-1.U2 (engineB's 'presumed unknots'; 700 longest of 76,584; 22..32 crossings): 700/700,
      median 4 ms, max 6 ms;  Codex's family m = -10..10 (6..86 crossings): 21/21, max 30 ms.
   SUCCESS RATE (a): 2721/2721 = 100% CERTIFIED_UNKNOT; 0 UNRESOLVED.  (Complete families and the (7,7) screen: sec. 9.)
 (b) KNOWN NONTRIVIAL KNOTS, BLIND mode (Tietze route forced, 1 s budget with restarts, then reps).  CHECKED(1944):
   B1 Alexander-trivial (Delta = 1 exactly, V_K != 1): 24 E3d words + 2 padded variants each + all mirrors: 144 knots,
      31..78 crossings: 144/144 CERTIFIED_NONTRIVIAL (A5 132, A6 12), median 1.1 s.
   B2 random V_K != 1 (450 flat_search.gen + 450 width-two words, 3..38 crossings): 900/900 (affine Aff(F_p), p = 3..37).
   B3 mirrors of B2 (x <-> y in every letter; V(t) -> V(1/t) CHECKED on 50): 900/900.
   FALSE CERTIFICATIONS: ZERO (0 Tietze successes in 1944 blind attempts; stress test below; 6,528 transplanted
   certificates rejected, section 3).  Rep finder success 1944/1944 = 100%.
   STRESS (stress_tietze.py; first run, previous code): 100 two-bridge knots (width-one words, V != 1) + the 48 E3d
      Alexander-trivial knots and mirrors, Tietze budget 20 s each (two seeds, unlimited randomised restarts, neutral
      moves, Whitehead/Nielsen active): 26,201 attempts, 228/296 runs end at 2-generator presentations, ZERO reach <a | >.
      Final-code rerun (out/v3/stress_tietze.json): 35,381 attempts, ZERO reach <a | >.  CHECKED(148).
 (c) TIMING (wall clock per knot, certify() defaults, shared machine):
   26..32 crossings: unknots (J = 1, |W| = 13..16; 334): median 4 ms, max 0.14 s;  nontrivial (200): median 24 ms,
     max 39 ms.
   about 64 crossings: unknots (60..62 crossings: products of two top re-hit words + Codex m = +-7; 102): median 18 ms,
     max 0.19 s;  nontrivial (exactly 64 crossings, 100): median 0.58 s, max 0.62 s (the exact Alexander polynomial needed
     by the affine search dominates).  Codex family at 86 crossings: 30 ms.  Alexander-trivial knots (A5/A6): ~1.1 s.
   Bulk: the 722,637 (7,7) survivors were classified + certified in 884 s wall on 5 processes (section 9).
## 7. Codex's challenge (msgs/20261117-020642-codex.md): regression family and 'presumed unknots'
 * FIXED REGRESSION (V = x2.x1, U = x1, direction (1,-1), offset 0): s.l1.l1.x2.x1.x1^(2m).y3^(2m).x1.u2.u2 (m < 0:
   y1^(2|m|).x3^(2|m|)).  lp.J = 1 for every m tested (-10..10, exact).  certify.py: CERTIFIED_UNKNOT for all 21 values of m
   by replayed Tietze certificates (6..86 crossings; m = 0 is the 6-crossing base diagram).  So the family is a CERTIFIED
   (not presumed) unknot family for |m| <= 10, consistent with Codex's geometric argument (cap/annulus slide).  CHECKED(21).
 * engineB's 'presumed unknots' (V_K = Delta = 1, > 24 crossings) are exactly the cases this certifier is for.  Status here:
   - bottom re-hit closures s.l1.l1.U1^-1.U2.u2.u2 (engineB 2(iii), depth 8): ALL 76,584 CERTIFIED; top re-hit closures:
     ALL 36,764 CERTIFIED (section 9).
   - J = 1 configurations with 26..32 crossings sampled at random (suite C1u): 334/334 CERTIFIED.
   - The complete (7,7) screen was regenerated (identical counts) and ALL 685,033 V_K = 1 survivors are CERTIFIED unknots
     (section 9).  What remains for the REGION claim is the geometric deduplication of bottom classes (GAP, section 9);
     so engineB's statement should now read 'no certified nontrivial J = 1 knot; every screen output certified; region
     emptiness conditional on geometric bottom deduplication' (Codex's distinction).
## 8. Soundness argument (summary; full text in README.md)
 tietze  -> CERTIFIED_UNKNOT: (i) the checker's starting presentation is the Wirtinger presentation of the Morse diagram
   of K (alex.diagram), with one uniform sign rule; the opposite rule is the reflected diagram's presentation, so the group
   is pi_1(S^3 - K) up to isomorphism in either case (PROVED, elementary); arcs and signs validated by Fox/Alexander
   (CHECKED 650), literal agreement with the PD construction (CHECKED 300) and |Hom(pi, G)| agreement with the Artin-action
   plat presentation (CHECKED 320 x 3 groups); (ii) every move is a composition of Tietze transformations and the
   checker verifies its precondition (PROVED, elementary); (iii) <a | > = Z => unknot (Dehn's lemma).  Independence: the
   checker shares no code with the simplifier; transplanted certificates are rejected (CHECKED 6528).
 jones24 -> CERTIFIED_UNKNOT: the Morse diagram has <= 24 crossings and its bracket (kauffman.py) is a unit; Tuzun-Sikora.
 rep     -> CERTIFIED_NONTRIVIAL: permutation images of all Wirtinger generators satisfy every relator (von Dyck) and two
   do not commute, so pi_1 is nonabelian, not Z.
 COUNTEREXAMPLE = rep + V_K = 1, V_K confirmed by BOTH brackets (PD and kauffman.py) before the HIT file is written.
   Path test (monkeypatched, write_hits=False, no file created): PD bracket faked to 1 on an E3d knot -> UNRESOLVED with
   a BUG note (project bracket disagrees); both brackets faked -> COUNTEREXAMPLE.  CHECKED.
 GAPs: none in the logic.  Trusted inputs: tools/alex.py (definition of K, alex.diagram traversal), tools/kauffman.py
 (bracket), the Tuzun-Sikora computation, Python itself.

## 9. Re-certification of engineB's width-two screen and re-hit families  [DONE 03:40]
 mitm_cert.py 7 7 (engineB mitm.py imported read-only, same BFS and zeta_7 filter) regenerated EXACTLY engineB's numbers:
 11,902 top classes, 26,089 bottom classes, 207,002,083 knot pairs, 722,637 zeta_7 survivors; of these 37,604 have
 V_K != 1 (= engineB's near-miss count) and 685,033 have V_K = 1 (= engineB's 'presumed unknots').  CHECKED(685,033):
   568,895 with <= 24 crossings: 'jones24' certificates (replay.py, project bracket);
   116,101 with 25..28 crossings: Tietze certificates (lean path, 5 s, replay.py);  23 more by the long path (60 s);
   14 were UNRESOLVED on the first pass (26..28 crossings, Delta = 1, no rep in 60 s): the first, deterministic Tietze
     attempt blew relators up to 36k-72k letters and crawled.  All 14 are J = 1 (lp.J) and V_K = 1 (project bracket);
     after adding an adaptive relator-length cap (start max(4000, 10 x initial length), x1.6 per restart) ALL 14 are
     CERTIFIED_UNKNOT in <= 0.65 s (out/mitm77_recert_37.json; the 14 words: out/mitm77_UNRESOLVED_14.json).
   => EVERY one of the 685,033 V_K = 1 representative junctions of the (7,7) screen is a CERTIFIED unknot (0 UNRESOLVED,
      0 CERTIFIED_NONTRIVIAL).  Certificates: out/mitm77_cert.tietze.jsonl.gz (all > 24-crossing ones), out/mitm77_recert_37.json.
 Independent re-replay from disk (replay.py, fresh process): 3,000 random certificates of the 116,124 stored (7,7) Tietze
 certificates, and all 5,401 certificates of the out/v3 suites: all accepted.  CHECKED.
 bulk_cert.py on the COMPLETE depth-8 re-hit families (gen_families, same rho_2 BFS; counts equal engineB's):
   bottom re-hits s.l1.l1.U1^-1.U2.u2.u2: 76,584/76,584 CERTIFIED_UNKNOT (1..32 crossings; median 3 ms);
   top re-hits s.l1.l1.g2.g1^-1.u2.u2: 36,763/36,764 on the run (pre-cap code); the remaining one
     (s.l1.l1.y2.y2.x1.y2.y2.x1.y2.y3.y2.y2.x1.x1.y2.x1.y2.u2.u2, 30 crossings, J = V = 1) CERTIFIED with the final code
     (0.09 s; out/bulk_top_d8_recert_1.json).  So 113,348/113,348.
 WHAT THIS DOES AND DOES NOT SETTLE (Codex's distinction).
   * The screen's OUTPUT is now certified: no J = 1 representative junction of length <= 14 is a presumed unknot any more.
   * The REGION claim 'no counterexample among all width-two theta-curves with |W| <= 14' additionally needs both
     deduplications to be geometric: a word G1.G2 has the same J as its representative pair (t, b), but its KNOT equals
     K(t, b) only if G1 ~ t and G2 ~ b are equal tangles.  Tops: engineB 2(ii) exact Artin-action test (its Hilden-type
     write-up is engineB's own GAP).  Bottoms: GAP.  A bottom re-hit whose closure U1^-1.U2 is an unknot (now certified for
     all 76,584) does NOT by itself prove B(U1) = B(U2) (cf. rational tangles: many bottoms close a given top to the
     unknot).  Recommended: the exact kernel test of engineB 2(ii) applied to bottom tangles (fgroup.py, cups instead of
     caps).  Until then the region statement reads: 'no certified nontrivial J = 1 knot; every screen output certified;
     region emptiness conditional on geometric bottom deduplication'.
 CROSS-REFERENCE (not my work, not re-verified here): a parallel lane wrote its own folder cert/extract/ (another agent,
   started 02:22; its REPORT.md is self-contained and was left untouched).  It regenerated the same sets from engineB's
   scripts with identical counts (S2 + |W| <= 12 = 369,158 + 315,875 = 685,033 J = 1 configurations, equal to my V_K = 1
   count) and certified them by word-level isotopies, Reidemeister reduction and Tietze, reporting 0 unresolved; it also
   reports exact bottom-TANGLE equality for 74,351 of the 76,584 bottom coincidences (2,233 open), which would reduce the
   bottom-deduplication GAP above to those classes.  The two certifications are independent (different code paths) and
   agree on every count I can compare.
