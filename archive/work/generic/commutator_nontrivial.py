"""Exact integer verification of the all-r commutator determinant recurrence."""
def mul(A,B):return [[sum(A[i][k]*B[k][j]for k in range(2))for j in range(2)]for i in range(2)]
def inv(A):return [[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]
A=[[1,2],[0,1]];B=[[1,0],[-2,1]];R=[[0,1],[-1,1]]
C=A
for r in range(1,11):
 a,b=C[0];c,d=C[1]
 assert b//2<=d<b
 assert a*d-b*c==1
 M=mul(C,R)
 determinant=abs(2-M[0][0]-M[1][1])
 assert determinant>1
 print(r,'determinant',determinant)
 D=[[1-2*b*d+4*b*b,2*b*b],[2-2*d*d+4*b*d,1+2*b*d]]
 assert D==mul(mul(mul(C,B),inv(C)),inv(B))
 assert sum(mul(D,R)[i][i]for i in range(2))>=3+b*b//2
 C=D
