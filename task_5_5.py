# 5. Задан список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
# Техническое задание
#
# Здесь нет условия создавать итератор/генератор или comprehensions.
# Сохранение исходного порядка в результирующем списке обязательно.
# Не используйте Counter из модуля collections или аналогичные.
# Примеры/Тесты:
#
#
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
# Алгоритм
#
# Сначала найдите способ определить уникальность элемента в списке.
# Затем подумайте о сохранении порядка исходного списка.
# Оцените эффективность вашего алгоритма.
# Вспомните о множестве - объекте, который пройден на этом уроке, его преимуществах. Как его можно применить.

from sys import getsizeof
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# with set
start = perf_counter()
src_new = set()
some = set()
for num in src:
    if num in some:
        src_new.discard(num)
    else:
        src_new.add(num)
    some.add(num)
src_unic_compr = [numb for numb in src if numb in src_new]
print(src_unic_compr, '-->', perf_counter() - start)
print(getsizeof(src_unic_compr))

# with comprehensions
src_unic_compr1 = [num for num in src if src.count(num) == 1]
print(src_unic_compr1, '-->', perf_counter() - start)
print(getsizeof(src_unic_compr1))

# with cycle
src_new1 = []
for num in src:
    if src.count(num) == 1:
        src_new1.append(num)
print(src_new1, '-->', perf_counter() - start)
print(getsizeof(src_new1))
