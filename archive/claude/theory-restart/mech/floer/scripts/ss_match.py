"""Spectral-sequence matching test (conditional on Baldwin's Conjecture 1.1 / Szabo degrees).
E_2 = Kh~(T(n)) in the 'block frame':
  special (c,d):  q' = c + {-5,-1,1,5},  delta' = d - 1/2
  rational part, n > k:  q' = q0 + 2i, i in {0,2,3,...,n-k}, delta' = dr - 1, q0 = 24j + 2k - 1
                 n < k:  q' = q1 - 2i, i in {0,2,3,...,k-n}, delta' = dr,     q1 = 24j + 2k + 1,   dr = 4j + 1/2
A cancelling pair (x,y): delta'(x) = delta'(y) + 1 and q'(y) - q'(x) >= 2   (rule '+', Szabo/Baldwin direction)
reversed rule '-':        delta'(x) = delta'(y) + 1 and q'(x) - q'(y) >= 2.
Needed number of pairs: (rank E_2 - rank HF^(S^3_n))/2,  rank HF^ = D' + |n - m|.
"""
import sys, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech/floer/scripts')
from knots import floer
from load import load138
from fractions import Fraction as Fr

def gens(specials, k, j, n):
    G = []
    for (c,d) in specials:
        for s in (-5,-1,1,5):
            G.append((Fr(d) - Fr(1,2), c+s, 'S'))
    dr = 4*j + Fr(1,2)
    if n > k:
        q0 = 24*j + 2*k - 1
        for i in [0] + list(range(2, n-k+1)):
            G.append((dr - 1, q0 + 2*i, 'R'))
    elif n < k:
        q1 = 24*j + 2*k + 1
        for i in [0] + list(range(2, k-n+1)):
            G.append((dr, q1 - 2*i, 'R'))
    else:
        raise ValueError
    return G

def maxmatch(G, rule):
    # bipartite: sources x, targets y with delta(x) = delta(y)+1
    n = len(G)
    adj = [[] for _ in range(n)]
    bylev = collections.defaultdict(list)
    for idx,(dl,q,t) in enumerate(G): bylev[dl].append(idx)
    for idx,(dl,q,t) in enumerate(G):
        for y in bylev.get(dl-1, []):
            qy = G[y][1]
            if (rule == '+' and qy - q >= 2) or (rule == '-' and q - qy >= 2):
                adj[idx].append(y)
    # nodes on even/odd levels form the bipartition: left = levels with (2*dl) % 4 == 1 say
    left = [i for i,(dl,q,t) in enumerate(G) if int(2*dl) % 4 == 1]
    # build undirected adjacency for left nodes
    und = collections.defaultdict(list)
    for x in range(n):
        for y in adj[x]:
            und[x].append(y); und[y].append(x)
    matchL = {}; matchR = {}
    def aug(u, seen):
        for v in und[u]:
            if v in seen: continue
            seen.add(v)
            if v not in matchR or aug(matchR[v], seen):
                matchL[u] = v; matchR[v] = u
                return True
        return False
    sys.setrecursionlimit(10000)
    for u in left:
        aug(u, set())
    return len(matchL)

def analyse(rec, L=30):
    k, j, sp = rec['k'], rec['j'], rec['specials']
    D = 4*len(sp)
    mabs, Dp, typ = floer(rec['knot'])
    out = {}
    for sgn in ([1,-1] if mabs else [1]):
        m = sgn*mabs
        res = []
        for n in (k+L, k-L):
            if n == m: continue
            G = gens(sp, k, j, n)
            need2 = len(G) - (Dp + abs(n-m))
            assert need2 % 2 == 0
            need = need2//2
            res.append((n, need, maxmatch(G,'+'), maxmatch(G,'-')))
        out[m] = res
    return D, Dp, out

if __name__ == '__main__':
    T = load138()
    tot = collections.Counter()
    rows = []
    for rec in T:
        D, Dp, out = analyse(rec)
        # choose chirality: sign(m) = sign(k) when k != 0 (forced for the torus knots by the rank inequality); else report both
        feas = {}
        for m,res in out.items():
            feas[m] = (all(need <= mp for (_,need,mp,mm) in res), all(need <= mm for (_,need,mp,mm) in res), res)
        rows.append((rec['name'], rec['k'], rec['j'], D, Dp, feas))
    okplus = 0; okminus = 0; amb = 0
    print("name k j D D' | per chirality m: [(n, needed pairs, max matching rule +, max matching rule -)]")
    for name,k,j,D,Dp,feas in rows:
        anyp = any(v[0] for v in feas.values()); anym = any(v[1] for v in feas.values())
        okplus += anyp; okminus += anym
        print(name, k, j, D, Dp, '|', '; '.join(f"m={m}: {v[2]} {'+ok' if v[0] else '+FAIL'} {'-ok' if v[1] else '-FAIL'}" for m,v in feas.items()))
    print('feasible with rule + (some chirality):', okplus, '/', len(rows))
    print('feasible with rule - (some chirality):', okminus, '/', len(rows))
