import sys; sys.path.insert(0,sys.argv[1])
from w60 import *
G={'c':[], 'x':[3], 'y':[4,3,2,3]}
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
for sw in ['Ycx','YcxC','Ycxcx','YcxcxC','XCXCy','cXCXCy','cXCycX','cXCycXC']:
    M=rmat(word(sw)); print(sw,'D =',D(M),' braid length',len(word(sw)))
