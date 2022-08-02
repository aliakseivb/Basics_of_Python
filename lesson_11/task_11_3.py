# 3. Создайте собственный класс-исключение, используемый для проверки содержимого списка на наличие только чисел.
# Техническое задание:
#
# Данные запрашиваются у пользователя по одному элементу.
# Длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду «stop».
# Список заполняется только числами. Для простоты ввода - целыми.
# При вводе не числа выбрасывается исключение. Оно корректно обрабатывается и ошибочные данные в список не заносятся.
# Отобразить диагностическое сообщение о неправильном вводе.
# Примечание:
#
# Вы можете написать функцию для проверки корректности введенных пользователем данных, тогда исключение должно
# выбрасываться в ней, такой вариант предпочтительнее. Но можете все делать в основной программе,
# тогда вам могут понадобиться вложенные блоки try except, а могут и не потребоваться.

class Impossible(ValueError):
    pass

# def valid_symbol(symbol):
#     try:
#
#         if not int(symbol):
#             print(False)
#             raise Impossible(f'requires only integers, not >> {symbol} <<!')
#     # except ValueError:
#     #     print(f'фффф')
#     except Impossible as err:
#         print(err)


list_symbol = []
symbol = None
while symbol != 'stop':
    symbol = input('Enter one at a time, or enter "stop": ')
    if symbol == 'stop':
        print('Your list is: ', list_symbol)
        break
    try:
        if not symbol.isdigit():
            raise Impossible(f"Requires only positive integers, not >> {symbol} <<!")
        else:
            list_symbol.append(symbol)
            print(list_symbol)
    except Impossible as err:
        print(err)

