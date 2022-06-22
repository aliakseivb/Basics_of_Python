# 6. [Задача со звездочкой]: усложненный вариант задания 5.
# Добавьте в функцию еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках: каждое слово можно использовать только в одной шутке.
#
# Техническое задание
#
# Проверьте работу функции для разного количества шуток. Убедитесь в том, что каждое слово встречается
# только один раз.
# Примечание:
#
# Внимательно посмотрите какие из функций модуля random, упомянутые в методичке, подходят для реализации уникальности.
# Подумайте о том, сколько шуток можно вернуть при требовании уникальности, как это связано с размерами списков.

from random import randrange, choice


def get_jokes(nouns, adverbs, adjectives, count, fl):
    jokes_txt = []
    index = 0
    if fl == 0:
        while index < count:
            index += 1
            jokes_txt += [f'{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} {adjectives[randrange(len(adjectives))]}']
    else:
        while index < count:
            index += 1
            del_non = choice(nouns)
            del_adv = choice(adverbs)
            del_adj = choice(adjectives)
            nouns.remove(del_non)
            adverbs.remove(del_adv)
            adjectives.remove(del_adj)
            jokes_txt += [f'{del_non} {del_adv} {del_adj}']
    print(jokes_txt)
    return jokes_txt


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
fl = int(input('Please make a choice - can each word be used in jokes more than once (enter: 1 - no, 0 - yes): '))
if fl == 0:
    count = int(input('Enter the number of jokes you would like to receive: '))
else:
    count = int(len(nouns))
get_jokes(nouns, adverbs, adjectives, count, fl)
