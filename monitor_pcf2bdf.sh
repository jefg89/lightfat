#!/bin/bash
app=pcf2bdf/pcf2bdf

for x in {0..200}
do
    for file in data/fonts/*
    do 
        scripts/get_trace_of_arg.sh $app $file
        sleep 1.5
    done
done
