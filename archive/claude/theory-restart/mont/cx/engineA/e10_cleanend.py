"""Clean-end analysis for vertical closures of rational products. Order-K log-jets of the a- and b-channels at the top
(normalised series of a(u), b(u)); targets from w1(a), wV(a) and the Phi_3 pattern."""
import sys, collections
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import vc, eng, lib, ser, jets
from fractions import Fraction as Fr
K=4
def chjets(f,end): d=ser.pdata(f,end,K); return (d[1],jets.logs(d[2]))
L=int(sys.argv[1]) if len(sys.argv)>1 else 9
R=lib.rational(L)
ta=collections.Counter(); tb=collections.Counter(); pair=collections.Counter()
for b in R:
    a,bb=b[1]
    ja=chjets(a,'top'); jb=chjets(bb,'top')
    ta[(ja[0],)+tuple(ja[1])]+=1; tb[(jb[0],)+tuple(jb[1])]+=1
    pair[((ja[0],)+tuple(ja[1]),(jb[0],)+tuple(jb[1]))]+=1
print('R(%d): %d boxes; distinct top a-jets %d, b-jets %d, (a,b) jet pairs %d'%(L,len(R),len(ta),len(tb),len(pair)))
def show(c,name):
    l1=collections.Counter(k[1] for k in c.elements())
    print(name,'l1 values',sorted((str(k),v) for k,v in l1.items()))
show(ta,'a-channel'); show(tb,'b-channel')
# b-channel jets among boxes with l1(b)=0
z=collections.Counter(k[1:] for k in tb.elements() if k[1]==0)
print('b-jets with l1=0: (l2,l3,l4) ->',sorted(((str(x[1]),str(x[2]),str(x[3])),v) for x,v in z.items()))
z=collections.Counter(k[1:] for k in ta.elements() if k[1]==0)
print('a-jets with l1=0: (l2,l3,l4) ->',sorted(((str(x[1]),str(x[2]),str(x[3])),v) for x,v in z.items())[:12])
for a in (3,5,7,9):
    a1,aV=eng.WV(a)
    print('a=%d  w1 top jet'%a,[str(x) for x in chjets(a1,'top')[1]],' wV top jet',[str(x) for x in chjets(aV,'top')[1]],
          ' w1 bot',[str(x) for x in chjets(a1,'bot')[1]],' wV bot',[str(x) for x in chjets(aV,'bot')[1]])
print('Phi3 pattern jet',[str(x) for x in jets.logs((1,1,0,0))])
