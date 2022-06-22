# [Задача со звездочкой]:
# усложненный вариант задания 1. Написать функцию num_translate_adv, которая корректно обработает
# числительные, начинающиеся с заглавной буквы. Если перевод сделать невозможно, вернуть объект None.
# Примеры/Тесты:
#
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"
#
# Техническое задание
#
# Функция возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Считаем, что только первая буква может быть заглавной.
# Обратите внимание, что функция возвращает перевод в том же регистре как и приняла.

def num_translate_adv(some_str):
    if some_str in dict_mumbers_digit:
        return f'{dict_mumbers_digit[some_str]} - {dict_mumbers[dict_mumbers_digit[some_str]]}'
    elif some_str in dict_mumbers:
        return dict_mumbers[some_str]
    elif some_str.lower() in dict_mumbers:
        return dict_mumbers[some_str.lower()].capitalize()
    else:
        return
#
#
# # dict_mumbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
# #                 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
# # dict_mumbers_digit = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
# #                       '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}
# # some_str = input('Enter a number in English in any case or numbers from 0 to 10: ')
# #
# # num_translate_adv(some_str)
# # print(num_translate_adv(some_str))
# a = 'zERo'
# indx = None
# result = ''
# count = 0
# exit_dict_numbers = ''
#
# dict_mumbers = {'zero': 'ноль'}
# if a in dict_mumbers:
#     print(dict_mumbers[a])
# else:
#     for key in dict_mumbers:
#         for lett in key:
#             for symbol in a:
#                 if lett == symbol:
#                     result += lett
#                 elif lett == symbol.lower():
#                     result += lett
#                     indx = count
#                 # if result in dict_mumbers:
#                 #     break
#             count += 1
# print(indx)
# # ниже часть программы, которая по индексу заглавной буквы введенного числительного делает заглавной
# # букву в переводе на том же индексе (делал на примере zero) и только в конце написания стало понятно,
# # что одинаковые по значению слова в англ и русском языке разные по длине, но решил код не менять, для первой
# # заглавной работать будет, как и для полносnью нижнего регистра)) - работает для dict_mumbers = {'zero': 'ноль'}
# и одной заглавной буквы - дальше запутался
# # if result in dict_mumbers:
# i = 0
# for x in dict_mumbers[result]:
#
#     if i == indx:
#         exit_dict_numbers += x.upper()
#     else:
#         exit_dict_numbers += x
#     i += 1
# print(exit_dict_numbers)

dict_mumbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
dict_mumbers_digit = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                      '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}
some_str = input('Enter a number in English in any case or numbers from 0 to 10: ')

num_translate_adv(some_str)
print(num_translate_adv(some_str))