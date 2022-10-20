#!/bin/bash

## getting the pid of target process in argument
pid=`pidof $1`

# set the sample period in ms
sampling_period=10

# call perf to get samples
sudo perf stat -I $sampling_period -e cycles,instructions,cache-references -p $pid  -o tmp.log sleep 1

#create sub-files

cat tmp.log | grep "cache" > cache.out
cat tmp.log | grep "ins" > ipc.out