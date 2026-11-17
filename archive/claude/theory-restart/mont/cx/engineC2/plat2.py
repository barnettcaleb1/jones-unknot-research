"""Two-pole symmetric plats (class S2).  Middle level (A_l, L, M, R, A_r) = 8 doubled points, plain matching basis (14).
Top half = PREFIX + word over letters; Theta(W) = W_top . f(W_top).  J =. <s_P, mirror(s_D)> (pairing delta^loops)."""
import sys, itertools, random
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import theta, sym, lp
from kauffman import padd, pshift, pdelta, cap as kcap, cup as kcup
PREFIX=[('capA',0),('splitR',0),('proj',1),('capK',2)]
LET={'a':[('Y',1)],'A':[('X',1)],          # s1 (L-M),  inverse
     'b':[('X',2)],'B':[('Y',2)],          # s2 = f(s1) (M-R)
     'c':[('Y',0),('Y',0)],'C':[('X',0),('X',0)],   # tl = full twist A_l with L (half-word y0)
     'd':[('X',3),('X',3)],'D':[('Y',3),('Y',3)]}   # tr = f(tl)
INVL={'a':'A','A':'a','b':'B','B':'b','c':'C','C':'c','d':'D','D':'d'}
FL={'a':'b','b':'a','A':'B','B':'A','c':'d','d':'c','C':'D','D':'C'}   # letter swap under f (with order reversal)
def top_events(w): 
    ev=list(PREFIX)
    for ch in w: ev+=LET[ch]
    return ev
def elem(events, cols, use_e):
    """partial expansion of undoubled events starting from colour list cols (mutated)"""
    out=[]
    def dpos(i): return sum(2 if c=='k' else 1 for c in cols[:i])
    def mult(i): return 2 if cols[i]=='k' else 1
    for ev in events:
        typ=ev[0]
        if typ in ('capA','capK'):
            i=ev[1]; d=dpos(i); c='a' if typ=='capA' else 'k'
            out+= [('cap',d)] if c=='a' else [('cap',d),('cap',d+1)]
            cols[i:i]=[c,c]
        elif typ in ('X','Y'):
            i=ev[1]; s=dpos(i); p=mult(i); q=mult(i+1); c=typ.lower()
            for j in range(p-1,-1,-1):
                for k in range(q): out.append((c,s+j+k))
            cols[i],cols[i+1]=cols[i+1],cols[i]
        elif typ=='splitR':
            i=ev[1]; d=dpos(i); out.append(('cap',d)); cols[i+1:i+1]=['k']
        elif typ=='proj':
            if use_e:
                d=dpos(ev[1]); out+=[('cup',d),('cap',d)]
        else: raise ValueError(ev)
    return out
def run(state, elem_ev):
    for c,i in elem_ev:
        new={}
        for m,p in state.items():
            if c=='cap': padd(new.setdefault(kcap(m,i),{}),p)
            elif c=='cup':
                m2,loop=kcup(m,i); padd(new.setdefault(m2,{}),pdelta(p) if loop else p)
            else:
                a,b=(1,-1) if c=='x' else (-1,1)
                padd(new.setdefault(m,{}),pshift(p,a))
                m2,loop=kcup(m,i); q=pdelta(p) if loop else p
                padd(new.setdefault(kcap(m2,i),{}),pshift(q,b))
        state={m:p for m,p in new.items() if p}
    return state
def loops(mu,nu):
    n=len(mu); seen=[False]*n; L=0
    for s in range(n):
        if seen[s]: continue
        L+=1; x=s
        while True:
            seen[x]=True; y=mu[x]; seen[y]=True; x=nu[y]
            if seen[x]: break
    return L
def rev(mu):
    n=len(mu); return tuple(n-1-mu[n-1-i] for i in range(n))
def pinv(p): return {-e:c for e,c in p.items()}
def states(w):
    cols=[]; eD=elem(top_events(w),cols,False); cols2=[]; eE=elem(top_events(w),cols2,True)
    sD=run({():{0:1}},eD); sE=run({():{0:1}},eE)
    return sD,sE
DELTA={2:-1,-2:-1}
def raw(w):
    sD,sE=states(w)
    sP={}
    for m,p in sD.items(): padd(sP.setdefault(m,{}),theta.pmul(DELTA,p))
    for m,p in sE.items(): padd(sP.setdefault(m,{}),p,-1)
    bot={rev(m):pinv(p) for m,p in sD.items()}
    tot={}
    for m,p in sP.items():
        if not p: continue
        for n,q in bot.items():
            L=loops(m,n)
            dl={0:1}
            for _ in range(L): dl=theta.pmul(dl,DELTA)
            padd(tot,theta.pmul(theta.pmul(p,q),dl))
    return tot
def J(w):
    if theta.THETA0_TIMES_DELTA is None: theta.THETA0_TIMES_DELTA=theta.theta_raw(theta.planar_theta())
    r=raw(w); q=theta.pdiv(r,theta.THETA0_TIMES_DELTA)
    if q is None: return None
    es=sorted(q); r0=es[0]%4
    if any((e-r0)%4 for e in es): return None
    return lp.normalize({(e-r0)//4:c for e,c in q.items()})
def is_arc(w):
    """connectivity rule: the strand from v_top must not be in the middle (position 2 of the k-strands) at the middle level"""
    pos=['v','x','y']   # labels of the three k strands L,M,R at the start (v = from v_top)
    for ch in w:
        if ch in 'aA': pos[0],pos[1]=pos[1],pos[0]
        elif ch in 'bB': pos[1],pos[2]=pos[2],pos[1]
    return pos[1]!='v'
if __name__=='__main__':
    rnd=random.Random(7); ok=bad=0
    for it in range(25):
        L=rnd.randint(1,7); w=''.join(rnd.choice('aAbBcCdD') for _ in range(L))
        if not is_arc(w): continue
        Jp=J(w); Jd=theta.J_events(sym.symmetric(top_events(w)))
        if Jp==Jd: ok+=1
        else: bad+=1; print('BAD',w,Jp,Jd)
    print('plat2 pairing vs direct:',ok,'ok',bad,'bad')
