"""Explicit V3-class examples: K (arborescent, hyperbolic?) and branch knots L_n = T(1/n) (det 1, Jones, extreme coefficients,
SnapPea solution of S^3_{1/n}(K) = Sigma_2(L_n))."""
import sys, json, time
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/engineA')
import bk, vc, lp, a2search, identK
import regina
EX={'E1':(-3,-3,['XY','xy']), 'E2':(3,0,['XY','XY']), 'E3':(3,1,['XY','XXY']), 'E4':(-3,-2,['XY','xxyy']), 'E5':(5,0,['XY','XY','xy']), 'E6':(-3,-2,['XXXXY','XYXyy','xxYXY']), 'E7':(3,2,['XXYY','xxxy'])}
def run(name, ns=(1,-1,2,-2,3,-3), quick=False):
    a,N,boxes=EX[name]
    hw=identK.halfword(a,N,boxes)
    J=lp.J(hw); a2=lp.a2(J)
    fK=bk.full_K(hw); pdK=bk.pd_code(fK)
    VK=identK.jones_of_pd(pdK)
    S=bk.snap(pdK)
    tri=regina.Link.fromPD(pdK).complement()
    sas=tri.hasStrictAngleStructure()
    out={'name':name,'a':a,'N':N,'boxes':boxes,'slopes':[str(a2search.slope(w)) for w in boxes],'halfword':hw,
         'J':sorted(J.items()),'spanJ':lp.span(J),'a2':a2,'K_crossings':len(pdK),'V_K':sorted(VK.items()),
         'K_volume':S.volume(),'K_solution':str(S.solutionType()),'K_strict_angle_structure':sas,'L':[]}
    print(name,'a=%d N=%d boxes=%s slopes=%s'%(a,N,boxes,out['slopes']),'spanJ',out['spanJ'],'a2',a2,
          '| K: cross',len(pdK),'vol %.6f'%out['K_volume'],out['K_solution'],'strictAS',sas,flush=True)
    f=bk.frame(hw)
    for n in ns:
        t0=time.time()
        full=bk.full_Ln(hw,n,f)
        br=bk.bracket_full(full); det=bk.det_from_bracket(br)
        pd=bk.pd_code(full)
        V=bk.jones_t(regina.Link.fromPD(pd))
        ks=sorted(V); lo,hi=ks[0],ks[-1]
        vol,st,h=bk.filled(S,1,n)
        Ls=regina.Link.fromPD(pd); Ls.simplify(); pds=[tuple(x) for x in Ls.pdData()]
        rec={'n':n,'simplified_crossings':len(pds),'simplified_adequacy':bk.adequacy(pds),'diagram_crossings':len(pd),'det':det,'V':sorted(V.items()),'spanV':hi-lo,'extreme':(V[lo],V[hi]),
             'V_is_1':V=={0:1},'diagram_adequacy':bk.adequacy(pd),'Sigma2_vol':vol,'Sigma2_solution':st,'Sigma2_H1':h,'nonsemiadequate_certified':abs(V[lo])!=1 and abs(V[hi])!=1}
        out['L'].append(rec)
        print('   L_%d: diagram %d crossings, det %d, span V %d, extreme coeffs %s, V==1? %s | S^3_{1/n}(K): vol %.6f %s H1=%s | non-semiadequate: %s | diagram A/B-adequate: %s | simplified %d cr, A/B-adequate: %s (%.1fs)'%(
            n,len(pd),det,hi-lo,rec['extreme'],rec['V_is_1'],vol,st,h,rec['nonsemiadequate_certified'],rec['diagram_adequacy'][:2],rec['simplified_crossings'],rec['simplified_adequacy'][:2],time.time()-t0),flush=True)
    return out
if __name__=='__main__':
    names=sys.argv[1:] or list(EX)
    res=[run(nm) for nm in names]
    json.dump(res,open('examples_%s.json'%('_'.join(names)),'w'),indent=1,default=str)
