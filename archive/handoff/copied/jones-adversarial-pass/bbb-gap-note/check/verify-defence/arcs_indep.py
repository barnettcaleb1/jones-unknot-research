# Independent re-implementation (verify-defence lens) of the arc / disk-sequence computation.
# It shares no code with check/defence/*.py and uses a DIFFERENT cut system and method:
#
#   * punctures p1..p4 on a horizontal line, base point p* on the bottom boundary (paper Fig. 2.2);
#   * cuts c_j = vertical ray from p_j UP to the top boundary; the complement Omega is one disk;
#   * x_j = clockwise loop at p* that crosses c_j once, left to right (letter +j); -j = right to left;
#   * sigma_i = counterclockwise half twist of p_i, p_{i+1}; its push-forward on loops (derived by hand):
#         x_i -> x_{i+1},   x_{i+1} -> x_{i+1}^-1 x_i x_{i+1}          (inverse: x_i -> x_i x_{i+1} x_i^-1, x_{i+1} -> x_i)
#     braid words act on the right (first letter first), as in the paper;
#   * the arc beta = (beta*_3)Phi is read off the reduced loop word u x_3 u^-1 of (x_3)Phi; the pieces of beta
#     between cut crossings are chords of Omega.  alpha = [p1,p2] is NOT a cut: a chord crosses alpha iff
#     exactly one of its ends lies on the sides {c1-right, c2-left} (the strip above alpha); sign +1 when the
#     chord leaves that strip (beta points down), -1 when it enters it.
#   * the disk Delta_i between consecutive alpha-points: winding number about p_j = net exponent of x_j in the
#     letters of u crossed between the two chords (alpha_i crosses no cut).
#
# Validation, independent of the chord logic: (1 - t3) * sum_i eps_i T^{K_i}  ==  t1 * dw/dx1 - dw/dx2
# (multivariable Fox calculus on w = (x_3)Phi, x_j -> t_j), Lemma 6.1 on every disk, and embeddedness.
import sys
from fractions import Fraction

N = 4

def red(w):
    out = []
    for a in w:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return out

def inv(w):
    return [-a for a in reversed(w)]

def twist_map(i, s):
    if s > 0:
        return {i: [i + 1], i + 1: [-(i + 1), i, i + 1]}
    return {i: [i, i + 1, -i], i + 1: [i]}

def subst(w, m):
    out = []
    for a in w:
        img = m.get(abs(a))
        if img is None:
            seg = [a]
        else:
            seg = img if a > 0 else inv(img)
        for b in seg:
            if out and out[-1] == -b:
                out.pop()
            else:
                out.append(b)
    return out

def image(braid, w):
    for g in braid:
        w = subst(w, twist_map(abs(g), 1 if g > 0 else -1))
    return w

def automorphism(braid, n=N):
    return {j: image(braid, [j]) for j in range(1, n + 1)}

# ---- homological Burau = Fox Jacobian of the automorphism, evaluated at a rational t ----
def fox_row_at(w, n, t):
    t = Fraction(t)
    row = [Fraction(0)] * n
    e = 0
    for a in w:
        j = abs(a) - 1
        if a > 0:
            row[j] += t ** e
            e += 1
        else:
            e -= 1
            row[j] -= t ** e
    return row

def fox_matrix_at(braid, n, t):
    A = automorphism(braid, n)
    return [fox_row_at(A[j], n, t) for j in range(1, n + 1)]

def is_identity(M):
    return all(M[i][j] == (1 if i == j else 0) for i in range(len(M)) for j in range(len(M)))

# ---- standard unreduced Burau, evaluated at rational t (a second, unrelated check) ----
def burau_at(braid, n, t):
    t = Fraction(t)
    M = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for g in braid:
        i = abs(g) - 1
        if g > 0:
            blk = [[1 - t, t], [Fraction(1), Fraction(0)]]
        else:
            blk = [[Fraction(0), Fraction(1)], [1 / t, 1 - 1 / t]]
        G = [[Fraction(int(r == c)) for c in range(n)] for r in range(n)]
        for r in range(2):
            for c in range(2):
                G[i + r][i + c] = blk[r][c]
        M = [[sum(M[r][k] * G[k][c] for k in range(n)) for c in range(n)] for r in range(n)]
    return M

# ---- the arc ----
STRIP = {(1, 'R'), (2, 'L')}   # cut sides bounding the region just above alpha

def entry_side(a):
    return (abs(a), 'L') if a > 0 else (abs(a), 'R')

def exit_side(a):
    return (abs(a), 'R') if a > 0 else (abs(a), 'L')

def arc_word(braid, end=3):
    w = image(braid, [end])
    L = len(w)
    assert L % 2 == 1
    h = (L - 1) // 2
    u, mid, ub = w[:h], w[h], w[h + 1:]
    assert mid == end and ub == inv(u), "loop word is not u x_end u^-1"
    assert not u or abs(u[-1]) != end
    return w, u

def analyse(braid, end=3, n=N):
    w, u = arc_word(braid, end)
    ends = ['P*'] + [exit_side(a) for a in u]
    starts = [entry_side(a) for a in u] + ['P3']
    K = [0] * n
    pts = []          # (chord index, eps, label vector)
    for c in range(len(u) + 1):
        s, e = ends[c], starts[c]
        ins, ine = s in STRIP, e in STRIP
        if ins != ine:
            pts.append((c, +1 if ins else -1, tuple(K)))
        if c < len(u):
            K[abs(u[c]) - 1] += 1 if u[c] > 0 else -1
    disks = []
    for (ca, ea, Ka), (cb, eb, Kb) in zip(pts, pts[1:]):
        D = [b - a for a, b in zip(Ka, Kb)]
        nz = [d for d in D if d]
        embedded = bool(nz) and all(abs(d) == 1 for d in nz) and len(set(nz)) == 1
        P = frozenset(j + 1 for j, d in enumerate(D) if d)
        disks.append(dict(P=P, chg=(ea != eb), emb=embedded, W=sum(D)))
    return dict(w=w, u=u, pts=pts, disks=disks)

def check_identity(w, pts, n=N):
    """(1 - t3) * sum eps T^K  ==  t1 * d w/dx1 - d w/dx2  (multivariable)."""
    lhs = {}
    def add(d, k, v):
        d[k] = d.get(k, 0) + v
        if d[k] == 0:
            del d[k]
    for _, eps, Kv in pts:
        add(lhs, Kv, eps)
        k2 = list(Kv); k2[2] += 1
        add(lhs, tuple(k2), -eps)
    rhs = {}
    K = [0] * n
    for a in w:
        j = abs(a)
        if a > 0:
            if j == 1:
                k2 = list(K); k2[0] += 1; add(rhs, tuple(k2), +1)
            elif j == 2:
                add(rhs, tuple(K), -1)
            K[j - 1] += 1
        else:
            K[j - 1] -= 1
            if j == 1:
                k2 = list(K); k2[0] += 1; add(rhs, tuple(k2), -1)
            elif j == 2:
                add(rhs, tuple(K), +1)
    return lhs == rhs

def lemma61_ok(d):
    one_end = len(d['P'] & {1, 2}) == 1
    return d['chg'] != one_end and not (d['P'] <= {1, 2})

LEMMA63 = {frozenset({2, 3}): False, frozenset({3}): True, frozenset({4}): True,
           frozenset({1, 2, 3}): True, frozenset({1, 2, 3, 4}): True}   # value = sign-changing

def summary(name, braid):
    R = analyse(braid)
    ds = R['disks']
    types = {}
    for d in ds:
        key = (tuple(sorted(d['P'])), 'chg' if d['chg'] else 'pres')
        types[key] = types.get(key, 0) + 1
    bad63 = [d for d in ds if LEMMA63.get(d['P']) is None or LEMMA63[d['P']] != d['chg']]
    n4 = sum(1 for d in ds if d['P'] == frozenset({1, 2, 3, 4}))
    has3 = any(d['P'] == frozenset({1, 2, 3}) for d in ds)
    parity = all(d['chg'] == (len(d['P']) % 2 == 1) for d in ds)
    m = len(R['pts'])
    Mm1 = sum(e * (-1) ** (sum(K) % 2) for _, e, K in R['pts'])
    out = dict(name=name, sigma_len=len(braid), loop_len=len(R['w']), m=m, n4=n4, has3=has3,
               bad63=len(bad63), parity=parity, M_at_minus1=Mm1,
               identity=check_identity(R['w'], R['pts']),
               lemma61_fail=sum(1 for d in ds if not lemma61_ok(d)),
               nonembedded=sum(1 for d in ds if not d['emb']), types=types)
    return out, R

# ---- braid words ----
def A(i, j):
    up = list(range(j - 1, i, -1))
    return up + [i, i] + inv(up)

PUSH = {1: A(3, 4), 2: A(2, 4) + A(3, 4), 3: A(1, 4) + A(2, 4) + A(3, 4)}

def push_word(yw):
    out = []
    for y in yw:
        out += PUSH[abs(y)] if y > 0 else inv(PUSH[abs(y)])
    return out

def comm(a, b):
    return a + b + inv(a) + inv(b)

W_GAMMA1 = [-2, -1, 2, 2, -3, -2, 1, 2]       # Gamma_1 as read off Fig. 6.3 by the construction lens
Y_S = red(comm([-3, -3], [1]))                 # [y3^-2, y1]

if __name__ == '__main__':
    # sanity: braid relations and the boundary loop for the hand-derived action
    for i in (1, 2):
        assert automorphism([i, i + 1, i]) == automorphism([i + 1, i, i + 1])
    assert automorphism([1, 3]) == automorphism([3, 1])
    for g in (1, 2, 3, -1, -2, -3):
        assert image([g], [1, 2, 3, 4]) == [1, 2, 3, 4]
        assert automorphism([g, -g]) == {j: [j] for j in range(1, 5)}
    # sanity: the Fox Jacobian is a representation that agrees with standard Burau up to conjugacy
    #         (compare characteristic data cheaply: traces of a few words at t = 2, -1, 3)
    import random
    random.seed(11)
    for _ in range(20):
        b = [random.choice([1, 2, 3, -1, -2, -3]) for _ in range(random.randint(1, 9))]
        for tv in (2, -1, 3, Fraction(1, 2)):
            F = fox_matrix_at(b, 4, tv); B = burau_at(b, 4, tv)
            trF = sum(F[i][i] for i in range(4)); trB = sum(B[i][i] for i in range(4))
            trFi = sum(fox_matrix_at(b, 4, 1 / Fraction(tv))[i][i] for i in range(4))
            assert trF == trB or trFi == trB, (b, tv, trF, trB, trFi)
    print("sanity checks on the action and on Burau passed")

    # random arcs: identity, Lemma 6.1, embeddedness
    tot = dict(arcs=0, disks=0, ident_fail=0, l61=0, nonemb=0)
    for _ in range(300):
        yw = [random.choice([1, 2, 3, -1, -2, -3]) for _ in range(random.randint(1, 6))]
        b = push_word(red(yw))
        if not b:
            continue
        o, _ = summary('rand', b)
        tot['arcs'] += 1; tot['disks'] += sum(o['types'].values())
        tot['ident_fail'] += (not o['identity']); tot['l61'] += o['lemma61_fail']; tot['nonemb'] += o['nonembedded']
    print("random pure braids (pushes of p4):", tot)

    # the defence's example S = Gamma_1^-1 [y3^-2, y1] Gamma_1  (as a y-word, then as a sigma-word)
    Sy = red(inv(W_GAMMA1) + Y_S + W_GAMMA1)
    Ss = push_word(Sy)
    print("S as y-word:", Sy, "length", len(Sy), "; sigma-length", len(Ss))
    assert automorphism(push_word(Y_S)) == automorphism(comm([1, 2] * 6, [3, 3])), "[y3^-2,y1] != [Delta3^4, A34]"
    print("[y3^-2, y1] equals [(s1 s2)^6, s3^2] = [Delta_3^4, A_34] as automorphisms: True")
    for tv in (-1, 2, 3):
        print(f"  t = {tv}: Fox/homological Burau of S is I: {is_identity(fox_matrix_at(Ss, 4, tv))};"
              f"  standard Burau of S is I: {is_identity(burau_at(Ss, 4, tv))}")
    print("  S is a pure braid with S(p3)=p3; automorphism nontrivial:", automorphism(Ss) != {j: [j] for j in range(1, 5)})
    o, R = summary('S', Ss)
    for k in ('sigma_len', 'loop_len', 'm', 'n4', 'has3', 'bad63', 'parity', 'M_at_minus1', 'identity',
              'lemma61_fail', 'nonembedded'):
        print(f"  {k}: {o[k]}")
    print("  disk types:", dict(sorted(o['types'].items(), key=lambda kv: (len(kv[0][0]), kv[0]))))
    sys.stdout.flush()
