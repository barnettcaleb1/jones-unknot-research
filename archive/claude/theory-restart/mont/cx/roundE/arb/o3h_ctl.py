"""NEGATIVE CONTROL for o3h: genuine units (two-bridge unknots) of single rational boxes at mu = +-2 live in the 'd=0 r=1' case
(refGen).  Feeding such a box as 'B' with n = 0 must leave at least one weak end OPEN at order 3 (else the order-3 equality is wrong)."""
import sys, pickle
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/roundE/arb')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import o3h, vc, lib, eng, ser, jets
from fractions import Fraction as Fr
from jbox_val import bdata
def lj3(f,end): return jets.logs(ser.pdata(f,end,3)[2])
R=lib.rational(6); found=0; results=[]
for k,v,T,tag in R:
    us=[(mu,N) for mu,N,J in eng.hclosures(v) if J is not None and len(J)==1 and abs(mu)==2]
    if not us: continue
    key,el=bdata(v)
    if not el: continue
    d3=(lj3(v[0],'top')[2],lj3(v[1],'top')[2],lj3(v[0],'bot')[2],lj3(v[1],'bot')[2])
    for mu in sorted(set(m for m,N in us)):
        out=[o3h.one((key,d3,mu,end,mu))[1] for end in ('top','bot')]
        results.append((T,mu,out)); found+=1
ok=all(any(('open' in o) or ('closed' not in o.lower()) for o in out) for T,mu,out in results)
for r in results[:12]: print(r)
print('unit boxes tested',found,'| every unit left OPEN at some end:',ok)
