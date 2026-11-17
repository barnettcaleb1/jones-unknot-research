"""E2: exact enumeration of class S2 (two-pole symmetric plats), words of length <= Lmax, split by first letter."""
import sys, pickle, time, cmath
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
import plat2, theta, lp, fastS
from kauffman import padd
COMM={frozenset(p) for p in [('a','d'),('a','D'),('A','d'),('A','D'),('b','c'),('b','C'),('B','c'),('B','C'),('c','d'),('c','D'),('C','d'),('C','D')]}
ORDER={ch:i for i,ch in enumerate('aAbBcCdD')}
def ok_next(w,ch):
    if w and plat2.INVL[w[-1]]==ch: return False
    if w and frozenset((w[-1],ch)) in COMM and ORDER[w[-1]]>ORDER[ch]: return False
    return True
def words(first,Lmax):
    stack=[first]
    while stack:
        w=stack.pop(); yield w
        if len(w)<Lmax:
            for ch in 'aAbBcCdD':
                if ok_next(w,ch): stack.append(w+ch)
DEL={2:-1,-2:-1}
def tropical(w):
    sD,sE=plat2.states(w)
    sP={}
    for m,p in sD.items(): padd(sP.setdefault(m,{}),theta.pmul(DEL,p))
    for m,p in sE.items(): padd(sP.setdefault(m,{}),p,-1)
    bot={plat2.rev(m):plat2.pinv(p) for m,p in sD.items()}
    tp=max(max(p)+max(q)+2*plat2.loops(m,n) for m,p in sP.items() if p for n,q in bot.items())
    bt=min(min(p)+min(q)-2*plat2.loops(m,n) for m,p in sP.items() if p for n,q in bot.items())
    return tp,bt
if __name__=='__main__':
    first=sys.argv[1]; Lmax=int(sys.argv[2])
    t0=time.time(); res={}; n=0; units=[]
    for w in words(first,Lmax):
        if not plat2.is_arc(w): continue
        J=plat2.J(w); n+=1
        if J is None: print('NONE',w); continue
        key=tuple(sorted(J.items()))
        if len(J)==1: units.append(w)
        if key in res: continue
        tp,bt=tropical(w)
        hs_pred=(tp-bt)/8.0          # predicted half-span in t units (A-span/4/2)
        hs=lp.span(J)/2.0
        a2,z10=fastS.gates(J)
        res[key]=(w,hs,hs_pred,a2,z10)
    pickle.dump((res,units,n),open('enum2_%s_%d.pkl'%(first,Lmax),'wb'))
    print(first,Lmax,'words',n,'distinct J',len(res),'unit words',len(units),'time %.0f'%(time.time()-t0))
