# def db_connect(x):
#     return x
#
# # def db_connect_reserve(*args, **kwargs):
# #     return db_connect(*args, **kwargs) # проброс параметров во внутренню функцию
#
#
# db_connect_reserve = db_connect #  то же самое что и выше - проброс

# def main_inf(man, process):
#     family, name, surname = man.split()  # разброс множества
#     if callable(process):  # если передаваемый параметр (process) является функцией
#         return process(man)  # то пишем функцию и операцию ее вызова
#     if process == 'FIO':
#         return f'{family[0]}{name[0]}{surname[0]}'
#     elif 'Family-I-O':
#         return f'{family}-{name[0]}-{surname[0]}'
#
# def func(man):
#     family, name, surname = man.split()  # разброс множества
#     return f'{family[0]}-{name[0]}-{surname[0]}'

# # сама функция передается как объект (параметр)
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
# print(main_inf('Иванов Петр Андреевич', func))

# lst = [1, 2, 3, 4, 5, 6]
# rez = map(lambda x: x**2, lst)
# print(*rez)  # 1 4 9 16 25 36

def log_func(func):                     # \
    def new_func(*args, **kwargs):      #  \
        print('LOG-begin')              #   \
        rez = func(*args, **kwargs)     #    => декоратор
        print('LOG-end')                #   /
        return rez                      #  /
    return new_func                     # /

def old_f1(x):
    return x**2
old_f1 = log_func(old_f1) # декорация напрямую (в лоб)

@log_func                 # декорация - синтаксический "сахар"
def old_f2(x):
    return x**3

def old_f3(x): # без декорации
    return x**5
