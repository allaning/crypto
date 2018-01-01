# crypto
Crypto related files and guides

## Overview
This repo contains setup instructions and scripts for Ubuntu 16.04 LTS running crypto currency mining software

## Features
* Power on motherboard if power was lost and is restored
* Automatically run GPU overclock script
* Autostart mining software
* Check GPU status periodically and restart miner if necessary

## Steps
1. Install Ubuntu 16.04 LTS
1. Update packages and install GNU Screen (or tmux, etc.) and other essential software
   ```
   sudo apt-get update
   sudo apt-get dist-upgrade
   sudo apt-get install screen vim
   ```
1. Install SSH:
   ```
   sudo apt-get install openssh-server
   ```
1. For NVIDIA GPUs
   1. Install libOpenCL.so
      ```
      sudo apt install ocl-icd-opencl-dev
      ```
   1. Install NVIDIA drivers
      1. Download from NVIDIA web site
      1. Change /etc/default/grub to boot to console
      1. ```sudo update-grub```
      1. When not in X server (e.g. boot to console), run the NVIDIA .run script as root
1. Power on when power applied (depends on your BIOS) by following the BIOS menu:
   ```BIOS > APM Configuration > Restore AC Power Loss > Power On```
1. Overclock the GPUs (Notes: Requires X server, so cannot boot OS only to console; Must be done as root)
   1. Confirm no errors from your GPUs
      ```
      nvidia-smi
      ```
   1. Update your /etc/X11/xorg.conf by executing (must do this every time the GPUs are changed)
      ```
      sudo nvidia-xconfig -a --cool-bits=28 --allow-empty-initial-configuration
      ```
   1. Create an overclock script (i.e. git/allaning/crypto/init/overclock/)
      * git/allaning/crypto/init/overclock/overclock.py
      * git/allaning/crypto/init/overclock/overclock.sh
      * git/allaning/crypto/init/overclock/ambit1_ethash.json
   1. Add overclock.sh file (or symbolic link) to /etc/init.d/ directory
   1. Add symbolic link in /etc/rc2.d while renaming it to prepend "S##" where ## is the order of execution between the files in the rc2.d directory, e.g. name the link S99overclock.sh (if the last script to be run is rc.local and it is named S99rc.local then you need to add your script as S99myscript)
      ```
      sudo ln -s /etc/init.d/overclock.sh /etc/rc2.d/S99overclock.sh
      ```
1. Download mining software (e.g. ethminer, EWBF, etc.)
   1. Create miner_launcher.sh startup script (change miner path, username) (see git/allaning/crypto/ambit1/)
   1. Add the startup script to /etc/rc.local
      ```
      /home/YOUR_UBUNTU_USERNAME/miner_launcher.sh 15 &
      ```
   1. Add alias to your ~/.bash_aliases file to help connect to your session when you SSH to your mining rig
      ```

