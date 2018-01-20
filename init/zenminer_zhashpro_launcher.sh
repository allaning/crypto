#!/bin/bash

# Launch zecminer in a screen session named zenm (mining Zencash)

DEFAULT_DELAY=0
if [ "x$1" = "x" -o "x$1" = "xnone" ]; then
   DELAY=$DEFAULT_DELAY
else
   DELAY=$1
fi
sleep $DELAY
cd /home/allan/
su allan -c "screen -dmS zenm ./start_zenminer_zhashpro.bash"
