# Width-two window referee R2: certificate replay

- Workflow: wf_c6df0491-3d8 (referee-width2-window-wf_c6df0491-3d8.js)
- Session: bridge session (Claude-Codex integrator)
- Launched (script written): 2026-11-17 02:24 local; journal last written: 2026-11-17 03:00 local
- Agents started: R1:proof, R2:certificates
- Results extracted here: R2:certificates
- Context: Launched 17 Nov 02:24. R1 wrote mont/referee/width2-window/R1_NOTES.md; R2 left only scripts and r2_all.log in the same folder. Its verdict text exists only in the journal.
- Provenance: contemporaneous agent outputs recorded in the workflow journal (runtime state, not copied). Text below is verbatim except formatting (JSON fields rendered as markdown), em dashes replaced by ' - ', email addresses redacted, and home-directory paths shortened to ~ (session scratchpad roots to <scratch>). These are internal AI agent outputs, not external review; statuses are as the agent stated them at the time and may be superseded by later board entries.


## Agent: R2:certificates


### verdicts

  -
    - claim: (a) Seven sector coefficients of both templates from rho2_matrices.json; E04=E40=0; F(m,n) agrees with lp.J on literal halfwords
    - verdict: SOUND
    - detail: Own code reads only rho2_matrices.json. X1,X3: x_i y_i=I, X1X3=X3X1, (X-1)(X+t)(X-t^3)=0, multiplicities 2,4,3; Lagrange projectors idempotent and complete; joint ranks exact by trace [[1,1,0],[1,2,1],[0,1,2]]; E04, E40 vanish identically as matrices. All 14 c_ab equal the exact_sectors.json strings (c42=-c44 in T1; c02=c20, c24=c42 in T2); denominators only t^a, t^2+1, t^2+t+1, so no pole at -1. sum c_ab t^q equals the direct letter-by-letter matrix action AND lp.J (independent flat_search path) on s.l1.l1.V.x1^(2m).x3^(2n).U.u2.u2 at 46 points, 23 per template, incl. negative m,n and (2,-7),(4,-22),(-4,-10). Codex's own scripts never compare with lp.J (they lean on engineB's rho2 validation); this closes that link.
  -
    - claim: (b) F0=1; F1=8m+8, a2=2m^2+3m+2n (T1); F1=8m+8n, a2=2m^2+3m+2n^2+3n (T2)
    - verdict: SOUND
    - detail: Per-sector (c,Dc,D^2c)(-1) recomputed symbolically: identical to the gate tables for both templates; F0=1 identically; F2 as stated. The a2 formulas agree with lp.a2(lp.J) at all 46 cross-check points. Logic: the gate needs only 'unit => M2=0', which is elementary (F(-1)=1 for all m,n; F=eps t^k gives F1=k, F2=k^2), so the banked a2 theorem is not load-bearing. All q_ab are even, so F1 is even and J=t^(-F1)F, matching lp.normalize.
  -
    - claim: (c) T1 integer core m=2k, n=-4k^2-3k; numerator table; target 16k+20; cases k>=1, k<=-2, k=-1,0
    - verdict: SOUND
    - detail: a2 = m mod 2 forces m=2k, then n=-4k^2-3k. d=t^8(t^2+1)(t^2+t+1) clears all seven c_ab into Z[t]; my min/max degrees and end coefficients equal the gate table row for row (00 top coeff -1); shifted tops and target 16k+20 confirmed. k>=1: all seven gaps positive (k=j+1 test); k<=-2: 00 strictly highest, target <= -12 (k=-j-2 test); also brute-checked from the table for |k|<=400. Independent J along the core k=-6..6 (|W| up to 357) by module matrix action and by lp.J: a2=0 throughout, only k=-1 gives J=1 (raw F=t^-8); k=0 gives J-1=-(t-1)(t+1)^3(t^2+1)(t^2-t+1)^2 Phi10/t^14 as claimed.
  -
    - claim: (d) T2 zero set (4m+3)^2+(4n+3)^2=18 has only (0,0); J(0,0)-1 = (t-1)^2(t+1)^3(t^2+1)(t^2-t+1)Phi10/t^11
    - verdict: SOUND
    - detail: 8*a2=(4m+3)^2+(4n+3)^2-18 checked symbolically. The conic is bounded: |4m+3|<=4 gives m in {-1,0}, and m=-1 needs (4n+3)^2=17, so (0,0) is the only integer point (Codex's square argument is equivalent). lp.J on s.l1.l1.y0.y2.y1.x0.x3.y2.y3.x2.x2.y3.x0.x1.u2.u2 gives J-1=(t-1)^2(t+1)^3(t^2+1)(t^2-t+1)Phi10/t^11 exactly, nonzero. Template 2 has no unit point.
  -
    - claim: (e) (-2,-1) reduces to y2.y2.y3.y3.x1; covering knot = L#rL, L the 4-plat (12/34; s2^-2 s3^-2 s1; 14/23); L unknot, det(L)=1
    - verdict: SOUND
    - detail: Mechanical reduction (free cancellation, far commutation incl. tau with s2,s3) gives y2.y2.y3.y3.x1; lp.J=1 on both words. No x0/y0 remain, so the plane through the axis meets K twice: K=L#rL. Swinging the outer arc (axis+strand c) over infinity gives bottom 14/23. My own plat code (not alex.py): L has 5 crossings, det 1, Alexander unit, bracket -A^3 at writhe 1 (V=1). Fraction: inf -s1-> -1 -s3^-2-> 1 -s2^-2-> -1, numerator closure N(-1) = unknot. With s1^-1 det would be 5, so the sign matters and is right. My 10- and 28-crossing symmetric covering diagrams: V=1, det 1, Delta unit. Codex minor det -1, PD bracket -A^3 confirmed. Nit: 'ordinary four-plat' has nested bottom; still 2-bridge.
  -
    - claim: Reproducibility of Codex's certificate scripts (width2_fixed_template_gate.py/.json, width2_source_geometry_check.py)
    - verdict: SOUND
    - detail: Reran both read-only (gate output redirected to my folder; Codex files untouched): every assertion passes and the regenerated JSON is identical to width2_fixed_template_gate.json. Scope: R2 did not referee section 2 (two-ended window theorem) or section 3 (AMPHI-PAIR).

### summary

No gap and no counterexample in the two fixed-template certificates. Independent recomputation from rho2_matrices.json reproduces all 14 sector coefficients, E04=E40=0 and the exact joint ranks; F(m,n) equals lp.J on literal halfwords at 46 points plus 13 core points. Moments, the T1 conic m=2k, n=-4k^2-3k, the seven-row degree table and k-case split, the T2 conic with only (0,0), and both J-1 factorizations check exactly. Along the T1 core (k=-6..6, lp.J) only k=-1 gives J=1. (-2,-1) reduces to y2.y2.y3.y3.x1. No axis crossings remain, so K=L#rL. L has det 1, V=1 and rational fraction -1: it is the unknot, so K is too. Only remark: Codex's scripts never tie the table to lp.J (they rely on engineB's rho2 validation); R2 closes that link. Scripts and logs: ~/jones-lanes/theory-restart/mont/referee/width2-window/ (r2_*.py, r2_all.log). Out of scope: the section 2 window theorem and AMPHI-PAIR.

### notes_path

~/jones-lanes/theory-restart/mont/referee/width2-window/r2_all.log
