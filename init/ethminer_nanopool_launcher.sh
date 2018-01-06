#!/bin/bash

# Launch ethminer in a screen session named ethm

DEFAULT_DELAY=0
if [ "x$1" = "x" -o "x$1" = "xnone" ]; then
   DELAY=$DEFAULT_DELAY
else
   DELAY=$1
fi
sleep $DELAY
cd /home/allan/
su allan -c "screen -dmS ethm ./start_ethminer_nanopool.bash"
#screen -dmS ethm ./start_ethminer_nanopool.bash
