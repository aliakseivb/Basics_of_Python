# 3. [Задача со звездочкой]: усложненный вариант задания 2.
# Доработать функцию currency_rates: теперь она должна возвращать курс валюты и дату,
# которая передаётся в ответе сервера. Название новой функции currency_rates_advanced.
# Формат вывода результата:
#
# Вызовите функцию для нескольких валют, обязательно для несуществующей валюты.
# Техническое задание
#
# Все требования задания 2 остаются в силе.
# Функция должна вернуть список или кортеж, содержащий дату и курс валюты.
# Дата должна быть объектом date пакета datetime стандартной библиотеки.
# Для ее создания используйте функции пакета datetime. Если это слишком сложно - оставьте дату строкой.
# Примеры/Тесты:
#
#
# >>> url = "<http://www.cbr.ru/scripts/XML_daily.asp>"
# >>> currency_rates_advanced(url, "USd")
# ([datetime.date(2021, 10, 15)], 71.7846)
# >>> currency_rates_advanced(url, "EuR")
# ([datetime.date(2021, 10, 15)], 83.3347)
# >>> currency_rates_advanced(url, "GBP")
# ([datetime.date(2021, 10, 15)], 98.3449)
# >>> currency_rates_advanced(url, "GBP2")
# ([datetime.date(2021, 10, 15)], None)
#
# Алгоритм
#
# Посмотрите ответ сервера, как с минимальными усилиями вытащить оттуда дату?
# Подумайте можно ли, и правильно ли вызывать из этой функции функцию предыдущей задачи: currency_rates
# Если есть требования, что мы используем обе функции в своей работе, как соблюсти принцип DRY?

from requests import get
import datetime
import test as t

def currency_rates_advanced(req, curr):
    if 4 <= len(curr) < 3 or req.find(curr) == -1 or curr.isalpha() != True:
        # print('Incorrect currency abbreviation!!!  Try next time, please')
        return
    elif curr in req:
        nom = req[(req.find('Nominal', req.find(curr)) + len('Nominal') + 1):(
                req.find('Nominal', ((req.find('Nominal', req.find(curr))) + 1)) - 2)]
        price = round(float((req[(req.find('Value', req.find(curr)) + len('Value') + 1):(
                    req.find('Value', ((req.find('Value', req.find(curr))) + 1)) - 2)]).replace(',', '.')), 2)

    a = req[req.find('"', req.find('Date')) + 1: req.find('"', req.find('Date')) + 11].split('.')
    date_today = datetime.date(int(a[2]), int(a[1]), int(a[0]))
    out = [date_today], price
    print(out)


req = get('http://www.cbr.ru/scripts/XML_daily.asp').text
print('== AUD, AZN, GBP, AMD, BYN, BGN, BRL, HUF, HKD, DKK, USD, EUR, INR, KZT, CAD, KGS, CNY ==\n'
      '== MDL, NOK, PLN, RON, XDR, SGD, TJS, TRY, TMT, UZS, UAH, CZK, SEK, CHF, ZAR, KRW, JPY ==')
curr = input('Enter currency abbreviation: ').upper()
currency_rates_advanced(req, curr)

