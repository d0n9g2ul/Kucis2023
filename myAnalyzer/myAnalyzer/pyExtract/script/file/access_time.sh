#!/bin/bash

directories="$1"
output_dir="result/access_time"
result_directory="result/access_time"

if [ ! -d "$result_directory" ]; then
    echo "Creating directory: $directory"
    mkdir "$result_directory"
fi

IFS=',' read -ra dirs <<< "$directories"



for dir in "${dirs[@]}"; do
    echo "[-]  Extract $dir [-]"
    output_file="${output_dir}/$(basename "$dir").txt"
    echo "Extract..."
    find "$dir" -type f -exec stat --format='%x %n' {} \; | sort -r > "$output_file"
done
