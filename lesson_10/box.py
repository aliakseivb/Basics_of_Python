from abc import ABC, abstractmethod
from random import randint


class Staffitem(ABC):  # создание абстрактного класса, который
    # предопределяет (гарантирует) что программист обязательно переопределит метод

    @abstractmethod  # декоратор - абстрактный метод
    def postcode(self):
        pass

class Box(Staffitem):
    def __init__(self):  # генерим различные коробки
        self.__postcode = '$' + str(randint(100000, 9999999))

    def __str__(self):
        return f'BOX: \t {self.__postcode}'  # переопределяем для визуализации

    @property  # декоратор, позволяющий использовать метод без (),
    # как будто вызываем функцию как атрибут (экземпляра)
    def postcode(self):
        return self.__postcode  # это возвращаемый атрибут/метод - интерфейс (о котором как правило договариваются заранее)


class Barrel(Staffitem):
    def __init__(self):
        self.__postcode = '#' + str(randint(100000, 9999999))

    def __str__(self):
        return f'BARREL: \t {self.__postcode}'

    @property  # декоратор, позволяющий использовать метод без (),
    # как будто вызываем функцию как атрибут (экземпляра)
    def postcode(self):
        return self.__postcode  # это возвращаемый атрибут/метод - интерфейс (о котором как правило договариваются заранее)


if __name__ == '__main__':
    print(Box())
    print(Box())
    print(Barrel())
    print(Barrel())
