# roundF / U1 REPORT: certification of engineC2's J = 1 theta-curves (S2 words, E4 pairs, periodic families)
Lane folder: ~/jones-lanes/theory-restart/mont/cx/roundF/u1/ (Claude, 17 Nov 2026, started 07:19 CST).  Marks: PROVED /
CHECKED(n) / CONJECTURE / GAP.  Nothing outside u1/ was edited.  Certifier: a COPY of the audited fixed cert/run/code in
u1/code (only sys.path strings re-pointed: `diff -r` shows exactly 9 sys.path.insert lines changed).
CERTIFICATION STANDARD (used exactly): CERTIFIED_UNKNOT only by (a) a diagram of K with <= 24 crossings and V_K = 1
(Tuzun-Sikora), (b) a replayable Tietze reduction of pi_1(S^3 - K) to <a | > (Dehn), (c) validated R-moves to 0 crossings;
for an infinite family a PROVED isotopy / identification plus certified members.  CERTIFIED_NONTRIVIAL only by an explicit
nonabelian representation checked on every relator.  Everything else UNRESOLVED (retained).

## STATUS (newest first)
- 07:58 FINAL.  NO HIT (no CERTIFIED_NONTRIVIAL knot with J = 1 or V = 1 anywhere; no HIT file; no bracket ALARMS).
  U1 is CLOSED: every J = 1 configuration of engineC2 is CERTIFIED_UNKNOT by the audited certifier on an actual diagram of
  the lifted knot K, and every certificate passed BOTH independent checkers in a fresh process (fraction 1.0):
  (i) S2 |W| <= 7: 11,481/11,481 (+ 5,330 stored mirror copies), region CERTIFIED (coverage, section 3);
  (ii) E4: 65/65 unit pairs; (iii) periodic families (BB)^n, (Ab)^n, (aB)^n, (AAbd)^n: CERTIFIED for every n >= 0 by
  Lemma K periods 1, 3, 3, 2 plus 44/44 certified members n = 0..12.
  The identification 'K(h) = lift of engineC2's arc' is the PROVED translation of section 2 (vertex slide + ring transfer
  by a 2 pi ball rotation), CHECKED by exact J equality on all 58,887 S2 words and 24 E4 configurations, and by the
  V_K/J relations (N1, N2) on 4,907 nontrivial knots.  Nontrivial controls: 1,883 + 3,000 + 24 = 4,907/4,907
  CERTIFIED_NONTRIVIAL, none certified unknot.  UNRESOLVED: 0.
- 07:29 running.  Translation S2/E4 theta-curve -> halfword built and PROVED (section 2); all 11,481 S2 J = 1 words
  CERTIFIED_UNKNOT (Tietze, 113 s); exhaustive J-validation of the translation on all 58,887 S2 words running; nontrivial
  controls (1,883) running; E4 rebuild running.

## 1. Route chosen
Route 1 (build K and run the certifier), with the certifier's own input format: a halfword h whose knot
K(h) = alex.symmetrize(h) is the lift of the arc.  engineC2's theta-curves are NOT halfwords: they have rings of k around
BOTH axis lines (c on A_l, d on A_r) and v_bot on A_r.  Section 2 gives two isotopies of theta-curves that turn every
S2 / E4 event list into exactly theta.from_halfword(h) of a halfword h; then K(h) is the lift (project convention:
from_halfword(h) is the quotient of alex.symmetrize(h), calibrated by engineC2 on 150/150 words, lp.J == theta.J_events).

## 2. The translation theta-curve -> halfword (translate.py)   [PROVED; CHECKED below]
Circle model (engineC2/theta.py, sym.py, plat2.py): A = A_l (position 0) u top cap u A_r (last position) u bottom cup;
v_top = splitR(0) on A_l at the top; S2 top half = capA(0), splitR(0), proj(1), capK(2), W (a = Y(1), A = X(1), b = X(2),
B = Y(2), c = YY at (0,1), C = XX at (0,1), d = XX at (3,4), D = YY at (3,4)); Theta(W) = top . f(top), so the bottom is
f(W) (reverse, a<->b, c<->d), then cup(1), mergeL(1) (v_bot on A_r), cup(0).  d/D are full twists ("rings") of the k strand
next to A_r around A_r.  A halfword h has from_halfword(h) = capA(0), splitR(0), proj(1), <letters>, mergeR(0), cup(0) with
x_s/y_s = (X|Y, s), x0/y0 = two (X|Y, 0), l_s = capK(s), u_s = cup(s): rings only on A_l, A_r untouched, v_bot on A_l.
 (V) BOTTOM VERTEX.  Below cup(1) the level is (A_l, k, A_r) and nothing else exists.  Sliding v_bot along the bottom cup
     of A from A_r to A_l is a planar isotopy of the projection (the vertex moves along the boundary of the face bounded by
     A_l, k, A_r and the cup; no strand crosses that face): mergeL(1), cup(0)  ->  mergeR(0), cup(0).  PROVED.
 (R) RING TRANSFER.  Let z0 be the level just above a ring Delta^2_eps(k_m, A_r) (k strands k_1..k_m at positions 1..m,
     A_r at m+1).  B := {z <= z0} u {oo} is a 3-ball; B n A = alpha = (A_l below z0) u (bottom cup) u (A_r below z0) is
     one unknotted arc (a U) with ends a1 = A_l(z0), a2 = A_r(z0); B n k is whatever lies below z0 (incl. v_bot on alpha).
     Fix a homeomorphism phi: (B, alpha) -> (D^3, diameter) and let H_s be the rotation by 2 pi s about the diameter on the
     inner ball, damped to 0 across a collar of dB.  H_s fixes alpha pointwise, is the identity outside B, and H_1 is the
     identity except in the collar, where each point of dB n k is dragged once around its latitude (the level sets on dB of
     the axial coordinate).  So H_1(Theta) ~ Theta and H_1(Theta) = Theta with the collar braid inserted at level z0.
     The latitude foliation of dB - {a1, a2} can be prescribed (any foliation of the twice-punctured sphere by circles is
     the phi-preimage of the round one; a sphere homeomorphism fixing a1, a2 extends conewise to (B, alpha)).  Choose it,
     in the level plane z = z0 (dB = plane u oo), as nested circles around a1 containing k_1..k_{m-1}, the vertical line
     between k_{m-1} and k_m (through oo) and nested circles around a2 containing k_m only.  A rigid rotation of a sphere
     turns counterclockwise around one pole and clockwise around the other when both are viewed from outside the ball
     (here: from above), so the collar braid is Delta^2_eps(a1, k_1..k_{m-1}) . Delta^2_{-eps}(k_m, a2) (disjoint supports,
     commuting; no motion through oo).  Insert it with eps = the handedness of the ring: Delta^2_{-eps}(k_m, a2) cancels
     the ring (Reidemeister II), leaving Delta^2_eps(A_l, k_1..k_{m-1}).  Hence
        ring of k_m around A_r  ~  full twist of positions 0..m-1 of the SAME handedness,
        Delta^2(0..m-1) = prod_{j=1..m-1} s_{j-1}..s_1 s_0^2 s_1..s_{j-1}  (s_i = X(i) for d-type XX rings, Y(i) for YY),
     which is a halfword word because s_0 occurs only squared (= x0/y0).  For S2 (m = 3): d -> x0.x1.x0.x1,
     D -> y0.y1.y0.y1 (the cover-side reading: Delta_4 = x0 x1 x0 x1, a half twist of the four inner strands).  PROVED.
     (Special cases, consistent: m-1 = 0 gives 'a ring of the only strand next to v is trivial' = the vertex rotation;
     the split with every k strand on the a1 side gives 'Delta^2 of A_l and all k strands is trivial' = in the cover the
     half twist Delta_2n absorbed by rotating the lower half of K by pi.)
 After (V) and every (R), the event list is literally from_halfword(h) (events_to_halfword asserts the round trip).
 S2 closed form (asserted equal to the event-level translation on all 58,887 words):
     h(W) = s.l2 . T(W) . T(f(W)) . u1,  T: a->y1, A->x1, b->x2, B->y2, c->y0, C->x0, d->x0.x1.x0.x1, D->y0.y1.y0.y1.
 K(h) := alex.symmetrize(h) is then the lift of the arc of Theta(W) (project convention: from_halfword(h) is the quotient of
 alex.symmetrize(h); engineC2 calib.py 150/150; every certified region of the cx lane rests on the same convention).

### 2a. Validation of the construction
 * EXHAUSTIVE J TEST (validate_s2.py, all 58,887 words of engineC2's |W| <= 7 enumeration, first letters a, B, d):
   event-level translation == closed form 58,887/58,887; lp.J(h(W)) == plat2.J(W) EXACTLY (engineC2's own evaluator)
   58,887/58,887, of which 47,406 non-unit; the J = 1 set is the same by both (11,481) and equals engineC2's stored unit
   list word for word.  CHECKED(58,887).
 * E4-type rings at m = 3, 5, 7, 9 (e4_controls.py): 24 non-unit E4 configurations (special words abba, abCa, BABA, dbab,
   aDB, Baba; rational and nested slot boxes, N in {-1,0,1}; rings at levels m = 3: 20, 5: 17, 7: 18, 9: 3 configurations):
   lp.J(translated halfword) == engineC2's J (fastS.J_of on the exactly fitted 2-slot form gtable.Ghat) 24/24.  CHECKED(24).
 * handedness control (sign_control.py): first 400 S2 words (|W| <= 5) containing c/C/d/D: lp.J(h(W)) == plat2.J(W) for
   400/400; with the WRONG-handed rule (d -> y0.y1.y0.y1) only 24/400.  So the J test sees the handedness.  CHECKED(400).
 * rule (R) at m = 5 (needed by E4 bodies with caps; rule_test_m5.py): random point-symmetric theta-curves with five k strands
   and rings on both axis lines: theta.J_events(original) == lp.J(translated halfword) 12/12 + 60/60 (wrong-handed: 5/12,
   31/60).  The full-twist word itself: equal to (s_0...s_{m-2})^m in the faithful Artin representation, m = 2..9
   (twist_identity.py).  CHECKED.
 * NONTRIVIAL CONTROLS (make_control_words.py): one word per distinct non-unit J of the S2 enumeration (1,883 words; J != 1
   => Theta nontrivial => K nontrivial, since the unknot has a unique strong inversion with trivial quotient):
   1,883/1,883 CERTIFIED_NONTRIVIAL (rep certificates), 0 certified unknot, 0 UNRESOLVED.  CHECKED(1,883).
   E4 controls: the 24 non-unit E4 configurations above: 24/24 CERTIFIED_NONTRIVIAL (rep), V_K/J relations 24/24.
 * V_K of the constructed K vs engineC2's J (vk_vs_j.py) on the same 1,883 knots: a_2(K) = -V_K''(1)/6 equals -J''(-1)/24
   (N1) AND J(t) == V_K(t^2) mod Phi_10 (N2) on 1,883/1,883.  CHECKED(1,883).

## 3. S2: the 11,481 J = 1 words (make_unit_words.py, code/cert_words.py)   [CERTIFIED]
Input: exactly engineC2's stored unit lists (enum2_s1p_7.pkl 3,781 + enum2_s2m_7.pkl 6,151 + enum2_trp_7.pkl 1,549 = 11,481
words, first letters a, B, d), each translated by the event-level translation (equal to the closed form, asserted).
11,481 distinct halfwords.  Audited certifier (u1/code = cert/run/code, paths only), 3 processes, default budgets:
 11,481/11,481 CERTIFIED_UNKNOT, all by Tietze certificates (route b), crossings of K: 4-49 (median 34; only 409 have
 <= 24, so route (a) alone would not have sufficed); median 0.011 s, max 0.43 s; 0 UNRESOLVED, 0 NONTRIVIAL, no HIT.
 (cert_s2_units.jsonl.gz holds every certificate with its full move list.)
Coverage of the region S2 |W| <= 7 (engineC2 sec. 5): the enumeration (engineC2/enum2.words) contains the lexicographically
least representative of every reduced commutation class, hence a representative of every word of length <= 7 up to planar
isotopy (commuting letters) and R2 cancellation; first letters c/C (ring of L at v_top = in the cover a kink y0/x0 on the
s-cap: R1) and b/B (kink on the k cap: R1) only shorten the word; first letters A, b, D are mirror copies (inverting every
letter mirrors Theta, hence K; the mirror of the unknot is the unknot).  The connectivity rule (plat2.is_arc) removes
exactly the configurations in which k is not one arc.  So EVERY J = 1 theta-curve of class S2 with |W| <= 7 has K = an
unknot certified by a replayable pi_1 certificate: region S2 |W| <= 7 CERTIFIED (PROVED translation + certified members).
 Bonus: the mirror copies stored by engineC2 (enum2_s1m_7 3,781 + enum2_trm_7 1,549 = 5,330 J = 1 words, first letters
 A, D) translated and certified the same way: 5,330/5,330 CERTIFIED_UNKNOT (Tietze), so the mirror argument is not even
 needed for those first letters (first letter b = mirror of B: covered by the argument).

## 4. Periodic families (families.py, gen_kernel.py, kernel_validate.py)   [PROVED + CERTIFIED members]
For W_n = (W0)^n the translated halfword is s.l2 . w^n . f(w)^n . u1 (w = T(W0), f(w) = T(f(W0)), asserted against the
event-level translation).  In the cover, K(W_n) = (top tangle T: the three caps of s.l2) . w^n . f(w)^n . (bottom tangle B:
the cups of u1 and the final u0).  If w^p stabilises T (T.w^p ~ T rel boundary) and f(w)^p stabilises B (f(w)^p.B ~ B),
then K(W_{n+p}) ~ K(W_n) for every n >= 0.  Stabilisers are decided EXACTLY by LEMMA K (cert/run REPORT sec. 5, PROVED:
trivial cap/cup tangles are determined by the kernel of pi_1(boundary) -> pi_1(complement)), via gen_kernel.py = the
audited code/tangle_kernel.py with N, pairs and letter map as parameters.
 gen_kernel VALIDATION (kernel_validate.py): (1) in tangle_kernel's own N = 10 setting, same_top/same_bottom agree with the
 audited tool on 3,000/3,000 random pairs (1,467 'equal' answers); (2) in the S2 picture (hw = 3; caps (0,1),(2,3),(4,5)
 and cups (1,2),(3,4),(0,5), re-derived from alex.symmetrize('s.l2.u1')) the known answers come out 11/11: x0, y0, x2, y2
 stabilise the top (legs of the s-cap / l2 caps), x1, y1 do not; x1, y1 stabilise the bottom (legs of the u1 cups), x0,
 x2, y0 do not.  CHECKED.
| family | w ; f(w) | theta-curve for | stabiliser powers (top ; bottom), p <= 6 | conclusion | certified members |
|---|---|---|---|---|---|
| (BB)^n | y2.y2 ; x1.x1 | all n | 1..6 ; 1..6 | K(W_n) = K(s.l2.u1) for all n (also directly: twists of the legs of a cap / cup) | n = 0..12, 13/13 |
| (Ab)^n | x1.x2 ; y1.y2 | n != 2 mod 3 (n = 2 mod 3: k = arc + closed loop, not in the family) | 3, 6 ; 3, 6 | period 3: two knot types, n = 0 and n = 1 mod 3; second proof: the k-braid is (s1 s2)^n (s2 s1)^-n in B_3 and (s1 s2)^3 = (s2 s1)^3 = Delta^2 is central, so the braid itself has period 3 | n = 0,1,3,4,6,7,9,10,12: 9/9 |
| (aB)^n | y1.y2 ; x1.x2 | n != 2 mod 3 | 3, 6 ; 3, 6 | period 3 (same two proofs) | 9/9 |
| (AAbd)^n | x1.x1.x2.x0.x1.x0.x1 ; y0.y1.y2.y2 | all n | 2, 4, 6 ; 2, 4, 6 (w itself is NOT a stabiliser) | period 2: K(W_n) = K(W_0) (n even) or K(W_1) (n odd) | n = 0..12, 13/13 |
 J = 1 re-checked for every theta-curve member n <= 8 by BOTH lp.J(h) and plat2.J(W) (families.json).  Certification of
 the 44 member halfwords (n = 0..12): 44/44 CERTIFIED_UNKNOT (Tietze; cert_families.jsonl.gz).  Hence every member of all
 four families (n >= 0) is the unknot: CERTIFIED (PROVED identification + certified members of every residue class).
 Note (correction to engineC2 sec. 10 wording): (Ab)^n and (aB)^n are theta-curves only for n != 2 mod 3; on those n they
 are identically J = 1 (engineC2's periodic.py already skipped the non-arc n).

## 5. Fresh-process re-check by BOTH independent checkers (code/verify_sample.py, fraction 1.0)
 replay.py (fixed checker) AND audit-2's a2lib (own Morse sweep, own Wirtinger presentation, own Tietze replayer):
| file | records | certificates | pass both |
|---|---|---|---|
| cert_s2_units.jsonl.gz (the 11,481) | 11,481 | 11,481 tietze | 11,481 |
| cert_s2_mirror_units.jsonl.gz | 5,330 | 5,330 tietze | 5,330 |
| cert_families.jsonl.gz (44 members) | 44 | 40 tietze + 4 unknot0 | 44 |
| cert_s2_controls.jsonl.gz (nontrivial controls) | 1,883 | 1,883 rep | 1,883 |
| cert_e4_units.jsonl.gz (65 E4 pairs) | 65 | 65 tietze | 65 |
| cert_s2_controls_random.jsonl.gz (3,000 random non-unit S2 words, seed 29) | 3,000 | 3,000 rep | 3,000 |
| cert_e4_controls.jsonl.gz (24 non-unit E4 configurations) | 24 | 24 rep | 24 |
 Totals: 16,920 CERTIFIED_UNKNOT records (16,916 tietze + 4 unknot0) and 4,907 CERTIFIED_NONTRIVIAL records (rep), every
 certificate accepted by both checkers; the 3,000 random controls also satisfy the V_K/J relations 3,000/3,000.

## 6. E4: the 65 unit (box, N) pairs (e4_words.py)   [CERTIFIED]
Rebuilt exactly as engineC2/cert_e4.py does (e4_s1p_4 / s2m_4 / trp_4 pickles: special S2 word W_s, slot box body
vc.word(T), T = box tree with the integral part N, on (A_l, k) at the end of the top half, point-symmetric gluing).  The
mirror body f(B) sits on (k, A_r): its rings are A_r rings at levels with m = 3, 5, 7 k strands (the body's caps add
strands), all transferred by rule (R) (Delta^2 of 3, 5, 7 strands; the word identity for Delta^2 checked in the faithful
Artin representation for m = 2..9, twist_identity.py; rule (R) at m = 5 checked on random theta-curves, 60/60 + 12/12,
rule_test_m5.py).  Results: 65/65 translated (round trip asserted), lp.J(halfword) = 1 on 65/65 (engineC2's cert_e4 had
theta.J_events = 1 on the originals), 65 distinct halfwords, K with 122-161 crossings; certifier: 65/65 CERTIFIED_UNKNOT
(Tietze, max 0.64 s), both checkers 65/65.  Observation: all 65 bodies are the same nested box r2.x1.r2.x1.y0.u1.x0.u1
followed by axis twists (x0/y0)^j (the units differ only in the special word and the integral part).

## 7. What this changes in CLAIMS.md (suggested; CLAIMS.md itself not edited)
 * E1 (engineC2 S2 / E4 / periodic families): UNJUSTIFIED -> CERTIFIED.
   - region S2 |W| <= 7 (two-pole symmetric plats): every J = 1 theta-curve has K = unknot, certified by a replayable
     Tietze certificate on a diagram of K (11,481 words, both checkers), the identification K = lift of the S2 arc being
     the PROVED translation of section 2 (planar vertex slide + ring transfer by a 2 pi ball rotation) and the coverage
     argument of section 3;
   - E4: the 65 unit pairs CERTIFIED (the E4 scan itself, i.e. 'no other unit in E4', remains engineC2's exact
     computation, EMPTY-EXACT type, not re-examined here);
   - periodic families: CERTIFIED for all n >= 0 (Lemma K periods + certified members, section 4).
 * U1 of CLAIMS section 3: DONE.
 * New general tool: translate.transfer turns ANY circle-model theta-curve event list with rings on both axis lines
   (and v_bot on A_r at the bottom) into a halfword, so the audited certifier applies to engineC2-style constructions
   directly; gen_kernel.Picture runs Lemma K for any cap/cup pattern.
 * Small correction to engineC2 sec. 10: (Ab)^n, (aB)^n are theta-curves only for n != 2 mod 3.

## 8. Files (all under roundF/u1/)
 code/                 copy of cert/run/code (sys.path strings re-pointed only); used: certify.py via cert_words.py,
                       verify_sample.py (replay.py + a2lib_indep.py), tangle_kernel.py (reference for gen_kernel)
 translate.py          theta-curve event list -> halfword: rule (V), rule (R), events_to_halfword (round trip asserted)
 validate_s2.py        exhaustive J test on 58,887 S2 words -> out/validate_s2.json, s2_unit_halfwords.json, s2_nonunit_halfwords.json
 sign_control.py, rule_test_m5.py, twist_identity.py, e4_controls.py   validation of rule (R) (handedness, m = 5, Delta^2 word, E4 m <= 9)
 make_unit_words.py, make_control_words.py, e4_words.py, families.py   word lists (out/words_*.json)
 gen_kernel.py, kernel_validate.py   Lemma K for general cap/cup patterns (validated against the audited tangle_kernel.py)
 vk_vs_j.py            a_2 and Phi_10 relations between V_K of the constructed K and J
 out/cert_*.jsonl.gz   every record with full certificates; out/verify_*.json fresh-process two-checker summaries;
                       out/families.json, e4_halfwords.json, e4_controls.json, rule_test_m5.log, validate_s2.json
