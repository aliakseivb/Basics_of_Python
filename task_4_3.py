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
def thesaurus_adv():
    pass


some_dict = {}
dict_sorted = {}
new_dict = {}
some_tuple = ("Иван Сергеев", "Алла Сидорова", "Инна Серова",
              "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")

for name_surname in some_tuple:
    if name_surname[name_surname.find(' ') + 1] in some_dict:
        name_surname_plus = {some_dict.get(name_surname[name_surname.find(' ') + 1]).append(name_surname)}
    else:
        some_dict[name_surname[name_surname.find(' ') + 1]] = [name_surname]
print(some_dict)

for key in sorted(some_dict.keys()):
    print(f'\t{key}:  {some_dict[key]}')
#     new_dict += {{key}:  {some_dict[key]}}
# for key in dict:
#     if key[name_surname.find(' ') + 1] in dict:
#         name_surname_plus = {dict.get(name_surname[name_surname.find(' ') + 1]).append(name_surname)}
#     else:
#         dict[name_surname[name_surname.find(' ') + 1]] = [name_surname]
    # {'А': {'П': ['Петр Алексеев']}, 'И': {'И': ['Илья Иванов']},
    #  'С': {'А': ['Алла Сидорова', 'Анна Савельева'], 'В': ['Василий Суриков'], 'И': ['Иван Сергеев', 'Инна Серова']}
# for key in sorted(dict.keys()):
#     dict =
#     print(dict)

    # new_dict = new_dict.update({key: {dict[key]}
#     new_dict.update({key: dict[key]})
#     # for key in sorted(dict.keys()):

# dict1 = {1: 1, 2: 9, 3: 4}
# sorted_values = sorted(dict1.values()) # Sort the values
# sorted_dict = {}
#
# for i in sorted_values:
#     for k in dict1.keys():
#         if dict1[k] == i:
#             sorted_dict[k] = dict1[k]
#             break
#
# print(sorted_dict)


