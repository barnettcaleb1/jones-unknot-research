# Search for one knot K with two strong inversions h, h' having equal j but different M_3 (decisive test for (b)).
# Enumerate TH-2BR words s.l1.W.u2, W over {y0,x0,x1,y1}, length <= LMAX; group by (V_K, Alexander at t=2,3).
import sys, itertools, collections, json
import clib, lp, alex
LMAX=int(sys.argv[1])
groups=collections.defaultdict(dict)
letters=['y0','x0','x1','y1']
cnt=0
for L in range(1,LMAX+1):
    for W in itertools.product(letters,repeat=L):
        if any(W[i][1:]==W[i+1][1:] and W[i][0]!=W[i+1][0] for i in range(L-1)): continue
        w='s.l1.'+'.'.join(W)+'.u2'
        J=lp.J(w)
        if J is None or J=={0:1}: continue
        V=clib.VK(w)
        if V is None or V=={0:1}: continue
        cnt+=1
        key=(tuple(sorted(V.items())), alex.alex_eval(w,2), alex.alex_eval(w,3))
        kJ=tuple(sorted(J.items()))
        if kJ not in groups[key]: groups[key][kJ]=w
print('knots',cnt,' distinct V-classes',len(groups))
hits=[]
for key,d in groups.items():
    if len(d)<2: continue
    rows=[]
    for kJ,w in d.items():
        J=dict(kJ); rows.append((clib.j_of(J),clib.M(J,3),clib.M(J,2),w,kJ))
    byj=collections.defaultdict(set)
    for jj,m3,m2,w,kJ in rows: byj[jj].add(m3)
    for jj,s in byj.items():
        if len(s)>1: hits.append((key,jj,rows))
    
print('V-classes with >=2 inversions:',sum(1 for d in groups.values() if len(d)>=2))
print('classes with equal j but different M_3:',len(hits))
shown=0
for key,jj,rows in sorted(hits,key=lambda h:len(h[0][0])):
    if shown>=6: break
    shown+=1
    print('V_K=',key[0],' alex(2),(3)=',key[1:],' j=',jj)
    for r in rows: print('     j=%d M3=%d M2=%d  %s'%(r[0],r[1],r[2],r[3]))
json.dump([[list(map(list,h[0][0])),h[1],[[r[0],r[1],r[2],r[3]] for r in h[2]]] for h in hits],open('b4_hits.json','w'))
