# L1 -- Categorification and Floer theory lens (bridge exploration, 17 Nov 2026)

Status: COMPLETE (sections 1-6). Best bridge: Section 3 (Theorem B3 reverse bridge) + Section 2 (projector channel).

## 0. Plan
- Read CONTEXT, morning summary, lit result.
- Lit check: KWZ multicurves (rational tangle detection, thin tangles, mutation), Hedden-Watson, Watson symmetry group, Lobb-Watson, Sano/Sano-Sato?, Kh of theta curves / quotient, involutive/equivariant Floer.
- Candidate bridges; pick one; develop.


## 1. Literature map (checked this session)
- KWZ, Immersed curves in Khovanov homology, arXiv:1910.14584. Gluing: Khr(T1 u T2) = HF(m(BN(T1)), Khr(T2)) (their Thm 1.9).
- KWZ, Khovanov homology and strong inversions, arXiv:2104.13592 (Open Book Series 5, 2022). READ (pdftotext, scratchpad). Key facts:
  preferred quotient tangle has tau(0) = Seifert-longitude surgery, tau(inf) = U; bijection nontrivial (K,h) <-> tangles with tau(inf) unknotted (via Gordon-Luecke).
  tau(inf)=U forces Khr(T) to meet a(inf) once: Khr(T) = r1(k) u (specials of slope inf) (given geography).
  Thm 3.1 (computer, F2, <=9 crossings): Khr(T_{K,h}) = r1(k) u n*s2(inf), k in 4Z.
  Lemma 2.3: HF(a(0), s_{2n}(inf)) = sum_{i=1}^n q^{4(2i-n-1)} h^{2(2i-n-1)} (shift) V_kappa, V_kappa 4-dim, one delta grading, q = -5,-1,1,5.
  Def 3.4: kappa(K,h) := HF(a(0), specials) = Watson's invariant. Conj 3.6 (=Watson Conj 28: kappa = sum of V_kappa), Conj 3.7 (specials are s_{2n}(inf)).
  Question 3.3: is the slope k always divisible by 4? (They show Conj 3.6 => 4|k via det tau(0)=0.)
  Remark 3.10: over Z/3, 7_4 (2nd inversion) has r1(6), two s2(inf) and FIVE s1(inf): slope 6 not in 4Z.
  dim Khr(tau(n)) = dim kappa + dim HF(a(n), r1(k)).
- KLMWZ, Cosmetic operations and Khovanov multicurves, Math. Ann. 389 (2023) 2903-2930, arXiv:2109.14049 (equivariant cosmetic surgery; split detection).
- KWZ, Thin links and Conway spheres, Compositio 160 (2024) 1467-1524, arXiv:2105.06308.
- Watson, Khovanov homology and the symmetry group of a knot, Adv. Math. 313 (2017), arXiv:1311.1085 (kappa as finite quotient of lim Kh(tau(n))).
- Rozansky, An infinite torus braid yields a categorified Jones-Wenzl projector, arXiv:1005.3266.
- Cooper-Krushkal, Categorification of the Jones-Wenzl projectors, Quantum Topol. 3 (2012), arXiv:1005.5117.
- Hogancamp, A polynomial action on colored sl(2) link homology, Quantum Topol. 10 (2019) 1-75, arXiv:1405.2574.
- Lipshitz-Sarkar, Khovanov homology of strongly invertible knots and their quotients, arXiv:2203.13895 (spectral sequence Kh(K) => annular Kh of the two quotient knots).
- Lobb-Watson, A refinement of Khovanov homology, Geom. Topol. 25 (2021) (arXiv number per search: 1908.00082; not opened).
- Board overlap (IMPORTANT, avoid duplication): letter 50 (Lemma Q iff compact part has nonzero class C(q)), letter 52 ARC LAW (P_tot = A(k,j) + (1-q^2) Pi), TH-BULLET-RANK (dim N_b = 1+2m), TH-BAR-MATCH formal B = a0+S+hS, TH-LADDER, TH-B-EXCLUSION, TH-TWOROW-UNIT, U5-WAT-MAP. No board hits for Rozansky / Cooper-Krushkal / Hogancamp / Lefschetz / Smith / foams.

## 2. BRIDGE A: the J-channel is Rozansky's projector closure (colour-2 theta homology = Watson's limit)
Setup (K_0 of 4-ended tangles, Kauffman bracket, <O> = delta = -A^2-A^-2). tau0, tauinf crossingless; tauinf u alpha = 2 circles where alpha = axis closure.
[T] = y tau0 + x tauinf, u := y + delta x (axis closure / delta; unit since T(inf)=U).
Prop A1 (PROVED, elementary). The infinity-twist sigma has eigenvectors p2 := tau0 - tauinf/delta (eigenvalue A) and tauinf (eigenvalue -A^-3). Hence
   [T] = y p2 + (u/delta) tauinf,
so the raw J-coefficient y is EXACTLY the p2 (Jones-Wenzl) channel and the unit u is the other channel. Pairing: <p2,p2> = Delta2, <p2,tauinf> = 0.
Proof: sigma(tau0) = A tau0 + A^-1 tauinf, sigma(tauinf) = -A^-3 tauinf; solve sigma(tau0 + c tauinf) = A(...) => c = -1/delta. QED.
Cor A2 (PROVED). <T(n)> = A^n Delta2 y + (-A^-3)^n (unit stuff); so A^-n <T(n)> -> Delta2 y  A^-1-adically. This is the board's two-channel TL formula, now read as: the colour-2 theta value is the infinite-twist limit of the branch-knot brackets.
Categorified reading (CONJECTURE A3, consistent with all KWZ data): Rozansky's P2 = lim of twist complexes, so Kh(T u P2) = lim Kh(tau(n)) (shifted) = Watson's inverse limit, and
   Kh(T u P2) = kappa(K,h) (+) Kh(r1(k) u P2)   [finite special part (+) coloured-unknot part],
matching KWZ's dim formula. Euler char: chi(Kh(T u P2)) = Delta2 * u * J. Hogancamp's End(P2) polynomial action should make the coloured-unknot part u-free and kappa = u-torsion; Lemma 2.3's n shifted copies for s_{2n} look like a u-tower of length n (QUESTION, degree bookkeeping not checked).
Leverage: imports Cooper-Krushkal/Hogancamp machinery (functoriality, polynomial action, finiteness over Z[u]) for the theta curve. Honest status: restatement-level for Lemma Q (Euler char of torsion part can still vanish), new as a dictionary entry for the board.

## 3. BRIDGE B (developed): Euler characteristic of the strong-inversion multicurve, and a REVERSE bridge (project theorems => new Khovanov multicurve laws)
Prop B1 (DERIVED from KWZ Lemma 2.3 + K_0 bilinearity; calibrated on data). Components disjoint from a(inf) have K_0 class in the p2 line (they pair to 0 with the axis arc). For s_{2n}(inf) at bigrading (h,q):
   contribution to preferred J = (-1)^h t^m (t^4 - 1) [n]_{t^2},   [n]_{t^2} = sum_{i=1}^n t^{2(2i-n-1)},  t = v^2 (v = KWZ quantum variable, = A^2 up to inversion).
Derivation: chi HF(a(0), s2(inf)) = v^-5 + v^-1 - v - v^5 = -(v - v^-1)(v^2+v^-2)(v^2+1+v^-2); dividing by Delta2 = v^2+1+v^-2 (pairing of p2 with a(0)) and multiplying by delta ~ (v+v^-1) gives (v^4 - v^-4) ~ t^-2 (t^4-1); Lemma 2.3 gives the [n] block with positive coefficients (all copies same h-parity).
Cor B2 (preferred normalization). J = t^k + (t^4 - 1) P(t),  P(t) = sum_{specials} (-1)^{h_s} t^{m_s} [n_s]_{t^2}.
   (This is the board's ARC LAW of letter 52 in KWZ language; new here: explicit [n] blocks, identification P <-> chi_q(kappa)/chi(V_kappa).)
DATA CHECKS (all PASS):
 - trefoil (KWZ: r1(-4) u s2(inf)); board J = t^-7 + t^-4 - t^-3 = t^-4 + (t^4-1)(-t^-7). Unique decomposition with one special: k = -4, P = -t^-7.
 - 4_1 (KWZ: k=0, two s2(inf), same h-parity); board J = t^-6+t^-3-t^-2+1-t = 1 + (t^4-1)(-(t^-6+t^-3)). Two specials, same sign, q-gap 3 (KWZ q-gap 22-16 = 6 = 2x3). Consistent.
 - board record l_bXXYa (mech2/verify/twobridge-compute/task3_runs.jsonl line 15: kh_components r(-8), s2(inf) x2; J_matrix = t^-3 - t^-2 + 1 - t + t^2 = J/t^k): J = t^-8 + (t^4-1)(t^-10 - t^-11). Unique decomposition. TWO SPECIALS OF OPPOSITE h-PARITY at adjacent q-levels (near miss of total cancellation).

Theorem B3 (REVERSE BRIDGE; proofs = the board's PROVED arithmetic + Cor B2; hypothesis H: every non-rational component is an even special s_{2n}(inf) with trivial local system [KWZ Conj 3.7 + linearity; true in all computed cases]):
 (a) J(i) = 1  =>  i^k = 1  =>  4 | k.   [KWZ Question 3.3 under H; KWZ had it under Conj 3.6 via det.]
 (b) J = 1 mod (t+1)^2 (TH-J-FACTORS)  =>  P(-1) = -k/4: the delta-parity-signed count of specials is -k/4. [Recovers KWZ's det tau(0)=0 argument exactly: derivative at t=-1 gives -k - 4P(-1) = 0.]
 (c) NEW mod-3 law: J(e^{i pi/3}) = 1 =>  P(zeta6) = (1 - zeta6^k)/(zeta6^4 - 1) = 0, -1, omega according as k/4 = 0, 1, 2 mod 3 (omega = e^{2 pi i/3}).
     Checks: trefoil k/4=-1 (=2): P(zeta6) = -zeta6^-7 = omega PASS; 4_1 k/4=0: P = -(1 + zeta6^3) = 0 PASS; l_bXXYa k/4=-2 (=1): zeta6^-10 - zeta6^-11 = omega - zeta6 = -1 PASS.
 (d) NEW 5th-root law: J(t) = V_K(t^{+-2}) mod Phi10 (MOMENT-CYC10)  =>  (t^4-1)P(t) = V_K(t^{+-2}) - t^k mod Phi10: chi_q(kappa) at primitive 10th roots is fixed by V_K(zeta5) and k. (Trefoil: J = V_{RH 3_1}(t^2) mod Phi10 checked by hand; chirality convention must be fixed before citing.)
 (e) Z/3 consistency: J is field independent but k and the special list are not (7_4: k=4 over F2 per Table 1, k=6 over Z/3). If s1(inf) contributes t^m(t^2-1) (CONJECTURED class, half of s2), (a) becomes k = 2 * (#odd specials weighted by i^m) mod 4, explaining Remark 3.10's k=6. Not verified.
Novelty: no trace of (c),(d) in KWZ 2104.13592 or KLMWZ; full-text search of 2602.23442 (On mutation invariance in Kh, 2026) not done. These are new constraints on Watson's kappa from the decategorified side.
Leverage for Lemma Q: NONE directly. Every constraint derived from J is satisfied by J = 1; flat formal models pass them all. Value: (i) sanity laws for kht++ runs; (ii) a precise statement of what a realization input must do.

## 4. Precise obstruction to the naive positivity bridge
Flat profile: J = 1 iff P = P_flat(k) := (1 - t^k)/(t^4 - 1) = -[k/4]_{t^4} (k>0), 0 (k=0), t^k[|k|/4]_{t^4} (k<0).
 (O1) For k != 0 the flat profile needs NO cancellation among specials: e.g. k = -4 with ONE s2(inf) at (even h, m = -4) gives J = t^-4 + (t^4-1)t^-4 = 1. Cancellation is between the rational unit and one special end. (Board: TH-TWOROW-UNIT says two-row Euler-1 profiles survive determinant-1 matching under conditions; so not excluded by MATCH.)
 (O2) "Parity-pure special strip" (all specials same h-parity) is FALSE for actual quotient tangles: l_bXXYa has P = t^-10 - t^-11. So no theorem of the form "kappa is h-parity-thin" can prove Lemma Q; and even parity-purity would not exclude (O1).
 (O3) Any statement proved only about chi (arithmetic, cyclotomic, end degrees) cannot exclude flat formal models; the missing input must constrain the POSITION of specials relative to r1(k) (bigraded, not Euler).
 Categorified end laws: top coefficient of J vanishes iff the specials on the top q-level have zero signed count (opposite h-parities on one level) or the rational unit hits that level; TH-END-COUNTEREXAMPLE ("top q8 has h4,5, Euler 0") is exactly this. "Two-ended blocked" = no simultaneous cancellation at both extreme special levels; in curve language a statement about extreme levels of kappa.

## 5. Other bridges scanned (short)
 - Lefschetz/Smith (Lipshitz-Sarkar localization): L_h(q) = sum (-1)^i q^j tr(h|Kh^{i,j}(K)). Quick test: J is NOT simply L_h (J(3_1) exponents vs V(3_1) mod 2 mismatch under obvious normalizations). CYC10/FROB5 look Smith-type; worth one precise computation of tr(h) on a transvergent diagram. UNCLEAR.
 - Instanton webs (Kronheimer-Mrowka J^sharp, arXiv:1508.07205): colours mismatch (SO(3) all edges colour 2 vs our (1,1,2)); no Jones-level Euler char. Low value.
 - HF analogue (HFT / immersed curves of E(K)): decategorifies to Alexander data; Alexander-trivial knots show the HF version of Lemma Q is FALSE decategorified. Useful negative control: any proof must use Jones-specific (q-graded Khovanov) structure.
 - Odd Khovanov / osp(1|2): same Euler characteristic, no positivity gained. Low value.

## 6. Recommended next step (bounded)
Use the existing kht++ pipeline to dump, for every computed (K,h), the full BIGRADED special list (h_s, q_s, n_s) relative to r1(k), and tabulate the offset of each special from the flat support of P_flat(k). Conjecture to test: no special ever occupies a flat-profile position with the flat parity (k != 0), and for k = 0 specials never cancel completely. This is the bigraded statement that an actual proof would need; Theorem B3(c),(d) give free consistency checks on every run.

STATUS: complete for this session (written 17 Nov 2026).

## 7. Sanity computation (exact-arithmetic check, scratchpad l1/check_b3.py, under 1 min)
For trefoil, 4_1 and l_bXXYa: the decompositions J = t^k + (t^4-1)P reproduce the board's J exactly; J = 1 at t = 1, -1, i, e^{+-i pi/3}; J'(-1) = 0; P(-1) = -k/4 (values 1, 0, 2); P(e^{i pi/3}) equals the predicted 0 / -1 / omega in all three cases. Phi10: board trefoil J = t^-7+t^-4-t^-3 matches V_{RH trefoil}(t^2) at all primitive 10th roots (not V(t^-2)), while KWZ list this tangle's chirality as slope -4 (left-handed): one mirror convention differs between board and KWZ; fix before quoting.
