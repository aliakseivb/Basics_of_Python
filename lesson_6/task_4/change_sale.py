# 5. [Задача со звездочкой]: усложненный вариант задания 4.
# Добавить возможность редактирования данных при помощи отдельного скрипта.
# Техническое задание
#
# Скрипт получает два параметра: номер записи и новое значение
# Файл не должен считываться в память целиком. Обязательно.
# Не создавать дополнительных/«промежуточных» файлов
# Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует:
# ничего в файле не меняем, выводим сообщение в консоль.
# Алгоритм
#
# Здесь есть сложность с записью «между другими данными». Подумайте как преодолеть эту сложность.
# У вас есть требование, что одна запись - одна строка. Все остальное на ваше усмотрение.

from sys import argv
from os.path import join

if len(argv) == 1 \
        or len(argv) > 3 \
        or int(argv[1]) == 0 or argv[1].isnumeric() == False \
        or (len(argv) == 3 and argv[2].isnumeric() == False):
    print('You have entered incorrect parameters. Use: \n'
          '--> "change_sale.py x y"\n'
          '--> x - line number where we will change, y - new value')

change_path = join('.', 'bakery.csv')
with open(file=change_path, mode='r', encoding='utf-8') as mf:
    lenght = 0

    for idx, record in enumerate(mf):
        print(idx)
        lenght += len(record)
        if idx + 1 == int(argv[1]) and (len(record)-1 == len(argv[2])):
            new = record.replace(record[0:len(record)], argv[2])
            with open(file=change_path, mode='r+', encoding='utf-8') as f:
                print(f.seek(lenght - len(record)))
                f.seek(0)
                f.seek(lenght - len(record))
                f.write(new)
                exit(0)
        elif idx + 1 == int(argv[1]) and (len(record)-1 != len(argv[2])):
            print('Unequal replacement! --> use "add_sale.py"')
            exit(0)
    print(f'This line number {argv[1]} does not exist! --> add_sale.py')


        # if idx+1 == int(argv[1]) and (len(record) == len(argv[2])):
        #     new = record.replace(record[0:len(record)], argv[2])
        #     with open(file=change_path, mode='r+', encoding='utf-8') as f:
        #         f.seek(lenght - len(record))
        #         f.write(new)
        # if idx+1 == int(argv[1]) and (len(record) == len(argv[2])+1):
        #     new = record.replace(record[0:len(record)], argv[2])
        #     with open(file=change_path, mode='r+', encoding='utf-8') as f:
        #         f.seek(lenght - len(record))
        #         f.write(new)
        # if idx+1 == int(argv[1]) and (len(record) == len(argv[2])-1):
        #     new = record.replace(record[0:len(record)], argv[2])
        #     with open(file=change_path, mode='r+', encoding='utf-8') as f:
        #         f.seek(lenght - len(record))
        #         f.write(new)
        # elif (idx+1 == int(argv[1])) and (len(record) != len(argv[2])):
        #     print('Unequal replacement, use "add_sale.py"')
        # elif int(argv[1])-1 not in idx:
        #     print('This line number does not exist!')



