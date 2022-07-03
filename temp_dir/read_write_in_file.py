# открывам файл, печатаем первую строку, печатаем остальные строки,
# закрываем файл (ОБЯЗАТЕЛЬНО)
file = open("spider.txt")
print(file.readline())
print(file.read())
file.close()

# здесь файл закрывается автоматически
with open("spider.txt") as file:
    print(file.readline())

# сохраняем содержимое файла в переменную и закрываем файл
# теперь можно использовать содержимое без файла
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

# запись в файл
# "w" обозначает запись в файл без чтения
with open("spider.txt", "w") as file:
    file.write("It was dark night")
