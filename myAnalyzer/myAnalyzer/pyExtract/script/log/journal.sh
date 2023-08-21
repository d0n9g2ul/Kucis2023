#!/bin/bash

result_directory="result/log"
output_dir="result/log/journal"
log_dir="result/log/journal"

if [ ! -d "$result_directory" ]; then
    echo "Creating directory: $result_directory"
    mkdir "$result_directory"
fi

if [ ! -d "$log_dir" ]; then
    echo "Creating directory: $log_dir"
    mkdir "$log_dir"
fi

echo journalctl
journalctl > journalAll.txt
echo "journal : sudo"
journalctl | grep sudo > sudo.txt
echo "journal : SSH Accept"
journalctl | grep Accept > Accept_SSH.txt
echo "journal : SSH Failed"
journalctl | grep Failed | grep sshd > Failed_SSH.txt

