import sys, json, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from tl6 import *

t0 = time.time()
out = {}
I = complex(0, 1)

def lstr_short(p):
    return lstr(p)

# ---------- 1. sanity: relations ----------
def ev(i, v):
    return e_vec(i, v)
basis_vecs = []
for j in range(DIM):
    v = vzero(); v[j] = dict(ONE); basis_vecs.append(v)
for v in basis_vecs:
    for i in range(1, 6):
        assert vec_eq(ev(i, ev(i, v)), [lmul(DELTA, x) for x in ev(i, v)])
        if i < 5:
            assert vec_eq(ev(i, ev(i + 1, ev(i, v))), ev(i, v))
            assert vec_eq(ev(i + 1, ev(i, ev(i + 1, v))), ev(i + 1, v))
            assert vec_eq(rho_vec([i, i + 1, i], v), rho_vec([i + 1, i, i + 1], v))
        assert vec_eq(rho_vec([i, -i], v), v)
    # far commutation
    assert vec_eq(rho_vec([1, 3], v), rho_vec([3, 1], v))
# H invariance, G e-symmetry
for a in basis_vecs:
    for b in basis_vecs:
        for g in (1, 2, 3, 4, 5, -3):
            assert Hform(rho_vec([g], a), rho_vec([g], b)) == Hform(a, b)
        for i in range(1, 6):
            assert Gform(ev(i, a), b) == Gform(a, ev(i, b))
out['basis'] = [str(m) for m in BASIS]
print("basis (partner tuples, points 0..5):", BASIS)
print("relations, H-invariance, G e-symmetry: OK")

# Gram determinant (nondegeneracy), via fraction-free elimination on Laurent polys -> just evaluate at random A
from fractions import Fraction
def det_eval(Mx):
    n = len(Mx); M = [row[:] for row in Mx]; d = Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]; d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return d
for Aval in (Fraction(2), Fraction(3, 2), Fraction(5, 7)):
    Gm = [[leval(GRAM[i][j], Aval) for j in range(DIM)] for i in range(DIM)]
    assert det_eval(Gm) != 0
print("Gram determinant nonzero at A=2,3/2,5/7")

# ---------- 2. full twist on {1,2,3} ----------
FT123 = [1, 2, 1, 2, 1, 2]
FT456 = [4, 5, 4, 5, 4, 5]
T = rho_mat(FT123)
T456 = rho_mat(FT456)
Am6 = mono(-6); Ap6 = mono(6)
Mm = [[ladd(T[i][j], Am6 if i == j else {}, -1) for j in range(DIM)] for i in range(DIM)]  # T - A^-6
Mp = [[ladd(T[i][j], Ap6 if i == j else {}, -1) for j in range(DIM)] for i in range(DIM)]  # T - A^6
# (T - A^6)(T - A^-6) = 0
for j in range(DIM):
    col = [Mm[i][j] for i in range(DIM)]
    assert all(x == {} for x in mat_vec(Mp, col))
# v_c := a nonzero column of T - A^-6, made primitive
cols = [[Mm[i][j] for i in range(DIM)] for j in range(DIM)]
vc = next(c for c in cols if any(c))
g = 0
lo = min(min(x) for x in vc if x)
for x in vc:
    g = math.gcd(g, content(x))
vc = [lscale(x, 1, 0) for x in vc]
vc = [{e - lo: c // g for e, c in x.items()} for x in vc]
# make primitive over Q[A^+-1]: divide by polynomial gcd of all entries
_g = None
for x in vc:
    if x:
        _s, _a = to_poly(x)
        _g = _a if _g is None else poly_gcd(_g, _a)
print("polynomial gcd of raw column:", _g)
_new = []
for x in vc:
    if not x:
        _new.append({}); continue
    _s, _a = to_poly(x)
    _q = poly_exact_div(_a, _g)
    _new.append({_s + k: c for k, c in enumerate(_q) if c})
vc = _new
# centre exponents so that v_c is bar-symmetric if possible
_lo = min(min(x) for x in vc if x); _hi = max(max(x) for x in vc if x)
_sh = -(_lo + _hi) // 2
vc = [{e + _sh: c for e, c in x.items()} for x in vc]
print("v_c bar-symmetric:", all(lbar(x) == x for x in vc))
# also every column of T - A^-6 is a multiple of vc (rank 1): check 2x2 minors
def proportional(u, w):
    for i in range(DIM):
        for j in range(i + 1, DIM):
            if ladd(lmul(u[i], w[j]), lmul(u[j], w[i]), -1) != {}:
                return False
    return True
assert all(proportional(vc, c) for c in cols)
assert vec_eq(mat_vec(T, vc), [lmul(Ap6, x) for x in vc])
# the A^-6 eigenspace = image of (T - A^6), dimension 4 (check rank by evaluation)
img = [[Mp[i][j] for i in range(DIM)] for j in range(DIM)]
def rank_eval(vecs, Aval):
    M = [[leval(x, Aval) for x in v] for v in vecs]
    # rank of rows
    M = [row[:] for row in M]; r = 0; ncol = DIM
    for c in range(ncol):
        piv = next((k for k in range(r, len(M)) if M[k][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for k in range(len(M)):
            if k != r and M[k][c] != 0:
                f = M[k][c] / M[r][c]
                M[k] = [M[k][t] - f * M[r][t] for t in range(ncol)]
        r += 1
    return r
print("rank(T-A^6) at A=2:", rank_eval(img, Fraction(2)), " rank(T-A^-6):", rank_eval(cols, Fraction(2)))
# full twist on {4,5,6} has the same rank-one line
vc456 = next([T456[i][j] if i != j else ladd(T456[i][j], Am6, -1) for i in range(DIM)] for j in range(DIM)
             if any([T456[i][j] if i != j else ladd(T456[i][j], Am6, -1) for i in range(DIM)]))
print("T_{456} same line as T_{123}:", proportional(vc, vc456), "; T123 == T456 exactly:",
      all(T[i][j] == T456[i][j] for i in range(DIM) for j in range(DIM)))
print("v_c (matching basis):")
for m, x in zip(BASIS, vc):
    pairs = sorted({tuple(sorted((a + 1, m[a] + 1))) for a in range(N)})
    print("   ", pairs, ":", lstr(x))
out['v_c'] = {str(sorted({tuple(sorted((a + 1, m[a] + 1))) for a in range(N)})): lstr(x) for m, x in zip(BASIS, vc)}

# H- and G-orthogonality of sectors
Horth = all(Hform(vc, c) == {} for c in img)
Gorth = all(Gform(vc, c) == {} for c in img)
print("H(v_c, A^-6-sector)=0:", Horth, "  G(v_c, A^-6-sector)=0:", Gorth)
nH = Hform(vc, vc); nG = Gform(vc, vc)
print("H(v_c,v_c) =", lstr(nH), "  =", fstr(factor_cyclo(nH)))
print("G(v_c,v_c) =", lstr(nG), "  =", fstr(factor_cyclo(nG)))
print("H(v_c,v_c) bar-symmetric:", lbar(nH) == nH)
out['H_vc_vc'] = lstr(nH); out['G_vc_vc'] = lstr(nG)
# pseudo-reflection formula: H(vc,vc)*(T - A^-6) x == (A^6 - A^-6) * vc * H(vc, x)
kap = ladd(Ap6, Am6, -1)
ok = True
for j, x in enumerate(basis_vecs):
    lhs = [lmul(nH, Mm[i][j]) for i in range(DIM)]
    hx = Hform(vc, x)
    rhs = [lmul(lmul(kap, x_), hx) for x_ in vc]
    ok &= vec_eq(lhs, rhs)
print("T_c = A^-6 (1 + (A^12-1) P_c), P_c = v_c H(v_c,.)/H(v_c,v_c):", ok)

# ---------- 3. overlaps ----------
def rat_reduce(num, den):
    s1, a = to_poly(num); s2, b = to_poly(den)
    gg = poly_gcd(a, b)
    a2 = poly_exact_div(a, gg); b2 = poly_exact_div(b, gg)
    return (s1 - s2), a2, b2
def poly_to_laurent(shift, a):
    return {shift + k: c for k, c in enumerate(a) if c}
def rat_str(num, den):
    sh, a, b = rat_reduce(num, den)
    N_ = poly_to_laurent(sh, a); D_ = poly_to_laurent(0, b)
    return N_, D_
def eval_c(p, z):
    return sum(c * z ** e for e, c in p.items())

PHIS = [("s3", [3]), ("s3 s2", [3, 2]), ("s3 s4", [3, 4]), ("s3^2", [3, 3]),
        ("s3 s2 s4 s3", [3, 2, 4, 3]), ("s3^-1 s2 s3", [-3, 2, 3]),
        ("s3 s3 s2 s4 s3 s3", [3, 3, 2, 4, 3, 3])]
EXTRA = [("s3^%d" % k, [3] * k) for k in (3, 4, 5, 6)] + \
        [("s3^-1", [-3]), ("s3^-2", [-3, -3]),
         ("(s3 s2 s4 s3)^2", [3, 2, 4, 3] * 2), ("(s3^-1 s2 s3)^2", [-3, 2, 3] * 2),
         ("s3 s2^-1", [3, -2]), ("s3^2 s2^2", [3, 3, 2, 2]),  # second one: T_d then (s2^2 fixes c)
         ("s2 s3^2 s2^-1", [2, 3, 3, -2]), ("s3^2 s4^2", [3, 3, 4, 4]),
         ("s3^2 s2 s3^2", [3, 3, 2, 3, 3]), ("s3 s2 s3", [3, 2, 3]),
         ("s3^2 s2^-1 s4^-1 s3^2", [3, 3, -2, -4, 3, 3]), ("s3^-2 s2 s4 s3^2", [-3, -3, 2, 4, 3, 3]),
         ("s3^2 s1 s3^2", [3, 3, 1, 3, 3]), ("s3^2 s5 s3^2", [3, 3, 5, 3, 3])]
res = []
for label, w in PHIS + EXTRA:
    wv = rho_vec(w, vc)
    h = Hform(vc, wv)
    assert Hform(wv, wv) == nH, label
    collinear = proportional(vc, wv)
    num = lmul(h, lbar(h)); den = lmul(nH, nH)
    Ng, Dg = rat_str(num, den)
    # 1 - gamma numerator
    one_minus = ladd(den, num, -1)
    N1, D1 = rat_str(one_minus, den) if one_minus else ({}, {0: 1})
    gG_num = lmul(Gform(vc, wv), Gform(vc, wv)); gG_den = lmul(nG, Gform(wv, wv))
    NG, DG = rat_str(gG_num, gG_den) if gG_num else ({}, {0: 1})
    gam_i = eval_c(num, I) / eval_c(den, I)
    gamG_i = (eval_c(gG_num, I) / eval_c(gG_den, I)) if gG_num else 0
    rec = dict(label=label, word=w, collinear=collinear,
               H_vc_w=lstr(h), H_span=span(h), H_spanwidth=(span(h)[1] - span(h)[0]) if h else None,
               H_factor=fstr(factor_cyclo(h)) if h else "0",
               gamma_num=lstr(Ng), gamma_den=lstr(Dg),
               gamma_num_factor=fstr(factor_cyclo(Ng)) if Ng else "0",
               gamma_den_factor=fstr(factor_cyclo(Dg)),
               one_minus_gamma_num_factor=fstr(factor_cyclo(N1)) if N1 else "0",
               gamma_at_A_eq_i=round(gam_i.real, 12),
               gammaG_num=lstr(NG), gammaG_den=lstr(DG), gammaG_at_i=round(complex(gamG_i).real, 12),
               G_w_w_equals_G_vc_vc=(Gform(wv, wv) == nG))
    res.append(rec)
    print("\n==", label, w)
    for k in ("collinear", "H_vc_w", "H_span", "H_spanwidth", "H_factor", "gamma_num_factor",
              "gamma_den_factor", "one_minus_gamma_num_factor", "gamma_at_A_eq_i", "gammaG_at_i",
              "G_w_w_equals_G_vc_vc"):
        print("   ", k, ":", rec[k])
out['overlaps'] = res
# distinct gamma classes
classes = {}
for r in res:
    classes.setdefault((r['gamma_num'], r['gamma_den']), []).append(r['label'])
print("\nDistinct gamma values (H-version):")
for k, v in classes.items():
    print("  ", v)
    print("      gamma =", k[0], " / ", k[1])
classesG = {}
for r in res:
    classesG.setdefault((r['gammaG_num'], r['gammaG_den']), []).append(r['label'])
print("\nDistinct gamma values (naive bilinear G-version):", len(classesG))
for k, v in classesG.items():
    print("  ", v)
out['seconds'] = time.time() - t0
json.dump(out, open(__file__.rsplit('/', 1)[0] + '/run_sep_out.json', 'w'), indent=1, default=str)
print("seconds", out['seconds'])
