#!/bin/bash

# This script will prompt for root password if not already root,
# then run the overclock.py python script with a predefined
# JSON configuration file.


# Script needs to run as sudo for nvidia-smi settings to take effect
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

# Switch to git repo
cd /home/allan/git/allaning/crypto/init/overclock

# Call with ambit1_ethash.json
python overclock.py ambit1_ethash.json

