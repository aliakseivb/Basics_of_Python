# 3. Написать декоратор для логирования(вывод в консоль) типов позиционных аргументов функции:
# Примеры/Тесты:
#
# def type_logger...
#     ...
#
# @type_logger
# def render_input(*args, **kwargs):
#    return 1
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# Call for: calc_cube
# 5: <class 'int'>
# Rezult: 125  type: <class 'int'>
#
# >>> render_input(1, a = 2, b = True, c = "q")
# Call for: render_input
# 1: <class 'int'>
# 'a' = 2: <class 'int'>, 'b' = True: <class 'bool'>, 'c' = q: <class 'str'>
# Rezult: 1  type: <class 'int'>
#
# Техническое задание:
#
# Если аргументов несколько - выводить данные о каждом через запятую.
# Все выводы должны быть внутри функции-обертки(декораторе)
# После того как вы «обернули»/«задекорировали» функцию убедитесь что и аргументы,
# и возвращаемое значение остались как у исходной функции.
# Усложнение:
#
# вывести тип возвращаемого значения функции
# решить задачу для именованных аргументов
# вывести имя функции


def type_var(func):
    def type_var_new(*args, **kwargs):
        print(f'Call function: {func.__name__}')
        out = func(*args, **kwargs)
        if func.__name__ == 'calc_cube':
            print(f'{out}: ', type(out))
            print(f'Rezult: {out}  type:', type(out))
        if func.__name__ == 'var_input':
            out_args = ''
            out_kwargs = ''
            rez = 'Rezult: '
            if len(kwargs) == 0 and len(args) > 0:
                for i in range(len(out[0])):
                    out_args += f'{out[0][i]}: ' + str(type(out[0][i])) + ', '
                    rez += f'{out[0][i]} type: ' + str(type(out[0][i])) + ', '
                out_args = out_args[0:len(out_args) - 2]
                rez = rez[0:len(rez) - 2]
                print(out_args)
                print(rez)
            elif len(kwargs) > 0 and len(args) == 0:
                for keys, values in out[1].items():
                    out_kwargs += f'{keys} = {values}: ' + str(type(values)) + ', '
                    rez += f'{keys} = {values}: ' + str(type(values)) + ', '
                out_kwargs = out_kwargs[0:len(out_kwargs) - 2]
                rez = rez[0:len(rez) - 2]
                print(out_kwargs)
                print(rez)
            else:
                total_rez = 'Rezult: '
                rez1 = ''
                for i in range(len(out[0])):
                    out_args += f'{out[0][i]}: ' + str(type(out[0][i])) + ', '
                    rez += f'{out[0][i]} type: ' + str(type(out[0][i])) + ', '
                rez1 = rez[0:len(rez) - 2]
                for keys, values in out[1].items():
                    out_kwargs += f'{keys} = {values}: ' + str(type(values)) + ', '
                    rez += f'{keys} = {values}: ' + str(type(values)) + ', '
                rez2 = rez[0:len(rez) - 2]
                total_rez = f'{rez1} {rez2}'
                print(total_rez)

    return type_var_new


def var_input(*args, **kwargs):
    return args, kwargs


var_input = type_var(var_input)

@type_var
def calc_cube(x):
    return x ** 3




