#!/bin/bash

result_directory="result/login"

if [ ! -d "$result_directory" ]; then
    echo "Creating directory: $result_directory"
    mkdir -p "$result_directory"
fi

echo "${result_directory}/last.txt"
last > "${result_directory}/last.txt"
lastb > "${result_directory}/lastb.txt"