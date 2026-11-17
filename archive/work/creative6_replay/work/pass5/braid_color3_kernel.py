"""Exact spin-one obstruction for all powers of the Bigelow Burau kernel.

R is Jackson--Kerler (0912.2114), equation (23), at s=q^2 and q=2.
We use the 15-dimensional total-lowering-two sector of (C^3)^tensor5.
If |trace(K)|>15 then some eigenvalue has modulus>1, so no nonzero
power or conjugate of K lies in the generic color-three braid kernel.
"""
from fractions import Fraction as F
from pathlib import Path
import itertools,sys,json
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'pass2'))
from braid_kernel import KERNEL,inv
q=F(2);s=q*q
def qnum(n):return (q**n-q**(-n))/(q-q**(-1))
def qfact(n):
    out=F(1)
    for i in range(1,n+1):out*=qnum(i)
    return out
def qb(n,k):return qfact(n)/(qfact(k)*qfact(n-k))
def ident(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)) if a[i][k] and b[k][j])
             for j in range(len(b[0]))] for i in range(len(a))]
def inverse(a):
    n=len(a);m=[row[:]+eye for row,eye in zip(a,ident(n))]
    for i in range(n):
        j=next(j for j in range(i,n) if m[j][i]);m[i],m[j]=m[j],m[i]
        v=m[i][i];m[i]=[x/v for x in m[i]]
        for j in range(n):
            if j==i:continue
            v=m[j][i]
            if v:m[j]=[x-v*y for x,y in zip(m[j],m[i])]
    return [row[n:] for row in m]
def local_R():
    R=[[F(0)]*9 for _ in range(9)]
    for i,j in itertools.product(range(3),repeat=2):
        for k in range(i+1):
            c=s**(-i-j)*q**(2*(i-k)*(j+k)+k*(k-1)//2)*qb(k+j,j)
            for a in range(k):c*=s*q**(-a-j)-s**(-1)*q**(a+j)
            if c:
                assert j+k<=2
                R[3*(j+k)+i-k][3*i+j]+=c
    return R

def run():
    R=local_R();Ri=inverse(R)
    states=[v for v in itertools.product(range(3),repeat=5) if sum(v)==2]
    assert len(states)==15
    index={v:i for i,v in enumerate(states)}
    generators={}
    for g in [1,2,3,4,-1,-2,-3,-4]:
        i=abs(g)-1;r=R if g>0 else Ri;M=[[F(0)]*15 for _ in range(15)]
        for col,v in enumerate(states):
            a,b=v[i:i+2]
            for c,d in itertools.product(range(3),repeat=2):
                val=r[3*c+d][3*a+b]
                if val:
                    target=v[:i]+(c,d)+v[i+2:];M[index[target]][col]+=val
        generators[g]=M
    I=ident(15)
    for i in range(1,5):assert mm(generators[i],generators[-i])==I
    for i in range(1,4):
        assert mm(mm(generators[i],generators[i+1]),generators[i])==mm(mm(generators[i+1],generators[i]),generators[i+1])
    def rho(word):
        out=I
        for g in word:out=mm(out,generators[g])
        return out
    K=rho(KERNEL);tr=sum(K[i][i] for i in range(15))
    assert abs(tr)>15
    assert mm(K,rho(inv(KERNEL)))==I
    data=dict(source='https://arxiv.org/abs/0912.2114; equation (23), s=q^2',
              q=2,dimension=15,kernel_word=KERNEL,trace=str(tr),
              trace_absolute_exceeds_dimension=True,
              conclusion='No nonzero power or conjugate of this Bigelow braid is in the generic color-three braid-representation kernel.',
              limitation='This does not exclude isolated colored-Jones trace coincidences of its knot closures.')
    (ROOT/'braid_color3_kernel.json').write_text(json.dumps(data,indent=2))
    print(data)

if __name__=='__main__':run()
