# Artin (right) action of B_n on F_n = <x1..xn>; check Phi0 is pure, nontrivial, and Brunnian
def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    return out
def winv(w): return [-x for x in reversed(w)]
def apply(word_img, m):
    out = []
    for x in word_img:
        img = m.get(abs(x), [abs(x)])
        out += img if x > 0 else winv(img)
    return red(out)
def gen_sub(i, s):
    return {i: [i, i+1, -i], i+1: [i]} if s > 0 else {i: [i+1], i+1: [-(i+1), i, i+1]}
def act(n, w):
    imgs = {j: [j] for j in range(1, n+1)}
    for g in w:
        m = gen_sub(abs(g), 1 if g > 0 else -1)
        imgs = {j: apply(imgs[j], m) for j in imgs}
    return imgs
def comm(a, b): return a + b + winv(a) + winv(b)
def A(i, j):
    up = list(range(j-1, i, -1)); return up + [i, i] + winv(up)
assert act(4, [1,2,1]) == act(4, [2,1,2]) and act(4, [1,3]) == act(4, [3,1])
a = [1,2]*6; inner = comm(A(1,4), A(2,4)); b = comm(inner, A(3,4)); phi0 = comm(a, b)
im = act(4, phi0)
print("Phi0 nontrivial:", any(im[j] != [j] for j in im))
pure = all(len(v) % 2 == 1 and v[len(v)//2] == j and red(v[:len(v)//2] + v[len(v)//2+1:]) == [] for j, v in im.items())
print("Phi0 pure (x_j -> conjugate of x_j):", pure)
for i in range(1, 5):
    kill = lambda w: red([x for x in w if abs(x) != i])
    print(f"delete strand {i}: trivial? {all(kill(im[j]) == [j] for j in im if j != i)}")
# which piece dies when strand 3 is deleted? the inner commutator [A14,A24] or only b?
for nm, w in (("[A14,A24]", inner), ("b=[[A14,A24],A34]", b)):
    imw = act(4, w)
    kill3 = lambda u: red([x for x in u if abs(x) != 3])
    print(f"delete strand 3 from {nm}: trivial? {all(kill3(imw[j]) == [j] for j in imw if j != 3)}")
