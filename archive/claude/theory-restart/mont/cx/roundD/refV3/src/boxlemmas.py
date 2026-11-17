"""refV3 (ii): EXACT verification of the rational-box lemmas used by Theorem V3 on all normal forms
u(m_0..m_{k-1}) = E Y^{m_{k-1}} ... E Y^{m_0} e_1 (E = Y^-1 X, m_0 not in {0,-1}, m_i != 0) with size := sum|m_i| <= SMAX.
Pure exact Laurent arithmetic (no automaton).  Checks at the TOP and at the BOTTOM (bottom computed directly, and compared with
the top of the mirror u'' = u(-m_0-1,-m_1,..)).  Lemmas: BX1 classes/lc, BX3 (rho_a, rho_b bounds + equality characterisations),
BX4, BX4' (exact formula), T2 (+ per-class bounds), BX5 (new), Lemma S (delta,sigma), S3 (tau), lambda_q per class,
and the C1 certificate sup used for n=1: 200 rho_a + 101 rho_q + 100 l2(a) + 100 lambda_q <= -150."""
import sys, itertools, time, pickle
from fractions import Fraction as Fr
sys.dont_write_bytecode=True
SMAX=int(sys.argv[1]) if len(sys.argv)>1 else 10
def mul(p,q):
    r={}
    for e,c in p.items():
        for f,d in q.items(): r[e+f]=r.get(e+f,0)+c*d
    return {e:c for e,c in r.items() if c}
def add(p,q):
    r=dict(p)
    for e,c in q.items(): r[e]=r.get(e,0)+c
    return {e:c for e,c in r.items() if c}
def shift(p,k): return {e+k:c for e,c in p.items()}
def Yapply(v,m):
    # Y = [[1,0],[t^-3,t^-3]] ; Y^-1 = [[1,0],[-1,t^3]]
    v1,v2=v
    if m>0:
        for _ in range(m): v1,v2=v1,shift(add(v1,v2),-3)
    else:
        for _ in range(-m): v1,v2=v1,add({e:-c for e,c in v1.items()},shift(v2,3))
    return (v1,v2)
def Eapply(v):
    # E = [[1,1-t^4],[-1,-1]]
    v1,v2=v
    return (add(v1,mul({0:1,4:-1},v2)), add({e:-c for e,c in v1.items()},{e:-c for e,c in v2.items()}))
def box(ms):
    v=({0:1},{})
    for m in ms:
        v=Yapply(v,m); v=Eapply(v)
    a=v[0]; b=add(v[0],mul({0:1,3:-1},v[1]))
    return a,b
def jet(p,end,K=3):
    """(deg, lc, (x1..xK)) normalised expansion at top (end='t', in t^-1) or bottom ('b', in t)"""
    if end=='t':
        d=max(p); c=p[d]; xs=tuple(Fr(p.get(d-i,0),c) for i in range(1,K+1))
    else:
        d=min(p); c=p[d]; xs=tuple(Fr(p.get(d+i,0),c) for i in range(1,K+1))
    return d,c,xs
def logs(xs):
    x1,x2,x3=xs
    return (x1, x2-x1*x1/2, x3-x1*x2+x1**3/3)
def enddata(a,b,end):
    da,ca,xa=jet(a,end); db,cb,xb=jet(b,end)
    la=logs(xa); lb=logs(xb); lq=tuple(y-x for x,y in zip(la,lb))
    return dict(da=da,ca=ca,db=db,cb=cb,la=la,lb=lb,lq=lq)
def topclass(a,b):
    da=max(a); db=max(b)
    if db-da==2:
        c=Fr(b[db],1)/a[da]
        x=jet(a,'t')[2][0]; y=jet(b,'t')[2][0]
        cc=y-x
        return 'R1' if cc==1 else ('R0' if cc==0 else 'R?%s'%cc)
    if db==da:
        d=add(b,{e:-c for e,c in a.items()})
        j=da-max(d)-1
        return 'S%d'%j if j<=2 else 'S3+'
    return '??'
def seqs(smax):
    # compositions with signs; m_0 not in {0,-1}
    out=[]
    def rec(pref,s):
        if pref: out.append(tuple(pref))
        for v in range(1,smax-s+1):
            for sg in (1,-1):
                m=sg*v
                if not pref and m==-1: continue
                rec(pref+[m],s+v)
    rec([],0)
    return out
def alternating_end(ms,sign):
    # sign sequence alternates and ends with given sign
    sg=[1 if m>0 else -1 for m in ms]
    return all(sg[i]!=sg[i+1] for i in range(len(sg)-1)) and sg[-1]==sign
if __name__=='__main__':
    t0=time.time()
    S=seqs(SMAX); print('normal forms with sum|m| <= %d: %d'%(SMAX,len(S)),flush=True)
    fails={}
    def fail(name,ms,info):
        fails.setdefault(name,[]).append((ms,info))
    stats={}; maxv={}
    def upd(key,val):
        if key not in maxv or val>maxv[key]: maxv[key]=val
    cache={}
    for idx,ms in enumerate(S):
        a,b=box(ms)
        k=len(ms); m0=ms[0]
        cls=topclass(a,b)
        T=enddata(a,b,'t'); B=enddata(a,b,'b')
        stats[cls]=stats.get(cls,0)+1
        # BX1: lc +-1 everywhere, class relations
        if abs(T['ca'])!=1 or abs(T['cb'])!=1 or abs(B['ca'])!=1 or abs(B['cb'])!=1: fail('BX1 lc',ms,(T['ca'],T['cb'],B['ca'],B['cb']))
        if cls.startswith('R'):
            if T['cb']!=-T['ca']: fail('BX1 R lc',ms,None)
            if (ms[-1]>0)!=True: fail('BX1 R iff last>0',ms,None)
        elif cls.startswith('S'):
            if T['cb']!=T['ca']: fail('BX1 S lc',ms,None)
            if ms[-1]>0: fail('BX1 S iff last<0',ms,None)
        else: fail('class',ms,cls)
        ra=T['la'][0]; rb=T['lb'][0]; rq=T['lq'][0]; l2a=T['la'][1]; l2b=T['lb'][1]; lq2=T['lq'][1]
        # rho_q / lambda_q per class
        upd(('rho_q',cls),rq); upd(('-rho_q',cls),-rq); upd(('lam_q',cls),lq2); upd(('-lam_q',cls),-lq2)
        # BX3
        if cls.startswith('R') and ra>-1: fail('BX3 R rho_a<=-1',ms,ra)
        if cls.startswith('S') and ra>0: fail('BX3 S rho_a<=0',ms,ra)
        if rb>0: fail('BX3 rho_b<=0',ms,rb)
        if cls.startswith('S') and ra==0 and not (cls=='S0' and alternating_end(ms,-1)): fail('BX3 eq S',ms,cls)
        if cls=='S0' and alternating_end(ms,-1) and ra!=0: fail('BX3 eq S conv',ms,ra)
        if cls in ('S1','S2','S3+') and ra>-1: fail('S>=1 rho_a<=-1',ms,ra)
        # BX4: alternating S-boxes
        if cls=='S0' and ra==0:
            pred=-Fr(k-(1 if m0<=-2 else 0),2)
            if l2a!=pred or T['la'][1]!=T['la'][1]: fail('BX4 l2(a)',ms,(l2a,pred))
        # BX4'
        if cls=='R1' and ra==-1:
            if not alternating_end(ms,1): fail("BX4' path",ms,None)
            pred=-Fr(k-(1 if m0<=-2 else 0)+1,2)
            if rb!=0 or l2b!=pred: fail("BX4' l2(b)",ms,(rb,l2b,pred))
            if l2b>-1: fail("BX4' <=-1",ms,l2b)
        if cls=='R1' and alternating_end(ms,1) and ra!=-1: fail("BX4' conv",ms,ra)
        # T2
        v=lq2+ra; upd(('T2',cls),v)
        bounds={'R1':Fr(-3,2),'S0':Fr(-1,2),'R0':Fr(-2),'S1':Fr(0),'S2':Fr(-1),'S3+':Fr(-1)}
        if v>bounds[cls]: fail('T2 class bound',ms,(cls,v))
        # BX5 (new): rho_a=-1, rho_q=0 => l2(b) <= 1/2 (R0: <= -1/2, S>=1: = 1/2 - (k_alt-[m0<=-2])/2)
        if ra==-1 and rq==0:
            upd(('BX5 l2b',cls),l2b)
            if cls=='R0':
                # trailing +1 run after the alternating part ending positive
                # trailing run of POSITIVE exponents: first one enters R_1 (end of the alternating part), the rest are +1's
                jr=0
                while jr<k and ms[k-1-jr]>0: jr+=1
                if jr<2 or any(ms[k-1-i]!=1 for i in range(jr-1)): fail('BX5 R0 shape',ms,jr)
                kalt=k-(jr-1); jp=jr-2
                pred=-Fr(kalt-(1 if m0<=-2 else 0),2)+1+(-2 if jp==0 else -1)
                if not alternating_end(ms[:kalt],1): fail('BX5 R0 alt prefix',ms,None)
                if l2b!=pred: fail('BX5 R0 formula',ms,(l2b,pred))
                if l2b>Fr(-1,2): fail('BX5 R0 bound',ms,l2b)
            else:
                # trailing run of NEGATIVE exponents: first one enters S_0 (end of the alternating part), the rest are -1's
                jr=0
                while jr<k and ms[k-1-jr]<0: jr+=1
                if jr<2 or any(ms[k-1-i]!=-1 for i in range(jr-1)): fail('BX5 S shape',ms,jr)
                kalt=k-(jr-1)
                pred=Fr(1,2)-Fr(kalt-(1 if m0<=-2 else 0),2)
                if not alternating_end(ms[:kalt],-1): fail('BX5 S alt prefix',ms,None)
                if l2b!=pred: fail('BX5 S formula',ms,(l2b,pred,cls))
                if l2b>Fr(1,2): fail('BX5 S bound',ms,l2b)
        # C1 n=1 certificate sup: 200 rho_a + 101 rho_q + 100 l2(a) + 100 lambda_q <= -150
        g=200*ra+101*rq+100*l2a+100*lq2; upd(('cert(100,100,1)',),g)
        if g>-150: fail('cert sup',ms,g)
        # Lemma S, S3 (top+bottom)
        dlt=(max(b)-min(b))-(max(a)-min(a))
        if dlt!=-1: fail('Lemma S delta',ms,dlt)
        if T['ca']*T['cb']*B['ca']*B['cb']*(-1)!=1: pass
        lcprod=Fr(T['cb'],T['ca'])*Fr(B['cb'],B['ca'])
        if lcprod!=-1: fail('Lemma S lc',ms,lcprod)
        sig=T['lq'][0]+B['lq'][0]
        if sig!=0: fail('Lemma S sigma',ms,sig)
        tau=T['lq'][1]+B['lq'][1]
        if tau!=-1: fail('S3 tau',ms,tau)
        # bottom = top of mirror
        mir=(-m0-1,)+tuple(-m for m in ms[1:])
        a2,b2=box(mir)
        T2m=enddata(a2,b2,'t')
        if T2m['lq']!=B['lq'] or T2m['la']!=B['la'] or T2m['lb']!=B['lb']: fail('R2 bottom=top(mirror)',ms,None)
        # span formula: span a >= 4
        if max(a)-min(a)<4: fail('span a>=4',ms,max(a)-min(a))
        if idx%20000==0: print(idx,round(time.time()-t0,1),flush=True)
    print('classes:',stats)
    for k_ in sorted(maxv,key=str): print('  max',k_,maxv[k_])
    print('FAILURES:',{k_:len(v) for k_,v in fails.items()})
    for k_,v in fails.items(): print('  ',k_,v[:5])
    print('time',round(time.time()-t0,1))
    pickle.dump((stats,maxv,fails),open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/refV3/boxlemmas_%d.pkl'%SMAX,'wb'))
