# check: delta = Delta_3^-2 Delta_4^2 lies in K_4 and Phi0 = [delta^-2, b], via the Artin action,
# composing block automorphisms (letter-by-letter evaluation of the long word blows up).
src = open("$HOME/jones-adversarial-pass/bbb-gap-note/check/quotes/brunn_check.py").read().split("assert act(4, [1,2,1])")[0]
ns = {}; exec(src, ns)
act, winv, comm, A, red, apply = ns['act'], ns['winv'], ns['comm'], ns['A'], ns['red'], ns['apply']
def compose(P, Q):          # right action: x.(UV) = (x.U).V
    return {j: apply(P[j], Q) for j in P}
D3sq = [1,2]*3; D4sq = [1,2,3]*4
delta = winv(D3sq) + D4sq
im = act(4, delta)
print("Delta_4^2 central:", all(act(4, D4sq + [g]) == act(4, [g] + D4sq) for g in (1,2,3)))
print("delta pure and in K_4 (deleting strand 4 trivial):",
      all(v[len(v)//2] == j and red(v[:len(v)//2] + v[len(v)//2+1:]) == [] for j, v in im.items())
      and all(red([x for x in im[j] if abs(x) != 4]) == [j] for j in (1,2,3)))
b = comm(comm(A(1,4), A(2,4)), A(3,4)); phi0 = comm([1,2]*6, b)
dm2 = winv(delta) * 1 + winv(delta)
blocks = [act(4, dm2), act(4, b), act(4, winv(dm2)), act(4, winv(b))]
R = blocks[0]
for Q in blocks[1:]: R = compose(R, Q)
print("Phi0 == [delta^-2, b]:", R == act(4, phi0))
