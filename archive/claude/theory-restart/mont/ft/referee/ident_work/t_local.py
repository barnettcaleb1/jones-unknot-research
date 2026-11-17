# Claim 2: local configurations (no x0/y0).  (i) exact check of M2=-24a2, M3=432v3, M4=M4loc(K) on K's invariants;
# (ii) K_1 = k u A_out invariants from my own Morse-word bracket/Alexander; (iii) colour-2 Jones of K_1 by the
# Jones-Wenzl 2-cable, compared with lp.J in both t-conventions.
import sys, random, json, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/referee/ident_work')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import refinv as R, lp, alex, flat_search as fs
from fractions import Fraction as Fr
def padd(p,q,c=1):
    for e,v in q.items():
        nv=p.get(e,0)+c*v
        if nv: p[e]=nv
        elif e in p: del p[e]
def shiftp(p,k): return {e+k:v for e,v in p.items()}
def mdelta(p): r={}; padd(r,shiftp(p,2),-1); padd(r,shiftp(p,-2),-1); return r
def bracket_tokens(toks):
    """unnormalised bracket <D> (each closed loop = delta) of a Morse word starting from the EMPTY state.
    tokens: ('r'|'l',i) cap at positions i,i+1; ('u',i) cup; ('x'|'y',i) crossing; same smoothing weights as kauffman.py"""
    st={():{0:1}}
    for c,i in toks:
        new={}
        for m,p in st.items():
            if c in 'lr':
                m2=[(x+2 if x>=i else x) for x in m]; m2[i:i]=[i+1,i]; padd(new.setdefault(tuple(m2),{}),p)
            elif c=='u':
                a,b=m[i],m[i+1]; m2=list(m); loop=(a==i+1)
                if not loop: m2[a]=b; m2[b]=a
                del m2[i:i+2]; m2=tuple(x-2 if x>i+1 else x for x in m2)
                padd(new.setdefault(m2,{}),mdelta(p) if loop else p)
            else:
                wa,wb=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),shiftp(p,wa))
                a,b=m[i],m[i+1]; m2=list(m); loop=(a==i+1)
                if not loop: m2[a]=b; m2[b]=a
                del m2[i:i+2]; m2=[x-2 if x>i+1 else x for x in m2]
                q=mdelta(p) if loop else p
                m3=[(x+2 if x>=i else x) for x in m2]; m3[i:i]=[i+1,i]
                padd(new.setdefault(tuple(m3),{}),shiftp(q,wb))
        st={m:p for m,p in new.items() if p}
    assert set(st)<={()}, st.keys()
    return st.get((),{})
def divpoly(num,den):
    num=dict(num); q={}
    while num:
        e=max(num); c=num[e]; d=max(den); cd=den[d]
        if c%cd: return None
        f=c//cd; q[e-d]=f
        for ee,cc in den.items(): padd(num,{ee+e-d:-f*cc})
        if num and max(num)<min(den)+(min(q)-max(den)+min(den))-50: return None
    return q
def k1_tokens(word):
    half=alex.parse(word); out=[('r',0)]
    for c,s in half:
        if s==0:
            if c in 'xy': continue   # local words have none; K_out deletes windings
        out.append((c,s))
    out.append(('u',0)); return out
def cable2(toks, insert_e=False):
    out=[]
    for k,(c,i) in enumerate(toks):
        if c in 'lr': out+=[(c,2*i),(c,2*i+1)]
        elif c=='u': out+=[('u',2*i+1),('u',2*i)]
        else: out+=[(c,2*i+1),(c,2*i),(c,2*i+2),(c,2*i+1)]
        if k==0 and insert_e: out+=[('u',0),('r',0)]
    return out
DELTA={2:-1,-2:-1}
def col2(word):
    t=k1_tokens(word)
    B=bracket_tokens(cable2(t)); Be=bracket_tokens(cable2(t,True))
    q=divpoly(Be,DELTA)
    num={}; padd(num,B); padd(num,q,-1)          # <K f_2> = <K^(2)> - <K^(2)_e>/delta
    three={4:1,0:1,-4:1}                          # [3] = delta^2 - 1 = A^4 + 1 + A^-4
    red=divpoly(num,three)
    return red
def to_t(p,sign):   # A^e -> t^(sign*e/4) after removing a common residue
    es=sorted(p); r=es[0]%4
    assert all((e-r)%4==0 for e in es)
    out={}
    for e,c in p.items(): out[sign*(e-r)//4]=out.get(sign*(e-r)//4,0)+c
    return out
def K1inv(word):
    toks=k1_tokens(word)
    B=bracket_tokens(toks)
    kb=divpoly(B,DELTA)
    V=R.V_from_bracket(kb); a2,v3,j4=R.vinv(V)
    full=toks[1:]   # alex.diagram starts with the initial cap
    cr=alex.diagram(full)
    if cr is None: return None
    # Alexander via the same modular interpolation as refinv (copy of logic on a given crossing list)
    n=len(cr)
    if n==0: D={0:1}
    else:
        res=[]
        for p in R.PRIMES:
            xs=list(range(1,n+1)); ys=[]
            for x in xs:
                M,_=alex.alex_matrix(cr,x); ys.append(R.det_mod([r[:-1] for r in M[:-1]],p))
            res.append(R.interp_mod(xs,ys,p))
        Pt=1
        for p in R.PRIMES: Pt*=p
        co=[]
        for k in range(n):
            x=0
            for p,c in zip(R.PRIMES,res):
                qq=Pt//p; x=(x+c[k]*qq*pow(qq,p-2,p))%Pt
            co.append(x-Pt if x>Pt//2 else x)
        P={i:c for i,c in enumerate(co) if c}; lo,hi=min(P),max(P); mid=(lo+hi)//2
        P={e-mid:c for e,c in P.items()}; s=sum(P.values()); D={e:s*c for e,c in P.items()}
    a2c,a4=R.conway_a2a4(D)
    assert a2c==a2,(word,a2c,a2)
    return dict(V=V,a2=a2,v3=v3,j4=j4,a4=a4)
if __name__=='__main__':
    seed=int(sys.argv[1]); N=int(sys.argv[2]); rnd=random.Random(seed)
    rows=[]; seen=set(); t0=time.time(); badK=0; badK1=0; badcol=0; colA=0; colB=0; ncol=0
    while len(rows)<N and time.time()-t0<200:
        if rnd.random()<0.5:
            w=fs.gen(rnd,rnd.randint(10,28))
            if not w: continue
            w='.'.join(t for t in w.split('.') if t not in ('x0','y0'))
        else:
            w=R.gen2(rnd,rnd.randint(8,22),maxw=rnd.choice([5,7]),pw=0.0)
        if w in seen: continue
        seen.add(w)
        v=R.all_vals(w,True)
        if v is None: continue
        k1=K1inv(w)
        if k1 is None: continue
        okK=(v['M2']==-24*v['a2'] and v['M3']==432*v['v3'] and v['M4']==R.M4loc(v['a2'],v['a4'],v['j4']))
        a2,v3,a4,j4=k1['a2'],k1['v3'],k1['a4'],k1['j4']
        okK1=(v['M2']==-48*a2 and v['M3']==864*v3 and v['M4']==576*a2*a2-2880*a4+1728*j4-240*a2
              and v['a2']==2*a2 and v['v3']==2*v3 and v['a4']==2*a4+a2*a2 and v['j4']==2*j4+9*a2*a2)
        badK+= not okK; badK1+= not okK1
        if ncol<40 and len(k1_tokens(w))<=16:
            c=col2(w); ncol+=1
            if c is None: badcol+=1
            else:
                JA=lp.normalize(to_t(c,+1)); JB=lp.normalize(to_t(c,-1))
                colA+= (JA==v['J']); colB+= (JB==v['J'])
        rows.append((w,str(a2),str(v3),str(a4),str(j4)))
    print('local words',len(rows),'distinct K_1 tuples',len(set(r[1:] for r in rows)),'| K-form failures',badK,'| K_1-form failures',badK1)
    print('colour-2 Jones (2-cable, f_2) of K_1 vs lp.J on %d words: equal with t=A^+4: %d ; equal with t=A^-4: %d ; failures %d'%(ncol,colA,colB,badcol))
    print('time %.0fs'%(time.time()-t0))
