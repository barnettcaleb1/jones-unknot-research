#!/usr/bin/env python3
"""HFK^ of the strongly invertible knot given by a kht++ half-diagram word, via spherogram + knot_floer_homology
(read-only use of the packages already installed in the Codex workspace).
usage: PYTHONPATH=<packages> python3 hfk_word.py WORD [WORD...]"""
import sys
sys.path.insert(0,'/Users/calebbarnett/jones-lanes/theory-restart/tools')
import alex
def pd_of_word(word):
    full=alex.symmetrize(alex.parse(word))
    cr=alex.diagram(full)
    if cr is None: return None
    lab={}
    def L(e):
        if e not in lab: lab[e]=len(lab)
        return lab[e]
    pd=[]
    for x in cr:
        ot,ob,ut,ub=L(x['ot']),L(x['ob']),L(x['ut']),L(x['ub'])
        if x['ty']=='x':
            # over TL-BR, under TR-BL
            if x['ud']: pd.append((ut,ot,ub,ob))
            else:       pd.append((ub,ob,ut,ot))
        else:
            # over TR-BL, under TL-BR
            if x['ud']: pd.append((ut,ob,ub,ot))
            else:       pd.append((ub,ot,ut,ob))
    return pd
if __name__=='__main__':
    import spherogram
    for w in sys.argv[1:]:
        pd=pd_of_word(w)
        print(w); print('PD',pd)
        K=spherogram.Link(pd)
        print('components',len(K.link_components),'crossings',len(K.crossings))
        try:
            print('alexander', K.alexander_polynomial())
        except Exception as e: print('alex err',e)
        h=K.knot_floer_homology()
        print({k:h[k] for k in h if k!='ranks'})
        print('ranks',sorted(h['ranks'].items()))
