import sys, json, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, diag, words, kauffman, alex
from fractions import Fraction as F
def M(J,k): return sum(c*(-1)**(e%2)*e**k for e,c in J.items())
def Kinv_fast(w):
    V=diag.jones_from_bracket(kauffman.bracket(w)); d=diag.der
    a2=F(-d(V,2),6); v3=F(-(d(V,3)+3*d(V,2)),36); j4=F(d(V,4)+6*d(V,3)+7*d(V,2)+d(V,1),24)
    full=alex.symmetrize(alex.parse(w)); cr=alex.diagram(full)
    Mx,wr=alex.alex_matrix(cr,2)
    n=len(Mx)
    def det_at(tv):
        Mt,_=alex.alex_matrix(cr,tv); return alex.bareiss([r[:-1] for r in Mt[:-1]])
    pts=list(range(2,2+n+1)); vals=[det_at(x) for x in pts]
    co=diag._interp(pts,vals); P={i:c for i,c in enumerate(co) if c}
    lo,hi=min(P),max(P); mid=(lo+hi)//2; P={e-mid:c for e,c in P.items()}
    s=sum(P.values()); P={e:c*s for e,c in P.items()}
    cw=diag.conway(P)
    return dict(V=V,a2=a2,v3=v3,j4=j4,a2c=cw[1] if len(cw)>1 else 0,a4=cw[2] if len(cw)>2 else 0,Delta=P)
out=[]
for k in range(1,int(sys.argv[1])+1):
    t0=time.time()
    w=words.mont(-k,[4*k-1,4*k+1])
    J=lp.J(w); inv=Kinv_fast(w)
    a2,v3,a4,j4=inv['a2'],inv['v3'],inv['a4'],inv['j4']
    assert inv['a2']==inv['a2c']
    m2,m3,m4=F(M(J,2)),F(M(J,3)),F(M(J,4))
    D=(m3-432*v3)/180; loc=-1440*a2*a2-1440*a4+864*j4-120*a2; F4=(m4-loc)/1440
    r=dict(k=k,word=w,spanJ=max(J)-min(J),a2=a2,v3=v3,a4=a4,j4=j4,M2=m2,M3=m3,M4=m4,D=D,F4=F4,
           Delta=sorted(inv['Delta'].items()),V=sorted(inv['V'].items()))
    out.append(r)
    print('k=%d P(%d,%d,%d): a2=%s v3=%s a4=%s j4=%s | M2=%s M3=%s M4=%s | D=%s F4=%s | v3 mod5=%s j4 mod5=%s | %.1fs'%(
        k,2*k,4*k-1,4*k+1,a2,v3,a4,j4,m2,m3,m4,D,F4,v3%5,j4%5,time.time()-t0),flush=True)
json.dump([{kk:str(v) for kk,v in r.items()} for r in out],open('family_values.json','w'))
