# list1 = [1, 2, 3, 4, 7, 12, 20, 102]
#
# lst_new = []
# for x in list1:
#     if x % 2 == 0:
#         lst_new.append(x**2)
#     else:
#         lst_new.append(str(x))
# print(lst_new)
#
# lst_new1 = [x ** 2 for x in list1 if x % 2 == 0]  # comprehensions
# lst_new1 = [x ** 2 if x % 2 == 0 else str(x) for x in list1]
# lst_new1 = (x ** 2 if x % 2 == 0 else str(x) for x in list1) # <generator object <genexpr> at 0x0000018DF4E09BD0>
#
# print(lst_new1)

# from sys import getsizeof  # измеряет размер объекта
#
# n = 100000
# lst1 = [el for el in range(n)]
# sum1 = 0
# for el in lst1:
#     sum1 += el
# # print(lst1)
# print(sum1)
# print(f'Размер списка: {getsizeof(lst1)}') # n=10-184, n=1000-9016
#
# gen1 = (el for el in range(n))  # итератор выстаскивает значение по одному, а не хранит весь список
# # print(gen1)
# # print(next(gen1), next(gen1), next(gen1), next(gen1), next(gen1), next(gen1), next(gen1), next(gen1), next(gen1), next(gen1))
# sum2 = 0
# for el in gen1:
#     sum2 += el
# print(sum2)
# print(f'Размер генератора: {getsizeof(gen1)}')  # n=10/1000 - 104
#
# while True:  # будет работать до исчерпания генератора и вывалится с ошибкой
#     el = next(gen1)
#     sum2 += el
# print(sum2)

from sys import getsizeof  # измеряет размер объекта

def gen_range (start, stop, step): # функция генератор
    rez = start
    lst = []
    while rez <= stop:
        print(f'\t\t Перед yeild')
        lst.append(rez)
        yield rez, lst # в этом месте функция запоминает свой итератор и заканчивает один проход возвращая найденное значение
        print(f'\t\t После yeild')
        rez += step

gen1 = gen_range(1, 10, 2)
for x in gen1:
    print(x)