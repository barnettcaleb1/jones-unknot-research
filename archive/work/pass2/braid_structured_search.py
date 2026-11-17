#!/usr/bin/env python3
"""Finite structured, exact search inside the normal closure of a Burau kernel.
No random braid sampling and no finite-field-only acceptance.
"""
from braid_kernel import *
import argparse

def run(radius=3):
    validate();started=time.monotonic()
    anchors=[[s*i for s,i in zip(signs,range(1,5))] for signs in itertools.product((-1,1),repeat=4)]
    contexts=[[]]+[[s*i] for s in (-1,1) for i in range(1,5)]
    pairs=[(m,n) for m in range(-radius,radius+1) if m for n in range(-radius,radius+1) if n]
    hits=[];best=[];done=0;rows=[]
    for m,n in pairs:
        kernel=comm(power(HALF,m),power(FULL,n))
        vec=tl_vector(kernel)
        localbest=None
        for c in contexts:
            for alpha in anchors:
                suffix=c+alpha+inv(c)
                w=sum(1 if s>0 else -1 for s in alpha)
                v=close_vector(tl_vector(suffix,vec),w)
                score=(len(v),max(v)-min(v),sum(abs(z) for z in v.values()))
                desc=dict(m=m,n=n,context=c,anchor=alpha,score=score)
                done+=1
                if v=={0:1}:
                    desc['word']=reduce(kernel+suffix);hits.append(desc)
                if localbest is None or score<localbest['score']:
                    localbest={**desc,'jones_A':v,'word':reduce(kernel+suffix)}
        rows.append(localbest)
        print('m,n',m,n,'checks',done,'hits',len(hits),'best',localbest['score'],'elapsed',round(time.monotonic()-started,1),flush=True)
    report=dict(radius=radius,pairs=len(pairs),anchors=anchors,contexts=contexts,checks=done,hits=hits,
                best_by_pair=rows,seconds=time.monotonic()-started)
    (ROOT/'braid_structured_results.json').write_text(json.dumps(report,indent=2))
    print('FINAL',done,'checks',len(hits),'Jones-one hits',round(report['seconds'],2),'seconds',flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--radius',type=int,default=3);run(ap.parse_args().radius)
