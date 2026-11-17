# family P(2k,4k-1,4k+1): J via the necklace formula (mont/BRIEF Theorem N; checked here against lp.J for k=1,2),
# classical invariants of K via a standard (non-symmetric) pretzel diagram.
import sys, json, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, diag, words, alex
from fractions import Fraction as F
P_=lp.P; mul=lp.mul; add=lp.add; mono=lp.mono
def a_row(j):   # a_r = 1 + t^-3 (1-t)(1+t^2)(1-(-t)^j)
    return add({0:1}, mul(mono(-3), mul(P_((1,0),(-1,1)), mul(P_((1,0),(1,2)), add({0:1},{j:-(-1)**j})))))
def b_row(j):   # b_r = t^-3 - t^-2 + t^-1 + (-1)^j (t^(j-2) - t^(j-1))
    return add(P_((1,-3),(-1,-2),(1,-1)), {j-2:(-1)**j}, {j-1:-(-1)**j})
def polydiv(num, den):
    num=dict(num); q={}
    while num:
        e=max(num); c=num[e]; d=max(den); cd=den[d]
        assert c%cd==0
        f=c//cd; q[e-d]=f
        for ee,cc in den.items():
            num[ee+e-d]=num.get(ee+e-d,0)-f*cc
        num={k:v for k,v in num.items() if v}
        if num and max(num)<min(den)+min(q)-1000: raise ValueError
    return q
def J_necklace(mu, js):
    A={0:1}; B={0:1}
    for j in js: A=mul(A,a_row(j)); B=mul(B,b_row(j))
    mt={mu:(-1)**mu} if mu>=0 else None
    # (-t)^mu
    m_t={mu:(-1)**(mu%2)}
    w1=add({1:1}, mul(P_((1,0),(1,2)), m_t))
    w3=mul(P_((1,0),(1,2)), add({0:1}, {mu:-(-1)**(mu%2)}))
    num=add(mul(w1,A), mul(w3,B))
    J=polydiv(num, P_((1,0),(1,1),(1,2)))
    return lp.normalize(J)
def pretzel_word(ps, c):
    toks=[('l',1),('l',3)]+[(c,0)]*ps[0]+[(c,2)]*ps[1]+[(c,4)]*ps[2]+[('u',3),('u',1),('u',0)]
    return toks
def bracket_full(full):
    import kauffman
    state={(1,0):{0:1}}
    for c,i in full:
        new={}
        for m,p in state.items():
            if c in 'lr': kauffman.padd(new.setdefault(kauffman.cap(m,i),{}),p)
            elif c=='u':
                m2,loop=kauffman.cup(m,i); kauffman.padd(new.setdefault(m2,{}),kauffman.pdelta(p) if loop else p)
            else:
                a,b=(1,-1) if c=='x' else (-1,1)
                kauffman.padd(new.setdefault(m,{}),kauffman.pshift(p,a))
                m2,loop=kauffman.cup(m,i); q=kauffman.pdelta(p) if loop else p
                kauffman.padd(new.setdefault(kauffman.cap(m2,i),{}),kauffman.pshift(q,b))
        state={m:p for m,p in new.items() if p}
    p=dict(state.get((),{})); r={}
    while p:
        e=max(p); v=p[e]; r[e-2]=-v; kauffman.padd(p,{e:-v,e-4:-v})
    return r
def K_inv_pretzel(ps, c):
    full=pretzel_word(ps,c)
    V=diag.jones_from_bracket(bracket_full(full)); d=diag.der
    a2=F(-d(V,2),6); v3=F(-(d(V,3)+3*d(V,2)),36); j4=F(d(V,4)+6*d(V,3)+7*d(V,2)+d(V,1),24)
    cr=alex.diagram(full); n=len(cr)
    def det_at(tv):
        Mt,_=alex.alex_matrix(cr,tv); return alex.bareiss([r[:-1] for r in Mt[:-1]])
    pts=list(range(2,2+n+1)); co=diag._interp(pts,[det_at(x) for x in pts]); P={i:cc for i,cc in enumerate(co) if cc}
    lo,hi=min(P),max(P); mid=(lo+hi)//2; P={e-mid:cc for e,cc in P.items()}; s=sum(P.values()); P={e:cc*s for e,cc in P.items()}
    cw=diag.conway(P)
    return dict(V=V,a2=a2,v3=v3,j4=j4,a2c=cw[1],a4=cw[2] if len(cw)>2 else 0,Delta=P)
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
if __name__=='__main__':
    # chirality / formula checks on k=1,2 against the half-words
    import kauffman
    for k in (1,2):
        w=words.mont(-k,[4*k-1,4*k+1])
        Jw=lp.J(w); Jn=J_necklace(k,[2*k-1,2*k])
        Vw=diag.jones_from_bracket(kauffman.bracket(w))
        match=[c for c in 'xy' if K_inv_pretzel([2*k,4*k-1,4*k+1],c)['V']==Vw]
        print('k=%d necklace J == lp.J: %s ; pretzel diagram type matching the half-word V: %s'%(k,Jn==Jw,match),flush=True)
    out=[]
    for k in range(1,5):
        t0=time.time()
        J=J_necklace(k,[2*k-1,2*k]); inv=K_inv_pretzel([2*k,4*k-1,4*k+1],sys.argv[1] if len(sys.argv)>1 else 'y')
        assert inv['a2']==inv['a2c']
        a2,v3,a4,j4=inv['a2'],inv['v3'],inv['a4'],inv['j4']
        m2,m3,m4=F(M(J,2)),F(M(J,3)),F(M(J,4))
        D=(m3-432*v3)/180; loc=-1440*a2*a2-1440*a4+864*j4-120*a2; F4=(m4-loc)/1440
        print('k=%d P(%d,%d,%d): spanJ=%d a2=%s v3=%s a4=%s j4=%s | M2=%s M3=%s M4=%s | D=%s F4=%s | v3 mod5=%s j4 mod5=%s | %.1fs'%(
            k,2*k,4*k-1,4*k+1,max(J)-min(J),a2,v3,a4,j4,m2,m3,m4,D,F4,v3%5,j4%5,time.time()-t0),flush=True)
        out.append(dict(k=k,J=sorted(J.items()),a2=a2,v3=v3,a4=a4,j4=j4,M2=m2,M3=m3,M4=m4,D=D,F4=F4,Delta=sorted(inv['Delta'].items()),V=sorted(inv['V'].items())))
    json.dump([{kk:str(v) for kk,v in r.items()} for r in out],open('family_values.json','w'))
