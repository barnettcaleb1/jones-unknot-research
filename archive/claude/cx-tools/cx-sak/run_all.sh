#!/bin/zsh
cd /private/tmp/claude-501/-Users-calebbarnett/7610ac96-4d03-4d32-b526-8a5647837809/scratchpad/cx-sak
run_one() {
  echo "START n=$1 inv=$2 $(date)"
  python3 -u run_pilot.py $1 $2 > out/pilot_n$1_inv$2.txt 2>&1
  echo "END n=$1 inv=$2 exit=$? $(date)"
  grep "VERDICT\|Traceback\|Error" out/pilot_n$1_inv$2.txt
}
# run_one 5 2 (done)
run_one 10 1
run_one 10 2
run_one 15 1
run_one 15 2
echo ALLDONE
