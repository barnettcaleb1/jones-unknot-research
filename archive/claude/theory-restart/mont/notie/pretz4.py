"""T2 pretzels: one positive row j, negative rows l_i, mu=-m<=-2 (k=0). Tabulate top(H) vs generic max(2, j+3-m, j+2-lmin)."""
from pretz import *
import itertools
from collections import Counter
def topH(mu,rows): return top(G(mu,rows))-2*len(rows)
C=Counter(); ex=[]
for m in range(2,7):
    for j in range(1,8):
        for q in (1,2,3):
            for ls in itertools.combinations_with_replacement(range(1,8),q):
                rows=[2*j+1]+[-(2*l+1) for l in ls]
                th=topH(-m,rows); lmin=min(ls)
                gen=max(2,j+3-m,j+2-lmin)
                key=('a' if j==m-1 else '')+('b' if (j==lmin and list(ls).count(lmin)==1) else '')
                C[(key,th-gen)]+=1
                if key and len(ex)<0: ex.append((m,j,ls,th,gen))
for k in sorted(C,key=str): print(k,C[k])
# exact pair identity: H for rows (2j+1, -(2j+1)), mu=-m
for m in (2,3,4,5):
    print('m',m,[ (j, topH(-m,[2*j+1,-(2*j+1)])) for j in range(1,8)])
