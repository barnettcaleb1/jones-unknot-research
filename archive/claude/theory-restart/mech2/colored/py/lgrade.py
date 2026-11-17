#!/usr/bin/env python3
"""Check the l-graded tensor-square identity: multiset {a+3b : (a,b) in N(T_K)} == multiset {h1+h2 : h_i in Kh~(K)} up to a shift.
Also print squares in (a0=a+3b, level=b) coordinates and the torsion (domino) positions of Kh~(K)."""
import sys,os,glob,collections
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from chains import lattice
from habiro import knot_kh,D
def data(name):
    kh=knot_kh(name)
    free=[(h,q) for h,q,k in kh if k=='free'][0]
    hs=sorted(h-free[0] for h,q,_ in kh)
    # thinness check
    deltas=set(q-2*h for h,q,_ in kh)
    rho,arc,sq,other=lattice(os.path.join(D,name,'cxBNr-c2-d'))
    pts=list(arc)
    for (a,b) in sq: pts+=[(a,b),(a+1,b),(a,b+1),(a+1,b+1)]
    return hs,deltas,arc,sq,pts
def check(name,verbose=False):
    hs,deltas,arc,sq,pts=data(name)
    N=sorted(a+3*b for a,b in pts)
    T=sorted(x+y for x in hs for y in hs)
    ok=None
    for sign in (1,-1):
        TT=sorted(sign*v for v in T)
        shift=N[0]-TT[0]
        if [v+shift for v in TT]==N: ok=(sign,shift)
    print('%-8s thin=%s  dimN=%d  l-graded tensor square: %s'%(name,len(deltas)==1,len(pts),ok))
    if verbose:
        doms=[]
        hh=list(hs); hh.remove(0)
        print('   Kh~ h-positions rel. free gen:',hs)
        lev=collections.defaultdict(list)
        for a,b in sq: lev[a+3*b].append(b)
        print('   arc:',arc)
        print('   squares by a0=a+3b -> levels b:',{k:sorted(v) for k,v in sorted(lev.items())})
    return ok
if __name__=='__main__':
    v='-v' in sys.argv
    names=[a for a in sys.argv[1:] if a!='-v'] or sorted([os.path.basename(p)[:-4] for p in glob.glob(D+'/*.kht') if os.path.exists(os.path.join(p[:-4],'cxBNr-c2-d'))],key=lambda s:[int(x) for x in s[1:].split('_')])
    for n in names: check(n,v)
