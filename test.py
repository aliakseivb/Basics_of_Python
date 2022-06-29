# def gen_range (start, stop, step): # функция генератор
#     rez = start
#     lst = []
#     while rez <= stop:
#         # print(f'\t\t Перед yeild')
#         lst.append(rez)
#         yield rez, lst # в этом месте функция запоминает свой итератор и заканчивает один проход возвращая найденное значение
#         # print(f'\t\t После yeild')
#         rez += step
#
# gen1 = gen_range(1, 10, 2)
# for x in gen1:
#     print(x)


# short list of tutors

# def gen_tutors_groups(tutors, groups):
#     gen_tutors = (name for name in tutors)
#     gen_groups = (group for group in groups)
#     print(type(gen_tutors))
#     print(type(gen_groups))
#     for name in tutors:
#         for group in groups:
#             if name[len(tutors)-1] == next(gen_tutors) and group[len(groups)-1] != next(gen_groups):
#                 yield next(gen_tutors), None
#             elif name[len(tutors)-1] != next(gen_tutors) and group[len(groups)-1] == next(gen_groups):
#                 yield None, next(gen_groups)
#             else:
#                 yield next(gen_tutors), next(gen_groups)
#
# tutors = ['Иван', 'Анастасия', 'Петр']
# groups = ['9А', '7В', '9Б', '9В']
# gen_tutors = gen_tutors_groups(tutors, groups)
# # for gen in gen_tutors:
# #     print(gen)

# def gen_tutors_groups(tutors, groups):
#     gen_tutors = (name for name in tutors)
#     print(type(gen_tutors))
#     for classes in groups:
#         if next(gen_tutors) and classes:
#             yield next(gen_tutors), classes
#         elif next(gen_tutors) and classes != True:
#             yield next(gen_tutors), None
#         elif next(gen_tutors) != True and classes:
#             yield None, classes
#
# tutors = ['Иван', 'Анастасия', 'Петр']
# groups = ['9А', '7В']
# gen_tutors = gen_tutors_groups(tutors, groups)
# for gen in gen_tutors:
#     print(gen)
# for gen in gen_groups:
#     print(gen)


# tutors = ['Иван', 'Анастасия', 'Петр']
# groups = ['9А', '7В']
#
# count = 0
# for count
#     for name in tutors:
#         print(name)
#     for classes in groups:
#         print(classes)



