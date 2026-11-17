
## 7. GAPs and next targets
 GAP-A (two-ended families, the real frontier after order 3): a-potential d2 classes (rho_a = +1 at one end, sigma = -1/-2) in
   d=0 / tie configurations: H mu = +-1 tie (n pinned = delta.k + 3) and 'd=0 r=1', V 'd=0 r=1' (mB = +-1) and the V tie (mB = 0),
   plus their multisets.  Next lemma (derived, not yet in the generator): at a two-ended tie with the tau-law violated
   (sum tau_j - n != tau*), one end stops at r = 2 exactly; with d_i = l_i(s1) - l_i(s2) at that end (d_1 = 0, d_2 != 0 known from
   tau) the Phi_3 pattern needs  d_3/d_2 + X1 = 1  (linear in the rational l3(q) sums and alpha for fixed k) and
   (d_4 - d_2^2/2)/d_2 + X1 d_3/d_2 + x_2(s1) = 1 (needs the K = 4 automaton, quadratic in X1: slice X1).  Same mechanism as 5.2.
 GAP-B: horizontal/vertical d=0 slices are exact only for the class sets tested; THEOREM M300 uses the phi-lemma (top-300 only).
 GAP-C: the order-3 closure of F1 (5.5) uses the K = 3 automaton and box-level l3 data; (b) relies on 2 MILP verdicts.
 GAP-D: 'open' verdicts are LP-feasibility in the relaxation (n * conv of automaton paths): they mean 'no certificate of this
   order', not that a unit exists; the exact searches (5.1, 5.6, 5.7) found none.
 CAVEAT (inherited): every theorem here is conditional on C1's framework being sound (Lemma W, BX1-BX4/BX4', T2, the K = 3 jet
   automaton, R2 mirror for bottom data); refGen (round D) is refereeing that framework.

## 8. Files (all in this folder)
 lpg.py (case rows affine in end data, LP assembly with automaton flows, exact Farkas extraction/verification), runner.py,
 classes.py (jet classes from C1's gen2_res.pkl), val1.py / val2.py (validation), run_uni.py (uniform runs; uni_*.pkl, uni_*.log),
 certs300.py + certs_M300.pkl (THEOREM M300 certificates), pairs_d2.py + pairs_d2.pkl, d2fix.py / d2fix2.py (+ .pkl/.log),
 f1o3.py (order-3 lemma for F1), f1uni.py, f1bound.py, f1large.py, f1milp.py (+ logs), exact.py / exact_run.py (+ exact_J*.pkl,
 exact_run.log), verify_unit.py (HIT protocol helper), ana.py, c1copy/ (unchanged copies of C1 modules, sys.path lines only).
