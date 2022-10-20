#!/bin/bash

## getting the pid of target process in argument
pid=`pidof $1`

# set the sample period in ms
sampling_period=10

# call perf to get samples
sudo perf stat -B -I $sampling_period -e cycles,instructions,L1-dcache-loads  -p $pid  -o tmp.log  sleep 1

#create sub-files
cat tmp.log | grep "cache" > cache_raw.log; cat cache_raw.log | grep -v not > cache.out
cat tmp.log | grep "ins" > ipc_raw.log; cat ipc_raw.log | grep -v not > ipc.out
rm -rf *.log

