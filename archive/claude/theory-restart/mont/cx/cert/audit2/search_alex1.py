"""search_alex1.py SEED SECONDS OUT -- random search for PRIME-candidate Alexander-trivial halfwords (own generator).
Filter: knot, det = 1, |Delta(2)| = |Delta(3)| = |Delta(5)| = 1 (alex.alex_eval), V != 1 (own bracket)."""
import sys, time, random, json
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/audit2')
sys.path.insert(0, '/Users/calebbarnett/jones-lanes/theory-restart/tools')
import a2lib, gen, alex
seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
rng = random.Random(seed)
t_end = time.time() + secs
found = []; tried = 0; knots = 0
while time.time() < t_end:
    L = rng.randint(6, 26)
    hw = gen.rand_halfword(rng, L, maxhw=rng.choice([3, 5]), p_axis=rng.choice([0.2, 0.35, 0.5]))
    tried += 1
    d = alex.alex_eval(hw, -1)
    if d is None: continue
    knots += 1
    if d != 1: continue
    if alex.alex_eval(hw, 2) != 1 or alex.alex_eval(hw, 3) != 1 or alex.alex_eval(hw, 5) != 1: continue
    full = a2lib.full_of(hw)
    br = a2lib.bracket_full(full)
    if a2lib.jones_unit_test(br): continue
    V = a2lib.VK_from_bracket(br)
    found.append({'hw': hw, 'V': sorted(V.items()), 'n': a2lib.morse_diagram(full)['n']})
json.dump({'tried': tried, 'knots': knots, 'found': found}, open(out, 'w'))
print('tried', tried, 'knots', knots, 'found', len(found))
