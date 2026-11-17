# roundF U4/U5 REPORT: stored and certified J = 1 words of engineB's guided searches (U4) and engineA's Lemma W units (U5)
Lane folder: ~/jones-lanes/theory-restart/mont/cx/roundF/u45/ (Claude, 17 Nov 2026, started 06:50 CST).  Nothing outside u45/
is edited.  Marks: PROVED / CHECKED(n) / CONJECTURE / GAP.
CERTIFICATION STANDARD (exactly as CLAIMS.md): CERTIFIED_UNKNOT only by (a) a diagram with <= 24 crossings and V_K = 1
(Tuzun-Sikora), (b) a replayable Tietze reduction of pi_1 to <a | > (Dehn), (c) validated R-moves to 0 crossings;
CERTIFIED_NONTRIVIAL only by an explicit nonabelian representation checked on every relator; else UNRESOLVED (retained).
CERTIFIED_NONTRIVIAL with J = 1 or V = 1 = HIT (collab/HIT-<HHMM>.md at once).
Certifier: a COPY of the audited fixed cert/run/code in u45/code (only the 9 sys.path strings re-pointed; `diff -r` = those
9 lines; certify/replay/diagram/wirtinger/tietze/a2lib_indep/cert_words/verify_sample byte-identical, md5 checked), run as
cert_words.py; every certificate re-checked in a FRESH process by BOTH independent checkers (replay.py and audit-2's a2lib)
with verify_sample.py at fraction 1.0.

## STATUS (newest first)
- 07:52 FINAL.  NO HIT (no COUNTEREXAMPLE, no LEMMA_Q_HIT, no HIT file, no bracket alarm: u45/out/ empty; no kcert-
  nontrivial J = 1 word).  0 UNRESOLVED, 0 CERTIFIED_NONTRIVIAL anywhere.
  U4: all 22 E3/E3b/E3c/E3d runs (engineB's 19 main runs + 3 test runs; 3,899,467 evaluations) re-run with the original
  seeds and evaluation budgets reproduce engineB's stored outputs IDENTICALLY (22/22); every J = 1 word they met is now
  stored: 437,543 probes = 424,236 distinct (run, word) pairs = 424,235 distinct words; 424,236/424,236 CERTIFIED_UNKNOT
  (tietze; 248,480 of them have 25-77 crossings), 424,236/424,236 pass BOTH checkers in a fresh process; exact lp.J = 1 on
  4,000/4,000 sampled stored words.  Per set: width two n = 16..40 (E3 163,011 + E3b 15,202 + E3d 11,155 = 189,368 words),
  width two n = 12 (inside B1; 167,089), width three via rho_3 (E3c, 67,779), the Delta = 1 class (E3d, 11,155).
  U5: engineA's 167 + 308 Lemma W units regenerated exactly; 475/475 units (335 distinct knots) CERTIFIED_UNKNOT, both
  checkers 335/335, exact lp.J = 1 335/335 (+ 2,460 'scalar' units, 2,040 knots, all certified, both checkers, lp.J = 1).
- 07:37 U4: ALL 22 reruns finished and ALL 22 reproduce engineB's stored outputs IDENTICALLY (3,899,467 evaluations in total).
  Stored: 424,236 distinct J = 1 words over the 22 runs (per-run counts in section 1).  Certified + verified so far: 15 of 22 runs (all CERTIFIED_UNKNOT,
  two-checker re-check 100%, 0 failures), incl. e3_n24 (27,017); e3_n12_s112 (136,492) certified, verification running.
  Exact lp.J sample (200 per width-two run, 100 per width-three run, 3,400 words) running.
- 07:28 U4: 16 of 22 reruns finished (all E3b, E3c, E3d + the 3 test runs), EVERY ONE reproduces engineB's stored output
  IDENTICALLY (e3/compare.py).  Certified + two-checker-verified so far: e3b n24/n20/n16/n12, e3w3 n18 (and the test runs):
  all CERTIFIED_UNKNOT, 0 failures.  The 6 E3 (abs) main runs are still running (07:28).  No kcert-nontrivial J = 1 word,
  no alert, no HIT.
- 07:12 U4 so far: engineB's 3 test runs reproduced IDENTICALLY; their 9,743 distinct stored J = 1 words (10,158 probes)
  are 9,743/9,743 CERTIFIED_UNKNOT (tietze), both checkers 9,743/9,743; exact lp.J = 1 on 600/600 sampled words.
  The 19 main reruns are at ~3.5 CPU-min each (machine load ~38, ~35% CPU per process); a background pipeline
  (cert/pipeline.sh) extracts, certifies and two-checker-verifies each run as it finishes.
- 07:10 U5 DONE: engineA's Lemma W validation units regenerated EXACTLY (167 horizontal + 140 + 168 = 308 vertical,
  same seeds, same random stream, recovered from engineA's session transcript) and ALL CERTIFIED_UNKNOT; both checkers pass
  (section 2).  U4: 21 E3 reruns running (07:01/07:02 starts; budgets = original evaluation counts).
- 07:01 E3 reruns launched (21 runs, original seeds, original evaluation budgets).  U5 units: regenerating.
- 06:58 setup: certifier copied; E3 drivers patched (u45/e3/make_patched.py); reproduction test on engineB's test run
  e3_n12_s1 (seed 1, 44,156 evals, 25 restarts): evals, restarts, distinct a_2 = 0 J's (132), best_any, hits and every
  top_a2zero record IDENTICAL to engineB's stored JSON (the only difference: the later code adds an 'f' field).  So the
  annealing IS reproducible when the time budget is replaced by the original evaluation count.  That test run met 7,331
  J = 1 probes = 6,982 distinct J = 1 words, all discarded unstored by the original.

## 1. U4: engineB's guided searches E3 / E3b / E3c / E3d with every J = 1 word stored   [DONE 07:50]
METHOD.  u45/e3/make_patched.py builds e3_search.py (E3, and E3b with 'rel'), e3w3.py (E3c, width three via rho_3 = fastJ3)
and e3d_alex.py (E3d, the Delta = 1 class) from engineB's originals by exact string replacement (originals untouched;
`diff` shows only these patches): (1) outputs go to u45/e3/out; (2) the time budget is replaced by the ORIGINAL run's
evaluation count (and restart count where engineB logged it), same seed, wall cap 3,300 s; (3) EVERY J = 1 word met is
STORED with its probe count, first evaluation index, origin ('inner' = an annealing probe, the ones the originals ran kcert on
and discarded; 'init' = a random restart word with J = 1, which the originals skipped silently, without even kcert), and the
kcert verdict (computed once per distinct word).  The walk itself is untouched (J = 1 probes are rejected exactly as before),
so a rerun with the same seed and evaluation count re-traces the original trajectory: CHECKED by comparing every original
output field (evals, restarts, distinct a_2 = 0 J's, best_any, hits, all top-40 a_2 = 0 records with word, J, span, gates)
with engineB's stored JSON (e3/compare.py).
Budgets (engineB/out logs): E3 n = 12,16,20,24,30,40 seeds 112..140 (827,336 / 547,505 / 395,334 / 296,938 / 204,224 / 127,109
evals); E3b ('rel') n = 12..40 seeds 212..240 (283,218 / 178,677 / 126,109 / 89,046 / 63,595 / 36,399); E3d n = 20,30,40 seeds
420,430,440 (101,851 / 33,907 / 15,456); E3c n = 14,18,24,30 seeds 314..330 (222,650 / 141,675 / 82,530 / 54,055); plus
engineB's three short test runs (e3_n12_s1 44,156; e3b_n12_s7 17,534; e3w3_n14_s1 10,163).
Certification: every distinct stored J = 1 word of a run -> cert_words.py (u45/code, 3-7 processes, default budgets:
Tietze 30 s x up to 5 seeds, reps 30 s) -> cert/u4_<run>.jsonl.gz (every record with its full certificate); then
verify_sample.py at fraction 1.0 (replay.py AND a2lib, fresh process) -> cert/verify_u4_<run>.json.  Each cert file holds
exactly its run's word list (22/22 checked: no word missing, none twice).
RESULTS (e3/u4_table.json, e3/u4_sets.json, e3/u4_table.md).  REPRODUCTION 22/22 IDENTICAL.  So engineB's searches are
reproducible after all (CLAIMS B7 said 'not reproducible'): the original time budget only fixed WHEN the walk stopped, and
the logged evaluation count pins that point; the stored J = 1 words below are therefore exactly the J = 1 configurations
the original E3/E3b/E3c/E3d runs met and discarded (CHECKED by the identical outputs, not assumed).
PER SET:
| set | runs | evaluations | J = 1 probes | distinct J = 1 words | CERTIFIED_UNKNOT | other status | crossings | > 24 crossings | both checkers pass |
|---|---|---|---|---|---|---|---|---|---|
| E3 width two n = 12 (inside B1) | 2 | 871,492 | 149,718 | 143,474 | 143,474 | 0 | 15-24 | 0 | 143,474 |
| E3 width two n = 16..40 | 5 | 1,571,110 | 167,391 | 163,011 | 163,011 | 0 | 22-76 | 161,881 | 163,011 |
| E3b width two n = 12 (inside B1) | 2 | 300,752 | 24,552 | 23,615 | 23,615 | 0 | 14-24 | 0 | 23,615 |
| E3b width two n = 16..40 | 5 | 493,826 | 15,605 | 15,202 | 15,202 | 0 | 22-77 | 15,078 | 15,202 |
| E3c width three (rho_3) | 5 | 511,073 | 68,795 | 67,779 | 67,779 | 0 | 20-60 | 60,366 | 67,779 |
| E3d Delta = 1 class (width two, n = 20..40) | 3 | 151,214 | 11,482 | 11,155 | 11,155 | 0 | 29-76 | 11,155 | 11,155 |
| ALL (22 runs) | 22 | 3,899,467 | 437,543 | 424,236 (424,235 globally distinct) | 424,236 | 0 | 14-77 | 248,480 | 424,236 |

PER RUN ('inner' = annealing probe, discarded by the original after kcert; 'init' = J = 1 random restart word, skipped by
the original without kcert; 'evalf' = E3d, where both kinds go through evalf):
| run (set, n, seed) | evals (orig = rerun) | reproduction | J = 1 probes | distinct J = 1 words stored (inner / init) | kcert verdict | certifier | crossings (min-max; > 24) | both checkers |
|---|---|---|---|---|---|---|---|---|
| e3_n12_s1 | 44,156 | IDENTICAL | 7,331 | 6,982 (inner 6,977 / init 5) | V=1,Delta=1 6,982 | 6,982 CERTIFIED_UNKNOT (tietze) | 15-24; 0 | 6,982/6,982 |
| e3_n12_s112 | 827,336 | IDENTICAL | 142,387 | 136,492 (inner 136,385 / init 107) | V=1,Delta=1 136,492 | 136,492 CERTIFIED_UNKNOT (tietze) | 15-24; 0 | 136,492/136,492 |
| e3_n16_s116 | 547,505 | IDENTICAL | 74,071 | 71,792 (inner 71,766 / init 26) | V=1,Delta=1 71,792 | 71,792 CERTIFIED_UNKNOT (tietze) | 22-32; 70,662 | 71,792/71,792 |
| e3_n20_s120 | 395,334 | IDENTICAL | 43,584 | 42,517 (inner 42,501 / init 16) | V=1,Delta=1 42,517 | 42,517 CERTIFIED_UNKNOT (tietze) | 27-40; 42,517 | 42,517/42,517 |
| e3_n24_s124 | 296,938 | IDENTICAL | 27,651 | 27,017 (inner 27,014 / init 3) | V=1,Delta=1 27,017 | 27,017 CERTIFIED_UNKNOT (tietze) | 34-48; 27,017 | 27,017/27,017 |
| e3_n30_s130 | 204,224 | IDENTICAL | 15,210 | 14,910 (inner 14,909 / init 1) | V=1,Delta=1 14,910 | 14,910 CERTIFIED_UNKNOT (tietze) | 45-60; 14,910 | 14,910/14,910 |
| e3_n40_s140 | 127,109 | IDENTICAL | 6,875 | 6,775 (inner 6,775) | V=1,Delta=1 6,775 | 6,775 CERTIFIED_UNKNOT (tietze) | 61-76; 6,775 | 6,775/6,775 |
| e3b_n12_s7 | 17,534 | IDENTICAL | 1,282 | 1,241 (inner 1,239 / init 2) | V=1,Delta=1 1,241 | 1,241 CERTIFIED_UNKNOT (tietze) | 14-24; 0 | 1,241/1,241 |
| e3b_n12_s212 | 283,218 | IDENTICAL | 23,270 | 22,374 (inner 22,330 / init 44) | V=1,Delta=1 22,374 | 22,374 CERTIFIED_UNKNOT (tietze) | 16-24; 0 | 22,374/22,374 |
| e3b_n16_s216 | 178,677 | IDENTICAL | 8,068 | 7,832 (inner 7,821 / init 11) | V=1,Delta=1 7,832 | 7,832 CERTIFIED_UNKNOT (tietze) | 22-32; 7,708 | 7,832/7,832 |
| e3b_n20_s220 | 126,109 | IDENTICAL | 4,394 | 4,298 (inner 4,297 / init 1) | V=1,Delta=1 4,298 | 4,298 CERTIFIED_UNKNOT (tietze) | 29-40; 4,298 | 4,298/4,298 |
| e3b_n24_s224 | 89,046 | IDENTICAL | 1,962 | 1,917 (inner 1,915 / init 2) | V=1,Delta=1 1,917 | 1,917 CERTIFIED_UNKNOT (tietze) | 35-47; 1,917 | 1,917/1,917 |
| e3b_n30_s230 | 63,595 | IDENTICAL | 902 | 883 (inner 883) | V=1,Delta=1 883 | 883 CERTIFIED_UNKNOT (tietze) | 46-59; 883 | 883/883 |
| e3b_n40_s240 | 36,399 | IDENTICAL | 279 | 272 (inner 272) | V=1,Delta=1 272 | 272 CERTIFIED_UNKNOT (tietze) | 65-77; 272 | 272/272 |
| e3w3_n14_s1 | 10,163 | IDENTICAL | 1,545 | 1,520 (inner 1,518 / init 2) | V=1,Delta=1 1,520 | 1,520 CERTIFIED_UNKNOT (tietze) | 21-28; 1,275 | 1,520/1,520 |
| e3w3_n14_s314 | 222,650 | IDENTICAL | 35,654 | 35,070 (inner 35,022 / init 48) | V=1,Delta=1 35,070 | 35,070 CERTIFIED_UNKNOT (tietze) | 20-28; 27,902 | 35,070/35,070 |
| e3w3_n18_s318 | 141,675 | IDENTICAL | 18,912 | 18,648 (inner 18,629 / init 19) | V=1,Delta=1 18,648 | 18,648 CERTIFIED_UNKNOT (tietze) | 26-36; 18,648 | 18,648/18,648 |
| e3w3_n24_s324 | 82,530 | IDENTICAL | 8,356 | 8,259 (inner 8,259) | V=1,Delta=1 8,259 | 8,259 CERTIFIED_UNKNOT (tietze) | 37-48; 8,259 | 8,259/8,259 |
| e3w3_n30_s330 | 54,055 | IDENTICAL | 4,328 | 4,282 (inner 4,279 / init 3) | V=1,Delta=1 4,282 | 4,282 CERTIFIED_UNKNOT (tietze) | 48-60; 4,282 | 4,282/4,282 |
| e3d_n20_s420 | 101,851 | IDENTICAL | 8,935 | 8,665 (evalf 8,665) | V=1,Delta=1 8,665 | 8,665 CERTIFIED_UNKNOT (tietze) | 29-40; 8,665 | 8,665/8,665 |
| e3d_n30_s430 | 33,907 | IDENTICAL | 1,874 | 1,830 (evalf 1,830) | V=1,Delta=1 1,830 | 1,830 CERTIFIED_UNKNOT (tietze) | 44-58; 1,830 | 1,830/1,830 |
| e3d_n40_s440 | 15,456 | IDENTICAL | 673 | 660 (evalf 660) | V=1,Delta=1 660 | 660 CERTIFIED_UNKNOT (tietze) | 61-76; 660 | 660/660 |

FINDINGS.
 * Every J = 1 configuration met by the guided searches is a CERTIFIED unknot (Dehn, replayed Tietze certificate on the
   original diagram), re-checked by two independent checkers.  CHECKED(424,236).  kcert had said 'V = 1, Delta = 1' on all
   of them (agreement, now certified).  V_K = 1 by both brackets on all 424,236.
 * Sanity: exact lp.J (mont/lp.py, independent of rho_2 / rho_3) = 1 on 4,000/4,000 random stored words (600 from the test
   runs, 200 per width-two run, 100 per width-three run): the stored words really are J = 1 configurations.  CHECKED(4,000).
 * The J = 1 probe rate falls with word length (E3: 17% of evaluations at n = 12, 5% at n = 40; E3b: 8% -> 0.8%), i.e. the
   annealer keeps stepping onto long presentations of the unknot next to its low-span targets, consistent with engineB's
   own tropical analysis (span against word length is presentation redundancy).  No J = 1 configuration of these searches
   is a candidate for anything.
 * Scope: this certifies the configurations the searches VISITED (B7 is not a region claim).  Width-two n <= 14 is in any
   case inside the CERTIFIED region B1; n = 16..40, width three and the Delta = 1 class have no region claim and need none.

## 2. U5: engineA's Lemma W validation units (167 + 308)   [DONE 07:10; u45/u5/, u45/cert/u5_*]
SOURCE.  engineA's REPORT (sec. 2) names eng.py (Lemma W candidate sets) and validate.py (calculus vs lp.J); the Lemma W
brute-force check itself was run INLINE (python -c) and never saved.  Its exact code was recovered from engineA's session
transcript (tool calls at 00:27:28 CST and 00:33:44 CST): seed 5: 80 horizontal trials (products of k in {1,1,2} random rational
words of length 1..5; brute force N in [-14,14], mu in [-30,30] minus 0; units on the 'scalar' N of eng.hclosures excluded),
then in the SAME random stream 50 vertical trials (length 0..5, odd a in [-31,31], N in [-14,14]); seed 11: 60 vertical trials.
engineA's printed results then: 'horizontal 80/80, 167 units', 'vertical 50/50, 140 units', 'vertical 60/60, 168 units'.
REGENERATION (u5/lemmaw_units.py; engineA's vc.py and eng.py imported read-only; the procedure copied statement by
statement): horizontal 80/80 complete, 167 units; vertical seed 5 50/50, 140 units; seed 11 60/60, 168 units.  IDENTICAL
counts, so the same units (CHECKED: deterministic stream).  Every unit is recovered by eng.hclosures / eng.vclosures (Lemma W
completeness re-confirmed, 475/475).  Knot of each unit built with engineA's own dictionary (units.py unit_word):
H (mu, N, T): s.r2.(y1)^(-mu).B(w_1)...B(w_k).(y0 or x0)^|N|.u1;  V (a, N, T): s.l1.B(w_1)...B(w_k).(y0/x0)^|N|.(x2 or y2)^|a|.u1.
| set | units | distinct halfwords | J = 1 by calculus | exact lp.J = 1 | certifier | both checkers (fresh process) |
|---|---|---|---|---|---|---|
| H (horizontal, seed 5) | 167 | 147 | 167/167 | (all 335 words) | | |
| V (vertical, seeds 5 + 11) | 140 + 168 = 308 | 94 + 94 | 308/308 | | | |
| all U5 units | 475 | 335 | 475/475 | 335/335 | 335/335 CERTIFIED_UNKNOT (tietze), 2-21 crossings | 335/335 (replay.py AND a2lib) |
| bonus: 'scalar' horizontal units (N with A = B_N: J constant in mu; excluded from engineA's 167) | 2,460 | 2,040 | 2,460/2,460 | 2,040/2,040 | 2,040/2,040 CERTIFIED_UNKNOT (tietze), 4-72 crossings | 2,040/2,040 |
All U5 knots have V_K = 1 by both brackets (PD and project).  0 UNRESOLVED, 0 NONTRIVIAL, no HIT.  CHECKED(475 units +
2,460 scalar units).  So CLAIMS row A3 ('UNJUSTIFIED under the standard (not stored)') is now CERTIFIED: every Lemma W
validation unit is a certified unknot; the sentence in engineA's REPORT can stand.
Files: u5/lemmaw_units.py, u5/units.json (every unit: trial, words, mu or a, N, halfword, calculus J, recovery flag),
u5/words_u5_units.json, u5/words_u5_scalar.json, u5/jcheck.py + jcheck_units.json + jcheck_scalar.json, cert/u5_units.jsonl.gz,
cert/u5_scalar.jsonl.gz (full certificates), cert/verify_u5_units.json, cert/verify_u5_scalar.json.

## 3. Effect on CLAIMS.md (proposed rows; CLAIMS.md itself is not edited by this lane)
| # | claim | status before | status now | basis |
|---|---|---|---|---|
| A3 | engineA sec. 2: Lemma W brute-force validation, 167 horizontal + 308 vertical units | UNJUSTIFIED (not stored) | CERTIFIED (475/475 units; 335 distinct knots) | section 2: exact regeneration (same seeds and stream, identical counts), every unit's knot CERTIFIED_UNKNOT (tietze), both checkers 335/335; exact lp.J = 1 335/335; Lemma W candidate sets recover 475/475 |
| B7 | engineB 3: guided searches E3/E3b/E3c/E3d 'HITS 0' | NCH (J = 1 configurations discarded unstored; annealing 'not reproducible') | CERTIFIED for every configuration the searches met (not a region claim) | section 1: 22/22 runs reproduced IDENTICALLY with the original seeds and evaluation counts; all 424,236 stored J = 1 words (width two n = 12..40, width three, Delta = 1 class) CERTIFIED_UNKNOT (tietze), both checkers 424,236/424,236; exact lp.J = 1 on 4,000/4,000 sampled |

## 4. Incidents and notes
 * 07:01 the 8 E3c/E3d processes stopped at import: fastJ / fastJ3 insert engineB/ at sys.path[0], so 'import e3_search'
   resolved to engineB's ORIGINAL (caught by the assertion added for exactly this); import order fixed, relaunched 07:02.
   Nothing had been written; no effect on any result.
 * 07:28 compare.py once read the E3 outputs while they were still being written (JSON decode error, harmless);
   u4_words.py now waits for a complete JSON.  Every pipeline extraction had parsed a complete file (it logs the run's
   evaluation count, which a truncated JSON cannot produce), and each cert file matches its word list exactly (22/22).
 * 07:29 the first pipeline (cert/pipeline.sh) was replaced by a lock-aware one (cert/pipeline2.sh, two instances); the old
   shell (killed by its PID, never by name) had already launched cert_words.py for e3_n24_s124; that process finished
   normally (27,017/27,017), the run was locked against double processing and verified by cert/finish_e3_n24.sh.
 * Load: the 22 reruns ran as 21 + 8 parallel processes for ~27 min (machine load 35-60), then up to 8-15 certification
   processes for ~20 min.  All processes of this lane have exited.
 * engineA's Lemma W validation script was never a file; its code was taken verbatim from engineA's session transcript.

## 5. Files (all under u45/)
 code/          COPY of cert/run/code (9 sys.path strings re-pointed; nothing else changed)
 e3/            make_patched.py (builds the patched drivers), e3_search.py, e3w3.py, e3d_alex.py (patched), run_e3_all.sh,
                run_e3_w3d.sh (the queues run), patch.diff (originals vs patched), compare.py (reproduction check),
                u4_words.py, aggregate.py (-> u4_table.json, u4_sets.json, u4_table.md),
                out/<run>.json (full original output fields + 'j1_words': every stored J = 1 word with count/origin/kcert)
 u5/            lemmaw_units.py, units.json, words_u5_*.json, jcheck.py, jcheck_units.json
 cert/          words_<run>.json, u4_<run>.jsonl.gz and u5_*.jsonl.gz (every record with full certificates), verify_*.json
                (fresh-process two-checker re-checks), jsample_* / jcheck_* (exact lp.J samples), pipeline.sh, pipeline2.sh,
                finish_e3_n24.sh, run_cert.sh
 code_vs_certrun.diff   `diff -r cert/run/code u45/code` (the 9 re-pointed sys.path lines)
 logs/          every run / certification / pipeline log
