# # n = int(input('Введите: '))
# # A = [True] * n
# # print(A)
# # A[0] = A[1] = False
# # for k in range(2, n):
# #     if A[k]:
# #         for m in range(2 * k, n, k):
# #             A[m] = False
# # for k in range(n):
# #     print(k, ' - ', 'простое' if A[k] else 'составное')
#

# A = [[1, 2, 3], [4, 55, 6], [7, 8, 119]]
# print('\n'.join(['| ' + '  '.join([str(j) for j in i]) + ' |' for i in A]))

# class MyClass:
#     def __init__(self, param):
#         self.param = param
# mc = MyClass("text")
# print(mc.param)
# print(type(mc.param))

# class MyClass:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def __add__(self, other):
#         return MyClass(self.width + other.width, self.height + other.height)
#     def __str__(self):
#         return f"Объект с параметрами ({self.width}, {self.height})"
# mc_1 = MyClass(10, 20)
# mc_2 = MyClass(30, 40)
# mc_3 = MyClass(40, 10)
# m4 = mc_1 + mc_2 + mc_3
# print(m4)

#
# class Class1:
#     def __init__(self, param):
#         self.param = param
#     def __str__(self):
#         return str(self.param)
# class Class2:
#     def __init__(self, *args):
#         self.my_list = []
#         for el in args:
#             self.my_list.append(Class1(el))
#     def __getitem__(self, index):
#         return self.my_list[index]
# my_obj = Class2(10, True, "text")
#
# print(my_obj.my_list[0])
# print(my_obj.my_list[1])
# print(my_obj[2])
# print(my_obj)

# m = [[44, 2, 3], [4, 55, 6], [7, 8, 119]]
# str_out = ''
# for i in m:
#     str_elem = '  '.join(str(j) for j in i)
#     print(str_elem)
#     # print(str_elem.center(12))
#     str_out += f'| {str_elem} | \n'
#     # str_out += '| {} |\n'.format(' '.join(str(j) for j in i))
# print(str_out)
# list1 = [[44, 2, 3], [4, 55, 6], [7, 8, 119], [1, 8, 1193]]
# len_elem = [len(str(max(i))) for i in list1]
# source = ''
# for k in range(len(list1[0])):
#     source += '{: >' + f'{len_elem[k]+2}' + '} '
# for i in list1:
#     matrix_out = f'|{source.format(*i)}|'
#     print(matrix_out)

# m1 = [[11, 2, 3], [4, 5, 6], [117, 8, 9]]
# m2 = [[1, 1, 1], [1, 11, 1], [1, 1, 1]]
# result = []
# for item in zip(m1, m2):
#     result.append([sum([j, k]) for j, k in zip(*item)])
#
# print(result)

# s = 'abc'
# print(type(s))
# t = (10, 20, 30)
# print(type(t))
#
# arr = [zip(s, t)]
# print(arr)
# print(type(arr))

