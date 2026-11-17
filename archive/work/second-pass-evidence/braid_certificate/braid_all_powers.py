#!/usr/bin/env python3
"""Exact all-integer exponent exclusion for Bigelow commutator closures.

Only four full Jones polynomials per anchor are required. After clearing a
known common denominator, Jones=1 for nonzero m,n is equivalent to
 a(t)(-t)^(m+0)t^(2n)+b(t)(-t)^m+c(t)t^(2n)+d(t)=0.
All integer roots are solved by leading-degree ties, not a bounded scan.
"""
from braid_kernel import *

def mul(p,q):
    out=defaultdict(int)
    for i,a in p.items():
        for j,b in q.items():out[i+j]+=a*b
    return {i:a for i,a in out.items() if a}
def scale(p,c):return {i:a*c for i,a in p.items() if a*c}
def subtract(p,q):return add(p,scale(q,-1))
def mono_x(k):return {k:1 if k%2==0 else -1}
def mono_y(k):return {2*k:1}
def deflate_A(v):
    assert all(e%4==0 for e in v)
    return {-e//4:c for e,c in v.items()}
def defect(m,n,suffix):
    word=comm(power(HALF,m),power(FULL,n))+suffix
    return add(deflate_A(search.jones_a(word,5)),{0:-1})

def coefficients(samples):
    """Coefficients multiplied by D*Q, with Q clearing grid denominators."""
    x={1:mono_x(1),-1:mono_x(-1)}
    y={1:mono_y(1),-1:mono_y(-1)}
    G={}
    for i,j in itertools.product((1,-1),repeat=2):
        p=mul(samples[i,j],mul(x[i],y[j]))
        p=mul(p,subtract(x[-i],{0:1}));p=mul(p,subtract(y[-j],{0:1}))
        G[i,j]=p
    a=add(G[1,1],scale(G[1,-1],-1),scale(G[-1,1],-1),G[-1,-1])
    b=add(scale(mul(y[-1],G[1,1]),-1),mul(y[1],G[1,-1]),mul(y[-1],G[-1,1]),scale(mul(y[1],G[-1,-1]),-1))
    c=add(scale(mul(x[-1],G[1,1]),-1),mul(x[-1],G[1,-1]),mul(x[1],G[-1,1]),scale(mul(x[1],G[-1,-1]),-1))
    d=add(mul(mul(x[-1],y[-1]),G[1,1]),scale(mul(mul(x[-1],y[1]),G[1,-1]),-1),scale(mul(mul(x[1],y[-1]),G[-1,1]),-1),mul(mul(x[1],y[1]),G[-1,-1]))
    Q={0:1}
    for p in (x[1],x[-1],y[1],y[-1]):Q=mul(Q,subtract(p,{0:1}))
    den=mul(Q,mul(subtract(x[1],x[-1]),subtract(y[1],y[-1])))
    return [a,b,c,d],den

WEIGHTS=((1,2),(1,0),(0,2),(0,0))
def eval_coeff(coeff,m,n):
    return add(*(shift(p,u*m+v*n,(-1 if m%2 else 1) if u else 1) for p,(u,v) in zip(coeff,WEIGHTS)))

def solve_integer_roots(coeff):
    """Return ALL integer roots and full affine-line families.

    Every zero has a tie between highest exponents of two nonzero terms.
    These ties give at most six affine integer lines. On each line, after
    splitting parity, group equal slopes; another highest-exponent tie then
    gives finitely many candidates, unless the whole line vanishes.
    """
    active=[(p,w) for p,w in zip(coeff,WEIGHTS) if p]
    if not active:return dict(all_pairs=True,roots=[],lines=[],candidate_lines=[],evaluated=0)
    if len(active)==1:return dict(all_pairs=False,roots=[],lines=[],candidate_lines=[],evaluated=0)
    from math import gcd
    lines=set()
    for (p,(a,b)),(q,(c,d)) in itertools.combinations(active,2):
        u,v=a-c,b-d;rhs=max(q)-max(p);g=gcd(u,v)
        if rhs%g:continue
        u//=g;v//=g;rhs//=g
        if u<0 or (u==0 and v<0):u,v,rhs=-u,-v,-rhs
        lines.add((u,v,rhs))
    roots=set();families=[];evaluated=0
    for u,v,rhs in sorted(lines):
        # Here u is 0 or 1; after dividing gcd, u=0 forces v=1.
        if u:
            m0,n0=rhs,0;ms,ns=v,-1
        else:
            assert v==1
            m0,n0=0,rhs;ms,ns=1,0
        parities=(0,1) if ms%2 else (0,)
        for parity in parities:
            M0=m0+ms*parity;N0=n0+ns*parity
            MS=ms*(2 if len(parities)==2 else 1)
            NS=ns*(2 if len(parities)==2 else 1)
            groups={}
            for p,(a,b) in active:
                slope=a*MS+b*NS
                q=shift(p,a*M0+b*N0,(-1 if M0%2 else 1) if a else 1)
                groups[slope]=add(groups.get(slope,{}),q)
            groups={s:p for s,p in groups.items() if p}
            if not groups:
                families.append(dict(origin=[M0,N0],step=[MS,NS]));continue
            if len(groups)==1:continue
            candidates=set()
            for (s,p),(t,q) in itertools.combinations(groups.items(),2):
                rhs2=max(q)-max(p);div=s-t
                if rhs2%div==0:candidates.add(rhs2//div)
            for z in candidates:
                evaluated+=1
                if not add(*(shift(p,s*z) for s,p in groups.items())):
                    m,n=M0+MS*z,N0+NS*z
                    assert not eval_coeff(coeff,m,n)
                    roots.add((m,n))
    return dict(all_pairs=False,roots=[list(x) for x in sorted(roots)],lines=families,
                candidate_lines=[list(x) for x in sorted(lines)],evaluated=evaluated)

def validate_recovery(audit_solver=True):
    suffix=ANCHOR
    samples={(m,n):defect(m,n,suffix) for m,n in itertools.product((1,-1),repeat=2)}
    coeff,den=coefficients(samples)
    for m,n in [(1,1),(-1,-1),(2,3),(-3,2),(4,-2)]:
        x,y=mono_x(m),mono_y(n)
        lhs=mul(defect(m,n,suffix),mul(mul(x,y),den))
        rhs=mul(mul(subtract(x,{0:1}),subtract(y,{0:1})),eval_coeff(coeff,m,n))
        assert lhs==rhs,(m,n)
    if audit_solver:
        # Solver regression cases: x-y, xy-1, and generic four-term product.
        assert solve_integer_roots([{}, {0:1},{0:-1},{}])['lines']
        assert solve_integer_roots([{0:1},{},{},{0:-1}])['lines']
        assert solve_integer_roots([{0:1},{0:-1},{0:-1},{0:1}])['lines']
    return coeff,den

def run():
    validate();validate_recovery();started=time.monotonic()
    anchors=[[s*i for s,i in zip(signs,range(1,5))] for signs in itertools.product((-1,1),repeat=4)]
    contexts=[[]]+[[s*i] for s in (-1,1) for i in range(1,5)]
    vectors={(m,n):tl_vector(comm(power(HALF,m),power(FULL,n))) for m,n in itertools.product((1,-1),repeat=2)}
    rows=[];hits=[]
    for c in contexts:
        for alpha in anchors:
            suffix=c+alpha+inv(c);w=sum(1 if s>0 else -1 for s in alpha)
            assert search.jones_a(suffix,5)=={0:1}
            samples={pair:add(deflate_A(close_vector(tl_vector(suffix,vec),w)),{0:-1}) for pair,vec in vectors.items()}
            coeff,den=coefficients(samples);sol=solve_integer_roots(coeff)
            nonzero=[r for r in sol['roots'] if r[0] and r[1]]
            families=[r for r in sol['lines'] if not (r['origin'][0]==r['step'][0]==0 or r['origin'][1]==r['step'][1]==0)]
            row=dict(context=c,anchor=alpha,coefficients=coeff,denominator=den,solution=sol,nonzero_roots=nonzero,nonzero_families=families)
            rows.append(row)
            if nonzero or families or sol['all_pairs']:hits.append(row);print('HIT',c,alpha,sol,flush=True)
    report=dict(variants=len(rows),full_polynomial_evaluations=4*len(rows),all_integer_exponents=True,
                hits=hits,rows=rows,seconds=time.monotonic()-started)
    (ROOT/'braid_all_powers_results.json').write_text(json.dumps(report,indent=2))
    print('ALL POWERS:',len(rows),'anchor/context variants,',len(hits),'with nonzero integer solutions;',round(report['seconds'],2),'seconds',flush=True)

if __name__=='__main__':run()
