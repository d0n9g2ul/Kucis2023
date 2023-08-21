#!/bin/bash
#directory
mkdir /home/statAnalyze

echo "extract ACCESS_TIME"
#최종 Access 시간
cd /home/statAnalyze
mkdir AccessTime
cd AccessTime

find /etc/ -type f -exec stat --format='%x %n' {} \; > Access_etc_file.txt
find /var/ -type f -exec stat --format='%x %n' {} \; > Access_var_file.txt
find /tmp/ -type f -exec stat --format='%x %n' {} \; > Access_tmp_file.txt
find /home/ -type f -exec stat --format='%x %n' {} \; > Access_home_file.txt
find /usr/ -type f -exec stat --format='%x %n' {} \; > Access_usr_file.txt
echo "extract CHANGE_TIME"

#최종 수정 시간
cd /home/statAnalyze
mkdir ChangeTime
cd ChangeTime

find /etc/ -type f -exec stat --format='%y %n' {} \; | sort -r > Change_etc_file.txt
find /var/ -type f -exec stat --format='%y %n' {} \; | sort -r > Change_var_file.txt
find /tmp/ -type f -exec stat --format='%y %n' {} \; | sort -r > Change_tmp_file.txt
find /home/ -type f -exec stat --format='%y %n' {} \; | sort -r > Change_home_file.txt
find /usr/ -type f -exec stat --format='%y %n' {} \; | sort -r > Change_usr_file.txt
echo "extract JOURNAL"

#journal 기록 가공 - Journal
cd /home/statAnalyze
mkdir journal
cd journal

journalctl | grep sudo > sudo.txt
journalctl | grep Accept > Accept_SSH.txt
journalctl | grep Failed | grep sshd > Failed_SSH.txt
journalctl | grep COMM

echo "extract last"
#last/last 기록 뽑기
cd /home/statAnalyze
mkdir last_lastb
cd last_lastb

last > last.txt
lastb > lastb.txt

echo "extract history"
#history
cd /home/statAnalyze
mkdir history
cd history

history > history.txt

echo "extract Network"
#pstree
cd /home/statAnalyze
mkdir network
cd network

pstree -ahn > pstree.txt
netstat -antp > netstat.txt

#access 추가할 것

echo "Move to shared"
cp /home/statAnalyze /mnt/hgfs

echo "DONE!!!"