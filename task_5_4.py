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


req = get('http://www.cbr.ru/scripts/XML_daily.asp').text
if argv[1].find(' ') != -1:
    print('Not entered currency! Try next time, please')
else:
    try:
        curr = argv[1].upper()
    except IndexError:
        print('Not entered currency! Try next time, please')
    except NameError:
        print('Not entered currency! Try next time, please')

u.currency_rates_advanced(req, curr)

