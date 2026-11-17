# Brief kht: kht++ convention check and trefoil dictionary test

Status: COMPLETE. All computations were run locally on 2026-11-15 with kht++ built from source.
Everything below that is marked [run] is a local computation (raw inputs/outputs under `out/`);
[doc] is the program's documentation; [code] is the program's source; [KWZ-SI] is
Kotelskiy-Watson-Zibrowius, "Khovanov homology and strong inversions", arXiv:2104.13592v1 (only version; TeX read, page
numbers from the v1 PDF); [KWZ] is "Immersed curves in Khovanov homology", arXiv:1910.14584v2 (TeX read, used only for
the idempotent convention).

## 0. Source and version

- Repository: https://github.com/cbz20/khtpp, cloned (depth 1) to `src/khtpp`, commit
  `a8be0afe9d8e80396449eeb891930b62f47a0cf8` (2024-12-20, "bugfix: remove global move for tangle simplification").
  The binary reports `kht++ 0.1`.
- Website: `https://cbz20.raspberryip.com/code/khtpp/` itself returns 403; the documentation is at `.../khtpp/docs/` and
  the example index at `.../khtpp/examples.html` (folders: Jones [its only link is a 404], RasmussenSOfSatellites,
  SInvariantAndTorsion, ThinLinksAndConwaySpheres, braids, knots, miscellaneous, pretzeltangles, strong_inversions, tests,
  torus-tangles, two-bridge). Input files for the strong inversions were taken from
  `.../examples/strong_inversions/2-bridge_knots/{3_1,4_1-1,4_1-2}.kht` (saved in `src/web/`).
- The repository's own `examples/` folder contains only `tests/3_1.kht` and `tests/PT2m3.kht`.

## 1. Build

- Dependencies per `docs/Installation.md`: a C++17 compiler and the header-only Eigen library. Eigen was not on the
  machine; following the README I downloaded the Eigen 3.4.0 tarball (sha256 8586084f...c1c72) into `src/libraries/` (no
  package manager, nothing installed system-wide).
- Build command (makefile untouched): `make -j8 PATH_EIGEN=../libraries/eigen-3.4.0` in `src/khtpp`, Apple clang 15.0.0,
  arm64 macOS. Builds in about 40 s with only unused-variable warnings from Eigen. Binary: `src/khtpp/kht++`.
- Portability problems met (the docs say the program is tested on Linux only):
  1. `-p <string>` (append a tangle string to an already computed complex) segfaults (exit 139) as soon as the appended
     string contains a cup `u`; appending crossings only works. Workaround used throughout: write the full tangle string
     of the closure into its own `.kht` file.
  2. A `.kht` file whose name contains `^` makes the program hang (the docs restrict names to alphanumerics, `-`, `_`).
  3. `seq 1 0` on macOS counts down; irrelevant to the program but it bit one of my shell loops (file
     `si_explicit/t31_x0.kht` is really the 2-twist-pair tangle; ignore it).

## 2. Program conventions

### 2.1 Field
Default F_2 (`-c2`). Options `-c3,-c5,-c7,-c11`; `-c0` = Q, flagged experimental (no overflow check); `--sum` is
documented to be wrong outside F_2 [doc Options]. All statements below are over F_2 unless said otherwise; the trefoil
and figure-eight quotient tangles, the pretzel tangle and the closures K_{+-1}, K_{+-2}, K_3 were rerun over F_3 and Q
with identical curves and identical H-torsion orders (`out/si/run_otherfields.log`).

### 2.2 Input format and tangle ends
A tangle is a top-to-bottom Morse word: `x<i>` = crossing whose over-strand starts at the top left of the crossing,
`y<i>` = over-strand starts at the top right, `l<i>`/`r<i>` = cap (oriented left/right), `u<i>` = cup; `<i>` = index of
the left strand involved, counted from 0. The last line lists the orientations of the top ends (1 = up, 0 = down)
[doc Input]. Tangle ends are numbered from 0: top ends left to right, then bottom ends left to right
[code `headers/Cob.h:47`].

**Special (reduction) end = end 0 = the top-left end** (default argument `special_end = 0` of `CobMor::to_BNMor`,
`headers/Cob.h:344`, used without argument in `Complex.cpp:630`). A Conway tangle can be entered as a 2-2 tangle
(ends TL, TR / BL, BR) or as a 1-3 tangle (one top end = the special end; bottom ends b1, b2, b3). The two pictures are
identified by pulling TR down on the right: (top; b1, b2, b3) = (TL; BL, BR, TR). This was checked on outputs [run
`out/rational`, `out/rational22`].

### 2.3 Idempotents and slopes
- `⬮` (called ●, b in the code) is the crossingless tangle joining the special end TL to TR (and BL to BR), i.e. the
  horizontal tangle; `⬯` (○, c) joins TL to BL (and TR to BR), the vertical tangle [code `Cob.cpp:801-824`; run].
  So ⬮ carries slope 0 and ⬯ slope ∞. This agrees with the papers at the level of labels: [KWZ] Section 4 (theorem
  with TeX label `thm:OmegaFullyFaithful`) sends • to the trivial tangle written \No and ◦ to \Ni, and [KWZ-SI]
  Lemma 2.3 (p.5) writes a(0) = BN~(\No); so • = ⬮ = Q_0 and ◦ = ⬯ = Q_∞. (The trivial-tangle symbols are pictures in
  the TeX; I did not render them, the horizontal/vertical reading is from the kht++ code and my runs.)
  WARNING: the 2021 website outputs (kht v0.1 of March 2021) have the two idempotent symbols interchanged relative to
  the current repository for the same input (trefoil quotient: website BN~ starts `⬯~~S~>⬮—>⬮...`, current build
  `⬮~~S~>⬯—>⬯...`), and the old `-qs` simplification comments describe 2-2 tangles while the current `-q` produces a
  1-3 tangle. Do not mix website output with output of the current build.
- Slope labels printed for Kh~ components (r = rational, s = special), calibrated on rational tangles [run]:

  | tangle (special end TL) | 1-3 input | 2-2 input | BN~ | Kh~ label |
  |---|---|---|---|---|
  | horizontal, TL-TR | `l0` | `u0.l0` | `h^0 q^0 ⬮` | r(0) |
  | vertical, TL-BL | `l1` | (identity) | `h^0 q^0 ⬯` | r(∞) |
  | one crossing, over-strand BL-TR | `l1.y0` or `l0.x1` | `y0` | `⬯~S~>⬮` | r(1) |
  | one crossing, over-strand TL-BR | `l1.x0` or `l0.y1` | `x0` | `⬮~S~>⬯` | r(-1) |
  | two vertical half twists of the +1 handedness | `l1.y0.y0` | `y0.y0` | `⬯~S~>⬮—D—>⬮` | r(1/2) |
  | two horizontal half twists of the +1 handedness | `l0.x1.x1` | | `⬯—D—>⬯~S~>⬮` | r(2) |
  | | `l1.x0.x0` | | `⬮—D—>⬮~S~>⬯` | r(-1/2) |
  | | `l0.y1.y1` | | `⬮~S~>⬯—D—>⬯` | r(-2) |

  So Q_0 = horizontal, Q_∞ = vertical, Q_1 = single crossing whose over-strand has positive slope in the plane picture
  with the special end at the top left; Kh~(Q_s) is labelled r(s) and BN~(Q_s) is the arc a(s).
- Appending twists: a half twist `x1` on the two right-hand ends (b2,b3) changes every slope label s to s+1 and fixes
  ∞ (run: trefoil quotient r(-4) -> r(-3), specials stay at ∞); `y1` gives s-1; `x0`/`y0` on (b1,b2) fix 0.
- **How rational closures are specified.** There is no closure option. One appends twists and a final cup to the
  1-3 tangle, which gives a 1-1 tangle (a knot or link cut open at the special end), and the program then prints the
  complex CKh~ over F[H]. For a 1-3 tangle T: `T.u1` (join b2,b3) is the closure of slope ∞ in the sense of [KWZ-SI]
  (T(p/q) := Q_{-p/q} ∪ T, p.2); `T.u0` (join b1,b2) is T(0); `T.x1^k.u0` = T(-k), `T.y1^k.u0` = T(+k);
  `T.y0^n.u1` and `T.x0^n.u1` are the two closures of slope ∓1/n (see 4.2 for which is which on the trefoil).
  Sanity: for the trefoil quotient, `T.u1` is the unknot, `T.x1.u0` and `T.y0.u1` give identical output, and so do
  `T.y1.u0` and `T.x0.u1`.
- Special-curve length: the program's label `s4(...)` is a closed chain with 12 generators (8 in one idempotent, 4 in
  the other). [KWZ-SI] calls this same curve s_2 (Example 2.1, Fig. 7 caption "total number of generators ... is 8n" for
  s_{2n}, Theorem 3.1). So **kht++ s_{m} = [KWZ-SI] s_{m/2}**. The kht++ docs cite the later thin-links paper for the
  names r_n, s_n (I did not open that paper to compare). Check which indexing your s_{2n}(p/q) uses: with the kht++
  indexing the trefoil's special component is s_4(∞), with the [KWZ-SI] indexing it is s_2(∞).

### 2.4 Gradings
- Three gradings h (homological), q (quantum), δ with q/2 = h + δ [doc Output].
- Links: CKh~ is a sum of towers `⬮` (a free F[H] summand, generator at the printed (h,q)) and pieces
  `⬮——H^n—>⬮` (torsion F[H]/H^n; the printed bigrading is that of the source; the target is at (h+1, q+2n)).
  Normalization [run]: unknot = `h^0 q^0 ⬮`; the positive (right-handed) trefoil `r1.y0.y0.y0.u1` gives `h^0 q^2 ⬮` and
  `h^2 q^6 ⬮—H—>⬮`, i.e. Kh~ = q^2 + q^6 h^2 + q^8 h^3. So q is the usual quantum grading of reduced Khovanov
  homology (unknot in degree 0, positive knots in positive degrees), the Jones polynomial is
  V = Σ (-1)^h q^q with t = q^2, and deg H = q^{-2} h^0.
- Tangles: the printed bigrading is that of the first generator of each chain. The other generators follow from
  deg D = q^{-2}, deg S = q^{-1}, differential of degree h^{+1} q^0: for an arrow x -> y labelled S^k (D^k) one has
  h(y) = h(x)+1, q(y) = q(x)+k (resp. +2k). Unlabelled `—>` is D, unlabelled `~>` is S, or S^2 when it joins equal
  idempotents. Verified: with this rule every cyclic chain in every output closes up consistently and reproduces the
  printed mean quantum grading (`out/scripts/khtparse.py`, `out/parsed_generators.txt`).
- Kh~(T) is the cone of H on BN~(T) with shifts [h^{-1}q^{-1} BN~ -> h^0 q^{+1} BN~] (e.g. BN~(Q_0) = `h^0 q^0 ⬮`,
  Kh~(Q_0) = `h^-1 q^-1 ⬮~~S^2~>⬮<—D—`, generators at (-1,-1), (0,1)).
- The absolute bigrading of a tangle invariant depends on the orientation of the tangle strands (reversing one strand
  shifts everything uniformly by the usual (n_+, n_-) correction). The `-q` output uses its own orientation, which is
  not the one induced by the unknot closure: for the trefoil the two differ by h^8 q^24 (see 4.3).
- In the component labels, `q^a` after the slope is the mean quantum grading of the generators, and `δ|^b` / `δ_^b`
  is the "vertical"/"horizontal" δ-grading in the sense of the thin-links paper [doc Output]; `δ_` is used for slope ∞.

### 2.5 Strong inversions
Input: the half-diagram to one side of the axis with prefix `s.` [doc Input]. Without `-q` the program computes the
knot itself; with `-q` the quotient tangle. [doc Options, "Quotients of strongly invertible knots"]: the quotient is
framed so that the closure of slope ∞ is the unknot and the closure of slope 0 corresponds to surgery along the
longitude. In the code (`Tangles.cpp:967-1040`) the quotient is a 1-3 tangle whose top end is the end of the axis arc,
and the framing is corrected by |writhe| pairs `x1.x1` or `y1.y1` on (b2,b3). [KWZ-SI] fixes the same
representative: S^3_{p/q}(K) = Σ(S^3, τ(p/q)) with τ(p/q) = Q_{-p/q} ∪ τ (p.2), τ(0) = Seifert longitude surgery and
τ(∞) = unknot (p.3).

## 3. Raw computations (F_2)

Notation: chains are copied verbatim; for cyclic chains the last arrow returns to the first generator.

### 3.1 Rational tangles (`out/rational/`, orientation: single top end up)
| tangle | BN~ | Kh~ |
|---|---|---|
| Q_0 (`l0`) | `h^0 q^0 δ^0 ⬮` | `h^-1 q^-1 δ^1/2 ⬮~~S^2~>⬮<—` r(0), mean q 0, δ| 1/2 |
| Q_∞ (`l1`) | `h^0 q^0 δ^0 ⬯` | `h^-1 q^-1 δ^1/2 ⬯~~S^2~>⬯<—` r(∞), mean q 0, δ_ 1/2 |
| Q_1 (`l1.y0`, also `l0.x1`) | `h^-1 q^-2 δ^0 ⬯~~S~>⬮` | `h^-2 q^-3 δ^1/2 ⬯~~S~>⬮—>⬮<~⬯<—` r(1), mean q -3/2, δ| 1/2 |
| Q_{1/2} (`l1.y0.y0`) | `h^-2 q^-4 δ^0 ⬯~~S~>⬮—>⬮` | `h^-3 q^-5 δ^1/2 ⬯~~S~>⬮—>⬮~>⬮<—⬮<~⬯<—` r(1/2), mean q -8/3, δ| 1/2 |

All are of length 1 (the program suppresses the length when it is 1). Further slopes ±1, ±2, ±1/2 are in
`out/rational/run.log`.

### 3.2 The (2,-3) pretzel tangle (`out/tests/PT2m3`, input `l1.x2.y0.x2.y0.x2.u1`, top `,1,1`)
- BN~: one non-compact component, 9 generators: `h^-2 q^-7 δ^-3/2 ⬮<—D——⬮<~⬯<—⬯~>⬮—>⬮~>⬮—>⬮~>⬯`.
- Kh~: `h^-5 q^-11 δ^-1/2 ⬯~~S~>⬮—>⬮~>⬮<—⬮<~⬯<—` = r(1/2), mean q -26/3, δ| -1/2 (6 generators);
  `h^-6 q^-13 δ^-1/2 ⬯~~S~>⬮—>⬮~>⬮—>⬮~>⬯—>⬯<~⬮<—⬮<~⬮<—⬮<~⬯<—` = s4(0), mean q -8, δ| -1 (12 generators).
  (The docs print δ| -1 for the rational component; the current build prints -1/2.)

### 3.3 Quotient tangles of strong inversions (`out/si/`, option `-q`)
Input files from the website: 3_1 = `s.l1.y0.y0.y1.u2`, 4_1-1 = `s.l1.y0.y0.x1.u2`, 4_1-2 = `s.l1.x0.x0.y1.u2`
(Sakuma's symmetries 1 and 2 of the 2-bridge knot 5/2). Without `-q` the program gives for 3_1:
`h^0 q^-2 ⬮`, `h^-3 q^-8 ⬮—H—>⬮`, i.e. Kh~ = q^-2 + q^-8 h^-3 + q^-6 h^-2: **the input knot is the left-handed
trefoil** (as [KWZ-SI] p.7 says of the first row of its Table 1).

| (K,h) | BN~ (single non-compact component) | Kh~ components |
|---|---|---|
| 3_1 (left-handed) | 11 gens: `h^0 q^10 δ^5 ⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯` | `h^3 q^15 δ^9/2 ⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬯<—⬯<~⬯<—⬯<~⬮<—` r(-4), mean q 96/5, δ| 9/2; `h^-1 q^9 δ^11/2 ⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮—>⬮<~⬯<—⬯<~⬯<—⬯<~⬮<—` s4(∞), mean q 14, δ_ 5 |
| 4_1-1 | 13 gens: `h^0 q^12 δ^6 ⬮~~S~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮` | `h^7 q^23 ⬮~~S^2~>⬮<—` r(0), mean q 24, δ| 9/2; s4(∞) first gen `h^3 q^17`, mean q 22, δ_ 5; s4(∞) first gen `h^-1 q^11`, mean q 16, δ_ 6 |
| 4_1-2 | 13 gens: `h^-8 q^-24 δ^-4 ⬮<—D——⬮~>⬯—>⬯~>⬯—>⬯~>⬮<—⬮~>⬯—>⬯~>⬯—>⬯~>⬮` | r(0), mean q -24, δ| -7/2; s4(∞) mean q -16, δ_ -5; s4(∞) mean q -22, δ_ -4 |

- In all three cases BN~ has exactly one component, which is non-compact, and **no compact components**.
- This reproduces [KWZ-SI] Theorem 3.1 / Table 1 (p.7): 3_1: k = -4, n = 1; 4_1 (both inversions): k = 0, n = 2,
  with their s_2(∞) = the program's s4(∞). The bigradings also match: from the two special components of 4_1-1
  (centres h = 2, 6; δ = 6, 5) Lemma 2.3 gives κ = h^{2.5}δ^{5.5}V_κ ⊕ h^{6.5}δ^{4.5}V_κ, which is exactly the value of
  κ(4_1^1) quoted in [KWZ-SI] Section 4 (p.10).
- The outputs for 4_1-1 and 4_1-2 are mirror images of each other (all gradings negated), as they should be for the
  two inversions of an amphichiral knot exchanged by the mirror symmetry.
- Over F_3 and Q the same chains appear (with signs on the first arrow).
- Explicit tangle word of the trefoil quotient (reconstructed from `Tangle::quotient()` and confirmed by identical
  output): `r1.r2.l1.l2.y0.y1.y1.y0.y0.y1.y1.y0.y2.y1.y3.y2.u4.u3.u0.y1.y1.y1.y1.y1.y1`, top `,0`
  (the last six letters are the framing correction, three pairs `y1.y1`; without them the rational component is r(2)).

Generator-level data (`out/parsed_generators.txt`). Trefoil quotient, with e_0 := [⬮], e_∞ := [⬯] and
χ = Σ (-1)^h q^q over generators:
- BN~: χ = (q^10 + q^16 - q^18) e_0 + (-q^11 + q^13 - q^15 + q^19 - q^21 + q^23) e_∞.
- r(-4): χ = (-q^15 + q^17) e_0 + (q^16 - 2q^18 + 2q^20 - 2q^22 + q^24) e_∞.
- s4(∞): χ = (-q^9 + q^11 + q^17 - q^19) e_0 + (q^10 - 2q^12 + 2q^14 - 2q^16 + q^18) e_∞
  = q^10 (1-q^2)^2 (1+q^4) · ( e_∞ - (q+q^{-1}) e_0 ).
- χ(Kh~) = (q - q^{-1}) χ(BN~) = χ(r) + χ(s), and χ(r(-4)) = (q - q^{-1}) (q^16 e_0 + (-q^17+q^19-q^21+q^23) e_∞).
- Same shape for every s4 seen: the pretzel s4(0) has χ = -q^{-12}(1-q^2)^2(1+q^4)·(e_0 - (q+q^{-1}) e_∞), and each
  s4(∞) of the figure-eight has χ = ±q^k (1-q^2)^2(1+q^4)·(e_∞ - (q+q^{-1}) e_0) (k = 12, 18 for 4_1-1).

## 4. Trefoil dictionary test

T denotes the `-q` quotient tangle of the left-handed trefoil (LHT), 1-3 form, as in 3.3.

### 4.1 Which component meets the unknot arc
Kh~(T) = r_1(-4) ∪ s4(∞). The arc of the unknot closure is a(∞). The special component has slope ∞ and pairs to
zero with it (decategorified check: the functional of the ∞-closure, e_0 -> 1, e_∞ -> q+q^{-1}, kills χ(s4(∞)) exactly);
the rational component has distance |(-4)·0 - 1·1| = 1 from ∞ and gives the one-dimensional Kh~ of the unknot.
The same rule gives the total rank of every closure computed below:
dim Kh~(T(s)) = Δ(s,-4) + 4Δ(s,∞) (with 2 in place of Δ(s,-4) when s = -4), Δ = distance of slopes. Checked for
s = ∞, 0, ±1,...,±7 and ±1/n, n ≤ 10 (ranks 8n-1 and 8n+1 for the two closures of slope ∓1/n).
In BN~(T) there is nothing to choose: its only component is the non-compact one.

### 4.2 Integer closures: identification of the slopes (`out/closures31/run_integer.log`)
| closure word | slope T(s) | CKh~ (towers; torsion pieces by order) | identification |
|---|---|---|---|
| `T.u1` | ∞ | `h^0 q^0 ⬮` | unknot |
| `T.u0` | 0 | towers (0,9), (8,23); H at (6,19), (2,13); H^2 at (4,15) | 2-component link, rank 8 |
| `T.x1.u0` | -1 | tower (0,8); H at (2,12), (6,18); H^2 at (4,14) | **T(3,5) = 10_124, positive** |
| `T.x1^2.u0` | -2 | towers (0,7), (6,17); H at (2,11); H^2 at (4,13) | link, rank 6 |
| `T.x1^3.u0` | -3 | tower (0,6); H at (2,10); H^2 at (4,12) | T(3,4) = 8_19 (rank 5) |
| `T.x1^4.u0` | -4 | towers (0,5), (4,11); H at (2,9), (4,13) | link, rank 6 |
| `T.x1^5.u0` | -5 | tower (0,4); H at (2,8), (4,12) | T(2,5) |
| `T.x1^6.u0` | -6 | towers (0,3), (2,7); H at (2,7), (4,11) | T(2,2)#T(2,3) (reducible surgery) |
| `T.x1^7.u0` | -7 | tower (0,2); H at (1,4), (2,6), (4,10) | 5_2 (rank 7, thin) |
| `T.y1.u0` | +1 | tower (0,10); H at (2,14), (6,20), (8,24); H^2 at (4,16) | **(-2,3,7) pretzel knot** (rank 9) |
| `T.y1^k.u0`, k=2..7 | +k | one more H piece each step; exactly one H^2, at (4,15+k) | rank 8+k (two towers for k even) |

The slope sign is fixed by the lens space and reducible closures: T(-5) = T(2,5), T(-6) = connected sum, T(-7) = 5_2
are the surgeries -5, -6, -7 on the LHT. So in this build **T(s) is the branch set of S^3_s(LHT)** with the printed
slope labels, consistent with [KWZ-SI] p.2-3, and T(-1) is the T(3,5) side.

Comparison with 10_124: from `T.x1.u0` (and identically from `T.y0.u1`),
Kh~ = q^8 + q^12 h^2 + q^14 h^3 + q^14 h^4 + q^18 h^5 + q^18 h^6 + q^20 h^7, rank 7. This is exactly the polynomial
in the brief, with no mirror or regrading needed. Jones polynomial q^8 + q^12 - q^20 (t^4 + t^6 - t^10).
The other distance-one closure T(+1): Kh~ = q^10 + q^14 h^2 + q^16 h^3 + q^16 h^4 + q^20 h^5 + q^20 h^6 + q^22 h^7
+ q^24 h^8 + q^26 h^9, rank 9, V = q^10 + q^14 - q^22 + q^24 - q^26 = t^5 + t^7 - t^11 + t^12 - t^13, the Jones
polynomial of the (-2,3,7) pretzel knot.

Observation (not asked): among the integer closures an H^2 summand is present exactly for s > -4, i.e. on one side of
the slope of the rational component; for s ≤ -4 all torsion has order 1.

### 4.3 The closures K_n of slope ∓1/n and their H-torsion (`run_1overn.log`, `run_1overn_6to10.log`)
`T.y0^n.u1` is the closure of slope -1/n (the T(3,5) side: n = 1 gives 10_124); `T.x0^n.u1` is slope +1/n
(n = 1 gives the (-2,3,7) pretzel knot). All are knots (one tower).

| n | slope -1/n: tower (h,q); torsion | rank | slope +1/n: tower; torsion | rank |
|---|---|---|---|---|
| 1 | (0,8); H ×2, H^2 ×1 | 7 | (0,10); H ×3, H^2 ×1 | 9 |
| 2 | (0,-2); H ×7 | 15 | (0,0); H ×8 | 17 |
| 3 | (0,8); H ×10, H^2 ×1 | 23 | (0,10); H ×11, H^2 ×1 | 25 |
| 4 | (0,-2); H ×15 | 31 | (0,0); H ×16 | 33 |
| 5 | (0,8); H ×18, H^2 ×1 | 39 | (0,10); H ×19, H^2 ×1 | 41 |
| 6 | (0,-2); H ×23 | 47 | (0,0); H ×24 | 49 |
| 7 | (0,8); H ×26, H^2 ×1 | 55 | (0,10); H ×27, H^2 ×1 | 57 |
| 8 | (0,-2); H ×31 | 63 | (0,0); H ×32 | 65 |
| 9 | (0,8); H ×34, H^2 ×1 | 71 | (0,10); H ×35, H^2 ×1 | 73 |
| 10 | (0,-2); H ×39 | 79 | (0,0); H ×40 | 81 |

- For odd n there is exactly one H^2 summand, always at source bigrading (4,14) on the -1/n side and (4,16) on the
  +1/n side (for n ≤ 5, where full lists were inspected); for even n all torsion has order 1. No torsion of order ≥ 3
  occurs anywhere. Identical over F_3 and Q for n ≤ 3.
- The tower position (the reduced s-invariant in this normalization) alternates with the parity of n: 8 / -2 on the
  -1/n side, 10 / 0 on the +1/n side. This is consistent: K_n and K_{n+2} differ by a full twist on two strands, i.e. a
  crossing change, and K_0 is the unknot.
- Jones polynomials (t = q^2), from the towers and torsion pairs: V(K_1) = q^8 + q^12 - q^20;
  V(K_2) = -q^-18 + q^-16 - q^-14 + q^-12 + q^-6 - q^-4 + q^-2; V(K_{-1}) = q^10 + q^14 - q^22 + q^24 - q^26;
  V(K_{-2}) = q^-14 - q^-12 + q^-10 - q^-8 - q^-2 + 2 - q^2 + q^4 (K_{-n} := slope +1/n). Higher n in
  `out/closures31/pairing_check.log`.

### 4.4 The decategorified pairing, tested (`out/scripts/pairing_check.py`, `out/closures31/pairing_check.log`)
Write a class in the skein module as x_0 e_0 + x_∞ e_∞ (e_0 = [⬮], e_∞ = [⬯]). Unshifted Khovanov bracket of an
appended crossing on (b1,b2): `y0`: e_∞ -> e_∞ - q e_0, e_0 -> -q^2 e_0; `x0`: e_∞ -> e_0 - q e_∞, e_0 -> q^{-1} e_0.
Closure `u1`: e_0 -> 1, e_∞ -> q + q^{-1} (`u0`: the other way round). Then, for all ten closures n = 1..5 on both
sides,

  V(K_n) = ± q^k · closure( twist^n ( χ(BN~(T)) ) ) = ± q^k · closure( twist^n ( χ(Kh~(T)) ) ) / (q - q^{-1}),

with a unit ±q^k that depends only on orientations. So χ(BN~(T)) is the Kauffman bracket vector [T] in this basis, and
the components of Kh~(T) split the Jones polynomial into two Laurent polynomials. Example, n = 1 on the T(3,5) side:
V = q^8 + q^12 - q^20 = (q^14 + q^18 - q^20) + (q^8 + q^12 - q^14 - q^18), the first bracket from r(-4) (it is
q^14 times the Jones polynomial of a trefoil, the 2-bridge closure of Q_{-4}), the second from s4(∞).
In closed form the s4(∞) contribution on the -1/n side is

  ± q^k (1+q^4)(1-q^6) · (1 - (-q^2)^n)/(1+q^2),

obtained from χ(s4(∞)) = q^10(1-q^2)^2(1+q^4)(e_∞ - (q+q^{-1})e_0); it is 0 for n = 0 (the unknot closure),
nonzero for every n ≥ 1, vanishes at q = 1 and equals ±4n at q^2 = -1 (so that det = (4n-1) - 4n in absolute value 1).
For the unknot closure `T.u1` the same recipe gives q^24 from the rational component alone; the actual output is
h^0 q^0, the discrepancy h^8 q^24 being the orientation shift mentioned in 2.4.

## 5. Claim checks

- **C1 (modified).** "Exactly one non-compact component": true for BN~(T_{3_1}) (and for both figure-eight
  inversions), and it is general: [KWZ-SI] p.4 (after Fig. 5) recalls from [KWZ, Section 6] that BN~(T) has exactly one
  non-compact component when T has no closed component, and Kh~(T) only compact ones. "The compact components all have
  the slope of the unknot closure": BN~(T_{3_1}) has no compact component at all (one chain with 11 generators). In
  Kh~(T_{3_1}) there are two compact components: the special one s4(∞) (= s_2(∞) of [KWZ-SI]) has the unknot slope ∞,
  but the rational one r_1(-4) does not (slope -4 for the left-handed trefoil, +4 for the right-handed one; [KWZ-SI]
  Example 2.1 p.5, Table 1 and the paragraph after Theorem 3.1 p.7). The correct statement, which [KWZ-SI] p.7 gives
  as a consequence of the unknot closure plus the expected geography of components (and as a computer-verified theorem
  only for knots up to 9 crossings, Theorem 3.1, over F_2): Kh~(T_{K,h}) = r_1(k) ∪ specials of slope ∞, k an integer (in 4Z in all computed
  cases; whether always is Questions 3.3, open).
- **C2 (confirmed, by computation).** The closure of slope -1/1 (T(3,5) = 10_124) has BN~ = F[H] ⊕ (F[H]/H)^2 ⊕
  F[H]/H^2, the H^2 summand at source bigrading h^4 q^14 (it is forced by the pair q^14 h^4, q^18 h^5 of Kh~).
  Closures of slope ∓1/n with n even have only order-one torsion for n = 2,...,10, on both sides; odd n have exactly one
  order-two summand, n = 1,...,9, on both sides. Field F_2; same over F_3 and Q where rerun (n ≤ 3). This is evidence
  for n ≤ 10, not a proof for all n.
- **C3 (confirmed, with the normalization made explicit).** BN~(T_{3_1}) has no compact part, so the statement is
  about the special component of Kh~. Its graded Euler characteristic in the skein module is
  q^10(1-q^2)^2(1+q^4)(e_∞ - (q+q^{-1})e_0) ≠ 0; paired with the arc of slope -1/n it contributes
  ±q^k(1+q^4)(1-q^6)(1-(-q^2)^n)/(1+q^2) to V(K_n) (after dividing by q - q^{-1}), a nonzero Laurent polynomial for
  every n ≥ 1; on the +1/n side the contributions for n ≤ 5 are also nonzero (log). It is zero when paired with the
  unknot arc a(∞), as it must be. Note that it always vanishes at q = 1 and that nonvanishing of this piece does not by
  itself say anything about V(K_n) ≠ 1, since the rational piece is another Laurent polynomial of the same size.

## 6. Surprises and open points

1. Both distance-one closures, not only the T(3,5) one, carry an H^2 summand, and the parity pattern in n holds on both
   sides up to n = 10. Among integer closures H^2 appears exactly for slopes s > -4 (the rational slope).
2. Idempotent symbols and the shape of the `-q` tangle changed between the website's stored 2021 outputs and the current
   repository; the special-curve index differs by a factor 2 between kht++/thin-links (s4) and [KWZ-SI] (s_2).
3. By the Montesinos trick a crossing change is a rational tangle replacement at distance 2, so the closures obtained
   from the unknot τ(∞) by one crossing change are those of slope ±1/2 (n = ±2), not all the K_n; K_{±1} = T(3,5),
   (-2,3,7) pretzel are not at unknotting distance one from τ(∞). The brief's formulation of "Lemma Q" in terms of all
   K_n should be checked against this (I did not look for a source for the equivalence). In the data, K_{±2} have
   only order-one H-torsion, which is what the known bound "maximal H-torsion order ≤ unknotting number"
   (Alishahi, Alishahi-Dowlin; quoted from memory, not checked here) forces for unknotting number one.
4. [KWZ-SI] Remark 3.10 (p.9): over Z/3 the picture changes (their example 7_4, second inversion: r_1(6), two s_2(∞)
   and five s_1(∞)); the divisibility of k by 4 and the conjectures on specials are F_2 statements. For the trefoil and
   figure-eight I saw no field dependence.

Open questions for the mathematician:
- Is the parity statement (one H^2 summand iff n odd) provable from the curve picture (a(1/n) is congruent to a(∞) mod 2
  exactly when n is even)? The data suggest a uniform mechanism localized at h = 4.
- The factor (1-q^2)^2(1+q^4) of χ(s4) is the same for all five s4 components seen (slopes 0 and ∞); is
  χ(s_{4n}(s)) = ±q^k (1-q^2)^2 (1+q^4+...+q^{8n-4})·(kernel vector of the slope-s closure) in general? Not tested for
  n > 1 (no example with a longer special component was run).

## 7. File index
- `src/khtpp/` program source and binary; `src/libraries/eigen-3.4.0/`; `src/web/` website pages and input files;
  `src/arxiv/` TeX of 2104.13592v1 and 1910.14584v2.
- `out/rational/`, `out/rational22/` rational tangles (1-3 and 2-2 inputs), `run.log` in each.
- `out/tests/` the two bundled examples. `out/si/` quotient tangles (`run_q.log`, `run_otherfields.log`);
  `out/si_knot/` the symmetric knots themselves; `out/si_explicit/` framing reconstruction.
- `out/closures31/` all closures of the trefoil quotient: `c_u1`, `c_u0`, `c_x1<k>_u0`, `c_y1<k>_u0` (k = 1..7),
  `c_y0<n>_u1`, `c_x0<n>_u1` (n = 1..10); logs `run_integer.log`, `run_1overn.log`, `run_1overn_6to10.log`,
  `pairing_check.log`. Each computed closure has a folder with the raw file `cxCKh-c2` (and `-c3`, `-c0` where rerun).
- `out/scripts/khtparse.py` (chain parser, generator gradings, Euler vectors), `out/scripts/pairing_check.py`.
- `out/parsed_generators.txt` generator-level gradings for the rational tangles and the figure-eight quotients.
