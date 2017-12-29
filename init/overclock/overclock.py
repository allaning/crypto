# This python script reads in a GPU configuration file and executes
# commands set up the GPU(s) accordingly.
#
# Platform: Ubuntu Linux 16.04 LTS
#
# Usage: python overclock.py [json_config_file]

import json
import sys

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

print("Name: " + d["name"])

print("Config:")
for config in d["config"]:
    print("GPU#: " + config["gpu_num"])
    print("  GPU Name: " + config["gpu_name"])
    print("  Memory Clock Offset: " + config["mem_clock_offset"])
    print("  GPU Clock Offset: " + config["gpu_clock_offset"])
    print("  Power Limit: " + config["power_limit"])

