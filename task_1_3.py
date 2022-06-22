# Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть объект None.
# Примеры/Тесты:
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Техническое задание
#
# Функция num_translate возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Здесь нет требований на регистр входного слова. Возвращается результат в нижнем регистре.
# Обратите внимание на глобальные и локальные объекты и на «чистоту функции»


def num_translate(some_str):
    if some_str in dict_mumbers_digit:
        return f'{dict_mumbers_digit[some_str]} - {dict_mumbers[dict_mumbers_digit[some_str]]}'
    elif some_str.lower() in dict_mumbers:
        return dict_mumbers[some_str.lower()]
    else:
        return


dict_mumbers = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
dict_mumbers_digit = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
                      '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}
some_str = input('Enter a number in English or numbers from 0 to 10: ')

num_translate(some_str)
print(num_translate(some_str))