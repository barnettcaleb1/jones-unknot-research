#!/usr/bin/env python3
"""Recompute the exact all-powers braid exclusion; Python standard library only.

Run from any directory. No data files are modified. The sibling proof notes
explain why the finite calculation certifies all integer exponent pairs.
"""
import itertools
import argparse
import json
import pathlib
import runpy
import time
import braid_all_powers as ap
import braid_kernel as bk
import tl5_block as tb

HERE=pathlib.Path(__file__).resolve().parent

def json_normalize(x):
    return json.loads(json.dumps(x))

def verify_matrix_TL_relations():
    """Ensure both matrix maps descend to the diagram Temperley--Lieb algebra."""
    I=tb.ident();delta={2:-1,-2:-1}
    e5=[tb.lincomb(({1:1},tb.rho([i])),({2:-1},I)) for i in range(1,5)]
    e4=[]
    for i in range(1,5):
        B=bk.burau([i])
        e4.append([[bk.shift(bk.add({-4*e:c for e,c in B[r][s].items()},
                                   {0:-1} if r==s else {}),2)
                    for s in range(5)] for r in range(5)])
    for generators in [e4,e5]:
        for i,E in enumerate(generators):
            assert tb.matmul(E,E)==tb.lincomb((delta,E))
            for j,F in enumerate(generators):
                if abs(i-j)==1:
                    assert tb.matmul(tb.matmul(E,F),E)==E
                elif abs(i-j)>1:
                    assert tb.matmul(E,F)==tb.matmul(F,E)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit-solver',action='store_true',
                        help='also run the general exhaustive integer-root algorithm')
    args=parser.parse_args()
    started=time.monotonic()
    bk.search.validate()
    bk.validate()
    assert bk.permutation(bk.FULL)==list(range(5))
    verify_matrix_TL_relations()
    runpy.run_path(str(HERE/'tl5_block.py'),run_name='__main__')
    ap.validate_recovery(audit_solver=args.audit_solver)
    stored=json.loads((HERE/'braid_all_powers_results.json').read_text())
    anchors=[[s*i for s,i in zip(signs,range(1,5))]
             for signs in itertools.product((-1,1),repeat=4)]
    contexts=[[]]+[[s*i] for s in (-1,1) for i in range(1,5)]
    vectors={(m,n):bk.tl_vector(bk.comm(bk.power(bk.HALF,m),bk.power(bk.FULL,n)))
             for m,n in itertools.product((1,-1),repeat=2)}
    assert stored['variants']==144 and stored['full_polynomial_evaluations']==576
    assert stored['all_integer_exponents'] and stored['hits']==[]
    assert len(stored['rows'])==144
    count=0
    for expected,(c,alpha) in zip(stored['rows'],itertools.product(contexts,anchors)):
        suffix=c+alpha+bk.inv(c)
        assert bk.search.knot(suffix,5)
        assert bk.search.jones_a(suffix,5)=={0:1}
        writhe=sum(1 if s>0 else -1 for s in alpha)
        samples={pair:bk.add(ap.deflate_A(bk.close_vector(bk.tl_vector(suffix,vec),writhe)),{0:-1})
                 for pair,vec in vectors.items()}
        coeff,den=ap.coefficients(samples)
        assert den and all(coeff)
        # CORE EXCLUSION: the shifts are m+2n, m, 2n, 0. For mn != 0
        # exactly one is largest, so equal-degree nonzero coefficients cannot
        # cancel. This covers all integer exponents without any root solver.
        assert len({max(p) for p in coeff})==1,(c,alpha)
        lead=[p[max(p)] for p in coeff]
        assert lead==[lead[0],-lead[0],-lead[0],lead[0]]
        actual=dict(context=c,anchor=alpha,coefficients=coeff,denominator=den)
        for key,value in actual.items():
            assert json_normalize(value)==expected[key],(c,alpha,key)
        if args.audit_solver:
            solution=ap.solve_integer_roots(coeff)
            assert not solution['all_pairs'] and not solution['roots'] and not solution['lines']
            assert json_normalize(solution)==expected['solution'],(c,alpha)
            count+=solution['evaluated']
    if args.audit_solver:
        assert count==576
        print('Optional integer-root audit passed: 576 exact candidate checks.')
    print('VERIFIED: 144 families; 576 exact Jones samples; all integer m,n covered.')
    print('Core proof: equal coefficient degrees give a unique leading term whenever mn != 0.')
    print('Jones=1 occurs exactly when m=0 or n=0; these are unknot closures.')
    print('This certificate does not settle Jones unknot detection for general knots.')
    print('Elapsed seconds:',round(time.monotonic()-started,3))

if __name__=='__main__':
    main()
