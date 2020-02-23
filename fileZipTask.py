import zipfile
import os
import shutil
import itertools
password =[]
for symbol in range(ord("a"), ord("z") + 1):
    password.append(chr(symbol))

password_list = list(itertools.product(password, repeat=3))
z = zipfile.ZipFile("C:\\Users\\Admin\\Desktop\\lesson6.zip", 'r')# обязательно указать путь к нашему архиву
print("Поиск пароля")
for i in (password_list[::-1]):
    try:
        tmp = str(i[0]+i[1]+i[2])
        z.extractall(pwd=tmp.encode("utf8"))
        real_password = i
        break
    except:
        pass
print("Пароль= "+ str(real_password))
z.printdir()
z.close()

all_files_paths = []
for d, dirs, files in os.walk('lesson6'):
    for f in files:
        path = os.path.join(d, f)
        all_files_paths.append(path)
print("Содержимое ")
print(len(all_files_paths))

if os.path.exists("folder1"):
    shutil.rmtree("folder1")

city_set = set()
dict1=dict()
os.mkdir("folder1")

for file in all_files_paths:
    f = open(file.encode("utf8"), "r", errors='ignore')
    line = f.readline()
    while line:
        city = line.split('\t')[3]
        user_id = line.split('\t')[4]
        search_keyword = line.split('\t')[5]
        if dict1.get(user_id, search_keyword)!=city:
            dict1[(user_id, search_keyword)] = city
        if city not in city_set:
            a = open("folder1\\{}.tsv".format(city), 'w')
            a.close()
            city_set.add(city)
        line = f.readline()
    f.close()
search_user_dict = dict()
for city in city_set:
    for key in dict1:
        if dict1[key] == city:
            if key[1] not in search_user_dict:
                search_user_dict[key[1]]= 1
            else:
                search_user_dict[key[1]] +=1

    a = open("folder1\\{}.tsv".format(city),'a')
    for key in search_user_dict:
        a.write(key + "\t " + str(search_user_dict.get(key)) + "\n")

    a.close()
    search_user_dict.clear()
print("Данные записаны в файлы ( каждый файл имеет названия города)")
#в итоге создается папка folder1 в PyCharm в папке с текущим проектом в которой находится список
# городов, с информацией внутри





