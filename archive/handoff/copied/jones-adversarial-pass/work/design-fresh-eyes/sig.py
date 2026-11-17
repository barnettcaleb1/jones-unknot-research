#!/usr/bin/env python3
# Own minimal numeric TL engine for W(6,0); checks signature of the invariant
# Hermitian form on the unit circle A = e^{i theta}, and the spin-3/2 vector v_c.
import itertools, cmath, math
import numpy as np

N = 6
def matchings(points):
    if not points: return [[]]
    a = points[0]; res = []
    for k in range(1, len(points), 2):          # noncrossing: pair a with points[k]
        b = points[k]
        inner = points[1:k]; outer = points[k+1:]
        for mi in matchings(inner):
            for mo in matchings(outer):
                res.append([(a, b)] + mi + mo)
    return res

basis = [tuple(sorted(m)) for m in matchings(list(range(N)))]
idx = {m: i for i, m in enumerate(basis)}
def partner(m):
    p = {}
    for a, b in m: p[a] = b; p[b] = a
    return p

def loops(m1, m2):
    p1, p2 = partner(m1), partner(m2); seen = set(); L = 0
    for s in range(N):
        if s in seen: continue
        L += 1; x = s; use1 = True
        while True:
            seen.add(x); y = p1[x] if use1 else p2[x]; seen.add(y); use1 = not use1; x = y
            if x == s and use1: break
    return L

def e_action(i, m):
    # e_i on positions i,i+1 (0-based): returns (new matching, number of closed loops)
    p = partner(m)
    a, b = i, i + 1
    if p[a] == b: return m, 1
    pa, pb = p[a], p[b]
    new = [pr for pr in m if a not in pr and b not in pr]
    new.append(tuple(sorted((pa, pb)))); new.append((a, b))
    return tuple(sorted(new)), 0

def mats(A):
    d = -A**2 - A**-2
    E = []
    for i in range(N - 1):
        M = np.zeros((5, 5), dtype=complex)
        for j, m in enumerate(basis):
            nm, l = e_action(i, m); M[idx[nm], j] += d**l
        E.append(M)
    S = [A*np.eye(5) + (1/A)*E[i] for i in range(N - 1)]
    G = np.array([[d**loops(m1, m2) for m2 in basis] for m1 in basis], dtype=complex)
    return d, E, S, G

def qint(n, A): return (A**(2*n) - A**(-2*n)) / (A**2 - A**-2)

def vc(A):
    # coordinates on basis as in verify-sep: ([2],1,1,[2],[3]) on (12)(34)(56),(12)(36)(45),(14)(23)(56),(16)(23)(45),(16)(25)(34)
    lab = {((0,1),(2,3),(4,5)): qint(2,A), ((0,1),(2,5),(3,4)): 1, ((0,3),(1,2),(4,5)): 1,
           ((0,5),(1,2),(3,4)): qint(2,A), ((0,5),(1,4),(2,3)): qint(3,A)}
    v = np.zeros(5, dtype=complex)
    for m, c in lab.items(): v[idx[tuple(sorted(m))]] = c
    return v

if __name__ == '__main__':
    print('basis', basis)
    for th_deg in [62, 64, 66, 67, 68, 70, 80, 90, 50, 55, 40]:
        th = math.radians(th_deg); A = cmath.exp(1j*th)
        d, E, S, G = mats(A)
        Gh = (G + G.conj().T)/2
        ev = np.linalg.eigvalsh(Gh)
        # unitarity check: S^* G S = G
        err = max(np.abs(Si.conj().T @ G @ Si - G).max() for Si in S)
        v = vc(A); Hvv = (v.conj() @ G @ v).real
        # check v is eigenvector of T_c = (s1 s2)^3 with eigenvalue A^6
        T = np.linalg.matrix_power(S[0] @ S[1], 3)
        eig_err = np.abs(T @ v - A**6 * v).max()
        print(f'theta={th_deg:5.1f} deg delta={d.real:+.4f} sig(+,-)=({sum(ev>1e-9)},{sum(ev<-1e-9)}) '
              f'unit_err={err:.1e} H(v,v)={Hvv:+.4f} Tv-A^6v={eig_err:.1e}  rot angle 12theta mod 360 = {(12*th_deg)%360:.1f}')
