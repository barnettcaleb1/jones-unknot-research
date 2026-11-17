from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'braid_classification/packages'))
from spherogram import Link,Crossing,Strand
from spherogram.links.tangles import join_strands
import regina

def make(L=3,fig='omega1',closure='vertical',fixed_orientation=False):
    names=['a','b','c','d']+[f'z{i}' for i in range(L)]
    cs={n:Crossing(n)for n in names}
    rots={n:0 for n in names}
    if fig=='omega1':rots.update(a=1,d=1)
    elif fig=='omega5':rots.update(b=1,c=1,z0=1)
    elif fig=='claimed':rots.update(a=1,d=1,z0=1)
    elif fig=='swapped':rots.update(b=1,c=1)
    def p(n,i):return cs[n],(i+rots[n])%4
    def e(n,i,m,j):join_strands(p(n,i),p(m,j))
    e('a',2,'b',2);e('a',3,'b',1)
    e('c',0,'d',0);e('c',3,'d',1)
    e('a',0,'z0',1);e('b',0,'z0',2)
    for i in range(L-1):e(f'z{i}',0,f'z{i+1}',1);e(f'z{i}',3,f'z{i+1}',2)
    e(f'z{L-1}',0,'c',2);e(f'z{L-1}',3,'d',2)
    if closure=='vertical':e('a',1,'b',3);e('c',1,'d',3)
    else:e('a',1,'c',1);e('b',3,'d',3)
    K=Link(list(cs.values()),check_planarity=not fixed_orientation,build=not fixed_orientation)
    if fixed_orientation:
        assert closure=='vertical'
        K._build(start_orientations=[p('a',1),p('c',1),p('a',2)])
    assert K.is_planar()
    return K

def rec(K):
    pd=K.PD_code();R=regina.Link.fromPD([[i+1 for i in c]for c in pd]);v=R.jones()
    o={'PD':pd,'Jones':str(v),'writhe':K.writhe(),'regina_writhe':R.writhe(),'components':len(K.link_components),'crossing_signs':{str(c.label):c.sign for c in K.crossings}}
    K.simplify('global');o['simplified_PD']=K.PD_code();o['simplified_components']=len(K.link_components)+K.unlinked_unknot_components
    return o
if __name__=='__main__':
    d={}
    for cl in ['vertical','horizontal']:
      for fig in ['omega1','omega5','claimed']:
        d[cl+'_'+fig]=rec(make(fig=fig,closure=cl));print(cl,fig,d[cl+'_'+fig])
    for fig in ['omega1','omega5','claimed']:
        d['fixed_'+fig]=rec(make(fig=fig,fixed_orientation=True));print('fixed',fig,d['fixed_'+fig])
    for fig in ['omega1','swapped']:
        d['L1_horizontal_'+fig]=rec(make(L=1,fig=fig,closure='horizontal'));print('L1 horizontal',fig,d['L1_horizontal_'+fig])
    Path(__file__).with_suffix('.json').write_text(json.dumps(d,indent=2)+'\n')
