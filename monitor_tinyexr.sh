#!/bin/bash
app=tinyexr/test_tinyexr

for x in {0..10}
do
    for file in data/tinyexr/exr/*
    do
        echo "$file"
        scripts/get_trace_of_arg.sh $app $file
        sleep 1.5
    done
done
