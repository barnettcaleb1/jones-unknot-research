#!/usr/bin/env python3
"""Check of the leading-term automaton (Theorem B): for normal forms  F(n_0,...,n_{k-1}) = (1 0) E Y^{n_{k-1}} E ... E Y^{n_0} (1 0)^T,
   E = [[1,1-t^4],[-1,-1]],  with n_1..n_{k-1} != 0:
   maxdeg F = sum of gains,  span F = G(n) + G(mirror n) - 4k,  mirror(n) = (-n_0-1, -n_1, ..., -n_{k-1})."""
import sys,itertools,collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mech2/twobridge/scripts')
from jmatrix import padd,pmul,apply,RHO,ONE,ZERO
E=((ONE,{0:1,4:-1}),({0:-1},{0:-1}))
def F(ns):
    v=(ONE,ZERO)
    for n in ns:
        for _ in range(abs(n)): v=apply(RHO['Y' if n>0 else 'y'],v)
        v=apply(E,v)
    return v[0]
def gains(ns):
    """automaton at t=infinity. states: 'O' (r=0), 'N' (r=-1 exactly), 'R', ('S') generic post-E states"""
    st='O'; G=0
    for n in ns:
        # Y^n step
        if st=='O':
            if n>0: pre='P'
            elif n==0: pre='O'
            elif n==-1: pre='Q1*'
            else: pre=('Q',-n)
        elif st=='N':
            if n==1: pre='O'
            elif n>=2: pre='P'
            elif n==0: pre='N'
            else: pre=('Q',-n+1)
        elif st=='R':
            assert n!=0
            pre='P' if n>0 else ('U',-n)
        elif st=='S':
            assert n!=0
            pre='P' if n>0 else ('Q',-n)
        # E step
        if pre=='O': g=0; st='N'
        elif pre=='N': g=4; st='O'   # E applied to r=-1 exactly: (1,-1) -> (t^4, 0)
        elif pre=='Q1*': g=4; st='O'
        elif pre=='P': g=1; st='R'
        elif pre[0]=='Q': g=3*pre[1]+1; st='S'
        elif pre[0]=='U': g=3*pre[1]+3; st='S'
        G+=g
    return G
def mirror(ns): return tuple([-ns[0]-1]+[-n for n in ns[1:]])
if __name__=='__main__':
    maxe=int(sys.argv[1]) if len(sys.argv)>1 else 3
    maxk=int(sys.argv[2]) if len(sys.argv)>2 else 4
    bad=0; tot=0
    inner=[e for e in range(-maxe,maxe+1) if e!=0]
    for k in range(1,maxk+1):
        for n0 in range(-maxe-1,maxe+1):
            for rest in itertools.product(inner,repeat=k-1):
                ns=(n0,)+rest
                f=F(ns); tot+=1
                md=max(f); mn=min(f)
                G=gains(ns); Gm=gains(mirror(ns))
                ok=(md==G and mn==4*k-Gm and abs(f[md])==1 and abs(f[mn])==1)
                if not ok:
                    bad+=1
                    if bad<12: print('MISMATCH',ns,'maxdeg',md,'pred',G,'mindeg',mn,'pred',4*k-Gm,'lead',f[md],f[mn])
    print('normal forms checked:',tot,'mismatches:',bad)
