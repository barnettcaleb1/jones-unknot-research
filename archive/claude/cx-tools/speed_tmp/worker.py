
import sys, json, time
sys.path.insert(0, '/private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-tools')
from bracket import jones_from_pd, pclean
pd = json.load(open(sys.argv[1]))
stats = {}
t0 = time.perf_counter()
V = jones_from_pd(pd, stats=stats)
dt = time.perf_counter() - t0
print(json.dumps({"seconds": dt, "max_states": stats["max_states"], "max_width": stats["max_width"],
                  "V_is_one": pclean(V) == {0: 1}, "V_terms": len(V), "V_at_1": sum(V.values()),
                  "components": stats["components"]}))
