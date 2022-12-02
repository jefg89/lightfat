#!/bin/bash

for x in {0..500}
do
    buffer_overflow/scripts/envexec.sh scripts/get_trace_of_arg.sh buffer_overflow/code/custom_app buffer_overflow/code/config.txt
    sleep 1.5
done