#!/usr/bin/env python3
"""Referee check A4/A5: recompute every transition of the automaton of Theorem B by exact arithmetic.
For each normal form (n_0,...,n_{k-1}) (n_i != 0 for i>=1) track v=(v_1,v_2) exactly and record, before and after each
E-step, the pair (deg, lc) of r = v_2/v_1 at t = infinity (deg r = deg v_2 - deg v_1, lc r = lc v_2 / lc v_1), or the exact
value when r = 0 or r = -1.  Compare with the report's list of states and gains."""
import sys, itertools, collections
from lp import *
def state(v):
    v1,v2=v
    assert v1, 'v_1 = 0 ?!'
    if not v2: return ('ZERO',)
    if add(v1,v2)=={}: return ('MINUS1',)
    d=deg(v2)-deg(v1); c=lc(v2)*lc(v1)  # lc(v1)=+-1 is asserted below
    return (d,c)
def classify_pre(s):
    if s==('ZERO',) or s==('MINUS1',): return s[0]
    d,c=s
    if (d,c)==(-3,1): return 'P'
    if c==-1 and d>=0 and d%3==0: return 'Q%d'%(d//3+1)
    if c==1 and d>=2 and d%3==2: return 'U%d'%((d+1)//3)
    return None
def classify_post(s):
    if s==('ZERO',) or s==('MINUS1',): return s[0]
    d,c=s
    if (d,c)==(-1,1): return 'R'
    if d<=-4 and c==(-1)**((-4-d)%2): return 'S%d'%(-4-d)
    return None
def run(ns):
    v=(ONE,ZERO); out=[]; prev_post='START'
    for i,n in enumerate(ns):
        for _ in range(abs(n)): v=mapply(RHO['Y' if n>0 else 'y'],v)
        pre=state(v); d0=deg(v[0])
        v=mapply(E,v)
        assert abs(lc(v[0]))==1
        gain=deg(v[0])-d0; post=state(v)
        out.append((prev_post,n,classify_pre(pre),gain,classify_post(post)))
        prev_post=classify_post(post)
    return out,v[0]
maxe=int(sys.argv[1]) if len(sys.argv)>1 else 4
maxk=int(sys.argv[2]) if len(sys.argv)>2 else 5
inner=[e for e in range(-maxe,maxe+1) if e!=0]
trans=collections.Counter(); unknown=0; tot=0; late_degenerate=0
gain_of={}
for k in range(1,maxk+1):
    for n0 in range(-maxe-1,maxe+1):
        for rest in itertools.product(inner,repeat=k-1):
            ns=(n0,)+rest; tot+=1
            steps,f=run(ns)
            seen_generic=False
            for (pp,n,pre,g,post) in steps:
                if pre is None or post is None: unknown+=1; print('UNLISTED STATE',ns,steps); break
                key=(pp if (pp=='START' or not pp.startswith('S')) else 'S_j', 'n>0' if n>0 else ('n=0' if n==0 else 'n=-%d'%(-n)), pre, g, post if not post.startswith('S') else ('S0' if post=='S0' else 'S_(j+1)' if pp!='START' and pp.startswith('S') and post=='S%d'%(int(pp[1:])+1) else post))
                trans[key]+=1
                deg_pre = pre in ('ZERO','MINUS1')
                if deg_pre and seen_generic: late_degenerate+=1; print('DEGENERATE AFTER GENERIC',ns,steps)
                if not deg_pre: seen_generic=True
print('normal forms:',tot,' unlisted states:',unknown,' degenerate-after-generic:',late_degenerate)
print('observed transitions  (state after previous E | Y-exponent | state before E | gain | state after E) : count')
for key,c in sorted(trans.items(),key=lambda kv:(kv[0][0],kv[0][1])): print('  ',key,c)
