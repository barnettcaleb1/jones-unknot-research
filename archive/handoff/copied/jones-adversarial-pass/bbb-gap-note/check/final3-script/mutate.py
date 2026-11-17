#!/usr/bin/env python3
"""Mutation tests for the NEW/CHANGED checks of phi0_check.py.  Each mutant is a copy of the shipped script
with one plausible edit; we run it with python3 -I and record exit status and which checks FAIL."""
import os, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '..', 'phi0_check.py')
base = open(SRC).read()
MUT = os.path.join(HERE, 'mut')

# (name, target-label-prefix that must FAIL, list of (old, new) replacements)
MUTANTS = [
 ('S1_Uinv_sign', '(S) U, UT, R, RT satisfy',
  [("[[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]", "[[{}, {0: 1}], [{-1: 1}, {0: 1, -1: 1}]]")]),
 ('S2_R_rowcut_B5only', '(S) U, UT, R, RT satisfy',
  [("if 0 <= c < n - 1: M[r][c] = v", "if 0 <= c < 3: M[r][c] = v")]),
 ('S3_REL_adjacent_commute', '(S) U, UT, R, RT satisfy',
  [("for j in range(i + 2, n)]", "for j in range(i + 1, n)]")]),
 ('S4_U_is_transposed', '(S) for every letter',
  [("return [list(x) for x in zip(*M)] if conv.endswith('T') else M",
    "return M if conv.endswith('T') else [list(x) for x in zip(*M)]")]),
 ('S5_U_at_inverse_t', '(S) for every letter',
  [("[[{0: 1, 1: -1}, {1: 1}], [{0: 1}, {}]] if a > 0 else [[{}, {0: 1}], [{-1: 1}, {0: 1, -1: -1}]]",
    "[[{0: 1, -1: -1}, {-1: 1}], [{0: 1}, {}]] if a > 0 else [[{}, {0: 1}], [{1: 1}, {0: 1, 1: -1}]]")]),
 ('S6_artin_inverse_typo', '(S) for every letter',
  [("{i: [i + 1], i + 1: [-i - 1, i, i + 1]}", "{i: [i + 1], i + 1: [i + 1, i, -i - 1]}")]),
 ('T1_TVALS_half_to_one', '(6) B_4 U ',
  [("TVALS = (Fraction(2), Fraction(1, 2), Fraction(3), Fraction(1, 3))",
    "TVALS = (Fraction(2), Fraction(1), Fraction(3), Fraction(1, 3))")]),
 ('T2_identity_at_half_only', '(6) B_4 U ',
  [("def is_I(M):", "_at0 = at\nat = lambda M, t: [[Fraction(i == j) for j in range(len(M))] for i in range(len(M))] if Fraction(t) == Fraction(1, 2) else _at0(M, t)\ndef is_I(M):")]),
 ('T3_identity_at_third_only', '(6) B_5 RT',
  [("def is_I(M):", "_at0 = at\nat = lambda M, t: [[Fraction(i == j) for j in range(len(M))] for i in range(len(M))] if Fraction(t) == Fraction(1, 3) else _at0(M, t)\ndef is_I(M):")]),
 ('T4_trivial_braid_in_loop', '(6) B_4 U ',
  [("        M = burau(Phi0, n, conv)", "        M = burau(Phi0 + inv(Phi0), n, conv)")]),
 ('D1_delta_order', '(10) delta == A14 A24 A34',
  [("trivial(delta + inv(A14 + A24 + A34), 4)", "trivial(delta + inv(A24 + A14 + A34), 4)")]),
 ('D2_kw_delta_plus2', '(10) in the free basis',
  [("kw = red(comm([-3, -2, -1] * 2,", "kw = red(comm([1, 2, 3] * 2,")]),
 ('D3_kw_wrong_inverse_order', '(10) in the free basis',
  [("kw = red(comm([-3, -2, -1] * 2,", "kw = red(comm([-1, -2, -3] * 2,")]),
 ('D4_kw_exponent_sum', '(10) in the free basis',
  [("kw = red(comm([-3, -2, -1] * 2, comm(comm([1], [2]), [3])))   # same word in the free basis a_i = A_i4",
    "kw = red(comm([-3, -2, -1] * 2, comm(comm([1], [2]), [3]))); kw = kw[:-1] + [-kw[-1]]")]),
 ('M1_mirror_factor_plus3', '(11) with every half twist reversed',
  [("pmul({0: 1, -3: 1}, p)", "pmul({0: 1, 3: 1}, p)")]),
 ('M2_mirror_is_identity', '(11) with every half twist reversed',
  [("mirror = lambda w: [-a for a in w]", "mirror = lambda w: w")]),
 ('M3_mirror_is_inverse_EQUIVALENT', None,
  [("mirror = lambda w: [-a for a in w]", "mirror = lambda w: inv(w)")]),
 ('C1_conj_is_square', '(12) U(Phi0) and U(s3 Phi0 s3^-1) do not commute',
  [("s3conj = [3] + Phi0 + [-3]", "s3conj = Phi0 + Phi0")]),
 ('C2_depth_second_commutator', '(12) [Phi0, s3 Phi0 s3^-1] has',
  [("dC = depth(burau(comm(Phi0, s3conj), 4, 'U'))", "dC = depth(burau(comm(Phi0, comm(Phi0, s3conj)), 4, 'U'))")]),
 ('C3_depth_in_R', '(12) [Phi0, s3 Phi0 s3^-1] has',
  [("dC = depth(burau(comm(Phi0, s3conj), 4, 'U'))", "dC = depth(burau(comm(Phi0, s3conj), 4, 'R'))")]),
 ('C4_depth_in_RT', '(12) [Phi0, s3 Phi0 s3^-1] has',
  [("dC = depth(burau(comm(Phi0, s3conj), 4, 'U'))", "dC = depth(burau(comm(Phi0, s3conj), 4, 'RT'))")]),
 ('C5_depth_in_UT', None,
  [("dC = depth(burau(comm(Phi0, s3conj), 4, 'U'))", "dC = depth(burau(comm(Phi0, s3conj), 4, 'UT'))")]),
 ('C6_trivial_commutator', '(12) [Phi0, s3 Phi0 s3^-1] has',
  [("dC = depth(burau(comm(Phi0, s3conj), 4, 'U'))", "dC = depth(burau(comm(Phi0, Phi0), 4, 'U'))")]),
 ('P1_MGamma_sign', '(13) paper Sec. 7',
  [("(-1, 2), (1, 3), (1, 1), (1, -1), (-1, -2),", "(-1, 2), (-1, 3), (1, 1), (1, -1), (-1, -2),")]),
 ('P2_MPhiGamma_exponent', '(13) paper Sec. 7',
  [("(1, -4), (1, -2), (1, 0)]", "(1, -3), (1, -2), (1, 0)]")]),
 ('P3_MPhi_drop_term', '(13) paper Sec. 7',
  [("(1, -3), (1, -1), (1, 1)]", "(1, -3), (1, -1)]")]),
 ('P4_MPhi_no_cancellation', '(13) eps_i (-1)^k_i is constant',
  [("M_Phi = [(1, 0), (1, 2), (1, 4), (-1, 3), (-1, 1), (1, -3), (1, -1), (1, 1)]",
    "M_Phi = [(1, 0), (1, 2), (1, 4), (-1, 3), (-1, 1), (-1, -3), (-1, -1), (-1, 1)]")]),
 ('P5_MGamma_parity_preserving_typo_BLINDSPOT', None,
  [("M_Gamma = [(-1, 0), (-1, 2), (1, 1), (1, -1),", "M_Gamma = [(-1, 0), (-1, 2), (1, 1), (1, 1),")]),
 ('X1_exit_status', '(4) unreduced concatenation',
  [("len(Phi0) == 112)", "len(Phi0) == 113)")]),
]
rows = []
for name, target, reps in MUTANTS:
    s = base
    for old, new in reps:
        assert s.count(old) == 1, (name, old, s.count(old))
        s = s.replace(old, new)
    path = os.path.join(MUT, name + '.py')
    open(path, 'w').write(s)
    t0 = time.time()
    r = subprocess.run([sys.executable, '-I', path], capture_output=True, text=True, timeout=600)
    dt = time.time() - t0
    fails = [l[6:] for l in r.stdout.splitlines() if l.startswith('FAIL  ')]
    open(os.path.join(MUT, name + '.out'), 'w').write(r.stdout + r.stderr)
    hit = (target is None and r.returncode == 0 and not fails) or \
          (target is not None and r.returncode == 1 and any(f.startswith(target) for f in fails))
    rows.append((name, target, r.returncode, len(fails), hit, dt, fails, r.stderr.strip()[-200:]))
for name, target, rc, nf, hit, dt, fails, err in rows:
    print(f"{'KILLED ' if target and hit else ('EQUIV-OK ' if hit else 'SURVIVED')} {name:45s} exit={rc} fails={nf:2d} {dt:5.1f}s target={target!r}")
    for f in fails[:12]: print('        FAIL', f)
    if len(fails) > 12: print('        ...', len(fails) - 12, 'more')
    if err: print('        stderr:', err)
print('\nall mutants behaved as expected:', all(r[4] for r in rows))
