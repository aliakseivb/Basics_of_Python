# a = range(1,4)
# print(a)
# for x in a:
#     print(x)
#
# a = input('Ввести: ')
# print(type(a))
# import time
# from itertools import cycle
# from time import sleep
# #
# color_map = ['red', 'yellow', 'green', 'yellow']
# cycler = cycle(color_map)
# while cycler:
#     print(type(next(cycler)))
#     sleep(3)
# # for k in color_map:
#     if k == 2:
#         print(color_map[k])

# from time import sleep
#
# class Auto:
# # атрибуты класса
#     auto_count = 0
#
#     def __init__(self):
#         Auto.auto_count += 1
#         print(Auto.auto_count)
# # методы класса
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1
#
# a = Auto()
# a = Auto()
# a = Auto()
# a = Auto()
# a = Auto()
# a = Auto()
# a = Auto()
# a = Auto()


# a.on_auto_start("Lexus", "RX 350L", 2019)
# print(a.auto_name)
# print(a.auto_count)
# a_2 = Auto()
# a_2.on_auto_start("Mazda", "CX 9", 2018)
# print(a_2.auto_name)
# print(a_2.auto_count)


# class TrafficLight:
#     __color_map = ['red', 'yellow', 'green', 'yellow']
#
#     def state(self, color):
#         self.__color = color
#         print(self.__color_map[int(self.__color)])
#
# tl = TrafficLight()
# # tl.state(1)  # >>> yellow
# from time import sleep
#
# __color_map = ['red', 'yellow', 'green', 'yellow']
# count = 7
# while count != 0:
#     for i in range(0,len(__color_map)):
#         if __color_map[i] == 'red':
#             print(__color_map[i])
#             sleep(7)
#         if __color_map[i] == 'yellow':
#             print(__color_map[i])
#             sleep(3)
#         if __color_map[i] == 'green':
#             print(__color_map[i])
#             sleep(5)
#     count -= 1

# def Func1():
#     var1 = 'data'
#     return var1
#
# def Func2(var1):
#     print(var1)
# Func2(Func1())
#
# # светофор с количеством итерации
#
# from time import sleep
#
#
# class TrafficLight:
#     __color_map = ['red', 'yellow', 'green', 'yellow']
#
#     def state(self, color):
#         self.__color = color
#         return self.__color
#
#     def running(self, count, t_red, t_yellow, t_green):
#         self.count = count
#         self.t_red = t_red
#         self.t_yellow = t_yellow
#         self.t_green = t_green
#         while self.count != 0:
#             for i in range(0, len(self.__color_map)):
#                 print(tl.state(self.__color_map[i]))
#                 if self.__color_map[i] == 'red':
#                     sleep(self.t_red)
#                 if self.__color_map[i] == 'yellow':
#                     sleep(self.t_yellow)
#                 if self.__color_map[i] == 'green':
#                     sleep(self.t_green)
#             self.count += -1
#
# if __name__ == '__main__':
#     while True:
#         count = input('Сколько циклов смены света пройти светофору: ')
#         time_for_color = input('Задайте количество секунд горения каждого цвета светофора \n'
#                                'в формате(535): ')  # без проверки - "we are all adults here" ))
#         try:
#             if int(count) and int(time_for_color): #  проверяем допустимость вводимых данных
#                 break
#         except ValueError:
#             print('Требуются целые числа, либо не выбрано текущее состояние светофора')
#     tl = TrafficLight()
#     tl.running(int(count), int(time_for_color[0]), int(time_for_color[1]), int(time_for_color[2]))

# __color_map = ['red', 'yellow', 'green', 'yellow']
# for i in __color_map:
#     print(i)
#
# a = '123'
# for x in a:
#     print(x)

s = 'hello world'

while len(s) > 5:
    s = s[1:]
    if len(s) > 5:
        continue
    print(s)
