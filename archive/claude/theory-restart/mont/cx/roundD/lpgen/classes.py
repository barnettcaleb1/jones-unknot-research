"""jet classes from engine C1's signature table (gen2_res.pkl): key = (top (ra,la,rb,lb), bot (...), sigma, delta)."""
import pickle, collections, sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen')
import lpg
G=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1/gen2_res.pkl','rb'))
SIGS=G['sigs']; TAGS=G['tags']; TREES=G['trees']
ORDER=sorted(SIGS.items(),key=lambda kv:(-len(kv[1]),str(kv[0])))
def top(K): return [lpg.Cls(k,len(xs),'top%d'%i) for i,(k,xs) in enumerate(ORDER[:K])]
def d2pos():
    out=[]
    for i,(k,xs) in enumerate(ORDER):
        if any(TAGS[x]=='d2pos' for x in xs): out.append(lpg.Cls(k,len(xs),'d2_%d'%i))
    return out
def allcls(): return [lpg.Cls(k,len(xs),'c%d'%i) for i,(k,xs) in enumerate(ORDER)]
