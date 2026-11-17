"""E4: generalised 2-slot symmetric closures.  Special part W_s (S2 word), slot box on (A_l, k at position 1) at the end of the
top half.  G(W_s) fitted exactly (gtable.Ghat), then boxes scanned with every tie-N (fastS)."""
import sys, pickle, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import gtable, plat2, sym, enum2, fastS, lp, vc, lib
from lp import span, shift
NEG=-10**9
def top(p): return max(p) if p else NEG
def bot(p): return min(p) if p else -NEG
first=sys.argv[1]; Lmax=int(sys.argv[2])
R6=lib.rational(6)
NL=[]; seen=set()
for u in lib.rational(4):
    for kk in [-3,-2,-1,1,2,3]:
        for NN in [-1,0,1]:
            try: nd=lib.node(kk,NN,[u])
            except AssertionError: continue
            if nd is None or nd[0] in seen: continue
            seen.add(nd[0]); NL.append(nd)
BOX=[(b[0],b[1],'R',b[2]) for b in R6]+[(b[0],b[1],'N',b[2]) for b in NL]
t0=time.time(); Gseen={}; out=[]; units=[]
for w in enum2.words(first,Lmax):
    if not plat2.is_arc(w): continue
    G=gtable.Ghat(lambda B: plat2.top_events(w)+sym.body(B,0))
    if G is None or isinstance(G,tuple): continue
    gk=tuple(tuple(tuple(sorted(x.items())) for x in row) for row in G)
    if gk in Gseen: continue
    Gseen[gk]=w
    bestd=(0,0,0); bestr=(0,0,0)
    for key,v,tg,Tr in BOX:
        a,b=v
        T1=top(G[0][0])+span(a); T4=top(G[1][1])+span(b)
        T20=top(G[0][1])+top(a)-bot(b); T30=top(G[1][0])+top(b)-bot(a)
        fin=[x for x in (T1,T20,T30,T4) if x>NEG//2]
        lo=-((sum(abs(x) for x in fin))//3+3)
        for N in range(lo,-lo+1):
            T2=T20+3*N; T3=T30-3*N
            Ts=sorted([x for x in (T1,T2,T3,T4) if x>NEG//2],reverse=True)
            if Ts[0]>4 and (len(Ts)<2 or Ts[0]!=Ts[1]): continue
            R=fastS.R_of(G,(a,shift(b,-3*N)))
            if len(R)==1: units.append((w,tg,Tr,N)); continue
            naive=Ts[0]-4; act=top(R)
            if naive<=0: continue
            if naive-act>bestd[0]: bestd=(naive-act,naive,tg)
            if (naive-act)/naive>bestr[0]: bestr=((naive-act)/naive,naive,tg)
    out.append((w,bestd,bestr))
pickle.dump((out,units),open('e4_%s_%d.pkl'%({'a':'s1p','B':'s2m','d':'trp'}[first],Lmax),'wb'))
out.sort(key=lambda r:-r[1][0])
print(first,Lmax,'distinct G',len(Gseen),'unit hits (box,N)',len(units),'time %.0f'%(time.time()-t0))
print(' deepest:',[(r[0],r[1]) for r in out[:6]])
print(' best rho:',sorted([(round(r[2][0],3),r[2][1],r[0]) for r in out],reverse=True)[:6])
