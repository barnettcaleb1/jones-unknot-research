# AUDIT-1: code soundness of cert/certify.py (Claude auditor, 17 Nov 2026)

Status: COMPLETE (17 Nov 2026, ~04:40).
Scripts and outputs: /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit1_work/ (auditor's own folder; no other file
edited).  Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.

## VERDICT (short)
SOUND_WITH_FIXES.  Every CERTIFIED_UNKNOT that certify() can return is sound (tietze / jones24 / unknot0 routes;
line-by-line proof below plus independent tests).  certify()'s own CERTIFIED_NONTRIVIAL / COUNTEREXAMPLE outputs are sound
as produced, BUT the independent checker replay.py accepts FORGED 'rep' certificates (F1): it does not verify that the
claimed non-commuting pair are images of generators.  Since replay.check is the declared trust anchor and a 'rep'
certificate + V_K = 1 is exactly the HIT evidence, F1 must be fixed before replay.py is used to (re)validate any
nontriviality or counterexample certificate.  No false certificate exists in the stored outputs (CHECKED 6,732/6,732 rep,
21,509 tietze re-replayed).  I could NOT make the code output CERTIFIED_UNKNOT on a nontrivial knot.

## 0. Scope and trusted base
Read line by line: certify.py, README.md, replay.py (checker), diagram.py, wirtinger.py, tietze.py, reps.py, refs.py,
bulk_cert.py, mitm_cert.py, validate_pd.py, validate_group.py, suites.py, stress_tietze.py, and the trusted inputs
tools/alex.py (parse, symmetrize, diagram), tools/kauffman.py (bracket).
Every CERTIFIED_* status returned by certify() requires replay.check(cert) == True (accept() in certify.py lines 66-72,
used on every route).  Hence soundness of certify()'s output reduces to replay.py + alex.parse/symmetrize/diagram +
kauffman.bracket + (Wirtinger's theorem, Dehn's lemma, Tuzun-Sikora).  The certifier's own PD code, PD Wirtinger, Tietze
simplifier and rep search are UNTRUSTED producers; errors there can only cause rejections, misrouting, or UNRESOLVED,
except for the HIT-detection routing noted in F3.

## 1. Diagram layer used by the checker (alex.symmetrize + alex.diagram)   PROVED (by reading) + CHECKED
- Morse word semantics: initial cap = positions (0,1) sharing edge 0; 'l'/'r' i: cap inserting one new edge at positions
  i, i+1 (l and r identical for the diagram); 'u' i: cup = union of the edge classes at i, i+1; 'x'/'y' i: crossing with
  TL = pos[i], TR = pos[i+1] (before), BL, BR new (after); 'x': over = TL-BR (keys ot=TL, ob=BR, ut=TR, ub=BL);
  'y': over = TR-BL (ot=TR, ob=BL, ut=TL, ub=BR).  Any word is a planar diagram (caps/cups/crossings are local).
- Knot test: every edge class has exactly two crossing ends; crossing-free circles are rejected (roots check, every
  cup-closed edge is in uf.p and edge 0 is added explicitly); one component is enforced by the traversal (seen == 2n).
  For n = 0, [] is returned only for exactly one circle.  od/ud = True iff the strand is traversed before -> after.
- Over/under convention is shared by diagram.py (CCW = TL,TR,BR,BL in the upward picture) and kauffman.py ('x':
  vertical smoothing weight A^+1 = A-smoothing for an over strand SW->NE; 'y': horizontal = A).  CHECKED below.

## 2. Wirtinger presentation in replay.py   PROVED (by reading) + CHECKED(30,828 counts on 1200 knots)
- Arcs: union of the two over edges at each crossing (uf.u(ot, ob)) -- the correct over-arc identification.  Generator
  k+1 = the arc containing the OUTGOING under edge of crossing k (ub if ud else ut); an arc beginning twice, or a
  lookup of an arc with no beginning, returns None.  Incoming under edge = ut if ud else ub.  Over arc = arc of ot.
- Sign: direction vectors in the upward picture ('x': over (1,1), under (-1,1); 'y': over (-1,1), under (1,1); negated
  when traversed against the word), s = sign(over x under) = the geometric crossing sign (a fixed global convention:
  under strand passing right-to-left of the over strand).  Relator x_{k+1}^-1 x_o^s x_in x_o^-s.  The rule is a function of the
  geometric sign only; the opposite global rule is the presentation of the reflected diagram (mirror), isomorphic group.
  So the presentation is pi_1(S^3 - K) (Wirtinger) -- given the arc data, which is the content of the next checks.
- INDEPENDENT TEST t2_homcount.py (auditor's own plat sweep with the exact Artin action on the Morse word -- no arcs, no
  orientation, no signs -- and an own DFS hom counter on replay's presentation; per conjugacy class C of G in
  {S3,S4,A4,A5,F20,F42,PSL(2,7)}: #{phi : phi(meridian) in C u C^-1}): 1200 random knots (own grammar walker with
  mid-word caps/cups and axis crossings, 2..24 crossings), 30,828/30,828 counts AGREE; 538 knots have nonabelian counts.
  CHECKED(30,828).
- POWER OF THE TEST t2b_sign_classes.py: flipping the sign rule on ONE crossing class (ty, od, ud) is detected on
  116-154 knots per class (68-86% of knots containing the class); flipping all od=False / ud=False / all 'y' detected on
  183 / 197 / 207 of 250; flipping ALL signs (mirror) is detected on 0/250, as it must be.  A planted single-crossing
  flip is detected on 382/538 knots.  So every one of the 8 sign cases is pinned (up to the global mirror).  CHECKED.
- The certifier's PD-based presentation equals the checker's literally after normal form: 1500/1500 own knots
  (t8_pd_vs_checker.py; diagram.check_pd 1500/1500).  (Only affects success rate.)  CHECKED(1500).

## 3. Tietze replay (replay.replay_moves)   PROVED (by reading) + CHECKED
- normal_form: free + cyclic reduction (cycred) applied to RELATORS only, rotation to a least rotation of r or r^-1
  (any rotation would do; ans < n always), drop empty and duplicate relators, sort.  All conjugations/inversions/
  deletions of trivial or repeated relators: Tietze.  Canonicality only matters for index agreement with the producer.
- elim (g, j): g must be a current generator, relator j must contain g^{+-1} EXACTLY once; rotate so it is first:
  w = g^e rest; img = rest^-1 if e = +1, rest if e = -1 (correct: g^e rest = 1); substitution g -> img and g^-1 ->
  img^-1 (subst uses inverse(img)), free reduction only (substitution words are never cyclically reduced); relator j and
  g deleted.  This is the inverse of "add generator g with relator g = img" (img free of g, re-checked).  Valid.
- mult (i, j, e, kj, ki): i != j both in range, e in {1,-1}; r_i := freered(rot(r_j^e, kj) . rot(r_i, ki)); r_j kept,
  so r_i is recovered: normal closure unchanged.  Valid.
- nielsen (x, a, d, side): x != a, both current generators, d = +-1: x -> x a^d or a^d x in all relators =
  elementary Nielsen automorphism of the free group: maps N(R) onto N(phi R).  Valid.
- Acceptance only at len(G) == 1 and R == []: <a | > = Z, so K is the unknot (Dehn's lemma; Papakyriakopoulos).
  Invariant: letters of R are always current generators (elim substitutes every occurrence).
- Python-level: JSON floats/bools equal to ints behave as the ints (no exploit found); non-integral or wrong types raise
  -> check() turns every exception into a rejection.
- INDEPENDENT TEST t4_replay_invariance.py: 600 own knots (<= 10 crossings), random VALID sequences (elim, mult with random
  rotations/exponents, nielsen) replayed by replay.replay_moves, then |Hom(<G|R>, H)| by brute force over H^|G| vs
  |Hom(pi_1, H)| from the auditor's plat sweep, H in {S3, A4, F20}: 1737/1737 invariant (266 nonabelian), 0 errors;
  280 sequences reached <a | >, all on knots with V_K = 1 (<= 10 crossings, hence unknots).  CHECKED(1737).

## 4. Independence of replay.py   CHECKED (reading)
- Imports only sys, json, tools/alex.py, tools/kauffman.py; no certifier module.  Own presentation (from alex.diagram,
  not from the PD code), own canonical form (Duval, not Booth), own move semantics.  In-process it shares the alex
  module object with diagram.py; grep finds no monkeypatching of alex or kauffman anywhere in cert/.  No other alex.py or
  kauffman.py exists in the project tree (sys.path shadowing impossible).

## 5. jones24 and unknot0   PROVED (by reading) + CHECKED
- jones24: knot test + crossing count of the actual Morse diagram (alex.diagram, <= 24) + VK_project(kauffman.bracket)
  == 1, i.e. the bracket is a single monomial (equivalent to V_K = 1 for a knot: a unit V with V(1)=1, V'(1)=0 is 1;
  normalisation-independent).  kauffman.bracket sweeps the same full word with the same over/under convention.
- INDEPENDENT TEST t3_bracket.py: kauffman.bracket == auditor's brute-force state sum (all 2^n states, own edge graph,
  A-smoothing derived from first principles) on 756/756 knots with 1..14 crossings; VK_project == diagram.jones on
  1239/1239 knots with 1..26 crossings (643 with V_K = 1).  CHECKED(756), CHECKED(1239).
- unknot0: accepted iff alex.diagram returns [] (crossing-free, exactly one circle).  Correct.
- External: Tuzun-Sikora (JUC verified for knots up to 24 crossings) is accepted by the task's certification standard.
  Remark (not a code issue): the code applies it to ANY diagram with <= 24 crossings (possibly composite knot types);
  this is within the standard as stated ("an actual diagram of K with <= 24 crossings together with V_K = 1").

## 6. rep checker (CERTIFIED_NONTRIVIAL)   DEFECT F1
- Verifies: every generator of the CHECKER's presentation has a permutation image of the stated degree; every relator
  evaluates to the identity (von Dyck: a homomorphism).  CORRECT.
- Does NOT verify that the 'noncommuting' labels g, h are generators.  It compares img[g], img[h] for ANY keys present in
  cert['images'].
F1 (DEFECT, replay.py lines 251-253).  Forged certificate (t1_forged_rep.py): all generators -> identity, extra keys
   999 -> (1 0 2), 998 -> (0 2 1), noncommuting [999, 998].  replay.check ACCEPTS it ('NONTRIVIAL: hom to S3 ...') on
   s.l1.x1.u2 (2-crossing unknot diagram) and on s.l1.l1.x2.x1.x1.x1.y3.y3.x1.u2.u2 (Codex family m=1), which the same
   checker also accepts as jones24 UNKNOT; also via the CLI after a JSON round trip (forged_rep_2.json,
   forged_rep_14.json).  The control (pair = two real generators) is rejected.  CHECKED.
   Impact: certify() never emits such a certificate (reps.noncommuting_pair iterates over gens), and all 6,732 stored rep
   certificates satisfy the strict condition (pair in gens, image keys == gens) (t5_saved_certs.py).  But the README's
   independence claim ("a bug in the certifier can only cause a rejection") is false for 'rep', and a HIT double-check
   by replay.py would pass a corrupted/forged counterexample certificate.
   REQUIRED FIX: in replay._check 'rep', reject unless g and h are in gens (ints, g != h); better: ignore the claim
   and accept iff SOME pair of generator images fails to commute; also reject image keys outside gens.

## 7. Other findings (no false certificate possible)
F2 (DEFECT, certifier PD layer) diagram.pd_from_halfword accepts split links "knot + crossing-free circles" as knots
   (morse_crossings: "number of closed components without crossings is irrelevant for knots with >= 1 crossing" -- it is
   not).  141 of 2500 words in t3 (all with alex.diagram = None and pd != None; never the converse), e.g. s.l1.y0.u1,
   s.r1.x1.x0.x1.u1, s.r1.r2.x4.y4.u4.u2 (own component count: 2-3 components).  Effect: certify() returns UNRESOLVED
   instead of NOT_A_KNOT and V_K is that of the knot component; every certificate is rejected by replay.check (alex.diagram
   rejects links), so no false certification.  Never the converse: no knot is discarded as NOT_A_KNOT (2500 words).
   FIX (recommended): in morse_crossings/pd_from_halfword reject when any edge class has no crossing end (as alex does).
F3 (ROBUSTNESS, HIT detection) the routing flag v_trivial and hence COUNTEREXAMPLE detection use only diagram.jones (the
   PD bracket); kauffman.bracket is consulted only when diagram.jones already says V_K = 1.  A diagram.jones error V != 1
   on a true V_K = 1 knot would turn a counterexample into a plain CERTIFIED_NONTRIVIAL (missed HIT).  diagram.jones ==
   kauffman on 1239/1239 (t3) and 650/650 (builder), so no evidence of such an error.  FIX (recommended): compute
   replay.VK_project for every CERTIFIED_NONTRIVIAL result and treat V_K = 1 by EITHER bracket as a HIT candidate.
F4 (MINOR) bulk_cert.one returns CERTIFIED_UNKNOT 'unknot0' for pd.n == 0 without calling replay.check (mathematically
   correct; violates "every certificate re-checked").  mitm_cert's 568,895 jones24 classifications were checker-accepted
   at run time but their words are not stored, so they are re-checkable only by regenerating the (7,7) screen.  The
   HIT file written by certify.write_hit lacks J (BRIEF section 5 asks for word, J, V_K, Delta, method).
F5 (MINOR, README) "two images that do not commute" is stated as checked; it is checked only for the labels supplied
   (F1).  README/REPORT stress counts differ (26,201 first run, 35,381 rerun; the summary's 61,582 is their sum).

## 8. Adversarial attempts to obtain CERTIFIED_UNKNOT on a nontrivial knot (all FAILED)
- t6_forge_tietze.py on the trefoil s.l1.y0.x1.u2: empty moves, moves as string/None, wrong kind spelling, unknot0 and
  jones24 kinds, missing halfword, 2195 short move sequences with type tricks (bool/float/negative/out-of-range indices,
  i == j via True, x == a via True, d in {0,2}, bad sides), 22 transplanted Tietze certificates of 3-crossing unknots:
  0 accepted.
- Split links (F2): certificates rejected by the checker.
- Random valid move sequences (t4): <a | > reached only on V_K = 1 knots.
- t7_blind_certify.py: certify() in BLIND mode (Tietze forced on every knot) on 300 auditor-generated knots and their
  mirrors (8..30 crossings): 138 CERTIFIED_UNKNOT, all with V_K = 1 (project bracket); 162 CERTIFIED_NONTRIVIAL, all with
  V_K != 1; 0 UNRESOLVED; 0 false unknot certificates; every returned certificate re-accepted by replay.check; all 162
  rep certificates satisfy the strict pair condition.  CHECKED(300).
- Codex regression family s.l1.l1.x2.x1.x1^(2m).y3^(2m).x1.u2.u2, m in {-10,-5,-1,0,1,5,10}: CERTIFIED_UNKNOT by replayed
  Tietze certificates (6..86 crossings), consistent with Codex's geometric unknotting.  CHECKED(7).

## 9. Stored outputs (t5_saved_certs.py)
28,241 stored certificates re-checked in a fresh process: all 6,732 'rep' certificates (accepted; pair in gens and image
keys == gens for 6,732/6,732, so F1 never occurred in the record) and 21,509 'tietze' certificates (all suite files in
out/ and out/v3/, 4,000 random from each bulk/mitm gzip, the two recert files): 21,509/21,509 accepted.  CHECKED(28,241).

## 10. Test index (all in audit1_work/)
 t1_forged_rep.py      F1 forged rep certificates accepted (2/2) + controls        -> forged_rep_2.json, forged_rep_14.json
 t2_homcount.py        replay Wirtinger vs own plat, 30,828/30,828 counts          -> t2_hom_1200.json
 t2b_sign_classes.py   test power vs systematic sign bugs                          -> t2b_sign_classes.json
 t3_bracket.py         kauffman vs brute force 756/756; vs PD 1239/1239; F2 141    -> t3_bracket_2500.json
 t4_replay_invariance.py  hom-count invariance of replayed random moves 1737/1737  -> t4_replay_600.json
 t5_saved_certs.py     stored certificates 28,241 re-checked                       -> t5_saved_certs.json
 t6_forge_tietze.py    forgery attempts on tietze/jones24/unknot0: 0 accepted
 t7_blind_certify.py   blind certify on 300 own knots: 0 false                     -> t7_blind_300.json
 t8_pd_vs_checker.py   PD Wirtinger == checker Wirtinger 1500/1500
 audlib.py             auditor's own generator, groups, plat sweep, hom counters

## 11. Verdict
SOUND_WITH_FIXES.
- CERTIFIED_UNKNOT (tietze, jones24, unknot0): SOUND.  PROVED by reading (sections 1-5) and CHECKED by independent
  implementations (t2, t2b, t3, t4, t6, t7).  Trusted: alex.py, kauffman.py (both independently re-tested here),
  Tuzun-Sikora (as in the standard), Wirtinger, Dehn's lemma.
- CERTIFIED_NONTRIVIAL / COUNTEREXAMPLE as emitted by certify(): sound (relators all checked; the pair comes from gens).
  replay.check for 'rep' is NOT sound against supplied certificates (F1).  REQUIRED before replay.py is used as the
  independent verifier of any nontriviality/HIT certificate: fix F1.
- REQUIRED (completeness of HIT detection, cheap): F3, cross-check V_K with kauffman for every CERTIFIED_NONTRIVIAL.
- RECOMMENDED: F2 (reject split links in the PD layer), F4 (route unknot0 through replay.check, store jones24 words,
  add J to the HIT file), F5 (README wording).
