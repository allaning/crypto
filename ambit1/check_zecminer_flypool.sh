#!/bin/bash
# This script modified from https://www.linuxserver.io/2017/12/17/how-to-get-started-mining-crypto-on-linux-with-nvidia/
#
# To run this script via cron, enter the following to edit your cron jobs (does not need to be run as root):
# crontab -e
# Add the following line to have the script executed every 5 minutes:
# */5 * * * * /home/allan/git/allaning/crypto/ambit1/check_ethminer_ethermine.sh >/dev/null 2>&1
# After you exit from the editor, the modified crontab is checked for errors and, if there are no errors, it is installed automatically.
# The file is stored in /var/spool/cron/crontabs but should only be edited using the crontab command.


# Flag indicating whether or not we need to restart the miner
RESTART_MINER=0

LOG=/home/allan/`date +%Y%m%d_%H%M%S`_check_zecminer_flypool.log

# TODO Set the upper bound below to (Number of GPUs - 1)
for GPU in {0..1}
do
  UTIL=`nvidia-smi -i $GPU --query-gpu=utilization.gpu --format=csv,noheader | cut -f1 -d" "`
  if (($UTIL < 75)); then
    GPUINFO=`nvidia-smi -i $GPU --query-gpu=index,name,utilization.gpu,temperature.gpu --format=csv,noheader`

    # restart miner
    echo Restarting miner! GPU $GPU not optimal: $GPUINFO >> $LOG
    let RESTART_MINER=1

  else
    echo GPU $GPU is well
  fi

done


# Check if the miner needs to be restarted (or started)
# The following must be updated if any of the following change:
#      1. Not using zecminer
#      2. Not using screen

if (($RESTART_MINER == 1)); then
  echo Restarting miner! Log: $LOG
  # Kill the processes
  pkill -f "bin/miner"
  pkill -f "screen"
  # Pause
  sleep 10  # seconds
  # Restart miner
  cd /home/allan/
  screen -dmS ethm ./start_zecminer_flypool.bash
fi

