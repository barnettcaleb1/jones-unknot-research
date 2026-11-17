"""Pairing adapter using exact rational PL transport of source arcs."""
from pathlib import Path
import sys,json,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'width6_targeted'))
import geometric_intersections as old
import transport_pl as pl

def transported(curve,word,step=None):
    rational=[(pl.F(z.real),pl.F(z.imag))for z in curve]
    return pl.complex_curve(pl.braid_curve(rational,word))

def run(matrix_word,source_caps=((1,2),(3,4)),resolution=64):
    old.braid_curve=transported
    result=old.model([-g for g in matrix_word],resolution,source_caps=source_caps)
    result['transport']='Exact rational PL cell splitting; float conversion only at intersection/winding stage'
    result['matrix_word']=matrix_word
    return result

if __name__=='__main__':
    word=[4,3,2,1,5,4,3,2,3,4,2,3,-1,-2]
    start=time.monotonic()
    result=run(word)
    result['seconds']=time.monotonic()-start
    print('RESULT',result['polynomial'],result['TL_line_specialization'],result['seconds'])
    (HERE/'transport_pairing_14.json').write_text(json.dumps(result,indent=2)+'\n')
