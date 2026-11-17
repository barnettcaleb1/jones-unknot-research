import sys,json
from pathlib import Path
sys.path.insert(0,str(Path('work/research20').resolve()))
import projected_clasp as pc
from collections import defaultdict
n=pc.n
assert n==3

def delta_pow(p,m):
 for _ in range(m):p=pc.loopmul(p)
 return p

def pairing(a,b,hermitian=False,normalized=False):
 out=defaultdict(int)
 for ai,(pa,A) in enumerate(zip(a,pc.BASIS)):
  if not pa:continue
  if hermitian:pa={-e:c for e,c in pa.items()}
  for pb,B in zip(b,pc.BASIS):
   if not pb:continue
   loops=len(set(pc.components([(i,A[i])for i in range(pc.N) if i<A[i]]+[(i,B[i])for i in range(pc.N)if i<B[i]],pc.N)))
   p=delta_pow(pc.mul(pa,pb),loops-int(normalized));pc.addto(out,p)
 return pc.clean(out)

def subtractvec(a,b):return [pc.sub(x,y)for x,y in zip(a,b)]
beta=[1,1,2,2,-1,-1,-2,-2]
doubled=[]
for j in beta:
 i=abs(j);s=1 if j>0 else -1
 doubled += [s*k for k in (2*i,2*i-1,2*i+1,2*i)]
def U(v,word):
 for j in word:v=pc.braid(v, (1 if j>0 else -1)*(abs(j)+1))
 return v
known=json.load(open('work/cancellation19/stoimenow_k3.json'))[0]
expected={-2*int(e):c for e,c in known['coefficients'].items()}
found=[]
for reverse in [False,True]:
 word=doubled[::-1]if reverse else doubled
 uv=U(pc.v,word)
 vk={e+6*n:c for e,c in pairing(pc.t,uv,normalized=True).items()}
 if vk==expected:found.append(reverse)
 lhs=delta_pow(pc.sub(vk,{0:1}),2*n+1)
 coeff={2*n:1}
 for _ in range(n):coeff=pc.mul(coeff,{4:1,0:-1})
 rhs=pc.mul(coeff,pairing(pc.pv,subtractvec(U(pc.pv,word),pc.pv),hermitian=True))
 assert lhs==rhs,(reverse,lhs,rhs)
 print('Exact norm identity verified. Matches source PD:',vk==expected,'reverse:',reverse)
assert found
Path('work/research20/norm_identity_check.json').write_text(json.dumps({'source_PD_match_word_reversal':found,'identity_verified_exactly':True,'scaled_identity':'delta^(2n+1)(V-1)=A^(2n)(A^4-1)^n <P_scaled v,(U-I)P_scaled v>'},indent=2))
