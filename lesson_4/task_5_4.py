# 5. [Задача со звездочкой]:
# Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Используйте аргументы командной строки.
# Техническое задание
#
# Скрипт должен корректно обрабатывать только одну переданную ему валюту.
# Сделайте значимые сообщения пользователю о работе скрипта
# Скрипт могут запустить вообще без параметров, а могут с любым количеством параметров. Это надо учесть.
# Сделайте скриншот нескольких вызовов скрипта с разными аргументами.
# Примеры/Тесты:
#
#
# py task-4_5.py USD
#        USD: 71.7846
# py task-4_5.py FFF
#        FFF: Не найдена валюта
#
# Алгоритм
#
# Если вы хотите использовать распаковку, подумайте не будет ли ошибок.

from sys import argv
from requests import get, utils
import utils as u


response = get('http://www.cbr.ru/scripts/XML_daily.asp.')
encodings = utils.get_encoding_from_headers(response.headers)
req = response.content.decode(encoding=encodings)
print('== AUD, AZN, GBP, AMD, BYN, BGN, BRL, HUF, HKD, DKK, USD, EUR, INR, KZT, CAD, KGS, CNY ==\n'
      '== MDL, NOK, PLN, RON, XDR, SGD, TJS, TRY, TMT, UZS, UAH, CZK, SEK, CHF, ZAR, KRW, JPY ==')
curr = input('Enter currency abbreviation: ').upper()
u.currency_rates_advanced(req, curr)

print(argv)
