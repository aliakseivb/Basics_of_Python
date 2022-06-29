# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.
# Полностью истощить генератор.
# Техническое задание
#
# Отличие от задания 1 - только в использовании yield.
# Алгоритм
#
# Помните, что фукция генератор вызывается один раз, она возвращает объект-генератор и с ним дальше и работаем.

# Усложнение [одна звездочка]:
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно), для чисел,
# квадрат которых меньше 200.
#
# Усложнение [две звездочки]:
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел. Например:
#
#
# gen1 = iterator_with_yield(14)
# next(gen1)
# (1, 1)
# next(gen1)
# (3, 4)
# next(gen1)
# (5, 9)
# next(gen1)
# (7, 16)
# next(gen1)
# (9, 25)
# next(gen1)
# (11, 36)
# next(gen1)
# (13, 49)
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration
#
# def iterator_without_yield(n):
#     gen_n = (num for num in range(1, n+1, 2))
#     yield next(gen_n)
#
# rez = 0
# n = int(input('Погенерим и истощим? Введите n положительное число: '))
# gen_n = iterator_without_yield(n)
# print(rez)
# print(rez)

def iterator_yield(n):
    gen_n = (num for num in range(1, n + 1, 2))
    while True:
        yield next(gen_n)


n = int(input('Погенерим и истощим? Введите n положительное число: '))
gen_n = iterator_yield(n)


# >>> one star <<<


def iterator_yield(n):
    gen_n = (num for num in range(1, n + 1, 2))
    while True:
        for num in range(1, n + 1, 2):
            if num**2 < 200:
                yield next(gen_n)


n = int(input('Погенерим и истощим? Введите n положительное число: '))
gen_n = iterator_yield(n)


# >>> two stars <<<

def iterator_yield(n):
    gen_n = (num for num in range(1, n + 1, 2))
    sum = 0
    for num in range(1, n + 1, 2):
        if num ** 2 < 200:
            sum += num
            yield next(gen_n), sum


n = int(input('Погенерим и истощим? Введите n положительное число: '))
gen_n = iterator_yield(n)
for x in gen_n:
    print(x)