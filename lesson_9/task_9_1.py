# 1. Создать класс TrafficLight (светофор).
# Техническое задание:
#
# Хорошо подумайте какие из атрибутов являются атрибутами экземпляра, а какие класса. определить у него один атрибут
# color (цвет) - приватный. Это текущий цвет светофора.
# Опредеdлить метод state (состояние), возвращающий текущий цвет в виде строки. определить метод running (запуск)
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный. продолжительность первого
# состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение
# переключение между режимами должно осуществляться как у реального светофора: красный, жёлтый, зелёный, жёлтый, красный и т.д.
# метод меняет текущий цвет светофора и печатает его с помощью state. Предусмотреть разумное ограничение на количество итераций.
# Проверить работу примера, создав экземпляр и вызвав метод running.
# Примечание:
#
# Для реализации задержек времени можно воспользоваться функцией sleep пакета time
# Циклическое переключение просто реализовать с помощью cycle пакета itertools

# СВЕТОФОР С КОЛИЧЕСТВОМ ИТЕРАЦИЙ

from time import sleep


class TrafficLight:
    __color_map = ['red', 'yellow', 'green', 'yellow']

    def state(self, color):
        self.__color = color
        return self.__color

    def running(self, count, t_red, t_yellow, t_green):
        self.count = count
        self.t_red = t_red
        self.t_yellow = t_yellow
        self.t_green = t_green
        while self.count != 0:
            for i in range(0, len(self.__color_map)):
                print(tl.state(self.__color_map[i]))
                if self.__color_map[i] == 'red':
                    sleep(self.t_red)
                if self.__color_map[i] == 'yellow':
                    sleep(self.t_yellow)
                if self.__color_map[i] == 'green':
                    sleep(self.t_green)
            self.count += -1

if __name__ == '__main__':
    while True:
        count = input('Сколько циклов смены света пройти светофору: ')
        time_for_color = input('Задайте количество секунд горения каждого цвета светофора \n'
                               'в формате(535): ')  # без проверки - "we are all adults here" ))
        try:
            if int(count) and int(time_for_color): #  проверяем допустимость вводимых данных
                break
        except ValueError:
            print('Требуются целые числа, либо не выбрано текущее состояние светофора')
    tl = TrafficLight()
    tl.running(int(count), int(time_for_color[0]), int(time_for_color[1]), int(time_for_color[2]))


# Усложнение:
#
# Тайминги передаются при создании экземпляра светофора в виде трех чисел.
# Внутри конструктора их надо соединить в единую структуру с цветами, так, чтобы было максимально понятно и лаконично.
# Ограничение на количество итераций в методе running убрать. Прерывание работы светофора реализовать
# через нажатие Crtl-C (или stop в IDE) в процессе выполнения. Найти какое исключение при этом возникает.
# Обработать его и завершить программу с выводом диагностического сообщения.

# БЕСКОНЕЧНЫЙ СВЕТОФОР И ПРЕРЫВАНИЕ
from time import sleep

class TrafficLight:
    __color_map = ['red', 'yellow', 'green', 'yellow']

    def __init__(self, t_red, t_yellow, t_green):
        self.t_red = t_red
        self.t_yellow = t_yellow
        self.t_green = t_green

    def state(self, color):
        self.__color = color

        return self.__color

    def running(self):
        try:
            while self.__color_map:
                for i in range(0, len(self.__color_map)):
                    print(tl.state(self.__color_map[i]))
                    if self.__color_map[i] == 'red':
                        sleep(self.t_red)
                    if self.__color_map[i] == 'yellow':
                        sleep(self.t_yellow)
                    if self.__color_map[i] == 'green':
                        sleep(self.t_green)
        except KeyboardInterrupt:
            print('Сами прервали!')
            exit(0)


if __name__ == '__main__':
    while True:
        time_for_color = input('Задайте количество секунд горения каждого цвета светофора \n'
                               'в формате(535): ')  # без проверки - "we are all adults here" ))
        try:
            if int(time_for_color): #  проверяем допустимость вводимых данных
                break
        except ValueError:
            print('Требуются целые числа, либо не выбрано текущее состояние светофора')
    tl = TrafficLight(int(time_for_color[0]), int(time_for_color[1]), int(time_for_color[2]))
    tl.running()

