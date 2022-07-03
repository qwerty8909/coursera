# вытаскиваем данные из файла и формируем построчно
import csv
f = open("csv_file.txt")
csv_f = csv.reader(f) # здесь читается csv
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name,phone, role))
f.close()

# записывам данные в файл
hosts = [['pc', '192.168.1.2'], ['route', '192.168.1.1']]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts_csv)

# превращаем данные в словарь (удобно если в файле много данных и столбцы имеют имя)
with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(('{} has {} users').format(row['name'], row['users']))
        #Например: Mail has 23 users

# записываем словарь в csv
users = [{'name': 'A', 'dep': 'it'}, {'name': 'B', 'dep': 'sale'}, ...]
keys = ['name', 'dep']
with open('name_dep.csv', 'w') as name_dep:
    writer = csv.DictWriter(name_dep, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
