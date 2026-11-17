"""Exact rational-root/cyclotomic factor extraction; no irreducibility claim."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
def trim(p):
    while p and p[-1]==0:p.pop()
    return p
def div(p,d):
    p=p[:];q=[0]*max(0,len(p)-len(d)+1)
    while len(p)>=len(d):
        assert p[-1]%d[-1]==0
        k=len(p)-len(d);a=p[-1]//d[-1];q[k]=a
        for j,z in enumerate(d):p[k+j]-=a*z
        trim(p)
    return trim(q),p
def pretty(p,var='q'):
    out=[]
    for i,a in reversed(list(enumerate(p))):
        if not a:continue
        atom=str(abs(a)) if not i else (''if abs(a)==1 else str(abs(a))+'*')+var+('^'+str(i)if i>1 else'')
        out.append(('+'if a>0 else'-')+atom)
    return ''.join(out).lstrip('+')or'0'
factors=[('q-1',[-1,1]),('q+1',[1,1]),('q^2+q+1',[1,1,1]),
         ('q^2+1',[1,0,1]),('q^2-q+1',[1,-1,1]),('q^4+1',[1,0,0,0,1]),
         ('q^4-q^2+1',[1,0,-1,0,1]),('q^4+q^3+q^2+q+1',[1,1,1,1,1])]
data=json.loads((HERE/'kernel_specific.json').read_text());out=[]
for row in data['cases']:
    p={int(k):v for k,v in row['Jhat_in_s'].items()};low=min(p)
    assert all((k-low)%2==0 for k in p)
    coeff=[0]*((max(p)-low)//2+1)
    for k,v in p.items():coeff[(k-low)//2]=v
    residual=coeff;found=[]
    for name,f in factors:
        power=0
        while True:
            quot,rem=div(residual,f)
            if rem:break
            residual=quot;power+=1
        if power:found.append({'factor':name,'multiplicity':power})
    result={'label':row['label'],'q_equals':'s^2=A^-4','s_prefactor':low,
            'q_coefficients_ascending':coeff,'extracted_factors':found,
            'residual_coefficients_ascending':residual,'residual_polynomial':pretty(residual),
            'irreducibility_claim':False}
    out.append(result);print(result)
(HERE/'kernel_factors.json').write_text(json.dumps(out,indent=2)+'\n')
