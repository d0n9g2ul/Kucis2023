#!/bin/bash

result_directory="result/system"

if [ ! -d "$result_directory" ]; then
    echo "Creating directory: $result_directory"
    mkdir -p "$result_directory"
fi

top -b -n 5 > "${result_directory}/top.txt"