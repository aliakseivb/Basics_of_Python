# 4. Написать свой модуль utils и перенести в него функцию currency_rates и currency_rates_advanced,
# если вы решали задание 2. Создать скрипт, импортировать в него модуль utils и выполнить несколько
# вызовов функции currency_rates. Убедиться, что ничего лишнего не происходит.
# Техническое задание
#
# В модуле utils не должно быть ничего лишнего, только создание функций. Если вы считает нужным
# поместить туда дополнительную инфу, например тесты - используйте конструкцию main.
# Основной скрипт импортирует модуль или требуемые функции модуля, например currency_rates и currency_rates_advanced.
# После импорта выполните вызов функций, аналогичный заданию 1 (и 2), чтобы убедиться, что все импортировалось верно.
# Примечание:
#
# Обратите внимание, что название создаваемого модуля совпадает с названием импортируемого из requests.
# Это не вызовет конфликтов.



from requests import get
import utils as u


req = get('http://www.cbr.ru/scripts/XML_daily.asp').text
print('== AUD, AZN, GBP, AMD, BYN, BGN, BRL, HUF, HKD, DKK, USD, EUR, INR, KZT, CAD, KGS, CNY ==\n'
      '== MDL, NOK, PLN, RON, XDR, SGD, TJS, TRY, TMT, UZS, UAH, CZK, SEK, CHF, ZAR, KRW, JPY ==')
curr = input('Enter currency abbreviation: ').upper()
u.currency_rates_advanced(req, curr)