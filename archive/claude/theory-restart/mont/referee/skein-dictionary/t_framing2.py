import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont'); sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
def signs(w):
    full=alex.symmetrize(alex.parse(w)); cr=alex.diagram(full)
    out=[]
    for x in cr:
        ov=(1,-1) if x['ty']=='x' else (-1,-1)
        un=(-1,-1) if x['ty']=='x' else (1,-1)
        if not x['od']: ov=(-ov[0],-ov[1])
        if not x['ud']: un=(-un[0],-un[1])
        out.append(1 if ov[0]*un[1]-ov[1]*un[0]>0 else -1)
    return out
d=json.load(open('check_dictionary.json'))
data=[]
for r in d['rows']:
    w=r['w']; k=r['halftwists_to_pref']
    half=alex.parse(w)
    sg=signs(w)
    # map full crossings to half letters: on-axis letters -> 1 crossing, off-axis -> 2
    i=0; s0=0; s1=0
    for c,s in half:
        if c in 'xy':
            if s==0: s0+=sg[i]; i+=1
            else:
                assert sg[i]==sg[i+1]; s1+=sg[i]; i+=2
    data.append((k,s0,s1))
import itertools
sol=None
for a in [x/2 for x in range(-8,9)]:
    for b in [x/2 for x in range(-8,9)]:
        if all(abs(k-(a*s0+b*s1))<1e-9 for k,s0,s1 in data): sol=(a,b); print('k = %s*s0 + %s*s1  (s0 = signed on-axis crossings of K, s1 = signed off-axis pairs)'%(a,b))
print('n=',len(data),'solution',sol)
print(data[:8])
