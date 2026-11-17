import sys; sys.path.insert(0,sys.argv[1])
from w60 import *
G={'c':[], 'x':[-3,2,-4], 'y':[5,-3,4,2,-3]}
def perm(word):
    p=list(range(6))
    for g in reversed(word):
        i=abs(g)-1
        p=[(i+1 if x==i else i if x==i+1 else x) for x in p]
    return p
for k,w in G.items():
    p=perm(w); print(k,'encloses',sorted(p[i]+1 for i in range(3)))
TC=[1,2]*3
def inv(w): return [-g for g in reversed(w)]
def gen(ch):
    s=ch.lower(); w=G[s]+TC*2+inv(G[s])
    return w if ch.islower() else inv(w)
def word(sw):
    out=[]
    for ch in sw: out+=gen(ch)
    return out
def D(M):
    lo=min(min(p) for row in M for p in row if p); hi=max(max(p) for row in M for p in row if p)
    return hi-lo
for sw in sys.argv[2:]:
    M=rmat(word(sw)); L=len(sw); print(sw,'L=%d exact D=%d  8L+16=%d'%(L,D(M),8*L+16))
