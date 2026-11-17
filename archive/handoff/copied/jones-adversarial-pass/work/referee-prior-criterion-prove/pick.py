import sys, random, itertools; sys.path.insert(0,sys.argv[1])
from w60 import *
def perm(word):
    p=list(range(6))
    for g in reversed(word):
        i=abs(g)-1
        p=[(i+1 if x==i else i if x==i+1 else x) for x in p]
    return p
def part(word):
    p=perm(word); a=frozenset(p[i]+1 for i in range(3)); b=frozenset(range(1,7))-a
    return min(sorted(a),sorted(b))
cands={'c':[], 'x':[3], 'y':[4,3,2,3], 'z':[-2,4,3,-5], 'u':[5,4,-2,3], 'v':[2,3,4,5,1], 'w':[-1,3,-5,2], 'q':[5,-4,3,-2,1,-3]}
for k,w in cands.items(): print(k,w,part(w))
