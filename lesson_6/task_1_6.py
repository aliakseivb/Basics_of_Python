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
import os.path

from requests import get, utils
from os.path import join, isfile

url = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(url.headers)
content = url.content.decode(encoding=encodings)
log_path = join('.', 'log_file.txt')
log_path_new = join('.', 'log_file_new.txt')
log_file = open(file=log_path, mode='w+', encoding='utf-8')
log_file_new = open(file=log_path_new, mode="w", encoding='utf-8')
list_prod = []
for lines in content:
    log_file.write(lines)
log_file.close()
log_file = open(file=log_path, mode='rt', encoding='utf-8')
for line in log_file:
    mac_adr = line[0:line.find('-')-1]
    serv = line[line.find('"')+1:line.find('/', line.find('"'))]
    prod = (line[line.find('/', line.find(serv)):line.find('HTTP')-1])
    # tuple_prod = mac_adr, serv, prod
    list_prod.append((mac_adr, serv, prod))
    log_file_new.write(f'{mac_adr} - {serv} - {prod} \n')
print(list_prod)
log_file.close()
log_file_new.close()
