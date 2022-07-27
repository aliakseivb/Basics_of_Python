import box as item


def item_verified(obj):  # внешняя по отношению к транспорту функция проверки уникальности коробки
    is_correct_sign = obj.postcode[0] == '$' or obj.postcode[0] == '#'
    is_correct_digits = obj.postcode[1:].isdigit()
    # isinstance - проверяет тип
    is_correct_type = isinstance(obj, item.Box) or isinstance(obj, item.Barrel)
    # или  is_correct_type = isinstance(obj, item.Staffitem) - поскольку Box и Barrel производные класса Staffitem
    if is_correct_type and is_correct_sign and is_correct_digits:
        return True
    else:
        return False


class Transport:
    __horse_force = 735.49875 / 16  # watt, атрибут класса, он же будет доступен в методах экземпляра

    def __init__(self, power_engine, mass, transport_type,
                 name='underfinder', color='break',
                 body='hachback', transmission='auto'):  # метод init - конструктор-иницализатор
        self.__power_engine = power_engine * self.__horse_force  # или Car.horse_force  # получает параметры уникальные для данного экземпляра
        self.__mass = mass  # обьявление атрибута экземпляра (обязательно self)
        self._velocity = 0
        self.__tire_friction = 0.7
        self.__gas_acceler = self.__power_engine / self.__mass
        self.__break_acceler = -9.81 / self.__tire_friction
        self.__type = transport_type
        self.__box_container = []  # сюда будем пихать коробки

        self.name = name
        self.color = color
        self.body = body
        self.transmission = transmission

    def gas_pedal(self, duration):  # создание функции-метода класса Car
        print(f'Вы жали на педаль газа {duration} сек')
        rez = ''
        for time in range(duration):
            velocity = self._velocity + time * self.__gas_acceler
            rez += f'{velocity:.0f} '  # .0f убирает лишние знаки после запятой
        self._velocity = velocity
        return rez

    def break_pedal(self, duration=None):  # создание функции-метода класса Car
        print(f'Вы жали на педаль тормоза {duration} сек')
        rez = ''
        time = 0
        while True:
            time += 1
            velocity = self.velocity + time * self.__break_acceler
            if velocity <= 0:
                self.velocity = 0
                rez += f'[stop]'
                break
            if duration is not None and time >= duration:
                break
            rez += f'{velocity:.0f} '
            self.velocity = velocity
        return rez

    def speedometer(self):  # создание функции-метода класса Car
        return self.velocity

    def __str__(self):  # переопределяем для класса дандер-метод __str__ для вывода параметров машины
        return f'Тип: {self.__type}\n'\
               f'\t Двигатель: {self.__power_engine}\n'\
               f'\t Масса: {self.__mass}\n' \
               f'\t Скорость: {self._velocity}\n'\

    def container_volume(self):  # метод вернет кол-во коробок
        return len(self.__box_container)

    def __iter__(self):  # переопределяем метод, для создания итератора
        return self  # если сам объект явл итератором (то есть сам транспорт) то такая запись

    def __next__(self):  # переопределяем метод, для создания итератора
        while len(self.__box_container):
            return self.__box_container.pop()  # опорожняем транспорт от груза - исчерпываем груз
        raise StopIteration

    # подбираем оператор, а точнее дандер-метод, для сложения коробок
    # // разным логическим операторам соответствуют определенный дандер-методы (читаем, ищем)
    def __iadd__(self, other):
        if item_verified(other):  # таким образом не достучимся, потому что Box имеет приватный метод
                                 # то есть в самом классе коробка требуется геттер, который откроет доступ
            self.__box_container.append(other)  # это ничего не вернет, точнее вернет None
        return self  # а это вернет t + box - то есть возврат значения после использования метода

# class Car(Transport): pass  # class Car - наследует класс Transport, pass если ничего не переопределяем в нем
class Car(Transport):
    def __init__(self, power_engine, mass):
        super().__init__(power_engine, mass, 'car')  # явно вызвать метод __init__ класса-предка

class Truck(Transport):
    def __init__(self, power_engine, mass, velocity_limit=None):
        self.__velocity_limit = velocity_limit
        super().__init__(power_engine, mass, 'truck')

    def gas_pedal(self, duration):  # создание функции-метода класса Car
        print(f'Вы жали на педаль газа {duration} сек')
        rez = ''
        for time in range(duration):
            velocity = self.velocity + time * self.__gas_acceler
            if self.__velocity_limit is not None and velocity >= self.__velocity_limit:
                rez += f'{self.__velocity_limit} [limit]'
                break
            else:
                rez += f'{velocity:.0f} '  # .0f убирает лишние знаки после запятой
        self._velocity = velocity
        return rez

    def __str__(self): # требуется перепределить для класса truck так как есть атрибут-параметр self.__velocity_limit
        rez = super().__str__()
        return rez + f'\t Привязка скорости: {self.__velocity_limit} \n'


c = Car(320, 2600)  # создание экземпляра класса Car с опред параметрами, определенными в конструкторе init
t = Truck(500, 7000, 50)
c.gas_pedal(12)
print(c)
print(t)

b1 = item.Box()
b2 = item.Box()
b3 = item.Barrel()

for i in range(2):
    t += item.Box()
for i in range(3):
    t += item.Barrel()
# t += b1  # данная операция имеет смысл только после переопределения метода __iadd__
# print(t.container_volume())
# t += b2
# print(t.container_volume())
# t += b3
print(t.container_volume())

for obj in t:  # пробегаемся прямо по итератору t - по транспорту
    print(obj)
# while True:
#     try:
#         print(next(t))
#     except StopIteration:
#         pass
#
# print(t.container_volume())
