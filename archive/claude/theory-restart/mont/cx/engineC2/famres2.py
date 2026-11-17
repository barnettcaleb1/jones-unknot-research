import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import sympy as sp
import famres
t=sp.symbols('t')
w3=sp.exp(2*sp.pi*sp.I/3)
def analyse(W1,x,W2):
    r=famres.fitfam(W1,x,W2)
    if r is None: print(W1,x,W2,'skip'); return
    F,K=r
    terms={}
    for q,f in enumerate(F):
        k11,k13,k31,k33=[K[i][j][q] for i,j in [(0,0),(0,1),(1,0),(1,1)]]
        if k11!=0 or k33!=0: terms[(f,0)]=('g0',k11,k33)
        if k13!=0: terms[(f,1)]=('ab~',k13)
        if k31!=0: terms[(f,-1)]=('ba~',k31)
    pts=list(terms)
    if len(set(p[1] for p in pts))==1 and len(set(p[0] for p in pts))==1: print(W1,x,W2,'J independent of k'); return
    H=famres.hull(pts)
    print('family %s.(%s)^2k.%s hull %s'%(W1,x,W2,H))
    for i in range(len(H)):
        p,q=H[i],H[(i+1)%len(H)]
        on=sorted(pt for pt in terms if (q[0]-p[0])*(pt[1]-p[1])-(q[1]-p[1])*(pt[0]-p[0])==0 and min(p[0],q[0])<=pt[0]<=max(p[0],q[0]) and min(p[1],q[1])<=pt[1]<=max(p[1],q[1]))
        kind='N-ray (fixed m): per-m Lemma W' if p[1]==q[1] else 'm-ray'
        if kind!='m-ray': print('   edge',p,q,kind); continue
        # resonance relation for the two (or more) terms; a~=a(1/t) etc.  Write in terms of q=b/a, Q=q~ : divide by a a~
        A,B=sp.symbols('q Q')
        expr=0; c=sp.symbols('c')
        for pt in on:
            T=terms[pt]
            if T[0]=='g0': e=T[1]+T[2]*A*B
            elif T[0]=='ab~': e=T[1]*B
            else: e=T[1]*A
            expr+= e*sp.Symbol('s_%d_%d'%(pt[0]+5,pt[1]+5))
        # test necessary conditions on a box: at t=-1: q=Q=eps (+-1); at t=omega: q=Q=1 (a=b mod 1-t^3); unknown monomial shifts -> signs/roots of unity
        ok_m1=False
        for eps in (1,-1):
            for sg in itertools.product((1,-1),repeat=len(on)):
                val=sum(s*( (terms[pt][1]+terms[pt][2]*eps*eps) if terms[pt][0]=='g0' else terms[pt][1]*eps).subs(t,-1) for s,pt in zip(sg,on))
                if sp.simplify(val)==0: ok_m1=True
        ok_w=False
        for ph in itertools.product(range(3),repeat=len(on)):
            val=sum(w3**k*((terms[pt][1]+terms[pt][2]) if terms[pt][0]=='g0' else terms[pt][1]).subs(t,w3) for k,pt in zip(ph,on))
            if abs(complex(sp.N(val)))<1e-9: ok_w=True
        verdict='EXCLUDED' if not (ok_m1 and ok_w) else 'not excluded by t=-1 / t=omega'
        print('   edge',p,q,'m-ray: t=-1 ok:',ok_m1,' t=omega ok:',ok_w,'=>',verdict)
for fam in [('','a',''),('d','a',''),('','a','d'),('ab','a',''),('','a','bD'),('A','a','b'.upper()) ,('','a','ab'),('db','a',''),('','a','Db')]:
    analyse(*fam)
