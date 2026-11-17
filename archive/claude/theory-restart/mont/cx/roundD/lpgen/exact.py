"""EXACT search of the LP-open frontier (Lemma W windows via engineA eng.hclosures / eng.vclosures; complete for units).
Gates logged for near misses: a_2 = 0 and J(zeta_10) = 1 (J - 1 divisible by Phi_10)."""
import sys, pickle, time, collections, itertools
EA='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA'; C1='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1'
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'); sys.path.insert(0,EA)
import vc, eng, lp
def load_items():
    L=pickle.load(open(C1+'/libA_jets.pkl','rb'))
    items=[(tag,T,v) for (k,T,tag,tp,bt),v in zip(L['boxes'],L['vecs']) if tag!='R']
    d2=pickle.load(open(EA+'/d2pos_boxes.pkl','rb'))
    items+=[('d2pos',b[2],b[1]) for b in d2]
    return items
def z10(Jn):
    r=[0]*5
    for e,c in Jn.items():
        q,rem=divmod(e,5); r[rem]+=c*(-1)**(q%2)
    r[0]-=1
    c4=r[4]   # subtract c4*Phi10 = c4(t^4 - t^3 + t^2 - t + 1)
    r=[r[0]-c4,r[1]+c4,r[2]-c4,r[3]+c4,0]
    return all(x==0 for x in r)
def check(job):
    tag,vecs=job
    p=vc.starall(vecs)
    out=dict(tag=tag,n=0,units=[],gates=[],minspan=None)
    try:
        cands=[('H',)+c for c in eng.hclosures(p)]+[('V',)+c for c in eng.vclosures(p)]
    except Exception as ex:
        out['err']=repr(ex); return out
    for kind,x,N,J in cands:
        if J is None: continue
        out['n']+=1
        if len(J)==1: out['units'].append((kind,x,N,J)); continue
        Jn=vc.norm(J)
        if Jn is None: continue
        sp=max(Jn)-min(Jn)
        if out['minspan'] is None or sp<out['minspan'][0]: out['minspan']=(sp,kind,x,N)
        if lp.a2(Jn)==0 and z10(Jn): out['gates'].append((kind,x,N,sp))
    return out
