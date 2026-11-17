#!/bin/zsh
cd /Users/calebbarnett/jones-lanes/theory-restart/mech2/dictionary/work
K=/Users/calebbarnett/jones-lanes/theory-restart/lit/kht/src/khtpp/kht++
for f in examples/kn/*.kht; do
  n=${f:t:r}
  if [[ -f examples/kn/$n/cxCKh-c2-s ]]; then continue; fi
  perl -e 'alarm 120; exec @ARGV' $K -c2 -s $f </dev/null >/dev/null 2>&1
  echo "$n $?"
done
