import sys, time, json
sys.path.insert(0,'nest')
from nlib import *
def Ta(a):  # outer twist letters on positions 1,2 ; a>0 -> x2 (mont sign convention: VP(3,-2) = T(3,4) = mont(1,[3,3]))
    return '.'.join((['x2'] if a>0 else ['y2'])*abs(a))
def Vword(B,a):
    return 's.l1.'+(B+'.' if B else '')+Ta(a)+'.u1'
boxes=load_boxes()
vy0=vec('y0'); print('pinned vector of body y0:',[fmt(x) for x in vy0[0]] if vy0 else vy0)
vx0=vec('x0'); print('pinned vector of body x0:',[fmt(x) for x in vx0[0]] if vx0 else vx0)
E1=[ONE,{}]
VY=vy0[0]
res={}
for a in (1,-1,3,-3,5,-5,7):
    J1=J(Vword('',a)); J2=J(Vword('y0',a))
    if J1 is None or J2 is None: print('a',a,'base not knot'); continue
    cands=[]
    for k in range(-60,61):
        for s in (1,-1):
            u2J2=mul(mono(k,s),J2)
            l1=J1
            # l.VY = l1*VY0 + l2*VY1 = u2 J2
            l2=divexact(sub(u2J2,mul(l1,VY[0])),VY[1])
            if l2 is None: continue
            L=[l1,l2]
            good=True
            for B,v in boxes[:6]:
                Jw=J(Vword(B,a))
                if Jw is None: continue
                if normalize(add(mul(L[0],v[0]),mul(L[1],v[1])))!=Jw: good=False; break
            if good: cands.append(L)
    print('a=%d: candidate functionals %d'%(a,len(cands)))
    if len(cands)==1:
        L=cands[0]; res[a]=L
        ok=bad=0
        for B,v in boxes:
            Jw=J(Vword(B,a))
            if Jw is None: continue
            if normalize(add(mul(L[0],v[0]),mul(L[1],v[1])))==Jw: ok+=1
            else: bad+=1
        print('   l_a =',fmt(L[0]),' | ',fmt(L[1]),'   test on all 50 boxes: ok',ok,'bad',bad,flush=True)
json.dump({str(a):[sorted(L[0].items()),sorted(L[1].items())] for a,L in res.items()},open('nest/p4_functionals.json','w'))
