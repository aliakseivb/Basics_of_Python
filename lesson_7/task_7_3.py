# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates:
#
# |--my_project
# ...
# |--templates
# |   |--mainapp
# |   |  |--base.html
# |   |  |--index.html
# |   |--authapp
# |   |  |--base.html
# |   |  |--index.html
#
# Техническое задание
#
# В папках mainapp, authapp и аналогичных могут быть и другие файлы, кроме приведенных в примере.
# Папку templates надо создать внутри исходной директории, в примере - внутри my_project
# Шаблон - это папка templates в исходной структуре папок. Ее уровень в структуре папок может быть любым.
# Исходные файлы и папки необходимо оставить; обратите внимание, что html-файлы расположены в родительских
# папках (они играют роль пространств имён).
# Предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

from pathlib import Path
from shutil import copytree
# from os.path import join, abspath


path_dest = Path('.', 'task_2', 'my_project', 'templates')
path_transf = Path('.', 'task_2', 'my_project')
# dir_prj = abspath('task_2')
# path_transf = join(dir_prj, 'my_project')
# path_dest = join(dir_prj, 'my_project', 'templates')
copytree(path_transf, path_dest)


# if not path_dest.is_dir():
#     path_dest.mkdir()
# for dept in path_transf.glob('**/*.*'):
#     print(dept.parts)
#     print(dept.parts[2])
#     path_transf = Path(path_transf, dept.parts[2])
#     path_dest = templates
#     try:
#         copytree(path_transf, path_dest)
#     except FileExistsError:
#         continue
    # list_path = []
    #
    # out_path = Path(templates, str_out)
    # for val in range(0, len(dept.parts)):
    #     if val > 1:
    #
    #         str_out = str(dept.parts[2:val+1])
    #         new_path = Path(templates, str_out)
    #         if not new_path.is_dir():
    #             new_path.mkdir()

            #         list_path.append(dept.parts[val])
    #         # if str(dept.parts[val]).find('.') == -1:
    #         #     temp = Path(dept.parts[1] / 'templates'
    #         #     if not templates.is_dir():
    #         #         templates.mkdir()
    # print(tuple(list_path))
    # new_path = Path(f'{tuple(list_path)}')
    # if not new_path.exists():
    #     new_path.mkdir()
    # print(new_path)
    # print(type(new_path))

# второе решение путем посчета в цикле количества parent и добавления
