"""T2 pretzels (one positive row j, q negative rows l_i, mu=-m<=-2, k=0): min top(H), and span - 3n."""
from pretz import *
import itertools, time
t0=time.time()
def topH(mu,rows): return top(G(mu,rows))-2*len(rows)
mn=(99,None); mnsp=(99,None); cnt=0
for m in range(2,9):
    for j in range(1,10):
        for q in (1,2,3,4):
            for ls in itertools.combinations_with_replacement(range(1,9),q):
                if q==4 and max(ls)>5: continue
                rows=[2*j+1]+[-(2*l+1) for l in ls]
                g=G(-m,rows); th=top(g)-2*len(rows); sp=span(g)-2; n=len(rows); cnt+=1
                if th<mn[0]: mn=(th,(m,j,ls))
                if sp-3*n<mnsp[0]: mnsp=(sp-3*n,(m,j,ls,sp))
print('T2 pretzels checked',cnt,'min top(H)',mn,'min span-3n',mnsp,'time',round(time.time()-t0,1))
