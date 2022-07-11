# 5. [Задача со звездочкой]: усложненный вариант задания 4.
# Написать скрипт, который для заданной папки выводит статистику размеров файлов по расширениям.
# Формат вывода результата:
#
#
# {
#     100: [15, ['txt']],
#     1000: [3, ['py', 'txt']],
#     10000: [7, ['html', 'css']],
#     100000: [2, ['png', 'jpg']]
#   }
#
# Техническое задание
#
# Директорию с файлами some_data_adv можно скачать из прикрепленных к уроку файлов.
# Результат возвращается в виде словаря
# ключи — верхняя граница размера файла (пусть будет кратна 10) - как в задании 4.
# значения — списки вида [<files_quantity>, [<files_extensions_list>]].
# В список <files_extensions_list> заносятся все расширения для файлов удовлетворяющих условию размера, без повторений.
# Словарь сохраните в файл <file_name>_summary.json в той же папке, где запустили скрипт.

from pathlib import Path
import json

find_dir = Path('task_2', 'some_data_adv')
min_byte = 0
mid_byte = 0
max_byte = 0
large = 0
dict_out = {}
suf_100 = []
suf_1000 = []
suf_10000 = []
suf_large = []
for dept in find_dir.glob('**/*.*'):
    dir = Path('.', '/'.join(dept.parts))
    if dir.is_file() and dir.stat().st_size < 100:
        min_byte += 1
        suf_100.append(dir.suffix)
        set_suf_100 = set(suf_100)
        dict_out[100] = [min_byte, list(set_suf_100)]
    if dir.is_file() and 1000 > dir.stat().st_size > 200:
        mid_byte += 1
        suf_1000.append(dir.suffix)
        set_suf_1000 = set(suf_1000)
        dict_out[1000] = [mid_byte, list(set_suf_1000)]
    if dir.is_file() and 10000 > dir.stat().st_size > 1000:
        max_byte += 1
        suf_10000.append(dir.suffix)
        set_suf_10000 = set(suf_10000)
        dict_out[10000] = [max_byte, list(set_suf_10000)]
    if dir.is_file() and dir.stat().st_size > 10000:
        large += 1
        suf_large.append(dir.suffix)
        set_large = set(suf_large)
        dict_out[100000] = [large, list(set_large)]
print(dict_out)
path_json = Path('.', 'dict_out_summary.json')
file_json = open(file=path_json, mode='wt', encoding='utf-8')
str_json = json.dump(dict_out, file_json, indent=2)
file_json.close()
# for keys, values in dict_out.items():
#     print(f'{keys} -- {values[0]} --> {values[1][0:len(values[1])]}')
