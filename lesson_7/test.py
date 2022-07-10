# from pathlib import Path
#
# templates = Path.cwd() / 'task_2' / 'my_project' / 'templates'
# if not templates.is_dir():
#     templates.mkdir()

a = ('task_2', 'my_project', 'authapp', 'models.py')
str_out = str(a[2:4])
print(str_out)
print(type(str_out))

for val in range(0, len(a)):
    if val > 1:
        str_out = ', '.join(a[2:val + 1])
print(str_out)

