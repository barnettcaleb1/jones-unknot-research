"""Stress test of the TILT law on quotient tangles of strong inversions of two-bridge knots, using kht++.

usage: python3 tilt_2bridge.py PMIN PMAX OUT.jsonl      (run from any directory; works in lit/kht/out/tilt)
For each odd p in [PMIN,PMAX] and each EVEN q coprime to p with 0 < q < p (the generator needs an even denominator),
generate the strong inversions with `kht++ -qNAME:p/q`, then compute Khr of each quotient tangle with `kht++ -c2 -q -s FILE`
and record the rational component and the special components (label q-grading and delta) printed by the program.
"""
import subprocess, sys, re, json, os, math, glob, time
WORK = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/out/tilt'
K = '/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++'
ANSI = re.compile(r'\x1b\[[0-9;]*[A-Za-z]')
LINE = re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*?)\s{3,}(r|s)(\d*)\(([^)]*)\)\s+q\^(-?[\d/]+)\s+δ[_|]\^(-?[\d/]+)\s*$')
BNLINE = re.compile(r'^\s*\d+\)\s+h\^\s*(-?\d+)\s+q\^\s*(-?\d+)\s+δ\^\s*(-?[\d/]+)\s+(\S.*)$')
def frac(s):
    if '/' in s:
        a, b = s.split('/'); return int(a) / int(b)
    return float(int(s))
def run(args, timeout):
    try:
        r = subprocess.run([K] + args, cwd=WORK, capture_output=True, text=True, timeout=timeout, stdin=subprocess.DEVNULL)
        return ANSI.sub('', r.stdout + r.stderr)
    except subprocess.TimeoutExpired:
        return None
def main():
    pmin, pmax, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    done = set()
    if os.path.exists(out):
        for l in open(out):
            try: done.add(json.loads(l)['file'])
            except Exception: pass
    fo = open(out, 'a')
    for p in range(pmin | 1, pmax + 1, 2):
        seen = set()
        for q in range(2, p, 2):   # the generator needs an even denominator (all published examples have one)
            if math.gcd(p, q) != 1: continue
            qi = pow(q, -1, p); rep = min(q, qi) if qi % 2 == 0 else q
            if rep in seen: continue
            seen.add(rep)
            name = 'b%d_%d' % (p, q)
            pat = os.path.join(WORK, 'examples/strong_inversions/2-bridge_knots', name + '*.kht')
            if not glob.glob(pat):
                if run(['-q%s:%d/%d' % (name, p, q)], 120) is None:
                    fo.write(json.dumps({'file': name, 'p': p, 'q': q, 'error': 'generation timeout'}) + '\n'); fo.flush(); continue
            for f in sorted(glob.glob(pat)):
                rel = os.path.relpath(f, WORK)
                if rel in done: continue
                t0 = time.time()
                txt = run(['-c2', '-q', '-s', rel], 300)
                rec = {'file': rel, 'p': p, 'q': q, 'time': round(time.time() - t0, 2)}
                if txt is None:
                    rec['error'] = 'timeout'
                else:
                    comps = []; bn = []
                    for l in txt.splitlines():
                        m = LINE.match(l)
                        if m:
                            comps.append({'type': m.group(5), 'len': m.group(6), 'slope': m.group(7), 'q': frac(m.group(8)), 'delta': frac(m.group(9))})
                        else:
                            m2 = BNLINE.match(l)
                            if m2: bn.append({'h': int(m2.group(1)), 'q': int(m2.group(2)), 'delta': frac(m2.group(3)), 'cyclic': m2.group(4).rstrip().endswith(('<—', '—>', '~>', '<~'))})
                    rec['khr'] = comps; rec['bn'] = bn
                    if not comps: rec['error'] = 'no components parsed'; rec['tail'] = txt[-400:]
                fo.write(json.dumps(rec, ensure_ascii=False) + '\n'); fo.flush()
    fo.close()
if __name__ == '__main__': main()
