from itertools import combinations
from math import gcd
from functools import reduce

def matmul(A,B): return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def foxmat(word,n=4):
    M=eye(n)
    for g in word:
        A=eye(n);i=abs(g)-1
        block=((2,-1),(1,0)) if g>0 else ((0,1),(-1,2))
        for j in range(2):
            for k in range(2): A[i+j][i+k]=block[j][k]
        M=matmul(A,M)
    return M

def det(A):
    if not A:return 1
    return sum((-1)**j*x*det([row[:j]+row[j+1:] for row in A[1:]]) for j,x in enumerate(A[0]))
def smith_invariants(A):
    ds=[1]
    for k in range(1,min(len(A),len(A[0]))+1):
        d=reduce(gcd,(det([[A[i][j] for j in J] for i in I]) for I in combinations(range(len(A)),k) for J in combinations(range(len(A[0])),k)),0)
        if not d:break
        ds.append(abs(d))
    return [ds[i]//ds[i-1] for i in range(1,len(ds))]+[0]*(len(A[0])-len(ds)+1)

if __name__=='__main__':
    word=[3]*3+[-2,-3,-1,-2]*2+[-1]*3
    M=foxmat(word)
    R=[[M[i][j]-int(i==j) for j in range(4)]for i in range(4)]
    print('LL2(1) word',word)
    print('Fox transfer',M)
    print('Fox relations M-I',R)
    print('color group SNF',smith_invariants(R))
    print('reduced (one global color removed) H1 SNF',smith_invariants([row[1:] for row in R]))
