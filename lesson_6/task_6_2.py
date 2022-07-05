# 2. [Задача со звездочкой]: усложненный вариант задания 1. Найти IP адрес спамера
# и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Спамер — это клиент, отправивший больше всех запросов.
# Формат вывода результата:
#
# Вывести IP спамера и количество запросов от него.
# Техническое задание
#
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# У нас изначально нет никакой информации о максимальном количестве запросов. Его надо определить из лог-файла.
# Примечание:
#
# Не используйте затратные операций типа сортировки и поисков. Они здесь абсолютно избыточны.
# Для примера представьте, что более половина лог-файла - это запросы от спамера. Оцените эффективность
# вашего алгоритма в таком случае.
# Не используте сторонние модули для подсчетов, типа «count» - они вам не нужны.
# Уверены ли вы, что максимальное кол-во запросов - уникально? Т.е. найденный спамер - только один?
# Или таких спамеров может быть несколько?

from requests import get, utils
from os.path import join

url = get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(url.headers)
content = url.content.decode(encoding=encodings)
log_path = join('.', 'log_file.txt')
log_file = open(file=log_path, mode='w', encoding='utf-8')
for lines in content:
    log_file.write(lines)
log_file.close()
list_prod = []
log_file = open(file=log_path, mode='rt', encoding='utf-8')
for line in log_file:
    ip_adr = line[0:line.find('-') - 1]
    serv = line[line.find('"') + 1:line.find('/', line.find('"'))]
    prod = (line[line.find('/', line.find(serv)):line.find('HTTP') - 1])
    list_prod.append((ip_adr, serv, prod))
log_file.close()
# очень долгое вычисление (ниже), но что-то не соображу, как сделать быстрее:
# патылся с генератором - не могу понять и как следствие сделать логику
# скорее всего весь код ниже (модифицировав его) можно засунуть сразу после получения переменной ip_adr в основном коде
spamer = {i[0]: list_prod.count(i) for i in list_prod}
max_value = max(spamer.values())
out_spamer = {k: v for k, v in spamer.items() if v == max(spamer.values())}
print(out_spamer)

# реально задание поставило в тупик перезанимался что ли? честно - решение подсмотрено)


