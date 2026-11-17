#!/bin/sh
# cert/run BONUS: certify the COMPLETE sets (not only the residues) with the FIXED certifier, storing every certificate:
# S3a, S3b (never certified by the audited tool), then S1 and S2 (certified earlier by the pre-fix certify.py; re-done with
# the fixed code so that every certificate, including the jones24 words, is stored).  Then 5% fresh-process re-checks.
PY=/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/code
F=../out/full
NP=${1:-4}
until [ -f ../out/residues/verify_done.flag ]; do sleep 10; done
for S in S3a S3b S1 S2; do
  $PY cert_words.py $F/words_$S.json $NP $F/$S > $F/$S.log 2>&1
  $PY verify_sample.py 0.05 23 $NP $F/verify5_$S.json $F/$S.jsonl.gz > $F/verify5_$S.log 2>&1
done
echo FULL_DONE > $F/full_done.flag
