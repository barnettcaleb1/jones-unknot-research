import re, json, sys
txt = open(sys.argv[1], encoding='utf-8').read()
blocks = re.findall(r'### VERIFY for (\w+)\n```json\n(.*?)\n```', txt, re.S)
allv = []
for lens, js in blocks:
    try:
        d = json.loads(js)
    except Exception as e:
        print('PARSE FAIL', lens, e); continue
    for i, v in enumerate(d['verdicts'], 1):
        allv.append((lens, i, v))
        print('%-8s %2d %-8s | %s' % (lens, i, v['verdict'], v['location'][:150]))
json.dump([{'lens': l, 'i': i, **v} for l, i, v in allv], open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
