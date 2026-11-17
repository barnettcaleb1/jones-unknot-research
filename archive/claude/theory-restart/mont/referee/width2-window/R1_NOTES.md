# R1 referee: WIDTH2-WINDOW and AMPHI-PAIR (Codex msg 20261117-022221)

Proof read: work/theory_restart/two_ended_potential_referee.md sections 2-3. Codex files untouched.
(r2_* files in this folder belong to a different referee and are not part of R1.)

## Verdicts
- (a) Window theorem |m|<=3B or |n|<=3B: SOUND.
  - Same-sign case: 00 is the unique bottom and 44 the unique top, so span >= 6(|m|+|n|)-W.
  - Opposite-sign case: the walls are N-2M=u42-u20 and M-2N=l02-l24. They cannot both hold, because 3M=-(2d+e).
  - On (U) the 02 packet is isolated (needs M>3W) and 24 is the unique bottom, so span >= 3M-3W. (L) is symmetric.
  - The written proof only needs M,N>3B, that is |m|,|n|>1.5B. So C=3B has a factor 2 of slack.
  - Units with min(|m|,|n|)=B do exist, at (3W/2,-W) for every even W tested. The optimal constant is therefore in [1,1.5].
  - Example (W=2, D=1): p00=3t^2, p02=-4, p20=4+t+4t^2, p22=-3, p24=4t^2, p42=1, p44=-p20. Then F(3,-2)=t^14.
- (b) Line step: SOUND.
  - Aggregating gives g0, g1, g3 (slopes 0, 2, 6). One surviving group means the whole line is units or none is.
  - Two or more surviving groups give |m| <= floor((W_line+S_D)/2), and W_line <= W+6|n0| <= W+18B.
  - The final square is |m|,|n| <= 10B; with the sharper 1.5B window it would be 5.5B.
  - The template constants 268 and 201 match the formula.
- (c) AMPHI-PAIR: SOUND within its stated scope.
  - delta(Q)=2delta(q) and sigma(Q)=2sigma(q); delta is even for any product of pairs.
  - The pole has delta*=-3 for |mu|=1 and -1 for |mu|>=2.
  - A two-ended first-order tie would force delta(B/A)=delta*. That is impossible by parity.
  - Scope: horizontal closures with mu!=0, a top-level product made only of mirror pairs, and two-ended ties only.
  - It does NOT apply to:
    - vertical closures: delta*_V=-|a|-1 is even for odd a;
    - bodies with any unpaired odd-delta factor;
    - one-ended (clean-end) units.
  - The geometric mirror (x<->y swap) gives q(mirror)=q(1/t) exactly (300 rational boxes). The 2x2 rigidity argument then extends this to all boxes.

## Numerics (all exact, rational arithmetic)
- wbf.py: brute-force unit detector. It is cross-checked against direct numerator construction at 60k points with 0 mismatches.
- exhaustive.py / run_exhaustive.py: an exact linear-algebra decision of whether ANY table with supports in [0,W], all six boundary sectors nonzero and a unit at (m0,n0) exists.
  - Ranges: W<=8, 10 choices of D (span 0..6), all off-axis targets with |m0|,|n0|<=3B+3.
  - Result: 90 profiles, 0 violations (exhaustive_W8.log/json).
  - construct.py and construct2.py validate the decision both ways (262 positive cases realised; 403 units recovered, none missed).
- run_families.py: 1,270 random and adversarial tables, with brute force over |m|,|n|<=10B+max(5,B).
  - Checks: window, line dichotomy, line bound and 10B square. 0 violations (families_2026.log).
- run_lines.py: 2,646 generic tables with units planted on axis lines up to 6 beyond the bound. 0 violations.
  - 432 targets beyond the bound are feasible. Every one is realised only as a one-group whole unit line (lines_3.log).
- amphi_check.py: pole spreads, delta/sigma doubling, parity of products, mirror relation, and the vertical-closure contrast.
