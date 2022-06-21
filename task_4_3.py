# [Задача со звездочкой]: усложненный вариант задания 3. Написать функцию thesaurus_adv(), принимающую в
# качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи —
# первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы.
# Техническое задание
#
# Количество передаваемых строк в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# Вернуть словарь, с ключами, отсортированными в алфавитном порядке.
# Примеры/Тесты:
#
# >>> thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
#            "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
# {
#    'А':{
#           'П': ['Петр Алексеев']},
#    'И': {
#           'И': ['Илья Иванов']},
#    'С': {
#           'А': ['Алла Сидорова', 'Анна Савельева'],
#           'В': ['Василий Суриков'],
#           'И': ['Иван Сергеев', 'Инна Серова']}
# }
#  {'А':{'П': ['Петр Алексеев']}, 'И': {'И': ['Илья Иванов']}, 'С': {'А': ['Алла Сидорова', 'Анна Савельева'],'В': ['Василий Суриков'],'И': ['Иван Сергеев', 'Инна Серова']}
# }
# new_dict_1 = {}
# # dict_end = {}
# dict_sorted = {'А': ['Петр Алексеев'], 'И': ['Илья Иванов']}
# for keys in dict_sorted:
#     print(keys)
#     new_dict = {}
#     for key in dict_sorted:
#         new_dict_1 = {}
#         for i in dict_sorted[key]:
#             new_dict_1[i[0]] = i
#         new_dict[key] = new_dict_1
#     # dict_end[keys] = new_dict
#     print(new_dict)

# for key in dict_sorted.items():
# print(key)
#
# print(key[1])
#
# print((key[1][0]))
#
# print((key[1][0][0]))
# new_dict_1[key[1][0][0]] = key[1]
# print(new_dict_1)
# # key[0] - ключи нового словаря
# key[1][0][0]) - ключи подсловарей

# for tuple_in in tuple(key)[1][0]:
#     print(tuple_in)
#     for i in tuple_in:
#         print(i)
#     new_dict_1[tuple(key)[0]] = tuple(key)[1]
# new_dict.update({key: new_dict_1[tuple(key)[0]]})

def thesaurus_adv(*args):
    some_dict = {}
    for name_surname in args:
        if name_surname[name_surname.find(' ') + 1] in some_dict:
            some_dict.get(name_surname[name_surname.find(' ') + 1]).append(name_surname)
        else:
            some_dict[name_surname[name_surname.find(' ') + 1]] = [name_surname]
    dict_sorted = dict(sorted(some_dict.items()))
    new_dict = {}
    for key in dict_sorted:
        dict1 = {}
        for i in dict_sorted[key]:
            if i[0] in dict1:
                dict1.get(i[0]).append(i)
            else:
                dict1[i[0]] = [i]
            new_dict[key] = dict(sorted(dict1.items()))
    return new_dict


thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
              "Василий Суриков")

# for name_surname in some_list:
#
#     if name_surname[name_surname.find(' ') + 1] in some_dict:
#         some_dict.get(name_surname[name_surname.find(' ') + 1]).append(name_surname)
#     else:
#         some_dict[name_surname[name_surname.find(' ') + 1]] = [name_surname]
# dict_sorted = dict(sorted(some_dict.items()))
#
# for key in dict_sorted:
#     dict1 = {}
#     for i in dict_sorted[key]:
#         if i[0] in dict1:
#             dict1.get(i[0]).append(i)
#         else:
#             dict1[i[0]] = [i]
#         new_dict[key] = dict(sorted(dict1.items()))
# print(new_dict)
