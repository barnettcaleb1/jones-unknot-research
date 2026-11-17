# Check the note's identity Phi0 = [delta^-2, b], delta = Delta_3^-2 Delta_4^2 = A14 A24 A34,
# with exact unreduced Burau at t = 2 and t = 3/2 (a sanity check, not a proof),
# and exactly via the Artin action on F_4 for the shorter identity delta = A14 A24 A34.
from fractions import Fraction as F
def eye(n): return [[F(int(i == j)) for j in range(n)] for i in range(n)]
def mul(A, B):
    n = len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def gen(n, i, t, inv=False):
    M = eye(n); t = F(t)
    blk = [[1-t, t], [F(1), F(0)]] if not inv else [[F(0), F(1)], [1/t, 1-1/t]]
    for r in range(2):
        for c in range(2): M[i-1+r][i-1+c] = blk[r][c]
    return M
def word(n, w, t):
    M = eye(n)
    for g in w: M = mul(M, gen(n, abs(g), t, g < 0))
    return M
def inv(w): return [-g for g in reversed(w)]
def comm(a, b): return a + b + inv(a) + inv(b)
A14, A24, A34 = [3, 2, 1, 1, -2, -3], [3, 2, 2, -3], [3, 3]
b = comm(comm(A14, A24), A34)
phi0 = comm([1, 2]*6, b)
D3sq = [1, 2]*3; D4sq = [1, 2, 3]*4
delta = inv(D3sq) + D4sq
alt = comm(inv(delta) + inv(delta), b)
for tv in (2, F(3, 2)):
    print('t=%s: rho(delta)==rho(A14 A24 A34):' % tv, word(4, delta, tv) == word(4, A14 + A24 + A34, tv),
          ' rho(Phi0)==rho([delta^-2,b]):', word(4, phi0, tv) == word(4, alt, tv))
# Artin action (faithful) for delta = A14 A24 A34
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x: out.pop()
        else: out.append(x)
    return out
def winv(w): return [-x for x in reversed(w)]
def sig(i,s):
    if s>0: return {i:[i,i+1,-i], i+1:[i]}
    else:   return {i:[i+1], i+1:[-(i+1),i,i+1]}
def subst(w,m):
    out=[]
    for x in w:
        a=abs(x); img=m.get(a,[a]); out+= img if x>0 else winv(img)
    return red(out)
def act(n,w):
    imgs={j:[j] for j in range(1,n+1)}
    for g in w:
        m=sig(abs(g),1 if g>0 else -1); imgs={j:subst(imgs[j],m) for j in imgs}
    return imgs
print('Artin action: delta == A14 A24 A34 exactly?', act(4, delta) == act(4, A14 + A24 + A34))
