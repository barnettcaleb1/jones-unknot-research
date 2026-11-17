# BRIEF: the geography reduction of Lemma Q (state of 15 November 2026, 19:30)

## 0. The problem
T (Jones unknot conjecture): V_K = 1 implies K is the unknot. Lemma Q: T for unknotting-number-one knots. Equivalent form used here:
for a nontrivial strongly invertible knot (kappa, h) with quotient tangle X = T_(kappa,h), the knots K_n (double branched cover S^3_{1/n}(kappa)) do not
all have Jones polynomial 1. "Flat" means all K_n have V = 1; equivalently the Kauffman bracket vector of X is a unit multiple of that of the
trivial tangle Q_0. T is known for all knots up to 24 crossings, so no small example is flat. T iff (Lemma Q and a separate rigid-case statement R).

## 1. Objects and conventions (Kotelskiy-Watson-Zibrowius = KWZ; coefficients F_2 unless stated)
- Conway tangle T with a distinguished end; BN~(T), Kh~(T): bigraded immersed multicurves on the four-punctured sphere; delta = q/2 - h;
  differentials have (h,q)-degree (1,0); H has degree (0,-2); Kh~(T) = cone of H on BN~(T).
- Q_s rational tangle of slope s, a(s) = BN~(Q_s) (an arc), Kh~(Q_s) = r_1(s). Pairing: Kh~(T(s)) = HF(a(s), Kh~(T)), BN~ similarly (wrapped),
  where T(p/q) = Q_{-p/q} union T. Seifert framing: T(infinity) = unknot, T(0) <-> Seifert longitude; K_n = T(1/n); integer closures T(n) have
  double cover S^3_n(kappa).
- Linear classification (arXiv:2202.01460 over F_2; arXiv:2602.23442 over any field): every component of Kh~(T) is r_n(p/q) or s_2n(p/q).
  This is NOT true for BN~(T): its compact components can wrap non-special punctures and carry local systems.
- kht++ labels (program of Zibrowius, built locally): a special is printed "s4(inf) q^c delta_^d": c = quantum offset, d = delta level (integer).
  The rational component is printed "r(k) q^{qr} delta|^{dr}". kht++'s s4 is the curve called s_2 in arXiv:2104.13592.
- A special s4(inf) at (c,d) paired with a(0) gives V_kappa: four generators on one delta-diagonal at q = c + {-5,-1,1,5}; in t = q^2 h the
  pattern is (1 + t^2)(1 + t^3). Paired with a(1/n): Poincare polynomial (1 + t^3)(1 + t^2)[n]_t, delta-thin, dimension 4n.
  A longer special (KWZ's s_2n(inf), n > 1) contributes n such blocks on one level at quantum shifts 4(2i - n - 1), i = 1..n (KWZ Lemma 2.3).
  None has occurred in our data; KWZ say they exist (arXiv:2104.13592, after Conjecture 3.7) without naming examples.

## 2. Theorems available
- STRUCTURE (Kotelskiy-Lidman-Moore-Watson-Zibrowius arXiv:2109.14049, proof of Thm 1.2, with the classification): if T has an unknot closure
  then in Seifert framing Kh~(T) = r_1(k) + special components of slope infinity, k an even integer, with at least one special iff T is not rational.
  The specials are exactly the linear curves disjoint from a(infinity).
- TORSION: for a knot K and a field F, BN~(K) = F[H]{0,s} + sum of F[H]/(H^l); max l = lambda(K;F) <= proper rational unknotting number
  (Lewark-Marino-Zibrowius arXiv:2409.05743 Prop 3.33, Thm 1.2). K_n for even n is a proper rational replacement of the unknot: all bars length one.
  For odd n long bars occur (trefoil: K_1 = T(3,5) has an H^2 bar; computed: exactly one H^2 summand for every odd n <= 9).
- DEFECT IDENTITY (ours): V~_K(q) = q^s + (1 - q^-2) chi_q(Tors BN~(K)); chi_1(Tors) = -s/2.
- Rank growth: dim Kh~(T(n)) = D + |n - k| for integers n, D = rank contributed by the specials.
- Each linear component of slope != s pairs with a(s) in a single delta grading (KWZ thin paper arXiv:2105.06308 Lemma 6.7).
- Field dependence: over F_3 some quotient tangles have s2 components and k = 2 mod 4 (arXiv:2104.13592 Remark 3.10); the Jones data is field independent.

## 3. The decategorification (ours; verified against a direct bracket computation on the trefoil and against multiplicativity on 3_1 # 3_1)
With j = lk(T(0))/4, computed from the rational component by  qr = 24 j + k(|k|+2)/(|k|+1):
    [T] = q^{24j} [Q_0] + x ([Q_inf] - (q + 1/q)[Q_0]),
    x = (1 - q^2)(1 + q^4) ( -q^-3 P(q) + q^{24j+1} [k/4]_{q^8} ),      P(q) = sum over specials of (-1)^{c/2 - d} q^c,
    [m]_{q^8} = (1 - q^{8m})/(1 - q^8)   (all data: specials are s4(inf), 4 | k).
FLAT iff x = 0 iff P = q^{24j+4} [k/4]_{q^8}. Call the right side the VIRTUAL STRING of r_1(k): |k|/4 virtual specials at offsets 24j+4+8i
(k > 0, i = 0..k/4-1, sign -) or 24j+4-8i (k < 0, i = 1..|k|/4, sign +).  P_tot := P - virtual string; x = -q^-3 (1-q^2)(1+q^4) P_tot.
Classical facts: (1 - t^4)(1 - t + t^2) | x with t = q^2, and x/((1-t^4)(1-t+t^2)) = -j at t = 1. So flat forces j = 0.
J := 1 - (q + 1/q) x q^{-24j} is multiplicative under equivariant connected sum; J = 1 mod delta^2; J a unit iff J = 1 (Codex TH-J-FACTORS).
BN~ level (data): BN~(T) = one immersed arc + compact components; each compact component at printed (q, delta) gives two specials at offsets
q+4, q+6 on level delta; the arc gives |2j + k/4| specials; the arc with its bigrading depends only on (k,j) (one exception in the table, 9_46 second
inversion). ARC LAW: A(k,j) := (arc specials) - (virtual string) is a universal function of (k,j); when k = 0 or sign(2j + k/4) = sign(-k) it is a string
of 2|j| monomials of one sign (steps 6 or 8), e.g. A(0,1) = q^16 + q^22, A(-4,1) = q^14 + q^20, A(-8,1) = q^12 + q^20; A(-4,0) = -q^-6 (1 - q^2).
    P_tot = A(k,j) + (1 - q^2) Pi(q),   Pi = sum over compact components of BN~(T) of (-1)^{(q+4)/2 - delta} q^{q+4}.
FLAT iff j = 0 and Pi = -A(k,0)/(1 - q^2); for k = j = 0 the arc is a(0) and FLAT iff Pi = 0.

## 4. The two empirical laws (no exception so far)
Write the specials as points (c, d) (expanded: a longer special counts as its n blocks).
- TILT: the occupied levels d are consecutive; passing from level d to d+1 strictly lowers BOTH the minimum and the maximum offset c on the level.
  (Mirror invariant. Steps seen: 2, 4, 6, 8; exactly 6 in all two-bridge quotients outside the published table.)
- OVERHANG: if k > 0, max c over specials >= (top of the virtual string, 24j + 2k - 4) + 6; if k < 0, min c <= (bottom, 24j + 4 - 2|k|) - 6.
- Sign coherence is FALSE: two specials with equal c on adjacent levels (cancelling in P) occur from nine crossings on, over F_2, F_3, F_5 and Q.
- Consequence: TILT puts all specials of extreme offset on one level, hence with one sign, and OVERHANG keeps the virtual string away, so the extreme
  coefficient of P_tot is nonzero: (STRUCTURE with s4 and 4|k) + TILT + OVERHANG => Lemma Q. For k = 0, TILT alone.
Evidence (about 950 adjacent level pairs, 0 failures): the 138 strong inversions on knots up to nine crossings; ~145 further two-bridge quotients
(denominators up to 45); 21 doubled-strand tangles T_K (quotient of K # K by the swap; Whitehead doubles are T_K(+-1/2)) with up to 84 specials
and 13 levels; ~60 equivariant connected sums.

## 5. Codex's formal countermodel and matching lemma  (work/theory_restart/curve_structure_read.md in the Codex workspace)
B = a(0) + S + hS in the Bar-Natan type D category (S a special s4(inf), hS its homological shift): the extra summands miss the unknot arc, cancel in
every Euler pairing, are H-annihilated in closures; the H-cone gives specials qS, q^-1 h^-1 S, q h S, q^-1 S on two adjacent levels with equal offset
sets. So strict TILT fails for B although the unknot pairing, all Euler identities, the H-cone and all unit-bar requirements hold. B is a formal object,
not a tangle. A proof of TILT (or of the extreme-coefficient statement) must therefore use a REALIZATION input that B violates.
Matching lemma: on each delta diagonal with the pawn removed, a length-one-bar structure exists iff b_h := n_h - b_{h-1} >= 0 and returns to 0; it is then forced.

## 6. What a mechanism must deliver
A precise statement about actual tangles with an unknot closure that (i) is violated by the formal object B (say which structure of actual tangles it
uses), (ii) implies TILT, OVERHANG, or directly "the extreme coefficient of P_tot is nonzero", (iii) comes with a proof, or a proof sketch with the
first lemma proved and the obstruction to the rest named. A proved negative result (this lens cannot work, for this exact reason) is also a result.
Honesty rules: mark every statement PROVED / DERIVED FROM DATA / CONJECTURED; no claim that T or Lemma Q is proved unless every step is; cite sources
with numbers; say what you did not check.

## 7. Files and tools
- Board (theory log, sections X.1-X.9 at the end): /Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/collab/THEORY-width-ladder.md
- Codex's files: /Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/work/theory_restart/*.md
- Literature digests with TeX sources: /Users/calebbarnett/jones-lanes/theory-restart/lit/{kwz-immersed,kwz-linear,kwz-inversions,kwz-thin,bn-torsion,boyle-spyropoulos,recent,kht}/REPORT.md (sources under each src/)
- Data: lit/kwz-inversions/data.json (the 138, with BN~ components from the kht++ site); JSON-lines files lit/kht/out/k138/k138.jsonl,
  lit/kht/out/tilt/run_3_45.jsonl (has a 'bn' list: h, q, delta, cyclic = compact), lit/kht/out/dbl/doubles.jsonl, lit/kht/out/comp/comp4.jsonl, comp5.jsonl.
  Each record: 'file' or 'knot', 'khr': list of {type: 'r' or 's', len, slope, q, delta}.
- Scripts: /Users/calebbarnett/jones-lanes/theory-restart/tools/{tilt_analyze.py, overhang.py, tiltplus.py, tilt_2bridge.py, tilt_composites.py, jq_tangle.py}; sympy in tools/venv/bin/python.
- kht++ binary: /Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++ . Run it from a folder that has the .kht file in a subfolder whose
  name is longer than one character (e.g. examples/mine/x.kht), ALWAYS under a time limit (perl -e 'alarm 120; exec @ARGV' ...), with stdin closed.
  Input: Morse words (x<i>, y<i> crossings; l<i>, r<i> caps; u<i> cups); a strongly invertible knot is "s.<half diagram>" with last line ",1";
  "-c2 -q -s FILE" computes the quotient tangle (BN~ list, then Kh~ list). "-qNAME:p/q" (attached; even q only) writes two-bridge inversions to
  examples/strong_inversions/2-bridge_knots/; "-rNAME:p/q" writes a (1,1) knot file to examples/knots/2-bridge_knots/; "-d FILE" doubles strands.
  Concatenating two half-diagram words gives the equivariant connected sum. Fields: -c2 (default), -c3, -c5, -c0 (rationals). No closure option:
  append twists and a cup by hand. See lit/kht/REPORT.md sections 2-3 for conventions.
