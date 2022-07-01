# my_file = open(file="inf.txt", mode='at', encoding='utf-8')
# # str1 = my_file.read(35) # '1. 0912130401\n2. 1928745728\n3. 9183'
# # str1 = my_file.readline()
# # str2 = my_file.readline()
# # str2 = my_file.readlines() # ['1. 0912130401\n', '2. 1928745728\n', '3. 9183756473\n', '4. 8374682910']
# for line in my_file:
#     print(line, end="")  # печать строк, но оставление невидимых символов
#     # print(line.strip())
#
# my_file.tell(5) # переход курсора в позицию 5
# my_file.seek(35) # переход курсора в позицию 35 (отсчет от 0)
# my_file.close()
#
# my_file = open(file="inf.txt", mode='at', encoding='utf-8')
# my_file.write('new_string1\n') # запись в файл, изменения вступят в силу после my_file.close()
# my_file.write('new_string2\n') # запись в файл
# my_file.close()

# import json
#
# dict1 = {
#     1: 132,
#     2: 23.123,
#     3: 'asdasdfasdf',
#     4: 'какая-то строка'
# }
#
# myfile = open(file='file1.json', mode='wt', encoding='utf-8')
# # str_json = json.dumps(dict1)
# # myfile.write(str_json)
# str_json = json.dump(dict1, myfile, indent=2) # словарь в строку json
# myfile.close()
#
# with open(file='file1.json', mode='rt', encoding='utf-8') as file_read:
#     dict2 = json.load(file_read) # json строка обратно в словарь

import json
from os.path import join, exists, abspath, dirname, basename # join - соединение путей в один
# dirname(mpath) - вернет директорию расположения файла
# basename(mpath) - вернет имя файла
# exists - проверка существования файла
# isfile
# isdir
mpath = join('.', 'data', 'file1.json') # >>> abspath(mpath) - покажет полный путь
if exists (mpath): # проверка существования файла
    with open(file=mpath, mode='rt', encoding='utf-8') as file_read:
        dict2 = json.load(file_read) # json строка обратно в словарь
else:
    print('Файл не существует')