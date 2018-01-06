# This python script reads in a GPU configuration file and executes
# commands set up the GPU(s) accordingly.
#
# Platform: Ubuntu Linux 16.04 LTS
#
# Usage: sudo python overclock.py [json_config_file]
#
# You can also use a helper script, e.g. overclock.sh,
# to invoke this python script with a default JSON config file.
# A symbolic link can be added to your home directory to make
# invocation easier.  E.g. use a link command such as:
# ln -s ~/git/allaning/crypto/init/overclock.sh ~/overclock.sh

import json
import os
import sys


# Execute system commands if True
EXECUTE_SYSTEM_COMMANDS = True


# Print in color
def prLightGray(message):
    print("\033[1;30m" + message + "\033[1;37m")
def prCyan(message):
    print("\033[1;36m" + message + "\033[1;37m")


def is_gpu_num_valid(num):
    """ Takes an integer and compares it to a range of valid numbers """
    MIN_GPU_NUM = 0
    MAX_GPU_NUM = 5
    if MIN_GPU_NUM <= num and num <= MAX_GPU_NUM:
        return True
    else:
        return False

def is_mem_clock_offset_valid(offset):
    """ Takes an integer and compares it to a range of valid numbers """
    MIN_MEM_OFFSET = -200
    MAX_MEM_OFFSET = 1200
    if MIN_MEM_OFFSET <= offset and offset <= MAX_MEM_OFFSET:
        return True
    else:
        return False

def is_gpu_clock_offset_valid(num):
    """ Takes an integer and compares it to a range of valid numbers """
    MIN_GPU_CLOCK_OFFSET = -100
    MAX_GPU_CLOCK_OFFSET = 200
    if MIN_GPU_CLOCK_OFFSET <= num and num <= MAX_GPU_CLOCK_OFFSET:
        return True
    else:
        return False

def is_power_limit_valid(num):
    """ Takes an integer and compares it to a range of valid numbers """
    MIN_POWER_LIMIT = 60
    MAX_POWER_LIMIT = 180
    if MIN_POWER_LIMIT <= num and num <= MAX_POWER_LIMIT:
        return True
    else:
        return False


# check if a json file was provided
if len(sys.argv) < 2:
    sys.exit("Please specify a .json file containing the GPU settings.")

input_file = sys.argv[1]

# read the file
try:
    with open(input_file, "r") as f:
        data = f.read()
except Exception as ex:
    print("Error reading file: " + str(ex))
    sys.exit()

# parse the json
d = ""
try:
    d = json.loads(data)
except Exception as ex:
    print("Error parsing file: " + str(ex))
    sys.exit()

print("")
prLightGray("Enable nvidia-smi settings so they are persistent the whole time the system is on.")
prLightGray("[exec] nvidia-smi -pm 1")
if EXECUTE_SYSTEM_COMMANDS:
    os.system("nvidia-smi -pm 1")

print("")
prLightGray("Name: " + d["name"])

for config in d["config"]:
    print("------------------------------------------------------------------------")
    prCyan("GPU#: " + config["gpu_num"])
    prCyan("  GPU Name: " + config["gpu_name"])
    prCyan("  Memory Clock Offset: " + config["mem_clock_offset"])
    prCyan("  GPU Clock Offset: " + config["graphics_clock_offset"])
    prCyan("  Power Limit: " + config["power_limit"])
    print("")

    # store the values
    gpu_num = int(config["gpu_num"])
    mem_clock_offset = int(config["mem_clock_offset"])
    graphics_clock_offset = int(config["graphics_clock_offset"])
    power_limit = int(config["power_limit"])

    if is_gpu_num_valid(gpu_num) == False:
        print("SKIPPING GPU%d: Invalid gpu_num." % (gpu_num))
        continue

    if is_mem_clock_offset_valid(mem_clock_offset) == False:
        print("SKIPPING GPU%d: Invalid mem_clock_offset: %d" % (gpu_num, mem_clock_offset))
        continue

    if is_gpu_clock_offset_valid(graphics_clock_offset) == False:
        print("SKIPPING GPU%d: Invalid graphics_clock_offset: %d" % (gpu_num, graphics_clock_offset))
        continue

    if is_power_limit_valid(power_limit) == False:
        print("SKIPPING GPU%d: Invalid power_limit: %d" % (gpu_num, power_limit))
        continue

    prLightGray("Set the power limit (note this value is in watts, not percent)")
    prLightGray("[exec] sudo nvidia-smi -i %d -pl %d" % (gpu_num, power_limit))
    if EXECUTE_SYSTEM_COMMANDS:
        os.system("sudo nvidia-smi -i " + str(gpu_num) + " -pl " + str(power_limit))

    prLightGray("Set the memory clock offset")
    prLightGray("[exec] sudo DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/:0 nvidia-settings -t -a \"[gpu:" + str(gpu_num) + "]/GPUMemoryTransferRateOffset[3]=" + str(mem_clock_offset) + "\"")
    if EXECUTE_SYSTEM_COMMANDS:
        os.system("sudo DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/:0 nvidia-settings -t -a \"[gpu:" + str(gpu_num) + "]/GPUMemoryTransferRateOffset[3]=" + str(mem_clock_offset) + "\"")

    prLightGray("Set the gpu clock offset")
    prLightGray("[exec] sudo DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/:0 nvidia-settings -t -a \"[gpu:" + str(gpu_num) + "]/GPUGraphicsClockOffset[3]=" + str(graphics_clock_offset) + "\"")
    if EXECUTE_SYSTEM_COMMANDS:
        os.system("sudo DISPLAY=:0 XAUTHORITY=/var/run/lightdm/root/:0 nvidia-settings -t -a \"[gpu:" + str(gpu_num) + "]/GPUGraphicsClockOffset[3]=" + str(graphics_clock_offset) + "\"")

print("------------------------------------------------------------------------")
print("Done.")

