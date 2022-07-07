#!/bin/bash
# будем менять расширение файлов .HTM на .html

for file in *.HTM; do
  name=$(basename "$file" .HTM)
  echo mv "$file" "$name.html" # echo написали чтоб проверить работу, потом удалим!
done
