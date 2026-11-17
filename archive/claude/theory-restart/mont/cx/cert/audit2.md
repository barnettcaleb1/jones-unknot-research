# AUDIT-2: adversarial tests of cert/certify.py (cx lane)
Auditor: Claude (audit-2 subagent), started 2026-11-17 04:02 CST.  Work folder: cert/audit2/ (scripts, data, logs).
Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.  Certification standard exactly as in the task (jones24 / tietze / unknot0;
rep = explicit nonabelian homomorphism checked on every relator; everything else UNRESOLVED).
Rule followed: the simplifier (tietze.py) was NOT read before the test cases were built and run (README API + certify.py only).

## STATUS / VERDICT (04:56, FINAL): SOUND_WITH_FIXES.  No false CERTIFIED_UNKNOT anywhere; one checker hole (F2) to fix.
- ZERO false unknot certificates: 984 runs on nontrivial knots (certify() on halfwords in default and blind mode, or
  the certifier's own pipeline on PD codes; 921 CERTIFIED_NONTRIVIAL, 63 UNRESOLVED, 0 CERTIFIED_UNKNOT), including Kinoshita-Terasaka, Conway (identified by |Hom(pi,PSL(2,7))| = 1512 vs 1176), P(-3,5,7),
  P(-5,7,17), P(-7,9,31), untwisted Whitehead doubles of 3_1 / 3_1-mirror / 4_1 (both clasps), Wh(Wh(3_1)), all mirrors,
  composites (incl. K # mirror K, K # Haken's Gordian unknot), long cancelling diagrams up to 333 crossings, 300 random
  long halfwords; plus 956 blind runs of the simplifier itself on 406 nontrivial knots (19,351 randomized attempts,
  up to 6 seeds x 12 s on the Alexander-trivial ones): 0 successes.  PROVED by code reading (after the tests): the Tietze checker's moves are exactly Tietze moves and its
  starting presentation equals my independent Wirtinger presentation (CHECKED on 3100 halfwords + 119 PD codes).
- F2 (REQUIRED FIX, checker hole, rep kind): replay.check accepts rep certificates whose noncommuting pair is not a
  pair of Wirtinger generators; forged certificates 'prove' the unknot nontrivial (5/5 accepted).  Not reachable from
  certify() as written (pairs come from reps.noncommuting_pair over gens, images keyed by gens), but it voids the
  checker-independence claim for the rep / COUNTEREXAMPLE path.
- False negatives (hard unknots): 29 of 30 hard-unknot runs CERTIFIED_UNKNOT by the Tietze route (Culprit, Monster,
  Goeritz, Thistlethwaite, Ochiai I, Tuzun-Sikora example, PZ31, FHW, fake FHW, Ochiai II reduced, all mirrors, sums of
  them up to 67 crossings, Haken's Gordian unknot mirror) and 247/247 unknot halfwords up to 246 crossings; the one
  miss is Haken's Gordian unknot (141 cr.) with the default seed 0 under load (certified with seeds 1-4 in 1.5-19 s,
  and its mirror with seed 0): F5, suggest trying several seeds.
- F1 (minor): split links (knot + crossing-free circle, e.g. s.l1.x1.y0.u1; 115 of 965 words of my random generator)
  are reported UNRESOLVED instead of NOT_A_KNOT, with V_K of the knotted component (replay.py rejects every certificate).
- F3 (performance): exact Alexander polynomial dominates long nontrivial diagrams (minutes at 230 crossings).
- F4 (cosmetic): halfword grammar not validated (unknown tokens silently ignored by alex.symmetrize AND by lp.J alike).
- Certificate cross-checks: 50 (explicit sample) + all 921 rep certificates produced here recomputed on my own
  presentation (all valid); 50 (explicit sample) + all 276 Tietze certificates produced here replayed by replay.check AND
  my replay (all valid); 130 of the builder's saved certificates from
  cert/out (mitm77 25-28 crossings, bulk_top/bottom_d8, Codex family to 86 crossings) re-verified (130/130).
- INCIDENT caused by this audit at 04:33 (see below): other lanes' pool workers were killed; main session notified.

## INCIDENT (04:33 CST, caused by this audit; please check)
While stopping my own batch I ran `pkill -f multiprocessing.spawn` for my user.  On this shared machine that pattern also
matched POOL WORKERS OF OTHER LANES.  Parents whose workers were respawned at 04:33 (so they very likely lost workers):
  roundD/refGen: rg_q4_boxes.py (pid 89117), rg_q5_closures.py (pid 90006), rg_q5_second.py (pid 92391);
  roundD/lpgen:  exact_run.py (pid 89166), d2fix2.py (pid 89741), probe_exact.py (pid 92525).
multiprocessing.Pool repopulates dead workers but LOSES the tasks they were running, so these runs may hang forever in
map/imap or end with missing results.  They should be checked and, if stalled, rerun.  (From then on this audit kills
only its own PIDs.)  Main session notified at 04:34 (SendMessage).  By 04:52 all six parent processes had exited;
whether their outputs are complete is unknown and should be checked by those lanes.

## 0. Plan
1. Independent infrastructure (my own code, imports nothing from cert/): PD codes of standard knots, my own Wirtinger
   presentation from a PD code, my own Morse-word -> PD/arcs (for halfwords), my own bracket check, my own replay of
   Tietze certificates (README move spec), my own relator check of rep certificates.
2. Hard NONTRIVIAL test cases (must never be CERTIFIED_UNKNOT): Alexander-trivial (Kinoshita-Terasaka, Conway,
   Whitehead doubles of 3_1 and 4_1, pretzel (-3,5,7)), composites, mirrors, long highly cancelling diagrams,
   random long halfwords with V_K != 1.  Halfwords where possible; PD codes through the internal API otherwise.
3. Hard UNKNOT diagrams (Culprit, Goeritz, ... ): false-negative rate.
4. Cross-checks: 50 CERTIFIED_UNKNOT certificates through replay.py AND my own replay; 50 CERTIFIED_NONTRIVIAL rep
   certificates against relators I compute myself.
5. Only then: read tietze.py / replay.py for soundness holes found by forged certificates.

## 1. Independent infrastructure (cert/audit2/a2lib.py; imports nothing from cert/)
- Morse word -> oriented diagram -> arcs/signs -> Wirtinger presentation with the README labelling (generator k+1 =
  arc beginning at crossing k): LITERALLY EQUAL to wirtinger.wirtinger(diagram.pd_from_halfword(hw)) on 400/400 random
  knotted halfwords (own generator gen.py, 3-22 letters, widths <= 5).  CHECKED(400).
- Own Morse-sweep Kauffman bracket: V_K == ident3/kauffman V_K exactly 400/400.  Own Fox-calculus |Delta(t)| at
  t = -1, 2, 3 == alex.alex_eval 400/400.  Own PD from the Morse word == diagram.pd_from_halfword 398/400 (the 2
  differences: 1-crossing diagrams whose sign is ambiguous from labels; the certifier stores signs explicitly: harmless).
- Own Tietze replayer (README move spec; canonical form re-implemented), own rep checker (bijectivity of every image,
  every relator of MY presentation, noncommuting pair), own hom counter (homcount.py).
- Test-knot sources: own Morse constructions (pretzels, 2-cables, untwisted Whitehead doubles with the framing fixed by
  the cable linking number, connected sums, cancelling insertions), Knot Atlas PD of 11n42 (cx-tools/katlas_reference.json),
  and Regina's ExampleLink data (conway, kinoshitaTerasaka, monster, gordian; data/regina_examplelink.json, transcribed
  and validated: planar (faces = n+2), one component, V and Delta as expected).
- Identity checks: Regina KT == Knot Atlas 11n42 (same V, |Hom(pi,PSL(2,7))| = 1176 both); Regina 'conway' has the same
  V and Delta = 1 but |Hom(pi, PSL(2,7))| = 1512 != 1176, so it is a different knot = the Conway knot (Riley's
  distinguishing count).  |Hom| to S3, S4, A5, S5, PSL(2,11) agree (6, 24, 180, 240, 7260).  CHECKED.
  P(-3,5,7), P(-5,7,17), P(-7,9,31): |Delta| = 1 at -1,2,3,5 (Alexander-trivial), V != 1.  Untwisted Whitehead doubles
  of 3_1, mirror 3_1, 4_1 (both clasps) and the iterated double Wh(Wh(3_1)) (90 crossings): Delta = 1, V != 1.
  monster (10 crossings): V = 1 (unknot by Tuzun-Sikora).  Gordian (141 crossings): planar, one component.

## 2. Results
### 2a. Forged certificates against replay.check (forge.py)  [04:28]
- rep: 5/5 forgeries with a non-generator noncommuting pair ACCEPTED (F2).  Non-bijective image, float entries,
  degree mismatch, honest abelian rep with pair inside gens: rejected.
- tietze: 13/13 forgeries rejected (elim with 2 occurrences, nielsen x == a / d = 2 / d = 0 / absent generator,
  mult i == j / e = 2 / e = 0, negative index, bool index, float rotation, unknown kind, empty list).
- jones24: rejected on V != 1, on V = 1 diagrams with 30, 38, 54 crossings, on a split link; unknot0 rejected on
  knots with crossings and on a 3-component crossing-free diagram.  Controls accepted.
- Code reading of replay.py (after the tests were built): elim/mult/nielsen preconditions are exactly the Tietze
  preconditions; canonical_cyclic always returns a cyclic conjugate of w or w^-1 (sound even if not minimal);
  the end test is 1 generator and 0 relators.  The Tietze kind is SOUND as a checker given the presentation.
- replay.wirtinger_presentation(hw) == my independent Wirtinger presentation: 600/600 random halfwords
  (widths <= 7, up to 30 letters).  CHECKED(600).

### 2b. Halfword route, public API certify(hw, write_hits=False), default mode  [04:20-04:33; res1.jsonl]
| set | what | n crossings | result |
|---|---|---|---|
| H1 | 300 random long halfwords (own generator, 20-60 letters, widths 3-7), V != 1 | 3-333 | 300 CERTIFIED_NONTRIVIAL (Aff(F_p)/S_n/A_n reps) |
| H2 | 120 mirrors of H1 (x <-> y) | | 120 CERTIFIED_NONTRIVIAL |
| H3 | 310 composites: 80 equivariant sums s.B1.B2, 40 K#K, 40 K#mirror K, 40 triple sums, 80 swap sums (no axis letters), 30 K # (V = 1 small unknot diagram) | | 310 CERTIFIED_NONTRIVIAL |
| H4 | 34 of 150 long cancelling diagrams (W.W^-1 insertions, 56-333 crossings) | | 34 CERTIFIED_NONTRIVIAL (run stopped: see F3) |
- ZERO CERTIFIED_UNKNOT on 764 nontrivial knots.  Every returned rep certificate (764) re-verified by MY relator check
  on MY presentation (bijectivity, all relators, noncommuting generators): 764/764 valid.  CHECKED(764).
- F3 (performance, not soundness): on long nontrivial diagrams certify() spends almost all its time in
  diagram.alexander (exact polynomial determinant), needed only for the affine-rep search: 64 s at 137 crossings,
  435-526 s at 228-238 crossings (machine load ~300, so perhaps 5-10x less unloaded).  The affine search only needs
  Delta mod p (or det of the Alexander matrix at t = lambda mod p), which is O(n^3) mod p.  Suggested fix only.

### 2c. PD route (certifier pipeline on PD codes built by me: wirtinger, tietze.simplify blind, reps.find_rep;
### every success re-checked by replay.replay_moves AND my replay / my relator check)  [04:34-04:40; res_pd.jsonl]
- The certifier's Wirtinger presentation of each PD == mine literally: 83/83.
- Alexander-trivial knots, Tietze forced (10 s) then reps: KT (Regina and Knot Atlas), Conway, all mirrors; P(-3,5,7),
  P(-5,7,17), P(-7,9,31) (47 cr.) and mirrors; Wh+-(3_1), Wh+-(3_1 mirror), Wh+-(4_1) and mirrors: ALL Tietze FAILED
  (correct) and ALL CERTIFIED_NONTRIVIAL (A5 or PSL(2,7)), certificates valid under my check.  Wh(Wh(3_1)) (90 cr.,
  rep search disabled > 60 cr.): Tietze failed, UNRESOLVED.
- Composites (PD connected sums at two different edge pairs): KT#Conway, KT#KT, Conway#Conway, KT#P(-3,5,7),
  Conway#Wh(3_1), Wh(3_1)#Wh(4_1), P(-3,5,7)#Wh(4_1), Conway#mirror(Conway), KT#mirror(KT), K#monster (4 knots),
  KT/Conway/P(-3,5,7) # Haken's Gordian unknot (152-156 cr.): Tietze failed on every one; reps found except
  KT#mirror KT, Wh(3_1)#Wh(4_1), Conway#Wh(3_1)@0,0 (UNRESOLVED in 60 s under load) and the > 60-crossing ones.
- Long cancelling Morse diagrams of Delta = 1 knots (P(-3,5,7), Wh(3_1), Wh(4_1), P(-5,7,17) with W.W^-1 insertions,
  54-200 crossings): Tietze failed on all 24 (correct); the simplifier typically ends at 2-3 generators.
- Hard unknots: Regina 'monster' (10), mirror, monster#monster_m (20), monster^3 (30): CERTIFIED by Tietze in < 10 ms;
  Haken's Gordian unknot mirror (141): CERTIFIED by Tietze in 25 s (6 attempts).

### 2d. Hard unknots (false negatives) and nontrivial knots with hard-unknot summands  [04:38; res_pd2.jsonl]
Gauss codes of Burton-Chang-Loffler-de Mesmay-Maria-Schleimer-Sedgwick-Spreer, 'Hard diagrams of the unknot'
(arXiv:2104.14076, appendix), transcribed (data/hard_unknots_burton2021.json); crossing signs recovered by planarity
(faces = n + 2; for the monster the recovered signs equal Regina's up to a global flip), every diagram one component,
planar, V = 1.  Haken's code in that appendix is identical to the Regina 'gordian' data transcribed in 2a.
| diagram | n | Tietze route (V = 1 path, budget 30 s) |
|---|---|---|
| Culprit, Culprit mirror | 10 | CERTIFIED_UNKNOT, 1 attempt, 2 ms |
| Monster (+ mirror) | 10 | CERTIFIED_UNKNOT, 1-2 ms |
| Goeritz (+ mirror) | 11 | CERTIFIED_UNKNOT, 2-70 ms |
| Thistlethwaite (+ mirror) | 15 | CERTIFIED_UNKNOT, 3 ms |
| Ochiai I (+ mirror) | 16 | CERTIFIED_UNKNOT, 3-5 ms |
| Tuzun-Sikora example (+ mirror) | 21 | CERTIFIED_UNKNOT, 6 ms |
| PZ31 (+ mirror) | 31 | CERTIFIED_UNKNOT, 20 ms |
| Freedman-He-Wang, 'fake' FHW (+ mirrors) | 32 | CERTIFIED_UNKNOT, 12-18 ms |
| Ochiai II reduced (+ mirror) | 35 | CERTIFIED_UNKNOT, 0.4-0.5 s |
| Ochiai I # Culprit; Goeritz^3; Culprit # Goeritz # Thistlethwaite | 26, 33, 36 | CERTIFIED_UNKNOT, 8-116 ms |
| FHW # Ochiai II reduced | 67 | CERTIFIED_UNKNOT, 2.4 s (2 attempts) |
| Haken's Gordian unknot, mirror (2c) | 141 | CERTIFIED_UNKNOT, 25 s |
=> 0 false negatives on these 24 runs (all > 24-crossing ones certified by the Tietze route itself); with 2c:
   29/30 hard-unknot runs certified, the miss being Gordian (non-mirror) with seed 0 (2e).
- Rep search ON UNKNOTS with the Tietze route disabled and jones24 skipped (Culprit, Goeritz, Thistlethwaite, Ochiai I,
  FHW, PZ31): all UNRESOLVED, no representation claimed (no false COUNTEREXAMPLE path).
- Nontrivial knots with a hard-unknot summand, Tietze forced 15 s: KT#Culprit, Conway#Goeritz, P(-3,5,7)#Thistlethwaite,
  Wh(3_1)#Ochiai I: Tietze failed, CERTIFIED_NONTRIVIAL (A5); KT#FHW (43), Conway#PZ31 (42): Tietze failed, UNRESOLVED
  (rep search disabled > 40 crossings in this run).  No false unknot.

### 2d'. Blind Tietze stress on nontrivial knots (tz_runner.py: tietze.simplify directly, several seeds; any
### success would be replayed by replay.check and by my replay)
- Set A (all 150 H4 cancelling diagrams 56-333 cr., 80 H1 random long, 80 H3 composites, 30 H2 mirrors): 340 knots
  x 2 seeds x 5 s: 680 runs, 13,520 randomized attempts, 0 successes.
- Set B (Alexander-trivial, 6 seeds x 12 s): KT (Regina, Knot Atlas), Conway, their mirrors, P(-3,5,7), P(-5,7,17),
  P(-7,9,31), all Whitehead doubles and mirrors, 12 composites: 36 knots, 216 runs, 4,787 attempts, 0 successes
  (final presentations 3 or 5 generators).  Stopped at 36 of 78 planned knots (time); the rest went to set C.
- Set C (2 seeds x 10 s): the 24 Alexander-trivial swap-sum halfwords and sums (30-94 cr.) and the 6 nontrivial #
  hard-unknot composites: 30 knots, 60 runs, 1,044 attempts, 0 successes (final presentations 5-11 generators).
  TOTAL: 406 nontrivial knots, 956 runs, 19,351 attempts, 0 successes.  CHECKED(956).

- Public API in BLIND mode (certify(hw, blind=True): Tietze forced 3 s, then reps) on 60 random H1/H2/H3/H4 knots
  (<= 80 crossings): 60/60 Tietze failed and CERTIFIED_NONTRIVIAL, certificates valid under my check.

### 2e. Unknot halfwords through the public API  [04:41-04:50; res678.jsonl]
- H6: 240 unknot halfwords (120 V = 1 diagrams with <= 24 crossings = unknots by Tuzun-Sikora; 120 of them inflated
  by W.W^-1 insertions to 25-182 crossings): 240/240 CERTIFIED_UNKNOT by the TIETZE route (median 10 ms, max 1.6 s);
  every certificate re-verified by my replay on my presentation.  CHECKED(240).
- H7: the same inflated unknots (> 24 crossings) with the Tietze route switched off (tietze_budget = 0): the
  representation search runs on a V = 1 unknot diagram and must find nothing: 43/43 so far UNRESOLVED (no false
  CERTIFIED_NONTRIVIAL / COUNTEREXAMPLE; write_hits=False throughout this audit).
- Haken's Gordian unknot (141 cr., non-mirror orientation): with the default seed 0 the Tietze route FAILED in 60 s
  (6 attempts, final 9 gens / 9 rels) under load ~300 -> UNRESOLVED (rep search then found nothing, correct).  Retried
  with seeds 1, 2, 3, 4: CERTIFIED in 1.5, 4.7, 15.1, 18.8 s (2-7 attempts, 144-161 moves), each certificate accepted
  by replay and by my replay.  Its mirror was certified with seed 0 in 25 s.  The only false negative in the audit;
  it is seed-specific (F5: certify() tries one seed only).
- H7 completed: 60/60 UNRESOLVED (rep search on V = 1 unknot diagrams of 25-182 crossings never claims a rep).
- H8: Codex's fixed template s.l1.l1.x2.x1.x1^(2m).y3^(2m).x1.u2.u2 at m = 12, 15, 20, 25, 30, -15, -25
  (102-246 crossings): 7/7 CERTIFIED_UNKNOT by Tietze, 1 attempt, <= 1.05 s each; my replay agrees.

### 2f. Alexander-trivial halfwords through the public API  [res5.jsonl, res9.jsonl]
- Swap sums K' # rK' built from MY Morse words (s.l1.<K' on the right side>.u2; V = V(K')^2 and Delta = Delta(K')^2
  CHECKED on 3_1, 4_1, P(-3,5,7), Wh(3_1), Wh(4_1)): K' in {P(-3,5,7), P(-5,7,17), Wh+-(3_1), Wh+(3_1 mirror),
  Wh+-(4_1)}, their mirrors, equivariant sums of two of them, cancel-inflated versions (30-220 crossings), Delta = 1 at
  -1, 2, 3 and V != 1 for all: 18 CERTIFIED_NONTRIVIAL (A5), 30 UNRESOLVED (rep search within 30 s fails on the
  70-220-crossing ones under load), 0 CERTIFIED_UNKNOT (48/48 finished).
- Random search with my own generator (2.1M halfwords, 654k knots, 15 min x 3 cores): 3 Alexander-trivial knots
  (|Delta| = 1 at -1, 2, 3, 5; V != 1; 20-33 crossings; V differs from KT/Conway).  They, their mirrors and 9
  cancel-inflated versions: default mode 15/15 CERTIFIED_NONTRIVIAL; blind mode (Tietze forced 10 s) 15/15 Tietze
  failed and CERTIFIED_NONTRIVIAL; all certificates valid under my check.  0 CERTIFIED_UNKNOT.

### 2g. Certificate cross-checks requested by the task
- 50 CERTIFIED_NONTRIVIAL rep certificates (random sample of my H1-H3 runs; certcheck.py rep): recomputed on MY
  Wirtinger presentation (own Morse sweep): 50/50 every image a permutation, every relator trivial, pair of generators
  noncommuting, image group order 6-21 (nonabelian), no image keys outside the generators; replay.check agrees 50/50.
  Plus every one of the 800+ rep certificates produced in this audit was checked the same way inline: all valid.
- 50 CERTIFIED_UNKNOT tietze certificates (random sample of H6; certcheck.py tietze): replay.check 50/50, MY replay
  50/50.  Transplant test (switch one crossing letter, keep the moves): 32 rejected, 18 accepted; an accepted transplant
  must be an unknot again (acceptance proves pi_1 = Z if the checker is sound): transplant_check.py ran EVERY
  single-crossing switch of 60 certified halfwords: 3803 transplants, 1291 accepted, ALL 1291 with V = 1 (my bracket),
  2512 rejected; 0 accepted with V != 1.  CHECKED(3803).
- Group-level validation independent of arcs and signs (platcheck.py): |Hom(pi, S3)|, |Hom(pi, S4)| (and |Hom(pi, A5)|
  for 25 of them) from my Wirtinger presentation (= the checker's) agree with my own plat presentation (Artin action on
  the Morse sweep, no arcs, no signs) on 80/80 random knots.  CHECKED(80).
- Targeted presentation test: replay.wirtinger_presentation == my presentation on 2500 further words with kinks at
  crossing 0, axis-only / axis-free words, widths up to 9.  CHECKED(2500) (3100 in total with 2a).
- 130 of the BUILDER's saved certificates (cert/out/: 70 from mitm77 incl. 60 with 25-28 crossings, 20 bulk_top_d8,
  20 bulk_bottom_d8, 20 Codex family up to 86 crossings): replay.check 130/130, MY replay 130/130, V = 1 by my
  bracket 130/130.  CHECKED(130).

Minimal reproduction of F2 (accepted by the current replay.check; the halfword is the crossing-free unknot):
```
import sys; sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert'); import replay
replay.check({'kind': 'rep', 'halfword': 's.l1.l1.u2.u2', 'degree': 3,
              'images': {'1': [0, 1, 2], '1000': [1, 0, 2], '1001': [1, 2, 0]}, 'noncommuting': [1000, 1001]})
# -> (True, 'NONTRIVIAL: hom to ? (degree 3), all 0 relators checked, images of 1000,1001 do not commute')
```

## 3. Required fix and suggested fixes
REQUIRED (F2), in replay._check, kind 'rep', before the commutation test:
```
        if set(img) != set(gens): return False, 'images must be given for exactly the Wirtinger generators'
        g, h = cert['noncommuting']
        if g not in gens or h not in gens or g == h:
            return False, 'noncommuting pair must be two distinct Wirtinger generators'
```
Prototype on a COPY (audit2/replay_fixed_proposal.py; the project file was not edited): rejects 5/5 forgeries,
accepts 300/300 genuine rep certificates and 100/100 genuine Tietze certificates from this audit.  After the fix,
re-run the saved-certificate replays and any HIT logic tests.
SUGGESTED: F1 pd_from_halfword should reject diagrams with crossing-free components (use the segment count it already
computes, ncomp0, for n > 0 as well) so split links give NOT_A_KNOT; F5 on V_K = 1 diagrams try several seeds before
giving up (Gordian: seed 0 failed in 60 s, seeds 1-4 succeeded in 1.5-19 s); F3 compute det(Alexander matrix) mod p at
t = lambda instead of the exact polynomial for the affine search; F4 validate the halfword grammar (or document that
unknown tokens are ignored by alex.symmetrize and lp.J alike).

## 4. Not covered / GAPs
- KT and Conway were NOT realised as halfwords (transvergent diagrams not constructed); they were run through the
  certifier's own pipeline on PD codes (same simplifier, rep search, replay.replay_moves) and, through the public API,
  Alexander-trivial knots were covered by swap sums of P(-3,5,7), P(-5,7,17), Wh(3_1), Wh(4_1) and by 3 Alexander-
  trivial halfwords found by random search.  GAP (minor).
- Trusted inputs not re-examined: alex.symmetrize as the definition of K (and its agreement with lp.J's knot), Dehn's
  lemma, and the Tuzun-Sikora theorem in the form used by the task standard (any diagram with <= 24 crossings).
- Ochiai II (unreduced, 45), III (67), IV (55) not transcribed; Haken's Gordian unknot (141) covers the large end.
- All timings were taken at load average 150-330 (other lanes); they are upper bounds, not the certifier's speed.
- The bracket-level COUNTEREXAMPLE path (V_K = 1 AND a valid rep) cannot be exercised without a counterexample; it was
  exercised negatively: rep search on 66 unknot diagrams with Tietze disabled never returned a representation.

## 5. Files (cert/audit2/)
a2lib.py (independent infrastructure), gen.py (halfword generator, cancelling insertions, swap sums), homcount.py,
pdknots.py, harness.py, run_batch.py, tz_runner.py, forge.py (+ forge_results.json), certcheck.py, check_saved.py,
transplant_check.py, totals.py, replay_fixed_proposal.py, selftest.py, search_alex1.py; case files cases*.json,
tz_cases_*.json; results res1/res5/res9/res9b/res678/res_pd/res_pd2/tz_A/tz_B/tz_gordian_*.jsonl;
data/regina_examplelink.json, data/hard_unknots_burton2021.json, data/hard_unknots_signed.json.

## 6. Summary for the orchestrator
VERDICT: SOUND_WITH_FIXES.  certify.py produced no false CERTIFIED_UNKNOT and no false CERTIFIED_NONTRIVIAL on any
adversarial input; its Tietze and jones24 checks in replay.py are sound (code reading + forgery, transplant and
presentation tests).  The rep check in replay.py has a real hole (F2: non-generator noncommuting pair accepted) that
must be closed before the checker can be called independent for the rep / COUNTEREXAMPLE path.  No HIT, no
COUNTEREXAMPLE status anywhere; write_hits=False was used for every certify() call in this audit.
