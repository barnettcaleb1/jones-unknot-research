import json, re, math
from fractions import Fraction as Fr
from collections import Counter
R='/Users/calebbarnett/jones-lanes/theory-restart/'
def load_jsonl(p):
    out=[]
    for l in open(p):
        l=l.strip()
        if not l: continue
        try: out.append(json.loads(l))
        except Exception as e: pass
    return out
def parse(rec):
    """return dict k, j, dr (rational delta), specials Counter of (c,d), ok flag"""
    khr=rec.get('khr') or []
    rat=[x for x in khr if x['type']=='r']
    sp=[x for x in khr if x['type']=='s']
    if len(rat)!=1: return None
    r=rat[0]
    k=int(r['slope'])
    qr=Fr(r['q']).limit_denominator(1000)
    jj=(qr-Fr(k*(abs(k)+2),abs(k)+1))/24
    S=Counter()
    lens=set()
    for x in sp:
        lens.add(x['len']); 
        assert x['slope']=='∞', x
        S[(int(round(x['q'])),int(round(x['delta'])))]+=1
        assert abs(x['q']-round(x['q']))<1e-9 and abs(x['delta']-round(x['delta']))<1e-9
    return dict(k=k,j=jj,dr=Fr(r['delta']).limit_denominator(4),S=S,lens=lens)
def mirror(p):
    S=Counter()
    for (c,d),m in p['S'].items(): S[(-c,1-d)]+=m
    return dict(k=-p['k'],j=-p['j'],dr=1-p['dr'],S=S,lens=p['lens'])
def norm(p):
    """normalised specials: c' = c-24j-4, d' = d-4j"""
    j=p['j']; assert j.denominator==1
    j=int(j)
    S=Counter()
    for (c,d),m in p['S'].items(): S[(c-24*j-4,d-4*j)]+=m
    return S
