# R2 referee notes: sections 7-8 of skein_dictionary_arbitrary_boxes.md (outer map, vertical formula)

17 Nov 2026. Scripts and logs are in this folder. Run them from here with tools/venv/bin/python.
Own view formed before reading Codex's internal notes. Those notes agree with it.

## Verdicts
- 7a. Nested-cap slide gives X^-m p up to a common unit: SOUND. The raw TL3 state of
  N=r2.(y1)^m.B1..Bn.u1 is exactly A^(8m) X^-m (raw product), in both channel coordinates.
  Checked on 42/42 cases (t3_outer_raw, 12+30). The only "ribbon unit" is the crossing
  normalisation A^(8m). The slide is a planar isotopy. X^-1 rather than X is forced by the
  eigenvalues, because the raw y band crossing has A^8 on the cap channel.
- 7b. F(-1)=1, F'(-1)=2m(1-eps) and v_outer=t^(2m(1-eps)) X^-m p: SOUND. This is conditional
  on Section 5 (p2 in Lambda) and Section 6 (p2(-1)=(eps-1)/2). I re-derived the first row
  (value 0 and derivative -4m at -1).
  - Exact unit, no normalisation: 110/110.
  - Full vector of N, computed independently: 110/110.
  - Depth-2 necklaces: 110/110 (t5).
- 7c. Stacking preferred bodies stays preferred, eps multiplies, and the outer map keeps eps:
  SOUND. Product law v(B1.B2)=v(B1)*v(B2) holds exactly 25/25. eps(v_N)=eps(p)=prod(-1)^n0
  holds 110/110. Parity holds for 50/50 bodies (29 with eps=-1).
- 7.2. Necklace functional: SOUND. Norm(e1^T X^-m p)=lp.J on 110 necklaces of non-rational
  bodies (n=1..3, m=+-1..+-3).
- 8a. Eigenvalues 1,-t,t^3 and F_a=sum lambda_c^a K_c for every integer a: SOUND. The raw
  identity A^(8a)<Theta_a>/Delta2 = sum lambda^a K_c(a_raw,b_raw) holds exactly:
  - 675/675 (75 bodies x a=-4..4, odd and even);
  - 32/32 at a=+-5,+-6 (t2_all, t7).
  Body amplitudes come from an independent TL3 sandwich. Theta is computed by a direct
  colored evaluator (r2lib.theta_eval), with f2 on the arc and on the loop.
- 8b. Prism zeros K0~A0, K4~B0: SOUND. One sentence is not written: each triangular face lies in
  a ball that meets the graph only in its three rungs. This holds because the part above B and
  the twist is planar. Perturbed zero patterns fail 0/60.
- 8c. Zero-twist partial trace F0=A0+(t+1/t)B0: SOUND, 75/75 exact. F0 is a colored-skein value
  with a closed color-2 loop. lp/flat_search's raw y leaves that loop UNCOLORED (identity body
  a=0: delta^2 instead of Delta2), so lp cannot test even a. This is not a counterexample.
- 8d. Empty-axis bubble, giving K_c(1,1)=Delta_c/Delta2, in the SAME marking as 8c: SOUND.
  Direct colored bracket for s.l1.(x2)^a.u1, a=-3..3 (t1):
  - planar theta = Delta2;
  - F_a(I)=sum lambda^a Delta_c/Delta2 exactly;
  - F_0(I)=Delta2=1+(t+1/t);
  - Delta2*y_flat=<Theta> for every a.
- 8e. K0,K2,K4 as stated and F_+-1(I)=t^(+-4): SOUND. The system has a unique solution (4
  unknowns, 4 independent equations, plus 1 consistency equation). Computed directly,
  F_1(I)=A^16 and F_-1(I)=A^-16. Norm(formula)=lp.J on 255/255 odd-a vertical closures
  (50 non-rational, 13 rational and 22 nested bodies; a in +-{1,3,5,7}). Three perturbed formulas
  match 0/60.
- Corollary S remark ("same bubble ... chirality retained"): GAP (minor, repairable). The note
  does not prove it for general K#K. The missing paragraph is: S is h-invariant, h|S is a
  reflection fixing the axis, K meets S in the two fixed points, so S/h is a disc bounded by the
  axis and meeting k only at the vertices. I checked that this argument holds. The chirality is
  quoted, not re-derived.

## Upstream (R1 scope, numerically consistent here, not proved by these checks)
- Dictionary (2.1). Delta2*y_flat = <Theta> holds on:
  - s.B for all 75 bodies;
  - 60 vertical closures plus the identity family.
- Section 4 identification of (H, X, e1). Confirmed at the raw level (7a).
- Section 5. v2 is in Lambda for every body computed, and delta divides c_e.
- Section 6. Parity holds 50/50 and 110/110.
- The independent body vectors equal the general_boxes.json pinned vectors 50/50.

## Mismatches
None. Controls:
- The X^{+m} control matched lp.J only 1/20 times. That body has v2=0, a local-knot body with
  state a*Id, which X fixes.
- The wrong-unit control matched 0/20.

## Files
r2lib.py (evaluator), tlib.py, t1_identity, t2_bodies/t2_all, t3_outer_raw, t4_vertical_lpJ,
t5_necklace_lpJ, t6_controls, t7_bigA (each .py has a matching .log).
