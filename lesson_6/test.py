# a = '57\n'
# print(len(a))
# b = 'hi'
# # a.replace(a[-1], 'hi')
# a = a.replace(a[0:2], b)
# print(a)
# print(len(a))
from os.path import join
change_path = join('.', 'bakery1.csv')
mf = open(file=change_path, mode='r+', encoding='utf-8')
mf.seek(8)
mf.write('13')
mf.close()
