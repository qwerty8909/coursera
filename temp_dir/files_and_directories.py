# импорт библиотеки управления файлами
# удаление файла
import os
os.remove("spider.txt")
# переименовываем файл
os.rename("spider.txt", "new_name.txt")
# проверяем наличие файла, возвращает True или False
os.path.exists("spider.txt")
# размер файла
os.path.getsize("")
# дата изменения в секундах от 1 января 1970
os.path.getmtime("")
# перевод времени изменения в понятный вид
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)
# возвращает полный(абсолютный) путь к файлу (нужно в разных ОС)
os.path.abspath("")

# узнаем рабочий каталог
print(os.getcwd())
# содаем новый каталог
os.mkdir("new_folder")
# смена рабочего каталога на new_folder
os.chdir("new_folder")
# удаление каталога работате только с пустым каталогом
os.rmdir("new_folder")

# проверка директории на наличие файлов и директорий
import os
os.listdir("folder")
dir = "folder"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name) # работает в любой ОС
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))