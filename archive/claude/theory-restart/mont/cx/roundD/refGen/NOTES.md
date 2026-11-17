# refGen referee notes (round D) — referee of C1 finite jet automaton + Farkas certificate generator
Started 2026-11-17. Claude (refGen). Marks: PROVED / CHECKED(n) / CONJECTURE / GAP / FALSE.
## Log
- read BRIEF.md, engineC1/REPORT.md
- read engineA, notie REPORTs; read C1 code jauto.py, v3lemmas.py, taulaw.py, v3b.py, v3b3.py, h3b.py, gen2.py, gen2_run.py
- gen2_res.pkl stores per-SIGNATURE verdicts (resV, resH), sigs, tags, trees -- NOT the certificates. So "re-verify 200
  certificates" = regenerate a witness y (with C1's search, copied) AND verify it with my own code (own B-data, own case
  equations, own automaton longest path); plus an independent search with my own code.
## Plan
 Q1 own automaton (own precision-tracked arithmetic), compare state/transition sets with jauto at K=2,3,4; exact test on all
    normal forms of size k+sum|m_i| <= 12 (top AND bottom computed directly at t=0); prove clipping lemma; verify R0, R2 identities.
 Q2 tau-law: own product automaton (u, u'') + exact check on size<=12 boxes.
 Q3 certificate logic: write reconstruction; check w-data/sigma*/delta* for all odd |a|<=41, |mu|<=40; identity check of the
    case formulas against exact closures.
 Q4 200 random per-box certs + 50 pair certs, own code; negative controls (theirs + planted B = rational unit box, n_min=0).
 Q5 2000 random closures from certified boxes via lp.J at Lemma-W N's.
## Q1 automaton (results so far)
- rg_core.py: own exact Laurent arithmetic + own precision-tracked series TS (lo = lowest known degree; mul precision
  max(lo_f + T_g, lo_g + T_f) with T = known top or lo-1) + own automaton build. rg_q1_auto.log:
  K=2: 9 states/89 transitions, K=3: 19/227, K=4: 35/489; state sets AND every transition (D-jet, next key) IDENTICAL to
  jauto. State degrees of r: {-1} u {-4..-3-K} u {init, tiny}  (hypothesis of the clipping lemma holds).
  Clipping: outputs for |m| = M..M+8 identical from every state (CHECKED); general proof written in REPORT (PROVED).
## Q2 tau-law
- rg_q2_tau.log: own product automaton (u, u''), K=3: 28 reachable product states, K=4: 54; ALL give
  (delta, lc_t lc_b, sigma, tau) = (-1,-1,0,-1). Direct exact check (no automaton, no R2): all 65,535 normal forms of
  size k+sum|m_i| <= 17: all (-1,-1,0,-1). => PROVED (computer-assisted finite automaton; inputs R0, R2, clipping lemma).
  By-product: l3_top+l3_bot of q is NOT constant (values 0 (52 states), 1 (2 states)) -> no 4th-order law of this form.
- rg_q1_exact_L12.log (284 s): ALL 531,440 reduced words of length <= 12 in X,x,Y,y with leftmost X/x (= every rational
  tangle with <= 12 crossings, before dedup; 517,004 non-integral, normal forms up to k = 11, |m| up to 11):
  own R0 rewriting (X = Y E, x = t^-4 E Y^-1, E^2 = t^4, E e1 = Y^-1 e1) EXACT on every word (v(word) = +-t^j Y^n u(nf));
  automaton K=3 and K=4 predictions (log-jets of a, b, q to order K, deg q, lc q) = exact data at BOTH ends
  (bottom computed directly at t=0, automaton run on the mirror u''): 0 mismatches.  CHECKED(517,004 x 2 ends x 2 K).
## Q3/Q4 generator re-implementation
- rg_gen.py: OWN derivation of the weak-end cases (offset >=3, 2, 1, 0(e=+1), 0(e=-1,r=1), -1, -2, <=-3; e = +-1),
  own w-data, own exact longest-path sup on own K=3 automaton (19 states, 89 dedup edges; Bellman-Ford + extra relaxation
  pass = positive-cycle test), own grid of multiplier directions (21 values incl. thirds), finer vertical classes
  (a=3, a=-3 pinned n; a>=5, a<=-5 with n >= delta(B)+6).  Case equations coincide with C1's v3b.cases/h3b.cases_pq
  (derived independently; the r=1 row: Lam + mB*alpha = mB + M1 - M2 - mB*K1 - mB^2/2 == C1's with kap = -mB).
- rg_gen_sanity.log: B empty: Q-MONT (n>=2, every mu) all closed; V3 (n>=1, every odd |a|>=3) all closed;
  NEGATIVE CONTROL (n>=1 horizontal): open exactly mu=+-1 off=-2 e=+1, mu=+-2 off=0 r=1, |mu|>=3 two-ended at n=1
  == C1's reported control.
- rg_q3_wdata.log: vertical classes stable |a|<=41, bottom(a) = top(-a), delta*_V = -|a|-1, sigma*_V = -1,
  wV(+-1) = t^(+-3) w_3(+-1); horizontal classes stable |mu|<=40, sigma* = -2,1,0,0 (|mu|=1,2,3,>=4), delta* = -3,-1,-1,-1;
  C1's v3b.wdata and h3b.WJ agree.  No problems.
- rg_r0r2.log (sympy): E = Y^-1 X, E^2 = t^4, E e1 = Y^-1 e1, X = Y E, X^-1 = t^-4 E Y^-1 (=> R0 normal form, PROVED);
  bar Y = D Y^-1 D^-1, bar X = D X^-1 D^-1, bar E = t^-4 D Y E Y^-1 D^-1, channel identities (=> R2, PROVED).
### Reconstruction of the automaton argument (Q1)
 r = v2/v1; Y^m acts as a Moebius map on r, E: r -> -(1+r)/D, a -> aD, D = 1 + (1-t^4) r_pre; so a(u) = prod D_i,
 q = 1 + (1-t^3) r_final.  KEY_K(r) = init (r=0) | tiny (ord r <= -4-K) | (deg r, relative K-jet).
 (i) DETERMINACY: precision-tracked series arithmetic (sum: lo = max; product: lo = max(lo_f + T_g, lo_g + T_f), T = known
     top or lo-1; inverse: relative precision preserved) is the standard error-propagation bound; computing a step on the
     whole class 'series with this key' and asserting the outputs are known to relative order K proves key -> (D-jet, key')
     is a function of the key.  ('tiny' is represented as 'zero to precision -3-K', a superset of the class: fine.)
 (ii) CLIPPING LEMMA (PROVED here, general m): every reachable key has deg r = -1 or <= -4 (or init/tiny).  m = p >= M:
     r_pre = t^-3(1 + u^3 + ... + u^(3p-3)) + t^(-3p) r; the last term sits at relative order >= 3p-2 > K, the geometric
     terms beyond order K are irrelevant, so jet_K(r_pre), jet_K(D) (lead -t^4 r_pre; '+1' at rel. order 1, 'r_pre' at 4)
     and jet_K(r') (r' = -(1+r_pre)/D, 1+r_pre = 1 + t^-3 + ..) are independent of p once 3p-2 > K+1.
     m = -p, p >= M: r_pre = t^(3p) r - (1 + t^3 + .. + t^(3p-3)).  deg r = -1: lead t^(3p-1), geometric terms at relative
     orders 2,5,8,..,3p-1; deg r <= -4: lead -t^(3p-3), t^(3p) r at relative order -3-deg r >= 1; init: geometric only.
     In all cases D = -t^4 r_pre + r_pre + 1 (the '1' at relative order >= 3p+1 > K) and 1 + r_pre (the constant cancels
     in the R case, leaving relative orders up to 3p-4 > K) have p-independent K-jets for p >= K+3, and deg r' = -4.
     So exponents can be clipped to [-M, M], M = K+3 (C1's M).  The empirical m = M..M+8 agreement is consistent.
 (iii) FINITENESS: closure of {init} under the clipped transitions terminates (9/19/35 states, two codes agree).
 (iv) R0: every rational box = unit * Y^n u(m), m in normal form (rewriting proof above, CHECKED exact on 517,004 words).
 => The top K-jets of a, b, q of EVERY non-integral rational box are read off a walk in the automaton, and every walk
    is realised by a box (take the clipped exponents).  sup over all boxes of a linear functional of
    (rho_a, l2(a), rho_q, l2(q)) = longest walk (Bellman-Ford; +inf iff a positive cycle is reachable).
    Bottom data = top data of the mirror u'' (R2), an involution on normal forms, so the SET of bottom data = SET of top data.
 VERDICT Q1: PROVED (computer-assisted finite computation, reproduced by an independent implementation) -- not merely
 checked on 79,422 boxes; the 79,422 + my 517,004 x 2 ends are validations.
- rg_q5_ident.log: 40,000 exact closures (C1 'BOTH' box B + 1..3 random rational boxes from words of length 2..5,
  H with mu in [-6,6]\0 or V with a in {+-1,+-3,+-5,+-7}; N at a Lemma-W degree tie when one exists: 21,752 forced):
  sigma-law (X2-X1)_top + (X2-X1)_bot = m_B = sigma(B) - sigma*: 40,000/40,000; generator's offset formulas for the
  normalised (x1,x2) of F = S1+S2: 76,000/76,000 ends; units 0.  CHECKED(40,000).
- rg_spana.log: precondition of the n = 0 pair claim (horizontal mu = +-1 needs span A >= 5 so that Tot = span A - 2 >= 3
  and some end has r >= 2): span a(B) >= 10 for all 27,585 boxes of the top-300 classes (>= 4 over all 48,683 eligible).
  OK (C1 asserted 'every non-rational library box has span a >= 4'; true).
## Negative controls (Q4)
- C1's control reproduced by MY generator (rg_gen_sanity.log): rational only, n >= 1, horizontal: open exactly
  mu=+-1 (off=-2,e=+1), mu=+-2 (off=0,r=1), |mu|>=3 (two-ended at n=1) -- identical to C1's report.
- PLANTED control (rg_negctl.log): exhaustive search of single-rational-box closures (normal forms of size <= 10,
  |mu| <= 8, a in {+-1,..,+-7}, N at Lemma-W ties): 133 genuine units (two-bridge unknots): H mu=+-1:17+17, +-2:14+14,
  +-3:10+10, +-4:6+6, +-5:2+2, -6:1; V only at a=+-1 (17+17) -- none at |a|>=3 (consistent with C1).
  Feeding each unit box u0 to the generators as 'B' with n_min = 0: ours and C1's gen2 leave the unit's class OPEN in
  99/99 cases (V a=+-1 skipped = H mu=+-1).  At the 62 units with exactly one strong end (r>=2), the unit satisfies the
  equations of its OWN weak-end case with zero rational sums (incl. the pin P = P0): the case equations are tight, i.e.
  the generator cannot certify a true unit.  37 units have both ends strong (m_B = 0; |mu|>=3) -> flagged open.
## Q3 certificate logic -- reconstruction (my derivation; rg_gen.cases)
 F = S1 + S2, S1 = w1 A, S2 = w2 t^-3N B; J unit <=> F = c t^e Phi_3.
 1 Lemma W: span S_i >= 3 => some end coincides in degree.
 2 Strong end: Tot := span S1 - 2 >= 3 for n >= 1 (span a_B >= 1 filter, span a(u) >= 4, span w_1 >= 0) and for the n = 0
   pair claim (span a >= 10 on the top-300 classes).  One coincident end only: r >= Tot; both: r_top + r_bot = Tot.
 3 Sigma-law: -S2/S1 = Q/q*, so X2 - X1 = s1(Q) - s1(q*) at each end; summed over ends = sigma(B) - sigma* = m_B
   (Lemma S).  m_B != 0 => exactly one strong end (r >= 2), weak end r <= 1 with mismatch m_B, i.e. P = P0 = m_B + K1 - K2.
   m_B = 0 => two-ended tie possible only if both ends coincide (pinned n) -> open.
 4 Weak end (off = deg S1 - deg S2 toward the expansion, e = lc S2/lc S1 = +-1): normalised (x1,x2) of F per offset;
   (1,1) required -> linear equations in (alpha, P, La, Lam) since X1, X2 are pinned.  Offsets exhaustive.  Rows equal C1's.
 5 Delta-law: off = 0 at the weak end => both ends coincide => n = delta(B) - delta* (H), delta(B) + |a| + 1 (V).
 6 Farkas: y.r = sum_i g.v(u_i) <= n s, s = sup over ALL rational boxes (longest walk). n free: s <= 0 & y.r > n_min s
   kills every n >= n_min (unbounded n OK); n pinned: y.r > n s.  Bottom weak end: same sup (R2 involution).  PROVED.
 7 Classes: (w_1, wV) order-2 jets constant on a=3, a=-3, a>=5, a<=-5 (top a>=3 == bottom a<=-3); (w_1, w_3) constant
   for mu>=4 / mu<=-4 (variable terms at relative order >= |mu|+1 >= 5); a = +-1 == horizontal mu = +-1.  PROVED + CHECKED.
 Remarks: (a) case off=0,e=+1 is vacuous for units (|lc F| = 2|lc S1| >= 2); certificates there redundant.
          (b) C1 merges a>=3 into one class with n >= delta(B)+4 at ties; finer classes equally valid.
          (c) certificates NOT archived (gen2_res.pkl = verdicts only); deterministic, re-runnable.
          (d) inherited: Theorem N (PROVED), Theorem V (PROVED modulo skein dictionary), Theorem O / halfword dictionary.
 VERDICT Q3: SOUND.
- rg_lemmas.log (MY automaton): BX3 Psi non-increasing on all 227 edges; max rho_a: R0 -1, R1 -1, S0 0, S1/S2/S3+ -1;
  q-data (deg, lc, rho_q, lambda_q): R1 (2,-1,1,-1/2), R0 (2,-1,0,-1)|(2,-1,0,-2), S0 (0,1,-1,-1/2), S1 (0,1,0,1),
  S2/S3+ (0,1,0,0); T2 max(lambda_q + rho_a): R0 -2, R1 -3/2, S0 -1/2, S1 0, S2 -1, S3+ -1; BX4': Psi-preserving walks
  ending in R1 have l2(b) <= -1.  ALL as in C1's REPORT section 1 (these are finite automaton facts => PROVED).
- Q5 lp.J run redesigned for load (machine load avg ~98 from other agents): 1,000 V closures from ALL certified boxes,
  1,000 H closures from certified boxes of nesting depth <= 3 (H costs ~8x V), 1-2 light rational companions, N forced at a
  Lemma-W tie when possible.  Progress saved in rg_q5_lpJ.pkl every 50.
- spot: my generator on 6 C1 signatures: identical verdicts incl. an identical OPEN set on a partly-open signature
  (mu=+-1 bot off=-2 e=+1; mu=+-2 two-ended n=2; mu=3, mu>=4 bot off=0 r=1).  Launched rg_allsig.py (ALL 5,157 signatures,
  48,683 boxes: signatures recomputed with my end-data code from vc.vec, then my generator on every signature).
- rg_allsig.log (part 1): signatures of ALL 48,683 eligible boxes recomputed with MY end-data code (from vc.vec): 48,683/48,683
  equal C1's keys (B-data both ends, sigma, delta) and are lc-admissible with span a >= 1.  Generator part running.
- Q5 progress: 100 closures, 0 units, 0 lp.J/vector-calculus disagreements.
## FULL independent re-derivation of the per-box theorem (rg_allsig.log, 110 s)
- MY generator on ALL 5,157 signatures (48,683 boxes), n_min = 1:
  V: (C1 yes, mine yes) 4,678; (no, no) 478; (C1 no, mine YES) 1 [finer a-classes]; (C1 yes, mine no) 0.
  H: (yes, yes) 4,798; (no, no) 359; no disagreement.
  BOTH: 4,400 signatures = 46,771 boxes proved by BOTH generators; 757 signatures = 1,912 boxes open in both.
  => every per-box claim of C1 (V3(B), H(B), BOTH) is independently re-proved (given the exact B vectors).
- C1's own gen2 negative control (rg_c1_negctl.log): open exactly mu=+-1 d=-2 e=1, mu=+-2 d=0 r=1, |mu|>=3 two-ended n=1;
  Q-MONT (n>=2) all closed; V3 (n>=1) proved.  Identical to my generator.
- rg_negctl_cases.log: the genuine n=1 units live EXACTLY in those open cases: mu=+-1 weak end off=-2 e=+1 (17+17),
  mu=+-2 weak end off=0 e=-1 r=1 (14+14), |mu|>=3 both ends r>=2 (37).  The negative control is tight, not merely passed.
## Q4 pairs (rg_q4_pairs.log)
- 50 random signature pairs from the top-300 classes (seed 20261118), n_min = 1 AND n_min = 0: my generator proves EVERY
  closure class (V a=3,-3,>=5,<=-5; H all 8 mu-classes) in 50/50 + 50/50.  C1's witnesses regenerated with C1's own search
  (gen2/v3b3 imported read-only): 28,000 witnesses, 28,000 pass MY exact re-check (my rows, my n-rule, my longest-path sup),
  0 failures; C1's case rows == my rows in every case; C1 found a witness in every case.
## VERDICTS (interim, 04:2x; Q4-boxes and Q5 numbers pending)
 Q1 automaton -> every rational box: PROVED (computer-assisted).  C1's clipping step was CHECKED only (m = M..M+2) with a
    one-line sketch ("argument in jauto.py" is not actually there): GAP in C1's write-up, CLOSED here by a general proof.
 Q2 tau-law: PROVED (product automaton, reproduced: 28 states K=3, 54 K=4; exact 65,535 normal forms).
 Q3 certificate logic: SOUND for every n >= n_min (sup <= 0), ties (delta-law pin), all offsets, every mu (stable classes),
    every odd a (classes; a = +-1 = H mu = +-1).  Inherited: Theorem N; Theorem V (vertical; PROVED modulo skein dictionary).
 Q4 per-box: all 46,771 BOTH boxes independently re-proved by my generator (rg_allsig); pairs 50/50 at n_min 1 and 0,
    28,000 C1 witnesses pass my exact check; negative controls tight.
 Q5: running (150 closures so far: 0 units, 0 disagreements lp.J vs vector calculus).
- rg_q4_pairs1000.log (seed 777): 1,000 further random signature pairs (top-300), n_min = 1 and 0: my generator proves
  all classes in 1,000/1,000 + 1,000/1,000; 560,224 regenerated C1 witnesses, 560,224 pass my exact re-check, rows identical.
## INCIDENT 04:33 (other lane's pkill of multiprocessing workers) and recovery
- ALL pool workers of my three pool runs were killed at 04:33:43-44 and respawned by Pool: rg_q4_boxes.py (pid 89117,
  200-box run, at 160/200; results only in memory -> would hang forever, unsalvageable), rg_q5_closures.py lpJ2 (90006),
  rg_q5_second.py (92391).  Each killed worker held one task -> lost tasks -> imap would hang.
- Unaffected (finished before 04:33, or no pool): rg_q1_exact L12 (Pool.map returned; 531,440 = 3^12 - 1 words = the full
  expected count), rg_q2_tau, rg_q5_ident (Pool.map returned 40,000 = 16 x 2,500), rg_allsig (finished ~04:16; comparison
  loop would KeyError on a missing signature), pairs 50 / 1000 (single process), negctl, lemmas, wdata, r0r2, spana.
- 04:37: killed ONLY my own PIDs (3 parents + their children, listed by ppid): 89117 89119 92802 92805 92806 92809 92813
  90006 90008 92798 92800 92801 92803 92807 92391 92393 92763 92766 92781 92787.  Stopped my watcher shell.
- Saved before the kill: rg_q5_lpJ.pkl 550 results (seeds 70000..70556, 550 distinct), rg_q5_lpJ_b.pkl 100 results
  (seeds 71894..71999, 100 distinct); 0 units, 0 disagreements.  These are complete, deterministic per-seed results.
- Recovery: rg_robust.py = ProcessPoolExecutor (a dead worker raises BrokenProcessPool instead of hanging -> restart on
  the remaining tasks) + one atomic result file per task in rg_results/ + resume skipping tasks that have a file.
  Task list: 200 'q4vec' (lp.J vector check of the SAME 200 boxes, seed 20261117) + 2,000 'q5' seeds 70000..71999.
  The 650 saved q5 results imported as files (source tagged).  The cheap per-box certificate part runs single-process
  (rg_q4_cert.py, kind 'q4cert', resumable).  ALL COUNTS BELOW ARE TAKEN FROM rg_results/ FILES, keyed by task, so lost
  tasks cannot be counted.
## Q4 per-box certificates -- FINAL (rg_q4_cert.log; from rg_results/q4cert_*.pkl, 200/200 present)
- Same 200 random boxes (seed 20261117) of the 46,771 'BOTH' boxes (NRR 121, NGR 76, NG 3; min span a 13):
  own B-data (from the exact vector) == C1 signature key, lc-admissible: 200/200; MY generator proves every closure class
  (V every odd |a| >= 3, H every mu): 200/200; C1's witnesses regenerated with C1's own search: 56,124, ALL pass my exact
  re-check (0 failures), C1 rows == my rows, C1 found a witness in every case.  CHECKED(200 boxes / 56,124 certificates).
- Extension running: rg_sigcert.py = same check for ALL 4,400 BOTH signatures (single process, resumable).
- lp.J vector check of the 200 boxes (kind q4vec) is in the robust pool.
- Q5 interim (04:40, machine load avg ~250): batch a 550 + batch b 100 closures: 0 units, 0 disagreements lp.J vs vector
  calculus.  Second batch rg_q5_second.py runs seeds 71999 downward (same seed -> same closure); combine with rg_q5_combine.py.
- 04:45 INCIDENT: all my background runs were SIGKILLed (exit 137; load avg ~250, ~1.5 GB free: memory-pressure kills).
  Q5 partial results survive (incremental saves: 650 distinct closures, 0 units, 650/650 lp.J == vector calculus).
  Q4 200-box run lost its in-memory results at 160/200 (no incremental save).  The generator part of Q4 is anyway fully
  covered by rg_allsig (all 46,771 boxes).  Restarting Q4 split into (b) fast per-box C1-witness re-check and
  (c) lp.J_raw vector check, both with incremental saves.
- rg_q4b_wit.log (200 random BOTH boxes, seed 20261117, incremental): own signature (from vc.vec) == C1 key 200/200; my
  generator proves EVERY closure class 200/200; C1 witnesses regenerated 56,124 -> 56,124 pass my exact re-check, 0 fail;
  C1 rows == my rows everywhere; C1 had a witness for every case.
- rg_q4b_vec.log: independent box vector from two RAW lp.J closures (BRIEF sec. 4 formula) == vc.vec up to a unit for
  200/200 of the sampled boxes (NRR 121, NGR 76, NG 3).  So the B-data feeding the certificates are confirmed from the
  actual knot diagrams for the sample.
- rg_q5_final.log: 2,000 distinct closures (1,000 H with mu in [-6,6]\0 from certified boxes of nesting depth <= 3;
  1,000 V with a in {+-1,+-3,+-5,+-7} from all certified boxes; 1-2 rational companions; N at a Lemma-W degree tie in
  ALL 2,000): exact lp.J units 0, J None 0, lp.J == vector-calculus J 2,000/2,000, min span J 13.  CHECKED(2,000).

## FINAL VERDICTS (05:15)
 1 Q1 automaton yields the top K-jets of a, b, q of EVERY non-integral rational box: SOUND = PROVED (computer-assisted).
   C1's write-up had a small GAP (clipping only CHECKED at m = M..M+2, 'argument in jauto.py' absent) -> CLOSED here.
   Independent reimplementation identical; exact check 517,004 boxes (all <= 12-crossing words) x both ends x K=3,4.
 2 Q2 tau-law: SOUND = PROVED (product automaton 28/54 states; exact 65,535 normal forms).  No 4th-order law.
 3 Q3 certificate logic: SOUND for every n (sup<=0), ties (delta-law pin), offsets (exhaustive), every mu, every odd a.
   Inherited: Theorem N (H), Theorem V (V; PROVED modulo skein dictionary), Theorem O / vector calculus.
 4 automaton lemmas (BX3, q-data, max rho_a, T2, BX4'): SOUND (identical on my automaton).
 5 per-box V3(B)/H(B)/BOTH (46,771 boxes): SOUND -- all 5,157 signatures re-run with my generator: every C1 proof
   reproduced (0 disagreements; +1 extra V signature); 200-box sample: witnesses 56,124/56,124, vectors 200/200 via lp.J.
   Caveat: certificates were not archived by C1 (verdicts only); they are deterministic and now independently re-derived.
 6 pairs (top-300 classes, n>=1 and n>=0): SOUND -- 1,050 random signature pairs re-proved at both n_min; 588,224 C1
   witnesses re-checked exactly, 0 failures; n=0 precondition (span A >= 5) holds (span a >= 10).
 7 negative controls: SOUND and TIGHT (open cases == where the 133 genuine single-box units live).
 8 Q5 lp.J spot check: 2,000 closures, 0 units.
 No FALSE claim found.
## INTEGRITY NOTE (original refGen instance, 05:20)
- Per NOTE-from-integrator.md (read as information): workers were killed at 04:33 by another lane's pkill, and a DUPLICATE
  copy of this agent killed my pool runs at 04:37 and wrote: the section "INCIDENT 04:33 ... and recovery", the section
  "Q4 per-box certificates -- FINAL (rg_q4_cert.log ...)", and the files rg_robust.py, rg_q4_cert.py, rg_sigcert.py,
  rg_results/, rg_results_sig/, rg_robust.log, rg_q4_cert.log, rg_sigcert.log.  Treated as a SECOND OPINION only; its
  200-box certificate result (56,124/56,124) coincides with mine (rg_q4b_wit.log).  rg_robust/rg_sigcert outputs are
  INCOMPLETE (stopped by the integrator) and NOT relied upon.  My '04:45 memory-pressure' guess above is superseded:
  the kills were the pkill (04:33) and the duplicate (04:37).
- None of my scripts was modified after 04:10 (mtimes checked); post-incident runs (rg_q4b.py, rg_q5_resume.py,
  rg_q5_combine.py, written 04:49) used unmodified code.
- COMPLETENESS AUDIT (counts from saved results): rg_allsig 5,157/5,157 signatures (my generator open on 0 of the 4,400
  C1-BOTH signatures); rg_q4b wit and vec 200/200 distinct boxes each (same box set); Q5 2,000 distinct seeds = exactly
  70000..71999 (550 + 100 pre-incident + 1,350 resumed); pairs 50 and 1,000 single-process (complete); rg_q1_exact
  531,440 = 3^12 - 1 words (full); rg_q5_ident 40,000 (full).  All verdicts above rest only on these complete runs.
