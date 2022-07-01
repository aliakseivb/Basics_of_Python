# Для всех заданий этого урока:
# Работа с файлами, доступ к элементам файла: строка, символ, цикл по строкам файла. Используйте эти инструменты для решения.
# Прикрепляя архив к ПЗ или сдавая через git, не забывайте прикреплять/загружать файлы данных, которые вы использовали.

# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Формат вывода результата:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     ...
# ]
#
# Техническое задание
#
# Не использовать библиотеки для парсинга. Только работа со строками.
# Создать список кортежей вида: `(<remote_addr>, <request_type>, <requested_resource>)`. Именно список кортежей.
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Вывести список на экран.
# Примечание:
#
# Файл логов можно загрузить отсюда: https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# В подобных структурированных файлах разделитель полей всегда очевиден.

from requests import get, utils
from sys import getsizeof


ser = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs') #.text
print(getsizeof(ser))
encodings = utils.get_encoding_from_headers(ser.headers)
content = ser.content.decode(encoding=encodings)
print(content)
print(getsizeof(content))