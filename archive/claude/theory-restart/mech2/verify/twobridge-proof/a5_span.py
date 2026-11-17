#!/usr/bin/env python3
"""Referee check A5: the span formula of Theorem B as literally stated, the mirror identity for F, extreme coefficients."""
import sys, itertools, collections
from lp import *
def sgn(n): return (n>0)-(n<0)
def mirror(ns): return tuple([-ns[0]-1]+[-n for n in ns[1:]])
def degenerate_prefix_len(ns):
    """number of leading degenerate E-steps: (0,1,1,...) or (-1,-1,...)"""
    if not ns: return 0
    if ns[0]==0:
        j=1
        while j<len(ns) and ns[j]==1: j+=1
        return j
    if ns[0]==-1:
        j=1
        while j<len(ns) and ns[j]==-1: j+=1
        return j
    return 0
def c_report(ns):
    """sum over generic steps of c_i exactly as printed in the report (sign(0) := 0, so 0 differs in sign from everything nonzero: try both readings)"""
    d=degenerate_prefix_len(ns); tot_a=0; tot_b=0
    for i,n in enumerate(ns):
        if i<d: continue
        if i==0:
            c=3*n+1 if n>=1 else 3*abs(n)-2
            tot_a+=c; tot_b+=c
        else:
            ca=3*abs(n)-2+2*(sgn(n)!=sgn(ns[i-1]))
            # reading b: sign(0) counted as +
            sb=sgn(ns[i-1]) if ns[i-1]!=0 else 1
            cb=3*abs(n)-2+2*(sgn(n)!=sb)
            tot_a+=ca; tot_b+=cb
    return tot_a,tot_b
maxe=int(sys.argv[1]) if len(sys.argv)>1 else 4
maxk=int(sys.argv[2]) if len(sys.argv)>2 else 5
inner=[e for e in range(-maxe,maxe+1) if e!=0]
tot=0; bad_mirror=0; bad_coeff=0; bad_span_nodeg=0; bad_span_deg=collections.Counter(); ndeg=0; unit_cnt=0; unit_not_alldeg=0; alldeg_not_unit=0
minspan_per_generic=10**9; examples=[]
for k in range(1,maxk+1):
    for n0 in range(-maxe-1,maxe+1):
        for rest in itertools.product(inner,repeat=k-1):
            ns=(n0,)+rest; tot+=1
            f=F(ns)
            # mirror identity F(n)(1/t) = t^{-4k} F(mirror n)(t)
            lhs=subs_inv(f); rhs=mul(mon(-4*k),F(mirror(ns)))
            if lhs!=rhs: bad_mirror+=1
            if abs(f[max(f)])!=1 or abs(f[min(f)])!=1: bad_coeff+=1
            d=degenerate_prefix_len(ns); generic=k-d
            if is_unit(f):
                unit_cnt+=1
                if generic!=0: unit_not_alldeg+=1
            elif generic==0: alldeg_not_unit+=1
            if generic>0: minspan_per_generic=min(minspan_per_generic, span(f)-generic)
            ca,cb=c_report(ns)
            if d==0:
                if span(f)!=ca: bad_span_nodeg+=1
            else:
                ndeg+=1
                key=('reading sign(0)=0: '+('ok' if span(f)==ca else 'WRONG'),'reading sign(0)=+: '+('ok' if span(f)==cb else 'WRONG'))
                bad_span_deg[key]+=1
                if span(f)!=cb and len(examples)<8: examples.append((ns,span(f),ca,cb))
print('normal forms:',tot)
print('mirror identity failures:',bad_mirror)
print('extreme coefficient not +-1:',bad_coeff)
print('F unit:',unit_cnt,'; unit but some generic step:',unit_not_alldeg,'; all steps degenerate but F not unit:',alldeg_not_unit)
print('min over forms with >=1 generic step of (span - number of generic steps):',minspan_per_generic)
print('span formula as printed, forms WITHOUT degenerate prefix (n_0 not in {0,-1}): mismatches =',bad_span_nodeg)
print('forms WITH a degenerate prefix:',ndeg,' ->',dict(bad_span_deg))
print('examples (ns, true span, formula[sign0=0], formula[sign0=+]):')
for e in examples: print('   ',e)
