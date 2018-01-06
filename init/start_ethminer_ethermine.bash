# Launches ethminer directly
# Or run ethminer_ethermine_launcher.sh to run in a screen session

export GPU_FORCE_64BIT_PTR=0
export GPU_MAX_HEAP_SIZE=100
export GPU_USE_SYNC_OBJECTS=1
export GPU_MAX_ALLOC_PERCENT=100
export GPU_SINGLE_ALLOC_PERCENT=100

# Mine Ethereum coin
# -U          For CUDA; -G for AMD; -X for combination
# -FS or -SF  Select failover server
# -RH         Report hash rate to pool
# -HWMON      Report temp and fan speed
# -v N        Set verbosity (0-9; default is 8)
cd /home/allan/
./bin/ethminer --farm-recheck 200 -U -S us2.ethermine.org:4444 -FS us1.ethermine.org:4444 -O 0xc1d3930276C4ebbd1A343D53C52774A026d4cF27.ambit1 -RH -HWMON -v 2
