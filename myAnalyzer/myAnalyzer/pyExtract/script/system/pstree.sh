#!/bin/bash

result_directory="result/system"

if [ ! -d "$result_directory" ]; then
    echo "Creating directory: $result_directory"
    mkdir -p "$result_directory"
fi

pstree -ahn > "${result_directory}/pstree.txt"