# REFEREE NOTES: ARB-CONTENT / ARB-RESONANCE-BUDGET (Codex 20261117-074231)
17 Nov 2026, Claude (independent referee). Folder: ~/jones-lanes/theory-restart/mont/referee/arb-resonance/
Read: collab/msgs/20261117-074231-codex.md, work/theory_restart/arborescent_resonance_divisor.md; background mont/proof/REPORT.md
(Theorem N, Prop 4.2), mont/nest/REPORT.md (Theorem O, Theorem V), cx/engineC1/REPORT.md (3.2 eigen-coordinate), cx/roundE/arb/REPORT.md.
Python: tools/venv/bin/python (sympy 1.14). All computations exact (integer Laurent dicts; sympy only for rational-function checks,
gcd and factorisation). No new enumeration; bodies are the existing libraries and frontier records.
Marks: SOUND / GAP / FALSE.

## Verdicts
 (1) INTEGRAL EIGENPAIR ............................................................. SOUND
 (2) ARB-CONTENT (invariance, superadditivity, exact gain, vertical survival) ......... SOUND
 (3) ARB-RESONANCE-BUDGET (span identity (5); two candidate twists (7), incl. H = 0) .. SOUND
 (4) formal budget-exhausting state ................................................... SOUND (formal only, as stated)
 Side claims checked: N-INF family primitive (SOUND); gcd(A,B) = gcd(a,c) on actual bodies (SOUND).
 Nothing FALSE found. One wording caveat (not a gap): identity (5) as written needs gcd(A,B) = 1; for non-primitive pairs the
 exact form is span f_m = span(gcd) + H + ... (CHECKED 1,863/1,863; the uncorrected form fails in all of them). The note does
 state primitivity as a hypothesis and rejects content first, so this is consistent.

## Library used (common.py)
 rational R(5) (40 boxes, lib.rational), all 50 general_boxes.json bodies, 200 random nests (R(4) + non-rational general children,
 depth 1-2, |m| <= 4, |N| <= 2), frontier records (274): 150 sampled dangerous depth-one classes D (greedy_n2.pkl reps), 100 of
 the 292 depth-2 positive-potential boxes (engineA d2pos_boxes.pkl), the N-INF family P_k, F_{-1,1,2}(P_k) (k = 6, 12), the 7
 positive-potential depth-one examples of arb REPORT section 3, and the min-span near-miss products of ex_d1..ex_d6, ex_o3, ex_o3b,
 ex_s2. Check 3 adds 120 random 2-3 factor products and 12 content-carrying products. 564 bodies (561 non-scalar: G25, G35, G44 have scalar states c = 0;
 note lib.py's comment lists 6, 35, 44 as scalar, but G6 is not scalar: it is content times the integral box y0, see (2)).

## (1) Integral eigenpair: SOUND (check1.py, check1.log; 84 s)
 Algebra by hand: A - B = a; A - eB = a + c[C + t(1-t)] = a + (1-t^3)c = b; t(A-B) + (1+t^2)(A-eB) = Phi3 A since (1+t^2)e = -t.
 X(a,c) = (a + (1-t^4)c, -tc) gives A' = A, B' = -tB. Star: b12 - a12 = (1-e)[A1B2 + B1A2 - (1+e)B1B2]. Integrality: on the lattice
 B_i = C c_i, e B1B2 = -t(1-t)^2(1+t^2) c1c2 and (1+e)B1B2 = Phi6 (1-t)^2 (1+t^2) c1c2; and B12 = C c12 with
 c12 = a1c2 + c1a2 + (1-t^3)c1c2 (since 2C - Phi6(1-t) = 1-t^3), so the lattice B in C*Lambda is closed under *. Y^N: matrix as
 stated, det r = t^-3N, and (1-t) | k = (t^-3N - 1)/Phi3, so Y^N also preserves B in C*Lambda.
 Exact checks on all 564 bodies (0 failures):
   a = A - B, (1+t^2)b = (1+t^2)A + tB, t a + (1+t^2) b = Phi3 A ......................................... 564/564
   raw outer map: independent rho(X)^-m powers on (a,c) give (A, (-t)^-m B) ............................ 1,122/1,122
   normalised vc.F (Theorem O): (A,B) -> t^(2m(1-eps)) (A, (-t)^-m B) .................................. 1,122/1,122
   Y^N matrix [[1+(1+t^2)k, tk], [(1+t^2)k, 1+tk]] and det = t^-3N ..................................... 564/564, 564/564
   horizontal closure: rho(X)^mu first row = A - (-t)^mu B, and Phi3 (A - (-t)^mu B) = w1 a + w3 b ....... 564/564, 564/564
   star product with e = -t/(1+t^2) as a sympy rational function: A12, B12 are Laurent and equal the
   eigenpair of the integral star product ............................................................... 300/300 pairs
   z12 = (z1 + z2 - (1+e) z1 z2)/(1 - e z1 z2) ......................................................... 60/60
   ROOTS facts a(1) = a(i) = 1, A(1) = 1, a(-1) = 1 ....................................................... 564/564
   gcd(A,B) = gcd(a,c) (sympy, up to units) ............................................................. 198/198
 Off-lattice control: (A_i,B_i) = (1,1) gives a non-Laurent A12 (integrality genuinely uses B in C*Lambda).
 Remarks. Codex's A is C1's alpha and Codex's z = B/A equals C1's z = -(1+t^2)beta/alpha; the new content is that the pair
 (alpha, -(1+t^2)beta) = (a + Cc, Cc) is integral and that the unit equation has no Phi3. Notation hazard: A, B here are the
 eigen-amplitudes, not Theorem N's channel products prod a_i, prod b_i; e here is C1's e2.

## (2) ARB-CONTENT: SOUND (check2.py, check2.log; content_census.py/.log)
 Hand: X, Y in GL2(Lambda) (det -t, t^-3) so the ideal (a,c), hence gamma_p, is invariant; each entry of the integral star law is
 bilinear, giving (2) at every p; for p not dividing 1-t^3, [[1,0],[1,d]] is invertible over the DVR Lambda_(p), so
 gamma_p = min(nu_p a, nu_p b) and (3) is 2min(x,y) = x + y - |x-y| summed. Vertical: Phi3 | w1 + wV (value at omega is
 omega + omega^2 * (-omega^2) = 0) and (w1 a + wV b)/Phi3 = [(w1+wV)/Phi3] a + (1-t) wV c.
 Exact test: primes harvested by factoring the channel amplitudes of 558 bodies (1,034 distinct irreducible factors; only 5 occur
 with children of BOTH signs: t^4-t^3-1, t^4+t-1, t^5-t^4+t^3-t+1, t^5-t^4+t^2-t+1 and one of degree 12).
   800 products (400 targeted opposite-sign products with 2-7 factors, 400 random 2-4 factor products), 3,995 evaluations at primes
   not dividing 1-t^3 (harvested primes, 2, 3): gain formula exact 3,995/3,995; gain histogram 0: 3,595, 1: 302, 2: 73, 3: 25.
   Excluded primes 1-t, Phi3: inequality (2) 1,600/1,600 (on actual bodies these are trivial: a(1) = b(1) = 1, and a, b never
   vanish at omega in the library).
   On 145 content-carrying products: gamma_p invariant under vc.F (m = +-1, +-2) 592/592 and Y^N 592/592; p^gamma divides every
   horizontal closure (mu in [-6,6]) 1,924/1,924 and every vertical closure (odd l in [-7,7]) 1,184/1,184; one further nest
   F_m(prod * child) keeps >= gamma 148/148.
   Vertical identity for every l in [-15,15] (odd and even): Phi3 | w1 + wV 31/31; identity on actual vectors 620/620; agrees with
   vc.raw_vert 320/320.
 Content is NOT vacuous on actual data (content_census.log): 8 of the 774 dangerous depth-one representatives carry content, e.g.
   g1_1478 = F_2(Y^2 (B(XY)B(y)) (B(XXXyy)B(y))), content t^4 - t^3 - 1; g1_1775 = F_-1(B(xxy) B(XXXY)B(y)), content
   t^5 - t^4 + t^2 - t + 1 (this box is the E-D3 near-miss MIN:ex_d3, which therefore is non-flat by content alone);
   0 of the 292 d2pos boxes; 2 of 200 random nests (N43, N132); general body G6 = g * (t^-11)(1, t^-3), i.e. a local knot g on the
   integral box y0: its content is the local-knot polynomial. So content is a cheap per-box filter that kills about 1% of the
   dangerous depth-one representatives; it is a property of the box, not of its order-2 signature class.

## (3) ARB-RESONANCE-BUDGET: SOUND (check3.py, check3.log; nearmiss.py/.log)
 Hand: (7) is the elementary support argument (if neither the bottom nor the top exponents of A and (-t)^-m B coincide, f_m has
 distinct extreme terms at min(bot) < max(top), so it is not a monomial); it needs neither primitivity nor H > 0. (5) is degree
 counting for 1 - w_m on P^1; under primitivity the finite zeros of 1 - w_m are exactly the roots of f_m; in elementary terms
 span f_m = span A + end overhangs - end cancellations, and H = span A for primitive pairs. This is Lemma W ("some end
 coincides") in the Phi3-free normalisation; removing Phi3 is what makes the statement hypothesis-free and exactly two-valued.
 Exact test (independent rho(X)^-m powers on (a,c), m in [-40,40]):
   693 non-scalar bodies (670 primitive, 23 non-primitive), 56,133 (body, m) points; f_m = A - (-t)^-m B and f_m(-1) = 1 at all.
   Unit events: 49 in 36 bodies; ALL 49 lie in {nu_0 z, -nu_inf z}. Cross-check: 16 unit events confirmed J = 1 and 27 values
   matched by direct half-diagram brackets (lp.J of s.r2.(y1)^m.<word>.u1).
   Span identity (5) at EVERY window point for primitive bodies: 54,270/54,270; positive contact only at an aligned end: always.
   Non-primitive bodies: the gcd-corrected identity 1,863/1,863; the uncorrected one fails 1,863/1,863 (primitivity is needed).
   Formal adversarial pairs (arbitrary Laurent A, B, units planted at a chosen twist; 1,351 with A a monomial, i.e. H = 0):
   2,366 unit events, all in the candidate set.
 Findings for the frontier:
   * The bound "two" is SHARP: 13 bodies have units at BOTH candidates (e.g. R:xy at m = -2 and -1); all have kappa = -1.
   * Every unit event belongs to a body with a RATIONAL (two-bridge) vector (17 R(5) boxes, 15 general bodies reducible to rational,
     4 single-child rational nests); all 36 unit bodies have kappa = -1; no unit at a kappa = 0 (simultaneous) resonance, although
     125 bodies have kappa = 0.
   * H = 0 is realised by actual bodies: 10 primitive frontier records with A = 1 exactly (mirror-pair nests such as
     F_-4(Y (B(XY)B(y)) B(xy)) = D:g1_575 and all 7 positive-potential examples F_+-5(B(XY)B(xy)), F_+-6(B(XXY)B(xxy)), ...); none
     has a unit (they have kappa = -8 etc.).
   * No primitive unit candidate exists among the 274 frontier records (0 units at their 509 candidate twists). Closest approach:
     D:g1_353 = F_-2(B(xy) B(xxxxy)) (also the E-D1 min-span record) at m = 1: kappa = 0, H = 10, (tau0, tauinf) = (1, 3),
     span f = 6 (= E-D1's min span J 6). Complete eigenpair (exponent: coefficient):
       A = {16:-1, 17:2, 18:-2, 19:2, 20:-1, 22:1, 23:-2, 24:3, 25:-2, 26:1}
         = t^16 (t^10 - 2t^9 + 3t^8 - 2t^7 + t^6 - t^4 + 2t^3 - 2t^2 + 2t - 1), irreducible: the 10 finite poles of z
       B = {17:1, 18:-3, 19:4, 20:-4, 21:2, 22:1, 23:-3, 24:4, 25:-3, 26:2, 27:-1}
         = -t^17 (t-1)^2 (t+1)(t^2+1)(t^2-t+1)(t^3+t-1)  (finite zeros of z: Phi1 twice, Phi2, Phi4, Phi6, t^3+t-1; 10 in all).
     Next: span 7 at the H = 0 bodies D:g1_575 / g1_579 (A = 1, B a 7-term polynomial).

## (4) Formal budget-exhausting state: SOUND, formal only (check4.py, check4.log)
 Message: "This is a formal state only, with no actual body or covering knot asserted." Note section 5: "only a formal lattice
 state, not an actual body or a counterexample knot". No realisation is claimed anywhere.
 Exact (60 trials, s = (-t)^mu, E = (t+1)^k Phi6 Phi10 * (random binomial), support of sCE centred on 0): A = 1 + sCE, B = CE,
 A - sB = 1, gcd(a,c) = gcd(A,B) = 1, a = 1 mod (t+1)^k, eps = b(-1) = +1, and at m = -mu: kappa = 0, m = nu_0 z = -nu_inf z,
 unit with H = tau0 + tauinf: 60/60 each.
 Gate survey of actual bodies (561, exact residues mod Phi_n): universal facts a = 1 mod (t+1)^2, a(1) = a(i) = a(zeta6) = 1,
 b(1) = 1, b(zeta6) = eps (equivalently A(zeta6) = 1 if eps = 1, 0 if eps = -1), A(1) = A(i) = 1, c(-1) in {0,-1}; b(i), a(omega),
 a(zeta10) are NOT constrained (mostly non-unit residues). Codex's E satisfies every one of these universal gates (eps = +1 class),
 so no surveyed finite scalar evaluation separates the formal fibre from actual bodies. (With Codex's E, b(i) and a(omega) take
 arbitrary values; adding Phi3 Phi4 to E sets them to 1 if ever wanted.)

## Not refereed here
 Message section 5 (M300/D36 status, ARB-2 scope, V3 n = 0 hand proof, N-INF wording) was outside this task.
 A file NOTE-from-integrator.md appeared in this folder at 07:49 asking to include "ARB-IDEAL" (ideal I(v) = (a,c) invariant under
 F_m, Y^N; I(v*w) in I(v)I(w); N-INF family zero mod (7, t-2)) if time allows. Not done: it is outside the computed task and arrived
 as a file note, so it is flagged for the coordinator instead. Overlap: invariance of (a,c)-content under F_m, Y^N and integrality
 of the star product in (a,c) coordinates are covered by (1)-(2) above; the ideal containment and the mod-7 evaluation were not run.

## Files
 common.py (helpers, library), check1.py/.log, check2.py/.log, check3.py/.log, check4.py/.log, content_census.py/.log,
 nearmiss.py/.log. Total run time about 3 minutes.
