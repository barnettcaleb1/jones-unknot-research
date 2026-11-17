# R1 referee: skein dictionary and root sign (note Sections 2-6)

17 Nov 2026. Referee of `work/theory_restart/skein_dictionary_arbitrary_boxes.md` (Codex 052407), Sections 2-6.
Formed my view and ran my own checks before reading Codex's internal reads (theta_dictionary_subproof,
box_root_sign_subproof, dictionary_skeptic, necklace_skein_referee). They agree with what follows; nothing in
them changed a verdict. Sections 7-8 belong to R2 and are not refereed here (one numerical bonus check of (7.1) is below).

Files (this folder is shared with R2 `r2/` and R3 `r3_*`; R1 files are the ones listed here):
- `refskein.py`: my own bracket sweep, ribbon doubling, explicit theta closures D_I/D_e, body TL3 expansion,
  macro (locality) sweep, Norm. It does not import flat_search, kauffman or lp.
- `check_dictionary.py/.log/.json`: dictionary on 46 words. `bodies.py/.json`, `check_bodies2.py/.log/.json`: 269 bodies.
- `regmodel.py` + `t_reg`, `t_root`, `t_regbodies`, `t_regconsist`, `t_closedcomp` (.py/.log): my implementation of the
  ft_integral regular model. `t_central.py/.log` (sympy algebra), `t_framing2.py/.log` (framing law), `t_macro` (locality validation).

## Verdicts

| claim | verdict |
|---|---|
| (a1) (2.1)-(2.2): <Theta;1,1,2> = L_b - delta^-1 L_c = Delta2 y; short closure delta u, long delta^2 y + delta x | SOUND |
| (a2) the project's evaluation is this one (cabling, vertex marking, local replacements) | SOUND |
| (b) Sec 3: y/u in Z[t^+-1], j0(-1)=1, Norm, uniqueness, no division by delta at delta=0 | SOUND |
| (c) Sec 4: H, and X, Y, v on all of H for arbitrary bodies | SOUND |
| (d) Sec 5: integral lattice, not circular | SOUND |
| (e) Sec 6: a(-1)=1, b(-1)=(-1)^w=(-1)^n0 for every actual body | SOUND |

Nothing FALSE. Below are the steps that are asserted rather than proved. Each needs at most one line or one
citation, and none changes a statement.

## (a) Dictionary

- (2.1) is bilinear algebra in TL2: pairing matrix [[d^2,d],[d,d^2]] in the basis (b,c). It is correct.
- **The marking in the code.** In `flat_search.quotient_word` the prefix `r1,r2` is the v_top vertex: the inner band strand
  meets A1 (position 0, top end T), and the outer strand reaches A2 by a spectator band at the far right. A2 is the
  axis through infinity, which lies in the outer face. The final `u0` is the v_bot vertex, with A1 meeting the inner strand.
  So c=(T b1)(b2 b3) is the short closure. It gives one loop, the axis with a finger along k (u = 1, writhe 0).
  b=(T b3)(b1 b2) is the long closure. It gives the two theta cycles A1 u k', A2 u k''.
- **Independent check (46 words).** The words are 8 two-bridge, 6 rational necklaces, 6 nonrational necklaces,
  4 depth-2 nests, 6 closures s.B of general_boxes bodies, 6 vertical closures, 2 swap words and 8 random fs.gen words.
  I built the closed diagrams D_I and D_e directly, with my own planar (1,1,2) vertices and A2 drawn separately, and evaluated
  them with my own sweep. Results:
  - (y,x) equals `flat_search.bracket_vector` exactly (no unit) in 46/46, and Norm(y/u) = lp.J exactly in 46/46.
  - Theta is divisible by Delta2 and u is a monomial in 46/46.
  - The turnback at v_top, at v_bot and at a random interior band point gives the same L_c in 46/46.
  - f2 duplication holds in 46/46: <(I - e_P/d)(I - e_Q/d)> = <(I - e_P/d)>.
- **The axis letter is a clasp.** The note asserts this; it is not derived there. The local quotient model
  w = (x+iz)^2 shows that k winds once around the axis at an on-axis crossing (over, U-turn, under). That is the full
  monodromy x0x1x1x0. Its chirality is the banked LP mirror convention. For N/O/V this construction is the definition
  of lp.J, so it is not a gap. It is a banked upstream identification with the geometric quotient, used only to read J
  as the invariant of (K,h).

## (b) Normalisation

- Norm(f) = (-t)^{f'(-1)} f, together with its uniqueness, equals lp.normalize. This was checked in 46 + 250 cases.
- At delta=0, delta^-1 L_c = u is a polynomial identity. The delta-division in Sec 5 is exact in Z[A^+-1].
  P1 = (delta/Delta2) p e1 p, which is singular in the JW lattice, is never specialised; Sec 6 uses the regular lattice.
  So the claim that no division by delta happens at delta=0 is correct.
- Small asserted step: "the common A-class cancels" (y/u in Z[t^+-1]). The proof is the Sec 5 parity rule applied to TL2.
- The longitude reading is interpretive, since J := Norm(y/u). There is non-tautological support. A half-twist of the band ends
  sends (y,x) to (A y, A^-1 y - A^-3 x) and multiplies y/u by -t (46/46). The number of half-twists from the raw marking to
  the preferred one is **exactly 2(s0+s1)** in 46/46, where s0 is the signed count of on-axis crossings of K and s1 the
  signed count of off-axis crossing pairs. That is the lifted linking number, so Norm selects the Seifert-longitude marking.
  At the preferred marking delta | x (this part is tautological).

## (c) Section 4

- The algebra is verified (`t_central.log`):
  - (Y X^-1)^2 = t^-4 I. This is exactly A^-32 times the inverse full-twist scalar theta_2^2 on Hom(V1, V1 x V2 x V2).
  - (Y X)^2 is **not** scalar.
  - tr(Y X^-1) = 0 if and only if xi*eta = t^-3(1 - t^4).
  - Y v(a,b) = v(a, t^-3 b).
- Implicit step: why the mixed word Y X^-1 is the central one. Repair in one line: in the sweep braid group on
  (axis, e, w*), x0 = sigma_a^2 and x1 = sigma_b. Hence Y ~ sigma_a^-2 and X ~ sigma_b, and (sigma_a^-2 sigma_b^-1)^2 is
  conjugate to Delta^-2.
- "On all of H" is automatic: X and Y are local operators on the 2-dimensional H, and E1 and Y E1 already span H.
- Independent check: a and b computed from the raw TL3 expansion of the cabled body give v = (a,(b-a)/(1-t^3)).
  - This equals the project's pinned vectors for all **50/50** nonrational bodies in general_boxes.json.
  - lp.J(s.B) = Norm(a) in 250/250. lp.J(s.r2.(y1)^m.B.u1) = Norm(e1^T X^-m v) in **776/776** (m = +-1, +-2).
  - The bodies y0 and x0 give (a,b) = (1, t^-3) and (1, t^3).

## (d) Section 5

Every step was checked on all 269 bodies:
- p e_j p is killed for j = e2, e1e2, e2e1, and U^2 = (delta - 1/delta)U.
- delta | c_e: 269/269.
- c1 and c_e/delta lie in the same A-class mod 4: 269/269, counting 23 cases with c_e = 0.
- beta_raw(A=1) = +-I in TL3 (this is stronger than "a multiple of p(1)"): 269/269.
- (1-t) | c_e/delta: 269/269.
- v2 lies in Z[t^+-1] after preferred normalisation: 269/269.

The argument is not circular. a = y(s.B) uses only (2.1) and the closure functional (<Theta_{s.B}> = Delta2 a exactly).
It uses neither integrality nor the dichotomy. As the note says, this is a containing lattice, not a realisation theorem.

## (e) Section 6

- **Local root facts** (my implementation of the ft_integral maps):
  - At generic q: U_q relations, intertwining of B12, B21, B22, invariance of coev and ev, both snakes, circle = [3],
    i and p intertwiners with p i = I, (T - q^-4)(T - q^2) = 0, and B22 eigenvalues q^-4, -q^2, q^2 with
    multiplicities 1, 3, 5. Also rot(B22) = B22^-1 exactly, so the model is an unoriented framed isotopy invariant;
    the curl is q^4.
  - As h -> 0: B22 converges to the super flip with error O(h). T -> I x (Pi_w1 - Pi_odd) and P1 -> I x Pi_w1, each with
    error O(sqrt h). Curl -> I.
- **Bodies in the regular model.** On 80 bodies of width at most 5, b/a equals the TL3 b/a at t = q^2, with the same
  identification for every body (x corresponds to the positive braiding). Near the root, on 60 bodies: raw a = 1 exactly,
  b/a = (-1)^n0, and the operator equals a(I x Pi_w1) + b(I x Pi_odd).
- **The project's (a,b)** from TL3, after preferred normalisation: a(-1) = 1 and b(-1) = (-1)^n0 in **269/269**.
  The raw ratio b(-1)/a(-1) = (-1)^n0 also holds in 269/269. The 269 bodies are:
  - 50 general_boxes, the T_n box, 8 integral and 45 rational bodies;
  - 70 random nonrational fs.gen bodies;
  - 30 deep-extrema bodies (up to 3 nested band caps);
  - 40 depth-2 and 25 depth-3 necklace bodies, computed by locality (macro sweep, validated 12/12 against direct sweeps).
  v2(-1) is -1 for 149 bodies and 0 for 120. Its parity matches n0 every time.
- The homotopy and winding argument is correct. A self-crossing change is invisible at the root because B22(0) = B22(0)^-1,
  and this also holds after rotation by cups and caps. Curls are 1. Axis-arc crossings never change because the homotopy
  stays in the complement of the straight axis. w = n0 mod 2 holds in this grammar because only x0 and y0 touch the axis.
- Implicit step, citation level: the regular U_q model and the Kauffman/JW model compute the same body state up to one
  common unit. This is standard Reshetikhin-Turaev/Kauffman bracket theory (Kirby-Melvin) and is only asserted here
  and in ft_integral Sec 2. Only b/a matters for the sign, and b/a was confirmed numerically above.
- The hypothesis is needed (`t_closedcomp.log`). An extra closed colour-two loop gives a(root) = 3 when it links the axis
  oddly and -1 when it links evenly, so the dichotomy fails as stated.

## Bonus, outside R1

Theorem O (7.1) was checked on 65 nested necklace bodies. The vector computed from the TL3 states of the children equals
t^{2m(1-eps)} X^-m (v1*...*vn) **exactly, unit included**: 65/65. The off-diagonal entry of e1^T X^-m has value 0 and
derivative -4m at t = -1 for m = 1..4.
