# valid_letters = {chr(sym_code) for sym_code in range(ord('а'), ord('я') + 1)}
# valid_letters.add('ё')
# def name_is_valid(name):
#     if not name or set(name.lower()) - set(valid_letters):
#         return False
#     return name.istitle()
#
# if __name__ == '__main__':
#     while True:
#         name = input('Введите имя:\n')
#         if name_is_valid(name):
#             break
# print(f'пользователь: {name}')

import re

# result = re.match(r'AVEN', 'AVEN Analytics Vidhya AVEN')
# print(result.start())
# print(result.end())
# email = 'someone@geekbrains.ru'
# if not re.search(r'(?P<username>[^\r\n\t\f\v @]+)@(?P<domain>(?:[^\r\n\t\f\v @]+)\.{1}[a-z]{2})', email):
#     print('A')
# else:
#     rez = re.search(r'(?P<username>[^\r\n\t\f\v @]+)@(?P<domain>\[^\r\n\t\f\v @]+\.{1}[a-z]{2})', email).groupdict()
#     print(rez)

#
# a = 'AV Analytics Vidhya AV'
# # result = re.search(r'(w+){6}', a)
# if not re.search(r'(w+){6}', a):
#     raise ValueError('No')

# import random
#
#
# class JobDone(Exception):
#     pass
#
#
# def nums_get(length, *args):
#     nums = []
#     try:
#         for series in args:
#             while series:
#                 random.shuffle(series)
#                 num = series.pop()
#                 if num % 2:
#                     nums.append(num)
#                 if len(nums) == length:
#                     raise JobDone
#     except JobDone:
#         return nums
#
# nums_1 = [3, 6, 8, 9, 17]
# nums_2 = [16, 22, 25]
# nums_3 = [7, 11, 18]
# print(nums_get(5, nums_1, nums_2, nums_3))
# out = re.compile(r'''(?<remote_address>(?:^(?::)(?::[0-9A-f]+){1,7})|       # \
# (?:(?:[0-9A-f]{3,4}:{1,2}){1,7}(?:[0-9A-f]+))                               #   This named group syntax is not supported in this regex dialect
# |(?:\d{1,3}\.){3}\d{1,3})                                                   #    (Этот синтаксис именованной группы не поддерживается
# .+(?<request_datetime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}\ \+\d{4})       #    в этом диалекте регулярных выражений.)
# .{3}(?<request_type>\w+)\s(?<requested_resource>\/\w+\/\w+)                 # /
# \s\w+\/\d\.\d.\s(?<response_code>\d+)\s(?<response_size>\d+)''', re.VERBOSE)

# str1 = "Привет как дела"
# a = []
# for line in str1:
#     a.append(line)
#
# print(a)
#
# a = ('88.159.11.200', '02/Jun/2015:08:06:59 +0000', 'GET', '/downloads/product_2', '200', '1768')
# for i in range(len(a)):
#     print(a[0])

# import requests
#
# res = requests.get('https://scotch.io')
#
# print(res)

# def main_inf(man, process):
#     family, name, surname = man.split()  # разброс множества
#     if callable(process):  # если передаваемый параметр (process) является функцией
#         return process(family, name, surname)  # то пишем функцию и операцию ее вызова
#     if process == 'FIO':
#         return f'{family[0]}{name[0]}{surname[0]}'
#     elif 'Family-I-O':
#         return f'{family}-{name[0]}-{surname[0]}'
#
# def func(family, name, surname):
#     return f'{family[0]}-{name[0]}-{surname[0]}'
#
# print(main_inf('Иванов Петр Андреевич', 'FIO'))  # => 'ИПА'
# print(main_inf('Иванов Петр Андреевич', 'Family-I-O'))  # => 'Иванов-П-А'
# print(main_inf('Иванов Петр Андреевич', func))  # => 'И-П-А'

# lst = [1, 2, 3, 4, 5, 6]
# rez = map(lambda x: x**2, lst)
# print(*rez)
#
# def newfunc(n):
#     def myfunc(x):
#         return x + n
#     return myfunc

# print(type(var_input(1, None, 'asd', 3.23)))
# <class 'tuple'>
# print((var_input(1, None, 'asd', 3.23))[0])
# 1
# print((var_input(1, None, 'asd', 3.23))[2])
# asd
# print((var_input(1, None, 'asd', 3.23))[1])
# None
# print(type((var_input(1, None, 'asd', 3.23))[1]))
# <class 'NoneType'>

# def typ(*args, **kwargs):
#     print(f'Call for: {typ.__name__}')
#
#     return 1
#
# # (1)
#
# dictionary = {'a':1,'b':1,'c':2}
# result = "".join(key + f' = {value}: ' + str(type(value)) + ', ' for key, value in dictionary.items())
# print(result)


# 4. [Задача с двумя звездочками]: усложненный вариант задания 3.
# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так
# Техническое задание:
# Посмотрите как реализуется декоратор с параметром в методичке - еще один уровень вложенности
# Не используйте поиск решения в сети вообще (от слова совсем) - попытайтесь разобраться по методичке что происходит.
# Переданная функция вычисляется от параметров, если True, то возвращаем результат, если False - выкидываем исключение.
# Сможете ли вы замаскировать работу декоратора?
# Примеры/Тесты:
#
# def val_checker...
#     ...
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5


# valid_letters = {chr(sym_code) for sym_code in range(ord('а'), ord('я') + 1)}
# valid_letters.add('ё')
#
#
# def name_is_valid(name):
#     if not name or set(name.lower()) - set(valid_letters):
#         return False
#     return name.istitle()
#
#
# if __name__ == '__main__':
#     while True:
#         name = input('Введите имя: \n')
#         if name_is_valid(name):
#             break
# print(f'пользователь: {name}')

import re
# RE_DATE = re.compile(r'^(\d{2}[./-]){2}\d{4}$')
# for date in ['23.01.2021', '23-01-2021', '23/01/2021']:
#     print(RE_DATE.match(date))
#     assert RE_DATE.match(date), f'wrong date {date}'
# RE_DATE = re.compile(r'(\d{2}[./-]){2}\d{4}')
# txt = 'Погода 23.01.2021 была отличная! Зато за день до этого (22/01/2021) - ' \
#       'очень холодно. ' \
#       'Надеемся, что 24-01-2021 будет без ветра.'
# print(RE_DATE.findall(txt))
# # ['23.01.2021', '22/01/2021', '24-01-2021']


# def logger(verbosity=0):
#       def _logger(func):
#             def wrapper(*args):
#                   result = func(*args)
#                   msg = f'call {func.__name__}'
#                   if verbosity > 0:
#                         msg = f'{msg}({", ".join(map(str, args))})'
#                   if verbosity > 1:
#                         msg = f'{msg} -> {result}'
#                   return msg
#             return wrapper
#       return _logger
# @logger()
# def render_input(field):
#       return f'<input id="id_{field}" type="text" name="{field}">'
#
# username_f = render_input('username')
# password_f = render_input('password')
# print(username_f)
# print(password_f)
