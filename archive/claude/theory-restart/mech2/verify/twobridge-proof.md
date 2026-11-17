# REFEREE NOTES: twobridge/REPORT.md sections 1, 2.2, 3 (Theorem A, Theorem B)

Referee: independent proof referee (written as I go; scripts and kht++ working folders in verify/twobridge-proof/).
Target: /Users/calebbarnett/jones-lanes/theory-restart/mech2/twobridge/REPORT.md, sections 1, 2.2, 3.
Convention in these notes: "OK" = I re-derived or recomputed it myself; "NOT CHECKED" = taken on trust; "ISSUE" = something wrong, missing or overstated.

## 0. Reading (done)
Read BRIEF2.md and the whole of REPORT.md (sections 1-8 and SUMMARY). Statements under review:
- 1.1-1.3 topology of the quotient tangle, the picture T_w (6 boundary points, braid w in Y, X, closing arc (c_1, m_1^-)).
- 2.2 J = (1,1,2)-coloured theta evaluation; 2-dimensional space H = Hom(V_1, V_1 (x) V_2 (x) V_2).
- Theorem A: J(T_w) = unit * (1 0) rho(L_m)...rho(L_1) (1 0)^T.
- Normal form F(n_0..n_{k-1}), E = rho(Y)^-1 rho(X), E^2 = t^4, trivial words.
- Theorem B: non-unit, extreme coefficients +-1, span formula, automaton P, Q_m, U_m, R, S_j.
- SCOPE: which strong inversions of two-bridge knots are some T_w.

## 1. Algebra of Theorem A (e), the normal form, and Theorem B: recomputed (scripts a1_matrices.py, lp.py, a4_automaton.py, a5_span.py, a7_words.py)

All arithmetic exact (sympy for identities, my own integer Laurent-polynomial code for the sweeps; none of the author's code is imported).

1.1 OK  rho(Y)^-1 = [[1,0],[-1,t^3]], rho(X)^-1 = [[1,(1-t^4)/t],[0,-1/t]]; E = rho(Y)^-1 rho(X) = [[1,1-t^4],[-1,-1]]; E^2 = t^4.
1.2 OK  Step (e). For X = [[1,xi],[0,lam]], Y = [[1,0],[eta,mu]]: Y X^-1 = [[1,-xi/lam],[eta,(mu-xi eta)/lam]], trace = (lam+mu-xi eta)/lam.
        A 2x2 matrix with scalar square is scalar or has trace 0 (Cayley-Hamilton); Y X^-1 is never scalar (if xi = eta = 0 it is diag(1, mu/lam)
        = diag(1,-t^-4)), so xi eta = lam + mu = -t + t^-3 = t^-3(1-t^4), as claimed. (The report says "it is not scalar" without the one-line reason; fine.)
        Braid identity used: (sigma_1^2 sigma_2)^2 = sigma_1 Delta sigma_1 sigma_2 = Delta sigma_2 sigma_1 sigma_2 = Delta^2. OK.
        Direct check: (rho(Y) rho(X)^-1)^2 = t^-4.
1.3 OK  One-block formula J(Y^a X^b) = 1 + t^-3 [a]_{t^-3} (1-t^4) [b]_{-t} for 1 <= a,b <= 5.
1.4 OK  Mirror: D rho(y) D^-1 = rho(Y)(1/t), D rho(x) D^-1 = rho(X)(1/t) with D = diag(1,-t^3) (the report's "conjugation by diag(1,-t^-3)" is the
        same statement read in the other direction). Hence J_{w^-}(t) = J_w(1/t) exactly (w^- = every letter inverted, order kept).
        The identity for F: E(1/t) ~ t^-4 Y E Y^-1 under the same conjugation, giving F(n_0,..,n_{k-1})(1/t) = t^{-4k} F(-n_0-1,-n_1,..,-n_{k-1})(t):
        re-derived by hand and verified on 46810 normal forms (k <= 5, |n_i| <= 4, n_0 in [-5,4]): 0 failures.
1.5 OK  Normal form. rho(X) = rho(Y) E, rho(x) = t^-4 E rho(y); E E = t^4; (1 0) rho(Y)^n = (1 0); rho(X)(1 0)^T = (1 0)^T. My own rewriting routine
        reproduces J_w = t^texp F(n_0..n_{k-1}) EXACTLY for all 349525 words of length <= 9 in Y, X, y, x (unreduced words included).
        Only the relation "e^2 central" is used, a true relation in B_3; uniqueness of the normal form is not needed for Theorem B.
1.6 OK  Automaton. For every normal form with k <= 5, |n_i| <= 4 (46810 forms) I tracked v = (v_1,v_2) exactly and read off (deg, lc) of r = v_2/v_1
        before and after every E-step. Observed transitions (state after previous E | Y-exponent | state before E | gain | state after E):
            R   | n>0  | P    | 1    | R            R   | n=-m | U_m     | 3m+3 | S_0
            S_j | n>0  | P    | 1    | R            S_j | n=-m, m>=2 | Q_m | 3m+1 | S_0        S_j | n=-1 | Q_1 | 4 | S_{j+1}
            START | n>0 | P | 1 | R                 START | n=-m, m>=2 | Q_m | 3m+1 | S_0       START | 0 | r=0 | 0 | r=-1      START | -1 | r=-1 | 4 | r=0
            r=-1 | n=1 | r=0 | 0 | r=-1             r=-1 | n>=2 | P | 1 | R                     r=-1 | n=-m | Q_{m+1} | 3m+4 | S_0
            r=0  | n=-1 | r=-1 | 4 | r=0            r=0 | n>0 | P | 1 | R                       r=0 | n=-m, m>=2 | Q_m | 3m+1 | S_0
        No state outside the report's list occurs; the list {P, Q_m, U_m | R, S_j | r = 0, r = -1} is closed under Y^n (n != 0) and E.
        The exact states r = 0, r = -1 never occur after a generic step (0 occurrences), because after a generic step r is R or S_j and
        Y^n of those is P, U_m, Q_m (m >= 2) or Q_1 = -1 + rho with rho = t^3 r_old != 0.  I also re-derived every row by hand (degrees of the
        two competing terms: -3 vs -1-3n or -4-j-3n; 3m-3 vs 3m-1 or 3m-4-j; 4 + deg r vs 0 with deg r in {-3} u [0,inf)): no ties. OK.
        ISSUE (minor, presentation): the report lists the sources of Q_m as "after Y^-m from S_j or from the start" and gives no transitions out
        of the exact post-states r = 0 / r = -1. The rows "r=-1 | n=-m | Q_{m+1}" and "r=-1 | n>=2 | P", "r=0 | ..." are missing from the text
        (they are in the author's script span_check.py). They stay inside the state list, so the proof is unaffected.
1.7 OK  Leading coefficient of v_1 is +-1 at every step (asserted in the sweep); extreme coefficients of F are +-1 for all 46810 forms and for
        all 232020 non-trivial words of length <= 9.
1.8 ISSUE (correction to the statement of Theorem B): the printed span formula
            span J = sum over generic steps of c_i,  c_i = 3|n_i| - 2 + 2[sign n_i != sign n_{i-1}] (i >= 1), c_0 = 3n_0+1 or 3|n_0|-2
        is correct for normal forms WITHOUT a degenerate prefix (n_0 not in {0,-1}): 0 mismatches. It is WRONG for forms with a degenerate
        prefix, under either reading of sign(0): 5344 of 9362 such forms fail (e.g. F(-1,1) = t^4 F(1): span 4, formula 3; F(0,-2): span 7,
        formula 6). Reason: the first generic step after a degenerate prefix starts from the exact state r = 0 or r = -1, where the gains are
        those of an initial step (from r=-1, Y^-m gives Q_{m+1}, gain 3m+4, not 3m+1). Fix: strip the prefix first, using
        F(0,n_1,n_2,..) = F(n_1 - 1, n_2,..) and F(-1,n_1,n_2,..) = t^4 F(n_1,n_2,..) (both verified: E e_1 = rho(y) e_1, E rho(y) e_1 = t^4 e_1),
        then apply the formula. The qualitative statement is unaffected: every generic step contributes >= 1 in all cases (hand check of the four
        prefix cases: 3n-2 (n>=2), 3m+1, 3n+1, 3m-2 (m>=2)); in the sweep, span >= (number of generic steps) + 3 whenever there is a generic step.
1.9 OK  Positive block words Y^{a_1}X^{b_1}...: span 3A+B, top (-1)^B t^B, bottom t^{-3A} for all 4368 words with <= 3 blocks, exponents 1..4.
1.10 OK "Which words give the trivial knot". With the integer matrices Y -> [[1,1],[0,1]], X -> [[1,0],[2,1]] (so (Y X^-1)^2 = -1; these generate
        Gamma_0(2), and PGamma_0(2) = Z/2 * Z), the first column of the matrix of w is (p,q)^T with p/q = [a_1, 2b_1, a_2, ...]. For all 349525
        words of length <= 9: J_w monomial <=> |p| = 1 <=> the normal form is all-degenerate ((0,1,..,1), (-1,..,-1) or k = 0).
        By hand: all-degenerate sequences are exactly rho(Y)^* rho(X)^k (k >= 0: (0,1,..,1)) and rho(Y)^* rho(X)^-k ((-1,..,-1)), i.e. w = X^k Y^*
        modulo the centre; and |p| = 1 <=> M_w e_1 = +-X^b e_1 <=> M_w in +-X^b <Y>. So "T_w trivial <=> w in <X><Y> (mod centre) <=> all steps
        degenerate" is right, and Theorem B only needs the easy direction (all-degenerate => w = central * X^k Y^n as a braid => K unknot).

