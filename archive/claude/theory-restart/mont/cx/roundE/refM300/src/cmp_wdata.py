"""OWN closure-side data (order 2 and 3) from the formulas w1, w3 (Theorem N) and wV (Theorem V); class stability;
comparison with lpgen's closure_classes / tie_classes and with f1o3.wq3 (order 3)."""
import sys, pickle
from fractions import Fraction as Fr
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/src')
import rlaurent as RL
def jets(f,end,K=3): return RL.logdata(f,end,K)
def wdat(W1,W2,K=3):
    """per end: (p = logjet w1, q = logjet w2); sigma* = sum_ends (p1 - q1); delta* = span W1 - span W2"""
    out={}
    for end in ('top','bot'):
        d1,c1,p=jets(W1,end,K); d2,c2,q=jets(W2,end,K)
        out[end]=(p,q,Fr(c2,c1))
    sig=sum(out[e][0][0]-out[e][1][0] for e in out)
    dst=RL.pspan(W1)-RL.pspan(W2)
    return out,sig,dst
# vertical: odd a, 3 <= |a| <= 41
V={}
for a in [x for x in range(-41,42) if x%2 and abs(x)>=3]:
    V[a]=wdat(RL.w1(a),RL.wV(a))
H={}
for mu in [x for x in range(-40,41) if x]:
    H[mu]=wdat(RL.w1(mu),RL.w3(mu))
# a = +-1 identity: wV(+-1) = t^(+-3) w3(+-1)
print('wV(1) == t^3 w3(1):',RL.wV(1)==RL.pshift(RL.w3(1),3),'  wV(-1) == t^-3 w3(-1):',RL.wV(-1)==RL.pshift(RL.w3(-1),-3))
# vertical classes: (end, sign a, |a|=3 or >=5): typ '+' = (top, a>0) or (bot, a<0)
def vclass(end,a):
    typ='+' if (end=='top')==(a>0) else '-'
    return (typ, abs(a)==3 if typ=='-' else True)
VC={}
for a,(o,sig,dst) in V.items():
    assert sig==-1 and dst==-abs(a)-1, (a,sig,dst)
    for end in ('top','bot'):
        key=(end,1 if a>0 else -1,vclass(end,a))
        p,q,eps=o[end]
        VC.setdefault(key,set()).add((p[:2],q[:2],abs(eps)))
print('vertical: sigma* = -1, delta* = -|a|-1 for all odd 3<=|a|<=41: OK')
for k,s in sorted(VC.items(),key=str): print('  V',k,'order-2 (p,q) values:',s)
# order 3 within classes
VC3={}
for a,(o,sig,dst) in V.items():
    for end in ('top','bot'):
        key=(end,1 if a>0 else -1,vclass(end,a)); p,q,eps=o[end]
        VC3.setdefault(key,set()).add((p,q))
for k,s in sorted(VC3.items(),key=str): print('  V order-3',k,s)
def hclass(mu): return mu if abs(mu)<=3 else (4 if mu>0 else -4)
HC={}; HS={}
for mu,(o,sig,dst) in H.items():
    c=hclass(mu); HS.setdefault(c,set()).add((sig,dst))
    for end in ('top','bot'):
        p,q,eps=o[end]; HC.setdefault((c,end),set()).add((p[:2],q[:2],abs(eps)))
for c in sorted(HS): print('  H class',c,'(sigma*, delta*):',HS[c])
for k,s in sorted(HC.items(),key=str): print('  H',k,'order-2 (p,q):',s)
HC3={}
for mu,(o,sig,dst) in H.items():
    for end in ('top','bot'):
        c=hclass(mu) if abs(mu)!=4 else ('4' if mu>0 else '-4'); c=c if abs(mu)<5 else ('>=5' if mu>0 else '<=-5')
        HC3.setdefault((str(c),end),set()).add((o[end][0],o[end][1]))
for k,s in sorted(HC3.items(),key=str): print('  H order-3',k,s)
pickle.dump(dict(V=V,H=H),open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/refM300/wdata.pkl','wb'))
# ---- compare with lpgen
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import lpg
bad=0
for cl in lpg.closure_classes():
    if cl['kind']=='V':
        key=(cl['end'],cl['asg'],(cl['typ'],cl['a3']))
        s=VC[key]; assert len(s)==1
        (p,q,ae),=s
        ok=(tuple(cl['p'])==p and tuple(cl['q'])==q and cl['sigstar']==-1)
        typ,a3=cl['typ'],cl['a3']
        exp_n=('eq',4) if (typ=='-' and a3) else (('ge',6) if typ=='-' else ('ge',4))
        ok=ok and cl['d0n']==exp_n
    else:
        mu=cl['mu']; s=HC[(mu,cl['end'])]; assert len(s)==1
        (p,q,ae),=s; (sg,ds),=HS[mu]
        ok=(tuple(cl['p'])==p and tuple(cl['q'])==q and cl['sigstar']==sg and cl['d0n']==('eq',-ds))
    if not ok: bad+=1; print('MISMATCH',cl['name'],cl['p'],cl['q'],cl['sigstar'],cl['d0n'])
print('lpgen closure classes:',len(lpg.closure_classes()),'mismatches:',bad)
for tc in lpg.tie_classes():
    if tc['kind']=='V': print('  tie',tc['name'],tc['sigstar'],tc['n'],'(expected sigma*=-1, n - delta.k = |a|+1 >= 4)')
    else:
        (sg,ds),=HS[tc['mu']]; print('  tie',tc['name'],tc['sigstar'],tc['n'],'expected',sg,('eq',-ds),'OK' if (tc['sigstar']==sg and tc['n']==('eq',-ds)) else 'MISMATCH')
