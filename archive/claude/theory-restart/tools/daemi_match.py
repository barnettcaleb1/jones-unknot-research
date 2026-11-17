#!/usr/bin/env python3
"""Daemi matchability of formal flat configurations at the closures of slope 1/n (knots K_n, determinant 1).
A BN~ square at (c, d) gives two specials at offsets c, c+2 on level d. In K_n a special at offset c on level d gives generators at
positions x + e (x = c/2), e in E_n = {0,2,3,5} + {0..n-1}, all on level d.  Allowed pair: (level L, pos p) -> (level L-1, pos p'), p' >= p+1
(bidegree (r, 2r-2), r = p'-p+1 >= 2).  The rational generator (pawn) is one extra generator at a free level/position.
Daemi (arXiv:1508.07650, Thms 2,3): Kh~ of a knot with determinant 1 must be matchable down to rank 1."""
import itertools,sys
def En(n):
    out=[]
    for a in (0,2,3,5):
        for i in range(n): out.append(a+i)
    return sorted(out)
def gens(squares,n):
    g=[]
    for (x,d) in squares:           # x = c/2 of the lower special; second special at x+1
        for e in En(n):
            g.append((d,x+e)); g.append((d,x+1+e))
    return g
def max_matching(g):
    n=len(g)
    und=[[] for _ in range(n)]
    for i,(L,p) in enumerate(g):
        for j,(L2,p2) in enumerate(g):
            if L2==L-1 and p2>=p+1: und[i].append(j); und[j].append(i)
    mate=[-1]*n
    def aug(u,seen):
        for v in und[u]:
            if v in seen: continue
            seen.add(v)
            if mate[v]==-1 or aug(mate[v],seen):
                mate[v]=u; mate[u]=v; return True
        return False
    size=0
    for u in range(n):
        if g[u][0]%2==0 and aug(u,set()): size+=1
    return size
def min_rank(squares,n):
    """minimal number of unmatched generators over all placements of the pawn"""
    g=gens(squares,n)
    base=len(g)-2*max_matching(g)       # pawn not interacting
    best=base+1
    levels=sorted(set(L for L,p in g)); pos=sorted(set(p for L,p in g))
    for L in range(levels[0]-1,levels[-1]+2):
        for p in range(pos[0]-2,pos[-1]+3):
            gg=g+[(L,p)]
            r=len(gg)-2*max_matching(gg)
            best=min(best,r)
    return best
if __name__=='__main__':
    print('bare B: squares at (0,0) and its (1,0)-shift (0,-1):')
    for n in (1,2,3):
        print('   n=%d minimal rank %d (need 1)'%(n,min_rank([(0,0),(0,-1)],n)))
    print('two cancelling pairs  Q1=(0,0), hQ1=(0,-1), Q2=(-g, j), hQ2=(-g, j-1):  minimal rank at n=1,2  (need 1)')
    for j in range(-3,4):
        row=[]
        for g in range(-12,13):
            r1=min_rank([(0,0),(0,-1),(-g,j),(-g,j-1)],1)
            row.append('%d'%r1 if r1<10 else '+')
        print('   j=%+d  g=-12..12: '%j+' '.join(row))
