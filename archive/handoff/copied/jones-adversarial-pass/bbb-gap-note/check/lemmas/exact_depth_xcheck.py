# Cross-check the truncated-series depths with exact Laurent arithmetic (depth.py helpers).
import json
src = open(__file__.replace("exact_depth_xcheck.py", "depth.py")).read().split("# ---------------- iterated commutators")[0]
src = src.split('print("Phi0 word length"')[0]
exec(src)
words = json.load(open(__file__.replace("exact_depth_xcheck.py", "odd_depth2_words.json")))
for d in ("1", "2", "3", "4", "5"):
    w = words[d]
    R = rho(4, w)
    print(f"claimed depth {d}: length {len(w)}, exact depth {depth(R)}, "
          f"identity at t=-1: {is_identity_at(R, -1)}, at t=2: {is_identity_at(R, 2)}")
