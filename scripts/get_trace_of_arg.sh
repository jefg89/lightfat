#!/bin/bash

## getting the pid of target process in argument
echo "Getting trace for $1, until finished"
now=$(date +"%d_%m_%Y_%H_%M")
prefix="$now"
mkdir $prefix
# set the sample period in ms
sampling_period=1

# call perf to get samples
#echo "perf stat -B -I $sampling_period -e cycles,instructions,L1-dcache-loads  -o tmp.log  $1 $2"
perf stat -B -I $sampling_period -e cycles,instructions,L1-dcache-loads  -o tmp.log  $1 $2

#create sub-files
cat tmp.log | grep "cache" > cache_raw.log; cat cache_raw.log | grep -v not > $prefix/cache.out
cat tmp.log | grep "ins" > ipc_raw.log; cat ipc_raw.log | grep -v not > $prefix/ipc.out
rm -rf *.log

python3 prep_file.py  $prefix/cache.out
python3 prep_file.py  $prefix/ipc.out
