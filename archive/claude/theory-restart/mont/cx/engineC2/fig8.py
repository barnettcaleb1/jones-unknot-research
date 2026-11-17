import sys, itertools
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/ft')
import lp, alex
sys.path.insert(0,"/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineC2"); from vk import VK
def pal(J): return J=={-e:c for e,c in J.items()}
seen={}
for L in range(1,7):
    for W in itertools.product(['x0','y0','x1','y1'],repeat=L):
        w='s.l1.'+'.'.join(W)+'.u2'
        J=lp.J(w)
        if J is None or len(J)==1: continue
        V=VK(w)
        if V is None: continue
        Vk=tuple(sorted(V.items()))
        palV = V=={-e:c for e,c in V.items()}
        if palV:   # amphicheiral-looking knot
            key=(Vk,tuple(sorted(J.items())))
            if key in seen: continue
            seen[key]=w
            print('K amph? V=',Vk,' det',alex.alex_eval(w,-1),' J pal:',pal(J),' span J',lp.span(J),' w=',w)
