#!/bin/bash

result=$(./ticky_check.py syslog.log)
if test $? -eq 0; then
        files=$(ls *.csv)
        for file in $files; do
                file_name=$(basename "$file" .csv)
                ./csv_to_html.py $file /var/www/html/$file_name.html
        done
else
        echo "Fail executing the command"
fi