import sys, json
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft/ident')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import lp, diag, words
from fractions import Fraction as F
import congr
out=[]
for k in range(1,5):
    w=words.mont(-k,[4*k-1,4*k+1])
    r=congr.check(w)
    J=lp.J(w)
    r['span']=max(J)-min(J); r['k']=k
    r['M2']=sum(c*(-1)**(e%2)*e**2 for e,c in J.items())
    out.append(r)
    print('k=%d P(%d,%d,%d) len(word)=%d spanJ=%d a2=%s v3=%s a4=%s j4=%s M2=%s M3=%s M4=%s D=%s F4=%s  v3 mod5=%s j4 mod5=%s'%(
        k,2*k,4*k-1,4*k+1,len(w.split('.')),r['span'],r['a2'],r['v3'],r['a4'],r['j4'],r['M2'],r['M3'],r['M4'],r['D'],r['F4'],r['v3']%5,r['j4']%5))
json.dump([{kk:str(v) for kk,v in r.items()} for r in out],open('family_values.json','w'))
