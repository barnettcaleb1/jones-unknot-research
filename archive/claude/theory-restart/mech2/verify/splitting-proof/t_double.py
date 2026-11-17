from t_common import *
which = sys.argv[1] if len(sys.argv) > 1 else '31'
words = {'31': 'r1.y0.y0.y0.u1', '31m': 'r1.x0.x0.x0.u1', '41': 'l1.l2.x0.y1.x0.y1.u2.u1', 'unknot_kink': 'r1.y0.u1', 'hopfband': 'r1.y0.y0.u1'}
D = double_closure(words[which])
print('2-cable of', words[which], ':', cable2(words[which]))
R = analyse(D, 'double of ' + which, show_pairs=(which != '41'))
