#!/bin/bash

# Launch claymore in a screen session named ethm

DEFAULT_DELAY=0
if [ "x$1" = "x" -o "x$1" = "xnone" ]; then
   DELAY=$DEFAULT_DELAY
else
   DELAY=$1
fi
sleep $DELAY
cd /home/allan/claymore
su allan -c "screen -dmS ethm ./start.bash"
