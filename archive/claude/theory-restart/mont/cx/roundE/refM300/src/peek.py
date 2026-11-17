import pickle, collections
from fractions import Fraction as Fr
G=pickle.load(open('/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1/gen2_res.pkl','rb'))
print(G.keys())
SIGS=G['sigs']; TAGS=G['tags']; TREES=G['trees']
ORDER=sorted(SIGS.items(),key=lambda kv:(-len(kv[1]),str(kv[0])))
print('signatures',len(SIGS),'boxes',sum(len(v) for v in SIGS.values()),'items',len(TAGS))
top=ORDER[:300]
print('top300 boxes',sum(len(x) for k,x in top))
print('example key',top[0][0])
sig=collections.Counter(k[2] for k,x in top); dl=collections.Counter(k[3] for k,x in top)
print('sigma values',sorted(sig.items())); print('delta values',sorted(dl.items()))
tg=collections.Counter(TAGS[i] for k,x in top for i in x); print('tags',tg)
# weight of 300th class
print('weights 0,1,299,300:',len(ORDER[0][1]),len(ORDER[1][1]),len(ORDER[299][1]),len(ORDER[300][1]))
# ties in ordering at the 300 boundary
w300=len(ORDER[299][1]); print('classes with weight == w300:',sum(1 for k,x in ORDER if len(x)==w300), 'index range', [i for i,(k,x) in enumerate(ORDER) if len(x)==w300][:3], [i for i,(k,x) in enumerate(ORDER) if len(x)==w300][-3:])
d2=[(i,k,x) for i,(k,x) in enumerate(ORDER) if any(TAGS[j]=='d2pos' for j in x)]
print('d2pos classes',len(d2))
print('d2pos sigma',sorted(collections.Counter(k[2] for i,k,x in d2).items()))
print('d2pos delta',sorted(collections.Counter(k[3] for i,k,x in d2).items()))
# overlap d2pos with top300?
print('d2pos within top300:',sum(1 for i,k,x in d2 if i<300))
