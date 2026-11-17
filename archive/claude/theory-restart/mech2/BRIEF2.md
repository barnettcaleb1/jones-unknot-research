# BRIEF 2: the outline law for N(T) (state of 15 November 2026, 23:30)

Read this whole file first. Then read ~/jones-lanes/theory-restart/notes/2026-11-15b-sutured-side.md (the derivations behind sections 2-5).
The older brief ~/jones-lanes/theory-restart/mech/BRIEF.md has the conventions of the multicurve calculus and of the program kht++ (its sections 1, 2, 7).

## 0. The problem
T = Jones unknot conjecture. Lemma Q = T for unknotting-number-one knots; equivalently: for a non-trivial strongly invertible knot (K,h) with quotient
tangle T (Seifert framed, T(infinity) = unknot), the Kauffman bracket vector of T is not a unit multiple of that of the trivial tangle Q_0 ("T is not flat").
We want a MECHANISM: a statement about actual tangles, with a proof or a proof route, that implies non-flatness. Theory first; computation only as a cheap check.

## 1. The object N(T) (all PROVED; Codex = our collaborator; F = F_2)
- C(T) = Bar-Natan complex over the two-object algebra B (objects b = Q_0 = kht++ symbol ⬮ = "bullet", c = Q_infinity = ⬯; generators D_b, D_c, S, relations DS = SD = 0,
  H = D + S^2; gradings deg D = (h,q) = (0,-2), deg S = (0,-1), differential (1,0), delta = q/2 - h). BN~(T) = reduced type D structure = immersed multicurve.
- N(T) := H(F_b C(T)), F_b = augmentation b -> F, c -> 0, paths -> 0. In a reduced model N(T) = span of the b-generators of BN~(T). Bigraded by (h,q).
- chi_q N(T) = u J(T), u a signed monomial; T is flat iff J = 1. J = 1 mod (q + 1/q)^2. J is multiplicative, and N(T1 + T2) = N(T1) (x) N(T2), under the horizontal tangle sum
  (= equivariant connected sum). dim N = 1 + 2m, m = number of special components of Kh~(T) (all of slope infinity). m = 0 iff T is rational.
- END: the Euler characteristic of N in its top quantum degree and in its bottom quantum degree is non-zero. END => Lemma Q (Codex). Stronger: NP (section 5).
- Formal object B0 := a(0) + S + hS (S a compact component, hS its shift by (h,q) = (1,0)): satisfies every algebraic constraint we know and has J = 1. It is not a tangle.
  Any mechanism must use an input that B0 violates. The offset (1,0) between two compact components DOES occur inside actual tangles (333 times in the data); only the
  bare object is excluded. So the law is global.

## 2. Three descriptions of N(T) (new today)
(a) REPRESENTATION. In the direction of the horizontal sum, T is an endomorphism of V (x) V = V_2 + V_0 (U_q sl_2). Eigenvalue on V_0: the unit u (T capped off on one side is a
    trivial arc). Eigenvalue on V_2: uJ. For the swap inversion on K # K, T = doubled-strand tangle T_K and J = reduced Jones polynomial of K coloured by the 3-dimensional
    representation (checked on 4_1 against Habiro's formula). So Lemma Q contains "the 3-dimensional coloured Jones polynomial detects the unknot".
(b) ANNULAR. N(T) = annular Khovanov homology of T(n) (annular closure of T sigma^n, any n) in annular weight 2: b-resolutions = two essential circles, c-resolutions = one
    inessential circle. AKh(T(n)) = N (x) V_2 + (weight-zero multiplicity space) under the sl_2 action.
(c) SUTURED. The same complex is Grigsby-Wehrli's Khovanov complex of the balanced tangle T in D x I. Their spectral sequence (arXiv:0807.1432; arXiv:0907.4375) goes to SFH of the
    double cover of D x I branched along T = exterior of K with two meridional sutures. THEOREM S: a spectral sequence from N(mirror T) to HFK^(K; F_2); 1 + 2m >= rank HFK^(K).
    DATA: equality 1 + 2m = rank HFK^(K) in 131 of 132 table cases (incl. 8_19, 9_42) and for all 21 doubles (rank HFK^(K # K) = det^2); exception 9_46 second inversion (15 vs 9).
(d) CURVES. N(T) = HF(BN~(T), A_b), A_b = loop at the special puncture * around the puncture p1; the arc from * to p1 has the slope of the unknot filling (meridian of K).

## 3. Strip picture, standard form, shape law (DATA unless marked)
Planar cover R^2 - Z^2: * = (even, even), p1 = (0,1), p3 = (1,0), p2 = (1,1) mod 2. Lifts of A_b = the two sides of vertical lenses L_n on the special line x = 0.
Every component of BN~(T) lies in the strip |x| < 1. Moves between consecutive b-generators along a curve:
    D^a (cross a lens):                                   (h,q) = (1, 2a),     delta-change 0
    P_n = S (D S^2)^(n-1) D S (run past n lenses on one side): (h,q) = (2n+1, 4n), delta-change -1
In every saved chain file the moves are D (a = 1) and P := P_2, except one D^2 (9_46 second inversion). Field independent (F_3, Q) on the cases rerun.
- All 1420 compact components (table + doubles) are the square  x -P-> . -D-> . <-P- . <-D- x.
- 548 of 551 arcs are pure staircases (all P one way, all D the other way), then a tail S (D S^2)^(|k|/2-1) D carrying the slope k of the rational component of Kh~(T).
So with d_D, d_P the arrow maps: N = Z_l + Lambda^r over Lambda = F[d_D, d_P]/(d_D^2, d_P^2); zigzag of 2l+1 = 2|2j + k/4| + 1 generators; H(d_D) = H(d_P) = F.
(j = lk(T(0))/4.) This is the structure of knot Floer complexes of thin knots. CONJ (shape law): this holds for every actual tangle with unit arrows; expected reason: in the
unreduced theory the dot on the second strand survives, so a composable pair D then P has non-zero composite unless completed to a square.
SETTLED (do not redo): moving the reduction point to the other strand (rotating the tangle by pi) gives the identical BN~ with identical gradings (checked on 3_1 and 9_42;
consistent with mutation invariance over F_2). So the two strands do not give two different arrow structures.

## 4. Lattice coordinates (PROVED from 3)
b-generator = rho + a D + b P, D = (1,2), P = (5,8) (rho = end of the arc): h = a + 5b, q = 2a + 8b, delta = -b.  N = finite multiset in Z^2 (rows b = delta-levels).
J = sum over N of (-t)^a (-t^4)^b (t = q^2). Square = unit square; J = chi(zigzag) + (1-t)(1-t^4) Pi(t), Pi = sum over squares of (-1)^(a+b) t^(a+4b).
Cancellation in J: (a,b) against (a - 4m, b + m), m odd. B0 = two unit squares offset by (-4, +1).
Print any example with: python3 ~/jones-lanes/theory-restart/tools/grid.py FILE.jsonl NAME   (files in section 7). Examples:
    3_1: rows b=0: a in {0*,1}; b=-1: {1}.        4_1: (0,0)*,(1,0),(1,-1),(2,-1),(2,-2).       9_42: point + squares at (1,0),(0,1).
    double of 4_1 (25 generators): point + six squares at (-3,1),(-2,0),(-1,0),(0,-1),(1,-1),(2,-2).

## 5. The outline law (DATA, 283 distinct tangles; no exception)
POLYGON LAW: the Newton polygon of N in the (a,b) plane has edges only in the directions (1,0) [D], (0,1) [P], (1,-1) [P - D = (4,6)], (2,-1) [P - 2D = (3,4)],
apart from (3,-2) seven times, (1,1) once (8_19), (7,-3) once (9_46 second inversion). Equivalently, in the (q/2, delta) plane every non-horizontal edge moves q/2 by 2, 3 or 4
per delta-level; in the (h,q) plane all edge slopes lie in [5/4, 2]. The Khovanov cube complex itself has a flat top and bottom (slope 0).
An extreme cancellation in J needs an edge of direction (4,-1) in the (a,b) plane, i.e. (h,q) = (1,0): the bidegree of the Khovanov differential, of the annular
differential d_-, and the excluded case k = 1 of the Szabo-type bidegrees (k, 2k-2) (k = 2,3,4,5 give exactly P - 3D, P - 2D, P - D, P).
    NP:  the maximum and the minimum of q on N(T) are each attained on a single delta-level.     NP => END => Lemma Q.
Newton polygons add under tangle sum. Old form (TILT): max q and min q on a delta-level strictly decrease as delta increases; steps 2, 4, 6, 8.
TEST where the Floer side cancels: a strongly invertible knot with Alexander polynomial 1 (half-diagram s.r1.y0.x2.r3.y0.y2.u1.x2.x2.y0.y1.x0.u1): r_1(4) + 15 specials,
dim N = 31 = 3-staircase + 7 squares, rows (b = 1..-2): [1 2 1 . .], [1 4 5* 2 .], [. 2 4 4 1], [. . 1 2 1]; END holds; hull directions (1,0), (0,1), (1,-1) only.

## 6. What to deliver
A report at the path given in your task, written AS YOU GO (append findings every time you establish something; a stopped agent must leave a usable file).
Mark every statement PROVED / CITED (with the exact source and statement number, and say whether you read it or recall it) / DATA / CONJECTURED.
Wanted, in order of value: (i) a mechanism: a precise statement that B0 violates, that actual tangles satisfy for a stated reason, and that implies NP or END,
with the first lemma proved and the remaining gap named; (ii) a proved theorem for a class of tangles; (iii) a proved negative (this lens cannot work, exactly why).
Complete ideas matter more than formal polish; do not spend effort on verification sweeps. No claim that Lemma Q or T is proved unless every step is.
Do not write anywhere except your own folder under ~/jones-lanes/theory-restart/mech2/. Do not contact anyone. Web access is for reading papers (arXiv etc.) only.

## 7. Files and tools
- Data (JSON lines; each record has 'khr' = Kh~ components {type r|s, slope, q, delta}): ~/jones-lanes/theory-restart/lit/kht/out/k138/k138.jsonl (138 inversions, knots to 9 crossings),
  tilt/run_3_45.jsonl (two-bridge; labels of about half the files are wrong, the tangles are valid), dbl/doubles.jsonl (doubled tangles T_K), comp/comp4.jsonl, comp/comp5.jsonl (sums),
  alex1/runs.jsonl (the Alexander-polynomial-one knot). Chain files (BN~ with arrows): e.g. lit/kht/out/k138/examples/si/<name>/cxBNr-c2-qs and cxKhr-c2-qs.
  In chain files: ⬮ = b, ⬯ = c, "—>" = D^k, "~>" = S^k (S^2 between equal symbols); the printed (h,q) is that of the first generator; an arrow x -> y of label S^k or D^k gives
  h(y) = h(x)+1, q(y) = q(x)+k resp. +2k; a chain ending in an arrow is cyclic (compact component).
- Scripts in ~/jones-lanes/theory-restart/tools/: grid.py (lattice picture), gtilde.py (J-set, END check), hull.py (Newton polygon), alex.py (Alexander polynomial of a half-diagram word),
  kauffman.py (bracket), run_words.py (run kht++ on half-diagram words), jq_tangle.py (bracket vectors). sympy in tools/venv/bin/python.
- kht++: /Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++ . Run it from a working folder of your own that has the .kht file in a subfolder whose name is
  longer than one character (examples/mine/x.kht), ALWAYS under a time limit (perl -e 'alarm 300; exec @ARGV' kht++ ...), with stdin closed (</dev/null).
  A .kht file: line 1 "% comment", line 2 the Morse word (x<i>, y<i> crossings, l<i>/r<i> caps, u<i> cups, i = index of the left strand, from 0), line 3 the orientations of the top
  ends as ",1" (one top end) or ",1,1". Strongly invertible knot: word "s.<half diagram>" with last line ",1"; "kht++ -c2 -q -s FILE" computes the quotient tangle (output folder next to
  the file: cxBNr-*, cxKhr-*). Without -q: the knot itself. "-d FILE": doubled strands. Fields: -c2 (default), -c3, -c0. The special (reduction) end is the top-left end.
  Source of the program (C++): lit/kht/src/khtpp/sources/modules/. Conventions report: lit/kht/REPORT.md.
- Literature digests with TeX sources: ~/jones-lanes/theory-restart/lit/{kwz-immersed,kwz-linear,kwz-inversions,kwz-thin,bn-torsion,boyle-spyropoulos,recent,kht}/REPORT.md.
- Codex's notes (read-only): /Users/calebbarnett/Documents/Codex/2026-10-31/it-is-an-open-problem-whether-4/work/theory_restart/jtilt_referee_synthesis.md and neighbours.
