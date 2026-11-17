#!/bin/bash
# run kht++ (F_2) on every component file under examples/comp, each under a time limit, stdin closed
KHT=/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++
cd /Users/calebbarnett/jones-lanes/theory-restart/mech2/verify/splitting-compute
: > run_comp.log
for f in examples/comp/*.kht; do
  b=${f%.kht}
  if [ -s "$b/cxCKh-c2" ]; then continue; fi
  s=$(date +%s)
  perl -e 'alarm 120; exec @ARGV' $KHT -c2 "$f" </dev/null > "$b.log" 2>&1
  rc=$?
  e=$(date +%s)
  echo "$f rc=$rc time=$((e-s))s" >> run_comp.log
done
echo done >> run_comp.log
