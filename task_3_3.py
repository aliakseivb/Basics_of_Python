# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имен, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.
# Техническое задание
# Количество передаваемых имен в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# Вернуть словарь с ключами, отсортированными в алфавитном порядке.
# Примеры/Тесты:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
# Алгоритм
# Вспомните как обработать произвольное количество передаваемых параметров.

# def thesaurus(*args):
#     pass
#     # for name[0] in args:
#     #     print(name)
#
#     #     for i in name:
#     #         dict1[name[i][0]] = [name[i]]
#     #         print(dict1)
#     # #     if name[0][0] in dict1:
#     #         dict1.get(name[0][0]).append(name)  # !!!! очень интересное свойство
#     #     else:
#     #         dict1[name[0][0]] = [name]
#     # dict_new = dict(sorted(dict1.items()))
#     # print(dict_new)
#     # return dict(sorted(dict1.items()))
#
# dic = {}
# some_list = "Иван", "Мария", "Петр", "Илья", "Кирилл", "Маша", "Алексей"
# for name in some_list:
#     if name[0] in dic:
#         print(name[0])
#         print(dic.get(name[0]))
#         print(type(dic.get(name[0])))
#         dic[name[0]] = dic.update({dic[name[0]]: [dic.get(name[0]).append(name)]})
#         print(dic)
#     else:
#         dic[name[0]] = [name]
# print(dic)
# # thesaurus(some_list)

def thesaurus(*args):
    dict1 = {}
    for name in args:
        if name[0] in dict1:
            dict1.get(name[0]).append(name)  # !!!! очень интересное свойство
        else:
            dict1[name[0]] = [name]
    return dict(sorted(dict1.items()))


thesaurus("Иван", "Мария", "Петр", "Илья", "Кирилл", "Маша", "Алексей", "Дмитрий", "Илья(второй)", "Костя", "Марина", "Андрей")