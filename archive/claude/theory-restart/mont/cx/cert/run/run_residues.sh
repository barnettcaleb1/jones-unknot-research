#!/bin/sh
# cert/run: certify the residues S1, S2, S3 (priority order) with the FIXED certifier, after the soundness gate passed.
PY=/Users/calebbarnett/jones-lanes/theory-restart/tools/venv/bin/python
cd /Users/calebbarnett/jones-lanes/theory-restart/mont/cx/cert/run/code
R=../out/residues
until [ -f ../out/validation/transplant.json ]; do sleep 5; done
$PY gate_check.py > $R/gate.log 2>&1 || { echo GATE_FAILED > $R/GATE_FAILED.flag; exit 1; }
for S in S1 S2 S3; do
  $PY cert_words.py $R/words_$S.json 4 $R/$S > $R/$S.log 2>&1
done
echo RESIDUES_DONE > $R/residues_done.flag
for S in S1 S2 S3; do
  $PY verify_sample.py 0.05 17 4 $R/verify5_$S.json $R/$S.jsonl.gz > $R/verify5_$S.log 2>&1
done
echo VERIFY_DONE > $R/verify_done.flag
