# NO-TIE lane: Lemma Q for Montesinos necklaces (horizontal-axis inversion)

Lane folder: ~/jones-lanes/theory-restart/mont/notie/  (Claude subagent, 16 Nov 2026)
Status: MAIN THEOREM PROVED (algebraic; topological reading conditional on Theorem N of the BRIEF).
Span: PROVED span >= 4 always, >= 4n-2 without ties, >= 4n-3 when the tie is only first-order; span >= 4n-3 is FALSE in general
(n = 13 example with extra twist, span 48); CONJECTURE span >= 3n (sharp at n = 2, 3). For genuine pretzels span >= 3n is PROVED
except one tie class (T2/B2), where it is CHECKED on 14,742 cases (Section 9). Sections 6, 7, 9.

## 0. Result in one paragraph
THEOREM Q-MONT (PROVED, Section 4). Let n >= 2, mu != 0, k in Z, and let v_1..v_n be rational boxes v_i = rho(w_i) e_1 with
a(v_i) not a unit. Then J = e_1^T X^mu Y^k (v_1 * ... * v_n) is NOT a unit. More precisely, exactly one of:
 (i) neither end of J has a first-order tie; then span(J) = sum_i span a(v_i) - 4 + T + T'' >= sum_i span a(v_i) - 2 >= 4n - 2;
 (ii) exactly one end ties (never both, for n >= 2); at the OTHER end the extreme coefficient is +-1 or +-2 and the next
      coefficient is nonzero, except in one explicit configuration P1 (or its mirror), where the next coefficient vanishes and
      the one after it is nonzero. In all cases J has at least two terms.
Mechanism: ties are one-ended; at the clean end a SECOND-ORDER extension of Astra's TH-2BR automaton shows the normalised
second coefficient of every box channel is <= 0 (a potential function), so the clean end's second coefficient cannot vanish.
With Theorem N (necklace formula, BRIEF section 1) this is Lemma Q for horizontal-axis inversions of Montesinos knots whose special
tangle is the twist X^mu (pretzels P(2mu', r_1..r_n) with |r_i| >= 3 odd, any signs, are a special case). The class contains
hyperbolic knots (e.g. P(-2,3,7)); for n >= 3 the knots are Montesinos with >= 4 rational tangles, hyperbolic by the standard
classification (recalled, not re-checked here). It is not covered by TH-2BR, U5-SF or CX-GRAPH.

## 1. Setup, conventions, reductions
Lambda = Z[t,1/t]. Matrices (BRIEF / board X.21): Y = [[1,0],[t^-3,t^-3]], X = [[1,1-t^4],[0,-t]], E = Y^-1 X = [[1,1-t^4],[-1,-1]],
E^2 = t^4. Channels of a vector v: a(v) = v_1, b(v) = v_1 + (1-t^3) v_2; slope q(v) = b/a; ratio r(v) = v_2/v_1, q = 1 + (1-t^3) r.
Star product multiplies channels. In (a,b)-coordinates Y = diag(1, t^-3) and
   J*Phi_3 = w_1 A + w_3 B,  A = prod a_i, B = prod b_i,  w_1 = t + (1+t^2)(-t)^mu,  w_3 = (1+t^2)(1-(-t)^mu),  Phi_3 = 1+t+t^2.
For f in Lambda (or in Q((1/t))) write top(f), bot(f), and at the top f = c1 t^D (1 + x_1 t^-1 + x_2 t^-2 + ...); rho(f) := x_1
(normalised second coefficient). rho is additive under products; so is l_2 := x_2 - x_1^2/2.

R0 (normal forms; PROVED from TH-2BR's prefix normalisation, board X.21). Every word gives rho(w) = unit * Y^{n_k} E Y^{m_{k-1}} ... E Y^{m_0}
   with interior m_i != 0 (E Y^0 E = t^4) and, after deleting the degenerate prefix, m_0 not in {0,-1}; if no E survives the box is
   integral (a a unit). So a non-integral rational box is v = unit * Y^{n_k} u, u = u(m_0..m_{k-1}) := E Y^{m_{k-1}} ... E Y^{m_0} e_1, k >= 1.
R1 (integral parts; PROVED). Y acts on channels as diag(1,t^-3), so all leading Y-powers and Y^k collect:
   J = unit * J(mu,N;u_1..u_n),  J(mu,N;u) := e_1^T X^mu Y^N (u_1 * ... * u_n),  N = k + sum n_k(i).
   So J*Phi_3 = A g with g := w_1 + w_3 Q,  Q := t^{-3N} prod q(u_i).
R2 (mirror; PROVED, and CHECKED 215 boxes + 400 necklaces exactly). With bar: t -> 1/t and u'' := u(-m_0-1, -m_1, ..., -m_{k-1})
   (again a normal form): bar a(u) = t^{-4k} a(u''), bar b(u) = t^{-4k-3} b(u''); bar w_i(mu) = t^-2 w_i(-mu); hence
   bar g(mu,N;u) = t^-2 g(-mu, n-N; u'')  and  bar J(mu,N;u) = t^{-4K} J(-mu, n-N; u''), K = sum k_i.
   Proof: bar Y = D Y^-1 D^-1, bar X = D X^-1 D^-1, D = diag(1,-t^3) (board X.21 sec. 3); bar E = t^-4 D Y E Y^-1 D^-1 telescopes to
   bar u = t^{-4k} D Y u''; then compute channels of D Y u''. []
   Consequently, with T := top g(mu,N;u) and T'' := top g(-mu,n-N;u''):
      span J = span A - 4 + T + T'',   span A = sum span a(u_i) >= 4n   (TH-2BR span formula: span a(u) = sum c_i >= c_0 >= 4).

## 2. Box laws (all at t = infinity; the bottom is the top of the mirror box by R2)
Run the TH-2BR automaton on r: Y: r -> t^-3(1+r), Y^-1: r -> -1 + t^3 r, E: r -> -(1+r)/D, a -> a D, D := 1 + (1-t^4) r_pre.
a(u) = prod over E-steps of D_i;  b(u) = a(u) q(u).
LEMMA BX1 (first order; = TH-2BR automaton, PROVED there). Post-E states R: r = t^-1(1+...), S_j: r = (-1)^j t^{-4-j}(1+...);
   init,n>=1 -> R; init,-m<=-2 -> S_0; any,n>=1 -> R; R,-m -> S_0; S_j,-m<=-2 -> S_0; S_j,-1 -> S_{j+1}. Every D_i has lc +-1.
   Hence q = -t^2 + ... (R) and q = 1 - (-1)^j t^{-1-j} + ... (S_j): deg b - deg a = 2, lc b = -lc a (state R);
   deg b = deg a, lc b = lc a (state S). State R iff last exponent m_{k-1} > 0. By R2, top-R <=> bottom-S.
LEMMA BX2 (second order; PROVED below; CHECKED 7095 sequences: all k<=4,|m|<=4 and 3000 random k=5..9,|m|<=5).
   Refine R to R_c: r = t^-1(1 + c t^-1 + ...), c in {0,1}. Transitions (new state, rho(D)):
     init,n>=1 -> (R_1,-1);  init,-m<=-2 -> (S_0,0);  R_c,1 -> (R_0,0);  R_c,n>=2 -> (R_1,-1);  S_j,n>=1 -> (R_1,-1);
     R_c,-m (m>=1) -> (S_0,+c);  S_j,-m<=-2 -> (S_0,-[j=0]);  S_j,-1 -> (S_{j+1},-[j=0]).
   rho_a(u) := rho(a(u)) = sum of the rho(D);  rho(q) = c (R_c), -1 (S_0), 0 (S_j, j>=1);  rho_b = rho_a + rho(q).
   Proof (each line is a two-term expansion; second-order data of S_j never matter):
   * positive power: r_pre = t^-3(1 + delta t^-1 + ...), delta = 1 iff (from R_c with n = 1) [t^-3(1+r), r = t^-1+...], else 0
     [n>=2: t^-3 + t^-6 + ...; from S_j or init: t^-3(1+O(t^-4))]. Then D = 1 + r_pre - t^4 r_pre = -t + (1-delta) + ..., so
     rho(D) = delta - 1, and r_post = (1+r_pre)/(t(1-(1-delta)t^-1+...)) = t^-1(1 + (1-delta)t^-1 + ...): c_new = 1 - delta.
   * from R_c with Y^-m: r_pre = t^{3m} r - (1 + t^3 + ... + t^{3m-3}) = t^{3m-1}(1 + c t^-1 + ...); D = -t^{3m+3}(1 + c t^-1 + ...)
     (r_pre and 1 are >= 4 lower); r_post = t^-4(1 + 0 t^-1 + ...) = S_0.
   * from S_j with Y^-m, m>=2: r_pre = -t^{3m-3}(1 - [j=0] t^-1 + ...) (the t^{3m} r term sits at relative order -1-j);
     D = -t^4 r_pre(1+...) = t^{3m+1}(1 - [j=0]t^-1 + ...); r_post = t^-4(1+...) = S_0.
   * from S_j with Y^-1: r_pre = -1 + t^3 r, 1 + r_pre = t^3 r exactly; D = t^4 - [j=0] t^3 + ...; r_post = -(1+r_pre)/D = S_{j+1}.
   * init with -m<=-2: r_pre = -(1 + ... + t^{3m-3}), D = t^{3m+1}(1 + 0 t^-1 + ...).  rho(q): q = 1 + r - t^3 r. []
COROLLARY BX3 (sign law; PROVED). Potential phi(R_0) = phi(R_1) = 1, phi(S_j) = phi(init) = 0. Psi := rho_a + phi is
   non-increasing along every transition (changes: 0, 0, 0, -1, 0, c-1, -[j=0], -[j=0] in the order above) and starts at 0. Hence
     rho_a(u) <= -1 for R-top boxes,  rho_a(u) <= 0 for S-top boxes,  rho_b(u) <= 0 for all boxes
   (R_c: rho_b = rho_a + c <= 0; S_0: rho_b = rho_a - 1; S_j: rho_b = rho_a).
   Equality rho_a = 0 for an S-top box iff every step preserves Psi iff the sign sequence (m_0,...,m_{k-1}) ALTERNATES and ends
   negative (R_0 and S_{j>=1} are never visited). Call these alternating S-boxes.
LEMMA BX4 (third order on alternating S-boxes; PROVED; CHECKED 1001 alternating boxes k<=6, |m|<=3). Along an alternating path the
   states are init, S_0, R_1 with r(R_1) = t^-1(1 + t^-1 + t^-2 + ...); every D has x_2(D) = 0, and x_1(D) = 0 for the step
   init -> S_0, x_1(D) = +-1 for all other steps. Hence x_2(a(u)) = l_2(a(u)) = -(k - [m_0 <= -2])/2 <= 0, = 0 iff u = u(-m), m >= 2.
   (Expansions: positive step r_pre = t^-3(1 + O(t^-3)), D = -t(1 - t^-1 + 0 t^-2 + ...); R_1 -> S_0: r_pre = t^{3m-1}(1 + t^-1 + 0 t^-2 + ...),
   D = -t^{3m+3}(1 + t^-1 + 0 t^-2 + ...); init -> S_0: D = t^{3m+1}(1 + 0 + 0 + ...).)

## 3. Necklace ends
w-data (direct): top/c1/rho of w_1: (mu+2, (-1)^mu, 0) for mu>=1; (-1,-1,0) for mu=-1; (1, 1, [mu=-2]) for mu<=-2.
                 top/c1/rho of w_3: (mu+2, -(-1)^mu, [mu=1]) for mu>=1; (2, 1, [mu=-1]) for mu<=-1.
Let rho := #R-top boxes, d := 2 rho - 3N = top(B') - top(A) (B' = t^{-3N} B), c1(B')/c1(A) = (-1)^rho.
Delta := top(w_3 B') - top(w_1 A) = d (mu>=1), d+3 (mu=-1), d+1 (mu<=-2); eps := c1(w_3 B')/c1(w_1 A) = c1(w_3) c1(w_1) (-1)^rho.
LEMMA N1 (top tie; PROVED). The top of J*Phi_3 cancels at first order iff Delta = 0 and eps = -1, i.e.
   T1: mu>=1, d=0, rho even;   T2: mu<=-2, d=-1, rho odd;   T3: mu=-1, d=-3, rho even.
   Otherwise T = top g = max(top w_1, top w_3 + d) exactly.
LEMMA N2 (bottom tie; PROVED via R2, mirror has rho'' = n - rho, d'' = -n - d):
   B1: mu<=-1, d=-n, rho = n mod 2;   B2: mu>=2, d=1-n, rho != n mod 2;   B3: mu=1, d=3-n, rho = n mod 2.
LEMMA N3 (ties are one-ended; PROVED). For n >= 2 no T_i holds together with any B_j: T1&B2 => n=1; T1&B3 => n=3 and rho
   even and odd; T2&B1 => n=1; T3&B1 => n=3 and rho even and odd; the other pairs need incompatible signs of mu. []
LEMMA N4 (no tie; PROVED). If neither end ties, T + T'' >= 2 (>= 5 if |mu| >= 2), so span J >= span A - 2 >= 4n - 2.
   (mu>=2: T = mu+2+max(0,d) >= 4, T'' = max(1, 2-n-d) >= 1; mu=1: T = 3+max(0,d), T'' = max(-1, 2-n-d), sum >= 2; mu<0 by R2.)
LEMMA N5 (second coefficient at a clean top; PROVED; CHECKED 19,574 random clean tops n=2..5, exact agreement).
   s_1 := rho(w_1) + sum rho_a(u_i), s_3 := rho(w_3) + sum rho_b(u_i). If the top does not tie, the normalised second coefficient
   of J*Phi_3 is  s_1 (Delta<=-2), s_1+eps (Delta=-1), (s_1+s_3)/2 (Delta=0, eps=+1), s_3+eps (Delta=1), s_3 (Delta>=2),
   and since J*Phi_3 = J (t^2+t+1):  c2(J) = c1(J) (ratio - 1). So c2(J) = 0 iff ratio = 1.

## 4. Main theorem and proof
THEOREM Q-MONT. As in Section 0. PROOF. By R0-R1 reduce to J(mu,N;u_1..u_n), u_i normal forms, k_i >= 1. If no end ties, N4.
By N3 at most one end ties; by R2 (the class is closed under mirror, and bar J is a unit multiple of the mirror necklace) we may
assume the BOTTOM ties (B1, B2 or B3) and the top is clean. Evaluate N5 with BX3: rho(w_1) <= 1, rho(w_3) <= 1, never both 1,
sum rho_a <= 0, sum rho_b <= 0, R-boxes have rho_a <= -1:
 B1, mu<=-2, n=2: Delta=-1, eps=(-1)^rho=+1, ratio = s_1+1 = 1 needs s_1 = 0: either mu<=-3 and all rho_a = 0 (then rho = 0, d=-3N=-2,
   impossible) or mu=-2 and sum rho_a = -1 (one box rho_a = 0 is S, rho even forces rho = 0, again -3N = -2): impossible.
 B1, mu<=-2, n>=3: Delta = 1-n <= -2, ratio = s_1 = rho(w_1) + sum rho_a = 1 iff mu = -2 and all rho_a = 0
   => all boxes alternating S-boxes, rho = 0, 3N = n, n even: CONFIGURATION P1 (n = 0 mod 6, N = n/3, mu = -2).
 B1, mu=-1: n=2: Delta=1, eps=-1, ratio = s_3 - 1 = sum rho_b <= 0;  n=3: Delta=0, eps=+1, ratio <= 1/2;
   n=4: Delta=-1, eps=-1, ratio = sum rho_a - 1 <= -1;  n>=5: ratio = sum rho_a <= 0.
 B2 (mu>=2): n=2: Delta=-1, eps=+1, ratio = sum rho_a + 1 = 1 forces all boxes S, rho = 0, but rho is odd: impossible;
   n>=3: ratio = sum rho_a <= 0.
 B3 (mu=1): n=2: Delta=1, eps=-1, ratio = sum rho_b <= 0; n=3: Delta=0, eps=+1, ratio <= 1/2; n=4: ratio = sum rho_a - 1;
   n>=5: ratio = sum rho_a <= 0.
So outside P1, c1(J) != 0 != c2(J) at the top. In P1: Delta = 1-n <= -5, so the top three coefficients of J*Phi_3 are those of
w_1 A, w_1(-2) = t(1 + t^-1 + 0 t^-2 + t^-3), and by BX4 A = c t^D (1 + 0 t^-1 + Y t^-2 + ...), Y = sum x_2(a(u_i)) <= 0.
Dividing by Phi_3 = t^2(1 + t^-1 + t^-2): J = c t^{D-1}(1 + 0 t^-1 + (Y-1) t^-2 + ...), and Y - 1 <= -1. So J has >= 2 terms. []
   (P1 is not empty: six copies of u(-2) (= row -3), mu = -2, N = 2 has top coefficients 1, 0, -1, 8 and bottom -6, 28, ...; span 24.)
COROLLARY (Lemma Q for the class; CONDITIONAL on Theorem N). Horizontal-axis inversions of Montesinos knots realised as
necklaces s.r2.(y1)^m.B_1...B_n.u1 with n >= 2 non-integral rational bodies and m != 0 (in particular all pretzels P(2m', r_1..r_n),
m' != 0, |r_i| >= 3 odd, any signs, any extra integral twist) have non-unit J, hence are not flat.
SCOPE NOTE. Only the special-twist (X^mu) necklaces of the task are covered; Montesinos inversions whose two fixed points lie in
two different tangles, or whose special tangle is a general rational tangle, are not of this form and are not claimed.

## 5. Verification log (exact pure-Python; scripts in this folder)
- auto2.py: second-order automaton vs exact rho_a, rho_b: 7095/7095.
- neck2.py: N5 prediction vs exact second coefficient at clean tops: 19,574/19,574 (n=2..5, |mu|<=6, N in [-4,6], boxes up to k=7).
- verify_main.py / verify_main2.py: 8,949 forced first-order ties (n=2..6): never two-ended; clean-end second coefficient as predicted
  and nonzero in all; 600 forced P1 instances (n=6): c2 = 0 and c3 = c1 (Y-1) != 0 in all; no unit found.
- verify_mirror.py: R2 identities (215 boxes, 400 necklaces) and BX4 (1001 alternating boxes): exact.
- tie2.py: S3 next-coefficient formula at 3306 forced top ties: exact; M4 congruence: no violation.
- pretzel_check.py: 36 mixed-sign pretzel half-diagram words (bracket state sum, lp.J): necklace formula exact, no unit.
- final_check.py: 1,310 further forced ties (n = 2..8, boxes up to k = 10, |m| <= 6, |mu| <= 7): clean-end prediction exact, no monomial;
  80 P1 instances with random alternating boxes up to k = 7 at n = 6 and n = 12: c2 = 0 and c3 = c1 (Y-1) exactly.

## 6. Span bounds
LEMMA M4 (congruence; PROVED; CHECKED 3306 tie cases). For the raw necklace J(mu,N;u) (normal-form boxes):
   J = 1 mod (t^4 - 1),  and more precisely  J = A + f_mu V'_2,  f_mu := (1-t)(1+t^2)(1-(-t)^mu),  V' := Y^N (u_1 * ... * u_n).
   Proof. e_1^T X^mu = (1, f_mu) (upper-right entry of X^mu is (1-t^4)(1-(-t)^mu)/(1+t)). At t^4 = 1, X = diag(1,-t), and Y, E and every
   multiplication matrix M(u) = [[a,0],[v_2,b]] are lower triangular with (1,1)-entry a; inductively a(u)(zeta) = 1 for zeta^4 = 1
   (E and Y have (1,1)-entry 1 and upper-right entry 0 there). So J(zeta) = A(zeta) = 1 at the four simple roots of t^4 - 1. []
COROLLARY S1 (PROVED). span J >= 4 for every n >= 2, mu != 0. (If span <= 3, the <= 4 coefficients lie in distinct classes mod 4,
   so J = 1 mod t^4-1 forces J = t^e, contradicting Theorem Q-MONT.) A span-4 J has the shape c t^D + t^{D-k} - c t^{D-4} (k in 1..3)
   or c t^D + (1-c) t^{D-4}.
S2 (PROVED, = N4). No tie: span J >= sum span a(u_i) - 2 >= 4n - 2.
LEMMA S3 (second-order tie end; PROVED; CHECKED 3306 forced top ties, exact). At a cancelling top tie the coefficient of J*Phi_3 one
   degree below the cancelled one is c1(w_1 A) (s_1 - s_3), with
     s_1 - s_3 = rho(w_1) - rho(w_3) - sum_i rho(q_i) = [mu=-2] - [mu=+-1] + #S_0-boxes - sum over R_c-boxes of c.
   So if s_1 != s_3 the deficit at the tie end is exactly 1, and then (using T''_gen of the clean end)
     T1, mu>=2: span = span A + mu - 2;  T1, mu=1: span A - 2 (n=2), span A - 3 (n>=3);  T2: span A + |mu| - 2;
     T3: span A - 2 (n=2), span A - 3 (n>=3).  Hence span J >= span A - 3 >= 4n - 3 (>= 6 for n = 2).
   Explains the minimal family: u = u(-2) (row -3) repeated, mu = -1, N = 1: T3 tie with s_1 - s_3 = n - 1 != 0: span = 4n - 3 for n >= 3,
   6 for n = 2 (CHECKED n = 2..6: 6, 9, 13, 17, 21; same for the mirror family u(1)^n, mu = -1, N = n).
OBSTRUCTION (second-order ties s_1 = s_3; CHECKED): the tie can cascade to arbitrary depth.
 * Deficit unbounded: mu = 3, N = 0, u_1 = u(-m,-1,-1) (state S_2: X^3 cancels its two trailing X^-1 factors), u_2 = u(-2,-1^j):
   (m,j) = (5,14): T = -11 against T_gen = 5, span J = 19, span A = 33. Along this family span J does not grow with j
   (j = 3, 6, 10, 14: m = 5 gives 20, 20, 20, 19; m = 8 gives 29, 29, 29, 29; m = 3 gives 14, 14, 16, 16) while span A grows by 1 per
   unit of j. So no bound of the form span J >= span A - C exists (CHECKED, cascade.py).
 * 4n-3 fails: 13 zero-excess boxes (u(-2) x 7, u(1) x 6), mu = 1, N = 4 (T1 with rho = 6): span 48 < 49 = 4n-3
   (same for mu = -1, N = 5 with u(1) x 6, u(-2) x 7). Here s_1 = s_3 and the deficit is 2.
CONJECTURE S4: span J >= 3n for all n >= 2 (sharp: 6, 9 at n = 2, 3).
   Evidence: zero-excess scan (all necklaces of copies of u(-2), u(1); n <= 28, |mu| <= 4, all relevant N): min span - 3n = 0,
   attained only at n = 2, 3; exhaustive n = 2 (63 boxes k <= 3, |m| <= 2, |mu| <= 5, N in [-3,4]): min 6; n = 3 (k <= 2): min 9;
   12,535 random tie cases with boxes of length <= 9: min span - 4n = -2 (n=2), +9 (n=3), +16 (n=4). The BRIEF's n = 4 minimum 14
   is not the true minimum (13, family above).
   A proof needs the full cascade: the k-th coefficient below a cancelled tie is a k-th order expression in the box data
   (S3 is k = 2); deep cascades occur only when the closure twist X^mu cancels into the X^-1-tail of one box while all other boxes
   are close to the trivial slope (S_j with large j, or R-boxes close to the X-eigenslope -t/(1+t^2)); those boxes then have large
   span, and span J stays large in every example, but the bookkeeping is not done.

## 7. Open problems and exact status
- Theorem N (necklace formula) is still unproved in writing (BRIEF); Q-MONT is a theorem about the algebraic necklace coefficient.
- Span >= 3n (S4) open in general; needs the higher-order tie-end theory (Section 6 obstruction). For pretzels only the T2/B2
  class remains (Section 9: reduce to top H >= -1).
- Scope: Montesinos inversions whose fixed points lie in two different tangles, or whose special tangle is a general rational tangle
  (not a pure X^mu twist), are outside this necklace model.
- Extreme coefficients: at the clean end |c1| in {1,2} (2 occurs: Delta = 0 non-cancelling, e.g. B1 with mu = -1, n = 3), so the
  TH-2BR "extremes +-1" property does NOT extend to necklaces.

## 8. Files (this folder)
nt.py (normal-form boxes, necklaces), auto2.py (second-order automaton + check), neck2.py (clean-end prediction + check),
verify_main.py, verify_main2.py (tie-case mechanism), verify_mirror.py (R2, BX4), tie2.py (S3, M4), tie3.py/tie4.py (span scans),
cascade.py/cascade2.py (deep cascades), span1-3.py (min-span data), pretzel_check.py (36 actual mixed-sign pretzel words via lp.J:
formula exact, no unit), explore*.py (exploration).

## 9. Pretzel closed form (added; PROVED algebraically from the BRIEF's row formulas, CHECKED 300 random cases exactly)
For rows r_i odd, |r_i| >= 3, put z_i := (-t)^{(r_i-1)/2} (so z = (-t)^j for r = 2j+1 > 0 and z = (-t)^{-(l+1)} for r = -(2l+1) < 0).
With Phi_6 = t^2 - t + 1, alpha = (t-1)(t^2+1), beta = t(t-1):
   a(row r) = u_r (Phi_6 + z alpha),  b(row r) = u_r (Phi_6 - z beta),  u_r = t^-3 (r > 0), t (r < 0)
(from the BRIEF's a_r, b_r and the mirror rule t -> 1/t), hence for the pretzel necklace with extra twist k
   J*Phi_3 = unit * G,  G := w_1 prod_i (Phi_6 + z_i alpha) + w_3 t^{-3k} prod_i (Phi_6 - z_i beta)
           = Phi_6^n sum_S z_S gamma_|S|,   gamma_m := w_1 (alpha/Phi_6)^m + (-1)^m t^{-3k} w_3 (beta/Phi_6)^m.
Key identities: gamma_0 = Phi_3 (k=0); gamma_1 = (t-1)(t^2+1) Phi_3 (-t)^mu / Phi_6 (k=0); and the DEGENERATION identity
   Phi_3 + (-t)^{-1-mu} gamma_1 = Phi_3 / (t Phi_6)       (single row -(2mu+1), or +(2|mu|-1) when mu<0, closes to the unknot).
Equivalently (all gamma_m are divisible by Phi_3 when k = 0, since alpha/Phi_6 = -beta/Phi_6 at primitive cube roots of unity):
   J = unit * Phi_6^n * sum_S z_S g_|S|,  g_0 = 1,  g_m = (t-1)^m (t^2+1) Phi_6^{-m} ( t [m-1] + (-t)^mu [m] )  (m >= 1),
   [k] := ((t^2+1)^k - (-t)^k)/(t^2+t+1)   (sympy-verified for m <= 3, sym1.py; the general m is the one-line expansion of gamma_m).
Pair identity (row 2j+1 next to row -(2j+1), z_+ z_- = -1/t):  Phi_3 - gamma_2/t = -Phi_3 [ (-t)^mu Phi_6 (t-1)^2 (t^2+1) - t^3 ] / (t Phi_6^2).

PRETZEL SPANS (genuine pretzels P(2mu', r_1..r_n), i.e. k = 0; write H := G/Phi_6^n, so span J = 2n + top H + top H'' - 4 where H'' is
the mirror pretzel (-mu, -r_i)). With k = 0 only the tie types T1 (all rows negative, mu >= 1), B1 (its mirror), T2 (exactly one
positive row, mu <= -2) and B2 (its mirror) occur (T3, B3 need an extra twist). Results:
 - Clean tops (PROVED, CHECKED within 3615): if mu >= 1 and p >= 1 positive rows, top H = sum_pos j_i + mu + 2 + p (unique maximising
   subset S = positive rows in the tropical expansion sum_S z_S gamma_|S|).
 - T1 (PROVED; CHECKED 1932 cases n=2..4, l<=7, mu<=6): rows -(2l_i+1), mu >= 1:
     top H = mu+2-l_min (l_min < mu);  2 (l_min > mu, or l_min = mu attained twice);  max(-1, mu+2-l_(2)) (l_min = mu attained once;
     the degeneration identity collapses Phi_3 + z gamma_1 to Phi_3/(t Phi_6), and the next row cannot cancel: its coefficient has
     the same sign). Hence span J >= 3n for every T1 and B1 pretzel. Proof: the mirror (B1 type: rows +(2l_i+1), -mu) has a clean
     top with unique maximiser S = all rows: top H'' = L + deg gamma_n(-mu), L = sum l_i, deg gamma_n = n+1 (mu >= 2), 2 (mu = 1, n <= 3),
     n-1 (mu = 1, n >= 4). mu >= 2: span = 3n + L - 3 + top H; top H >= 2 unless l_min = mu once, and then L >= mu + (n-1)(mu+1)
     >= 3n-1 and top H >= -1, so span >= min(4n-1, 6n-5) >= 3n. mu = 1: span = 2n + L - 2 + top H (n <= 3), 3n + L - 5 + top H (n >= 4);
     top H = 2 gives >= 3n; if l_min = 1 once, top H = max(-1, 3 - l_(2)) and L >= 1 + (n-1) l_(2), l_(2) >= 2, giving 3 + max(l_(2)-1, 3)
     >= 6 (n=2), >= 10 (n=3), >= 5n - 7 (n >= 4). []
 - T2 (PROVED reduction, CHECKED 3615): one positive row j, negative rows l_i (L = sum l_i), mu = -m <= -2:
     span J = 3n + L + m - 3 + top H.  CHECKED (14,742 cases: m<=8, j<=9, up to 4 negative rows): top H >= -1 and span J >= 3n + 1.
     (top H >= -1 implies span J >= 3n: L + m >= 3, and when L = 1, m = 2 (pretzel P(-4, 2j+1, -3)) no top cancellation occurs.)
     Structure (PROVED): H/Phi_3 = A_0 + (-t)^j A_1 with A_0 = sum_{S in neg} z_S g_|S| = 1 + O(t^-3) (clean all-negative necklace)
     and A_1 = sum_{S in neg} z_S g_{|S|+1}, top A_1 = max(1-m, -l_min) (no cancellation inside A_1). The top cancels exactly in
     (a) j = m-1 < l_min  [twist-row degeneration]  or  (b) j = l_min < m-1 attained once  [row/antirow pair];  j = l_min = m-1 does
     NOT cancel (coefficients add). After a cancellation the next coefficients of H/Phi_3 are -x_1(A_1), -x_2(A_1), [A_0]_{-3} - x_3(A_1)
     (x_k = normalised coefficients of A_1).
     (a) PROVED (CHECKED 495): x_1 = -#{l_i = m}, x_2 = -#{l_i = m+1} (if x_1 = 0), x_3 = -1 - #{l_i = m+2} (if x_1 = x_2 = 0; the -1 is
         g_1 = (-t)^mu t (1 - t^-3 - ...)), and [A_0]_{-3} = 0; so top H = 1, 0, -1 according as l_min = m, m+1, >= m+2.
     (b) PROVED: x_1 = -[l_1 = m-2] - #{l_i = l_1+1}; if nonzero, top H = 1 (CHECKED). If x_1 = 0 then
         x_2 = -1 + [l_1 = m-3] + #{l_i = l_1+2}, which CAN vanish (e.g. the pair alone with j = m-3): third order needed. OPEN, but
         CHECKED top H >= -1 in all 14,742 cases.
 - No tie: span >= 4n - 2 (N4).
 So for genuine pretzels: span J >= 3n PROVED in all classes except T2/B2, where it is CHECKED (and reduced to top H >= -1).
 Pretzel minimum (CHECKED rows |r| <= 11, n <= 5, |mu| <= 6): 6, 9, 13, 17 = max(3n, 4n-3), attained by P(-2, 3, ..., 3) (mu = -1).
