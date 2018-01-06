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
   1. Create an overclock script/program (e.g. git/allaning/crypto/init/ where the .sh is a launcher of the .py script which takes a .json config file)
      * git/allaning/crypto/init/overclock.py  <-- The python script (called by overclock.sh) that configures GPU settings based on json file
      * git/allaning/crypto/init/overclock.sh  <-- Bash script that calls overclock.py passing it a hardcoded json file
      * git/allaning/crypto/ambit1/overclock_ethash.json  <-- File containing GPU settings
   1. Add overclock.sh file (or preferably a symbolic link) to the /etc/init.d/ directory
   1. Add symbolic link in /etc/rc2.d while renaming it to prepend "S##" where ## is the order of execution between the files in the rc2.d directory, e.g. name the link S99overclock.sh (if the last script to be run is rc.local and it is named S99rc.local then you need to add your script as S99myscript)
      ```
      sudo ln -s /etc/init.d/overclock.sh /etc/rc2.d/S99overclock.sh
      ```
1. Choose a mining pool and set up miner execution script (see git/allaning/crypto/init/start_ethminer_ethermine.bash)
1. Download mining software (e.g. ethminer, EWBF, etc.)
   1. Create miner launcher startup script (see git/allaning/crypto/init/ethminer_ethermine_launcher.sh, change miner path, username) to run miner execution script (e.g. start_ethminer_ethermine.bash) in a Screen session
   1. Add the launcher script to /etc/rc.local
      ```
      /home/YOUR_UBUNTU_USERNAME/ethminer_ethermine_launcher.sh 15 &
      ```
   1. Add alias to your ~/.bash_aliases file to help connect to your session when you SSH to your mining rig (i.e. when your mining rig is running, you can SSH to it and enter 'miner' to see the miner output)
      ```
      alias miner='screen -x ethm'
      ```
1. Set up cron job to check status (see git/allaning/crypto/ambit1/check_ethminer_ethermine.sh)
   ```
   crontab -e
   ```
   1. Add the following line to have cron run check_ethminer_ethermine.sh every minute or so. (After you exit from the editor, the modified crontab is checked for errors and, if there are no errors, it is installed automatically. The file is stored in /var/spool/cron/crontabs but should only be edited using the crontab command.)
      ```
      */5 * * * * /home/allan/git/allaning/crypto/ambit1/check_ethminer_ethermine.sh >/dev/null 2>&1
      ```

