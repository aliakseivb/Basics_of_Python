# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в json-файл. Проверить сохранённые данные.
# Техническое задание
#
# Данные файлов синхронизированы построчно: 1-ой строке файла с ФИО соответствует 1-ая строка файла с хобби и т.п.
# При хранении данных используется принцип: одна строка — один пользователь.
# Разделитель между значениями — запятая. Не используем пакеты для парсинга CSV файлов.
# При формировании словаря хобби следует разделить символом «точка с запятой».
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО использовать
# вместо хобби None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Вы можете использовать здесь функции zip и zip_longest, но лучше обойтись без них.
# Примеры/Тесты:
#
# Фрагмент файла с данными о пользователях (task_3_users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби (task_3_hobby.csv):
#
# скалолазание,охота
# горные лыжи
#
# Фрагмент результирующего файла (task_3_rezult.txt):
#
# {'ИИИ': 'скалолазание;охота', 'ППП': 'горные лыжи'}

from os.path import join
import json

path_person = join('.', 'data_person.txt')
path_hobby = join('.', 'data_hobby.txt')

with open(file=path_person, mode='rt', encoding='utf-8') as per:
    with open(file=path_hobby, mode='rt', encoding='utf-8') as hob:
        keys = []
        my_dict = {}
        for person in per:
            key = ''
            for idx in person.split(','):
                key += idx[0]
            keys.append(key)
        hobby = [hobby.replace(',', ';').rstrip() for hobby in hob]
        if len(keys) >= len(hobby):
            for indx in range(0, len(keys)):
                if indx not in range(len(hobby)) or hobby[indx] == '':
                    my_dict[keys[indx]] = None
                else:
                    my_dict[keys[indx]] = hobby[indx]
            print(my_dict)
        else:
            for indx in range(0, len(keys)):
                my_dict[keys[indx]] = hobby[indx]
            print(my_dict)
            exit(1)
path_json = join('.', 'dict.json')
file_json = open(file=path_json, mode='wt', encoding='utf-8')
str_json = json.dump(my_dict, file_json, indent=2)
file_json.close()
with open(file=path_json, mode='rt', encoding='utf-8') as f_read:
    my_dict2 = json.load(f_read)
    print(my_dict2)