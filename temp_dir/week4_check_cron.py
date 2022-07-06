import subprocess

# выводит системную дату и код вывода (returncode=0)
subprocess.run(["date"])

result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result.stdout.decode().split()) # переводим в Unicode-8
print(result.returncode) # смотрим результат вывода

# ищем ошибки в лог файле, которые вызыват CRON
#!usr/bin/env python3
import re
import sys

logfile = sys.argv[1]
usermames = {} # теперь создадим словарь для подсчета количества USER
with open(logfile) as f:
    for line in f:
        # если это не CRON то искать дальше
        if 'CRON' not in line:
            continue
        # ищем USER в конце строки с параметрами и создаем группу захвата (в скобках)
        patern = r'USER \((\w+)\)$'
        result = re.search(patern, line)
        # print(line.strip()) заменили на
        # print(result[1]) теперь и это заменили на
        if result is None:
            continue
        name = result[1]
        usermames[name] = usermames.get(name, 0) + 1 # считаем
print(usermames)