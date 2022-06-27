# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, …) и возвращающую курс этой валюты по отношению к рублю.
# Формат вывода результата:
#
# Вызовите функцию для нескольких валют, обязательно для несуществующей валюты.
# Техническое задание
#
# Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. В каком формате
# возвращен ответ?
# Функция принимает два аргумента: строка с URL, куда стучимся и строку с кодом валюты (только одной).
# Возвращает результат числового типа, например float. Если в качестве аргумента передали код валюты, которого
# нет в ответе, вернуть объект None.
# Для извлечения данных использовать только методы объект str.
# Сделать работу функции не зависящей от того, в каком регистре был передан аргумент.
# Функция должна корректно обрабатывать любой код валюты. Правильность параметра url можно не проверять.
# Вводить коды валют с клавиатуры (input) необязательно.

from requests import get


def currency_rates(req, curr):
    if (4 <= len(curr) or len(curr) < 3) or req.find(curr) == -1 or curr.isalpha() != True or curr.find(' ') != -1:
        # print('Incorrect currency abbreviation!!!  Try next time, please')
        return
    elif curr in req:
        nom = req[(req.find('Nominal', req.find(curr)) + len('Nominal') + 1):(
                req.find('Nominal', ((req.find('Nominal', req.find(curr))) + 1)) - 2)]
        price = round(float((req[(req.find('Value', req.find(curr)) + len('Value') + 1):(
                    req.find('Value', ((req.find('Value', req.find(curr))) + 1)) - 2)]).replace(',', '.')), 2)
        out = f'курс {curr} ----> {nom} {curr} = {price} рублей'
        print(out)


req = get('http://www.cbr.ru/scripts/XML_daily.asp').text
print(
    '== AUD, AZN, GBP, AMD, BYN, BGN, BRL, HUF, HKD, DKK, USD, EUR, INR, KZT, CAD, KGS, CNY ==\n== MDL, NOK, PLN, RON, XDR, SGD, TJS, TRY, TMT, UZS, UAH, CZK, SEK, CHF, ZAR, KRW, JPY ==')
curr = input('Enter currency abbreviation: ').upper()

currency_rates(req, curr)

# print(req)
# print(type(req.text))
# print(dir(req))
# print(type(req)) # <class 'requests.models.Response'>
# print(str(req))
# print(req.encoding)
# print(req.headers)
# print(req.elapsed)
