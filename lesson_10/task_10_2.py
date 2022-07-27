# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Формат вывода результата:
#
# Создать не менее 3 экземпляров классов с различными данными.
# Провести расчет ткани для каждого - вывести на экран
# Продемонстрировать накопительный счетчик по каждому классу.
# Техническое задание:
#
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название/имя (атрибут).
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это целые числа, например V и H, соответственно.
# Создать метод расчета ткани для каждого класса: пальто, костюм по формуле: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Выполнить общий подсчёт расхода ткани. Для всех экземпляров пальто и отдельно для всех экземпляров костюма.
# Алгоритм должен работать для любого кол-ва экземпляров.
# Проверить на практике полученные на этом уроке знания. Использовать абстрактный класс для «одежды» и наследование.
# Проверить работу декоратора @property. Не допускайте дублирования кода или спагетти-кода (кода с многочисленными проверками условий).
# Тщательно продумайте что должно быть данными (атрибутами), а что методами.
# Не принципиально будет ли накапливаться общий расход ткани определенным методом или будет скрыт внутри других методов/конструктора.
# Примеры/Тесты:
# Здесь специально не показан вывод общего количества ткани, чтобы это не было для вас избыточной подсказкой.
#
# >>> c1 = Coat(12)
# >>> c2 = Coat(1)
# >>> c3 = Coat(121)

# >>> c1.add_to_reserve
# >>> c2.add_to_reserve
# >>> c3.add_to_reserve

# Алгоритм:
#
# Исходя из условия задачи подумайте, где здесь абстрактный класс, и какие наследники.
# Какие методы следует сделать абстрактными.
# Как методами ООП реализовать «накопительный счетчик» расхода ткани для всех экземпляров пальто или костюма?

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, source):
        self.source = source

    @abstractmethod
    def require_cloth(self):
        pass

    @abstractmethod
    def sum_require_cloth(self, source):
        pass

    def __str__(self):
        return str(self.source)


    # def __add__(self, other):
    #     final_sum_require_cloth = 0
    #     final_sum_require_cloth += self.source + other.source
    #     return final_sum_require_cloth

class Coat(Clothes):

    @property
    def require_cloth(self):
        return round(self.source / 6.5 + 0.5, 1)

    def sum_require_cloth(self, source):
        self.source = source
        rez = 0
        rez += round(self.source / 6.5 + 0.5, 1)
        return rez

    # def add_to(self, other):
    #     sum_require_cloth_c = 0
    #     sum_require_cloth_c += self.source + other.source
    #     return Coat(sum_require_cloth_c)

class Jacket(Clothes):

    @property
    def require_cloth(self):
        return round(self.source * 2 + 0.3, 1)

    # def __add__(self, other):
    #     sum_require_cloth_j = 0
    #     sum_require_cloth_j += self.source + other.source
    #     return sum_require_cloth_j

if __name__ == '__main__':
    c1 = Coat(10)
    c2 = Coat(30)
    c3 = Coat(50)
    c1.sum_require_cloth(20)
    print(c1.require_cloth)
    print(c2.require_cloth)
    print(c3.require_cloth)
    print(c1.require_cloth + c2.require_cloth + c3.require_cloth)

    # j1 = Jacket(20)
    # j2 = Jacket(40)
    # print(j2)
    # print(j1.require_cloth)
    # print(j2.require_cloth)
    # print(j1.require_cloth + j2.require_cloth)
    #
    # print(c1.require_cloth + j1.require_cloth)


