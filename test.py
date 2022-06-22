# # # nums = ['1578.4', '892.4', '354.1', '871.5']
# # # print(sum(map(float, nums)))
# #
# # # def accepted(el):
# # #     return el.lower().startswith('i')
# #
# #
# # # products = ['iPad', 'Samsung Galaxy', 'iPhone', 'iRiver']
# # # products_sample = filter(accepted, products)
# # # print(type(products_sample)) # <class 'filter'>
# # # print(*products_sample)
# # #
# # # def box_show(w, h, unit='м', lang='ru'):
# # #     if lang == 'ru':
# # #         print(f'ширина {w} {unit}, высота {h} {unit}')
# # #     else:
# # #         print(f'width {w} {unit}, height {h} {unit}')
# # #
# # #
# # # box_show(5, 10)  # ширина 5 м, высота 10 м
# # # box_show(5, 10, 'см', lang='en')  # ширина 5 см, высота 10 см
# # #
# # # user_names = ['Иван', 'Петр', 'Ольга', 'Сергей']
# # # user_logins = ['ivan', 'petr', 'olga', 'sergey']
# # # user_roles = ['user', 'staff', 'admin', 'user']
# # # for name, login, role in zip(user_names, user_logins, user_roles):
# # #     print(f'{name}, {login}, {role}')
# # # nums = ['0', 'SamsungыGalaxy', '15.5', '18,1', 'iPhone', '748', 'HelloWord']
# # # int_nums = list(filter(str.isalpha, nums))
# # # print(int_nums)
from random import randint, randrange, choice
# #
# #
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# index = 0
# jokes_txt = []
# while index < 5:
#     index += 1
#     del_non = choice(nouns)
#     del_adv = choice(adverbs)
#     del_adj = choice(adjectives)
#     nouns = nouns.remove(del_non)
#     adverbs = adverbs.remove(del_adv)
#     adjectives = adjectives.remove(del_adj)
#     jokes_txt += [f'{del_non} {del_adv} {del_adj}']
# print(jokes_txt)
#

#
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
i = 0
while i < 5:
    i += 1
    del_non = choice(nouns)
    nouns.remove(del_non)
    print(nouns)
