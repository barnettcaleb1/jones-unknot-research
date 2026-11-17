"""Replay one actual LL2(2) Goeritz computation and the split-union gate."""
import json, sys
from pathlib import Path
from fractions import Fraction as F
from math import gcd, lcm
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'work/research33'))
from lll_linking_form import hopf,RationalTangle,goeritz,rref,det,inv,fox_factors,regina

L=hopf(RationalTangle(17,6),RationalTangle(-17,6))
G=goeritz(L)
rr,p=rref(G)
free=[i for i in range(len(G))if i not in p]
assert len(free)==1
k=[F(0)]*len(G);k[free[0]]=1
for i,j in enumerate(p):k[j]=-rr[i][free[0]]
den=lcm(*[x.denominator for x in k]);k=[int(x*den)for x in k]
g=gcd(*k);k=[x//g for x in k]
pivot=next(i for i,x in enumerate(k)if abs(x)==1)
ids=[i for i in range(len(G))if i!=pivot]
B=[[G[i][j]for j in ids]for i in ids];Bi=inv(B)
N=abs(int(det(B)))
j=next(j for j in range(len(B))if lcm(*[r[j].denominator for r in Bi])==N)
vec=[int(i==j)for i in range(len(B))]
a=int(Bi[j][j]*N)%N
r=regina.Link.fromPD([[x+1 for x in row]for row in L.PD_code()])
assert N==433 and a==75
assert r.countComponents()==2 and str(r.jones())=='-x - x^-1'
assert fox_factors(L.PD_code())==([433],1)
assert 178**2%433==75 and (-180**2)%433==75
saved=json.loads((ROOT/'work/research41/ll2_auxiliary_pairing.json').read_text())
assert saved['pd']==[list(row)for row in L.PD_code()]
assert saved['Goeritz']==G and saved['block']==B and saved['kernel']==k
assert saved['generator']==vec and saved['linking_numerator']==a
lll=json.loads((ROOT/'work/research33/lll_linking_form.json').read_text())[1]
assert lll['torsion_order']==144 and lll['linking_numerator']==143
totalN=433*144
totalA=(144*75-433)%totalN
assert totalA==10367 and (1727**2+totalA)%totalN==0
assert gcd(1727,totalN)==1
print('Actual PD Jones, Goeritz pairing, saved certificate, and combined unit-square gate all pass.')
