import json, re, os
from fractions import Fraction as Fr
BASE='/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/tilt'
def load():
    recs=[]
    for l in open(os.path.join(BASE,'run_3_45.jsonl')):
        r=json.loads(l)
        if 'khr' not in r or not r['khr']: continue
        f=os.path.join(BASE,r['file'])
        txt=open(f).read().splitlines()
        word=txt[1].strip()
        com=txt[3] if len(txt)>3 else ''
        m=re.search(r'= \[([\d,\-]+)\]',com)
        cf=[int(x) for x in m.group(1).split(',')] if m else None
        sym = 1 if 'symmetry 1' in com else (2 if 'symmetry 2' in com else 0)
        rat=[c for c in r['khr'] if c['type']=='r']
        sp=[c for c in r['khr'] if c['type']=='s']
        assert len(rat)==1
        k=int(rat[0]['slope']); qr=Fr(rat[0]['q']).limit_denominator(1000)
        # qr = 24 j + k(|k|+2)/(|k|+1)
        j=(qr-Fr(k*(abs(k)+2),abs(k)+1))/24
        specials=sorted([(int(c['q']),int(c['delta'])) for c in sp], key=lambda x:(x[1],x[0]))
        recs.append(dict(name=os.path.basename(f)[:-4],p=r['p'],q=r['q'],word=word,cf=cf,sym=sym,k=k,j=j,dr=rat[0]['delta'],specials=specials,lens=set(c['len'] for c in sp),bn=r.get('bn',[])))
    return recs
if __name__=='__main__':
    for r in load():
        lev={}
        for c,d in r['specials']: lev.setdefault(d,[]).append(c)
        print(r['name'],r['cf'],'sym',r['sym'],r['word'],'k',r['k'],'j',r['j'],'dr',r['dr'],' '.join('%d:%s'%(d,sorted(v)) for d,v in sorted(lev.items())), r['lens'])
