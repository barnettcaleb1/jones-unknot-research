"""find the order-3 subclasses d2_497/16 and d2_460/12 (lpgen F1' survivors) and their boxes."""
import sys, pickle
LPG='/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundD/lpgen'
sys.path.insert(0,LPG); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import f1uni, classes, exact, f1o3
items=exact.load_items()
d2=classes.d2pos()
out={}
for c in d2:
    if c.label not in ('d2_497','d2_460'): continue
    xs=classes.SIGS[c.key]
    for x in xs:
        d3=f1o3.boxdata3(items[x][2])
        k=(c.key,d3['top'][2],d3['top'][5],d3['bot'][2],d3['bot'][5])
        out.setdefault(c.label,{}).setdefault(k,[]).append(x)
for l,d in out.items():
    print(l,'order-3 subclasses',len(d))
    for i,(k,xs) in enumerate(d.items()): print('  sub',i,'boxes',xs[:10],len(xs))
sub=f1uni.subclasses(items,[c for c in d2 if c.label in ('d2_497','d2_460')])
for b in sub: print(b.label,b.x,b.w)
pickle.dump(dict(out=out,sub=[(b.label,b.x,b.w) for b in sub]),open('f1b_o4_prep.pkl','wb'))
