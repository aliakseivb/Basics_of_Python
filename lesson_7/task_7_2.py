# 2. [Задача со звездочкой]: усложненный вариант задания
# 1. Написать скрипт, создающий из config_2.yaml стартер для проекта со следующей структурой:
#
# |--my_project
# |  |--settings
# |  |  |--__init__.py
# |  |  |--dev.py
# |  |  |--prod.py
# |  |--mainapp
# |  |  |--__init__.py
# |  |  |--models.py
# |  |  |--views.py
# |  |  |--templates
# |  |  |  |--mainapp
# |  |  |  |  |--base.html
# |  |  |  |  |--index.html
# |  |--authapp
# |  |  |--__init__.py
# |  |  |--models.py
# |  |  |--views.py
# |  |  |--templates
# |  |  |  |--authapp
# |  |  |  |  |--base.html
# |  |  |  |  |--index.html
#
# Техническое задание
#
# Пример файла config_2.yaml можно скачать из прикрепленных к уроку файлов.
# Или его можно создать в любом текстовом редакторе «руками» (не программно).
# Не используйте библиотеки для работы с YAML, проведите парсинг вручную.
# Правильный парсинг yaml - интересная задача, но может быть сложной.
# В этой задаче примем: глубина иерархии в директории определяется количеством пробелов;
# отличие директории от файла выберите сами: например в имени файла будет точка или после имени директории стоит двоеточие.
# Подумайте о возможных исключениях при работе скрипта.
# Алгоритм
#
# Чтобы распарсить YAML файл, внимательно проанализируйте его структуру: как в файле обозначен следующий уровень папок.
# Здесь надо немного повозиться с уровнями вложенности папок. Для каждой строки мы либо уходим «вглубь» и путь нарастает,
# либо возвращаемся «наверх» и надо убрать лишние элементы из пути.
# Создание файла отличается от создания директории: на Windows используйте для этого «открыть для записи и ничего не записать»,
# на linux - mknod. Помните о переносимости кода между ОС.

from os.path import join, exists, abspath
from os import mkdir

dir_prj = abspath('task_2')
start_file = join(dir_prj, 'config_2.yaml')
with open(start_file, mode='r', encoding='utf-8') as sf:
    for lines in sf:
        if lines[0].isalpha() and lines.find(':') != -1:
            path_prj = join(dir_prj, lines[0:lines.find(':')])
            if not exists(path_prj):
                mkdir(path_prj)
        if lines.find('-') != -1 and lines.find(':') != -1:
            name_dir = lines[lines.find('-') + 2:lines.find(':')]
            if lines.find('-') == 2:
                path_part_prj = join(path_prj, name_dir)
                if not exists(path_part_prj):
                    mkdir(path_part_prj)
            elif lines.find('-') == 4:
                path_part_in_prj = join(path_part_prj, name_dir)
                if not exists(path_part_in_prj):
                    mkdir(path_part_in_prj)
            else:
                path_part_end_prj = join(path_part_in_prj, name_dir)
                if not exists(path_part_end_prj):
                    mkdir(path_part_end_prj)
        if lines.find('.') != -1:
            name_file = lines[lines.find('-') + 2:-1]
            if lines.find('-') == 4:
                path_file_prj = join(path_part_prj, name_file)
                f = open(path_file_prj, 'w')
                f.close()
            else:
                path_file_end_prj = join(path_part_end_prj, name_file)
                f = open(path_file_end_prj, 'w')
                f.close()