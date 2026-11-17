# Is [Delta_3^4, A34] (hence S = Gamma1^-1 [Delta_3^4, A34] Gamma1) Brunnian?  Functions copied from phi0_check.py.
def inv(w): return [-a for a in reversed(w)]
def comm(x, y): return x + y + inv(x) + inv(y)
def red(w):
    s = []
    for a in w: s.pop() if s and s[-1] == -a else s.append(a)
    return s
def artin(w, n):
    img = {j: [j] for j in range(1, n + 1)}
    for a in w:
        i = abs(a)
        sub = {i: [i, i + 1, -i], i + 1: [i]} if a > 0 else {i: [i + 1], i + 1: [-i - 1, i, i + 1]}
        for j in img:
            out = []
            for c in img[j]:
                s = sub.get(abs(c), [abs(c)])
                out += s if c > 0 else inv(s)
            img[j] = red(out)
    return img
def trivial(w, n): return all(v == [j] for j, v in artin(w, n).items())
def pure(w, n):
    p = list(range(n))
    for a in w: k = abs(a); p[k - 1], p[k] = p[k], p[k - 1]
    return p == list(range(n))
def delete(w, n, d):
    p, out = list(range(1, n + 1)), []
    for a in w:
        k = abs(a)
        if d not in (p[k - 1], p[k]):
            kk = k - 1 if p.index(d) < k - 1 else k
            out.append(kk if a > 0 else -kk)
        p[k - 1], p[k] = p[k], p[k - 1]
    return out
X = [1, 2] * 6; A34 = [3, 3]
Y = comm(X, A34)
print("Y = [Delta_3^4, A34]: sigma-length", len(Y), "pure", pure(Y, 4), "nontrivial", not trivial(Y, 4))
for d in (1, 2, 3, 4):
    print(f"  delete strand {d}: trivial in B_3? {trivial(delete(Y, 4, d), 3)}")
