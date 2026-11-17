# BRIEF: necklace (equivariant Conway sphere) calculus for J of strongly invertible knots
Lane folder: ~/jones-lanes/theory-restart/mont/   (written 16 Nov 2026, Claude integrator)

## 0. Background you need (read, do not re-derive)
- Project: Jones unknot conjecture. For a strongly invertible knot K with inversion h, the quotient (S^3, K u Fix(h))/h is a theta-curve:
  axis (two edges, colour V_1) and the arc K/h (colour V_2, the spin-one / f_2-projected doubled strand). The quotient tangle T has
  bracket vector alpha[Q_0] + beta[Q_inf]; J(T) := alpha / (unit), normalised so that J = 1 mod (t+1)^2 (unique such unit multiple).
  "Flat" = J is a unit. LEMMA Q (target): J unit => K is the unknot (T rational). J''(-1) = -24 a_2(K) (a_2 = Conway coefficient).
- TH-2BR-A/B (PROVED by both agents; board THEORY-width-ladder.md X.21-X.22 in
  /Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/collab/): for standard side-preserving inversions of
  two-bridge knots, J = unit * e_1^T rho(L_m)...rho(L_1) e_1 with rho(Y)=[[1,0],[t^-3,t^-3]], rho(X)=[[1,1-t^4],[0,-t]], acting on
  H = Hom(V_1, V_1 (x) V_2 (x) V_2) (dim 2). Y = full twist of the adjacent (axis, arc) pair (eigenvalues 1, t^-3; left eigenvector
  e_1^T = colour-one fusion functional), X = half twist of the two arc points (eigenvalues 1, -t). E = Y^-1 X, E^2 = t^4.
  Automaton states R:(deg,lc)=(-1,1), S_j:(-4-j,(-1)^j); span formula after prefix normalisation; extremes +-1.
- Half-diagram words (kht++ format, 's.' prefix): strands to the right of a vertical axis; letters x_i/y_i = crossing of half-strands
  i-1,i (i>=1) or of strand 0 with its mirror (i=0, "axis crossing"); l_i/r_i = cap inserting new half-strands at positions i-1,i;
  u_i = cup joining half-strands i-1,i; implicit final u0 = bottom fixed point; the top fixed point is the start (one half-strand).
  Parser/symmetriser: ~/jones-lanes/theory-restart/tools/alex.py (parse, symmetrize, diagram, alex_poly). Bracket of the quotient:
  ~/jones-lanes/theory-restart/tools/flat_search.py (bracket_vector, gen = random words).
- Fast exact tools (pure Python, use these): ~/jones-lanes/theory-restart/mont/lp.py
  (Laurent polys as dicts; J(word) = normalised J or None if not a knot; a2(J); matrices Xm, Xi(=X^-1), Ym, Yi; apply('XXY') = X X Y e_1
  (last letter acts first); star(v,w); a_of, b_of; close(m,p) = e_1^T X^m p). Pretzel/necklace word builders: mont/words.py
  (row(r), mont(m,rows)). Use /Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python (sympy available there).

## 1. NEW (Claude, 16 Nov evening): THEOREM N, the necklace formula (strong numerical evidence, no written proof yet)
- A BOX is a ball B meeting the theta-curve in one axis string and one arc string, both running from the west pair (W axis, w arc) of
  the four points of dB to the east pair (E, e). Its state lies in End_{U_q}(V_1 (x) V_2) = C P_1 (+) C P_3, a COMMUTATIVE algebra.
  In TH-2BR coordinates a box has a vector v = (v_1, v_2) in Lambda^2 (Lambda = Z[t,1/t]); channel amplitudes
  a(v) = v_1 (P_1 channel) and b(v) = v_1 + (1 - t^3) v_2 (P_3 channel). Stacking boxes along a necklace multiplies channels:
      v * w = (v_1 w_1,  v_1 w_2 + v_2 w_1 + (1 - t^3) v_2 w_2)     [box ring R = Lambda[s]/(s^2 - (1-t^3) s) = {(a,b): a = b mod 1-t^3}]
- NECKLACE CLOSURE with m half-twists in the special region (the region containing both vertices):
      J = e_1^T X^mu (v_1 * ... * v_n)  (mu = -m in the half-diagram convention below)
        = [ (t + (1+t^2)(-t)^mu) A + (1+t^2)(1 - (-t)^mu) B ] / (1 + t + t^2),   A = prod a(v_i), B = prod b(v_i).
  mu = 0: J = A (equivariant connected sum, multiplicative). Twisted closures of one box: J = P + Q (-t)^mu (two channels, ratio -t).
- HALF-DIAGRAM REALISATION: s.r2.(y1)^m.B_1.B_2...B_n.u1 where each B_i is ANY half-diagram body (a word without 's.', it maps one
  half-strand to one half-strand). Sign dictionary (checked): y1 in the twist <-> X^-1 (mu = -m); x1 <-> X. Twist row with r = 2j+1
  crossings: (r1)^j.y0.y2.y4...y_(2j).(u1)^j has vector X^j Y e_1; its mirror (x letters) X^-j Y^-1 e_1.
  mont(m,[r_1,..,r_n]) builds the horizontal-axis inversion of the pretzel P(-2m, r_1, ..., r_n) (identified by Alexander polynomials:
  mont(1,[3,3]) = T(3,4) = 8_19, its J equals the k138 table J of 8_19 exactly; mont(1,[3,5]) = T(3,5); mont(1,[3,7]) = P(-2,3,7), det 1).
- EVIDENCE: 8/8 sign variants of P(+-2,+-3,+-3); 48/48 pretzel cases (rows up to 9 crossings, up to 3 boxes, m = -3..3);
  random non-rational boxes (flat_search.gen bodies): STRICT test test_general2.py: 50 boxes, each vector pinned uniquely by three
  twisted closures (m = 1, 2, -1), then 150 further single-box twists (m = 3, -2, -3) and 120 necklaces of 2-3 random boxes with random
  twists: ALL EXACT. Box vectors of these 50 boxes: mont/general_boxes.json.
- FORMULA SURVEY (survey_formula.py): 60,000 random Montesinos necklaces (2-4 non-integral rational boxes v = rho(w)e_1, w random
  words of length <= 7 in X,Y and inverses, twist mu in [-5,5]\{0}, integral part Y^k, k in [-4,4]): NO unit J; minimum span of J
  6 (n=2), 9 (n=3), 14 (n=4). Integral tangles act as Y^k (diagonal in the (a,b) basis: a -> a, b -> t^(-3k) b).
- Twist rows in closed form (r = 2j+1 >= 3): a_r = 1 + t^-3 (1-t)(1+t^2)(1-(-t)^j)  [= J(T(2,r)), top j coef (-1)^j, bottom -3 coef 1];
  b_r = t^-3 - t^-2 + t^-1 + (-1)^j (t^(j-2) - t^(j-1))  [top j-1, bottom -3 coef 1]; mirror rows: t -> 1/t (no unit shift).
- Examples: J(P(-2,3,7)) = -t^-20 + 2t^-19 - t^-18 + 2t^-16 - 2t^-15 + t^-14 (span 6); J(P(-2,3,5)) = t^-17 - t^-16 + t^-15 - t^-13 + 2t^-12 - t^-11.
- No-tie status: J * Phi_3 = w_1 A + w_3 B with w_1 = t + (1+t^2)(-t)^mu, w_3 = (1+t^2)(1-(-t)^mu). All-positive rows and mu >= 1:
  no tie at either end, span(J) = mu + sum j_i + 3n. But mu < 0 with positive rows (e.g. P(-2,3,7)) gives a tie WITH cancellation at the
  bottom (non-alternating case); mixed-sign rows also tie. The general no-tie lemma is OPEN.

## 2. Ground rules
- Write findings to your REPORT.md file CONTINUOUSLY as you go (usage limits have killed agents before; anything not on disk is lost).
- Definitions, statements with reasons, proofs or precise obstructions. Compute only cheap exact checks (pure-Python lp.py, seconds to
  a few minutes); no large sweeps, no kht++ runs unless your task says so. Mark every claim PROVED / CHECKED(n cases) / CONJECTURE.
- Do not contact anyone outside; do not edit files outside your own folder under mont/.
