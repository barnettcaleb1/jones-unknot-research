# Referee notes: TWOBRIDGE Theorems A and B, role = independent computation

Target: mech2/twobridge/REPORT.md sections 2 and 3 (THEOREM A: matrix formula for J of side-preserving two-bridge
inversions; THEOREM B: J is never a unit for a non-trivial knot of the class).
Referee scripts and kht++ working folders: mech2/verify/twobridge-compute/ (all scripts are my own; the lens's scripts in
mech2/twobridge/scripts were not run and not imported).
Notes are appended as the work proceeds. Marks: [OK] verified by me, [MISMATCH], [GAP], [NOTE].

## 0. Setup (16 Nov 2026)
- Read BRIEF2.md, REPORT.md sections 1-4, tools/gtilde.py (function jset), lit/kht/REPORT.md (kht++ conventions).
- J from saved data: b-generators = {(24j+2k, 4j)} + {(c+4, d-1), (c-4, d) : special at (q,delta) = (c,d)},
  h = q/2 - delta, J = sum (-1)^h t^(q/2) (t = q^2), then normalised by a unit.

## 1. TASK 1: saved kht++ data against the matrix formula  [OK, no mismatch]
Script: twobridge-compute/task1.py (library twobridge-compute/reflib.py, all my own code).
Three independent legs for every record whose half-diagram word is s.<l1|r1>.<letters y0,x0,x1,y1>.u2:
  (D) J from the saved Kh~ components (b-generator rule, re-implemented from the description in the task);
  (M) the matrix formula (1 0) rho(L_m)...rho(L_1) (1 0)^T, L_1 = first letter after the cap;
  (K) my own Kauffman-bracket evaluation of the kht++ quotient tangle (Tangle::quotient re-implemented from
      Tangles.cpp:967; planar-matching state sum; J = coefficient of the horizontal tangle e_0, t = A^-4).
      Leg (K) does not use kht++ output at all; it tests the b-generator rule and the formula separately.
Dictionary letter -> matrix, worked out on 3_1, 4_1-1, 4_1-2 and then frozen:
      y0 -> rho(Y),  x0 -> rho(Y)^-1,  x1 -> rho(X),  y1 -> rho(X)^-1      (cap l1 or r1: no effect on J).
Result (comparison of coefficient vectors after normalising by a unit +-t^n; NO use of t <-> 1/t was needed):
  - records with a two-letter word: 305 (k138: 90, tilt/run_3_45: 215); 3 of them have no saved Kh~ (timeouts
    b37_18-2, b37_36, b39_2-1) -> 302 compared.
  - (D) = (M): 302 of 302.   (D) = (K): 302 of 302.   (K) = (M): 302 of 302.   Mismatches: NONE.
  - breakdown: k138: 80 mixed-sign words + 10 one-signed, all non-trivial; tilt: 180 non-trivial one-signed
    + 32 words of the form Y^n or y^n (J = 1, dim N = 1: the mislabelled trivial tangles). 231 distinct words,
    174 distinct normalised J, word length up to 19, dim N up to 55.
  - 61 words end in Y or y (so "Y on the right is trivial" is exercised by the data); NO saved word starts with
    X or x (so "X on the left is trivial" is not tested by the saved data; tested separately below).
  - sanity of leg (D) outside the class: for the 44 other k138/tilt records with a standard Kh~ record and at
    most 14 letters, (D) = (K) as well (0 disagreements). So the b-generator rule reproduces the e_0-coefficient
    of the Kauffman bracket of the quotient tangle in all 346 records tested.
[NOTE] The report's count "130 tangles: 24 positive and 16 mixed own runs and all 90 table entries, 80 of them
mixed" is consistent with what I see for the table (90 two-letter entries, 80 mixed). Its 40 own runs were not
re-examined (I did not open the lens's cache).

## 2. Exact check of the FORMULA of Theorem A, independent of kht++ and of the report's proof  [OK]
Script: twobridge-compute/thmA_exact.py.
Model: J(T) = coefficient of the horizontal crossingless tangle e_0 in the Kauffman bracket of the kht++ quotient
tangle (up to a unit; kht++ letter conventions <y_i> = A + A^-1 U_i, <x_i> = A U_i + A^-1, t = A^-4; this is the
decategorification of N(T) and agrees with the saved Kh~ data on all 346 records of section 1).
For a two-letter half-diagram everything happens on the 5 crossingless matchings of {top,0,1,2,3,4}:
E_1 = (top 0)(1 4)(2 3), letters Y = y0.y1.y1.y0, Y^-1 = x0.x1.x1.x0, X = x2.x1.x3.x2, X^-1 = y2.y1.y3.y2 as 5x5
matrices over Z[A,1/A], functional phi = (cup u0, coefficient of e_0). With f(w) = phi(w E_1):
   f(w) = c(w) * (1 0) rho(L_m) ... rho(L_1) (1 0)^T,   c multiplicative, c(Y) = A^-8 = t^2, c(X) = A^8 = t^-2,
 - verified exactly on all 2047 positive words of length <= 10 and on all 21845 words in X, Y, X^-1, Y^-1 of
   length <= 7 (0 failures);
 - this is a PROOF of the formula for all words: f/c - g is a matrix coefficient of a representation of dimension
   <= 5 + 2 = 7, the spans S_n of {R(w) v_0 : w positive, |w| <= n} stabilise at n <= 6, the stable span is invariant
   under the inverses as well, and the identity holds on all 127 positive words of length <= 6.
So the formula of Theorem A, with the dictionary y0 -> Y, x0 -> Y^-1, x1 -> X, y1 -> X^-1 and with exactly the
matrices rho(Y) = [[1,0],[t^-3,t^-3]], rho(X) = [[1,1-t^4],[0,-t]], is CORRECT for the kht++ quotient tangle of
s.<cap>.w.u2 for every word w. (This does not referee the report's own proof, steps (a)-(e); it replaces it by a
finite exact computation. The report's proof quotes the twist eigenvalues from memory and fixes the handedness
"by the kht++ trefoil"; the computation shows that the outcome is right.)
All five matchings occur in the orbit of E_1 (the orbit is not confined to a 2-dimensional subspace; the 2x2
formula is a quotient statement, as the report says in step (b)).

## 3. TASK 2 (part A): all freely reduced words in X, Y, X^-1, Y^-1  [OK up to length 13; length 15 running]
Scripts: twobridge-compute/task2.py, detcheck.py.  Log: twobridge-compute/task2_len13.log.
For every freely reduced word w (first letter nearest the cap) I computed, with exact integer arithmetic,
   g(w) = (1 0) rho(w) (1 0)^T,
   U(w): g(w) is a unit +-t^n,
   D(w): det K_w = 1, where det K_w = |(1 0) D(L_m)..D(L_1) (1 0)^T|, D(Y^e) = [[1,0],[-e,1]], D(X^e) = [[1,-2e],[0,1]]
         (validated against the Kauffman bracket at A = exp(i pi/4) of the FULL symmetric knot diagram, built by my
         own code from the half-diagram, on all 21845 words of length <= 7: 0 mismatches). K_w is a two-bridge
         knot, so det K_w = 1 iff K_w is the unknot,
   N(w): my own normal form in Z/2 * Z (X = e.Y, X^-1 = Y^-1.e in word order, e.e = 1, trailing Y-power dropped) is
         empty, (0,1,...,1) or (-1,...,-1), i.e. w lies in <X><Y> modulo the centre (the report's "trivial" words).
Result, lengths 0..13, 3 188 645 words:  U(w) <=> D(w) <=> N(w) for EVERY word (84 977 words have all three, the
other 3 103 668 have none). No counterexample to Theorem B.
In the same run, for every word: span_t g(w) = the report's formula (sum of c_i over the stripped normal form:
c_0 = 3 n_0 + 1 for n_0 >= 1, 3|n_0| - 2 for n_0 <= -2, c_i = 3|n_i| - 2 + 2[sign n_i != sign n_{i-1}]), 0 failures;
both extreme coefficients of g(w) are +-1, 0 failures.
(Stripping = removal of the degenerate prefix: F(0,n_1,n_2,..) = F(n_1 - 1, n_2,..), F(-1,n_1,..) = t^4 F(n_1,..);
both identities checked by hand from the matrices. The report does not spell this out; see section 6, note N2.)
