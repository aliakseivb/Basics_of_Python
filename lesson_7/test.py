# from pathlib import Path
#
# templates = Path.cwd() / 'task_2' / 'my_project' / 'templates'
# if not templates.is_dir():
#     templates.mkdir()

# a = ('task_2', 'my_project', 'authapp', 'models.py')
# str_out = str(a[2:4])
# print(str_out)
# print(type(str_out))
#
# for val in range(0, len(a)):
#     if val > 1:
#         str_out = ', '.join(a[2:val + 1])
# print(str_out)

# a = ('task_2', 'some_data', 'some_data_new', 'ailsk.bin')
# for x in range(len(a)):
#     print(a[x])
# #     b = str(', '.join(a[x]))
# #     print(b)
# # print(type(b))

# from pathlib import Path
#
# find_dir = Path('task_2', 'some_data')
# min_byte = 0
# mid_byte = 0
# max_byte = 0
# large = 0
# large_plus = 0
# dict_out = {}
# for dept in find_dir.glob('**/*.*'):
#     dir = Path('.', '/'.join(dept.parts))
#     if dir.is_file() and dir.stat().st_size < 100:
#         min_byte += 1
#         dict_out[100] = min_byte
#     if dir.is_file() and 1000 > dir.stat().st_size > 100:
#         mid_byte += 1
#         dict_out[1000] = mid_byte
#     if dir.is_file() and 10000 > dir.stat().st_size > 1000:
#         max_byte += 1
#         dict_out[10000] = max_byte
#     if dir.is_file() and 50000 > dir.stat().st_size > 10000:
#         large += 1
#         dict_out[50000] = large
#     elif dir.is_file() and dir.stat().st_size > 50000:
#         large_plus += 1
#         dict_out[100000] = large_plus
# print(dict_out)
# print(dept.parts) # ('task_2', 'some_data', 'some_data_new', 'akhitnol.bin')
# print(type(dept.parts)) # tuple
# print(dir) # task_2\some_data\some_data_new\akhitnol.bin
# print(type(dir))  # <class 'pathlib.WindowsPath'>
# print(dir.absolute()) # D:\Python\Basics_of_Python\lesson_7\task_2\ some_data\ some_data_new\ akhitnol.bin
# dir.anchor # ''
# dir.as_posix() # 'task_2/ some_data/ some_data_new/ akhitnol.bin'
# 'as_uri'
# 'chmod', 'cwd', 'drive', 'exists',
# 'expanduser', 'glob', 'group', 'hardlink_to', 'home', 'is_absolute',
# 'is_block_device', 'is_char_device', 'is_dir', 'is_fifo', 'is_file',
# 'is_mount', 'is_relative_to', 'is_reserved', 'is_socket', 'is_symlink',
# 'iterdir', 'joinpath', 'lchmod', 'link_to', 'lstat', 'match', 'mkdir',
# 'name', 'open', 'owner', 'parent', 'parents', 'parts', 'read_bytes',
# 'read_text', 'readlink', 'relative_to', 'rename', 'replace', 'resolve',
# 'rglob', 'rmdir', 'root', 'samefile', 'stat', 'stem', 'suffix', 'suffixes',
# 'symlink_to', 'touch', 'unlink', 'with_name', 'with_stem', 'with_suffix', 'write_bytes', 'write_text'

list1 = [1, 2, 3, 4, 2, 3]
a = set(list1)
print(a)
a.add(44)
print(a)
a.add(3)
print(a)
print(list(a))