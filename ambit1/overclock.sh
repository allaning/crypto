#!/bin/bash

# Script needs to run as sudo for nvidia-smi settings to take effect.
[ "$UID" -eq 0 ] || exec sudo bash "$0" "$@"

# Enable nvidia-smi settings so they are persistent the whole time the system is on.
nvidia-smi -pm 1


# NVIDIA GTX 1060 6GB
GPU0=0
MEM0=500
CLO0=20
PL0=90

# Set the power limit (note this value is in watts, not percent)
nvidia-smi -i ${GPU0} -pl ${PL0}
# Apply overclocking settings
sudo DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/:0 nvidia-settings -t -a "[gpu:${GPU0}]/GPUMemoryTransferRateOffset[3]=${MEM0}"
sudo DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/:0 nvidia-settings -t -a "[gpu:${GPU0}]/GPUGraphicsClockOffset[3]=${CLO0}"


# NVIDIA GTX 1070ti
GPU1=1
MEM1=600
CLO1=0
PL1=120

# Set the power limit (note this value is in watts, not percent)
sudo nvidia-smi -i ${GPU1} -pl ${PL1}
# Apply overclocking settings
# These are not working for 1070ti
sudo DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/:0 nvidia-settings -t -a "[gpu:${GPU1}]/GPUMemoryTransferRateOffset[3]=${MEM1}"
sudo DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/:0 nvidia-settings -t -a "[gpu:${GPU1}]/GPUGraphicsClockOffset[3]=${CLO1}"

