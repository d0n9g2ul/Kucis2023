#!/bin/bash

directories="$1"
output_dir="result/birth_time"
result_directory="result/birth_time"

if [ ! -d "$result_directory" ]; then
    echo "Creating directory: $directory"
    mkdir "$result_directory"
fi

IFS=',' read -ra dirs <<< "$directories"



for dir in "${dirs[@]}"; do
    echo "[-]  Extract $dir [-]"
    output_file="${output_dir}/$(basename "$dir").txt"
    echo "Extract..."
    find "$dir" -type f -exec stat --format='%w %n' {} \; | sort -r > "$output_file"
done

