# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх заданных списков:
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Техническое задание
#
# Функция должна вернуть список строк-шуток.
# Функция принимает 4 параметра: количество шуток и 3 списка со словами.
# В списках nouns, adverbs, adjectives не обязательно одинакое количество элементов. Они могут быть произвольной длины.
# Проверьте работу функции для кол-ва шуток больше, чем длины списков слов и меньше.
# Сделайте вызов функции как с позиционными аргументами, так и с именованными.
# Менять исходные списки nouns, adverbs, adjectives нельзя. Это «side effects»
# Документируйте код функции.
# Примеры/Тесты:
##
# >>> get_jokes(3, nouns, adverbs, adjectives)
# ['автомобиль ночью мягкий', 'лес сегодня утопичный', 'дом вчера зеленый']
# >>> get_jokes(5, nouns, adverbs, adjectives)
# ['автомобиль вчера зеленый',
#  'дом ночью мягкий',
#  'огонь ночью утопичный',
#  'дом позавчера зеленый',
#  'город вчера утопичный']
# >>>
import random


def get_jokes(n, a, ad, count):
    jokes_txt = []
    index = 0
    while index < count:
        index += 1
        number_n = random.randint(0, len(nouns) - 1)
        number_a = random.randint(0, len(adverbs) - 1)
        number_j = random.randint(0, len(adjectives) - 1)
        jokes_txt += [f'{nouns[number_n]} {adverbs[number_a]} {adjectives[number_j]}']
    return jokes_txt


count = int(input('Enter the number of jokes you would like to receive: '))
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
get_jokes(nouns, adverbs, adjectives, count)
