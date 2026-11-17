"""Mixed commutators and balanced products of short conjugates of K."""
from braid_conjugates import *

def run(maxlen=3):
    started=time.monotonic();K=evaluate(tl.rho(bk.KERNEL));Ki=evaluate(tl.rho(bk.inv(bk.KERNEL)))
    entries=[];seen=set()
    for c,G,Gi in words(maxlen):
        X=mm(mm(Gi,K),G)
        if key(X) in seen:continue
        seen.add(key(X));entries.append((c,X,mm(mm(Gi,Ki),G)))
    anchors=[[s*i for s,i in zip(signs,range(1,5))] for signs in itertools.product((-1,1),repeat=4)]
    AM=[rho(a) for a in anchors];targets=[traceprod(I,a) for a in AM]
    hits=[];count=0
    for (c,X,Xi),(d,Y,Yi) in itertools.combinations(entries,2):
        choices=[('XYi',mm(X,Yi)),('XiY',mm(Xi,Y))]
        choices += [(f'comm_{s}_{t}',comm(a,b,ai,bi))
                    for s,a,ai in [(1,X,Xi),(-1,Xi,X)]
                    for t,b,bi in [(1,Y,Yi),(-1,Yi,Y)]]
        for kind,M in choices:
            for alpha,A,target in zip(anchors,AM,targets):
                count+=1
                if traceprod(M,A)==target:
                    # For balanced products, this exact braid equality makes
                    # the whole closure visibly conjugate to alpha.
                    tautology=(kind in ('XYi','XiY') and
                        artin(d+alpha+bk.inv(c))==[[i] for i in range(1,6)])
                    hits.append(dict(c=c,d=d,kind=kind,anchor=alpha,
                                     matrix_identity=M==I,geometric_tautology=tautology))
    report=dict(conjugators=len(entries),maxlen=maxlen,trace_tests=count,hits=hits,
                seconds=time.monotonic()-started)
    (ROOT/'braid_pairs_results.json').write_text(json.dumps(report,indent=2))
    print('pairs',len(entries),'trace tests',count,'hits',len(hits),'unresolved',
          sum(not h['geometric_tautology'] for h in hits),'seconds',round(report['seconds'],2),flush=True)
    return report

if __name__=='__main__':run()
