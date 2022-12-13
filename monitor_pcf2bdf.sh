#!/bin/bash
app=pcf2bdf/pcf2bdf

for x in {0..23}
do
    for file in data/pcf2bdf/fonts/*
    do
        scripts/get_trace_of_arg.sh $app $file
        sleep 1.5
    done
done
