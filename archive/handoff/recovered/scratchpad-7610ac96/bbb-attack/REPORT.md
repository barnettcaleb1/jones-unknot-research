# BBB (arXiv:2607.05283v2) unmodified-push check -- work record

Everything here is reproducible from `scripts/` (pure Python 3.13 + numpy/scipy/PIL/pymupdf; exact integer arithmetic).
Paper PDF and the figure PNGs extracted from it are under `paper/` (treated as data).

## Scripts
- `scripts/braidarc.py` -- exact model: free group + Artin action, cutting sequences w.r.t. the horizontal diameter,
  Moody polynomials (1 and 2 variables, canonical lift at p*), disk sequences, planar faces/winding numbers,
  push maps (nested basis Y_k), Fox/Burau. `python3 braidarc.py` runs a 600-case random self-test.
- `scripts/trace_fig.py` -- raster tracer for the paper's figures (dots -> punctures, colour mask -> Zhang-Suen
  skeleton -> walk -> cutting sequence). Outputs in `traces/*.json`.
- `scripts/validate_section7.py` -- the whole pipeline against the paper's Section 7 (log: `results/validate_section7.log`).
- `scripts/construct_gamma.py` -- unmodified Prop 6.7 push (q, gamma_1 with the wall beta*_3, gamma_2 through the band);
  on the paper's example it reproduces the paper's own Gamma word exactly (q = face ('L',1)).
- `scripts/size_and_facts.py`, `scripts/small_candidate.py` -- exact Burau facts, candidate ranking, Phi_0 arc census
  (logs/json in `results/`). `scripts/main_phi.py` is the full pipeline for Phi (NOT feasible, see obstacle).

## Conventions (fixed and verified against Section 7)
sigma_i = counterclockwise half twist (p_i passes below p_{i+1}); braid words act on arcs left to right ((beta)g1g2);
x_j = ccw loop from p* (bottom) around p_j; sigma_i: x_i -> x_{i+1}, x_{i+1} -> x_{i+1} x_i x_{i+1}^{-1}.
Moody exponent: passing clockwise over p_j adds +1 (paper's Lemma 3.1 sign); epsilon = +1 for a downward crossing of alpha.
With these, the exponents of the Section 7 polynomials are reproduced exactly; the paper's listed global signs are the
negatives of the literal epsilon-convention (M is only defined up to +-t^k).
Burau: Fox Jacobian with phi(x_j) = t^{-1}, rho(g1 g2) = rho(g1) rho(g2); class of (beta*_3)Phi = row 3;
<loop, alpha~> = -rho_31 + t^{-1} rho_32 = (1 - t^{-1}) M_arc.

## Words
y1 = s3^2, y2 = s3 s2^2 s3, y3 = s3 s2 s1^2 s2 s3 (ccw nested loops of p4, top first, Fig 6.13).
Gamma_1 (Fig 6.3, traversed as the arrow shows, leaving p4 into the lower half-disk): cutting sequence
[1,3,2,1,3,1,0,3,1,2,3,1]; word y2^-1 y1^-1 y2^2 y3^-1 y2^-1 y1 y2 (a conjugate of y3^-1; begins with y2^-1 as the paper says);
braid = Push of that word (30 letters, in results/size_and_facts.json: Gamma1_braid).
Phi_0 = [(s1 s2)^6, [[A14,A24],A34]], A_ij = s_{j-1}...s_{i+1} s_i^2 s_{i+1}^-1...s_{j-1}^-1 (112 letters);
in the y-basis (30 letters): y3^-1 y1^-1 y2 y3^-1 y1 y2^-1 y1 y2 y1^-1 y3 y2^-1 y1 y3^-1 y1^-1 y3^2 y1 y3 y1^-1 y2 y3^-1 y1 y2^-1 y1^-1 y2 y1^-1 y3 y2^-1 y1 y3^-1.
m = 31; Phi = Gamma_1^-1 y1^31 Phi_0 y1^-31 Gamma_1 (all three juxtapositions freely reduced; braid length 300).

## Exact facts
- rho_4, rho_5 of Phi_0 and of Phi: identity at t = -1, not at t = 2 (and Phi_0 Brunnian by strand deletion).
- Exact-Burau coefficient sums: Phi_0 1.26e7 (row 3: 4.26e6); Phi 1.55e11 (row 3: 7.67e10); Gamma_1 288.
- (beta*_3)Phi_0: cutting sequence 6,842,015; iota(alpha, beta) = 976,672; disk census
  {p4}chg 358288, {p1,p4}prs 260096, {p1,p2,p4}chg 228241, {p3}chg 127391, {p1,p2,p3,p4}chg 2655 (the only parity
  violators = 2655 nested 4-disks); M_{Phi_0}(-1) = 0 exactly (488336 '+' and 488336 '-' in M(-t)); simplified M_{Phi_0}
  in results/size_and_facts.json.
- Smallest Brunnian cap BI_4 candidate found: [(s2 s3)^6, [A14,[A24,A34]]] (coefficient sum 100,802); but every
  proper-product conjugate Gamma_1^-1 y1^m (.) y1^-m Gamma_1 has coefficient sum >= 7.9e6 (row 3 >= 3.7e6), i.e. iota ~ 1e6.
- Paper's Section 7: M_Phi and M_{Phi.Gamma} reproduced term by term; M_Gamma: the figure (and the braid) give the 19th
  and 20th terms as t^-4, t^-2 (paper lists t^-2, t^0): simplified -t^-5+2t^-4-3t^-3+4t^-2-4t^-1+3-2t+t^2 (up to +-t^k).
- Two-variable (weights t,t,t,t,u) for the paper's example: results/two_variable_example.log (D(t,u), u-levels {-1,0},
  six collisions under u = t).

## Obstacle
iota(alpha, (beta*_3)Phi) is of order 1e10-1e11 (exact Burau row sum 7.7e10), so beta cannot be tracked; Gamma (which must
run parallel to beta inside the innermost 4-disk) would have ~1e11 alpha-crossings. Every proper-product form found of any
Brunnian cap BI_4 element exceeds the 1e6 stop rule because conjugation by Gamma_1 multiplies the size by ~80.
