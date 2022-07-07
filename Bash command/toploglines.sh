#!/bin/bash
# проверям 5 последних файлов в каждом логе и сортируем
for logfile in /var/log/*log ; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done