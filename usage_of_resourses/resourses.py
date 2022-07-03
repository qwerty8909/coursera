#!/usr/bin/env python3
import shutil
import psutil

# проверяем наличие свободного пространства на диске более 20%
def check_disk_usage (disk):
    du = shutil.disk_usage(disk)
    free = du.free/du.total*100
    return free > 20

# проверяем загрузку процессора за 1 минуту 30 секунд менее 75%
def check_cpu_usage ():
    usage = psutil.cpu_percent(1.5)
    return usage < 75

if not check_disk_usage('/') or not check_cpu_usage():
    print('ERROR')
else:
    print('Everething is OK!')
