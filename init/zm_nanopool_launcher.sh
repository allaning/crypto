#!/bin/bash

# Launch dstm's Zcash miner in a screen session named zecm

DEFAULT_DELAY=0
if [ "x$1" = "x" -o "x$1" = "xnone" ]; then
   DELAY=$DEFAULT_DELAY
else
   DELAY=$1
fi
sleep $DELAY
cd /home/allan/
su allan -c "screen -dmS zecm ./start_zm_nanopool.bash"
