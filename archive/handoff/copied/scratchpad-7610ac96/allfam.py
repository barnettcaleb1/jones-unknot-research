import sys, json, random
sys.path.insert(0, '$HOME/jones-lanes/theory-restart/mont/cx/cert')
import gen_families as gf
rnd = random.Random(5); t = rnd.randrange(2, gf.P - 1)
T = sorted(set(gf.top_rehits(8, 0, t))); B = sorted(set(gf.bottom_rehits(8, 0, t)))
json.dump({'top': T, 'bottom': B}, open('$HOME/jones-lanes/theory-restart/mont/cx/cert/out/set_families_all_d8.json', 'w'))
print('top', len(T), 'bottom', len(B))
