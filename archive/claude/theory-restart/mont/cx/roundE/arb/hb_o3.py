"""Per dangerous class B (n=2 depth-one, 636 with order-3 data): H(B) = 'B + any n >= 1 rational boxes, any N, any mu' at ORDER 2
by C1's generator gen2.proveH (imported read-only), then the remaining TWO-ENDED cases ('d=0 r=1', ties) from o3h at ORDER 3.
A class is H-CLOSED if every open order-2 case is two-ended and closed at order 3 for every order-3 subclass."""
import sys, pickle, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC1')
import gen2
O=pickle.load(open('o3h.pkl','rb'))
OK=('n<0','r1: closed@2','r1: order3 CLOSED','tie T3=False T2:closed')
per=collections.defaultdict(lambda: collections.defaultdict(list))
for (key,d3,mu,end,mu3),v in O['res']: per[key][mu].append(v)
stat=collections.Counter(); closed=[]; why=collections.Counter()
for key,mus in per.items():
    bd={'top':key[0],'bot':key[1]}
    res=gen2.proveH(bd,key[2],key[3],1)
    allok=True
    for mu,opn in res.items():
        if not opn: continue
        o3ok=all(v in OK for v in mus.get(mu,[]))
        names=[o.split(':')[-1] if isinstance(o,str) else str(o) for o in opn]
        two=all(('d=0' in x) or ('tie' in x) or ('sigma' in x) or ('n=' in x) for x in names)
        if not (two and o3ok):
            allok=False; why[(mu,tuple(sorted(set(names)))[:3],o3ok)]+=1
    stat['H-closed' if allok else 'open']+=1
    if allok: closed.append(key)
print('dangerous n=2 classes (with order-3 data):',len(per),dict(stat))
for k,v in why.most_common(12): print('   open:',k,v)
pickle.dump(dict(closed=closed,why=dict(why)),open('hb_o3.pkl','wb'))
