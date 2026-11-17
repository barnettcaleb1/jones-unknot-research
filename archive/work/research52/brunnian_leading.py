from itertools import combinations
import json

def mm(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def comm(a,b):
    ab,ba=mm(a,b),mm(b,a)
    return [[x-y for x,y in zip(u,v)] for u,v in zip(ab,ba)]
def rep(size):
    basis=list(combinations(range(5),size)); index={x:i for i,x in enumerate(basis)}
    mats=[]
    for leaf in range(4):
        perm=list(range(5));perm[leaf],perm[4]=perm[4],perm[leaf]
        a=[[0]*len(basis) for _ in basis]
        for j,x in enumerate(basis): a[index[tuple(sorted(perm[z] for z in x))]][j]=1
        mats.append(a)
    c=comm(mats[0],comm(mats[1],comm(mats[2],mats[3])))
    norm=sum(x*x for row in c for x in row)
    return {'basis':[list(x) for x in basis],'matrix':c,'frobenius_squared':norm}
r1,r2=rep(1),rep(2)
result={'one_subset_rep':r1,'two_subset_rep':r2,'residual_32_frobenius_squared':r2['frobenius_squared']-r1['frobenius_squared']}
assert result['residual_32_frobenius_squared']>0
print(json.dumps(result,indent=2))
